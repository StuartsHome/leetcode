# Leetcode 1451. Rearrange Words in a Sentence
# Solution taken from discussions

class Solution:
    def arrangeWords(self, text):
        
        text = sorted(text.split(" "), key=len) # sorted function sorts on length of each word
        text = " ".join(text)       
        return text.capitalize()                # capitalize function lowers the rest of the word
        

Run = Solution()
Run.arrangeWords("Keep calm and code on")

("To be or not to be")


("To be or not to be")




("Leetcode is cool")
        