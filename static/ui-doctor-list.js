/**
 *organizes patients by first name and last name filter by
 *  database and also changes the background of the patient card to grey
 */
$(document).on("click", "th", async function(event) {
    event.preventDefault();
    const clickedClass = $(this).attr("class")
    const sortedBy = await sortByDoctors(clickedClass)
    $('.doctor-table').empty();
    console.log(sortedBy)
    const doctorHTML = generateDoctorListHTML(sortedBy);
    $('.doctor-table').append(doctorHTML)
})

/**
 * Generates patient list html for each medication of a specific patient
//  */
function generateDoctorListHTML(doctorArray) {

    marks = doctorArray.map(function(d){
       
       let markUp =  $(`
   
       <tr>
            <td>${d.last_name}</td>
            <td>${d.first_name}</td>
            <td>${d.office_phone}</td>
        </tr>
   
       `);
       return markUp
       })
       return marks;
   }
   