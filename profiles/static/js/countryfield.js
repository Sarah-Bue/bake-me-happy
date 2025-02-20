// This code has been adapted from Code Institute's "Boutique Ado" project

let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#6c757d');
};
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#6c757d');
    } else {
        $(this).css('color', '#000');
    }
});