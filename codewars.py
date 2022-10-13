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
# def calculator(x, y, op):
#     if op in ("+", "-", "*", "/") and isinstance(x, int) and isinstance(y, int):
#         if op == "+":
#             return x + y
#         elif op == "-":
#             return x - y
#         elif op == "*":
#             return x * y
#         else:  # op == "/"
#             return x / y
#     else:
#         return "unknown value"
#
#
# print(calculator(6, -5, "="))

# list_of_numbers = [1, 2, 3]
# new_list = list_of_numbers.copy()
#
# new_list.append(len(list_of_numbers))
# print(new_list)

# lst_o = []
# for i in lst:
#     str_i = str(i)
#     if "7" in str_i:
#         lst_o.append(i)
# print(lst_o)

# from math import factorial
#
# number = 145
# sum_n = 0
# num_str = str(number)
# for i in num_str:
#     sum_n += factorial(int(i))
# if sum_n == number:
#     print("STRONG!!!!")
# else:
#     print("Not Strong !!")

# ==============================
def ascend_descend(length, minimum, maximum):
    str_out = ""
    cur_num = minimum
    i = 1
    flag = True

    if length == 0 or maximum < minimum:
        return str_out

    while i <= length:

        if cur_num >= 0:
            str_out += str(cur_num)
        else:
            str_out += "-"
            i += 1
            if i <= length:
                str_out += str(-cur_num)

        if flag and cur_num < maximum:
            cur_num += 1
        elif cur_num == maximum:
            flag = False
            cur_num -= 1
        elif not flag and cur_num > minimum:
            cur_num -= 1
        elif cur_num == minimum:
            flag = True
            cur_num += 1

        i += 1

    return str_out
# не решена
# эксперименты с git-ом

print(ascend_descend(10, 9, 12))
