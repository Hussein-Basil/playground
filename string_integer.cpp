#include<iostream>
#include<string>
using namespace std;

/*
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
More Info : https://leetcode.com/problems/string-to-integer-atoi/
*/

int myAtoi(string str) {
    int i = 0;
    int sign = 1;
    int result = 0;
    if (str.length() == 0) return 0;

    //Discard whitespaces in the beginning
    while (i < str.length() && str[i] == ' ')
        i++;

    // Check if optional sign if it exists
    if (i < str.length() && (str[i] == '+' || str[i] == '-'))
        sign = (str[i++] == '-') ? -1 : 1;

    // Build the result and check for overflow/underflow condition
    while (i < str.length() && str[i] >= '0' && str[i] <= '9') {
        if (result > INT_MAX / 10 ||
                (result == INT_MAX / 10 && str[i] - '0' > INT_MAX % 10)) {
            return (sign == 1) ? INT_MAX : INT_MIN;
        }
        result = result * 10 + (str[i++] - '0');
    }
    return result * sign;
}