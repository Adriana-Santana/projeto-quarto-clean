# 🛏️ Projeto Cálculo do Quarto - Versão 2.0

Este é um projeto desenvolvido em **Python** integrado com um banco de dados **SQLite**. O sistema foi criado para ajudar no planejamento de uma reforma de quarto, calculando a ocupação de espaço nas paredes e organizando onde cada móvel será alocado.

## 🚀 Funcionalidades
- **Criação de Banco de Dados:** Criação automática da tabela de móveis usando `CREATE TABLE IF NOT EXISTS`.
- **Limpeza Automática:** Sistema inteligente que limpa os dados antigos com `DELETE FROM` antes de rodar, evitando registros duplicados.
- **Cálculo de Espaço:** Soma a largura de todos os móveis e valida se eles ultrapassam o limite disponível na parede principal.
- **Relatório de Paredes:** Varre o banco de dados usando `SELECT` e exibe um relatório organizado mostrando em qual parede (A, B ou C) cada móvel foi planejado.

## 🛠️ Tecnologias Utilizadas
- **Python 3**
- **SQLite3** (Banco de dados relacional leve)

## 📌 Aprendizados (Faculdade & Portfólio)
Nesta versão do projeto, os principais conceitos aplicados foram:
1. Conexão e manipulação de bancos de dados via código.
2. Comandos SQL essenciais: `CREATE`, `INSERT`, `DELETE` e `SELECT`.
3. Estruturas de repetição (`for`) em Python para gerar relatórios dinâmicos a partir de dados do banco.