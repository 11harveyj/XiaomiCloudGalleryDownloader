import requests
import os
import shutil
import datetime


while (True):
    auth_header = {'Cookie': input('Enter Cookie from i.mi.com after logging in: ')}
    response = requests.get('https://i.mi.com/gallery/user/galleries?startDate=19500101&endDate={}'.format(datetime.datetime.now().strftime('%Y%m%d')), headers=auth_header)
    try:
        galleries = response.json().get("data").get("galleries")
        print("Got response from i.mi.com")
        break
    except:
        print("Seems like the Cookie you have provided may have expired, try again")

destPath = input('Enter destination folder path: ')


def download_file(url, destFolder, fileName):
    folder_path = destFolder
    path = os.path.join(folder_path, fileName)

    if (os.path.exists(path)):
        print("Already downloaded this")
    else:
        with requests.get(url, stream=True) as r:
            with open(path, "wb") as f:
                shutil.copyfileobj(r.raw, f)

    return path

for i in galleries:
    fileName = i.get("fileName")
    imgInfo = i.get("bigThumbnailInfo")
    isUrl = imgInfo.get("isUrl")
    data = imgInfo.get("data")
    print("Saving {}..".format(fileName))
    try:
        print("Saved {} to {}".format(fileName, download_file(data, destPath, fileName)))
    except:
        print("Unable to download {}".format(fileName))
    
