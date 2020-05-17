list1=['A', 'S', 'F', 'D', 'G', 'W']
print("Guessed letters:",end=" ")
for i in list1:
    print(i,end=" ")
print()

user_guess='l'
print(f"Nice, you guessed correct letter. '{user_guess}' is in the word")


secret_word ="hello"
indices = [i for i, letter in enumerate(secret_word) if letter==user_guess]
print(indices)

string1 = " "* 5
word_list =list(string1)


for index in indices :
    word_list[index] = user_guess