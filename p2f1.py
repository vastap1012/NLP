import nltk
from nltk.corpus import brown
#nltk.download('brown')
tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
nltk.FreqDist(tags).max()
raw = 'I do not like green eggs and ham, I do not like them Sam I am!'

print("\n Raw text :"+raw)
tokens = nltk.word_tokenize(raw)
default_tagger = nltk.DefaultTagger('NN')
print("\n")
print(default_tagger.tag(tokens))
