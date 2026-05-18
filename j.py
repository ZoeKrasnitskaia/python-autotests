# Напиши функцию, принимающую список строк и возвращающую только те, чья длина > 5.
def maxi(word):
    for i in word:
        if len(i) > 5:
            print(i)

user_input = input().split()
maxi(user_input)
