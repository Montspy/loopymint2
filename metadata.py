import json
import argparse
from os import path, getenv, makedirs
from dotenv import load_dotenv
import traits
import shutil

load_dotenv()

# check for command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--cid", nargs=1, help="Specify starting ID for images", type=int)
args = parser.parse_args()

dataPath = "./metadata"
genPath = dataPath + "/generated"

# Set starting ID
if args.cid:
    cid = args.cid[0]
else:
    cid = getenv("IMAGES_CID")

# Make paths if they don't exist
if not path.exists(genPath):
    makedirs(genPath)
if not path.exists(dataPath):
    makedirs(dataPath)

#### Generate Metadata for each Image

f = open(dataPath + '/all-traits.json')
data = json.load(f)

# Changes this IMAGES_BASE_URL to yours
IMAGES_BASE_URL = "ipfs://" + cid + "/"
COLLECTION_LOWER = traits.COLLECTION_NAME.replace(" ", "_").lower()

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }

for i in data:
    token_id = i['ID']
    token = {
        "name": traits.COLLECTION_NAME + ' #' + str(token_id),
        "image": IMAGES_BASE_URL + COLLECTION_LOWER + "_" + str(token_id) + '.png',
        "animation_url": IMAGES_BASE_URL + COLLECTION_LOWER + "_" + str(token_id) + '.png',
        "royalty_percentage": getenv("ROYALTY_PERCENTAGE"),
        "tokenId": token_id,
        "artist": getenv("ARTIST_NAME"),
        "minter": getenv("MINTER"),
        "attributes": [],
        "properties": {}
    }

    # set the attributes
    n = 1
    for l in traits.layers:
        token["attributes"].append(getAttribute(traits.layers[n]["layer_name"], i[traits.layers[n]["layer_name"]]))
        n = n + 1

    # set the properties
    n = 1
    for l in traits.layers:
        token["properties"][traits.layers[n]["layer_name"]] = i[traits.layers[n]["layer_name"]]
        n = n + 1

    with open(genPath + "/" + COLLECTION_LOWER + "_" + str(token_id) + ".json", 'w') as outfile:
        json.dump(token, outfile, indent=4)

f.close()