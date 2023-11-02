import re
from pdfminer.high_level import extract_text
from docx import Document
from regexDadosPessoais import RegexDadosPessoais
import pandas as pd

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
    
    def anonimiza_docx(self, arquivo, flag):
        document = Document(arquivo)

        # Regex referente ao formato do dado escolhido
        pattern = self.retorna_pattern(flag)
        
        for paragraph in document.paragraphs:
            paragraph.text = re.sub(pattern, '#########', paragraph.text)
        document.save(arquivo)
    
    def anonimiza_xlsx(self, arquivo, flag):

        pattern = self.retorna_pattern(flag)
        text = pd.read_excel(arquivo)
        text = text.apply(lambda x: x if x.dtype != 'object' else x.str.replace(pattern,'#########', regex=True))
        text.to_excel(arquivo, index=False)

        print(text)


        
        
# Criando uma instância da classe e chamando métodos

teste = input()

Anonimizador().anonimiza_xlsx("teste.xlsx", teste)