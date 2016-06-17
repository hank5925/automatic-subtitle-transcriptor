import sys
import os
from subgen import subtitle_parsing

import datetime
import json

def main():
    # Input Handling
    if (len(sys.argv) != 3):
        raise TypeError("Usage: " + sys.argv[0] + " subtitle.ass audio.mp3")
    elif (os.path.exists(sys.argv[1]) == False):
        raise FileNotFoundError(sys.argv[0] + ": subtitle file " + sys.argv[1] + "not found.")
    elif (os.path.exists(sys.argv[2]) == False):
        raise FileNotFoundError(sys.argv[0] + ": audio file " + sys.argv[2] + "not found.")

    # Timeline Parsing
    list_start, list_end, offset = subtitle_parsing.subtitle_parser(sys.argv[1])
    list_size = len(list_start)
    assert(len(list_start) == len(list_end))
    list_duration = [(datetime.datetime.strptime(ts[1], '%H:%M:%S.%f')\
                    - datetime.datetime.strptime(ts[0], '%H:%M:%S.%f')) for ts in zip(list_start, list_end)]

    # Audio File Cutting, and change to wav, and call transctiption.
    if os.path.isdir('wav') == False:
        os.system('mkdir wav')

    if os.path.isdir('json') == False:
        os.system('mkdir json')
    
    # Write to output file.
    (subname, subext) = os.path.splitext(sys.argv[1])
    outsubpath = subname + '_out' + subext

    #cmd1 = ' '.join(['cp', sys.argv[1], outsubpath])
    #os.system(cmd1)

    with open(outsubpath, 'w') as f:
        for idx in range(list_size):
            print()
            print('######## ROUND ' + str(idx) + ' ########')
            filename = str(idx).zfill(5) + '.wav'
            jsonname = str(idx).zfill(5) + '.json'
            filepath = os.path.join('wav', filename)
            jsonpath = os.path.join('json', jsonname)

            # IBM Speech To Text API accepts .wav format
            #cmd = 'ffmpeg -y -ss 00:00:17.46 -t 0:00:04.32 -i audio.mp3 audio_out.mp3'
            cmd2 = 'ffmpeg -y -ss {} -t {} -i {} {}'.format(list_start[idx], list_duration[idx], sys.argv[2], filepath)
            os.system(cmd2)

            # IBM Speech To Text API
            # TODO: REMEMBER TO REPLACE THE -u LINE TO YOUR OWN USER/PASSWORD!!!!
            cmd3 = 'curl -X POST '\
                    + '-u "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx":"xxxxxxxxxxxx" '\
                    + '--header "Content-Type: audio/wav" '\
                    + '--data-binary @' + filepath + ' '\
                    + '"https://stream.watsonplatform.net/speech-to-text/api/v1/recognize'\
                    + '?timestamps=true&word_alternatives_threshold=0.9"'\
                    + ' > ' + jsonpath
            os.system(cmd3)

            # Parse result json and directly write to output file
            with open(jsonpath, 'r') as g:
                d = json.load(g)
                f.write(d['results'][0]['alternatives'][0]['transcript'] + '\n')


if __name__ == "__main__":
    main()
