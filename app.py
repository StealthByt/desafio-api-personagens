from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api, Resource, fields

# Inicialização do aplicativo Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///personagens.db'
db = SQLAlchemy(app)

# Configuração da extensão Flask-RESTPlus
api = Api(app, version='1.0', title='API de Personagens', description='Uma API para gerenciar personagens')

# Definição do modelo Personagem
class Personagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    link_imagem = db.Column(db.String(200), nullable=False)
    programa = db.Column(db.String(100), nullable=False)
    animador = db.Column(db.String(100), nullable=False)

# Definição dos recursos da API
@api.route('/characters/')
class CharacterList(Resource):
    @api.doc('list_characters')
    def get(self):
        '''List all characters'''
        personagens = Personagem.query.all()
        return jsonify([personagem.__dict__ for personagem in personagens])

    @api.doc('create_character')
    @api.expect(api.model('Character', {
        'nome': fields.String(required=True, description='Nome do personagem'),
        'descricao': fields.String(required=True, description='Descrição do personagem'),
        'link_imagem': fields.String(required=True, description='Link da imagem do personagem'),
        'programa': fields.String(required=True, description='Programa do personagem'),
        'animador': fields.String(required=True, description='Animador do personagem'),
    }))
    def post(self):
        '''Create a new character'''
        data = request.json
        novo_personagem = Personagem(**data)
        db.session.add(novo_personagem)
        db.session.commit()
        return jsonify(novo_personagem.__dict__), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

