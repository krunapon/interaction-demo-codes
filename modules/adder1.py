import sys

num_args = len(sys.argv)
print(f"Number arguments is {num_args}")
for arg in sys.argv:
    print(f"Argv program is {arg}")
total = 0
for i in range(1, num_args):
    prog_argv = float(sys.argv[i])
    print(f"The program argument is {prog_argv}")
    total = total + prog_argv
print(f"Total of these numbers is {total}")