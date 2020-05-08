// "// Access-Control-Allow-Origin": '*',
// 'Access-Control-Allow-Credentials': true,
// const axios = require('axios');
// const oauth = require('axios-oauth-client');
// const getAuthorizationCode = oauth.client(axios.create(), {
//   url: 'https://drchrono.com/o/token/',
//   grant_type: 'authorization_code',
//   client_id: 'IvnxhWMo16B9BQBVs89XfvEWYgDrPch5ZGnwCBvK',
//   client_secret: 'BHHd5xFV1arUnXykMl5CRiSKu8q6GFNCEcgKVyYMZktalOo2VE3dZlG8z94QJoaUT9RuMCf8OWehrKz0Vj4ShrXLmA6GHCBwGUJdqP0dUiJbf9xKhAVwuDEltTz4n3qw',
//   redirect_uri: 'http://127.0.0.1:5000/token',
//   code: '...',
// });
 
// const auth = await getAuthorizationCode();


// const axios = require('axios');
// const oauth = require('axios-oauth-client');
// const getOwnerCredentials = oauth.client(axios.create(), {
//   url: 'https://drchrono.com/o/token/',
//   grant_type: 'authorization_code',
//   client_id: 'IvnxhWMo16B9BQBVs89XfvEWYgDrPch5ZGnwCBvK',
//   client_secret: 'BHHd5xFV1arUnXykMl5CRiSKu8q6GFNCEcgKVyYMZktalOo2VE3dZlG8z94QJoaUT9RuMCf8OWehrKz0Vj4ShrXLmA6GHCBwGUJdqP0dUiJbf9xKhAVwuDEltTz4n3qw',
//   username: '',
//   password: ''
// });
 
// const auth = await getOwnerCredentials();
// console.log(auth)
const COR_URL = "https://cors-anywhere.herokuapp.com/"
const BASE_URL = "https://app.drchrono.com/api";

async function getPatientId(patient_id) {
  console.log(patient_id,"patient_id")
  const headers = {
    'headers':{
      "Authorization":`Bearer ${access_token}`, 
      "Access-Control-Allow-Origin": '*',
      "Content-type":"application/json"
    }
  }
  const response = await axios.get(`https://cors-anywhere.herokuapp.com/${BASE_URL}/medications?patient=${patient_id}`,headers)
  return response
};

async function getMedication(searchMedication){
  const response = await axios.get(`https://rxnav.nlm.nih.gov/REST/drugs.json?name=${searchMedication}`)
  console.log(response,'inside get medicated response')
  console.log(response)
  return response
}
