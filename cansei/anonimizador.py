import re
from pdfminer.high_level import extract_text
import docx2txt

class Anonimizador:
    def __init__(self):
        self.dados = []

    def retorna_pattern(self, flag):
        if flag == 'CPF':
            regexCPF = re.compile(r'(?<!\d)\d{3}\.\d{3}\.\d{3}-\d{2}(?!\d)')
            return regexCPF

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