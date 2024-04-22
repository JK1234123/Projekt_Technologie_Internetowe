from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

app.config['SECRET_KEY'] = "AS@!zxd412SA754gh"
app.run(port=5000)
