from extensions import app, db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash 



class Accounts(db.Model, UserMixin):
    nickname = db.Column(db.String)
    password_hash = db.Column(db.String)
    id = db.Column(db.Integer, primary_key = True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute!')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return  check_password_hash(self.password_hash, password)

    def __str__(self):
        return f"{self.nickname}"   
    
@login_manager.user_loader
def load_user(id):
    return Accounts.query.get(id)

        

if __name__ == "__main__":   
    with app.app_context():
        db.create_all()