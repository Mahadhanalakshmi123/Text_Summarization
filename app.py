from flask import Flask, send_file, request, jsonify
from transformers import BartTokenizer, BartForConditionalGeneration
import fitz  # PyMuPDF for PDFs
import requests
from bs4 import BeautifulSoup
import base64

app = Flask(__name__)

# Load BART tokenizer and model
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

# Function to generate summary
def generate_summary(text):
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs["input_ids"], max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Extract text from PDF
def extract_text_from_pdf(pdf_data):
    doc = fitz.open(stream=pdf_data, filetype="pdf")
    text = "\n".join([page.get_text() for page in doc])
    return text

# Extract text from URL
def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = [p.get_text() for p in soup.find_all("p")]
    return " ".join(paragraphs)

@app.route('/')
def about():
    return send_file('about.html')

@app.route('/summarize')
def summarize():
    return send_file('summarize.html')

@app.route('/styles.css')
def styles():
    return send_file('styles.css')

@app.route('/script.js')
def script():
    return send_file('script.js')

@app.route('/summarize_text', methods=['POST'])
def summarize_text():
    data = request.json
    if "text" in data:
        summary = generate_summary(data["text"])
    elif "pdfContent" in data:
        pdf_data = base64.b64decode(data["pdfContent"].split(",")[1])  # Decode Base64 PDF
        extracted_text = extract_text_from_pdf(pdf_data)
        summary = generate_summary(extracted_text)
    elif "url" in data:
        extracted_text = extract_text_from_url(data["url"])
        summary = generate_summary(extracted_text)
    else:
        return jsonify({"error": "Invalid input"}), 400

    return jsonify({"summary": summary})

if __name__ == '__main__':
    app.run(debug=True)
