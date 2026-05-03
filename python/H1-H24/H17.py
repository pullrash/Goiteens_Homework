text = input("Введіть текст ")
text_s = text.split(" ")
max_word = ""
for i in text_s:
    if len(i) > len(max_word):
        max_word = i
print(text_s)
print(f"найбільше слово - {max_word}")