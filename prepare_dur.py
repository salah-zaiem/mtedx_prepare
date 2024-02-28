import pandas as pd 
import sys
import os
import random
random.seed(22)
max_dur = 3600*100
max_file = 20
pandas_in =sys.argv[1]
pandas_out = sys.argv[2]


def shuffle_and_select(df, target_duration):
    # Shuffle the DataFrame
    shuffled_df = df.sample(frac=1, random_state=22).reset_index(drop=True)
    shuffled_df = shuffled_df[shuffled_df["duration"]<max_file]
    # Select rows until the sum of 'duration' is higher than the target value
    selected_rows = []
    current_sum = 0

    for index, row in shuffled_df.iterrows():
        selected_rows.append(row)
        current_sum += row['duration']

        if current_sum >= target_duration:
            break

    # Create a new DataFrame with the selected rows
    result_df = pd.DataFrame(selected_rows)

    return result_df


dataframe = shuffle_and_select(pd.read_csv(pandas_in), max_dur)

dataframe.to_csv(pandas_out, index=None)
