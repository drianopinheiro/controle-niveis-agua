# Controle de Níveis de Água

## 📚 Atividade

**Agenda 11 - Desenvolvimento de Sistemas I**

Atividade desenvolvida para o curso de **Técnico em Desenvolvimento de Sistemas – ETEC**.

🔗 **Agenda 11:** Controle de Níveis de Água

## 📌 Sobre o projeto

Este projeto foi desenvolvido em **Python** para simular o monitoramento dos níveis de água de um reservatório.

O programa exibe mensagens de alerta no terminal com cores diferentes, de acordo com o nível de água do reservatório, utilizando a biblioteca **Colorama**.

## 🎯 Objetivo

O objetivo do projeto é praticar conceitos básicos de programação, principalmente:

* Listas
* Funções
* Estruturas de decisão `if`
* Estruturas de repetição `for`
* Importação e utilização de bibliotecas
* Exibição de mensagens no terminal

## 📝 Níveis do reservatório

O sistema trabalha com cinco níveis de água:

| Nível | Situação | Cor |
|---|---|---|
| 1 | Muito baixo (crítico) | Vermelho |
| 2 | Baixo | Amarelo |
| 3 | Médio | Verde |
| 4 | Alto | Ciano |
| 5 | Muito alto (alerta) | Azul |

## ⚙️ Funcionamento

O programa armazena os níveis e suas respectivas situações em uma lista.

Uma função define a cor da mensagem conforme o nível informado. Outra função exibe o alerta correspondente no terminal.

A simulação percorre os cinco níveis do reservatório, exibindo cada situação com sua respectiva cor e restaurando o estilo padrão do terminal após cada mensagem.

## 🧪 Teste

Foi realizada uma simulação com os cinco níveis do reservatório para verificar se as mensagens são exibidas corretamente e se cada nível recebe a cor correspondente.

## 💻 Tecnologias utilizadas

* Python
* Biblioteca Colorama
* Visual Studio Code
* Git
* GitHub

## 📂 Estrutura do projeto

```text
controle-niveis-agua/
│
├── main.py
├── requirements.txt
└── README.md
```

## 👨‍💻 Autor


Projeto desenvolvido para atividade acadêmica de **Desenvolvimento de Sistemas I – ETEC**.
