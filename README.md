# Komensky taxonomy item uploader

The taxonomy item uploader uploads new skills to the taxonomy classification API.

The following rules apply when uploading.

1. If an item exists the uploader does nothing, the item will not be updated. The existing item is searched by id 
   (skillID)
2. If the item does not exist, the item will be created. The keywords are extracted from the description.

## Installation 
```shell
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt 
```

## Running the scripts
```shell
python3 uploader.py Komensky_skills_16122021.json --api-key=...
```

## Common errors 
```shell
Unexpected response code: 401, reason: Unauthorized
```
The API key is invalid, please make sure to use the provided API key.
