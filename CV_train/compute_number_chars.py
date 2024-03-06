import pandas as pd 
import sys 

def count_unique_chars(df):
    # Check if the 'wrd' column exists in the DataFrame
    if 'wrd' not in df.columns:
        print("Error: 'wrd' column not found in DataFrame.")
        return

    # Concatenate all strings in the 'wrd' column into a single string
    for el  in list(df["wrd"]):
        if "1" in el:
            print(el)
    all_strings = ''.join(df['wrd'].astype(str))

    # Count the number of unique characters
    unique_chars_count = len(set(all_strings))

    # Print the result
    print(f"Number of unique characters in the 'wrd' column: {unique_chars_count}")
    print(set(all_strings))
# Example usage:
# Assuming 'your_dataframe' is your pandas DataFrame
your_dataframe = pd.read_csv(sys.argv[1])
count_unique_chars(your_dataframe)

