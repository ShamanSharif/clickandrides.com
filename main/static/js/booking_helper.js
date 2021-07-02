
// Grabbing return date and time boolean and hide it initially
var returnDateTimeField = document.getElementById("id_returnDateTime");
returnDateTimeField.style.display = "None";

// Grabbing return booking boolean to a variable and set a event Listener
var returnChoice = document.getElementById('id_doBookReturn');
returnChoice.addEventListener("click", returnChoiceFunc);

// Function to run when return boolean pressed, mainly hiding return date time
// picker and show it again
function returnChoiceFunc() {
    if (returnChoice.checked === true) {
        returnDateTimeField.style.display = "block";
    } else {
        returnDateTimeField.style.display = "None";
    }
}