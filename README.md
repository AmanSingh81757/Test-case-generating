# Test cases Generator for Competitive programming contest

## How to generate cases?
 - The repo consists of 3 main files: the generate.py which generates test cases, main_code.cpp which contains the ideal solution for problem which will be used to generate the solutions to the test cases and the lat file main.py which is the entry point for this task where you can configure commands and number of test case files to generate
 - The main.py stores  a variable to denote the number of test case files which need to be generated and executs the commands to generate test cases and compiling the main_code.cpp file for those test cases
 - The generate.py contains the logic to generate the test cases. It basically makes uses of random libraray to generate random numbers for a given range to create test cases. The logic is simple to understand.
 - the main_code.cpp file contains the ideal code for your solution.

 _Note:_
 1. Do not enter the input and output file stream inside of the main_code.cpp file as we will be defining the input output source for the ideal code in the main.py itself.
 2. There is a special file to generate tree test cases as random numbers generating may result in a cycle for normal graph test cases.