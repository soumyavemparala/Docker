import re
from collections import Counter
import socket
import os

# Create output directory if it doesn't exist
output_dir = '/home/data/output'
os.makedirs(output_dir, exist_ok=True)

# Function to handle contractions
def handle_contractions(text):
    # Splitting common contractions into separate words
    contractions = {
        "can't": "cannot", "won't": "will not", "don't": "do not", 
        "i'm": "i am", "they're": "they are", "it's": "it is"
    }
    for contraction, full_form in contractions.items():
        text = text.replace(contraction, full_form)
    return text

# Function to count words in a text file
def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().lower()
        text = handle_contractions(text)
        words = re.findall(r'\b\w+\b', text)  # Regular expression to extract words
        return words

# Read the files and count words
words_if = count_words('/home/data/IF.txt')
words_arutw = count_words('/home/data/AlwaysRememberUsThisWay.txt')

# Total word count
total_if = len(words_if)
total_arutw = len(words_arutw)
grand_total = total_if + total_arutw

# Top 3 frequent words for both files
top_3_if = Counter(words_if).most_common(3)
top_3_arutw = Counter(words_arutw).most_common(3)

# Get IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Write results to result.txt
result_file_path = os.path.join(output_dir, 'result.txt')
with open(result_file_path, 'w') as f:
    f.write(f"Word count for IF.txt: {total_if}\n")
    f.write(f"Word count for AlwaysRememberUsThisWay.txt: {total_arutw}\n")
    f.write(f"Grand total word count: {grand_total}\n\n")
    f.write(f"Top 3 frequent words in IF.txt: {top_3_if}\n")
    f.write(f"Top 3 frequent words in AlwaysRememberUsThisWay.txt: {top_3_arutw}\n\n")
    f.write(f"IP address of the machine: {ip_address}\n")

# Print the content of result.txt to the console
with open(result_file_path, 'r') as f:
    print(f.read())
