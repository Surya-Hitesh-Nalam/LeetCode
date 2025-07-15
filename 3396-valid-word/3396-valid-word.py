class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        vowels = 0
        conents = 0
        vowel_set = {'a','e','i','o','u'}

        for ch in word:
            if not ch.isalnum():
                return False
            if ch.isalpha():
                if ch.lower() in vowel_set:
                    vowels+=1
                else:
                    conents+=1
        return vowels>0 and conents>0


        