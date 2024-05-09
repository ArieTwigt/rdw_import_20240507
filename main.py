from custom_modules.download_functions import download_rdw_brand
from custom_modules.conversion_functions import convert_list_to_df
from custom_modules.export_functions import export_df_csv

# get the brand from the input
selected_brand = input("Select a brand:\n")

# use the function with the brandh
cars_list = download_rdw_brand(selected_brand)

# convert the cars_list to a DataFrame
cars_df = convert_list_to_df(cars_list)

# export the data frame
export_df_csv(cars_df, selected_brand)

pass