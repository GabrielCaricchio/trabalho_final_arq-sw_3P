from datetime import datetime
from adapters.repositories.InterfaceDB import db

class Turma(db.Model):
    __tablename__ = 'turmas'

    id           = db.Column(db.Integer, primary_key=True)
    nome         = db.Column(db.String(100), nullable=False)   # Ex: 'Turma A - Nível 1'
    nivel        = db.Column(db.String(50))                    # Ex: 'Pré-Silábico', '1º Ano'
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'))
    escola_id    = db.Column(db.Integer, db.ForeignKey('escolas.id'))
    ativa        = db.Column(db.Boolean, default=True)
    criado_em    = db.Column(db.DateTime, default=datetime.utcnow)

    # Relacionamentos
    professor = db.relationship('Professor', back_populates='turmas')
    escola    = db.relationship('Escola',    back_populates='turmas')
    alunos    = db.relationship('Aluno',     back_populates='turma_obj')

    def __repr__(self):
        return f'<Turma {self.nome}>'
