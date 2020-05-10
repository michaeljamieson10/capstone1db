
$('.patient').click(async function(event) {
    event.preventDefault();
    patient_id = $(this).attr('id')
    $('.medication-emr').empty();
    const med = await getPatientId(patient_id)
    medHTML = generateMedicationHTML(med.data)
    $('.medication-emr').append(medHTML);
});

function generateMedicationHTML(medicationArray) {
 console.log(medicationArray,"inside med arry")
//     // render medication markup
   marks = medicationArray.map(function(med){
       console.log(med.name)
        let markUp =  $(`

        <div class="card">
            <h3 class="card-header"></h5>
            <div class="card-body">
            <h5 class="card-title">${med.name}</h5>
            <p class="card-text">${med.description}</p>
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
