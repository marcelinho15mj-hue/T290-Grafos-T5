# Trabalho Prático 5 - Unidade 2

**Disciplina:** Resolução de Problemas com Grafos  
**Professor:** Ricardo Carubbi  

---

## 🔗 Link do Vídeo
[Acesse a demonstração aqui](https://drive.google.com/file/d/1OLTeTYT5Xlk6JTiWwXxAHUxasfTSvEzQ/view?usp=sharing)

---

## 👥 Alunos
* Bernardo Pinheiro  
* Marcelo Kalsovik Junior  
* Guilherme Abrunheiro De Souza  

---

## 📌 Descrição do Projeto

Este projeto implementa o algoritmo **DSatur (Degree of Saturation)** para a resolução do problema de **Coloração de Grafos**. 

O objetivo é atribuir uma cor a cada vértice de um grafo de forma que dois vértices adjacentes nunca compartilhem a mesma cor, buscando minimizar o número total de cores utilizadas através de uma abordagem heurística.

### Funcionamento do DSatur:
1. **Grau de Saturação:** O algoritmo seleciona o próximo vértice a ser colorido com base no número de cores diferentes já presentes em seus vizinhos.
2. **Critério de Desempate:** Caso haja empate na saturação, escolhe-se o vértice com o maior grau no grafo original.
3. **Atribuição de Cores:** O vértice recebe a primeira cor disponível de uma lista predefinida (Verde, Amarelo, Azul, Branco, etc.).

---

## Como executar

Execute o programa: py src/main.py dados/brasil.txt

## 📁 Estrutura do Projeto

```text
T5/
├── README.md              
├── dados/
│   └── brasil.txt         
└── src/
    ├── main.py            
    ├── dsatur.py         
    └── graph.py 
