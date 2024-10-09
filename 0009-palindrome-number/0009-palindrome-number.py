class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        lunghezza = len(x)
        i = 0
        for i in range (lunghezza):
            if(x[i] == x[lunghezza - 1]):
                lunghezza -= 1
            else:
               break
        if (lunghezza == 0):
            return True
        else:
            return False       

 