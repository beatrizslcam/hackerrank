#!/bin/python3

import math
import os
import random
import re
import sys



def amount_letters(sentence):
    spaces = sentence.count(" ")
    return len(sentence) - spaces



def amount_words(sentence):
    
    listOfWords = sentence.split()
    
    return len(listOfWords)



def automated_readability_index(sentence):
    
    amountWordsResult = amount_words(sentence)
      
    result = 4.71 *  (amount_letters(sentence)/amountWordsResult) + 0.5 * (amountWordsResult/1) -21.4
    
    decimalPart = result % 1

    if(decimalPart  == 0):
    
        return int(result)
        
    elif(result < 14):

        return int(result - decimalPart + 1)
        
    else:

        return 14
    

##sentence = "And you may ask yourself Well how did I get here"
##print(automated_readability_index(sentence))

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    output = automated_readability_index(sentence)

    fptr.write(str(output) + '\n')

    fptr.close()
