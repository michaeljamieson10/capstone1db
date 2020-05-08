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
function generateMedicationSearchHTML(medArray) {
    console.log(medArray,"inside med arry")
   //     // render medication markup
      marks = medArray.map(function(med){
          if(med.conceptProperties){
              return med.conceptProperties.map(function(x){
                  return x.name

                })
          }else{return null}
        })  
    var merged = [].concat.apply([], marks);
    console.log(merged)
 
    function sortByLength (array) {
        return array.sort((x,y) => x.length - y.length);
     }
    merged = merged.map(function(med_names){
        if(med_names != null){
            return med_names            
        }  
    }) 
    console.log(merged, "new merger")
    merged = sortByLength(merged)
    return merged.map(function(med_names){
        if(med_names != null){
            console.log(med_names, "what ur looking for")
            markUp = $(`
                <tr>
                    <td>
                    <p>${med_names}</p>
                    <a href="/medications-add/${med_names}" class="btn btn-primary">Add medication to patient</a>
                    </td>
                </tr>

            `)
            return markUp
        }
        }
    
    )
   
   }