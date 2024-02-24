# scheme_edesia/common/firebase_admin_init.py

import firebase_admin
from firebase_admin import credentials

def initialize_firebase_admin(json_credentials_path, databaseURL=None, storageBucket=None):
    cred = credentials.Certificate(json_credentials_path)
    options = {}
    if databaseURL:
        options['databaseURL'] = databaseURL
    if storageBucket:
        options['storageBucket'] = storageBucket

    firebase_admin.initialize_app(cred, options)
