import re


def anagram_number(number):
    numberlist = str(number)
    reversenumber = numberlist[::-1]
    return (reversenumber == numberlist)

roman ={'I':1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D': 500, 'M':1000, 'TV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
    
def roman_to_int(s):
    ret = sum(roman[key] for key in re.fidall(r'I[XV]|X[LC]|C[DM]|[IVXLXDM]',s))

if __name__=="__main__":
     print (roman_to_int("XLXC"))