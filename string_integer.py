'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
More Info : https://leetcode.com/problems/string-to-integer-atoi/
'''

def myAtoi(s):
   
    result = 0
    sign = 1
    seen_operator = False
    seen_sequence = False
    
    for character in s:
        
        if (character == ' ') and not(seen_sequence or seen_operator):
            continue
        
        elif (character in ['-','+']) and not (seen_sequence or seen_operator):
            sign = (-1 if character=='-' else 1)
            seen_operator = True


        elif character.isdigit():
            result = (result * 10) + int(character)
            seen_sequence = True

            if result > 2**31-1:
                result = (2**31 if sign==-1 else 2**31-1)
        
        else:
            break
    
    return result * sign
