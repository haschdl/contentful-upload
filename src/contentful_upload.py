#!/usr/bin/env python3

from pickletools import string1
from contentful_management import Client
import argparse
import sys
import os
import subprocess
from pathlib import Path


#Works only on MacOS
def getKeyChain(s):
    cmd=['security','find-generic-password','-s',s,'-w']
    res=subprocess.run(cmd, capture_output=True, text=True)
    if res.stderr:
         raise Exception(res.stderr)
    else:
        return res.stdout


CONTENTFUL_SPACE_ID = str(getKeyChain('CONTENTFUL_SPACE_ID')).rstrip()
CONTENTFUL_ENV = str(getKeyChain('CONTENTFUL_ENV')).rstrip()
CONTENTFUL_API_KEY = str(getKeyChain('CONTENTFUL_API_KEY')).rstrip()

print("Using secrets from MacOS Key Chain. Contentful Space ID: " + CONTENTFUL_SPACE_ID)


# Other restrictions
EXT_ALLOWED=['.png','.jpeg','.jpg']


parser = argparse.ArgumentParser(description='Uploads files to Contentful')
parser.add_argument('-i', '--input', type=str,
                    help='A file or folder containing files', required=True)
parser.add_argument('-t', '--title', type=str,
                    help='Title to be assigned to the assets', required=True)

parser.add_argument('-m', '--markdown', type=str,
                    help='A file containing markdown text to be used in the description field.', required=True)

args = parser.parse_args()

MODE_FILE = "files"
MODE_DIR = "dir"
mode = MODE_FILE
file = ""

# Checking if input is file or dir
if (os.path.isdir(args.input)):
    mode = MODE_DIR
    dir = args.input
    print("Using directory as input.")
else:
    print("Using a single file as input.")
    file = args.input


if (mode == MODE_FILE and not os.path.exists(file)):
    raise Exception("File does not exist:" + file)

# /Users/hasci/Creative Cloud Files/H Scheidl E commerce material/Products/2020-03 Moon

client = Client(CONTENTFUL_API_KEY)
space = client.spaces().find(CONTENTFUL_SPACE_ID)

def uploadAsset(filepath,title):
    fileName = os.path.basename(filepath)
    print(f"Uploading: {fileName}")

    upload = client.uploads(CONTENTFUL_SPACE_ID).create(filepath)

    print("Upload result:" + upload.id)
    uploadId = upload.id

    asset = client.assets(CONTENTFUL_SPACE_ID, CONTENTFUL_ENV).create(None,
                                            {
                                                "fields": {
                                                    "title": {
                                                        "en-US": title
                                                    },
                                                    "file": {
                                                        "en-US": {
                                                            "contentType": "image/png",
                                                            "fileName": fileName,
                                                            "uploadFrom": {
                                                                "sys": {
                                                                    "type": "Link",
                                                                    "linkType": "Upload",
                                                                    "id": uploadId
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                            )

    return asset.process()

if (mode == MODE_FILE):
    asset=uploadAsset(file,args.title)
    print(asset)

if (mode == MODE_DIR):
    files = os.listdir(dir)
    #filtering by extension
    files = [f for f in files if Path(f).suffix in EXT_ALLOWED]
    files = [os.path.join(dir,f) for f in files if os.path.isfile(os.path.join(dir,f))]
    
    print(files)
    
    print("A total of %d files will be uploaded." % len(files))
    if input("Yes to continue? (y/n)") != "y":
        exit()
    for f in files:
        asset=uploadAsset(f,args.title)
        print(asset)
