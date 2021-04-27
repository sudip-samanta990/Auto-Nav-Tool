#!/usr/bin/env python
# license removed for brevity
# Description: autoNav() will generate a sequence of Way-points from source to destination.

import os
from map_analyzer import *
from SMT_constraint_generator import *



def autonav1():
	try:
		#call Map-Analyzer
		#os.system("python update_generate1.py")
		map_analyzer()


		#call SMT-constraint-Generator
		smt()

		#call SMT-Solver
		#os.system("z3 output.smt2 > sequence.txt")

	except RuntimeError:
		print("Invalid input!")
		print(RuntimeError)



if __name__ == '__main__':
    autonav1()
