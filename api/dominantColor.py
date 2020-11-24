from PIL import Image
from api.utils import findMaxFrequency

# To find the dominant color
def findDominantColor(img):

    r, g, b = img.split()
    return [
        findMaxFrequency(r.histogram()),
        findMaxFrequency(g.histogram()),
        findMaxFrequency(b.histogram()),
    ]
