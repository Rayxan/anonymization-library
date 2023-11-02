import re
from pdfminer.high_level import extract_text
import docx2txt
from regexDadosPessoais import RegexDadosPessoais 

class Anonimizador:
    def __init__(self):
        self.dados = []

    def retorna_pattern(self, flag):
        if flag == 'CPF':
            return  RegexDadosPessoais.regexCPF
        elif flag == 'Telefone':
            return RegexDadosPessoais.regexTelef
        elif flag == 'Data':
            return RegexDadosPessoais.regexData
        elif flag == 'CEP':
            return RegexDadosPessoais.regexCEP
        elif flag == 'Email':
            return RegexDadosPessoais.regexEmail

    def anonimiza_pdf(self, arquivo, flag):
        # extraindo o texto do arquivo pdf passado
        text = extract_text(arquivo)

        # Regex referente ao formato do dado escolhido
        pattern = self.retorna_pattern(flag)
        
        text =  re.sub(pattern, '#########', text)

        return text

    def anonimiza_string(self, text, flag):
        # Regex referente ao formato do dado escolhido
        pattern = self.retorna_pattern(flag)
        
        text =  re.sub(pattern, '#########', text)

        return text
    
    def anonimiza_docx2txt(self, arquivo, flag):
        # Regex referente ao formato do dado escolhido
        pattern = self.retorna_pattern(flag)

        # Extrair texto de um arquivo .docx
        text = docx2txt.process(arquivo)

        text = re.sub(pattern, '#########', text)

        return text
        
        
# Criando uma instância da classe e chamando métodos

teste = input()

print(Anonimizador().anonimiza_docx2txt("exemplo.docx", teste))