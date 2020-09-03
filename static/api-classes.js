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

async function sortBy(header){
  const response = await axios.get(`/patients/sort/${header}`)
  return response.data
}

async function sortByDoctors(header){
  const response = await axios.get(`/doctors/sort/${header}`)
  return response.data
}
