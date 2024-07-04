Take-Home Coding Assessment

Files
- `main.py`: The main script that contains the solution.
- `input_texts.txt`: Sample input file.
- `predefined_words.txt`: Sample predefined words file.
- `Readme.txt`: This file.


Usage:
- Ensure you have your input file (e.g., input_texts.txt) and predefined words file (e.g., predefined_words.txt) in the same directory as the script or adjust the file paths accordingly.
- Run the script using :- python main.py.


Explanation:

load_predefined_words function:
- Reads the predefined words from a file and stores them in a set for quick look-up.

clean_word function:
- Checks if a word ends with a period (.) and removes the period if present.

match_words function:
- Loads the predefined words using the load_predefined_words function.
- Reads the input file line by line, splitting each line into words.
- Cleans each word using the clean_word function.
- Checks if the cleaned word is in the predefined_words set and, if so, adds it to the matched_words set to avoid duplicates.
- Returns the matched words

Main block:
- Sets the file paths for the input file and the predefined words file.
- Calls the match_words function to process the files and prints the matched_words.
