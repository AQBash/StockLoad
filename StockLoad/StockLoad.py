def LetterToASCII10(letter):
    #this function takes a letter as input and
    #returns its position in the english alphabet
    #starting with 0
    #A=>0; B=>1, C=>3 etc.
    return ord(letter) - 65


def StockLoad(combination, end, init="A"):
    #This function returns the number
    #of items in a slot of a Stock

    # string: combination as like "ABC" or "BCD" as argument !!letters must be in lexical order!!
    # string: init is the overall first letter usually "A" if nothing is given
    # string: end is the lastletter possible letter in that combination e.g. "Z"

    sol=[]
    firstLetter=init
    lastLetter=end

    for idx, i in enumerate(list(combination)): # iterate through the combination
        #caculates the gab between two subsequent leters in the array
        if idx==0:
            sol.append(LetterToASCII10(combination[idx])-LetterToASCII10(firstLetter))#initially the gap between the first entry and the overall initial ("A") is calculated
        elif idx==len(combination)-1:
            sol.append(LetterToASCII10(lastLetter)-LetterToASCII10(combination[idx]))#the end gap is calculated between the last llasteletter and the last entry
        else:
            sol.append(LetterToASCII10(combination[idx+1])-LetterToASCII10(combination[idx])-1)# in any other case the gap is the difference between two seubsequent entries -1, because if two bars are placed side by side there is no space inbetween
    return sol

