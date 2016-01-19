# Lam Minh Le

# write a program that:
# 1. greets the user in English
# 2. asks the user to choose from 1 of 3 spoken languages (pick your favorite languages!) 
# 3. displays the greeting in the chosen language
# 4. exits

# make sure that your code contains comments explaining your logic!




print('Hello world!')
print("Choose a language and I'll greet you in that language!") #Asking for what language to say hello in
print('1. Spanish')
print('2. French')
print('3. Vietnamese')

lang = input()
if lang == '1': #1 = Spanish
    print('Hola') #Hello in Spanish

elif lang == '2': #2 = French
    print('Bonjour') #Hello in French

elif lang == '3': #3 = Vietnamese
    print('Chào') #Hello in Vietnamese

exit()
