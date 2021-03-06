
import string
#take fundamental freq as input, return dict with alphabets mapped to freqs in order.
class MapOvertones(object):
    def __init__(self):
        self.freqs = []

    def calc(self,fundamental):

        self.fundamental = fundamental
        self.ot1 = self.fundamental
        self.freqs = [self.fundamental]

        for i in range(25):
            ot2 = self.freqs[-1]+self.fundamental
            self.freqs.append(ot2)

        self.out = {letter:freq for letter,freq in zip(string.ascii_lowercase, self.freqs)}

        print(self.out)
        return (self.out)

a = MapOvertones()
a.calc(110)

