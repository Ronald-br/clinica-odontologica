# Sistema Clínica Odontológica - Containerização com Docker

## Visão Geral do Projeto

Este projeto foi desenvolvido como atividade da disciplina de Arquitetura de Sistemas. A proposta consiste em organizar a aplicação em containers utilizando Docker, permitindo que o sistema seja executado de forma padronizada em diferentes ambientes.

A aplicação representa um sistema simples de clínica odontológica.

Tecnologias utilizadas:

- HTML
- CSS
- JavaScript
- Docker
- Docker Compose
- Nginx

---

## Explicação do Dockerfile

O Dockerfile foi criado para definir o ambiente necessário para executar a aplicação dentro de um container.

Principais instruções utilizadas:

- FROM: define a imagem base utilizada (nginx), responsável por servir arquivos web.
- WORKDIR: define o diretório de trabalho dentro do container.
- COPY: copia os arquivos do projeto para dentro do container.
- EXPOSE: indica a porta utilizada pela aplicação.
- CMD: define o comando inicial responsável por iniciar o servidor nginx.

---

## Explicação do Docker Compose

O arquivo docker-compose.yml foi utilizado para facilitar a execução da aplicação.

Serviços configurados:

- app: responsável pela construção da imagem e execução do container.

Configurações:

- Mapeamento de portas para permitir acesso externo à aplicação.

---

## Funcionamento da Aplicação no Docker

A aplicação é iniciada através do Docker utilizando o servidor nginx. Após iniciar o container, o sistema pode ser acessado pelo navegador através da porta configurada.

A principal diferença entre a execução local e via Docker é que, utilizando containers, o ambiente fica isolado e padronizado, evitando problemas de configuração.

---

## Comandos Utilizados

Para executar o projeto, siga os passos abaixo:

1️⃣ Certifique-se de que o Docker esteja instalado na máquina.

2️⃣ Clone o repositório:

git clone https://github.com/Ronald-br/clinica-odontologica.git

3️⃣ Acesse a pasta do projeto:

cd clinica-odontologica

4️⃣ Execute o comando abaixo para construir a imagem e iniciar o container:

docker-compose up --build

5️⃣ Após a inicialização, acesse no navegador:

http://localhost:8080

Para encerrar a execução do container, utilize:

docker-compose down

