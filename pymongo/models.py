import datetime
import pprint
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

username = "Lirovsk"
password = "f0guet@oS2"
encoded_password = quote_plus(password)
encoded_username = quote_plus(username)

uri = f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.6jrv4gw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.test_db
first_collection = db.first_collection

post_model = {
    "name": "Lirovsk",
    "text": "Bem, foi uma honra ser parte da equipe",
    "date_of_post": datetime.datetime.now(),
}

# Inserting the document into the collection
try:
    result = first_collection.insert_one(post_model)
    print("Inserted post with id:", result.inserted_id)
except Exception as e:
    print("Error inserting post:", e)

# Retrieving the document from the collection
try:
    post = first_collection.find_one({"_id": result.inserted_id})
    print("Retrieved post:")
    pprint.pprint(post)
except Exception as e:
    print("failed to reatriver the post: ", e)
    
collections = db.list_collection_names()
print ("Collections in the database:", collections)