// Function to handle input in the JSON textarea
function handleJsonInput() {
    const updateJsonInput = document.getElementById("updateJsonInput") || document.getElementById("insertJsonInput");
    const errorMessage = document.getElementById("jsonErrorMessage");

    // Validate JSON input while typing
    updateJsonInput.addEventListener("input", function () {
        const jsonValue = updateJsonInput.value;
        try {
            JSON.parse(jsonValue);
            errorMessage.textContent = ""; // Clear error message
        } catch (error) {
            if (jsonValue.trim() === "") {
                errorMessage.textContent = "";
            }
            else {
                errorMessage.textContent = "Invalid JSON input";
            }
        }
    });
}

function displayViewData(document, data, callback) {
    const contentDiv = document.getElementById("content");
    // Clear existing content
    contentDiv.innerHTML = `${callback()} <br>`;

    // Check if data is available
    if (!data || data.length === 0) {
        contentDiv.innerHTML += "<p>No data available for the selected table.</p>";
        return;
    }

    const recordsArray = data.records;
    if (typeof (recordsArray) === "string") {
        contentDiv.innerHTML += `<p style="color: green;">${recordsArray}</p>`;
        return;
    }
    if (!recordsArray || recordsArray.length === 0 || recordsArray[0] === null) {
        contentDiv.innerHTML += "<p>No data available for the selected table.</p>";
        return;
    }

    contentDiv.innerHTML += `<p style="color: green;">${data.message}</p>`
    // Iterate over each record and create a box for each
    recordsArray.forEach(record => {
        const recordBox = document.createElement("div");
        recordBox.className = "record-box";

        // Create a paragraph for each property in the record and display it
        Object.keys(record).forEach(key => {
            const propertyParagraph = document.createElement("p");
            propertyParagraph.innerHTML = `<strong>${key}:</strong> ${JSON.stringify(record[key])}`;
            recordBox.appendChild(propertyParagraph);
        });
        contentDiv.appendChild(recordBox);
    });
}