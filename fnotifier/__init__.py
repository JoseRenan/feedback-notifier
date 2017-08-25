from . factory import create_app
from flask_marshmallow import Marshmallow

app = create_app(__name__)
ma = Marshmallow(app)
