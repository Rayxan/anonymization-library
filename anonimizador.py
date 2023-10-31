import re
from pdfminer.high_level import extract_text
from regexDadosPessoais import RegexDadosPessoais 

class Anonimizador:
    def __init__(self):
        self.dados = []

    def anonimiza_texto(self, arquivo, flag):
        # extraindo o texto do arquivo pdf passado
        text = extract_text(arquivo)

        # Regex referente ao formato do dado escolhido
        if flag == 'CPF':
            pattern = RegexDadosPessoais.regexCPF
        elif flag == 'Telefone':
            pattern = RegexDadosPessoais.regexTelef
        elif flag == 'Data':
            pattern = RegexDadosPessoais.regexData
        elif flag == 'CEP':
            pattern = RegexDadosPessoais.regexCEP
        elif flag == 'Email':
            pattern = RegexDadosPessoais.regexEmail
        
        text =  re.sub(pattern, '#########', text)

        return text
        
# Criando uma instância da classe e chamando métodos

teste = input()

texto = Anonimizador().anonimiza_texto("exemplo.pdf", teste)

print(texto)