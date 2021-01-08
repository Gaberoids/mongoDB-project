// this code initialize the mobil version of nav page. It was taken from normalize css web page https://materializecss.com/navbar.html
$(document).ready(function () {
    $('.sidenav').sidenav({ edge: "right" }); // sidenav show on the right https://materializecss.com/sidenav.html#options
    $('.collapsible').collapsible();  // this is for the acordedon collapsable items from materializecss too
    $('.tooltipped').tooltip(); // materialized
    $('select').formSelect(); // All below the same as above
    $('.datepicker').datepicker({
        format: "dd mmm yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
});