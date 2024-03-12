import nltk
# nltk.download('punkt')
seq= str(input("Enter your sequance: \n"))

print('''
        Choice number 1: print tokenized words\n 
        Choice number 2: print tokenized sentences\n 
        Choice number 3: print output using split function.\n''')
choice=int(input("Enter the choice number : "))
if choice==1:
    print(nltk.word_tokenize(seq))
elif  choice==2:
    print(nltk.sent_tokenize(seq))
elif choice==3:
    print(seq.split("."))
else:
    print("Wrong choice!!")

