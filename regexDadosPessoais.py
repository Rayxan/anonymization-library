import re

class RegexDadosPessoais:
    regexCPF = re.compile(r'\d{3}\.\d{3}\.\d{3}-\d{2}')