from . import db

class User(db.Model):
    __tablename__ ="User"
    Id = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(80), unique=True, nullable=False)
    Email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.UserName

class Asset(db.Model):
    __tablename__ ="Asset"
    Id = db.Column(db.Integer,primary_key = True)
    Code = db.Column(db.String(10), unique = True, nullable = False)
    Description = db.Column(db.String(30), nullable = True)
    CreateBy =  db.Column(db.Integer, nullable = True)
    CreatedDateTime = db.Column(db.DateTime, nullable = True)
    UpdateBy = db.Column(db.Integer, nullable = True)
    UpdatedDateTime = db.Column(db.DateTime, nullable = True)
    AssetType = db.Column(db.String(2), nullable = True)
    
    def __repr__(self):
        return self._repr(Id=self.Id, Code=self.Code, Description=self.Description)

