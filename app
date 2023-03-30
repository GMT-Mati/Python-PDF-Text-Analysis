import PyPDF2

import nltk

from nltk.tokenize import word_tokenize

from nltk.probability import FreqDist

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

# Close the PDF file

pdf_file.close()

