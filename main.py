from flask import Flask, g, render_template, request, flash
from flask_login.utils import login_required, logout_user
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokeBase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#home
@app.route('/')
def home():
    return render_template('home.html', page_title='IT WORKS!')

# star t
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)