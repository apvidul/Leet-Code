
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        mul= 1
        
        if x<0:
            x = x*-1
            mul = -1
            
        val=0
        
        while x:
            val = val*10 + (x % 10)
            x = x / 10
           
        
        res = val*mul
        
        max_num =  pow(2, 31)
        
        return 0 if res > max_num - 1 or res < -max_num else res
        

            
        
