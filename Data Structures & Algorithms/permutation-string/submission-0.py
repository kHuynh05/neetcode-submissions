class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0
        set1 = {}
        set2 = {}

        for ch in s1:
            set1[ch] = 1 + set1.get(ch, 0)

        for r in range(len(s2)):
            ch = s2[r]
            set2[ch] = 1 + set2.get(ch, 0)

            # Keep the window the same length as s1
            if r - l + 1 > len(s1):
                left_ch = s2[l]
                set2[left_ch] -= 1

                if set2[left_ch] == 0:
                    del set2[left_ch]

                l += 1

            if set2 == set1:
                return True

        return False