def findGCD(s: str, t: str, gcd: str = '', largestGCD: str = ''):
    if len(t) == len(gcd):
        return largestGCD
    gcd = t[:len(gcd) + 1]
    mockS = gcd * (len(s) // len(gcd))
    mockT = gcd * (len(t) // len(gcd))
    if mockS == s and mockT == t:
        largestGCD = gcd 
    
    return findGCD(s, t, gcd, largestGCD)

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return findGCD(str1, str2)
