import requests

 #type_of_property can either be "traditional" or "airbnb" 

def rental_rates_via_city(city: str, state: str, type_of_property: str)-> dict:

    url = "https://mashvisor-api.p.rapidapi.com/rental-rates"
    querystring = {"state": state, "source": "traditional", "city": city}
    headers = {
        "X-RapidAPI-Key": "8e8fd03760msh5bc972b41b82763p13156fjsn91b722deace6",
        "X-RapidAPI-Host": "mashvisor-api.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

