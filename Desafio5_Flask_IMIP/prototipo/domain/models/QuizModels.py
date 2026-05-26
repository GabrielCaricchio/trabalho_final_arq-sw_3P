from datetime import datetime
from adapters.repositories.InterfaceDB import db

class Quiz(db.Model):
    __tablename__ = 'quizzes'

    id         = db.Column(db.Integer, primary_key=True)
    livro_id   = db.Column(db.Integer, db.ForeignKey('livros.id'), nullable=True)
    titulo     = db.Column(db.String(200), nullable=False)
    nivel      = db.Column(db.String(50))
    gerado_ia  = db.Column(db.Boolean, default=False)   
    criado_em  = db.Column(db.DateTime, default=datetime.utcnow)

    # Relacionamentos
    livro     = db.relationship('Livro',         back_populates='quizzes')
    questoes  = db.relationship('Questao',       back_populates='quiz', cascade='all, delete-orphan')
    progressos = db.relationship('Progresso',    back_populates='quiz')

    def __repr__(self):
        return f'<Quiz {self.titulo}>'
