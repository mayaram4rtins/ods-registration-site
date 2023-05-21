from main import db

class User(db.Model):
    _tablename='cadastro_usuario'
    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(14), nullable=False)
    telefone = db.Column(db.String(19), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


class Projetos(db.Model):
    id_proj = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('cadastro_usuario.id_user'), nullable=False)
    desc = db.Column(db.String(150), nullable=False)
    telefone = db.Column(db.String(19), nullable=False)
    data_cadastro = db.Column(db.DateTime(), nullable=False)
    status_projeto = db.Column(db.String(19), nullable=False)
    tag = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name