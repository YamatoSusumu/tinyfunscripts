#Import required libraries:
import nasapy
import os
from datetime import datetime
import requests
from tqdm import tqdm

#Initialize Nasa class by creating an object:
k = "523p5hPYHGzafYGLCkqa54kKMTV2vbP0XcPxkcLm" # demo api, allows 50 calls per day
nasa = nasapy.Nasa(key = k)

#Get today's date in YYYY-MM-DD format:
d = datetime.today().strftime('%Y-%m-%d')

#Get the image data:
apod = nasa.picture_of_the_day(date=d, hd=True)

#Check the media type available:
if(apod["media_type"] == "image"):
    
    #Displaying hd images only:
    if("hdurl" in apod.keys()):
        
        #Saving name for image:
        title = apod["title"].replace(" ","_").replace(":","_") + ".jpg"
        
        #Path of the directory:
        image_dir = "./Astro_Images"
 
        #If it doesn't exist then make a new directory:
        if (os.path.exists(image_dir) == False):
            os.makedirs(image_dir)

        ans = input("Downlaod | " + apod["title"] + " (y/n) ")
        if (ans == "n"):
            quit()
        #Retrieving the image:
        url = apod["hdurl"]
        fname = os.path.join(image_dir,title)

        resp = requests.get(url, stream=True)
        total = int(resp.headers.get('content-length', 0))
        with open(fname, 'wb') as file, tqdm(
            desc="Downloading",
            total=total,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for data in resp.iter_content(chunk_size=1024):
                size = file.write(data)
                bar.update(size)


        #get information related to image:
        image_discrp = ""
        if("date" in apod.keys()):
            image_discrp = "Date image released: " + apod["date"]
        if("copyright" in apod.keys()):
            image_discrp += "\nThis image is owned by: " + apod["copyright"]
        if("title" in apod.keys()):
            image_discrp += "\n\nTitle of the image: " + apod["title"]
        if("explanation" in apod.keys()):
            image_discrp += "\n\nDescription for the image: " + apod["explanation"]
        if("hdurl" in apod.keys()):
            image_discrp += "\n\nURL for this image: "+ apod["hdurl"]

        answer = input("Do you want to also download image info (y/n) ")
        if (answer == "y"):
            with open(fname[:-4:] + ".txt", "x") as file_object:
                file_object.write(image_discrp)

        
#If media type is not image:
else:
    print("Sorry, Image not available!")

