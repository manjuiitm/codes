###To create acronyms using Python, you need to write a python program that generates a short form of a word from a given sentence. You can do this by splitting and indexing to get the first word and then combine it. Let’s see how to create an acronym using Python:

user_input = str(input("Enter a Phrase: "))
text = user_input.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)
