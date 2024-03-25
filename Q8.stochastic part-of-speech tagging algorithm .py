import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import brown
from collections import defaultdict

nltk.download('brown')
nltk.download('universal_tagset')

training_data = brown.tagged_sents(tagset='universal')

def calculate_word_tag_frequencies(training_data):
    word_tag_freq = defaultdict(lambda: defaultdict(int))
    tag_freq = defaultdict(int)

    for sentence in training_data:
        for word, tag in sentence:
            word_tag_freq[word][tag] += 1
            tag_freq[tag] += 1

    return word_tag_freq, tag_freq

word_tag_freq, tag_freq = calculate_word_tag_frequencies(training_data)

def pos_tag(sentence):
    tagged_sentence = []
    for word in sentence:
        if word in word_tag_freq:
            most_common_tag = max(word_tag_freq[word], key=word_tag_freq[word].get)
            tagged_sentence.append((word, most_common_tag))
        else:
            # If word is unseen, assign the most common tag from training data
            most_common_tag = max(tag_freq, key=tag_freq.get)
            tagged_sentence.append((word, most_common_tag))
    return tagged_sentence

sentence = "The quick brown fox jumps over the lazy dog."

tokenized_sentence = word_tokenize(sentence.lower())

tagged_sentence = pos_tag(tokenized_sentence)

print("POS Tagging:")
print(tagged_sentence)
