from . import db


class UserProfile(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name  = db.Column(db.String(80))
    email      = db.Column(db.String(255))
    gender     = db.Column(db.String(16))
    location   = db.Column(db.String(255))
    biography  = db.Column(db.Text)
    profilePic = db.Column(db.String(255))
    created_on = db.Column(db.Date)
    
    
    def __init__(self,first_name,last_name,email,gender,location,biography,profilePic,created_on):
        self.first_name = first_name
        self.last_name  = last_name
        self.email      = email
        self.gender     = gender
        self.location   = location
        self.biography  = biography
        self.profilePic = profilePic
        self.created_on = created_on
    
    def __repr__(self):
        return '<User %r>' % self.first_name