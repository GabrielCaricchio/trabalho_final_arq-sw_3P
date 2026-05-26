from datetime import datetime
from adapters.repositories.InterfaceDB import db

class Progresso(db.Model):
    __tablename__ = 'progresso'

    id           = db.Column(db.Integer, primary_key=True)
    aluno_id     = db.Column(db.Integer, db.ForeignKey('alunos.id'),    nullable=False)
    conteudo_id  = db.Column(db.Integer, db.ForeignKey('conteudos.id'), nullable=True)
    livro_id     = db.Column(db.Integer, db.ForeignKey('livros.id'),    nullable=True)
    quiz_id      = db.Column(db.Integer, db.ForeignKey('quizzes.id'),   nullable=True)
    status       = db.Column(db.String(30), default='iniciado')
    # Status: 'iniciado' → 'em_andamento' → 'concluido'
    pontuacao    = db.Column(db.Float,   nullable=True)     
    pagina_atual = db.Column(db.Integer, nullable=True)     
    tempo_gasto  = db.Column(db.Integer, nullable=True)     
    atualizado_em = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relacionamentos
    aluno    = db.relationship('Aluno',    back_populates='progressos')
    conteudo = db.relationship('Conteudo', back_populates='progressos')
    livro    = db.relationship('Livro',    back_populates='progressos')
    quiz     = db.relationship('Quiz',     back_populates='progressos')

    def __repr__(self):
        return f'<Progresso aluno={self.aluno_id} | {self.status}>'
