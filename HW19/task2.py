# https://leetcode.com/problems/roman-to-integer/description/

def romanToInt(s):
    roman_int={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    res = 0
    back_int = 0
    for i in range(len(s) - 1, -1, -1):
        if(back_int/10 == roman_int[s[i]]  or back_int/5 == roman_int[s[i]]):
            res -= roman_int[s[i]]
            back_int = 0
        else:
            res += roman_int[s[i]]
            back_int = roman_int[s[i]]

    return res

print(romanToInt("MCMXCIV"))
