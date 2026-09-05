# Corretor de Simulado

Projeto desenvolvido para automatizar a correção de um simulado a partir de arquivos Excel contendo o gabarito e as respostas dos alunos.

O projeto realiza o tratamento dos dados, compara as respostas com o gabarito, calcula o desempenho individual dos alunos e disponibiliza os resultados para análise em um dashboard desenvolvido no Power BI.

## 🎯 Objetivo

Desenvolver uma aplicação capaz de:

- Corrigir automaticamente as respostas dos alunos;
- Identificar respostas corretas, incorretas e sem resposta;
- Calcular o total de acertos e erros de cada aluno;
- Calcular o percentual de acertos individual;
- Calcular a média geral de acertos da turma;
- Gerar um arquivo Excel com os resultados detalhados;
- Disponibilizar os resultados para análise por meio de um dashboard no Power BI.

## 🛠️ Tecnologias utilizadas

- Python
- Pandas
- OpenPyXL
- Power BI
- Excel

## 📂 Estrutura do projeto

corretor_simulado/
│
├── data/
│   ├── Gabarito.xlsx
│   └── Respostas.xlsx
│
├── output/
│   └── resultado_simulado.xlsx
│
├── powerbi/
│   └── corretor_simulado.pbix
│
├── src/
│   └── corretor.py
│
├── .gitignore
├── README.md
└── requirements.txt

## 🔄 Funcionamento

O processo de correção segue as seguintes etapas:

1. Leitura dos arquivos de respostas dos alunos e do gabarito;
2. Padronização das respostas;
3. Validação das questões e dos dados recebidos;
4. Tratamento de registros duplicados;
5. Junção das respostas dos alunos com o gabarito;
6. Classificação de cada resposta como:
   - Correta
   - Incorreta
   - Sem resposta
7. Cálculo do desempenho individual dos alunos;
8. Geração do arquivo final com os resultados.

## 📊 Resultados

O arquivo `resultado_simulado.xlsx` possui duas abas principais:

### Desempenho_Alunos

Apresenta o resultado consolidado de cada aluno, incluindo:

- Total de acertos;
- Total de erros;
- Quantidade de questões sem resposta;
- Total de questões;
- Percentual de acertos.

### Correcao_Detalhada

Apresenta a correção questão por questão, contendo:

- Aluno;
- Questão;
- Resposta do aluno;
- Gabarito;
- Resultado da questão.

## 📈 Dashboard

Os resultados são utilizados em um dashboard desenvolvido no Power BI, permitindo visualizar:

- Média geral de acertos da turma;
- Média geral de acertos em percentual;
- Total de questões;
- Total de alunos;
- Desempenho individual dos alunos;
- Distribuição de respostas corretas, incorretas e sem resposta;
- Correção detalhada das questões por aluno.

## ▶️ Como executar

### 1. Instalar as dependências

Com o Python instalado, execute no terminal:

pip install -r requirements.txt

### 2. Verificar os arquivos de entrada

Os arquivos devem estar na pasta:

data/

com os nomes:

Gabarito.xlsx
Respostas.xlsx

### 3. Executar o corretor

A partir da pasta principal do projeto, execute:

python src/corretor.py

### 4. Verificar o resultado

Após a execução, o arquivo será gerado em:

output/resultado_simulado.xlsx

## 📌 Observações

O projeto foi desenvolvido com foco em automatizar o processo de correção e transformar os resultados em informações úteis para análise do desempenho dos alunos.