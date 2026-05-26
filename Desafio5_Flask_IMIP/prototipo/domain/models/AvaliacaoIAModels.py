from datetime import datetime
from adapters.repositories.InterfaceDB import db

class AvaliacaoIA(db.Model):
    __tablename__ = 'avaliacao_ia'

    id             = db.Column(db.Integer, primary_key=True)
    aluno_id       = db.Column(db.Integer, db.ForeignKey('alunos.id'), nullable=False)
    nivel_detectado = db.Column(db.String(50))       
    relatorio      = db.Column(db.Text)              
    sugestoes      = db.Column(db.Text)              
    modelo_ia      = db.Column(db.String(100))       
    criado_em      = db.Column(db.DateTime, default=datetime.utcnow)

    # Relacionamentos
    aluno = db.relationship('Aluno', back_populates='avaliacoes')

    def __repr__(self):
        return f'<AvaliacaoIA aluno={self.aluno_id} | {self.criado_em.date()}>'
