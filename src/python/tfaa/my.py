from pymongo import MongoClient


class MongoDB:
    def __init__(self, db_url, db_name):
        self.db_url = db_url
        self.db_name = db_name
        self.client = None
        self.db = None

    def connect(self):
        self.client = MongoClient(self.db_url)
        self.db = self.client[self.db_name]

    def insert(self, collection_name, data):
        self.db[collection_name].insert_one(data)

    def find(self, collection_name, query={}):
        return self.db[collection_name].find(query)

    def update(self, collection_name, query, data):
        self.db[collection_name].update_many(query, {"$set": data})

    def delete(self, collection_name, query):
        self.db[collection_name].delete_many(query)

    def disconnect(self):
        self.client.close()


if __name__ == "__main__":

    db = MongoDB("mongodb://localhost:27017/", "mydatabase")
    db.connect()
    db.insert("users", {"name": "John", "age": 30})
    results = db.find("users", {"age": {"$gt": 25}})
    for result in results:
        print(result)
    db.update("users", {"name": "John"}, {"age": 35})
    db.delete("users", {"name": "John"})
    db.disconnect()
