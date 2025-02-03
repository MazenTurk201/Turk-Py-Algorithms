wordd="Mazen Sameh Sayed"

def foundd(word,char):
    for i in range(len(word)-1):
        if (word[i]).lower() == (char[0]).lower():
            if len(char)-1 >= 1:
                if (word[i:i+len(char)]).lower() == char.lower():
                    print(i+1,end=" ")
            elif (word[i]).lower() == char.lower():
                print(i+1,end=" ")

foundd(wordd,"sa")
print()
foundd(wordd,"a")