print ("Name: Abhishekkumar Mishra \tRoll No.:08")
from nltk.corpus.reader import WordListCorpusReader
reader_corpus = WordListCorpusReader('.', ['wordfile.txt'])
print (reader_corpus.words ())
