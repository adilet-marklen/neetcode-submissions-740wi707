class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        for ch in s:
            hashmap[ch] = hashmap.get(ch, 0) + 1
        
        for ch in t:
            hashmap[ch] = hashmap.get(ch, 0) - 1
        
        for value in hashmap.values():
            if value != 0:
                return False
                
        return True
