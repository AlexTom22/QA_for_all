# =======================================
# def solve(s):
#     s_o = s
#     c_l = 0
#     c_u = 0
#     for char in s:
#         if char.islower():
#             c_l += 1
#         else:
#             c_u += 1
#     if c_l >= c_u:
#         return s_o.lower()
#     else:
#         return s_o.upper()
#
#
#
# r = solve("CODe")
# print(r)
#

# =====================================
# def solution(string):
#     str_o = ""
#     list_in = list(string)
#     for i in range(len(string) - 1, -1, -1):
#         char = list_in[i]
#         str_o += char
#     return str_o

# def solution(string):
#     return string[::-1]
#
# print(solution("12345"))

# def is_triangle(a, b, c):
#     flag = False
#     if a > 0 and b > 0 and c > 0:
#         if a < b + c and b < c + a and c < a + b:
#             flag = True
#     return flag
#
#
# def is_triangle(a, b, c):
#     return (a + b) > c and (a + c) > b and (b + c) > a

# =====================================
def calculator(x, y, op):
    if op in ("+", "-", "*", "/") and isinstance(x, int) and isinstance(y, int):
        if op == "+":
            return x + y
        elif op == "-":
            return x - y
        elif op == "*":
            return x * y
        else:  # op == "/"
            return x / y
    else:
        return "unknown value"


print(calculator(6, -5, "="))
