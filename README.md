python-anonimiza-pt-br
============

python-anonimiza-pt-br é uma biblioteca para a linguagem de programação python, que permite o desenvolvedor criar códigos capazes de anonimizar dados pessoais brasileiros presentes em arquivos pdf, docx, xlsx, assim como strings.

Ferramentas
--------
* Anonimizar dados pessoais brasileiros dentro de um arquivo PDF. 
* Anonimizar dados pessoais brasileiros dentro de um arquivo DOCX. 
* Anonimizar dados pessoais brasileiros dentro de um arquivo XLSX.
* Anonimizar dados pessoais brasileiros em um texto do tipo String.

Como utilizar
----------

* Intale o Python 3.6 ou atual.

* Instale e/ou atualize o pip, setuptools e wheel.

  `pip install wheel setuptools pip --upgrade`

*  Instale a versão mais atual do docx2txt

    `pip install docx2txt`
   
*  Instale a biblioteca python-anonimiza-pt-br

    `pip install -i https://test.pypi.org/simple/ python-anonimiza-pt-br==0.0.1`

* Utilizando no código. 

```python
from python_anonimiza_pt_br import Anonimizador

texto_gerado = Anonimizador().anonimiza_docx2txt("exemplo.docx", "CPF")

print(texto_gerado)
```
