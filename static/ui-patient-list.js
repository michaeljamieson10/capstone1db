/**
 *organizes patients by first name and last name filter by
 *  database and also changes the background of the patient card to grey
 */
$(document).on("click", "th", async function(event) {
    event.preventDefault();
    const clickedClass = $(this).attr("class")
    const sortedBy = await sortBy(clickedClass)
    $('.patient-table').empty();
    const patientHTML = generatePatientListHTML(sortedBy);
    $('.patient-table').append(patientHTML)
})

/**
 * Generates patient list html for each medication of a specific patient
//  */
function generatePatientListHTML(patientArray) {

    marks = patientArray.map(function(pt){
       
       let markUp =  $(`
   
       <tr>
            <td><a href="/patients/${pt.id}">${pt.id}</a></td>
            <td>${pt.last_name}</td>
            <td>${pt.first_name}</td>
            <td>${pt.date_of_birth}</td>
        </tr>
   
       `);
       return markUp
       })
       return marks;
   }
   