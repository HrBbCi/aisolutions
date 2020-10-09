import shutil
import time
import os
import requests


def downloadFile(AFileName):
    # extract file name from AFileName
    filename = AFileName.split("/")[-1]
    # download image using GET
    rawImage = requests.get(AFileName, stream=True)
    # save the image recieved into the file
    with open("guitar/" + filename, 'wb') as fd:
        print(filename)
        for chunk in rawImage.iter_content(chunk_size=1024):
            fd.write(chunk)
    return


def main():
    with open("guitar/guitar.txt", "r") as f:
        for url in f:
        	time.sleep(2.5)
            try:
                downloadFile(url)
                time.sleep(1.5)
            except:
                pass


if __name__ == "__main__":
    main()
