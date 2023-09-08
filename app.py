import fitz
import tkinter as tk
from tkinter import filedialog, ttk

def extract_text_from_pdf(pdf_path):
    # Extract text from a PDF file and return it as a string.
    text = ""
    pdf_document = fitz.open(pdf_path)
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()
    return text

def count_word_frequency(text):
    # Count the frequency of each word in the provided text and return a dictionary.
    words = text.split()
    word_count = {}
    for word in words:
        word = word.lower()  # Convert to lowercase to ensure case-insensitive counting
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def sort_words(word_count, sort_by):
    # Sort words either by frequency or alphabetically and return a sorted list of tuples.
    if sort_by == 'Frequency':
        return sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    else:
        return sorted(word_count.items(), key=lambda x: x[0])

def browse_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        pdf_text.delete("1.0", tk.END)  # Clear the previous text
        pdf_text.insert(tk.END, f"Selected PDF: {file_path}\n\n")

        text = extract_text_from_pdf(file_path)
        word_frequency = count_word_frequency(text)
        
        selected_sort = sort_option.get()  # Get the selected sorting option
        
        sorted_words = sort_words(word_frequency, selected_sort)
        
        for word, frequency in sorted_words:
            pdf_text.insert(tk.END, f"{word}: {frequency}\n")

# Create the main GUI window
root = tk.Tk()
root.title("PDF Word Frequency Counter")

# Create a button to browse for PDF files
browse_button = tk.Button(root, text="Browse for PDF", command=browse_pdf)
browse_button.pack()

# Create a sorting option dropdown menu
sort_option_label = tk.Label(root, text="Sort by:")
sort_option_label.pack()
sort_option = ttk.Combobox(root, values=["Frequency", "Alphabetically"])
sort_option.set("Frequency")
sort_option.pack()

# Create a text widget to display PDF text and word frequency
pdf_text = tk.Text(root, wrap=tk.WORD, width=40, height=20)
pdf_text.pack()

# Start the Tkinter main loop
root.mainloop()
