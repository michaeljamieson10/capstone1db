/**
 * When clicking patient this retrieves medications from
 *  database and also changes the background of the patient card to grey
 */
$(document).on("click", ".patient", async function(event) {
    event.preventDefault();
    patient_id = $(this).attr('id')
    $('.medication-emr').empty();
    const med = await getPatientId(patient_id)
    medHTML = generateMedicationHTML(med.data)
    $(this).siblings().css('background', '#ffffff')
    $(this).css('background', '#ccc'); 
    $('.medication-emr').append(medHTML);
})

/**
 * Generates medication html for each medication of a specific patient
 */
function generateMedicationHTML(medicationArray) {

 marks = medicationArray.map(function(med){

    let markUp =  $(`

        <div class="card" >
            <h3 class="card-header"></h5>
            <div class="card-body">
            <h5 class="card-title">${med.name}</h5>
            <a href="/medications/${med.id}/patients/${med.patients_id}/given">View History</a>
            <p class="card-text">${med.description}</p>
            <a class="btn btn-primary given" data-medId=${med.id} data-ptId=${med.patients_id}>Give</a>
            <span id="ifGiven"></span
            </div>
        </div>

    `);
    return markUp
    })
    return marks;
}

/**
 * This allows clicking given button and adds the 
 * medication to the given database, with time given by whom and which doctor
 */

$(document).on("click", ".given", async function(event) {
    event.preventDefault();
    medication_id = $(this).attr('data-medId')
    patients_id = $(this).attr('data-ptId')
    await createGivenMedication(patients_id,medication_id)
    $('#ifGiven').text("Given")
});

/** 
 * This is to add the active class to the navlink that has the current url
 */

$(function() {
    pathArray = location.pathname.split("/")
    pathArray.shift()
    newPath = "";
    for(x=0; x < pathArray.length; x++){
        if (x > 0){
            newPath += "/" + pathArray[x]
        }else{
            newPath += pathArray[x]
        }

    }
    $('.navbar-nav li a[href^="/' + newPath + '"]').first().addClass('active');
});
