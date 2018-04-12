"""
This script uses data from inside airbnb
and downloads images based on data there (the urls)

inside airbnb only has one picture per listing
rather than scraping multiple images
"""

import urllib
import pandas as pd
import urllib.request
import time
import os

def process_images(listings_img):
    """
    # to download images from url to filesystem...
    urllib.request.urlretrieve(img_loc, fs_loc)
    """
    for nrow, mdict in enumerate(listings_img):
        idx = mdict['id']
        img = mdict['picture_url']

        img_loc, _ = img.split(".jpg", 1)
        #basenm = os.path.basename(img_loc)+".jpg"
        img_loc = img_loc+".jpg"

        pathnm = "room_{}".format(idx)
        if not os.path.exists(pathnm):
            os.makedirs(pathnm)
            try:
                urllib.request.urlretrieve(img_loc, "{}/0.jpg".format(pathnm))
            except Exception as e:
                print("\t{}".format(e))
                print("\tFailed to process: {}".format(idx))
            time.sleep(0.5) # reduce flooding...
        else:
            if not os.path.exists("{}/0.jpg".format(pathnm)):
                try:
                    urllib.request.urlretrieve(img_loc, "{}/0.jpg".format(pathnm))
                except Exception as e:
                    print("\t{}".format(e))
                    print("\tFailed to process: {}".format(idx))
                time.sleep(0.5) # reduce flooding...
            print("Skipping row number: {}, id: {}".format(nrow, idx))
        if nrow % 100 == 0:
            print("Processing row number: {}".format(nrow))

if __name__ == "__main__":
    listings = pd.read_csv("data/listings.csv.gz", compression='gzip')

    # we shall use listings[['id', 'picture_url']]
    # to get the required information and download the correct data

    # listings = pd.read_csv("data/listings.csv.gz", compression='gzip')
    # listings.columns

    listings_img = listings.to_dict(orient='records')
    print("Attempting to download {} images".format(len(listings_img)))

    process_images(listings_img)
