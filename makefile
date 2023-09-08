.PHONY: run install clean

run:
	python3 app.py

install:
	pip install -r requirements.txt

clean:
	rm -f *.pyc
