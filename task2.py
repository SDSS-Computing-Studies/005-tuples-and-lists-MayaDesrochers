#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""
myList=[]
a=(input("Enter first word:").strip())
b=(input("Enter second word:").strip())
c=(input("Enter third word:").strip())
d=(input("Enter fourth word:").strip())
e=(input("Enter fifth word:").strip())

myList.insert(0,a)
myList.insert(1,b)
myList.insert(2,c)
myList.insert(3,d)
myList.insert(4,e)
print(myList)
