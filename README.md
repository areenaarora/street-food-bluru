## Goal
To create a database of eateries (restaurants, bars, street food) in Bangalore that's sortable by user reviews and price ranges. I used Google Maps' API to scrape the data. 
The first challenge was — Google doesn't give out more than 20 results per query and caps results at 60 per search. To start off, I inserted the latitude and longitude for Bangalore from a Google search and made the search radius 20 kms; an arbitrary choice.
Moving forward, I need to figure out how to scale this model to be able to scrape the entire city all at once so that the project is applicable to other cities as well.

### Process
1. Requested an API key from Google Maps
2. Made a request to scrape all eateries from Bangalore using the city's latitude and longitude and looking up "restaurant" in the type of place parameter
3. Tried working on a while loop to be able to get all sixty results possible for one search, but ended up writing out the request manually. Here's the code I used which didn't work (went into an infinite loop)

```py
while True:
    try:
        api_response = gmaps.places_nearby(
            location="12.9716, 77.5946",
            radius=10000,
            type="restaurant",
            page_token=next_page_token
        )
        print(api_response)
        all_results_list.append(api_response.results)
        next_page_token = api_response.next_page_token
    except:
        print(api_response)
```

4. Converted the json into a dataframe, cleaned it up and exported to a CSV
5. Made a preliminary chart using datawrapper