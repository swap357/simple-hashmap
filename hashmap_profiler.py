import cProfile
import pstats
import io
import memory_profiler
import subprocess
import os
import sys
from line_profiler import LineProfiler


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.hashmap_v2 import HashMap

def profile_hashmap():
    m = HashMap()
    
    # Populate the HashMap
    for i in range(10000):
        m.set(f"key_{i}", i)
    
    # Perform various operations
    for i in range(5000):
        m.get(f"key_{i}")
    for i in range(2000, 3000):
        m.delete(f"key_{i}")
    for i in range(5000, 6000):
        m.set(f"new_key_{i}", i)

def line_profile_hashmap():
    lp = LineProfiler()
    lp.add_function(HashMap.get)
    lp.add_function(HashMap.set)
    lp.add_function(HashMap.delete)
    lp.add_function(HashMap._resize_if_needed)
    lp.add_function(HashMap._resize)
    lp_wrapper = lp(profile_hashmap)
    lp_wrapper()
    
    stats = io.StringIO()
    lp.print_stats(stream=stats)
    return stats.getvalue()

def memory_profile_hashmap():
    mem_usage = memory_profiler.memory_usage((profile_hashmap,))
    return f"Peak memory usage: {max(mem_usage)} MiB"

def time_profile_hashmap():
    pr = cProfile.Profile()
    pr.enable()
    profile_hashmap()
    pr.disable()
    
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats()
    return s.getvalue()

def hardware_profile_hashmap():
    if sys.platform != "linux":
        return "Hardware profiling is only supported on Linux systems."
    
    if not os.path.exists('/usr/bin/perf'):
        return "perf not found. Install it to get hardware metrics."

    cmd = [
        'sudo', 'perf', 'stat', '-e', 'cycles,instructions,cache-references,cache-misses,branches,branch-misses',
        sys.executable, '-c', 
        'from hashmap_profiler import profile_hashmap; profile_hashmap()'
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stderr  # perf outputs to stderr

if __name__ == "__main__":
    print("Line-by-line profiling:")
    print(line_profile_hashmap())
    
    print("\nMemory profiling:")
    print(memory_profile_hashmap())
    
    print("\nTime profiling:")
    print(time_profile_hashmap())
    
    if sys.platform == "linux":
        print("\nHardware profiling:")
        print(hardware_profile_hashmap())
    else:
        print("\nHardware profiling is only available on Linux systems.")