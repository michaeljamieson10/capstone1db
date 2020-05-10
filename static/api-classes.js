async function getPatientId(patient_id) {
  const response = await axios.get(`/medications/get-current-patient/${patient_id}`)
  console.log(response.data)
  return response
};

async function getMedication(searchMedication){
  const response = await axios.get(`https://rxnav.nlm.nih.gov/REST/drugs.json?name=${searchMedication}`)
  return response
}
