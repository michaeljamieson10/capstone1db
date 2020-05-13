async function getPatientId(patient_id) {
  const response = await axios.get(`/medications/get-current-patient/${patient_id}`)
  console.log(response.data)
  return response
};

async function getMedication(searchMedication){
  const response = await axios.get(`https://rxnav.nlm.nih.gov/REST/drugs.json?name=${searchMedication}`)
  // console.log(response, "INSIDE GET MEDICATION")
  return response
}
async function getMedication_two(searchMedication){
  // currently does nothing myb echange over entirely to otehr government api on
  // https://clinicaltables.nlm.nih.gov/apidoc/rxterms/v3/doc.html
  // const response = await axios.get(`https://rxnav.nlm.nih.gov/REST/drugs.json?name=${searchMedication}`)
  // console.log(response, "INSIDE GET MEDICATION")
  return response
}
