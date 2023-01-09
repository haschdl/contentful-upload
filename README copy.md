---
title: Contentful Upload Script
---

#  Contentful Upload Script 

>> Disclaimer: This script was tested on MacOS only. It depends on MacOS `security` utility.

The script `contentful_upload` is used to upload files as Assets to Contentful.

## Getting started

> You need to have a Contentful account and one [Content Management API Key](https://www.contentful.com/developers/docs/references/authentication/#the-content-management-api).

1. Clone this repository
2. Copy or rename `.env.local.template` to `.env.local`
3. Paste your API keys into `.env.local``
    ```
    CONTENTFUL_SPACE_ID="cccc"
    CONTENTFUL_ENV="master"
    CONTENTFUL_API_KEY="dssdsd"
    ```
4. Execute `deploy.sh` 

## Usage

Once you completed the deployment steps, you can call `contentful_upload` from the terminal, passing the arguments.  

 * `-i, --input`  A filename or a directory to upload.
 * `-t, --title` A title to set to the Asset.

## Deployment details

Running `deploy.sh` will perform the following tasks:

1. Copy `src/contentful_upload.py`to `$HOME/usr/.local/bin` (removing the py extension)   
2. Make the file `contentful_upload` executable
3. Fetch the key-value pairs from from `.env.local` and store them in MacOS key chain as generic passwords.

## Known issues

1. The functionality to upload text content is not yet implemented.
2. A btter approach for the `deployment` would be for `deploy.sh` to ask for the credentials in the terminal, so the secret is not stored in `.env.local`



