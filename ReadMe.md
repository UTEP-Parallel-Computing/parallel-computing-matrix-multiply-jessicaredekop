# Parallel Computing Matrix Multiply Assignment

## Part 1: Serial Matrix Multiplication

### Instructions
You can run this assignment by running the python program matrixmultiplyp1.py

### Performance Measurements:
My computer only has 2 cores with 4 threads each:
Square matrix of:
256x256 ~12.1 seconds.

Increasing that by 1 bit to 
512x512 ~105 seconds (~2 minutes).

## Part 2: Parallel Matrix Multiplication

### Instructions
You can run this assignment by running the python program matrixmultiplyp2.py and manually changing the number of threads.

### Issues encountered:
As I'm running this program on my own Linux OS, I came across a very interesting issue. I imported the python module 'pymp' to use pymp.Parallel() however, when running my code the following error occurred: "module 'pymp' has no attribute 'Parallel'".

A second issue I encountered, is When creating a shared array. I recieved the following error: 'maximum supported dimension for an ndarray is 32, found 256'

### How I overcame some problems:
I followed the process: 
1. Check spelling. 
2. Check syntax. 
3. uninstall 'pymp' module 
4. reinstalling 'pymp' module.
5. Changing IDEs(per classmates advice)
6. Checking documentation (which of course is the solution)
Therefore, in fact, the pymp.Parallel() module does not come from 'pymp', but as found in the git documentation, comes from the module 'pymp-pypi'

### Bugs in program:
There are no bugs in the program that I am aware of.

### How long it took me to complete this assignment:
The coding did not take long, however the issue I encountered with the module took a couple hours to debug.

### Performance Measurements:
The performance measurements used will be time in seconds from the Python time module.

### Increasing # of Threads:
Square matrix of:

#### 256x256
With 1 Thread
~15.3 s

With 2 Threads
~7.89 s

With 4 Threads
~8.6 s

With 8 Threads
~8.6 s

#### 512x512
With 1 Thread
~144.8 s

With 2 Threads
~74.9 s

With 4 Threads
~80.5 s

With 8 Threads
~77.4 s

### Observations:
Increasing two 2 threads almost halves the computation time for the 256x256 and 512x512 matricies.
However, having 4 and 8 threads for both matricies did not decrease to the computational time it took 

### Output of cpuInfoDump.sh:
Intel(R) Core(TM) i7-7560U CPU @ 2.40GHz
4 -- 36 -- 216
