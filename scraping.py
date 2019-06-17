"""
from bs4 import BeautifulSoup
import requests

def request_webpage(url):
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as e:
        print('There was some problem {}'.format(e))
    return res

#### collecting the movie posters#####

coming_soon = request_webpage('https://www.imdb.com/movies-coming-soon/2019-06/')

#print(coming_soon.text)

coming_soon_soup = BeautifulSoup(coming_soon.text, features='html.parser')
#print(coming_soon_soup.prettify())

details = coming_soon_soup.find('div', attrs={'class': 'list detail'})
image_details = details.find_all('img')

image_list = [img['src'] for img in image_details if 'poster' in img['class']]
#print(image_list)

## Removing everything between v1 and .jpg
## This would get us the full size image.

image_url = image_list[0]
slice_index = image_url.find('_V1_')
full_size_image_url = image_url[:slice_index] + '_v1_.jpg'

########### till here ##########

######################################################################################

##### collecting names ########

## getting the names of all the movies for this month
movies_in_june = request_webpage('https://www.imdb.com/movies-coming-soon/2019-06')
movies_in_june_soup = BeautifulSoup(movies_in_june.text, features='html.parser')

names = movies_in_june_soup.find('div', attrs={'class': 'list detail'})
name_details = names.find_all('h4')
#print(name_details[:5])

name = [x.text for x in name_details]

fp = open('names.txt', 'w+')
for nm in name:
    if "\\" in r'%r' % nm:
        continue 
    fp.write(nm)
    fp.write('\n')
fp.close()

print(name)

#######################################################################

###### collecting the movie posters and putting them in a folder #####

import os

current_month = 'June'
os.mkdir(current_month)

for i in range(len(image_list)):    
    image_url = image_list[i]
    slice_index = image_url.find('_V1_')
    full_size_image_url = image_url[:slice_index] + '_v1_.jpg'
    img_res = request_webpage(full_size_image_url)
    try:
        imageFile = open(os.path.join(current_month, name[i] + '.jpg'), 'wb')
        for chunk in img_res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    except Exception as e:
        print(e)

print('made the folder')
"""
import os
from zipfile import ZipFile

with ZipFile('June.zip', 'w') as zip:
    for fileName in os.listdir('./June/'):
        zip.write('./June/' + fileName)
    