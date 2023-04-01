import spacy
import PyPDF2
from collections import Counter

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Open the PDF file in read binary mode
pdf_file = open('sample.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# Initialize an empty list to store the text
texts = []

# Loop through each page of the PDF file and extract the text
for i in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(i)
    text = page.extractText()
    texts.append(text)

# Join the text from all pages into a single string
text = " ".join(texts)

# Use spaCy to analyze the text
doc = nlp(text)

# Print the 10 most common tokens
tokens = [token.text for token in doc if not token.is_stop and not token.is_punct and not token.is_space]
token_counts = Counter(tokens)
print("Top 10 most common tokens:")
for token, count in token_counts.most_common(10):
    print(f"{token}: {count}")

# Perform named entity recognition
entities = [(entity.text, entity.label_) for entity in doc.ents]
print("Named Entity Recognition Results:")
print(entities)

# Generate dependency tree
for sentence in doc.sents:
    print(f"Sentence: {sentence.text}")
    for token in sentence:
        print(f"{token.text} --{token.dep_}--> {token.head.text}")

# Close the PDF file
pdf_file.close()
