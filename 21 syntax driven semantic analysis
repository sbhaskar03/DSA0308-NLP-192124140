import nltk
from nltk.corpus import wordnet

def extract_noun_phrases(sentence):
    grammar = r"""
        NP: {<DT|JJ|PR.*>*<NN.*>+}
    """
    chunk_parser = nltk.RegexpParser(grammar)
    tagged_words = nltk.pos_tag(nltk.word_tokenize(sentence))
    tree = chunk_parser.parse(tagged_words)

    noun_phrases = []
    for subtree in tree.subtrees(filter=lambda t: t.label() == 'NP'):
        noun_phrase = ' '.join(word for word, tag in subtree.leaves())
        noun_phrases.append(noun_phrase)

    return noun_phrases

def get_noun_phrase_meanings(noun_phrases):
    noun_phrase_meanings = {}
    for noun_phrase in noun_phrases:
        synsets = wordnet.synsets(noun_phrase)
        meanings = set()
        for synset in synsets:
            meanings.update(synset.definition().split(';'))
        noun_phrase_meanings[noun_phrase] = list(meanings)
    return noun_phrase_meanings

# Example usage
sentence = "The quick brown fox jumps over the lazy dog."
noun_phrases = extract_noun_phrases(sentence)
noun_phrase_meanings = get_noun_phrase_meanings(noun_phrases)

print("Noun phrases:", noun_phrases)
print("Noun phrase meanings:")
for noun_phrase, meanings in noun_phrase_meanings.items():
    print(f"{noun_phrase}: {meanings}")
