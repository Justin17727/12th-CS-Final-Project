List=["ADMIT","BUILD","CABLE","DELAY","EXTRA","FORUM","GOING","HUMAN",\
      "ISSUE","JUDGE","KNOWN","LUCKY","MORAL","NORTH","OFTEN","PRIME",\
      "QUIET","ROMAN","SIGHT","TWICE","USAGE","VITAL","WASTE","YOUTH"]
from random import*
random_number=randint(0,len(List)-1)
random_word_for_query=List[random_number]
#To style a word from "a,b,c,d,e" to "--a--b--c--d--e--"
def style(a,b,c,d,e):
    Dash="-- -- -- -- -- --"
    List_of_dashes=Dash.split()
    for i in range(0,10):
        if i==1:
            List_of_dashes.insert(i,a)
        if i==3:
            List_of_dashes.insert(i,b)
        if i==5:
            List_of_dashes.insert(i,c)
        if i==7:
            List_of_dashes.insert(i,d)
        if i==9:
            List_of_dashes.insert(i,e)
        else:
            continue
    S=""
    for i in List_of_dashes:
        S=S+i
    return(S)
#To extract letters from word in "abcde" to "a,b,c,d,e"
def extract_letters_from_word(a):
    uppercase_of_word=""
    for i in a:
        uppercase_of_word=uppercase_of_word+i.upper()
    list_of_letters_of_word=[]
    for letter in uppercase_of_word:
        list_of_letters_of_word.append(letter)
    for i in list_of_letters_of_word:
        if i==list_of_letters_of_word[0]:
            a=i
        if i==list_of_letters_of_word[1]:
            b=i
        if i==list_of_letters_of_word[2]:
            c=i
        if i==list_of_letters_of_word[3]:
            d=i
        if i==list_of_letters_of_word[4]:
            e=i
    return(a,b,c,d,e)
#To take a guess from the user
def asking_for_answer():
    guessed_word_with_wrong_font=input("Type the five letter word:")
    list_of_letters_of_guessed_word=[]
    R=len(guessed_word_with_wrong_font)
    if R!=5:
        return "Word should have length of 5 letters with no spaces in between!"
    if R==5:
        for i in guessed_word_with_wrong_font:
            if i.isdigit()==True:
                  return "No numbers are allowed!"
                  break
            if i.isalpha()==False:
                  if i==" ":
                         return "No spaces are allowed!"
                         break
                  else:
                         return "Use English letters only!"
                         break
                  break
            else:
                  list_of_letters_of_guessed_word.append(i.upper())
    R=len( list_of_letters_of_guessed_word)
    if R>5:
        return "Word should have length of 5 letters with no spaces in between!"
    if R==5:
        a,b,c,d,e=extract_letters_from_word(list_of_letters_of_guessed_word)
        S=style(a,b,c,d,e)
        return(S)
a,b,c,d,e=extract_letters_from_word(random_word_for_query)
Question=style(a,b,c,d,e)
#To process the guess given by the user
def guess():
    global Guess
    Guess=asking_for_answer()
    if Guess=='Word should have length of 5 letters with no spaces in between!':
        print(Guess)
        return "TRY AGAIN!"
    if Guess=='No numbers are allowed!':
        print(Guess)
        return "TRY AGAIN!" 
    if Guess=='Use English letters only!':
        print(Guess)
        return "TRY AGAIN!"
    if Guess=='No spaces are allowed!' :
        print(Guess)
        return "TRY AGAIN!"
    if Guess=='Enter a proper English word!':
        print(Guess)
        return "TRY AGAIN!"
    else:
        return Guess
#To extract word of 5 letter length in "--h--e--l--l--o--" form
def extract_letters_from_styled_words(k):
    L7=[]
    if type(k)=="<class 'Nonetype'>":
        return "None"
    for i in k:
        if i.isalpha()==True:
            L7.append(i)
        else:
            continue
    for i in range(0,5):
        if i==0:
            a=L7[0]
        if i==1:
            b=L7[1]
        if i==2:
            c=L7[2]
        if i==3:
            d=L7[3]
        if i==4:
            e=L7[4]
    return a,b,c,d,e 
#To interact with user
for i in range(0,6):
    print(guess())
    if Guess==Question:
        print("YOU WON!")
        break
    elif i!=5 and Guess!=Question:
        if Guess=="TRY AGAIN":
            continue
        if Guess=="Enter a proper English word!":
            continue
        if Guess=="Word should have length of 5 letters with no spaces in between!":
            continue
        if Guess=="Use English letters only!":
            continue            
        if Guess=="No numbers are allowed!":
            continue
        if Guess=="Enter a proper English word!":
            continue
        if Guess=="No spaces are allowed!":
            continue
        if type(Guess)=="<class 'NoneType'>":
            print("Don't type anything!")
            break
        if Guess=="None":
            print("Don't type anything!")
            break
        else:
            p,q,r,s,t=extract_letters_from_styled_words(Guess)
            a,b,c,d,e=extract_letters_from_styled_words(Question)
            list_of_letters_of_guessed_word=[p,q,r,s,t]
            list_of_letters_of_question=[a,b,c,d,e]
            for i in range(0,5):
                if list_of_letters_of_guessed_word[i] in list_of_letters_of_question:
                    if list_of_letters_of_guessed_word[i]==list_of_letters_of_question[i]:
                        print(list_of_letters_of_guessed_word[i],"is in the word and in right place!")
                    else:
                        print(list_of_letters_of_guessed_word[i],"is in the word but not in right place!")
                else:
                    print(list_of_letters_of_guessed_word[i],"is not in the word!")
        print("try again!")
    else:
        print("GAME OVER!")
        print("THE WORD WAS:",Question)
