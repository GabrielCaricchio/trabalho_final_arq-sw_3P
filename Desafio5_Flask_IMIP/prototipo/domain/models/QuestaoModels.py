from adapters.repositories.InterfaceDB import db

class Questao(db.Model):
    __tablename__ = 'questoes'

    id             = db.Column(db.Integer, primary_key=True)
    quiz_id        = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=False)
    enunciado      = db.Column(db.Text, nullable=False)
    opcao_a        = db.Column(db.String(300))
    opcao_b        = db.Column(db.String(300))
    opcao_c        = db.Column(db.String(300))
    opcao_d        = db.Column(db.String(300))
    resposta_correta = db.Column(db.String(1))    # 'a', 'b', 'c' ou 'd'
    explicacao     = db.Column(db.Text)           

    # Relacionamentos
    quiz = db.relationship('Quiz', back_populates='questoes')

    def __repr__(self):
        return f'<Questao quiz={self.quiz_id} | {self.enunciado[:40]}>'
