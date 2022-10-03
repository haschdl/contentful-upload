echo "Copying file to $HOME"
cp src/contentful_upload.py $HOME/.local/bin/contentful_upload
echo "Update permissions, make file executable"
chmod +x $HOME/.local/bin/contentful_upload
echo "Exporting required environment variables"
#export $(grep -v '^#' .env.local | xargs)

input="./.env.local"
while IFS= read -r line
do
    key=${line%%\=*}
    value=${line##*\=}       
    echo "Adding new generic password to key chain: [$key]"
    security add-generic-password -a "$USER" -s $key -w $value -U
    echo .
done < "$input"
