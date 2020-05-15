async function getPatientId(patient_id) {
  const response = await axios.get(`/medications/get-current-patient/${patient_id}`)
  console.log(response.data)
  return response
};
async function getGivenMedication(patient_id, medication_id){
  const response = await axios.get(`/medications/${medication_id}/${patient_id}/given`)
  return response.data
}
async function createGivenMedication(patient_id, medication_id){

  const response = await axios.post(`/medications/${medication_id}/${patient_id}/given`)
  // console.log(response.data)
  return response.data
}

async function removeMedication(){

  // const response = await axios.delete(`/medications`)

}

async function getMedication(searchMedication){
  const response = await axios.get(`https://rxnav.nlm.nih.gov/REST/drugs.json?name=${searchMedication}`)
  return response
}
