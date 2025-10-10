#!/usr/bin/env python3
"""
word_frequency.py
Simple console app: reads a text file, cleans text, counts word frequencies,
and displays summary (total words, unique words, top N).
"""

import re
import sys
from collections import Counter

# Small built-in stopwords set for the optional feature
DEFAULT_STOPWORDS = {
    "the","and","is","in","to","a","of","that","it","on","for","as","with",
    "was","were","this","by","an","be","are","or","from","at","which","but",
    "not","have","has","had","they","you","I","we","he","she","them","his","her"
}

DEFAULT_TOP_N = 10
DEFAULT_MIN_WORD_LEN = 1

def read_text_file_with_retry():
    """Prompt user for file path; allow retry or exit on error."""
    while True:
        path = input("Enter path to text file (or type 'exit' to quit): ").strip()
        if path.lower() == 'exit' or path == '':
            print("Exiting.")
            sys.exit(0)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print("File not found. Type another path or 'exit' to quit.")
        except UnicodeDecodeError:
            # try fallback encoding
            try:
                with open(path, 'r', encoding='latin-1') as f:
                    return f.read()
            except Exception as e:
                print(f"Could not read file (encoding error): {e}")
        except Exception as e:
            print(f"Error opening file: {e}")

def clean_text(text):
    """Lowercase, remove punctuation/special chars, normalize whitespace."""
    text = text.lower()
    # keep letters and digits and whitespace, replace others with space
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    # collapse multiple spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def count_words(text, min_len=DEFAULT_MIN_WORD_LEN, stopwords=None):
    """Return Counter of words after applying min length and stopword filters."""
    if not text or not text.strip():
        return Counter()
    cleaned = clean_text(text)
    words = cleaned.split()
    if min_len > 1:
        words = [w for w in words if len(w) >= min_len]
    if stopwords:
        stopset = set(w.lower() for w in stopwords)
        words = [w for w in words if w not in stopset]
    return Counter(words)

def prompt_positive_int(prompt_msg, default_value):
    s = input(prompt_msg).strip()
    if s == '':
        return default_value
    try:
        v = int(s)
        if v <= 0:
            print("Please enter a positive integer. Using default.")
            return default_value
        return v
    except ValueError:
        print("Invalid integer. Using default.")
        return default_value

def main():
    print("=== Word Frequency Counter ===")
    text = read_text_file_with_retry()
    if not text.strip():
        print("The file is empty. Nothing to do.")
        sys.exit(0)

    # Optional filters (kept simple; user can press Enter for defaults)
    min_len = prompt_positive_int(f"Minimum word length to include (press Enter for {DEFAULT_MIN_WORD_LEN}): ",
                                 DEFAULT_MIN_WORD_LEN)
    use_stop = input("Exclude common stopwords? (y/N): ").strip().lower()
    stopwords = DEFAULT_STOPWORDS if use_stop == 'y' else None

    counts = count_words(text, min_len=min_len, stopwords=stopwords)
    total_words = sum(counts.values())
    unique_words = len(counts)

    if unique_words == 0:
        print("No words found after filtering. Exiting.")
        sys.exit(0)

    top_n = prompt_positive_int(f"How many top words to display? (default {DEFAULT_TOP_N}): ", DEFAULT_TOP_N)
    top_n = min(top_n, unique_words)

    # Display summary
    print("\n--- Summary ---")
    print(f"Total words (after filtering): {total_words}")
    print(f"Unique words: {unique_words}\n")

    print(f"Top {top_n} words (by frequency):")
    print("{:>3} {:<20} {:>6}".format("#", "Word", "Count"))
    for i, (w, c) in enumerate(counts.most_common(top_n), start=1):
        print("{:>3} {:<20} {:>6}".format(i, w, c))

    # Optionally save full output
    save = input("\nSave full word-frequency list to file? (y/N): ").strip().lower()
    if save == 'y':
        out_path = input("Enter output filename (press Enter for 'wordcount_output.txt'): ").strip() or "wordcount_output.txt"
        try:
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(f"Total words: {total_words}\nUnique words: {unique_words}\n\n")
                f.write("Word\tCount\n")
                for w, c in counts.most_common():
                    f.write(f"{w}\t{c}\n")
            print(f"Saved to {out_path}")
        except Exception as e:
            print("Could not save file:", e)

if __name__ == "__main__":
    main()