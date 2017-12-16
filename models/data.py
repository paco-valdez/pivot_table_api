from sqlalchemy.dialects.postgresql import JSONB
from . import db


class Dataset(db.Model):
    __tablename__ = 'datasets'
    key = db.Column(db.VARCHAR, primary_key=True)
    column = db.Column(db.VARCHAR)
    row = db.Column(db.VARCHAR)
    value = db.Column(db.VARCHAR)
    func = db.Column(db.VARCHAR)
    data = db.Column('metadata_poi', JSONB)

    def __repr__(self):
        return '<Dataset %r>' % (self.key,)

    def to_dict(self):
        return {
            'column': self.column,
            'row': self.row,
            'value': self.value,
            'func': self.func,
            'data': self.data
        }
