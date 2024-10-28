# https://leetcode.com/problems/length-of-last-word/description/

def lengthOfLastWord(s):
    res = 0
    for i in range(len(s)-1, -1, -1):
        if(s[i]==" " and res > 0):
            break
        if((s[i]>="A" and s[i]<="Z") or (s[i]>="a" and s[i]<="z")):
            res += 1
    return res

print(lengthOfLastWord("luffy is still joyboy"))
