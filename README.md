Cosmogramma
========

python library for easily constructing ngrams (2 &lt;= n &lt;= 4) and building sentences from them

what's inside:
  * ngram.py
    * class NGram
    * Object that reads from a specified text file and generates sentences according to a specified n and start and end symbols.
    * Functions:
      *  ngram.NGram(fileName, n, start="&lt;s&gt;", end ="&lt;e&gt;")
        * creates the object
        * fileName = name of file to read from (string)
        * n = size of ngram to be constructed (int, between 2 and 4)
        * start = symbol representing the beginning of a sentence in text file (string)
          * "<s>" by default
        * end = symbol representing the end of a sentence in text file (string)
          * "<e>" by default
      
      * ngram.setN(self, n)
        * sets a new value for the size of ngram to be used
        * reconstructs list of ngrams according to new selection
          * n = new n value (int, between 2 and 4)

      * ngram.setSymbols(start, end)
        * sets new start and end symbols
          * start = new start symbol (string)
          * end = new end symbol (string)
          
