# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#Asks the user for their name, and prints the name to the screen
name = input("what is your name?  ")
#print the user name
#Asks the user for a number, then multiply that number by itself, and print the results to the screen
number = float(input("Tell me a number: "))
answer = (number * number)
print("The answer is: ", answer)
#Asks the user for any word, counts how many letters are in that word, and prints the result to the screen
word = input("Tell me a word: ")
print(len(word))