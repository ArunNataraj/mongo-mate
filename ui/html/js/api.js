const server = "http://localhost:8000/"
const accessToken = localStorage.getItem("accessToken")
let queryParams = {}

function loadViewDataPage(document) {
    const contentDiv = document.getElementById("content");
    const tableNameSelect = document.getElementById("tableNameSelect");
    const selectedTableName = tableNameSelect.value;
    const selectedValue = document.querySelector('input[name="trueFalseOption"]:checked').value;
    const field = document.getElementById("field").value;
    const operator = document.getElementById("operator").value;
    const fieldValue = document.getElementById("fieldValue").value;
    let path = "record"
    let queryParameter = ""
    if (selectedValue === "true") {
        path = "records"
    }
    if (field && operator && fieldValue) {
        queryParameter = `?&field=${field}&operator=${operator}&value=${fieldValue}`;
    }
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
            displayViewData(document, data, getViewForm);
        })
        .catch(error => {
            console.error("Error fetching data:", error);
            contentDiv.innerHTML = "Error fetching data";
        });
}

function handleInsertFormSubmission(document) {
    const tableNameSelect = document.getElementById("tableNameSelect");
    const selectedTableName = tableNameSelect.value;
    const insertFieldsValue = JSON.parse(document.getElementById("insertJsonInput").value);
    const isArray = Array.isArray(insertFieldsValue)
    let path = "record"
    if (isArray) {
        path = "records"
    }
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
                console.error("Network response was not ok", response);
                if (response.status === 401) {
                    window.location.href = "login.html";
                }
            }
            return response.json();
        })
        .then(data => {
            // Display the inserted record as view data
            displayViewData(document, data, getInsertForm);
        })
        .catch(error => {
            console.error("Error during API call:", error);
        });
}

function handleUpdateFormSubmission(document) {
    const tableNameSelect = document.getElementById("tableNameSelect");
    const selectedTableName = tableNameSelect.value;
    const updateFieldsValue = document.getElementById("updateJsonInput").value;
    const selectedValue = document.querySelector('input[name="trueFalseOption"]:checked').value;
    const field = document.getElementById("field").value;
    const operator = document.getElementById("operator").value;
    const fieldValue = document.getElementById("fieldValue").value;
    let reqBody = {};
    let path = "record"
    if (selectedValue === "true") {
        path = "records"
    }
    if (field && operator && fieldValue) {
        reqBody = {
            field,
            operator,
            value: fieldValue
        }
    }

    fetch(`${server}${path}`, {
        method: "PUT",
        headers: {
            "Authorization": `Bearer ${accessToken}`,
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            collection_name: selectedTableName,
            fields: JSON.parse(updateFieldsValue),
            ...reqBody
        }),
    })
        .then(response => {
            if (!response.ok) {
                console.error("Network response was not ok", response);
                if (response.status === 401) {
                    window.location.href = "login.html";
                }
            }
            return response.json();
        })
        .then(data => {
            // Display the updated record as view data
            displayViewData(document, data, getUpdateForm);

        })
        .catch(error => {
            console.error("Error during API call:", error);
        });
}

function handleDeleteFormSubmission(document) {
    const tableNameSelect = document.getElementById("tableNameSelect");
    const selectedTableName = tableNameSelect.value;
    const selectedValue = document.querySelector('input[name="trueFalseOption"]:checked').value;
    const field = document.getElementById("field").value;
    const operator = document.getElementById("operator").value;
    const fieldValue = document.getElementById("fieldValue").value;
    let reqBody = {};
    let path = "record"
    if (selectedValue === "true") {
        path = "records"
    }
    if (field && operator && fieldValue) {
        reqBody = {
            field,
            operator,
            value: fieldValue
        }
    }
    fetch(`${server}${path}`, {
        method: "DELETE",
        headers: {
            "Authorization": `Bearer ${accessToken}`,
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            collection_name: selectedTableName,
            ...reqBody
        }),
    })
        .then(response => {
            if (!response.ok) {
                console.error("Network response was not ok", response);
                if (response.status === 401) {
                    window.location.href = "login.html";
                }
            }
            return response.json();
        })
        .then(data => {
            // Display the deleted records as view data
            displayViewData(document, data, getDeleteForm);
        })
        .catch(error => {
            console.error("Error during API call:", error);
        });
}

function handleQueryExecutionFormSubmission() {
    const selectedQuery = document.getElementById("querySelect").value;
    const queryParameter = document.getElementById("queryParameter").value;
    const tableNameSelect = document.getElementById("tableNameSelect");
    const selectedTableName = tableNameSelect.value;

    // Define the data to be sent in the request body
    const requestBody = {
        pre_defined_query: selectedQuery,
        collection_name: selectedTableName
    };
    if (selectedQuery === "query1") {
        requestBody.collection_name = queryParameter
    }
    else if (selectedQuery === "query2" || selectedQuery === "query3" || selectedQuery === "query4") {
        requestBody.field = queryParameter
    }
    else if (selectedQuery === "query5") {
        requestBody.limit_count = parseInt(queryParameter)
    }
    else if (selectedQuery === "query6") {
        requestBody.fields = queryParameter.split(" ")
    }

    fetch(`${server}execute-pre-defined-queries`, {
        method: "POST",
        headers: {
            "Authorization": `Bearer ${accessToken}`,
            "Content-Type": "application/json",
        },
        body: JSON.stringify(requestBody),
    })
        .then(response => {
            if (!response.ok) {
                console.error("Network response was not ok", response);
                if (response.status === 401) {
                    window.location.href = "login.html";
                }
            }
            return response.json();
        })
        .then(data => {
            displayViewData(document, data, getQueryExecutionForm)
            getPredefinedQueries(document);
        })
        .catch(error => {
            console.error("Error during API call:", error);
        });
}



function getCollectionNames(document) {
    if (accessToken === null) {
        window.location.href = "login.html";
    }
    fetch(`${server}collections`, {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${accessToken}`,
        },
    })
        .then(response => {
            if (!response.ok) {
                console.error("Network response was not ok", response);
                if (response.status === 401) {
                    window.location.href = "login.html";
                }
            }
            return response.json();
        })
        .then(data => {
            // Extracting table names from the response
            const tableNames = data.collection_names;
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
        });
}


function getPredefinedQueries(document) {
    fetch(`${server}pre-defined-queries`, {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${accessToken}`,
        },
    })
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then(data => {
            // Extracting queries from the response
            const queries = data.queries;
            const querySelect = document.getElementById("querySelect");

            // Clear existing options
            querySelect.innerHTML = "";

            // Populate dropdown with dynamic table names
            Object.keys(queries).forEach(key => {
                const query = queries[key];
                const option = document.createElement("option");
                option.value = key
                option.text = Object.keys(query)[0];
                querySelect.appendChild(option);
                queryParams[option.value] = query[option.text]
            })
        })
        .catch(error => {
            console.error("Error fetching pre-defined-queries:", error);
        });
}

function getQueryParams() {
    return queryParams
}