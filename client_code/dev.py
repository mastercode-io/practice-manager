import anvil.js
from anvil.js.window import jQuery, ej
from AnvilFusion.tools.utils import AppEnv, init_user_session
from AnvilFusion.datamodel import migrate
from . import app

AppEnv.APP_ID = 'practiceMANAGER'
AppEnv.data_models = app.models

migrate.migrate_db_schema()
