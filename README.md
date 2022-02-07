# Where's the best  Biryani at?

Indians love Biryani. Our cities fight over them and we're obsessed with proving ours is the ONE supreme kind. This project will (hopefully) help settle the bet and use data to prove which city REALLY has the best Biryani!

### Goal
To create a database of eateries (restaurants, bars, street food) that's sortable by user reviews and price ranges. I first used Google Maps' API to scrape the data. After a major challenge, I pivoted to using [Zomato]('https://www.zomato.com/') and since Zomato doesn't allow API requests, I used Selenium and Beautiful Soup.

##### *The challenge with using Google Maps API*
*The API doesn't give out more than 20 results per query and caps results at 60 per search. I googled the latitude and longitude values for the intended city and set the search radius as 20 kms— an arbitrary choice. But, to scale this model up, I needed a way to scrape the entire city without having to constantly change lat-long values and get reliable results.*

#### Process and caveats
1. Scraped Zomato using a webdriver with selenium
2. Used Beautiful Soup to parse the page
3. Wrote a function to loop through a list of cities and scrape out user rating and price ranges for each restaurant that delivers Biryani
4. Converted the dataset into a Pandas dataframe and analyzed it
5. Some arbitrary choices made:
- 6 restaurants had "range not given" for their price ranges. I changed them to 100 (most common price range)
- 107 restaurants had no rating value. I changed those to a '0' rating score.

#### Tech stack used
- Python: BeautifulSoup and Pandas
- Selenium
- HTML