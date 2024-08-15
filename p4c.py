import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at two buying U.K. startup for $1 billion")
for token in doc:
    print(token.text)
    
print("\n",doc[9]," : ",doc[9].is_currency)

print("\n",doc[4]," : ",doc[9].like_num)

import nltk
#nltk.download('punkt')
from nltk.tokenize import word_tokenize

text = """Founded in 2002, SpaceX’s mission is to enable humans to become a spacefaring civilization and a multi-planet species by building a self-sustaining city on Mars. In 2008, SpaceX’s Falcon 1 became the first privately developed liquid-fuel launch vehicle to orbit the Earth."""
a=word_tokenize(text)
print(a)
