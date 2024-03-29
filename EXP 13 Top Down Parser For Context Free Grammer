import nltk

def generate_parse_tree(grammar, sentence):
    parser = nltk.ChartParser(grammar)
    tokens = nltk.word_tokenize(sentence)
    for tree in parser.parse(tokens):
        return tree

# Example usage:
if __name__ == "__main__":
    # Example grammar
    grammar = nltk.CFG.fromstring("""
        S -> NP VP
        VP -> V NP | V NP PP
        PP -> P NP
        V -> "saw" | "ate" | "walked"
        NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
        Det -> "a" | "an" | "the" | "my"
        N -> "man" | "dog" | "cat" | "telescope" | "park"
        P -> "in" | "on" | "by" | "with"
    """)

    input_sentence = "Mary saw Bob with a telescope"

    parse_tree = generate_parse_tree(grammar, input_sentence)

    # Print out the parse tree
    print("Parse Tree:")
    print(parse_tree)
