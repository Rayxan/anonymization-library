from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='anonijojo-pt-br',
    version='0.0.1',
    license='MIT License',
    author='Raylan Sales and Stefano Luppi',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='raylanwork@gmail.com',
    keywords='anonimizador pt-br',
    description=u'Anonimizador pt-br',
    packages=['anonijojo_pt_br'],
    install_requires=['docx2txt==0.8', 'pdfminer.six==20221105'],)