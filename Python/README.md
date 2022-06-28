# anagrammer
Explorations in anagram creation.

Goal
----
Find all of the anagrams in a dictionary text file in which there are at least 4 letters in the word and at least as many anagrams as there are letters in the word.

The dictionary should be a file on disk with one line per word. 

Output should be in this format:

emit, item, mite, time  
merit, miter, mitre, remit, timer  
reins, resin, rinse, risen, serin, siren  
inert, inter, niter, retin, trine  
inset, neist, snite, stein, stine, tsine  

How Not to Do It
----------------

- get a word
- make sure word is at least 4 characters long
- find all of the permutations of the word
- check to see if any of the permutations are in the dictionary
- do this for every word in the dictionary

Why is this a bad idea?  Because as I found out, simply calculating all of the permutations is horrendously expensive.  Just the permutation calc by itself is N factorial in cost, where N is the number of letters in the word.  And it's a high cost with little payoff.  Take for example the name "Lois".  If we convert it to lower-case and calculate its permutations, we end up with this list of 24 items:

['lois', 'olis', 'oils', 'oisl', 'lios', 'ilos', 'iols', 'iosl', 'liso', 'ilso', 'islo', 'isol', 'losi', 'olsi', 'osli', 'osil', 'lsoi', 'sloi', 'soli', 'soil', 'lsio', 'slio', 'silo', 'siol']

But in fact, we only care about these 4: ['lois', 'oils', 'silo', 'soil']

A Better Way to Do It
---------------------
Since the goal is to find all the anagrams for a word that exist in the dictionary file, it would be smarter to index all of the words in the file in such a way that we group the anagrams together.  This can be done by using the individual letters of each word and sorting them in a-z order.  For example, given 'lois', 'oils', 'silo' and 'soil', all of these sort down to 'ilos', which we can store together like this: {'ilos': ['lois', 'oils', 'silo', 'soil']}  

This then becomes a much easier and more efficient problem to solve.  We have to evaluate every word in the text file, but only once to identify it's signature and assign it to the right bucket.  After that's it's simple to check for our display conditions and print each signature's anagram list if the conditions are met.



