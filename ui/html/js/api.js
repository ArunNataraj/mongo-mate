const server = "http://localhost:8000/"

function loadViewDataPage(document) {
    const contentDiv = document.getElementById("content");
    const tableNameSelect = document.getElementById("tableNameSelect");
    const selectedTableName = tableNameSelect.value;
    const accessToken = localStorage.getItem("accessToken");
    const selectedValue = document.querySelector('input[name="trueFalseOption"]:checked').value;
    const field = document.getElementById("field").value;
    const operator = document.getElementById("operator").value;
    const fieldValue = document.getElementById("fieldValue").value;
    let path = "record"
    let queryParameter=""
    if (selectedValue === "true") {
        path = "records"
    }
    if (field && operator && fieldValue) {
        queryParameter=`?&field=${field}&operator=${operator}&value=${fieldValue}`;
    }
    // Make API request to fetch data based on the selected table name
    fetch(`${server}${path}/${selectedTableName}${queryParameter}`, {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${accessToken}`,
            "Content-Type": "application/json",
        }
    })
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then(data => {
            // Display the fetched data in the content area
            displayViewData(document, data);
        })
        .catch(error => {
            console.error("Error fetching data:", error);
            contentDiv.innerHTML = "Error fetching data";
        });
}

function handleInsertFormSubmission(document) {
    const tableNameSelect = document.getElementById("tableNameSelect");
    const selectedTableName = tableNameSelect.value;
    let accessToken = localStorage.getItem("accessToken");
    const insertFieldsValue = JSON.parse(document.getElementById("insertJsonInput").value);
    const isArray = Array.isArray(insertFieldsValue)
    let path = "record"
    if (isArray) {
        path = "records"
    }
    // Make API request to insert data using the values obtained
    fetch(`${server}${path}`, {
        method: "POST",
        headers: {
            "Authorization": `Bearer ${accessToken}`,
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            collection_name: selectedTableName,
            fields: insertFieldsValue,
        }),
    })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Handle successful API response
            console.log("API response:", data);
            // Optionally, provide user feedback on success
        })
        .catch(error => {
            // Handle error during API call
            console.error("Error during API call:", error);
            // Optionally, provide user feedback on failure
        });
}

function handleUpdateFormSubmission(document) {
    const tableNameSelect = document.getElementById("tableNameSelect");
    const selectedTableName = tableNameSelect.value;
    let accessToken = localStorage.getItem("accessToken");
    const updateRecordIdValue = document.getElementById("updateRecordId").value;
    const updateFieldsValue = document.getElementById("updateJsonInput").value;



    fetch(`${server}record`, {
        method: "PUT",
        headers: {
            "Authorization": `Bearer ${accessToken}`,
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            collection_name: selectedTableName,
            query: { _id: updateRecordIdValue },
            fields: JSON.parse(updateFieldsValue),
        }),
    })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Handle successful API response
            console.log("API response:", data);

            // Optionally, provide user feedback on success
        })
        .catch(error => {
            // Handle error during API call
            console.error("Error during API call:", error);

            // Optionally, provide user feedback on failure
        });
}

function handleDeleteFormSubmission(document) {
    const tableNameSelect = document.getElementById("tableNameSelect");
    const selectedTableName = tableNameSelect.value;
    let accessToken = localStorage.getItem("accessToken");
    const deleteRecordButton = document.getElementById("deleteRecord");
    const deleteAllRecordsButton = document.getElementById("deleteAllRecords");

    deleteAllRecordsButton.addEventListener("submit", function () {
        console.log("ALL RECORDS DELETE")
    });


    deleteRecordButton.addEventListener("submit", function () {
        console.log("ONE RECORD DELETE")
    });

    // Make API request to delete data using the value obtained
    fetch(`${server}record`, {
        method: "DELETE",
        headers: {
            "Authorization": `Bearer ${accessToken}`,
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            collection_name: selectedTableName,
            // fields: { _id: deleteRecordIdValue },
        }),
    })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Handle successful API response
            console.log("API response:", data);

            // Display the deleted record as view data
            displayViewData(document, { records: [data.deleted_record], message: data.message });

            // Optionally, provide user feedback on success
        })
        .catch(error => {
            // Handle error during API call
            console.error("Error during API call:", error);
            // Optionally, provide user feedback on failure
        });
}

function handleQueryExecutionFormSubmission() {
    const selectedQuery = document.getElementById("querySelect").value;
    const queryParameter = document.getElementById("queryParameter").value;

    // Make API request to execute the selected query with the provided parameter
    // ...

    // Optionally, provide user feedback on success or failure
}


function getCollectionNames(document) {
    let accessToken = localStorage.getItem("accessToken");
    // Fetch table names dynamically and populate the dropdown
    fetch(`${server}collections`, {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${accessToken}`, // Replace yourAccessToken with the actual user's access token
        },
    })
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then(data => {
            const tableNames = data.collection_names; // Extracting table names from the response
            const tableNameSelect = document.getElementById("tableNameSelect");

            // Clear existing options
            tableNameSelect.innerHTML = "";

            // Populate dropdown with dynamic table names
            tableNames.forEach(tableName => {
                const option = document.createElement("option");
                option.value = tableName;
                option.text = tableName;
                tableNameSelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error("Error fetching table names:", error);
            // Handle the error, show a message, or fallback to default table names
        });
}