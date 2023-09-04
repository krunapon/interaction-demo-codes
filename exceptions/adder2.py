import sys
import pdb
try:
   pdb.set_trace()
   n1 = int(sys.argv[1])
   n2 = int(sys.argv[2])
   answer = n1 + n2
   print(f'The answer of {n1} + {n2} is {answer}')
except IndexError:
   print("Please access a correct index")
