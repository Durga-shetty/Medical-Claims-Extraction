import re
import json
from typing import Optional, List

from pydantic import BaseModel, ValidationError
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.llms import Ollama
from pdf2image import convert_from_path
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"
from config import prompt

#Schema
class ClaimSchema(BaseModel):
    patient_name:Optional[str]
    contact_number: Optional[str]
    policy_number: Optional[str]
    provider_name: Optional[str]
    hospital_name: Optional[str]
    total_bill_amount: Optional[str]


## LLM INIT

llm = Ollama(model = 'llama3')

## ocr for scanned or images

def ocr_pdf(path: str) -> List[str]:
    images = convert_from_path(path)
    pages_text = []
    for img in images:
        text = pytesseract.image_to_string(img)
        pages_text.append(text)
    return pages_text


##Load pdf page by page

def load_pdf_pages(path: str) -> List[str]:
    try:
        loader = PyPDFLoader(path)
        documents = loader.load()

        pages = [doc.page_content for doc in documents]

        # If empty or very small text → scanned PDF
        if sum(len(p.strip()) for p in pages) < 100:
            return ocr_pdf(path)

        return pages

    except:
        return ocr_pdf(path)


##extract data from llm for a page

def extract_from_page(page_text: str) -> dict:
    prompt = f"""
You are an AI system that extracts structured information from medical claim documents.

Extract the following fields from this page:

- Patient Name
- Contact Number
- Policy Number
- Provider Name (Insurance Company)
- Hospital Name
- Total Bill/claim Amount

Rules:
1. Return ONLY valid JSON.
2. If field not present on this page, return null.
3. No explanation.
4. No markdown.

Output format:

{{
  "patient_name": null,
  "contact_number": null,
  "policy_number": null,
  "provider_name": null,
  "hospital_name": null,
  "total_bill_amount": null
}}

Page Content:
\"\"\"
{page_text}
\"\"\"
"""
 
    response = llm.invoke(prompt)
    ##Extract JSON safely
    json_match = re.search(r'\{.*\}', response, re.DOTALL)
    if not json_match:
        return None

    try:
        data = json.loads(json_match.group())
        validated = ClaimSchema(**data)
        return validated.dict()
    except (json.JSONDecodeError, ValidationError):
        return None

def extract_pdf_pagewise(pdf_path: str):

    pages = load_pdf_pages(pdf_path)

    all_results = []

    for i, page in enumerate(pages):
        print(f"Processing page {i+1}/{len(pages)}...")
        result = extract_from_page(page)
        #print(result, "______")
        all_results.append({
            "page_number": i + 1,
            "extracted_data": result
        })

    return all_results


# -----------------------------
# RUN
# -----------------------------
if __name__ == "__main__":

    pdf_path = "data/sample_medical_claim.pdf"  # 🔹 Change this to your input path

    results = extract_pdf_pagewise(pdf_path)

    print("\nFinal Output:\n")
    print(json.dumps(results, indent=2))
