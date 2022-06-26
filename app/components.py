from app import db

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_en = db.Column(db.String(64), index=True, unique=True)
    category_ru = db.Column(db.String(64), index=True, unique=True)    
    words = db.relationship('Word', backref ='engl')
    def __repr__(self):
        return '<Categories {}>'.format(self.category_en) 

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word_en = db.Column(db.String(140))
    word_ru = db.Column(db.String(140)) 
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    def __repr__(self):
        return '<Word {}>'.format(self.word_en)
