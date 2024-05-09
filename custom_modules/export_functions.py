import os
import pandas as pd


def export_df_csv(df, file_name="export"):

    # create the folder
    os.makedirs(f"data/{file_name}", exist_ok=True)

    # compose the file name
    file_name = f"data/{file_name}/{file_name}.csv"

    # export the data frame
    df.to_csv(file_name, index=False)
    
    print("✅ Succesfully exported ")