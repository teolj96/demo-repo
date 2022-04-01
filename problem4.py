from bs4 import BeautifulSoup
import requests

url = 'https://kamernet.nl/huren/kamers-nederland'

for i in range(0,5): # ONLY 5 PAGES FOR THIS PROGRAM
    source = requests.get(url).text

    soup = BeautifulSoup(source, 'html.parser')

    rooms = soup.find_all('div', class_='rowSearchResultRoom col s12 m6 l4')

    for room in rooms:
        link = room.find('a', class_='tile-title truncate')['href'] #LINK
        new_source = requests.get(link).text
        new_soup = BeautifulSoup(new_source,'html.parser')
        location = new_soup.find('div',class_='h1_line3').text.split(' ')[1] #LOCATION
        size = new_soup.find('div',class_='surface').text #ROOM SIZE
        price = new_soup.find('div',class_='price').text #PRICE
        available = new_soup.find('div',class_='availability').text.split(' ')[3] #AVAILABILITY
        description = new_soup.find('div',class_='col s12 m12 l8 offset-l2 no-padding description').div.text #DESCRIPTION

        print(f'''
        Room link: {link}
        Room location: {location}
        Room size: {size}
        Room price: {price}
        Room availabilty: {available}
        Room description: {description}
        ''')
        print('')

    url = 'https://kamernet.nl/huren/kamers-nederland'+f'?pageno='+str(i+1)
