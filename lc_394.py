class Solution:

    def decodeString(self, s: str) -> str:
        return self.recurse(1, s)[0]
        
    def recurse(self, num: int, s: str):
    
        stringy = ""
        i = 0
    
        while i < len(s):
            if s[i] >= '0' and s[i] <= '9':
                new_num = int(s[i])
                i += 1
                while s[i] != '[':     # grab the whole num in case it is longer than one digit
                    new_num *= 10
                    new_num += int(s[i])
                    i += 1
                
                new_s, new_i = self.recurse(new_num, s[i+1:])    # recurse with the rest of the string after the [
                stringy += new_s
                i += new_i
            
            elif s[i] == ']':       # reached the end of the inside string, return (itself * num)
                i += 2
                return self.mult(num, stringy), i
            
            else:                   # add to stringy
                stringy += s[i]
                i += 1

        return stringy, i
                
    # function multiplies string s by num. Ex. 3 * ab = ababab
    def mult(self, num: int, s: str) -> str:
        r = ""
        for j in range(num):
            r += s
            
        return r
