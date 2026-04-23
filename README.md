# Trabalho Prático 5 - Unidade 2

**Disciplina:** Resolução de Problemas com Grafos  
**Professor:** Ricardo Carubbi  

---

## 🔗 Link do Vídeo
[Acesse a demonstração aqui](https://drive.google.com/file/d/1OLTeTYT5Xlk6JTiWwXxAHUxasfTSvEzQ/view?usp=sharing)

---

## Grupo B

## 👥 Alunos
* Bernardo Pinheiro  
* Marcelo Kalsovik Junior  
* Guilherme Abrunheiro De Souza  

---

## 📌 Descrição do Projeto

Este projeto aplica a teoria dos grafos para resolver o problema de coloração do mapa político do Brasil. Utilizamos o algoritmo DSatur (Degree of Saturation) para garantir que nenhum estado brasileiro compartilhe a mesma cor com seus vizinhos de fronteira terrestre, buscando atingir o número cromático do grafo de forma eficiente.

### Funcionamento do DSatur:
1. **Grau de Saturação:** O sistema identifica qual estado está mais "pressionado" por vizinhos já coloridos. Por exemplo, se Minas Gerais (MG) tem vizinhos coloridos com Verde e Amarelo, sua saturação é 2. O algoritmo sempre colore primeiro quem tem a maior saturação.
2. **Critério de Desempate (Grau do Estado):** Em caso de empate, o algoritmo escolhe o estado com mais fronteiras terrestres no total (maior grau). Isso ajuda a reduzir conflitos rapidamente em regiões densas como o Sudeste e Nordeste.
3. **Atribuição de Cores Nominais:** Diferente de implementações básicas que usam números (1, 2, 3), este projeto atribui nomes de cores reais (Verde, Amarelo, Azul, etc.), facilitando a visualização e interpretação do resultado final.

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
