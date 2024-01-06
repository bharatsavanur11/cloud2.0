import spacy
import numpy as np
import faiss

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Sample text data
text_data = [
    "This is an example document.",
    "Another example document with some words.",
    "Similarity search using FAISS for text documents."
]

# Convert text data to vectors using spaCy embeddings
def text_to_vector(text):
    doc = nlp(text)
    # Using the mean of word vectors as the document vector
    vector = np.mean([token.vector for token in doc], axis=0)
    return vector

# Create vectors for each document
vectors = [text_to_vector(text) for text in text_data]
vectors = np.array(vectors).astype('float32')

# Initialize the FAISS index
index = faiss.IndexFlatL2(vectors.shape[1])  # L2 norm (Euclidean distance) for similarity

# Add vectors to the index
index.add(vectors)

# Query vector
query_text = "A query document for similarity search."
query_vector = text_to_vector(query_text).reshape(1, -1).astype('float32')

# Perform similarity search
k = 2  # Number of nearest neighbors to retrieve
distances, indices = index.search(query_vector, k)
print("Indices",indices)
# Display results
print("Query Text:", query_text)
print("\nNearest Neighbors:")
for i, idx in enumerate(indices[0]):
    print(f"Neighbor {i+1}: {text_data[idx]} - Distance: {distances[0][i]}")
