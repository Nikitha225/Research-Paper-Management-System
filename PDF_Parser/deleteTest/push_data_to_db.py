from pymongo import MongoClient


def get_database():
    
    CONNECTION_STRING = "mongodb+srv://researchpaperrepo:researchpaperrepo@cluster0.jbeoezw.mongodb.net/ResearchPapersRepo?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    
    return client['ResearchPapersRepo']


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # Get the database
    dbname = get_database()


# from pymongo import MongoClient

# db = cluster["ResearchPapersRepo"]
# collection = db["researchPaperDocs"]


# collection.insert_one({"_id": "0", "test": "test"})