import re

class RegexDadosPessoais:
    regexCPF = re.compile(r'(?<!\d)\d{3}\.\d{3}\.\d{3}-\d{2}(?!\d)')

    regexTelef = re.compile(r'(?<!\d)\(\d{2}\)[ ]*\d{5}\-\d{4}(?!\d)')

    regexData = re.compile(r'(?<!\d)\d{2}/\d{2}/\d{4}(?!\d)')

    regexCEP = re.compile(r'(?<!\d)\d{5}\-\d{3}(?!\d)')

    regexEmail = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')