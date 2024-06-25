.PHONY: run install clean

run:
	python3 pdf_word_counter.py

install:
	pip install -r requirements.txt

clean:
	rm -f *.pyc
	rm -f wordcloud.png
	rm -f *.csv
