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
As I'm running this program on my own Linux OS, I came across a very interesting issue. I imported the python module 'pymp'
to use pymp.Parallel() however, when running my code the following error occurred: "module 'pymp' has no attribute 'Parallel'".
A second issue I encountered, is When creating a shared array. I recieved the following error: 'maximum supported dimension for an ndarray is 32, found 256'

### How I overcame some problems:
I followed the process: 
1. Check spelling. 
2. Check syntax. 
3. uninstall 'pymp' module 
4. reinstalling 'pymp' module.
5. Changing IDEs(per classmates advice)
6. Checking documentation (which of course is the solution)
Therefore, in fact, the pymp.Parallel() module does not come from 'pymp',
but as found in the git documentation, comes from the module 'pymp-pypi'

### Bugs in program:


### How long it took me to complete this assignment:
The coding did not take long, however the issue I encountered with the module took a couple hours to debug.

### Performance Measurements:


### Increasing # of Threads:


### Observations:


### Output of cpuInfoDump.sh:
N/A
