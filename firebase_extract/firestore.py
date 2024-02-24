# scheme_edesia/firestore/firestore_backup.py

from firebase_admin import firestore
import json
from datetime import datetime

class FirestoreEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

def backup_firestore():
    db = firestore.client()
    collections = db.collections()
    backup_data = {}

    for collection in collections:
        collection_name = collection.id
        backup_data[collection_name] = {}
        docs = collection.stream()
        for doc in docs:
            doc_dict = doc.to_dict()
            doc_dict['id'] = doc.id
            backup_data[collection_name][doc.id] = doc_dict

    json_data = json.dumps(backup_data, indent=4, cls=FirestoreEncoder)
    with open('firestore_database_backup.json', 'w') as file:
        file.write(json_data)
