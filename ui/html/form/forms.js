function getViewForm() {
    return `<h3>View Record(s)</h3>
    <form id="viewForm">
        <label for="field">Field:</label>
        <input type="text" id="field" name="field" placeholder="field...">
        <label for="operator">Operator:</label>
        <select id="operator" name="operator" placeholder="operators">
            <option value="equals">Equals</option>
        </select>
    
        <label for="value">Value:</label>
        <input type="text" id="fieldValue" name="fieldValue" placeholder="value..."><br><br>
        <label>
            <input type="radio" name="trueFalseOption" value="false" checked>
            Record
        </label>
        <label>
            <input type="radio" name="trueFalseOption" value="true">
            All Records
        </label>
        <button id="viewRecord" type="submit">View Record(s)</button>
    </form>`;
}

function getInsertForm() {
    return `<h3>Insert Record(s)</h3>
    <form id="insertForm">
        <div style="margin-bottom: 10px;">
            <label for="insertJsonInput">JSON Input:</label>
            <textarea id="insertJsonInput" name="insertJson" rows="10" style="width: 100%;" required></textarea>
            <p id="jsonErrorMessage" class="error-message"></p>
        </div>
        <button type="submit">Insert Record</button>
    </form>`;
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

            <button id="deleteRecord" type="submit">Delete Record</button>
            <button id="deleteAllRecords" type="submit">Delete All Records</button>
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