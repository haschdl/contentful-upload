#  Contentful Upload Script 

>> Disclaimer: This script was tested on MacOS only. It depends on MacOS `security` utility.

The script `contentful_upload` is used to upload files as Assets to Contentful.

## Usage

Once you completed the deployment steps, you can call `contentful_upload` from the terminal, passing the arguments.  

 * `-i, --input`  A filename or a directory to upload.
 * `-t, --title` A title to set to the Asset.

## Deploying
Running `deploy.sh` will perform the following tasks:

1. Copy `src/contentful_upload.py`to `$HOME/usr/.local/bin` (removing the py extension)   
2. Make the `contentful_upload` executable
3. Fetch the key-value pairs from from `.env.local` and store them in MacOS key chain as generic passwords.





