#Brian Ross Lab4 CSC201 March 29, 2016
def pass_word(password):
    while(True): #loop to prompt the user until they create a valid password
        import re
        password = str(input("Create a password: "))
        if len(password) < 8: #password must be longer than 8 characters
            print("Password must be larger than 8 characters. Try again: ")
        elif bool(re.search("[^\w\d\s]",password)) == False: #the password must contain something other than a number, letter, or white space
            print("Passwords must contain a symbol. Try again: ")
        elif bool(re.search("\d", password)) == False: #password must have a digit
            print("Passowrds must contain a number. Try again: ")
        else:
            print("your new password is: '", password,"'")
            break
new_pass = print("You will be instructed to create a password")
pass_word(new_pass)

def sentence(string):
    import re #import regex
    import warnings #import warnings module so they can be ignored
    warnings.filterwarnings('ignore') #ignores a warning about non-empty pattern matches
    word = re.split("\s*",string) #splits the sentence into words
    no_duplicates = set(word) #sets contain unique "characters"
    print(no_duplicates) #prints the words in the sentence
some_input = input("Write a sentence: ") #user creates a sentence for the function
sentence(some_input) 



