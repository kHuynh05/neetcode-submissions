class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for i in strs:
            #get value of string and store in hashmap [number:value]
            total = [0] * 26
            for j in i:
                total[ord(j)-97]+=1
            total = tuple(total)
            if(total in anagram):
                anagram[total].append(i)
            else:
                anagram[total] = [i]
        return list(anagram.values())