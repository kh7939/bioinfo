# This will time how long it takes to run a code

from time import perf_counter

strt_time = perf_counter()

# put a code you wnat to test out here

elapsed_time = perf_counter()

print(f'Loop took: {(elapsed_time - start_time):0.6f}s\n')
#0.6f = show me until 6th position after the decimal point
