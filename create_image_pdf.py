from fpdf import FPDF
from PIL import Image, ImageDraw, ImageFont

# ---------------------------
# Step 1: Create the claim image
# ---------------------------
img = Image.new('RGB', (600, 400), color=(255, 255, 255))
d = ImageDraw.Draw(img)

# Load a font (default if Arial not found)
try:
    font = ImageFont.truetype("arial.ttf", 16)
except:
    font = ImageFont.load_default()

# Add medical claim details
d.text((20, 20), "Medical Claim Document", fill=(0,0,0), font=font)
d.text((20, 60), "Patient Name: Rahul Sharma", fill=(0,0,0), font=font)
d.text((20, 90), "Contact Number: +91-9876543210", fill=(0,0,0), font=font)
d.text((20, 120), "Policy Number: POL123456789", fill=(0,0,0), font=font)
d.text((20, 150), "Provider Name: ABC Health Insurance Pvt Ltd", fill=(0,0,0), font=font)
d.text((20, 180), "Hospital Name: City Care Hospital", fill=(0,0,0), font=font)
d.text((20, 210), "Total Bill: 84,500", fill=(0,0,0), font=font)

# Save image
image_path = "sample_medical_claim.png"
img.save(image_path)

# ---------------------------
# Step 2: Convert image to PDF
# ---------------------------
pdf = FPDF()
pdf.add_page()
pdf.image(image_path, x=10, y=10, w=180)  # fit the image in PDF page
pdf_path = "sample_medical_claim.pdf"
pdf.output(pdf_path)

print(f"PDF saved as: {pdf_path}")
