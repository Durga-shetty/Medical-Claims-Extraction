prompt = f"""
You are an AI system that extracts structured information from medical claim documents.

Extract the following fields from this page:

- Patient Name
- Contact Number
- Policy Number
- Provider Name (Insurance Company)
- Hospital Name
- Total Bill Amount

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
%s
\"\"\"
"""
