import sys
import importlib
import os
import argparse
import random
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
parser.add_argument("--type", choices=["int", "float"], default="int", help="Data type for generated numbers (default: int)")

# Parse command-line arguments
args = parser.parse_args()

# Extract directory and module name
file_path = os.path.abspath(args.file)
dir_path = os.path.dirname(file_path)  # Directory of the file
file_name = os.path.basename(file_path).replace(".py", "")  # Extract filename (e.g., "math_operations")

# Path for log file in the same directory as the function file
log_file_path = os.path.join(dir_path, f"{file_name}_runtime_stats.txt")

# Add directory to sys.path
sys.path.append(dir_path)

try:
    # Import the module dynamically
    module = importlib.import_module(file_name)

    # Get the function from the module
    function = getattr(module, args.func)

    runtimes = []

    # ✅ Regular Randomized Tests
    for _ in range(args.reps):
        if args.type == "int":
            inputs = [random.randint(int(args.lower), int(args.upper)) for _ in range(args.count)]
        else:
            inputs = [random.uniform(args.lower, args.upper) for _ in range(args.count)]
        
        # Measure execution time
        start_time = time.time()
        result = function(*inputs)
        end_time = time.time()

        runtime = end_time - start_time
        runtimes.append(runtime)

        print(f"{args.func}({', '.join(map(str, inputs))}) = {result} | Runtime: {runtime:.6f} sec")

    
    if(args.type=="int"):
        lower_bound_inputs = [int(args.lower)] * args.count
        upper_bound_inputs = [int(args.upper)] * args.count
    else:
        lower_bound_inputs = [args.lower] * args.count
        upper_bound_inputs = [args.upper] * args.count
    
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
        log_file.write(f"Command Args: {vars(args)}\n")
        log_file.write(f"Avg. Runtime: {avg_runtime:.6f} sec\n")
        log_file.write(f"Min Runtime: {min_runtime:.6f} sec\n")
        log_file.write(f"Max Runtime: {max_runtime:.6f} sec\n")
        log_file.write(f"Lower Bound Runtime: {lower_runtime:.6f} sec (Inputs: {lower_bound_inputs})\n")
        log_file.write(f"Upper Bound Runtime: {upper_runtime:.6f} sec (Inputs: {upper_bound_inputs})\n")
        log_file.write("=" * 50 + "\n")

    print(f"\n✅ Results logged to: {log_file_path}")

except ModuleNotFoundError:
    print(f"Error: Module '{file_name}' not found in '{dir_path}'")
except AttributeError:
    print(f"Error: Function '{args.func}' not found in '{file_name}'")
except TypeError as e:
    print(f"Error: {e}")
