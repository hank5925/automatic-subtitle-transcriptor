import math
import datetime
#from subgen.subtitle import Subtitle

#def time_parse(s):
    #hour, minute, second_decimal = [t for t in s.split(':')]
    #second, microsec = second_decimal.split('.')
    #microsec = microsec.ljust(6, '0')
    #return [int(hour), int(minute), int(second), int(microsec)]

def subtitle_parser(sub_file):
    res_start = []
    res_end = []
    res_offset = 0
    with open(sub_file, 'r') as f:
        inEvents = False
        ss = f.readlines()
        for s in ss:
            if inEvents == True:
                sl = s.strip().split(',')
                if sl[1] != ' Start':
                    #rs = time_parse(sl[1])
                    #re = time_parse(sl[2])
                    rs = sl[1]
                    re = sl[2]
                    res_start.append(rs)
                    res_end.append(re)
            else:
                res_offset += len(s)
            if s.strip() == "[Events]":
                inEvents = True
                res_offset += len(s)
    return res_start, res_end, res_offset

#if __name__ == "__main__":
    #import sys
    #import os
    #if os.path.exists(sys.argv[1]) == True:
        #subtitle_parser(sys.argv[1])
    #else:
        #raise FileNotFoundError(sys.argv[0] + ": " + sys.argv[1] + "not found.")
