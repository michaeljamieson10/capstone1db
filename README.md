# capstone1db
capstone1db remade without dr.chrono

This is a capstone project to develop a small emr. You can create medications and patients, assign a doctor and nurse, 
then give the medication in the emr
2. Please include the following details:
  a. The title of your site and a link to the URL where it is deployed
      EMR is the title of the site
  b. Describe what your website does
       You can create medications and patients, assign a doctor and nurse, 
then give the medication in the emr
c. List the features you implemented and explain why you chose those
features to implement
  I chose to implement these features because at the facility I used to work I dealt with these parts the most.
  I was curious how they work, and I plan on adding more features that may be useful for someone working in healthcare.
d. Walk someone through the standard user flow for the website
  The navbar has all the features, administer medications has the emr where you can give medications,
  the create tabs where you can create.
e. Keep the API in there, and if you have anything to say about the API then
  I got the api from a government website https://clinicaltables.nlm.nih.gov/api
  which actually creates the search inputs for you for the icd10 diagnosis and the name of the medication
  They are up to date, they include a diagnosis for covid-19.
f. Identify the technology stack used to create your website
  I used FLASK Python for server side SQL alchemy for backend and HTML/CSS JS for front end
g. Include anything else that you feel is important to share
  I used WTForms for the forms, and tested the views and models. 
