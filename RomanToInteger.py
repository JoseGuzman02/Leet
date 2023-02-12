romanDic = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

class Solution(object):
    def __init__(self):
        self.isAfter = False
        self.prevRoman = ''
        self.sum = 0
    def romanToInt(self, s):
        for roman in s:
            self.sum += romanDic[roman]
            #print(roman + " : " + str(self.sum) + " : " + self.prevRoman + " : " + str(self.isAfter))
            # checks if the previous roman numeral is either I, X, C
            if self.isAfter:
                # checks roman numeral I
                if self.prevRoman == 'I':
                    self.sum -= romanDic[self.prevRoman]
                    if roman == 'V':
                        self.sum -= romanDic[self.prevRoman]
                    elif roman == 'X':
                        self.sum -= romanDic[self.prevRoman]
                    else:
                        self.sum += romanDic[self.prevRoman]

                # checks roman numeral X
                elif self.prevRoman == 'X':
                    self.sum -= romanDic[self.prevRoman]
                    if roman == 'L':
                        self.sum -= romanDic[self.prevRoman]
                    elif roman == 'C':
                        self.sum -= romanDic[self.prevRoman]
                    else:
                        self.sum += romanDic[self.prevRoman]

                # checks roman numeral C
                elif self.prevRoman == 'C':
                    self.sum -= romanDic[self.prevRoman]
                    if roman == 'D':
                        self.sum -= romanDic[self.prevRoman]
                    elif roman == 'M':
                        self.sum -= romanDic[self.prevRoman]
                    else:
                        self.sum += romanDic[self.prevRoman]

                self.isAfter = False
                self.prevRoman = ''
                # end of isAfter
            else:
                #  if the roman numeral is I, X, C - hold the value and set isAfter true
                if roman == 'I' or roman == 'X' or roman == 'C':
                    self.isAfter = True
                    self.prevRoman = roman


        return self.sum
        
