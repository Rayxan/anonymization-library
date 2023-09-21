import aspose.pdf as pdf
import re

from pdfminer.high_level import extract_pages, extract_text

text = extract_text("example2.pdf")
# print(text)

pattern = re.compile(r'\d{3}\.\d{3}\.\d{3}-\d{2}')
matches = pattern.findall(text)

print(matches)

###########################################################

for match in matches:
    # Open the PDF document
    inputPDFFile = pdf.Document("example2.pdf")

    # Instantiate a TextFragmentAbsorber object
    # matches[0] has the first CPF
    txtAbsorber = pdf.text.TextFragmentAbsorber(match)

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

##########################################################################
# # VERSÃO SEM O FOREACH 
# # (DESCOMENTAR ESSE E COMENTAR A DE CIMA A PARTIR DO FOREACH (LINHAS 16 A 37))

# # Open the PDF document
# inputPDFFile = pdf.Document("example2.pdf")

# # Instantiate a TextFragmentAbsorber object
# # matches[0] has the first CPF
# txtAbsorber = pdf.text.TextFragmentAbsorber(matches[0])

# # Search text
# inputPDFFile.pages.accept(txtAbsorber)

# # Get reference to the found list
# textFragmentCollection = txtAbsorber.text_fragments

# # Parse all the searched text fragments
# for txtFragment in textFragmentCollection:
#     txtFragment.text = "*"

# # Save the output PDF
# inputPDFFile.save("output.pdf")

# print("Text found and replaced successfully")