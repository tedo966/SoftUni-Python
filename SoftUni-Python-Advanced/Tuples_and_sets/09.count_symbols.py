# text = tuple(input())
# printed_chars = ""
# for char in sorted(text):
#     if char in printed_chars:
#         continue
#     print(f"{char}: {text.count(char)} time/s")
#     printed_chars += char
txt = input()
[print(f"{ch}: {txt.count(ch)} times/s") for ch in sorted(set(txt))]