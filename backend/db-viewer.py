import streamlit as st
from pymongo import MongoClient

# MongoDB connection URI
uri = "mongodb+srv://aybh299:testForSIHat2024@testsih.ojvu8.mongodb.net/hts"

# Establish connection to MongoDB
def connect_to_mongo():
    try:
        client = MongoClient(uri)
        db = client['hts']  # Access the 'hts' database
        return db
    except Exception as e:
        st.error(f"Error connecting to MongoDB: {e}")
        return None

# Fetch all documents from a collection
def fetch_documents(collection_name):
    db = connect_to_mongo()
    if db is not None:  # Use explicit None check
        try:
            collection = db[collection_name]
            documents = list(collection.find())
            return documents
        except Exception as e:
            st.error(f"Error fetching documents: {e}")
            return None
    return None

# Streamlit interface
def main():
    st.title("MongoDB Document Viewer")

    # Input for collection name
    collection_name = st.text_input("Enter the collection name to view documents:")

    if collection_name:
        # Fetch and display documents
        documents = fetch_documents(collection_name)

        if documents:
            st.write(f"Documents in collection: {collection_name}")
            for doc in documents:
                st.json(doc)
        else:
            st.write("No documents found or error in fetching documents.")

if __name__ == "__main__":
    main()
