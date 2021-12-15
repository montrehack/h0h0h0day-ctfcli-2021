
document.querySelector('#form').addEventListener('submit', function(e){
    e.preventDefault();
    var query = e.target.elements['name'].value;
    post(query);
});

function showMessage(input, message, type) {
    // get the small element and set the message
    const msg = input.parentNode.querySelector("small");
    msg.innerText = message;
    // update the class for the input
    input.className = type ? "success" : "error";
    return type;
}

function renderTable(data) {
    const tbody = document.getElementById('List').getElementsByTagName('tbody')[0];
    tbody.innerHTML = "";

    data.rows.map((row) => {
        const newRow = tbody.insertRow();
        for (const [_, value] of Object.entries(row)) {
            const newCell = newRow.insertCell();
            const newText = document.createTextNode(value);
            newCell.appendChild(newText);
          }
    });
}

function post(query) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/view-list", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    xhr.onreadystatechange = function() {
        const tbody = document.getElementById('List').getElementsByTagName('tbody')[0];
        tbody.innerHTML = "";

        if (this.readyState == XMLHttpRequest.DONE && this.status == 200) {
            const dict = JSON.parse(this.responseText);
            renderTable(dict.data);
        } else if (this.readyState == XMLHttpRequest.DONE && this.status == 400) {
            alert("Hacker Detected");
        }
    };
    xhr.send("name=" + query);
};

