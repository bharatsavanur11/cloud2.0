import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

class TextVectorDatabase:
    def __init__(self):
        self.documents = {}
        self.vectorizer = CountVectorizer(stop_words=stopwords.words('english'))

    def preprocess_text(self, text):
        """
        Tokenize and remove stopwords from the text.
        """
        tokens = nltk.word_tokenize(text)
        tokens = [word.lower() for word in tokens if word.isalnum() and word.lower() not in stopwords.words('english')]
        return ' '.join(tokens)

    def add_document(self, document_id, text):
        """
        Add a text document to the database.
        :param document_id: Unique identifier for the document
        :param text: Text content of the document
        """
        preprocessed_text = self.preprocess_text(text)
        self.documents[document_id] = preprocessed_text

    def vectorize_documents(self):
        """
        Vectorize the documents using the CountVectorizer.
        """
        self.vector_matrix = self.vectorizer.fit_transform(self.documents.values()).toarray()
        self.feature_names = self.vectorizer.get_feature_names_out()

    def search_similar_documents(self, query_text, threshold=0.8):
        """
        Search for documents similar to the given query text using cosine similarity.
        :param query_text: Text content of the query document
        :param threshold: Similarity threshold for the search
        :return: List of document IDs that are similar to the query document
        """
        query_vector = self.vectorizer.transform([self.preprocess_text(query_text)]).toarray()

        similarities = {doc_id: np.dot(query_vector, document_vector) /
                                (np.linalg.norm(query_vector) * np.linalg.norm(document_vector))
                        for doc_id, document_vector in zip(self.documents.keys(), self.vector_matrix)}

        similar_documents = [doc_id for doc_id, similarity in similarities.items() if similarity >= threshold]
        return similar_documents

# Example usage
text_vector_db = TextVectorDatabase()

text_vector_db.add_document("doc1", "This is an example document about natural language processing.")
text_vector_db.add_document("doc2", "Machine learning algorithms play a crucial role in NLP applications.")
text_vector_db.add_document("doc3", "Text vectorization is an important step in information retrieval.")

text_vector_db.vectorize_documents()

query_text = "I want to understand more about natural language processing."
similar_documents = text_vector_db.search_similar_documents(query_text, threshold=0.7)
print("Similar Documents:", similar_documents)
