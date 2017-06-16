from pymongo import MongoClient

def connect(client,db,collection):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['db']
    collection = db['post']
    #client = MongoClient('mongodb://localhost:27017/')
    #db = client['db']
    #collection = db['posts']

post = {"author": "Mike","text": "My first blog post!","tags": ["mongodb", "python", "pymongo"]}
posts = db.posts
post_id = posts.insert_one(post).inserted_id
post_id
print (*db.collection_names(include_system_collections=False))
print (posts.find_one({"_id": post_id}))

# The web framework gets post_id from the URL and passes it as a string
def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})
    