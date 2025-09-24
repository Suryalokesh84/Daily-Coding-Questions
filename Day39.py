# # code chef problem
# Decrement OR Increment
# Write a program to obtain a number 
# N
# N and increment its value by 1 if the number is divisible by 4 
# o
# t
# h
# e
# r
# w
# i
# s
# e
# otherwise decrement its value by 1.

# Input Format
# First line will contain a number 
# N
# N.

# Output Format
# Output a single line, the new value of the number.

# Constraints
# 0
# ≤
# N
# ≤
# 1000
# 0≤N≤1000
# Sample 1:
# Input
# Output
# 5
# 4
# Explanation:
# Since 5 is not divisible by 4 hence, its value is decreased by 1.

n = int(input())

if n % 4 == 0:
    print(n + 1)
else:
    print(n - 1)






    # ==============================================================================================

    # leetcode problem































    class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []

        # Determine the sign
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        # Integer part
        integer_part = numerator // denominator
        result.append(str(integer_part))

        remainder = numerator % denominator
        if remainder == 0:
            return "".join(result)

        result.append(".")

        # Dictionary to store remainders and their positions
        remainder_map = {}
        while remainder != 0:
            if remainder in remainder_map:
                start = remainder_map[remainder]
                result.insert(start, "(")
                result.append(")")
                break

            remainder_map[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(result)
