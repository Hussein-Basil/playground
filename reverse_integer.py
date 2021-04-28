'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
'''

def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        sign = (-1 if x<0 else 1)
        x *= sign
        result = 0
        
        while x!=0:
            pop = x % 10 # get most right digit (123 --> 3)
            x = int(x/10) # remove it from integer (123 --> 12)
            
            # Ex. we want to get 43 from single 4 and single 3
            # so we multiply left digit by 10 (40) and add right digit (3)
            result = (result * 10) + pop 
            
            if result>=2**31-1 or result=<-2**31:
              return 0
            
        return result * sign
