class MapOvertones(object):
    def calc(self,fundamental):
        self.alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
        self.fundamental = fundamental
        self.ot1 = self.fundamental
        self.freqs = [self.fundamental]

        for i in range(26):
            ot2 = self.ot1+self.fundamental
            self.freqs.append(ot2)
            self.ot1 = ot2

        self.out = dict()

        i=0
        for letter in self.alph:
            self.out[letter]=self.freqs[i]
            i+=1
        print(self.out)
        return (self.out)
