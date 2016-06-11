import sys
import os
from subgen.subtitle import Subtitle

def main():
    if (len(sys.argv) != 3):
        print("Usage: " + sys.argv[0] + " subtitle.ass audio.mp3")
        return -1
    elif (os.path.exists(sys.argv[1]) == False):
        print(sys.argv[0] + ": subtitle file " + sys.argv[1] + " not found.")
        return -1
    elif (os.path.exists(sys.argv[2]) == False):
        print(sys.argv[0] + ": audio file " + sys.argv[1] + " not found.")
        return -1

    print("Success!")

    subtitle = Subtitle()
    subtitle.append([0,0,1], [0,0,2], "dude.")
    subtitle.append([0,10,1,273000], [0,10,2,343000], "what the heck.")
    print(subtitle)
    #subtitle.clean()
    #print(subtitle)


if __name__ == "__main__":
    main()
