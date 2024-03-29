import numpy as np
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_coherence(text):

    sentences = nltk.sent_tokenize(text)


    vectorizer = CountVectorizer().fit_transform(sentences)
    sentence_embeddings = vectorizer.toarray()


    similarity_matrix = cosine_similarity(sentence_embeddings)


    coherence_score = np.mean(similarity_matrix)

    return coherence_score


text = """
Natural language processing (NLP) is a field of computer science, artificial intelligence, and computational linguistics concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data. Challenges in natural language processing frequently involve speech recognition, natural language understanding, and natural-language generation.
NLP tasks include text translation, sentiment analysis, named entity recognition, parsing, and many others.
Coherence is the quality of being logical and consistent. In text, coherence refers to the connectivity or flow of ideas and information from one sentence to another.
"""

coherence_score = compute_coherence(text)
print("Coherence score:", coherence_score)
