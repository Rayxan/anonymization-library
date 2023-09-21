import re

from pdfminer.high_level import extract_pages, extract_text

text = extract_text("example2.pdf")
# print(text)

pattern = re.compile(r'\d{3}\.\d{3}\.\d{3}-\d{2}')
matches = pattern.findall(text)

print(matches)