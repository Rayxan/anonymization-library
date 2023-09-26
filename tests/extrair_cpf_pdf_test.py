from anonimizadorCPF import AnonimizadorCPF

def test_extrair_cpfs():
    anonimizador = AnonimizadorCPF()
    texto = "Exemplo de CPFs: 123.456.789-00, 987.654.321-00"
    cpfs = anonimizador.extrair_cpf_pdf(texto)
    assert cpfs == ["123.456.789-00", "987.654.321-00"]

# def test_anonimizar_cpf():
#     anonimizador = AnonimizadorCPF()
#     anonimizador.cpfs = ["123.456.789-00", "987.654.321-00"]
#     texto = "Exemplo de CPFs: 123.456.789-00, 987.654.321-00"
#     texto_anonimizado = anonimizador.anonimizar_cpf(texto)
#     assert texto_anonimizado == "Exemplo de CPFs: ###.###.###-##, ###.###.###-##"
