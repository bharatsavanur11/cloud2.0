import spacy
import numpy as np

class TextVectorDatabase:
    def __init__(self):
        self.documents = {}  # Dictionary to store text documents
        self.index = {}      # Index for quick retrieval
        self.nlp = spacy.load("en_core_web_sm")  # spaCy model with pre-trained word embeddings

    def add_document(self, document_id, text):
        """
        Add a text document to the database.
        :param document_id: Unique identifier for the document
        :param text: Text content of the document
        """
        if document_id in self.documents:
            raise ValueError("Document with the same ID already exists.")

        self.documents[document_id] = text

        # Tokenize and get word vectors
        doc = self.nlp(text)
        document_vector = np.mean([token.vector for token in doc if token.has_vector], axis=0)

        # Indexing the document vector for quick retrieval
        self.index[document_id] = document_vector

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
        similarities = {doc_id: np.dot(query_vector, document_vector) / (np.linalg.norm(query_vector) * np.linalg.norm(document_vector))
                        for doc_id, document_vector in self.index.items()}

        # Sort the documents by similarity
        similarities = {doc_id: similarity for doc_id, similarity in sorted(similarities.items(), key=lambda item: item[1], reverse=True)}
        print(similarities)
        # Filter documents based on the threshold
        similar_documents = [doc_id for doc_id, similarity in similarities.items() if similarity >= threshold]

        return similar_documents

# Example usage
text_vector_db = TextVectorDatabase()

# Add documents
text_vector_db.add_document("doc1", "This is an example document about natural language processing.")
text_vector_db.add_document("doc2", "Machine learning algorithms play a crucial role in NLP applications.")
text_vector_db.add_document("doc3", "Text vectorization is important understanding Natural Language Processing.")
text_vector_db.add_document("doc4", "Learn, understand natural language processing  skills.")


# Search for similar documents
query_text = "I want to understand more about natural language processing."
similar_documents = text_vector_db.search_similar_documents(query_text, threshold=0.6)
print("Similar Documents:", similar_documents)
