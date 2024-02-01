import nltk
from nltk import CFG
from nltk import parse

grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog'
    V -> 'chased' | 'ate'
""")

parser = parse.ChartParser(grammar)

def generate_parse_tree(sentence):
    words = nltk.word_tokenize(sentence)
    chart = parser.chart_parse(words)
    parse_tree = list(chart.parses(grammar.start()))[0]
    parse_tree.pretty_print()

sentence = "the cat chased the dog"

generate_parse_tree(sentence)
