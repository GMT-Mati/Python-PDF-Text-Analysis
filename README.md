# PDF Word Frequency Counter

The PDF Word Frequency Counter is a Python-based GUI tool that allows users to analyze word frequencies in PDF files. It provides various features including sorting options, stop words filtering, word cloud visualization, and exporting results to a CSV file.

## Features

- **Browse and Select PDF File:** Select a PDF file from your file system.
- **Word Frequency Analysis:** Extracts text from the PDF and counts the frequency of each word.
- **Sorting Options:** Sort word frequencies either by frequency or alphabetically.
- **Top N Words Display:** Display the top N frequent words.
- **Stop Words Filtering:** Option to exclude common stop words from the analysis.
- **Export to CSV:** Export word frequency results to a CSV file.
- **Search Feature:** Search for specific words within the results.
- **Word Cloud Visualization:** Generate and display a word cloud based on word frequencies.

## Installation

Ensure you have Python installed on your system. You will also need to install the following Python libraries:

- PyMuPDF (fitz)
- Tkinter (usually included with Python installations)
- WordCloud
- Matplotlib
- Pillow

You can install these libraries using pip:

```sh
pip install pymupdf wordcloud matplotlib pillow
```

Alternatively, you can use the provided `Makefile` to install the dependencies:

```sh
make install
```

## Usage

1. **Run the Application:**

   Run the Python script to start the application:

   ```sh
   python pdf_word_counter.py
   ```

   Or use the `Makefile`:

   ```sh
   make run
   ```

2. **Browse PDF:**

   Click the "Browse for PDF" button to open a file dialog and select a PDF file.

3. **Set Options:**
   - **Sort by:** Choose between "Frequency" or "Alphabetically" to sort the word frequencies.
   - **Display Top N Words:** Enter the number of top words to display.
   - **Filter Stop Words:** Check the checkbox to exclude common stop words from the analysis.

4. **View Results:**

   The word frequencies will be displayed in the text widget.

5. **Export Results:**

   Click the "Export to CSV" button to save the results to a CSV file.

6. **Search Words:**

   Enter a word in the search bar and click the "Search" button to filter the results.

7. **Generate Word Cloud:**

   Click the "Generate Word Cloud" button to create and display a word cloud based on the word frequencies.

## Example

Here is a screenshot of the application in action:

![PDF Word Frequency Counter Screenshot](screenshot.png)

## Makefile

A `Makefile` is included to streamline running the application, installing dependencies, and cleaning up generated files.

### Available Commands:

- **Run the Application:**
  ```sh
  make run
  ```

- **Install Dependencies:**
  ```sh
  make install
  ```

- **Clean Up Generated Files:**
  ```sh
  make clean
  ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## Contact

For any questions or feedback, please contact [mateusz.gruszka@linux.pl](mailto:mateusz.gruszka@linux.pl).


