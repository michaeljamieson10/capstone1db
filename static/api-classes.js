async function getPatientId(patient_id) {
  const response = await axios.get(`/medications/get-current-patient/${patient_id}`)
  
  return response
};
async function getGivenMedication(patient_id, medication_id){
  const response = await axios.get(`/medications/${medication_id}/patients/${patient_id}/given`)
  return response.data
}
async function createGivenMedication(patient_id, medication_id){

  const response = await axios.post(`/medications/${medication_id}/patients/${patient_id}/given`)
  return response.data
}

async function getMedication(searchMedication){
  const response = await axios.get(`https://rxnav.nlm.nih.gov/REST/drugs.json?name=${searchMedication}`)
  return response
}
