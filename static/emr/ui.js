$(document).on("click", ".patient", async function(event) {
    event.preventDefault();
    patient_id = $(this).attr('id')
    $('.medication-emr').empty();
    const med = await getPatientId(patient_id)
    medHTML = generateMedicationHTML(med.data)
 
    processArray(med.data)

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
            <a href="/medications/${med.id}/${med.patients_id}/given">View History</a>
            <p class="card-text">${med.description} <b>Time Last Given: </b><span id="time-last-given">-</span></p>
            <a class="btn btn-primary given" data-medId=${med.id} data-ptId=${med.patients_id}>Give</a>
            </div>
        </div>

    `);
    return markUp
    })
    return marks;
}
async function giveMedAsync(p_id, m_id) {
        const l = await createGivenMedication(p_id,m_id)
        return l
}
async function processArray(array) {
    // let newArr = [];
    console.log("WORK")
    newArr = [];
    for (const item of array) {
        console.log(item.id, item.patients_id, "inside processArry")
        const plswork = await getGivenMedication(item.patients_id,item.id)
        console.log(plswork, "data i really want")
        newArr.push(plswork)
    }
    console.log(newArr);
  }


$(document).on("click", ".given", async function(event) {
    event.preventDefault();
    medication_id = $(this).attr('data-medId')
    patients_id = $(this).attr('data-ptId')
    console.log(medication_id)
    console.log(patients_id, "pts id")
    const med = await createGivenMedication(patients_id,medication_id)
    console.log(med)
    $(this).siblings('.card-text').children('#time-last-given').text(med)
});
