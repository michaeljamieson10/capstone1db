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
     $('.medication-search').prepend(`<div id="medication-add-name" class="alert alert-danger m3" role="alert"> Please insert a name of the medication</div>`)
    //  let given_med = $(`#medication-add-name`)
    //  setTimeout(function(){
    //      given_med.fadeOut('slow')
    //  },1500)
   }
   if($('#drug_strengths').val() == ""){
    event.preventDefault()
    // alert('PLEASE INSERT A Drug strength')
    $('.medication-search').prepend(`<div id="medication-add-name" class="alert alert-danger m3" role="alert"> Please insert a strength of the medication</div>`)

  }
   if($('#icd10').val() == ""){
    event.preventDefault()
    // alert('PLEASE INSERT A DIAGNOSIS')
    $('.medication-search').prepend(`<div id="medication-add-name" class="alert alert-danger m3" role="alert"> Please insert a diagnosis.</div>`)
  }
 })