from datetime import datetime
from adapters.repositories.InterfaceDB import db

class Escola(db.Model):
    __tablename__ = 'escolas'

    id        = db.Column(db.Integer, primary_key=True)
    nome      = db.Column(db.String(150), nullable=False)
    cidade    = db.Column(db.String(100))
    estado    = db.Column(db.String(2))           
    ativa     = db.Column(db.Boolean, default=True)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    # Relacionamentos
    professores = db.relationship('ProfessorEscola', back_populates='escola')
    turmas      = db.relationship('Turma',           back_populates='escola')

    def __repr__(self):
        return f'<Escola {self.nome}>'
