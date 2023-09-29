import aspose.pdf as pdf
from pdfminer.high_level import extract_text
from regexDadosPessoais import RegexDadosPessoais 

class AnonimizadorCPF:
    def __init__(self):
        self.dados = []

    def anonimiza_pdf(self, arquivo, flag):
        # Usando a biblioteca pdfminer para ler e extrair dados do PDF
        text = extract_text(arquivo)

        # Regex referente ao formato do dado escolhido
        if flag == '1':
            pattern = RegexDadosPessoais.regexCPF
        elif flag == '2':
            pattern = RegexDadosPessoais.regexTelef
        elif flag == '3':
            pattern = RegexDadosPessoais.regexData
        elif flag == '4':
            pattern = RegexDadosPessoais.regexCEP
        elif flag == '5':
            pattern = RegexDadosPessoais.regexEmail
        
        dados = pattern.findall(text)
        print(dados)
        self.dados.extend(dados)

        self.substituir_pdf(arquivo)

    def substituir_pdf(self, arquivo):
        # Usando a biblioteca aspose.pdf para ler o PDF e fazer a substituição

        for dado in self.dados:
            # Documento PDF é aberto
            # Condição criada para atualizar o documento a cada loop
            
            inputPDFFile = pdf.Document(arquivo) 

            # Objeto TextFragmentAbsorber é instanciado
            txtAbsorber = pdf.text.TextFragmentAbsorber(dado)
            
            # Procura texto no documento PDF (não sei que comentário utilizar aqui)
            # A função "accept" recebe o objeto "txtAbsorber" como parâmetro, o qual retorna uma coleção de objetos "TextFragment".
            inputPDFFile.pages.accept(txtAbsorber)

            # Obtém uma referência à lista de fragmentos de texto encontrados
            textFragmentCollection = txtAbsorber.text_fragments

            # Analisa todos os fragmentos de texto encontrados
            for txtFragment in textFragmentCollection:
                # Substitui o texto encontrado
                txtFragment.text = "###########"

            # Salva em um novo pdf
            inputPDFFile.save(arquivo)
        
# Criando uma instância da classe e chamando métodos

teste = input()

AnonimizadorCPF().anonimiza_pdf("exemplo.pdf", teste)