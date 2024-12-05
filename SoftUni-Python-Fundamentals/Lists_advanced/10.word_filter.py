words = input().split(" ")
result_even_words = [even_word for even_word in words if len(even_word) % 2 == 0]
print("\n".join(result_even_words))