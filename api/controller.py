import io
import requests
from PIL import Image
from api.dominantColor import findDominantColor
from api.border import findBorderColor
from api.utils import colorHex

# To GET the image from the URL
def getImage(URL):

    response = requests.get(url=URL, stream=True)
    if response.status_code == 200:
        image_file = io.BytesIO(response.raw.read())
        image = Image.open(image_file)
        return image


# To convert a PNG image to JPG format
def checkPNG(image):
    if str(image.format.lower()) == "png":
        print("hello")
        image = image.convert("RGB")
    return image


# The main controller function to find the
# most dominant and border color of image URL.
def homeController(URL):

    try:
        # Get the image
        image = getImage(URL)

        # Convert if it is in PNG format
        image = checkPNG(image)

        # Find the dominant color
        dominantPixel = findDominantColor(image)

        # Find the Border color
        borderPixel = findBorderColor(image)

        # Return the result
        return {
            "code": 200,
            "message": {
                "dominantColor": colorHex(dominantPixel),
                "borderPixel": colorHex(borderPixel),
            },
        }
    # If exception occurs
    except Exception as e:
        return {"code": 403, "message": "Error Occured"}
