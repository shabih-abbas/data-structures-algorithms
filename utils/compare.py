from import_module import *
from input_generator import *
import time
import os 
import sys
import argparse


def compare_functions(func1, func2, lower, upper,count,data_type, reps):
    func1_runtimes=[]
    func2_runtimes=[]
    func1_fast_count=0
    func2_fast_count=0
    
    for rep in range(reps):
        inputs= generate_inputs(lower, upper, count, data_type)
        start_time= time.time()
        func1(*inputs)
        func1_runtimes.append(time.time()-start_time)
        start_time= time.time()
        func2(*inputs)
        func2_runtimes.append(time.time()-start_time)
        func1_fast_count+= func1_runtimes[rep]<func2_runtimes[rep]
        func2_fast_count+= func2_runtimes[rep]<func1_runtimes[rep]
    
    #upper and lower bound inputs tests
    lower_bound_inputs= generate_boundary_inputs(lower,count,data_type)
    upper_bound_inputs= generate_boundary_inputs(upper, count, data_type)
    start_time= time.time()
    func1(*lower_bound_inputs)
    func1_lower_bound_time=time.time()-start_time
    start_time= time.time()
    func1(*upper_bound_inputs)
    func1_upper_bound_time=time.time()-start_time
    start_time= time.time()
    func2(*lower_bound_inputs)
    func2_lower_bound_time=time.time()-start_time
    start_time= time.time()
    func2(*upper_bound_inputs)
    func2_upper_bound_time=time.time()-start_time
    
    stats= dict(
        func1_avg=sum(func1_runtimes)/len(func1_runtimes), 
        func2_avg=sum(func2_runtimes)/len(func2_runtimes),
        func1_faster=func1_fast_count,
        func2_faster=func2_fast_count,
        func1_upper_time=func1_upper_bound_time,
        func2_upper_time=func2_upper_bound_time,
        func1_lower_time=func1_lower_bound_time,
        func2_lower_time=func2_lower_bound_time,
    )
    return stats
if __name__=="__main__" :
    parser = argparse.ArgumentParser(description="Import two function, generate random inputs, compare execution time, and log results.")
    parser.add_argument("--file", required=True, help="Relative path to the Python file (e.g., './modules/math_operations.py')")
    parser.add_argument("--func1", required=True, help="Function name to call")
    parser.add_argument("--func2", required=True, help="Function name to call")
    parser.add_argument("--lower", type=float, default=0, help="Lower bound for random inputs")
    parser.add_argument("--upper", type=float, required=True, help="Upper bound for random inputs")
    parser.add_argument("--count", type=int, default=1, help="Number of random inputs to generate (default: 1)")
    parser.add_argument("--reps", type=int, default=1, help="Number of times to call the function (default: 1)")
    parser.add_argument("--type", choices=["int", "float"], default="int", help="Data type for generated numbers (default: int)")
    args= parser.parse_args()
    dir_path= os.path.dirname(args.file)
    log_file_path= os.path.join(dir_path, f"{args.func1}_v_{args.func2}.txt")
    function1= import_function(args.file, args.func1)
    function2= import_function(args.file, args.func2)
    stats= compare_functions(function1, function2, args.lower, args.upper, args.count, args.type, args.reps)
    with open(log_file_path,"a") as log_file:
        log_file.write(f"\n{args.func1} vs {args.func2}\n\n")
        log_file.write(f"lower input bound: {args.lower}\n")
        log_file.write(f"upper input bound: {args.upper}\n")
        log_file.write(f"no. of tests: {args.reps}\n\n")
        log_file.write(f"{args.func1} avg: {stats.get("func1_avg"):.6f} sec\n")
        log_file.write(f"{args.func2} avg: {stats.get("func2_avg"):.6f} sec\n\n")
        log_file.write(f"{args.func1} lower bound input: {stats.get("func1_lower_time"):.6f} sec\n")
        log_file.write(f"{args.func2} lower bound input: {stats.get("func2_lower_time"):.6f} sec\n\n")
        log_file.write(f"{args.func1} upper bound input: {stats.get("func1_upper_time"):.6f} sec\n")
        log_file.write(f"{args.func2} upper bound input: {stats.get("func2_upper_time"):.6f} sec\n\n")
        log_file.write(f"{args.func1} was faster {stats.get("func1_faster")} times out of {args.reps}\n")
        log_file.write(f"{args.func2} was faster {stats.get("func2_faster")} times out of {args.reps}\n")
    print(stats)
    print(f"\n✅ Results logged to: {log_file_path}")