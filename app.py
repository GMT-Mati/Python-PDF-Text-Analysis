import PyPDF2

import nltk

from nltk.tokenize import word_tokenize

from nltk.probability import FreqDist

from nltk.sentiment import SentimentIntensityAnalyzer

import spacy

from spacy import displacy

from collections import Counter

from langdetect import detect

from gensim import corpora, models

from wordcloud import WordCloud

import matplotlib.pyplot as plt

# Open the PDF file in read binary mode

pdf_file = open('sample.pdf', 'rb')

# Create a PDF reader object

pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# Get the number of pages in the PDF file

num_pages = pdf_reader.getNumPages()

# Initialize an empty string to store the text

text = ""

# Loop through each page of the PDF file and extract the text

for i in range(num_pages):

    page = pdf_reader.getPage(i)

    text += page.extractText()

# Tokenize the text

tokens = word_tokenize(text)

# Get the frequency distribution of the tokens

fdist = FreqDist(tokens)

# Print the 10 most common tokens

print(fdist.most_common(10))

# Perform sentiment analysis on the text

sia = SentimentIntensityAnalyzer()

sentiment = sia.polarity_scores(text)

print("Sentiment Analysis Results:")

print(sentiment)

# Perform named entity recognition

nlp = spacy.load("en_core_web_sm")

doc = nlp(text)

entities = [(entity.text, entity.label_) for entity in doc.ents]

print("Named Entity Recognition Results:")

print(entities)

# Detect language of the text

language = detect(text)

print("Detected Language:", language)

# Perform topic modeling on the text

texts = [tokens]

dictionary = corpora.Dictionary(texts)

corpus = [dictionary.doc2bow(text) for text in texts]

lda_model = models.ldamodel.LdaModel(corpus, num_topics=3, id2word=dictionary, passes=10)

print("Topic Modeling Results:")

for idx, topic in lda_model.print_topics(-1):

    print("Topic {}: {}".format(idx, topic))

# Generate word cloud of the text

wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud, interpolation='bilinear')

plt.axis("off")

plt.show()

# Close the PDF file

pdf_file.close()



