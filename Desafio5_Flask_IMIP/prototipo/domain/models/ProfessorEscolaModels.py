from datetime import datetime
from adapters.repositories.InterfaceDB import db

class ProfessorEscola(db.Model):
    __tablename__ = 'professor_escola'

    id            = db.Column(db.Integer, primary_key=True)
    professor_id  = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)
    escola_id     = db.Column(db.Integer, db.ForeignKey('escolas.id'),     nullable=False)
    data_entrada  = db.Column(db.DateTime, default=datetime.utcnow)
    ativo         = db.Column(db.Boolean, default=True)

    # Relacionamentos
    professor = db.relationship('Professor', back_populates='escolas')
    escola    = db.relationship('Escola',    back_populates='professores')

    # Garante que o mesmo professor não seja vinculado 2x à mesma escola
    __table_args__ = (
        db.UniqueConstraint('professor_id', 'escola_id', name='uq_professor_escola'),
    )

    def __repr__(self):
        return f'<ProfessorEscola prof={self.professor_id} escola={self.escola_id}>'
