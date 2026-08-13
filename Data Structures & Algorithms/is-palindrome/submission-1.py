class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = True
        st = list(s)
        s = ""
        for i in st:
            if ord(i)>=97 and ord(i)<=123 or ord(i)>=65 and ord(i)<=91 or ord(i)>=48 and ord(i)<=57:
                s+=i.strip().lower()
        f,b=0,len(s)-1
        print(s)
        while f<=b:
            if s[f]!=s[b]:
                print(f," ",b)
                valid=False
            f+=1
            b-=1
        return valid