# array_scores.py

import sys

if len(sys.argv)>1:
  script_name=sys.argv[0]
  scores = [int(arg) for arg in sys.argv[1:]]
  print("user details inputted.")

else:
    print("default details.")
    script_name=sys.argv[0]
    scores=[10,20,30,40]
    
total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)
