# Projeto: Front-end com Vue.js e Back-end com Python usando a biblioteca DeepFace
Este repositório contém um projeto empolgante que combina o poderoso front-end do Vue.js com um sólido back-end em Python, usando a biblioteca DeepFace para reconhecimento facial e análise de atributos faciais, como idade, gênero, emoção e raça.

## Descrição do Projeto
O objetivo deste projeto é criar uma interface web interativa que permita aos usuários enviar suas fotos para análise utilizando a tecnologia avançada do DeepFace. Por meio da integração do Vue.js no front-end e Python no back-end, oferecemos aos usuários uma experiência intuitiva e amigável ao interagir com o sistema de reconhecimento facial.

## Funcionalidades Principais
Interface de Usuário Amigável: O front-end desenvolvido com Vue.js proporciona uma interface web fácil de usar, onde os usuários podem enviar suas fotos com apenas alguns cliques.

## Reconhecimento Facial Avançado: 
O back-end, construído em Python, utiliza a biblioteca DeepFace para realizar o reconhecimento facial e extrair atributos faciais como idade, gênero, emoção e raça.

## Processamento Eficiente: 
A biblioteca DeepFace é conhecida por sua eficiência e precisão, o que garante resultados confiáveis em tempo hábil.

## Links

## VueJs:
https://vuejs.org/guide/introduction.html

## QuasarJs:
https://quasar.dev/start/vue-cli-plugin#introduction

## Python:
Pré-requisitos: Certifique-se de ter o Python instalado em seu sistema.

https://www.python.org/downloads/
OBS: Na pasta back tem um arquivo "guia.ipynb" com os comandos para instalações no projeto.

## DeepFace:
https://github.com/serengil/deepface/tree/master

## Como Executar o Projeto Front
``` bash
cd front && yarn install 

```
``` bash
cd front && yarn serve
```

## Como Executar o Projeto back
``` bash
cd back &&  uvicorn api:app --reload
