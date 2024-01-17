document.addEventListener("DOMContentLoaded", function () {
    const contentDiv = document.getElementById("content");
    getCollectionNames(document)

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

    viewDataLink.addEventListener("click", function (event) {
        event.preventDefault();
        loadContent(getViewForm());
        getCollectionNames(document);
    });
    insertDataLink.addEventListener("click", function (event) {
        event.preventDefault();
        loadContent(getInsertForm());
        getCollectionNames(document);
        handleJsonInput(document);
    });

    updateDataLink.addEventListener("click", function (event) {
        event.preventDefault();
        loadContent(getUpdateForm());
        getCollectionNames(document);
        handleJsonInput(document);
    });

    deleteDataLink.addEventListener("click", function (event) {
        event.preventDefault();
        loadContent(getQueryForm());
        getCollectionNames(document);
    });

    queryExecutionLink.addEventListener("click", function (event) {
        event.preventDefault();
        loadContent(getQueryExecutionForm());
        getCollectionNames(document);
        getPredefinedQueries(document);
        const querySelect = document.getElementById("querySelect");
        querySelect.addEventListener("change", function () {
            // Get the selected value from the dropdown
            const queryParams = getQueryParams()
            console.log(queryParams)
            const queryParameterInput = document.getElementById("queryParameter");
            const selectedQuery = querySelect.value;

            // Update the placeholder of the queryParameter input based on the selected query
            queryParameterInput.placeholder = queryParams[selectedQuery]
        });
    });

    logoutLink.addEventListener("click", function (event) {
        event.preventDefault();
        // Implement logic for logout, redirect to login page, or perform other actions
        localStorage.clear();
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
                loadViewDataPage(document);
                break;
            case "insertForm":
                handleInsertFormSubmission(document);
                break;
            case "updateForm":
                handleUpdateFormSubmission(document);
                break;
            case "deleteForm":
                handleDeleteFormSubmission(document);
                break;
            case "queryExecutionForm":
                handleQueryExecutionFormSubmission();
                break;
        }
    });
});
