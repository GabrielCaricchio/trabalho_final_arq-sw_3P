from datetime import datetime
from adapters.repositories.InterfaceDB import db

class Conteudo(db.Model):
    __tablename__ = 'conteudos'

    id          = db.Column(db.Integer, primary_key=True)
    titulo      = db.Column(db.String(200), nullable=False)
    tipo        = db.Column(db.String(30),  nullable=False)   
    nivel       = db.Column(db.String(50))                   
    descricao   = db.Column(db.Text)
    url_arquivo = db.Column(db.String(300))                   
    ativo       = db.Column(db.Boolean, default=True)
    criado_em   = db.Column(db.DateTime, default=datetime.utcnow)

    # Relacionamentos
    progressos = db.relationship('Progresso', back_populates='conteudo')

    def __repr__(self):
        return f'<Conteudo {self.titulo} | {self.tipo}>'
