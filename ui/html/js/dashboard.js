document.addEventListener("DOMContentLoaded", function () {
    const contentDiv = document.getElementById("content");
    let accessToken = localStorage.getItem("accessToken")

    // Function to load content dynamically
    function loadContent(content) {
        contentDiv.innerHTML = content;
    }

    // Event listeners for navigation links
    const viewDataLink = document.getElementById("viewDataLink");
    const insertDataLink = document.getElementById("insertDataLink");
    const updateDataLink = document.getElementById("updateDataLink");
    const deleteDataLink = document.getElementById("deleteDataLink");
    const queryExecutionLink = document.getElementById("queryExecutionLink");
    const logoutLink = document.getElementById("logoutLink");
    const viewRecordBtn = document.getElementById("viewRecord");
    const viewRecordsBtn = document.getElementById("viewRecords");

    viewDataLink.addEventListener("click", function (event) {
        event.preventDefault();
        loadContent(getviewForm());
        // loadViewDataPage();
    });
    // if (viewRecordBtn) {
    //     viewRecordBtn.addEventListener("click", function (event) {
    //         event.preventDefault();
    //         loadViewDataPage();
    //     });
    // }

    insertDataLink.addEventListener("click", function (event) {
        event.preventDefault();
        loadContent(getInsertForm());
        handleJsonInput();
    });

    updateDataLink.addEventListener("click", function (event) {
        event.preventDefault();
        loadContent(getUpdateForm());
        handleJsonInput();
    });

    deleteDataLink.addEventListener("click", function (event) {
        event.preventDefault();
        loadContent(getDeleteForm());
    });

    queryExecutionLink.addEventListener("click", function (event) {
        event.preventDefault();
        loadContent(getQueryExecutionForm());
    });

    logoutLink.addEventListener("click", function (event) {
        event.preventDefault();
        // Implement logic for logout, redirect to login page, or perform other actions
        localStorage.clear();
        accessToken = ""
        // history.pushState(null, null, "login.html");
        window.location.href = "login.html";
    });

    // Event listener for form submissions
    contentDiv.addEventListener("submit", function (event) {
        event.preventDefault();

        // Identify which form was submitted
        const formId = event.target.id;

        switch (formId) {
            case "viewForm":
                loadViewDataPage();
            case "insertForm":
                handleInsertFormSubmission();
                break;
            case "updateForm":
                handleUpdateFormSubmission();
                break;
            case "deleteForm":
                handleDeleteFormSubmission();
                break;
            case "queryExecutionForm":
                handleQueryExecutionFormSubmission();
                break;
        }
    });

    function loadViewDataPage() {
        const selectedTableName = tableNameSelect.value;
    
        // Make API request to fetch data based on the selected table name
        fetch(`http://localhost:8000/records/${selectedTableName}`, {
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
                displayViewData(data);
            })
            .catch(error => {
                console.error("Error fetching data:", error);
                contentDiv.innerHTML = "Error fetching data";
            });
    }
    

    function displayViewData(data) {
        // Clear existing content
        contentDiv.innerHTML = `${getviewForm()} <br>`;

        // Check if data is available
        if (!data || data.length === 0) {
            contentDiv.innerHTML += "<p>No data available for the selected table.</p>";
            return;
        }

        const recordsArray = data.records;

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

    // Example CSS styles for the boxes
    const styles = `
        .records-container {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }
    
        .record-box {
            border: 1px solid #ccc;
            border-radius: 10px;
            padding: 10px;
            margin: 0 auto 20px;
            margin-bottom: 10px;
            width: calc(100% - 20px);
            word-wrap: break-word; /* Add this line for line wrapping */
            box-sizing: border-box;
        }
    `;

    // Create a style element and append it to the head
    const styleElement = document.createElement("style");
    styleElement.innerHTML = styles;
    document.head.appendChild(styleElement);

    // Example function to handle Insert Data form submission
    function handleInsertFormSubmission() {
        const insertFieldsValue = document.getElementById("insertJsonInput").value;

        // Parse the input JSON string to an object
        const selectedTableName = tableNameSelect.value;

        // Make API request to insert data using the values obtained
        fetch("http://localhost:8000/record", {
            method: "POST",
            headers: {
                "Authorization": `Bearer ${accessToken}`,
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                collection_name: selectedTableName,
                fields: JSON.parse(insertFieldsValue),
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


    // Example function to handle Update Data form submission
    function handleUpdateFormSubmission() {
        const updateRecordIdValue = document.getElementById("updateRecordId").value;
        const updateFieldsValue = document.getElementById("updateJsonInput").value;

        // Make API request to update data using the values obtained
        const selectedTableName = tableNameSelect.value;

        fetch(`http://localhost:8000/record`, {
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


    // Example function to handle Delete Data form submission
    function handleDeleteFormSubmission() {
        const selectedTableName = tableNameSelect.value;
        const deleteRecordIdValue = document.getElementById("deleteRecordId").value;

        // Make API request to delete data using the value obtained
        fetch("http://localhost:8000/record", {
            method: "DELETE",
            headers: {
                "Authorization": `Bearer ${accessToken}`,
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                collection_name: selectedTableName,
                fields: { _id: deleteRecordIdValue },
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
                displayViewData({ records: [data.deleted_record], message: data.message });

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

    // Fetch table names dynamically and populate the dropdown
    fetch("http://localhost:8000/collections", {
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
});
