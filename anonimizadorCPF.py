import aspose.pdf as pdf
from pdfminer.high_level import extract_text
from regexDadosPessoais import RegexDadosPessoais 

class AnonimizadorCPF:
    def __init__(self):
        self.cpfs = []

    def extrair_cpf_pdf(self, arquivo):
        # Usando a biblioteca pdfminer para ler e extrair CPFs do PDF
        text = extract_text(arquivo)

        # Regex referente ao formato do CPF
        pattern = RegexDadosPessoais.regexCPF
        cpfs = pattern.findall(text)
        
        return self.cpfs.extend(cpfs)

        # self.substituir_cpf_pdf(arquivo)

    def substituir_cpf_pdf(self, arquivo):

        extrair_cpf_pdf(arquivo)

        # Usando a biblioteca aspose.pdf para ler o PDF e fazer a substituição
        primeiro_loop = True
        contadorCpf = 0
        total_cpfs = len(self.cpfs)

        for cpf in self.cpfs:
            # Documento PDF é aberto
            # Condição criada para atualizar o documento a cada loop
            if(primeiro_loop):
                inputPDFFile = pdf.Document(arquivo)
                primeiro_loop = False
            else:
                inputPDFFile = pdf.Document("arquivoAnonimizado.pdf") 

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
                txtFragment.text = "###.###.###-##"

            # Salva em um novo pdf
            inputPDFFile.save("arquivoAnonimizado.pdf")

            contadorCpf += 1
            if contadorCpf == total_cpfs:
                print(str(contadorCpf) + " CPFs encontrados e substituídos com sucesso.")
        
# Criando uma instância da classe e chamando métodos
AnonimizadorCPF().extrair_cpf_pdf("exemplo.pdf")
