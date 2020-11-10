import sys
import Checker

def print_instruction():
    print("Usage: run.py [type] [input]")
    print("Parameter [type] can be either 1 for string or 2 for text file.")
    print("If type is 1, enter the string in [input].")
    print("If type is 2, enter the path to [input] text file.")

def main():
    if len(sys.argv) != 3:
	print_instruction()
        sys.exit()
    in_type = sys.argv[1]
    usr_in = sys.argv[2]
    if in_type == 1:
        cor_str = Checker.str_checker(usr_in)
        print("Correction: %s" % (cor_str))
    elif in_type == 2:
    	Checker.file_checker(usr_in)
    	print("Saving corrected file to %s_cort.txt" % (usr_in[:-4]))
    else:
        print("Error: Invalid Type.")
        print_instruction()

if __name__ == "__main__":
    main()
