from api import app
from api.resources.config import *
from development.common_util.config import *

print(app.url_map)

app.run(port=5000, host='0.0.0.0')