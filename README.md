This is the GitHub repository for my project_03 submission for Computing for the Web (CS 40). To see the project instructions click [here](https://github.com/mikeizbicki/cmc-csci040/tree/2022fall/project_03).

My file ebay.d1 converts eBay search queries into a json or csv file. First I used argparse to search for different items on the eBay website. Then, I used a for loop to loop over the ebay webpages. 
Within the for loop I built the url and then downloaded the html using requests and processed the html using bs4 (BeautifulSoup.) 
Finally, I looped over the items on the page to extract the `name` of the item, its `price`, its `status`, the price of `shipping`, the ability to ask for `free_returns`, and the number of `items_sold`.
All this information is included in a dictionary that I created and is outputted on the json or csv files. 
 
To run the ebay-d1 use the command line:
```
PS C:\Users\CHRISTINA\Desktop\cs 40> python ebay.py 'camera'
PS C:\Users\CHRISTINA\Desktop\cs 40> python ebay.py 'water_bottle'
PS C:\Users\CHRISTINA\Desktop\cs 40> python ebay.py 'pen'
```
 
Note that this corresponds to my laptop and directory and might need be different for others. 
 
To run the ebay-d1 use the command line:
