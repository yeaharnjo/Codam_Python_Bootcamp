#!/usr/bin/env python3

# Import the sys module to access command line arguments
import sys 

# sys.argv is a list of command-line arguments passed to the script.
# sys.argv[0] is always the script name.
# Parameters start from sys.argv[1] onwards.

# Calculate the number of parameters passed to the script, ignoring the script name.
num_params = len(sys.argv) - 1

# Print the number of parameters with the required exact format followed by a newline
print(f"Number of parameters: {num_params}.")