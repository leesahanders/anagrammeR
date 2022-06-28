#! /usr/local/bin/python

import unittest
import anagrammer

class TestAnagrammer(unittest.TestCase):

  def test_getData(self):
    '''Test that we deal with non-existent file.'''
    with self.assertRaises(IOError) as context:
      anagrammer.getData("foo.txt")
    self.assertTrue("Can't open file" in context.exception)

  def test_getSignature(self):
    '''Test that we generate the right signature for words.'''
    sig = anagrammer.getSignature('Lois')
    self. assertEqual(sig, 'ilos')
    sig2 = anagrammer.getSignature('cool')
    self. assertEqual(sig2, 'cloo')

  def test_processData(self):
    '''Test that we get the right dictionary using data in the sample file.'''
    word_data = anagrammer.getData('sample_dict.txt')
    word_dict = anagrammer.processData(word_data)
    self.assertEqual(word_dict['ilos'], ['Lois', 'oils', 'silo', 'soil'])

if __name__ == '__main__':
  unittest.main()
