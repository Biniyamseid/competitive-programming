class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        "if the first letter is capital all letters have to be capital or all have to be small letters"
        "if the first letter is not capital all letters have not to be capital"
        return (len(word) == 1 or word[1:].islower() or word.isupper())
