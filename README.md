# Medical Claim PDF Extractor

A Python application to **extract structured information from medical claim PDFs** using OCR and LLMs. Users can upload PDFs via a **Streamlit frontend**, which calls a **FastAPI backend** to process the document and return extracted data in JSON format.

---

## Features

- Extract key fields from medical claim documents:
  - `patient_name`
  - `contact_number`
  - `policy_number`
  - `provider_name` (Insurance Company)
  - `hospital_name`
  - `total_bill_amount`
- Supports **scanned PDFs** using OCR (`pytesseract` + `pdf2image`)
- Easy **web interface** with Streamlit
- **FastAPI backend** handles PDF uploads and processing
- LLM-based extraction using LangChain + Ollama

---

## Requirements

- Python 3.9+
- macOS / Linux / Windows
- Virtual environment (recommended)
- **Ollama LLM running locally** (for the `llama3` model)

### Python Packages

```text
fastapi
uvicorn
python-multipart
streamlit
pytesseract
pdf2image
pydantic
requests
langchain_community
langchain_ollama
```

> Tesseract OCR and Poppler must be installed on your system (see Installation below).

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Durga-shetty/Medical-Claims-Extraction.git
cd medical-claim-extractor
```

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv rag_venv
source rag_venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## Install System Dependencies (macOS)

### Install Tesseract OCR

```bash
brew install tesseract
```

Verify:

```bash
tesseract --version
```

### Install Poppler (Required for pdf2image)

```bash
brew install poppler
```

Verify:

```bash
pdfinfo -v
```

---

## Run Ollama LLM

Make sure you have Ollama installed locally.

Download from:  
https://ollama.com/download

Pull the model:

```bash
ollama pull llama3
```

Run the model:

```bash
ollama run llama3
```

⚠️ Keep this running while using your application.

---

## FastAPI Backend

Start the FastAPI server:

```bash
uvicorn app:app --reload --port 8000
```

Endpoint:

```
POST /upload
```

Upload a PDF and receive extracted JSON.

---

## Streamlit Frontend

Run Streamlit app:

```bash
streamlit run streamlit_app.py
```

- Upload a PDF (only `.pdf` allowed)
- View extracted information in JSON format

---

## Project Structure

```text
.
├── app.py                      # FastAPI backend
├── streamlit_app.py            # Streamlit frontend
├── medical_info_extractor.py   # OCR + LLM extraction logic
├── config.py                   # Prompt configuration
├── uploaded_pdfs/              # Folder to store uploaded PDFs
├── data/                       # Sample PDFs
└── requirements.txt            # Python dependencies
```

---

## Notes / Tips

- Make sure `tesseract` and `pdfinfo` (from Poppler) are in your PATH.
- FastAPI handles file uploads; Streamlit calls the `/upload` endpoint.
- Ollama LLM must be running locally before calling the backend.
- Virtual environment is highly recommended to avoid version conflicts.
