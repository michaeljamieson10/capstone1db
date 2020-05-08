
$('.patient').click(async function(event) {
    event.preventDefault();
    console.log(access_token,"")
    patient_id = $(this).attr('id')
    $('.medication-emr').empty();
    const med = await getPatientId(patient_id)
    console.log(med.data.results)
    medHTML = generateMedicationHTML(med.data.results)
    $('.medication-emr').append(medHTML);
});

function generateMedicationHTML(medicationArray) {
 console.log(medicationArray,"inside med arry")
//     // render medication markup
   marks = medicationArray.map(function(med){
        let markUp =  $(`

        <div class="card">
            <h5 class="card-header">LOL</h5>
            <div class="card-body">
            <h5 class="card-title">Special title treatment</h5>
            <p class="card-text">${med.name}</p>
            <a href="" class="btn btn-primary">Give</a>
            </div>
        </div>

    `);
    return markUp
    })
    return marks;
}

$('#search-drug').click(async function(evt){
    evt.preventDefault()
    $searchMedication = $('#search-input').val();
    const medArray = await getMedication($searchMedication); 
    console.log(medArray.data.drugGroup, "INSIDE UI LOL")
    medSearchHTML = generateMedicationSearchHTML(medArray.data.drugGroup.conceptGroup)   
    console.log(medSearchHTML,"MEDSEARCHTML")
    $('#tbody-medications').empty()
    $('#tbody-medications').append(medSearchHTML)
})
