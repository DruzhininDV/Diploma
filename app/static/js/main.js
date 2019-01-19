$('[data-toggle=confirmation]').confirmation({
    rootSelector: '[data-toggle=confirmation]'
    //btnOkLabel: 'Si',
    //btnCancelLabel: 'No'
});

$(document).ready(function () {
    console.log("ready!");
    var slider = document.getElementById("myRange");
    var output = document.getElementById("demo");
    output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
    slider.oninput = function () {
        output.innerHTML = this.value;
    }

});