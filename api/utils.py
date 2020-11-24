# To find the max frequency
def findMaxFrequency(pixelList):
    maxFreq, maxFreqIndex = 0, 0
    for index in range(len(pixelList)):
        if maxFreq < pixelList[index]:
            maxFreq = pixelList[index]
            maxFreqIndex = index
    return maxFreqIndex


# Convert a decimal number to Hexadecimal
def convertToHexaDecimal(number):
    if int(number) < 16:
        return "0{}".format(hex(number).lstrip("0x").rstrip("L"))
    else:

        return hex(number).lstrip("0x").rstrip("L")


# Convert a RGB color value array to hexadecimal color format
def colorHex(color):
    return "#{red}{green}{blue}".format(
        red=convertToHexaDecimal(color[0]),
        green=convertToHexaDecimal(color[1]),
        blue=convertToHexaDecimal(color[2]),
    )
