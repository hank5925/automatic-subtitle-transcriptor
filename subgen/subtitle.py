import datetime

check_int = [24, 60, 60, 1000000]

class Subtitle:
    """
    Subtitle
    A data structure that contains a pair of time that indicates starting and
    ending timepoint, and some text for the subtitle.
    We don't check if the given time is legit or not (for example, start_time
    being smaller than end_time, the current start_time being smaller than
    the next start_time, etc.)
    """
    def __init__(self):
        self._data = []
        #self.index = 0

    #def __iter__(self):
        #return self

    #def __next__(self):
        #if self.index + 1 > len(self._data):
            #raise StopIteration
        #self.index = self.index + 1
        #return self._data[self.index]

    def __str__(self):
        s = ""
        #s += "length: %d" % (self.index)
        s += "length: %s" % len(self._data)
        for d in self._data:
            s += "\n" + str(d)
        return s

    def checkIntValid(self, testee, tester):
        if testee >= 0 and testee < tester:
            return True
        return False

    def getLength(self):
        return len(self._data)

    """
    append()
    start_time: [hour(int,0-23)=0, minute(int,0-59)=0, second(int,0-59)=0,
                 microsecond(int,0-999999)=0]
    end_time: [hour(int,0-23)=0, minute(int,0-59)=0, second(int,0-59)=0,
               microsecond(int,0-999999)=0]
    sub: string as the subtitle.
    """
    def append(self, start_time, end_time, sub=""):
        start_list = []
        end_list = []
        d = {}

        for idx, val in enumerate(start_time):
            if self.checkIntValid(val, check_int[idx]) == False:
                raise ValueError("The " + str(idx) + "th value " + str(val) + \
                                 " in start_time is not between 0 and " + \
                                 str(check_int[idx]))
            else:
                start_list.append(int(val))

        for idx, val in enumerate(end_time):
            if self.checkIntValid(val, check_int[idx]) == False:
                raise ValueError("The " + str(idx) + "th value " + str(val) + \
                                 " in end_time is not between 0 and " + \
                                 str(check_int[idx]))
            else:
                end_list.append(int(val))

        if isinstance(sub, str) == False:
            raise TypeError("The sub value is not a string at all.")

        d['start_time'] = start_list
        d['end_time'] = end_list
        d['text'] = sub

        self._data.append(d)
        #self.index += 1;

    def addSubtitle(self, idx, sub):
        if idx >= len(self._data):
            raise IndexError("The index for self._data is out of bound.")
        if isinstance(sub, str) == False:
            raise TypeError("The sub value is not a string at all.")

        self._data[idx]['text'] = sub


    def clean(self):
        del self._data[:]
        #self.index = len(self._data)

