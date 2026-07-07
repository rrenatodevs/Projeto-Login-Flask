from flask import Flask, request, jsonify, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Usuario

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.config["SECRET_KEY"] = "troque-essa-chave-depois"

db.init_app(app)

with app.app_context():
    db.create_all()  # cria o arquivo banco.db e a tabela na primeira vez que rodar


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/cadastro", methods=["POST"])
def cadastro():
    dados = request.get_json()
    nome = dados.get("nome")
    email = dados.get("email")
    senha = dados.get("senha")

    if not nome or not email or not senha:
        return jsonify({"erro": "Preencha todos os campos"}), 400

    if Usuario.query.filter_by(email=email).first():
        return jsonify({"erro": "Email já cadastrado"}), 409

    novo_usuario = Usuario(
        nome=nome,
        email=email,
        senha_hash=generate_password_hash(senha)
    )
    db.session.add(novo_usuario)
    db.session.commit()

    return jsonify({"mensagem": "Cadastro realizado com sucesso!"}), 201


@app.route("/api/login", methods=["POST"])
def login():
    dados = request.get_json()
    email = dados.get("email")
    senha = dados.get("senha")

    usuario = Usuario.query.filter_by(email=email).first()

    if not usuario or not check_password_hash(usuario.senha_hash, senha):
        return jsonify({"erro": "Email ou senha incorretos"}), 401

    return jsonify({"mensagem": f"Bem-vindo, {usuario.nome}!"}), 200


if __name__ == "__main__":
    app.run(debug=True)