function getInsertForm() {
    return `
        <h3>Insert Data</h3>
        <form id="insertForm">
            <div style="margin-bottom: 10px;">
                <label for="insertJsonInput">JSON Input:</label>
                <textarea id="insertJsonInput" name="insertJson" rows="10" style="width: 100%;" required></textarea>
                <p id="jsonErrorMessage" class="error-message"></p>
            </div>
            <!-- Add more fields as needed -->

            <button type="submit">Insert Record</button>
        </form>
    `;
}

function getUpdateForm() {
    return `
        <h3>Update Data</h3>
        <form id="updateForm">
            <div style="margin-bottom: 10px;">
                <label for="updateRecordId">Record ID:</label>
                <input type="text" id="updateRecordId" name="recordId" required>
            </div>

            <div style="margin-bottom: 10px;">
                <label for="updateJsonInput">JSON Input:</label>
                <textarea id="updateJsonInput" name="updateJson" rows="10" style="width: 100%;" required></textarea>
                <p id="jsonErrorMessage" class="error-message"></p>
            </div>
    
            <button type="submit">Update Record</button>
        </form>
    `;
}

function getDeleteForm() {
    return `
        <h3>Delete Data</h3>
        <form id="deleteForm">
            <label for="deleteRecordId">Record ID to Delete:</label>
            <input type="text" id="deleteRecordId" name="recordIdToDelete" required>

            <button type="submit">Delete Record</button>
        </form>
    `;
}

function getQueryExecutionForm() {
    return `
        <h3>Query Execution</h3>
        <form id="queryExecutionForm">
            <label for="querySelect">Select Query:</label>
            <select id="querySelect">
                <option value="query1">Query 1</option>
                <option value="query2">Query 2</option>
                <!-- Add more queries as needed -->
            </select>

            <label for="queryParameter">Query Parameter:</label>
            <input type="text" id="queryParameter" name="queryParameter" required>

            <button type="submit">Execute Query</button>
        </form>
    `;
}

function getviewForm() {
    return `
        <h3>View Record(s)</h3>
        <form id="viewForm">
            <label for="field">Field:</label>
            <input type="text" id="field" name="field" placeholder="field...">
            <label for="operator">Operator:</label>
            <select id="operator" name="operator" placeholder="operators">
                <option value="operator..." disabled selected>operators...</option>
                <option value="equals">Equals</option>
                <option value="contains">Contains</option>
                <!-- Add more options based on your needs -->
            </select>

            <label for="value">Value:</label>
            <input type="text" id="value" name="value" placeholder="value..."><br><br>

            <button id="viewRecord" type="submit">View Record</button> <button id="viewRecords" type="submit">View All Records</button>
        </form>
    `;
}