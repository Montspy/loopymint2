""" START COMMENT SECTION

Consider the lowest number to be your background layer. Then you are adding new layers on top in order.

You must have at least 2 layers to run this script.

Only change the values and layer numbers in the layers dictionary.

Add as many layers as you need, just remember to increase the layer number when copying a new section.

Add as many "filenames" and "weights" as needed.

    1. You have to have the same amount of weights as you do filenames.
    2. When you add up all the weights together, they must equal exactly 100.

    What you're doing is setting a "percentage chance this item gets picked"

An Example of 1 Layer:

1: {
    "layer_name": "Pretty Trait Name 0X",
    "filenames": {
        "Pretty Item Name 01": "item_01.png",
        "Pretty Item Name 02": "item_02.png"
    },
    "weights": [
        50,
        50
    ]
}

END COMMENT SECTION """

## Give the collection a name
COLLECTION_NAME="Collection Title"

## Layers dictionary
layers = {
    1: {
        "layer_name": "Pretty Trait Name 01",
        "filenames": {
            "Pretty Item Name 01": "item_01.png",
            "Pretty Item Name 02": "item_02.png"
        },
        "weights": [
            50,
            50
        ]
    },
    2: {
        "layer_name": "Pretty Trait Name 02",
        "filenames": {
            "Pretty Item Name 01": "item_01.png",
            "Pretty Item Name 02": "item_02.png"
        },
        "weights": [
            50,
            50
        ]
    }
}
