import aspose.pdf as pdf
import re
# Load License
#license = pdf.License()
#license.set_license("Aspose.Total.lic")

# Open the PDF document
inputPDFFile = pdf.Document("example2.pdf")

# Instantiate a TextFragmentAbsorber object
# reg = re.compile(r'\d{3}\.\d{3}\.\d{3}-\d{2}')
txtAbsorber = pdf.text.TextFragmentAbsorber("marco")

# Search text
inputPDFFile.pages.accept(txtAbsorber)

# Get reference to the found list
textFragmentCollection = txtAbsorber.text_fragments

# Parse all the searched text fragments
for txtFragment in textFragmentCollection:
    txtFragment.text = "*"

# Save the output PDF
inputPDFFile.save("output.pdf")

print("Text found and replaced successfully")