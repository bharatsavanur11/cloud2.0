from gensim.models import Word2Vec
from gensim.models.keyedvectors import KeyedVectors
import numpy as np

class TextVectorDatabase:
    def __init__(self, model_path=None):
        if model_path:
            self.model = KeyedVectors.load(model_path)
        else:
            self.model = None
        self.documents = {}

    def train_word2vec(self, corpus):
        """
        Train Word2Vec model on the given corpus.
        :param corpus: List of tokenized documents
        """
        self.model = Word2Vec(sentences=corpus, vector_size=100, window=5, min_count=1, workers=4)
        self.model.init_sims(replace=True)

    def save_model(self, model_path):
        """
        Save the Word2Vec model to a file.
        :param model_path: File path to save the model
        """
        if self.model:
            self.model.save(model_path)

    def add_document(self, document_id, text):
        """
        Add a text document to the database.
        :param document_id: Unique identifier for the document
        :param text: Text content of the document
        """
        if not self.model:
            raise ValueError("Word2Vec model not trained. Please train the model first.")

        tokens = text.lower().split()
        document_vector = np.mean([self.model.wv[token] for token in tokens if token in self.model.wv], axis=0)
        self.documents[document_id] = document_vector

    def search_similar_documents(self, query_text, threshold=0.8):
        """
        Search for documents similar to the given query text.
        :param query_text: Text content of the query document
        :param threshold: Similarity threshold for the search
        :return: List of document IDs that are similar to the query document
        """
        if not self.model:
            raise ValueError("Word2Vec model not trained. Please train the model first.")

        query_tokens = query_text.lower().split()
        query_vector = np.mean([self.model.wv[token] for token in query_tokens if token in self.model.wv], axis=0)

        similarities = {doc_id: np.dot(query_vector, document_vector) /
                                (np.linalg.norm(query_vector) * np.linalg.norm(document_vector))
                        for doc_id, document_vector in self.documents.items()}

        similar_documents = [doc_id for doc_id, similarity in similarities.items() if similarity >= threshold]
        return similar_documents

# Example usage
text_vector_db = TextVectorDatabase()

corpus = [
    ["this", "is", "an", "example", "document", "about", "natural", "language", "processing"],
    ["machine", "learning", "algorithms", "play", "a", "crucial", "role", "in", "nlp", "applications"],
    ["text", "vectorization", "is", "an", "important", "step", "in", "information", "retrieval"]
]

text_vector_db.train_word2vec(corpus)

text_vector_db.add_document("doc1", "This is an example document about natural language processing.")
text_vector_db.add_document("doc2", "Machine learning algorithms play a crucial role in NLP applications.")
text_vector_db.add_document("doc3", "Text vectorization is an important step in information retrieval.")

query_text = "I want to understand more about natural language processing."
similar_documents = text_vector_db.search_similar_documents(query_text, threshold=0.6)
print("Similar Documents:", similar_documents)
