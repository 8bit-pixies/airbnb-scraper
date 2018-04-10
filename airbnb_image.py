
import requests
import urllib.request
import os
from bs4 import BeautifulSoup

sample_page = 'https://www.airbnb.com.au/rooms/18285386'
page = requests.get(sample_page)

soup = BeautifulSoup(page.content, 'html.parser')

# download all images that are under class slideshow images pattern
all_img = soup.find_all("img")

for img in all_img:
    #print(img['src'])
    try:
        img_nm = img['src']
        if 'jpg' in img_nm:
            #print(img_nm)
            img_loc, type_pic = img_nm.split(".jpg", 1)
            if 'profile' in type_pic:
                continue
            basenm = os.path.basename(img_loc)+".jpg"
            img_loc = img_loc+".jpg"
            urllib.request.urlretrieve(img_loc, basenm)
            #print("tried to download: ", img_loc)
        else:
            pass
            #print(img_nm)
    except Exception as e:
        print(e)

def get_images(airbnb_id):
    page_path = "https://www.airbnb.com.au/rooms/{}".format(airbnb_id)
    page = requests.get(page_path)
    soup = BeautifulSoup(page.content, 'html.parser')

    all_img = soup.find_all("img")
    
    for idx, img in enumerate(all_img):
        #print(img['src'])
        try:
            img_nm = img['src']
            if 'jpg' in img_nm:
                #print(img_nm)
                img_loc, type_pic = img_nm.split(".jpg", 1)
                if 'profile' in type_pic:
                    continue
                basenm = os.path.basename(img_loc)+".jpg"
                img_loc = img_loc+".jpg"
                if not os.path.exists(airbnb_id):
                    os.makedirs(airbnb_id)
                urllib.request.urlretrieve(img_loc, "{}/{}.jpg".format(airbnb_id, idx))
                #print("tried to download: ", img_loc)
            else:
                pass
                #print(img_nm)
        except Exception as e:
            print(e)

get_images('18285386')