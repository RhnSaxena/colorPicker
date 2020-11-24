import numpy as np
from PIL import Image
from api.utils import findMaxFrequency


# The function to update the frequency of intensity value
#  of a particular channel as per the bloc dimensions
def findFrequencies(imageArray, channel, block):

    for row in range(block["rowStart"], block["rowEnd"]):
        for column in range(block["colStart"], block["colEnd"]):

            redValue = imageArray[row][column][0]
            blueValue = imageArray[row][column][1]
            greenValue = imageArray[row][column][2]

            channel[0][redValue] = channel[0][redValue] + 1
            channel[1][blueValue] = channel[1][blueValue] + 1
            channel[2][greenValue] = channel[2][greenValue] + 1


# The function to fing the border color of the image
def findBorderColor(img):
    # Creating array of the image pixel values
    imageArray = np.array(img)

    # Initializing the height and width of the image
    height = len(imageArray)
    width = len(imageArray[0])

    # Initializing the channels
    # with initial value as '0'
    red = [0] * 256
    green = [0] * 256
    blue = [0] * 256
    channels = [red, green, blue]

    # Setting the border size as 10
    borderSize = 10

    # Setting border definitions
    borderDef = {
        "top": {"rowStart": 0, "rowEnd": borderSize, "colStart": 0, "colEnd": width},
        "left": {
            "rowStart": borderSize,
            "rowEnd": height - borderSize,
            "colStart": 0,
            "colEnd": borderSize,
        },
        "right": {
            "rowStart": borderSize,
            "rowEnd": height - borderSize,
            "colStart": width - borderSize,
            "colEnd": width,
        },
        "bottom": {
            "rowStart": height - borderSize,
            "rowEnd": height,
            "colStart": 0,
            "colEnd": width,
        },
    }

    # Find the frequency of intensity values for each block definition
    for block in borderDef:
        findFrequencies(imageArray, channels, borderDef[block])

    # return the intensity value with highest frequency
    return [findMaxFrequency(red), findMaxFrequency(green), findMaxFrequency(blue)]
