import requests



base_mealdb_url = "https://www.themealdb.com/api/json/v1/1/search.php"

def fetch_data_from_mealdb(s):
    query_params = "?s={}".format(s)
    
    final_url = base_mealdb_url + query_params
    response = requests.get(final_url)
    extract_data(response)
    # print(response.text)


def extract_data(response):
    response_json = response.json()
    for meal in response_json["meals"]:
        print(meal["strMeal"],"\nInstructions:\n",meal["strInstructions"])

if __name__ == "__main__":
    fetch_data_from_mealdb("dal")