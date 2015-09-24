#!/usr/bin/python

 _................,._
| |run.py   |  |
| |             |  |
| |________|  |
|   ______     |
|   |        |  |   |
|__|____|_|__|
            
            
# import modules used here -- sys is a very standard one
import sys

from urbansounds import data;
from urbansounds import features;
from urbansounds import classifier;
from urbansounds import evaluate;


def run():
  input_files_list = data.download(..)
  input_files_cleaned_list = data.prepare(input_files_list)
  file_list_folded = data.split_10crossvalidation(input_files_cleaned_list)
  
  features.extract
  feature_processing
  feature_discovery
   selection
   reduction

  classifierl.train
  classifier.test
  
  evaluate.measure



# Gather our code in a main() function
def main():
  print 'Hello there', sys.argv[1]
  # Command line args are in sys.argv[1], sys.argv[2] ..
  # sys.argv[0] is the script name itself and can be ignored
  
  run()

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()
