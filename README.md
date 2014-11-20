Cosmogramma
========

python library for easily collecting ngrams from an input file, and constructing sentences with them.

what's inside:
  * cosmogramma.py
    * class NGram
    * Object that reads from a specified text file and generates sentences according to a specified n and start and end symbols.
    * Functions:
      *  cosmogramma.Cosmogramma(fileName, n, start="&lt;s&gt;", end ="&lt;e&gt;")
        * creates the object
        * fileName = name of file to read from (string)
        * n = size of ngram to be constructed (int > 1)
        * start = symbol representing the beginning of a sentence in text file (string)
          * "&lt;s&gt;" by default
        * end = symbol representing the end of a sentence in text file (string)
          * "&lt;e&gt;" by default
          
      * getters and setters for n, start symbol, and end symbol
      * combined setter for start and end symbols (cosmogramma.set_symbols(start, end))

  * class NException
    * special exception thrown when an n value is less than 2
  
  * class SymbolException
    * special exception thrown when a start or end symbol does not appear in input file 
