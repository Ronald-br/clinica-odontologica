# Sistema de Gestão Odontológica 🦷

Sistema web desenvolvido para auxiliar na gestão de uma clínica odontológica, permitindo o cadastro e a visualização de informações básicas, como pacientes, dentistas, consultas e pagamentos.

Este projeto foi desenvolvido com foco na aplicação dos conceitos de **Arquitetura de Software em Camadas**, conforme proposto na disciplina de Arquitetura de Sistemas.

---

## 📋 Descrição Geral

O sistema tem como objetivo organizar informações essenciais de uma clínica odontológica, oferecendo funcionalidades básicas para cadastro e consulta de dados, de forma simples e estruturada.

A aplicação foi dividida em **front-end**, **back-end** e **camada de persistência**, evitando uma solução monolítica e garantindo melhor organização do código.

---

## ✅ Requisitos Funcionais

- Cadastrar pacientes;
- Listar pacientes;
- Cadastrar dentistas;
- Listar dentistas;
- Cadastrar consultas;
- Listar consultas;
- Cadastrar pagamentos;
- Listar pagamentos.

---

## ⚙️ Requisitos Não Funcionais

- Utilização de arquitetura de software em camadas;
- Separação entre interface, regras de negócio e persistência de dados;
- Código organizado e de fácil manutenção;
- Comunicação entre front-end e back-end via API REST.

---

## 🧱 Arquitetura do Sistema

O sistema adota uma **Arquitetura em Camadas**, composta por:

- **Camada de Apresentação (Front-end):**  
  Responsável pela interface com o usuário e pelo consumo da API REST.

- **Camada de Aplicação / Negócio (Back-end):**  
  Responsável pelo processamento das requisições e aplicação das regras do sistema.

- **Camada de Persistência de Dados:**  
  Responsável pelo armazenamento e recuperação das informações no banco de dados.

Essa arquitetura foi escolhida para garantir **baixo acoplamento**, **alta coesão** e **facilidade de manutenção**.

---

## 🧩 Diagrama Simplificado da Arquitetura

Front-end (HTML + JavaScript)  
&nbsp;&nbsp;&nbsp;&nbsp;↓  
API REST (Flask)  
&nbsp;&nbsp;&nbsp;&nbsp;↓  
Services  
&nbsp;&nbsp;&nbsp;&nbsp;↓  
Repositories  
&nbsp;&nbsp;&nbsp;&nbsp;↓  
Banco de Dados (SQLite)

---

## 🛠️ Tecnologias Utilizadas

### Back-end
- Python 3
- Flask
- Flask-CORS

### Front-end
- HTML
- JavaScript

### Banco de Dados
- SQLite

---

## 📁 Estrutura de Pastas

