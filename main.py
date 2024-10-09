import json

import nltk
nltk.download("punkt_tab")

with open("intents.json") as intents_file:
    intents = json.load(intents_file)

words = []
labels = []
docs = []

for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        tokenized_words = nltk.word_tokenize(pattern)
        words.extend(tokenized_words)
        docs.append(pattern)

    if intent["tag"] not in labels:
        labels.append(intent["tag"])
