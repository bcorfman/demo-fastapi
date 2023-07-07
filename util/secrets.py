import os

from starlette.config import Config

DATA_KEY = os.getenv('DETA_SPACE_DATA_KEY')
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
SECRET_KEY = os.getenv('SECRET_KEY')

if not DATA_KEY or not GOOGLE_CLIENT_ID or not GOOGLE_CLIENT_SECRET or not SECRET_KEY:
    starlette_config = Config('.env')
else:
    starlette_config = Config(environ={'GOOGLE_CLIENT_ID': GOOGLE_CLIENT_ID,
                                       'GOOGLE_CLIENT_SECRET': GOOGLE_CLIENT_SECRET,
                                       'SECRET_KEY': SECRET_KEY,
                                       'DATA_KEY': DATA_KEY})
