import pandas as pd

def convert_list_to_df(input_list):

    # convert the list of cars to a pandas DataFrame
    df = pd.DataFrame(input_list)

    return df