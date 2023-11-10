function addEntry() {
    var nameInput = document.getElementById("nameInput");
    var numberInput = document.getElementById("numberInput");

    var name = nameInput.value.trim();
    var number = numberInput.value.trim();

    if (name !== "" && number !== "") {
        var entryList = document.getElementById("entryList");
        var listItem = document.createElement("li");
        listItem.textContent = "Name: " + name + ", Number: " + number;
        entryList.appendChild(listItem);
        nameInput.value = "";
        numberInput.value = "";
    }
}

// Get the input fields
var nameInput = document.getElementById("nameInput");
var numberInput = document.getElementById("numberInput");

// Listen for "Enter" key press on both input fields
nameInput.addEventListener("keyup", function(event) {
    if (event.key === "Enter") {
        addEntry();
    }
});

numberInput.addEventListener("keyup", function(event) {
    if (event.key === "Enter") {
        addEntry();
    }
});

// Function to add entry
function addEntry() {
    var name = nameInput.value.trim();
    var number = numberInput.value.trim();

    if (name !== "" && number !== "") {
        // Create a data string with name and number
        var data = "Name: " + name + ", Number: " + number + "\n";

        // Create a Blob with the data and specify the MIME type as text/plain
        var blob = new Blob([data], { type: "text/plain" });

        // Create a temporary anchor element and set its download attribute and href
        var a = document.createElement("a");
        a.href = URL.createObjectURL(blob);
        a.download = "data.txt";

        // Append the anchor element to the document body and simulate a click event
        document.body.appendChild(a);
        a.click();

        // Remove the temporary anchor element
        document.body.removeChild(a);

        // Clear the input fields
        nameInput.value = "";
        numberInput.value = "";
    }
}

