class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        
        num = x
        lst = []
        
        rev = 0
        
        while x>0.9:
            i = x%10 
            rev = rev*10 + (x % 10)
            x/=10
            
        return rev==num
                
            
        
            
            

            
            
        
