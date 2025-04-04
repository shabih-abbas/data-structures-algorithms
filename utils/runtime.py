import sys
from import_module import *
from input_generator import *
import os
import argparse
import time
from datetime import datetime

# Set up argument parser
parser = argparse.ArgumentParser(description="Import a function, generate random inputs, measure execution time, and log results.")
parser.add_argument("--file", required=True, help="Relative path to the Python file (e.g., './modules/math_operations.py')")
parser.add_argument("--func", required=True, help="Function name to call")
parser.add_argument("--lower", type=float, default=0, help="Lower bound for random inputs")
parser.add_argument("--upper", type=float, required=True, help="Upper bound for random inputs")
parser.add_argument("--count", type=int, default=1, help="Number of random inputs to generate (default: 1)")
parser.add_argument("--reps", type=int, default=1, help="Number of times to call the function (default: 1)")
parser.add_argument("--type", choices=["int", "float", "list(int)", "list(float)"], default="int", help="Data type for generated numbers (default: int)")

# Parse command-line arguments
args = parser.parse_args()
dir_path= os.path.dirname(args.file)
# Path for log file in the same directory as the function file
log_file_path = os.path.join(dir_path, f"{args.func}_runtime_stats.txt")

# Add directory to sys.path
sys.path.append(dir_path)

try:
    
    # Get the function from the module
    function = import_function(args.file, args.func)

    runtimes = []

    # ✅ Regular Randomized Tests
    for _ in range(args.reps):
        inputs= generate_inputs(args.lower, args.upper, args.count, args.type)
        # Measure execution time
        start_time = time.time()
        result = function(*inputs)
        end_time = time.time()

        runtime = end_time - start_time
        runtimes.append(runtime)
    
    
    lower_bound_inputs = generate_boundary_inputs(args.lower, args.count, args.type)
    upper_bound_inputs = generate_boundary_inputs(args.upper, args.count, args.type)
    
    start_time = time.time()
    function(*lower_bound_inputs)
    lower_runtime = time.time() - start_time
    
    start_time = time.time()
    function(*upper_bound_inputs)
    upper_runtime = time.time() - start_time

    # Compute runtime statistics
    avg_runtime = sum(runtimes) / len(runtimes)
    min_runtime = min(runtimes)
    max_runtime = max(runtimes)

    # Log results
    with open(log_file_path, "a") as log_file:
        log_file.write(f"\n=== {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n")
        log_file.write(f"function: {args.func}\n")
        log_file.write(f"input lower-bound: {args.lower}\n")
        log_file.write(f"input upper-bound: {args.upper}\n")
        log_file.write(f"input type: {args.type}\n")
        log_file.write(f"length of input: {args.count}\n\n")
        log_file.write(f"No. of tests: {args.reps}\n")
        log_file.write(f"Avg. Runtime: {avg_runtime:.6f} sec\n")
        log_file.write(f"Min Runtime: {min_runtime:.6f} sec\n")
        log_file.write(f"Max Runtime: {max_runtime:.6f} sec\n")
        log_file.write(f"Lower Bound Runtime: {lower_runtime:.6f} sec \n")
        log_file.write(f"Upper Bound Runtime: {upper_runtime:.6f} sec \n")
        log_file.write("=" * 50 + "\n")

    print(f"\n✅ Results logged to: {log_file_path}")

except ModuleNotFoundError:
    print(f"Error: Module '{file_name}' not found in '{dir_path}'")
except AttributeError:
    print(f"Error: Function '{args.func}' not found in '{file_name}'")
# except TypeError as e:
#     print(f"Error: {e}")
