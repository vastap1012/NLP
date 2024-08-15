import nltk
from nltk import pos_tag
from nltk import RegexpParser
text = "This is practical no 6a".split()
print("After Split:", text)
nltk.download('averaged_perceptron_tagger')

tokens_tag = pos_tag(text)
print("After Token:", tokens_tag)

patterns = """mychunck:{<NN.?>*<VBD.?>*<JJ.?>*<CC>?}"""
chunker = RegexpParser(patterns)
print("After Regex:",chunker)
output = chunker.parse(tokens_tag)
print("After Chuncking",output)
