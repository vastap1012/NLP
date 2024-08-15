import nltk
#nltk.download('brown')
from nltk.corpus import brown
print (brown.categories())
print("\n")
print(brown.words(categories = 'news'))
print("\n")
print(brown.fileids())
print("\n")
print(brown.words(fileids='cg22'))
print("\n")
print(brown.sents(categories=['news','editorial','reviews']))
