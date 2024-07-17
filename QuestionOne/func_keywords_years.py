import requests

# In this script you give the year and returns you the number of the documentations that have been published in this year 

def fetch_total_documents_for_year_with_keywords(year, keywords):
    base_url = "https://api.zbmath.org/v1/document/_search" # The url where I do the API calls
    formatted_list_keywords = f"({keywords})" # The list with the keywords 
    params = {
        "search_string": f"py: {year} & ( {formatted_list_keywords} )",
        "page": 0,
        "results_per_page": 1  # Set to the minimum since we only need the total count
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        total_results = data.get("status", {}).get("nr_total_results") # The "nr_total_results" gives the number of documentations that have any of listed keywords 
        return total_results
    else:
        print(f"Failed to fetch data: {response.status_code}, Response: {response.text}")
        return None