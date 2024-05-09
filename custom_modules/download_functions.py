import requests

def download_rdw_brand(brand_name):
    # uppercase the brand name
    brand_name_upper = brand_name.upper()

    # define the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_name_upper}"
    
    # execute the request
    response = requests.get(endpoint)

    # only proceed when status_code is 200
    if response.status_code == 200:

        # get the data from the response
        data = response.json()

        # check if the data is not empty
        if len(data) == 0:
            raise ValueError(f"No brands found for {brand_name}")

        return data
