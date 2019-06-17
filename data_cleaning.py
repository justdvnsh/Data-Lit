from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

filename = 'meta.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

stop_words = stopwords.words('english')

## Tokenizing
tokens = word_tokenize(text)
print(tokens[:100])

## Making the letters all of the same format
tokens = [w.lower() for w in tokens]

## Removing Punctuations
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]
print(stripped[:100])

## Filtering out words that are not alphabets
words = [word for word in stripped if word.isalpha()]

## Filtering out stopwords
words = [word for word in words if not word in stop_words]

## Applying Stemming
porter = PorterStemmer()
words = [porter.stem(word) for word in words]

#print(words[:100])

