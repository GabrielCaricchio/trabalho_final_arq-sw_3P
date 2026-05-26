from datetime import datetime
from adapters.repositories.InterfaceDB import db

class Livro(db.Model):
    __tablename__ = 'livros'

    id          = db.Column(db.Integer, primary_key=True)
    titulo      = db.Column(db.String(200), nullable=False)
    autor       = db.Column(db.String(150))
    nivel       = db.Column(db.String(50))          
    num_paginas = db.Column(db.Integer)
    capa_url    = db.Column(db.String(300))          
    pdf_url     = db.Column(db.String(300))          
    descricao   = db.Column(db.Text)
    ativo       = db.Column(db.Boolean, default=True)
    criado_em   = db.Column(db.DateTime, default=datetime.utcnow)

    # Relacionamentos
    quizzes    = db.relationship('Quiz',      back_populates='livro')
    progressos = db.relationship('Progresso', back_populates='livro')

    def __repr__(self):
        return f'<Livro {self.titulo}>'
