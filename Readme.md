# API de Personagens

Este projeto consiste em uma API para gerenciar personagens. Foi desenvolvida utilizando Flask, Flask-RESTPlus e SQLAlchemy.

## Funcionalidades Principais

- *Listar Personagens*: Endpoint para listar todos os personagens cadastrados.
- *Cadastrar Personagem*: Endpoint para cadastrar novos personagens.

## Como Executar

1. Clone este repositório.
2. Instale as dependências com o comando:
   
   pip install -r requirements.txt
   
3. Execute o arquivo app.py para iniciar o servidor Flask.
4. Acesse a API através do endereço http://localhost:5000.

## Documentação da API

A documentação da API está disponível no endpoint http://localhost:5000/swagger/.

## Modelo de Dados

A API utiliza o seguinte modelo de dados para os personagens:

- id: Identificador único do personagem (inteiro).
- nome: Nome do personagem (texto).
- descricao: Descrição do personagem (texto).
- link_imagem: Link da imagem do personagem (texto).
- programa: Programa ao qual o personagem pertence (texto).
- animador: Animador responsável pelo personagem (texto).

## Licença

Este projeto é licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT). Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.

---# desafio-api-personagens
# desafio-api-personagens
