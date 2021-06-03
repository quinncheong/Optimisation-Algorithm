from localconfig.keys import keys
import pymongo

def DB_instance(database_name, collection_name):
    connection = pymongo.MongoClient(keys['mongoDB'])
    db = connection[database_name]
    collection = db[collection_name]
    return collection