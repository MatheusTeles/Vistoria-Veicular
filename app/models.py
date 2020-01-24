from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), index=True)
    email = db.Column(db.String(128), index=True, unique=True)
    hash_senha = db.Column(db.String(128))

    def __repr__(self):
        return f'<Usuario {self.nome}>'

    def set_senha(self, senha: str):
        self.hash_senha = generate_password_hash(senha)

    def check_senha(self, senha: str):
        return check_password_hash(self.hash_senha, senha)


class Veiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(128), index=True)
    placa = db.Column(db.String(16), index=True, unique=True)
    km = db.Column(db.Integer)

    def __repr__(self):
        return f'<Veiculo {self.modelo} - {self.placa}>'


class Viagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    de = db.Column(db.String(128), index=True)
    para = db.Column(db.String(128), index=True)
    passageiros = db.Column(db.Integer)
    veiculo_id = db.Column(db.Integer, db.ForeignKey('veiculo.id'))
    veiculo = db.relationship("Veiculo", backref="viagens")
