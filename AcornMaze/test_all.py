"""
A simple program that will import your tests and run them all!

Usage: python3 test_all.py
"""

import subprocess
import os
from test_game import run_tests as test_game
from test_grid import run_tests as test_grid
from test_parser import run_tests as test_parser
from test_solver import run_tests as test_solver

print("###########################")
print("### Running unit tests! ###")
print("###########################\n")

test_game()
test_grid()
test_parser()
test_solver()
print("All unit tests passed!\n")

#Run the e2e script
os.system('chmod u+x ./test_e2e.sh')
subprocess.call(['./test_e2e.sh'])
