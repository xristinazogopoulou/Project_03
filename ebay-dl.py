import argparse
import requests
from bs4 import BeautifulSoup
import json
import csv

def parse_itemssold(text): 
    '''
    takes as input a string and returns the number of items sold, as specified in the string
    >>> parse_itemssold('195 sold')
    195
    >>> parse_itemssold('4 watchers')
    0
    >>> parse_itemssold('Last one')
    0
    '''
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers += char
    if 'sold' in text:
        return int(numbers) 
    else:
        return 0  

def parse_shipping(text):
   
    '''
    >>> parse_shipping('Free shipping')
    0
    >>> parse_shipping('+$10.60 shipping')
    1060
    >>> parse_shipping('+$5.99 shipping')
    599
    '''
    shipping=''
    if text[0]=='+':
        for s in text:
            if s in '1234567890':
                shipping+=s
            elif s==' ':
                break
        return int(shipping)
    else:
        return 0

def parse_price(text):
    price =''
    for char in text: 
        if char in '1234567890':
                price+=char
        elif char==' ':
                break
    if '$' in text:
        return int(price)
    else:
        return 0
        

# only run the code below when the python file is run 'normally'
# where normally means not in doctest 
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Download information from ebay and convert to JSON.')
    parser.add_argument('search_term')
    parser.add_argument('--num_pages', default=10) 
    parser.add_argument('--csv', default =False) 
    args = parser.parse_args()

    print('args.search_term=', args.search_term)

    #list of all items found in all ebay webpages
    items =[]

    #loop over the ebay webpages
    for page_number in range (1,int(args.num_pages)+1):

        #build the url
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw='
        url += args.search_term 
        url += '&_sacat=0&LH_TitleDesc=0&_pgn='
        url += str(page_number)
        url += '&rt=nc'
        print('url=', url)

        #download the html
        r = requests.get(url)
        status = r.status_code
        print ('status=', status) 
        html = r.text

        #process the html
        soup = BeautifulSoup(html, 'html.parser')

        #loop over the items on the page
        tags_items = soup.select('.s-item')
        for tag_item in tags_items:

            #extract the name
            name = None
            tags_name= tag_item.select('.s-item__title')
            for tag in tags_name:
                name = tag.text

            #extract the freereturns 
            freereturns = False
            tags_freereturns = tag_item.select('.s-item__free-returns')
            for tag in tags_freereturns:
                freereturns = True

            #extract the items_sold
            items_sold = None 
            tags_itemssold = tag_item.select ('.s-item__quantitySold')
            for tag in tags_itemssold:
                items_sold = parse_itemssold(tag.text)

            #extract the status
            status = None
            tags_status = tag_item.select('.SECONDARY_INFO')
            for tag in tags_status:
                status = tag.text

            tags_price=tag_item.select('.s-item__price')   
            price=None
            for tag in tags_price:
                price=parse_price(tag.text)


            #extract the shipping price
            tags_shipping = tag_item.select('.s-item__shipping, .s-item__freeXDays')
            shipping = None
            for tag in tags_shipping:
                shipping=parse_shipping(tag.text)

            item = {'name': name, 
            'free_returns': freereturns,
            'items_sold': items_sold,
            'status': status,
            'shipping': shipping,
            'price': price}
            items.append(item)

        print('len(tags_items)=', len(tags_items))
        print('len(items)=', len(items)) 

if args.csv:
    field_names=list(items[0].keys())
    csv_filename = args.search_term+'.csv'
    with open(csv_filename, 'w', encoding ='utf-8') as f: 
        writer = csv.DictWriter(f, fieldnames = field_names)
        writer.writeheader()
        writer.writerows(items)
else:
    filename = args.search_term+'.json'
    with open(filename, 'w', encoding = 'ascii') as f:
        f.write(json.dumps(items))


   
