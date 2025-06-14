function toggleInputFields() {
    let inputType = document.getElementById("inputType").value;
    document.getElementById("textInput").style.display = (inputType === "text") ? "block" : "none";
    document.getElementById("pdfInput").style.display = (inputType === "pdf") ? "block" : "none";
    document.getElementById("urlInput").style.display = (inputType === "url") ? "block" : "none";
}

function summarizeText() {
    let inputType = document.getElementById("inputType").value;
    let data = {};

    if (inputType === "text") {
        data.text = document.getElementById("inputText").value;
    } else if (inputType === "pdf") {
        let file = document.getElementById("pdfFile").files[0];
        if (file) {
            let reader = new FileReader();
            reader.onload = function(event) {
                data.pdfContent = event.target.result;
                sendRequest(data);
            };
            reader.readAsDataURL(file);
            return;
        } else {
            alert("Please select a PDF file.");
            return;
        }
    } else if (inputType === "url") {
        data.url = document.getElementById("inputURL").value;
    }

    sendRequest(data);
}

function sendRequest(data) {
    fetch("/summarize_text", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("summary").innerText = data.summary;
    })
    .catch(error => console.error("Error:", error));
}
