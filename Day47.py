# # # recursion notes



# # 🌀 Recursion in Python – Basic Notes
# # 🔹 What is Recursion?

# # Recursion is a programming technique where a function calls itself to solve a smaller version of a problem.

# # 🔹 Structure of a Recursive Function

# # A recursive function must have:

# # Base case – the condition that stops recursion.

# # Recursive case – the part where the function calls itself.

# # def recursive_function():
# #     if base_condition:
# #         return result
# #     else:
# #         return recursive_function()


# 🔹 Simple Example: Factorial
# def factorial(n):
#     if n == 0 or n == 1:     # Base case
#         return 1
#     else:
#         return n * factorial(n - 1)   # Recursive case


# Explanation:

# factorial(3) = 3 × factorial(2)

# factorial(2) = 2 × factorial(1)

# factorial(1) = 1 → Base case hit → Returns 1