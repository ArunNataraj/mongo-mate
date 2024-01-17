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
        <button type="submit">Insert Record(s)</button>
    </form>`;
}

function getUpdateForm() {
    return `<h3>Update Record(s)</h3>
    <form id="updateForm">
        <div style="margin-bottom: 10px;">
            <label for="field">Field:</label>
            <input type="text" id="field" name="field" placeholder="field...">
            <label for="operator">Operator:</label>
            <select id="operator" name="operator" placeholder="operators">
                <option value="equals">Equals</option>
            </select>
    
            <label for="value">Value:</label>
            <input type="text" id="fieldValue" name="fieldValue" placeholder="value..."><br><br>
        </div>
    
        <div style="margin-bottom: 10px;">
            <label for="updateJsonInput">JSON Input:</label>
            <textarea id="updateJsonInput" name="updateJson" rows="10" style="width: 100%;" required></textarea>
            <p id="jsonErrorMessage" class="error-message"></p>
        </div>
        <label>
            <input type="radio" name="trueFalseOption" value="false" checked>
            Record
        </label>
        <label>
            <input type="radio" name="trueFalseOption" value="true">
            All Records
        </label>
        <button type="submit">Update Record(s)</button>
    </form>`;
}

function getDeleteForm() {
    return `<h3>Delete Record(s)</h3>
    <form id="deleteForm">
        <label for="field">Field:</label>
        <input type="text" id="field" name="field" placeholder="field..." required>
        <label for="operator">Operator:</label>
        <select id="operator" name="operator" placeholder="operators" required>
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
        <button id="deleteRecord" type="submit">Delete Record(s)</button>
    </form>
    `;
}

function getQueryExecutionForm() {
    return `
        <h3>Query Execution</h3>
        <form id="queryExecutionForm">
            <label for="querySelect">Select Query:</label>
            <select id="querySelect"></select>

            <label for="queryParameter">Query Parameter:</label>
            <input type="text" id="queryParameter" name="queryParameter" required><br>
            <div>
            <button type="submit">Execute Query</button>
            </div>
        </form>
    `;
}