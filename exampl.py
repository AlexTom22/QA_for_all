# количество цифр 3 в нем;
# сколько раз в нем встречается последняя цифра;
# количество четных цифр;
# сумму его цифр, больших пяти;
# произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
# сколько раз в нем встречается цифры 0 и 5 (всего суммарно).

# n_str = "56639"
# n = int(n_str)
# q_3 = 0
# last_dig = n % 10
# q_last = 0
# q_even = 0
# sum_dig_over_5 = 0
# mul_dig_over_7 = 1
# q_bet_0_5 = 0
# while n > 0:
#     cur_dig = n % 10
#     if cur_dig == 3:
#         q_3 += 1
#     if cur_dig == last_dig:
#         q_last += 1
#     if cur_dig % 2 == 0:
#         q_even += 1
#     if cur_dig > 5:
#         sum_dig_over_5 += cur_dig
#     if cur_dig > 7:
#         mul_dig_over_7 *= cur_dig
#     if cur_dig in [0, 5]:
#         q_bet_0_5 += 1
#     n //= 10
#
# print(q_3)
# print(q_last)
# print(q_even)
# print(sum_dig_over_5)
# print(mul_dig_over_7)
# print(q_bet_0_5)
# max_range = 33
# for a in range(1, max_range):
#     for b in range(1, max_range):
#         for c in range(1, max_range):
#             for d in range(1, max_range):
#                 sum_1 = a ** 3 + b ** 3
#                 sum_2 = c ** 3 + d ** 3
#                 if sum_1 == sum_2:
#                     if a != b and a != c and a != d and b != c and b != d and c != d:
#                         print(f"{a} ** 3 + {b} ** 3 = {c} ** 3 + {d} ** 3  = {sum_1}")

s = input()
for i in range(0, len(s), 2):
    print(s[i])
    br
