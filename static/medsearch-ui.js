/**
 * This is directly from the api 
 *https://clinicaltables.nlm.nih.gov/api
 */
new Def.Autocompleter.Prefetch('drug_strengths', []);
new Def.Autocompleter.Search('rxterms',
 'https://clinicaltables.nlm.nih.gov/api/rxterms/v3/search?ef=STRENGTHS_AND_FORMS');
Def.Autocompleter.Event.observeListSelections('rxterms', function() {
  var drugField = $('#rxterms')[0];
  var autocomp = drugField.autocomp;
  var strengths =
    autocomp.getSelectedItemData()[0].data['STRENGTHS_AND_FORMS'];
  if (strengths)
    $('#drug_strengths')[0].autocomp.setListAndField(strengths, '');
})

new Def.Autocompleter.Search('icd10', 'https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search?sf=code,name',
 {tableFormat: true, valueCols: [0,1], colHeaders: ['Code', 'Name']});

 $("#medication-add").on("click", function(event){
   if($('#rxterms').val() == ""){
     event.preventDefault()
    /**
     * Will show to html that user needs to enter medication name
     */
    //  $('.medication-search').prepend(`<div id="medication-add-name" class="alert alert-danger m3" role="alert"> Please insert a name of the medication</div>`)
    $('#rxterms').attr("placeholder", "Enter A Medication!")
   }
   if($('#drug_strengths').val() == ""){
    event.preventDefault()
    /**
     * Will show to html that user needs to enter drug strength
     */
    // $('.medication-search').prepend(`<div id="medication-add-name" class="alert alert-danger m3" role="alert"> Please insert a strength of the medication</div>`)
    $('#drug_strengths').attr("placeholder", "Enter A Strength!")
  }
   if($('#icd10').val() == ""){
    event.preventDefault()
    /**
     * Will show to html that user needs to enter diagnosis
     */
    // $('.medication-search').prepend(`<div id="medication-add-name" class="alert alert-danger m3" role="alert"> Please insert a diagnosis.</div>`)
    $('#icd10').attr("placeholder", "Enter A Diagnosis!")
  }
 })