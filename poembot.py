import time
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
from PIL import Image, ImageGrab
import csv
import sys
import pyttsx3

engine = pyttsx3.init()

if len(sys.argv) != 2:
    print("Usage: python poembot.py poemwords.csv")
    sys.exit(1)

poemwords_file = sys.argv[1]

# what girl??
girl = input("Who are you writing this poem for? (n, y, s) ")

words = []
# : Read words into memory from file
with open(poemwords_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        words.append({"word": row["word"], "sPoint": int(row["sPoint"]), "nPoint": int(row["nPoint"]), "yPoint": int(row["yPoint"])})
# find sayori words
sWords = []
for word in words:
    if word["sPoint"] == 3:
        sWords.append(word["word"])
# find natsuki words
nWords = []
for word in words:
    if word["nPoint"] == 3:
        nWords.append(word["word"])
# find yuri words
yWords = []
for word in words:
    if word["yPoint"] == 3:
        yWords.append(word["word"])

# wait
time.sleep(5)

def findWord(girl, wordList):
    poemWordCount = 0
    for poemWord in wordList:
        poemWordCount = poemWordCount + 1
        for codeWord in girl:
            if codeWord == poemWord:
                print(poemWord)
                engine.say(poemWord)
                engine.runAndWait()
                return(poemWordCount)
    return(0)

if girl == "n":
    girl = nWords
elif girl == "y":
    girl = yWords
elif girl == "s":
    girl = sWords
else:
    print("Not a valid input")
    sys.exit(1)

for i in range(20):
    #take ss of text
    im1 = ImageGrab.grab(bbox =(1294, 438, 2673, 1695))
    #find text
    text = pytesseract.image_to_string(im1)
    newText = ",".join(text.split())
    #splice it
    wordList = newText.split(",")
    areaCode = findWord(girl, wordList)
    if areaCode == 0:
        sys.exit("No matching words found")
    time.sleep(3)

print("Program done.")
