Word Frequency Counter (Core Python)

## Project Overview
This mini-project reads a **text file**, processes its content, and analyzes the frequency of each unique word.  
It displays:
- Total number of words  
- Number of unique words  
- Top N most frequent words  

The goal is to demonstrate **file handling**, **string processing**, **exception handling**, and **data analysis** using only **core Python** (no external libraries).

---

## Folder Structure
PROJECT-1/
├── sample_texts/
│ └── sample1.txt # example input file
├── wordfreq.py # main Python script
└── README.md # this documentation file

---

##  Requirements
- Python **3.8+**
- No external libraries needed (uses built-in modules only)

---

##  How to Run the Program
1. Open a terminal or command prompt in the `PROJECT-1` folder.  
2. Run the script:
   python wordfreq.py
3. When prompted:
Enter the path to your text file, for example:
sample_texts/sample1.txt
Press Enter for the default settings or provide your own.
4. The program will display:
Total word count
Unique word count
Top N frequent words (default 10)

Features Implemented
File input (with retry and error handling)
Text cleaning (removes punctuation, converts to lowercase)
Word frequency counting using collections.Counter
Optional stopword removal
Optional minimum word length filter
Option to save results to an output file

Concepts Used

File handling (open, read, write)
Regular expressions (re module)
Dictionaries & collections.Counter
Functions & user input
Exception handling (try/except)
String manipulation

Optional Improvements

You can extend the project with:
Export results as CSV file
Display word cloud visualization (using matplotlib later)
Ignore numeric tokens
Process multiple files in a folder

Author
Sripathi Sanjana Reddy
