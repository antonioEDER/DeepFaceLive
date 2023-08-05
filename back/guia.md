# Guia de instalação

- Doc. Instalação Py (https://www.python.org/downloads/)
- GIT (https://github.com/serengil/deepface/tree/master)
- Documentação (https://pypi.org/project/deepface/)

### Instalar o Python p/ MAC:
```
brew install python3@3.8.1"
```
### Instalar o Python p/ Linux:
```
apt install python3.8
```
### Validar versão do pip (gerenciador de pacotes Python)
```
pip3 --version
```
### Instalar bibliotecas do projeto
```
pip3 install deepface
pip3 install  deepface fastapi uvicorn numpy
```
### Clonar o repositório na raiz da pasta back
```
git clone https://github.com/serengil/deepface/tree/master
```
### Comando para rodar a API (Deve ser executado na raiz da pasta back)
```
uvicorn api:app --reload
```