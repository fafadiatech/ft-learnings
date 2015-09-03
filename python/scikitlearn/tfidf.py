import re
import feedparser

from hashlib import md5
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

URL = "http://economictimes.indiatimes.com/rssfeedsdefault.cms"
feed = feedparser.parse(URL)

vectorizer = CountVectorizer(min_df=1)
transformer = TfidfTransformer()
corpus = []

def clean_text(sentence):
    """
    This method is used to clean text using regex
    """
    pattern=re.compile("[^\w']|\'")
    return pattern.sub(' ', sentence).strip()

for item in feed.entries:
    title = item.title
    corpus.append(clean_text(title.lower()))

X = vectorizer.fit_transform(corpus)
tfidf = transformer.fit_transform(X.toarray())
print tfidf.toarray()
