This is the GitHub repository for my project_03 submission for Computing for the Web (CS 40). To see the project instructions click [here](https://github.com/mikeizbicki/cmc-csci040/tree/2022fall/project_03).

My file ebay.dl converts eBay search queries into a `.json` or `.csv` file. First, I used argparse to search for different items on the eBay website. Then, I used a for loop to loop over the ebay webpages. 
Within the for loop I built the url and then downloaded the html using requests and processed the html using bs4 (BeautifulSoup.) 
Finally, I looped over the items on the page to extract the `name` of the item, its `price`, its `status`, the price of `shipping`, the ability to ask for `free_returns`, and the number of `items_sold`.
All this information is included in a dictionary that I created and is outputted on the json or csv files. 
 
To run the ebay-d1 use the command line:
```
PS C:\Users\CHRISTINA\Desktop\cs 40> python ebay-dl.py 'camera'
PS C:\Users\CHRISTINA\Desktop\cs 40> python ebay-dl.py 'water bottle'
PS C:\Users\CHRISTINA\Desktop\cs 40> python ebay-dl.py 'candy'
```
 
Note that this corresponds to my laptop and directory and might need be different for others. Make sure to replace the search term in quotes with your desired item. If you would like to search for items in a specific page make sure to inculde that in your command line. For example:

```
PS C:\Users\CHRISTINA\Desktop\cs 40> python ebay-dl.py 'camera' --num_pages=1
```

If you want to create a csv file instead of a json file make sure to change the command line as following:

```
PS C:\Users\CHRISTINA\Desktop\cs 40> python ebay-dl.py 'camera' --csv=True 
```

 
