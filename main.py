import funcs

while True:
    
    print('Hi! I\'m cool MARKOVRUNNER2021\nPlease, enter your input word:')
    
    inputword = ""
    while (inputword == ""):
        inputword = input()
        if (inputword == ""):
            print("Error: Empty word. Try again:")
            
    print('\nOK! Now enter your rules. Enter STOP for, well, stop input\nExamples: aa -> a OR aa -> .a OR (empty symbol) aa -> E')
    
    rules = ''''''
    
    temprule = ''
    
    while (temprule != 'STOP'):
        temprule = input()
        if (temprule == ''):
            print("Error. Empty rule. Try again:\n")
        elif (temprule == 'STOP'):
            break
        else:
            rules += ('\n' + temprule)
            
    print('\nHa-ha, thanks. Now look at the magic\n--------')
    
    funcs.MarkovReplace(inputword, funcs.GetRules(rules))
    
    print("--------\n\nWow, it was incredible. Do you want more? If yes, then write Y, if not - N\n[Y/N]:")
    
    cont = input()
    
    if cont == "Y\n":
        continue
    if cont == "N\n":
        break
    else:
        print("IDK what you want, so goodbye\n")
        break
    