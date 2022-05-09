import sys
from solve import solve

# Ensures correct usage
if len(sys.argv)<3:
    sys.exit("Usage: python3 solver.py <filename> <mode>")





if __name__ == "__main__":
    solution_found = False
    ans = solve(sys.argv[1],sys.argv[2])
    if ans!=None:
        print(ans)
        sys.exit()
    else:
        print("There is no possible path.")



