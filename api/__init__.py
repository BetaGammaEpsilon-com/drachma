from flask import Flask
from flask_cors import CORS
from .routes import home, treasurer, user

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

# registers prefixes and allows app to find routes
# bp for routes/home.py
app.register_blueprint(home.home_bp)
# bp for routes/treasurer.py
app.register_blueprint(treasurer.tres_bp)
# bp for routes/user.py
app.register_blueprint(user.user_bp)