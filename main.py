
def encrypt():
    shift_amount = 5

    #Get the word(s) to encrypt from the user
    print("Enter the word that you would like to encrypt (in lowercase characters)")
    word_to_encrypt = input("Word to encrypt: ")

    length_of_word = len(word_to_encrypt)
    curr_letter = 0

    print("Encrypted word: ",end="")

    while( curr_letter < length_of_word ):
        new_letter = ""
        if( word_to_encrypt[curr_letter] < 'v' ):

            new_letter = chr(ord(word_to_encrypt[curr_letter]) + shift_amount)
        else:
            new_letter = chr(ord(word_to_encrypt[curr_letter]) - 26 + shift_amount)

        print(new_letter, end = "")

        curr_letter = curr_letter + 1;

    print()


def getInts(count):
    vals = []
    for i in range(count):
        vals.append(int(input("please give me a number: ")))
    return vals



def average(values):
    sum = 0;
    for i in range(len(values)):
        sum = sum + values[i]
    return sum/count;



# Start main
choice = input("Please chose encrypt, slice, or average: ")

print("You chose " + choice)


if ("encrypt" == choice):

    encrypt()

if ("average" == choice):
    count = int(input("How many numbers are we averaging? "))
    values = getInts(count)
    print("The average is " + str(average(values)))

if ("slice" == choice):
  print(input("Please inut a word or phrase")[int(input("Where should we start the slice")):int(input("Where should we end the slice"))])


a = "tufts"
b = "university"
c = "coding"

print(a[2] + b[2] + b[5:7] + a[0])


# For homework please do one or more of:
# 1. Rewrite this program in english so that a friend or parent could follow the instructions
# 2. Change the encrypt method so that it takes shift_amount as an argument. Make sure that the code still works.
# 3. Add lines after 68 using the letters in variables a, b, and c to print: institute, studying, diction or a word of your own
# 4. Read this https://iopscience.iop.org/book/978-1-6817-4093-5/chapter/bk978-1-6817-4093-5ch1
# 5. Make a rock, paper, scissors game

