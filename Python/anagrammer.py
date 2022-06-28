#! /usr/local/bin/python

__author__ = 'Roger Andre, May 2015'

'''Find every anagram for a word that is present in a dictionary file.  
Only evaluates words that are at least 4 letters long.  Only list anagrams 
where there are at least as many words as there are letters in the seed.'''

import sys

def getData(txt_file = 'dict.txt'):
  '''Opens the text file that contains our words and loads it into the word_data array.'''
  try:
    word_file = open(txt_file, 'r')
  except IOError:
    raise IOError("Can't open file")
    sys.exit(1)
  word_data = word_file.readlines()
  word_file.close()
  return word_data

def getSignature(word):
  '''Converts a word into its "signature", ie lower case alpha sorted set of letters'''
  word = word.lower() # ELIMINATE CASE SO THAT "Lois" AND "soil" MATCH'''
  signature = ''.join(sorted(word))
  return signature

def processData(word_data):
  '''Processes all of the words in the word_data list. Only looks at words >= 4 chars in length.
  Gets the signature for each word and uses it to create a dictionary where the keys are every unique
  signature in the data set.  The values are all the words that reduce to the same signature.'''
  sig_dict = {}
  for word in word_data:
    word = word.strip() # REMOVE TRAILING \n
    if len(word) >= 4:
      signature = getSignature(word)
      if signature not in sig_dict:
        sig_dict[signature] = [word]
      else:
        sig_dict[signature].append(word)
  return sig_dict

def printData(processed_data):
  '''Check that there are as many words as there are letters in signature and print each list.'''
  for signature in processed_data:
    word_length = len(signature)
    list_length = len(processed_data[signature])
    if list_length >= word_length:
      print ','.join(processed_data[signature])
  
def main():
  word_data = getData()
  processed_data = processData(word_data)
  printData(processed_data)

if __name__ == '__main__':
  main()
