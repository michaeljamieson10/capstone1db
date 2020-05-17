$(document).on("click", ".patient", async function(event) {
    event.preventDefault();
    patient_id = $(this).attr('id')
    $('.medication-emr').empty();
    const med = await getPatientId(patient_id)
    medHTML = generateMedicationHTML(med.data)
 

    $('.medication-emr').append(medHTML);
})


function generateMedicationHTML(medicationArray) {

 marks = medicationArray.map(function(med){
// /medications/<int:medication_id>/<int:patient_id>/given
    let markUp =  $(`

        <div class="card" >
            <h3 class="card-header"></h5>
            <div class="card-body">
            <h5 class="card-title">${med.name}</h5>
            <a href="/medications/${med.id}/patients/${med.patients_id}/given">View History</a>
            <p class="card-text">${med.description}</p>
            <a class="btn btn-primary given" data-medId=${med.id} data-ptId=${med.patients_id}>Give</a>
            </div>
        </div>

    `);
    return markUp
    })
    return marks;
}



$(document).on("click", ".given", async function(event) {
    event.preventDefault();
    medication_id = $(this).attr('data-medId')
    patients_id = $(this).attr('data-ptId')
    await createGivenMedication(patients_id,medication_id)
});
