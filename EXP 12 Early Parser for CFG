import nltk

def nltk_earley_parse(grammar, input_string):
    parser = nltk.parse.EarleyChartParser(grammar)
    tokens = nltk.word_tokenize(input_string)
    chart = parser.chart_parse(tokens)
    return chart

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

    input_string = "Mary saw Bob with a telescope"

    chart = nltk_earley_parse(grammar, input_string)

    # Print the chart
    for i, parse in enumerate(chart):
        print("Chart[{}]:\n{}".format(i, parse))
