import re

rules = [
    (r'\b(?:[Tt]he|[Aa]n?)\b', 'DET'),  # Determiners
    (r'\b(?:[A-Z]\w*)+\b', 'NOUN'),      # Proper nouns
    (r'\b(?:[Aa]?\w+ed|[Ii]s|[Aa]m|[Aa]re)\b', 'VERB'),  # Verbs
    (r'\b(?:[Aa]n?|[Tt]he|[Aa]ll|[Tt]hese?)\b', 'DET'),  # Determiners
    (r'\b(?:[Aa]bout|[Aa]t|[Bb]y|[Ff]or|[Ii]n|[Oo]n|[Uu]p)\b', 'ADP'),  # Prepositions
    (r'\b(?:[Aa]nd|[Bb]ut|[Oo]r|[Yy]et)\b', 'CONJ'),  # Conjunctions
    (r'\b(?:[Aa]n?|[Tt]he)\b', 'DET'),   # Articles
    (r'\b(?:[Hh]e|[Ss]he|[Ii]t|[Ww]e|[Tt]hey|[Mm]e|[Yy]ou|[Hh]im|[Hh]er)\b', 'PRON'),  # Pronouns
    (r'\b(?:[0-9]+\.[0-9]+|[0-9]+)\b', 'NUM'),  # Numbers
    (r'\b(?:[Aa]bout|[Aa]bove|[Aa]fter|[Aa]gainst|[Aa]long|[Aa]mid|[Aa]mong|[Aa]round|[Aa]t|[Aa]way|[Bb]efore|[Bb]ehind|[Bb]elow|[Bb]eneath|[Bb]eside|[Bb]etween|[Bb]eyond|[Bb]ut|[Bb]y|[Dd]own|[Ff]or|[Ff]rom|[Ii]n|[Ii]nto|[Ll]ike|[Nn]ear|[Oo]f|[Oo]ff|[Oo]n|[Oo]ut|[Oo]ver|[Pp]ast|[Rr]ound|[Ss]ince|[Tt]hrough|[Tt]hroughout|[Tt]ill|[Tt]o|[Tt]oward|[Tt]owards|[Uu]nder|[Uu]ntil|[Uu]pon|[Ww]ith)\b', 'ADP'),  # Prepositions
    (r'\b(?:[Cc]an|[Cc]ould|[Dd]o|[Dd]oes|[Dd]id|[Hh]ad|[Hh]as|[Hh]ave|[Ii]s|[Mm]ay|[Mm]ight|[Mm]ust|[Ss]hall|[Ss]hould|[Ww]as|[Ww]ere|[Ww]ill|[Ww]ould)\b', 'AUX'),  # Auxiliary verbs
    (r'\b(?:[Ff]or|[Aa]nd|[Nn]or|[Bb]ut|[Oo]r|[Yy]et|[Ss]o)\b', 'CONJ'),  # Coordinating conjunctions
    (r'\b(?:[Ss]o|[Tt]hat|[Aa]lthough|[Tt]hough|[Ww]hile|[Ii]f)\b', 'SCONJ'),  # Subordinating conjunctions
    (r'\b(?:[Ww]ho|[Ww]hom|[Ww]hich|[Tt]hat|[Ww]here|[Ww]hen)\b', 'PRON'),  # Relative pronouns
    (r'\b(?:[Tt]o)\b', 'PART'),  # Particles
    (r'\b(?:[Aa]n?|[Tt]he)\b', 'DET'),  # Articles
    (r'\b(?:[Hh]ow|[Ww]hat|[Ww]ho)\b', 'PRON'),  # Interrogative pronouns
    (r'\b(?:[Ww]ell|[Nn]ow|[Oo]h)\b', 'INTJ'),  # Interjections
    (r'\b(?:[A-Z][a-z]*)\b', 'PROPN'),  # Proper nouns
    (r'\b(?:[A-Za-z]+ing)\b', 'VERB'),  # Gerunds
    (r'\b(?:[A-Za-z]+ly)\b', 'ADV'),  # Adverbs
    (r'\b(?:[A-Za-z]+ness)\b', 'NOUN'),  # Nouns
    (r'\b(?:[A-Za-z]+(ed|d))\b', 'VERB'),  # Past tense verbs
    (r'\b(?:[A-Za-z]+s)\b', 'NOUN'),  # Plural nouns
    (r'\b(?:[A-Za-z]+est)\b', 'ADJ'),  # Superlative adjectives
    (r'\b(?:[A-Za-z]+er)\b', 'ADJ'),  # Comparative adjectives
    (r'\b(?:[A-Za-z]+)\b', 'NOUN')  # Default: assume noun
]

def rule_based_pos_tagging(sentence, rules):
    tagged_sentence = []
    for word in sentence:
        for pattern, tag in rules:
            if re.match(pattern, word):
                tagged_sentence.append((word, tag))
                break
        else:
            tagged_sentence.append((word, 'UNK'))  # Assign UNK tag if no rule matches
    return tagged_sentence

sentence = "The quick brown fox jumps over the lazy dog."

tokenized_sentence = re.findall(r'\b\w+\b', sentence.lower())

tagged_sentence = rule_based_pos_tagging(tokenized_sentence, rules)

print("POS Tagging:")
print(tagged_sentence)
