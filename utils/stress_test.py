import argparse
from import_module import *
from input_generator import *
import time

def stress_test(func1, func2, max_time, lower, upper, count, data_type):
    """Continuously test two functions with random inputs until a mismatch or max_time is reached."""
    start_time = time.time()
    total_tests = 0

    while time.time() - start_time < max_time:
        inputs = generate_inputs(lower, upper, count, data_type)
        
        # Run both functions with the same inputs
        result1 = func1(*inputs)
        result2 = func2(*inputs)

        # Check if results match
        if result1 != result2:
            print("\n❌ MISMATCH FOUND!")
            print(f"Test #{total_tests + 1}: {inputs}")
            print(f"{func1.__name__} → {result1}")
            print(f"{func2.__name__} → {result2}")
            print("\nTerminating script...")
            return  # Exit immediately

        total_tests += 1

    # If max_time is reached without mismatches
    print(f"\n✅ All {total_tests} tests passed without mismatches.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Stress test two functions from different files.")
    
    parser.add_argument("--file", required=True, help="Path to the first Python file.")
    parser.add_argument("--func1", required=True, help="Function name in the first file.")
    parser.add_argument("--func2", required=True, help="Function name in the second file.")
    
    parser.add_argument("--lower", type=float, default=0, help="Lower bound of input range.")
    parser.add_argument("--upper", type=float, required=True, help="Upper bound of input range.")
    parser.add_argument("--count", type=int, default=1, help="Number of inputs per function call.")
    parser.add_argument("--type", choices=["int", "float", "list(int)", "list(float)"], default="int", help="Type of input values.")
    parser.add_argument("--max_time", type=int, default=1, help="Maximum runtime in seconds.")

    args = parser.parse_args()

    # Import functions from the specified files
    function1 = import_function(args.file, args.func1)
    function2 = import_function(args.file, args.func2)

    # Run the stress test
    stress_test(function1, function2, args.max_time, args.lower, args.upper, args.count, args.type)
