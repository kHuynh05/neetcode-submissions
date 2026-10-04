class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        pos = 0
        while(pos < len(s)):
            num = ""
            while(s[pos] != "#"):
                num += s[pos]
                print(num)
                pos += 1
            pos +=1
            num = int(num)
            decoded.append(s[pos:pos+num])
            pos = pos + num
        return decoded