import re

class RegexDadosPessoais:
    regexCPF = re.compile(r'\d{3}\.\d{3}\.\d{3}-\d{2}')

    regexTelef = re.compile(r'[(]\d{2}[)][ ]*\d{4}|\d{5}-\d{4}')

    regexData = re.compile(r'\d{2}[/]\d{2}[/]\d{2}|\d{4}')

    regexCEP = re.compile(r'\d{5}[-]\d{3}')

    regexEmail = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')