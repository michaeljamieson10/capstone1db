$(document).ready(function(){
    $('#startModal').modal('show');
});
$(document).on('hidden.bs.modal','#startModal', function () {
    window.location = "/medications";
  });
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
    $(this).css('background', '#1168D9'); 
    $('.medication-emr').append(medHTML);
})

/**
 * Generates medication html for each medication of a specific patient
 */
function generateMedicationHTML(medicationArray) {

 marks = medicationArray.map(function(med){

    let markUp =  $(`

        <div class="card" >
            <h3 class="card-header p-3"></h5>
            <div class="card-body">
            <h5 class="card-title">${med.name}</h5>
            <a href="/medications/${med.id}/patients/${med.patients_id}/given">View History</a>
            <p class="card-text">${med.description}</p>
            <a class="btn btn-primary given" data-medName=${med.name} data-medId=${med.id} data-ptId=${med.patients_id}>Give</a>
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
    console.log("this buttonw orks")
    medication_id = $(this).attr('data-medId');
    patients_id = $(this).attr('data-ptId');
    medication_name = $(this).attr('data-medName');
    await createGivenMedication(patients_id,medication_id);
    $('.medication-emr').prepend(`<div id="given_${medication_id}"class="alert alert-success" role="alert">${medication_name} was given</div>`)
    let given_med = $(`#given_${medication_id}`)
    setTimeout(function(){
        given_med.fadeOut('slow')
    },3000)
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
