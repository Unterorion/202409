#sentence = "Python is the best choice."

'''print("="*50)
print("My program")
print("="*50)'''

#print(a.index('t'))

def find_entire_indx():
    idxlist=[]
    sentence = input("A sentence to search: ")
    while True:
        letter = input("Searching for indices for the letter: ")
        if sentence.find(letter) != -1:
            while sentence.find(letter) != -1:
                idx = sentence.find(letter)
                idxlist += [idx]
                sentence = sentence[:idx] + "*" + sentence[idx+1:]
            #print(idxlist)
            print(sentence)
            return(idxlist)
        else:
            print("No such letter on the sentence.")
            continue

print(find_entire_indx())