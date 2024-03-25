import nltk
nltk.download('averaged_perceptron_tagger')

nltk.download('punkt')

text = "Artificial intelligence is rapidly transforming the world."

tokens = nltk.word_tokenize(text)

pos_tags = nltk.pos_tag(tokens)

print("Original Text:", text)
print("POS Tags:", pos_tags)
print("Part of speech for 'intelligence':", pos_tags[2][1])
