// This code has been adapted from Code Institute's "Boutique Ado" project

/**
 * Form Field Styling
 * 
 * Function to provide dynamic styling for county and country form fields in profile and checkout forms.
 */
function styleCountyField(fieldId) {
    let countySelected = $(fieldId).val();
    if(!countySelected) {
        $(fieldId).css('color', '#6c757d');
    }

    $(fieldId).change(function() {
        countySelected = $(this).val();
        if(!countySelected) {
            $(this).css('color', '#6c757d');
        } else {
            $(this).css('color', '#000');
        }
    });
}

// Apply styling to profile form county field
if ($('#id_default_county').length) {
    styleCountyField('#id_default_county');
}

// Apply styling to checkout form county field
if ($('#id_county').length) {
    styleCountyField('#id_county');
}

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