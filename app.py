import fitz
import tkinter as tk
from tkinter import filedialog, ttk
import string
import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

# Stop words list
STOP_WORDS = set([
    "the", "and", "is", "in", "it", "of", "to", "a", "with", "that", "for", "on", 
    "as", "are", "was", "were", "this", "be", "by", "an", "or", "which", "at", 
    "from", "but", "not", "have", "has", "had", "they", "you", "we", "he", "she", 
    "his", "her", "their", "its", "if", "then", "else", "when", "where", "who", 
    "what", "how", "why", "can", "will", "would", "should", "could"
])

def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_document = fitz.open(pdf_path)
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()
    return text

def count_word_frequency(text, filter_stop_words=True):
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    word_count = {}
    for word in words:
        word = word.lower()  # Convert to lowercase to ensure case-insensitive counting
        if filter_stop_words and word in STOP_WORDS:
            continue
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def sort_words(word_count, sort_by):
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
        filter_stop_words = filter_stop_words_var.get()
        word_frequency = count_word_frequency(text, filter_stop_words)
        
        selected_sort = sort_option.get()  # Get the selected sorting option
        sorted_words = sort_words(word_frequency, selected_sort)

        display_top_n = int(top_n_entry.get()) if top_n_entry.get().isdigit() else len(sorted_words)
        sorted_words = sorted_words[:display_top_n]

        for word, frequency in sorted_words:
            pdf_text.insert(tk.END, f"{word}: {frequency}\n")

def export_to_csv():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if file_path:
        text = pdf_text.get("1.0", tk.END)
        lines = text.strip().split('\n')[2:]  # Skip the first two lines (header and empty line)
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Word", "Frequency"])
            for line in lines:
                if line:
                    word, frequency = line.split(": ")
                    writer.writerow([word, frequency])

def search_word():
    query = search_entry.get().lower()
    content = pdf_text.get("1.0", tk.END)
    pdf_text.delete("1.0", tk.END)
    lines = content.strip().split('\n')
    pdf_text.insert(tk.END, f"{lines[0]}\n\n")
    for line in lines[2:]:
        if query in line.lower():
            pdf_text.insert(tk.END, f"{line}\n")

def generate_word_cloud():
    text = pdf_text.get("1.0", tk.END)
    lines = text.strip().split('\n')[2:]  # Skip the first two lines (header and empty line)
    word_freq_dict = {line.split(": ")[0]: int(line.split(": ")[1]) for line in lines if line}
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq_dict)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    
    # Save word cloud to a file
    wordcloud_path = "wordcloud.png"
    wordcloud.to_file(wordcloud_path)
    
    # Display word cloud in the Tkinter window
    img = Image.open(wordcloud_path)
    img = ImageTk.PhotoImage(img)
    wordcloud_label.config(image=img)
    wordcloud_label.image = img

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

# Create an entry to specify the top N words to display
top_n_label = tk.Label(root, text="Display Top N Words:")
top_n_label.pack()
top_n_entry = tk.Entry(root)
top_n_entry.insert(0, "10")  # Default to top 10 words
top_n_entry.pack()

# Create a checkbox to filter out stop words
filter_stop_words_var = tk.BooleanVar()
filter_stop_words_checkbox = tk.Checkbutton(root, text="Filter Stop Words", variable=filter_stop_words_var)
filter_stop_words_checkbox.pack()

# Create a button to export results to CSV
export_button = tk.Button(root, text="Export to CSV", command=export_to_csv)
export_button.pack()

# Create a search bar to search for specific words
search_label = tk.Label(root, text="Search for a word:")
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()
search_button = tk.Button(root, text="Search", command=search_word)
search_button.pack()

# Create a button to generate word cloud
wordcloud_button = tk.Button(root, text="Generate Word Cloud", command=generate_word_cloud)
wordcloud_button.pack()

# Create a label to display the word cloud
wordcloud_label = tk.Label(root)
wordcloud_label.pack()

# Create a text widget to display PDF text and word frequency
pdf_text = tk.Text(root, wrap=tk.WORD, width=50, height=20)
pdf_text.pack()

# Start the Tkinter main loop
root.mainloop()
