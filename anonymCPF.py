import aspose.pdf as pdf
import re
from pdfminer.high_level import extract_text

# Usando a biblioteca pdfminer para ler e extrair CPFs do PDF
text = extract_text("example2.pdf")

# Regex referente ao formato do CPF
pattern = re.compile(r'\d{3}\.\d{3}\.\d{3}-\d{2}')
cpfs = pattern.findall(text)

# Usando a biblioteca aspose.pdf para ler o PDF e fazer a substituição
first_loop = True
for cpf in cpfs:
    # Documento PDF é aberto
    # Condição criada para atualizar o documento a cada loop
    if(first_loop):
        inputPDFFile = pdf.Document("example2.pdf")
        first_loop = False
    else:
        inputPDFFile = pdf.Document("output.pdf") 

    # Objeto TextFragmentAbsorber é instanciado
    txtAbsorber = pdf.text.TextFragmentAbsorber(cpf)

    # Procura texto no documento PDF (não sei que comentário utilizar aqui)
    # A função "accept" recebe o objeto "txtAbsorber" como parâmetro, o qual retorna uma coleção de objetos "TextFragment".
    inputPDFFile.pages.accept(txtAbsorber)

    # Obtém uma referência à lista de fragmentos de texto encontrados
    textFragmentCollection = txtAbsorber.text_fragments

    # Analisa todos os fragmentos de texto encontrados
    for txtFragment in textFragmentCollection:
        # Substitui o texto encontrado
        txtFragment.text = "***.***.***-**"

    # Salva em um novo pdf
    inputPDFFile.save("output.pdf")

    print("Texto encontrado e substituído com sucesso")