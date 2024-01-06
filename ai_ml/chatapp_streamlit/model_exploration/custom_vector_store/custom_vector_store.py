import spacy
import numpy as np
import faiss


class TextVectorDatabase:
    def __init__(self):
        self.documents = {}  # Dictionary to store text documents
        self.index = {}  # Index for quick retrieval
        self.nlp = spacy.load("en_core_web_sm")  # spaCy model with pre-trained word embeddings
        self.docs_by_index = []

    def add_document(self, document_id, text):
        """
        Add a text document to the database.
        :param document_id: Unique identifier for the document
        :param text: Text content of the document
        """
        if document_id in self.documents:
            raise ValueError("Document with the same ID already exists.")

        self.documents[document_id] = text
        self.docs_by_index.append(text)

        # Tokenize and get word vectors
        doc = self.nlp(text)
        document_vector = np.mean([token.vector for token in doc if token.has_vector], axis=0)

        # Indexing the document vector for quick retrieval
        self.index[document_id] = document_vector
        return self.index, text

    def fetch_document_by_id(self, document_ids):
        """
        Fetch a document from the database by its ID.
        :param document_ids: Unique identifier for the document
        :return: Text content of the document
        """
        docs = []
        if (len(document_ids) > 0):
            for document_id in document_ids:
                docs.append(self.documents[document_id])
        else:
            docs = self.documents.values()

        return docs

    def search_similar_documents(self, query_text, threshold=0.8):
        """
        Search for documents similar to the given query text.
        :param query_text: Text content of the query document
        :param threshold: Similarity threshold for the search
        :return: List of document IDs that are similar to the query document
        """
        # Tokenize and get vector for the query text
        query_doc = self.nlp(query_text)
        query_vector = np.mean([token.vector for token in query_doc if token.has_vector], axis=0)

        # Calculate similarity with each document
        similarities = {doc_id: np.dot(query_vector, document_vector) / (
                np.linalg.norm(query_vector) * np.linalg.norm(document_vector))
                        for doc_id, document_vector in self.index.items()}

        # Sort the documents by similarity
        similarities = {doc_id: similarity for doc_id, similarity in
                        sorted(similarities.items(), key=lambda item: item[1], reverse=True)}
        print(similarities)
        # Filter documents based on the threshold
        similar_documents = [doc_id for doc_id, similarity in similarities.items() if similarity >= threshold]

        return similar_documents

    def text_to_vector(self, text):
        doc = self.nlp(text)
        # Using the mean of word vectors as the document vector
        vector = np.mean([token.vector for token in doc], axis=0)
        return vector


# Example usage
text_vector_db = TextVectorDatabase()

# Add documents
text_vector_db.add_document("doc1", "This is an example document about natural language processing.")
text_vector_db.add_document("doc2", "Machine learning algorithms play a crucial role in NLP applications.")
text_vector_db.add_document("doc3", "Text vectorization is important understanding Natural Language Processing.")
text_vector_db.add_document("doc4", "Learn, understand natural language processing  skills.")

# Search for similar documents
query_text = "I want to understand more about natural language processing."
similar_documents = text_vector_db.search_similar_documents(query_text, threshold=0.55)
print("Similar Documents:", similar_documents)

# Fetch the documents
documents = text_vector_db.fetch_document_by_id(similar_documents)
print("Documents:", documents)

# -------------------------


vector_data = [text_vector_db.text_to_vector(text) for text in text_vector_db.documents.values()]
vector_data = np.array(vector_data).astype('float32')

## Adding it in Faiss Index
print(vector_data.shape)
print(vector_data)

# Initialize the FAISS index
index = faiss.IndexFlatL2(vector_data.shape[1])  # L2 norm (Euclidean distance) for similarity

# Add vectors to the index
index.add(vector_data)

# Query vector
query_text = "I want to understand more about natural language processing."
query_vector = text_vector_db.text_to_vector(query_text).reshape(1, -1).astype('float32')

# Perform similarity search
k = 2  # Number of nearest neighbors to retrieve
distances, indices = index.search(query_vector, k)


# Display results
print("Query Text:", query_text)
for i, idx in enumerate(indices[0]):
    print(i,idx)
    print(f"Neighbor: {text_vector_db.docs_by_index[idx]} - Distance: {distances[0][idx]}")
