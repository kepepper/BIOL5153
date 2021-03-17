#! /usr/bin/env python3

# This script generates a PBS file for the AHPCC Razor cluster


# Define some variables

job_name = 'test'

queue = 'med16core'

output = job_name

nodes = 1

ppn = 1

time = 3 # this is in hours


# This setion prints the head/required info for the PBS script

print('#PBS -N ' + job_name)
print('#PBS -q' + ' ' + queue) # which queue to use
print('#PBS -j oe') # join the STDOUT and STDERR into a single file
print('#PBS -o ' + output + '.$PBS_JOBID') # set the name of the job output file
print('#PBS -l nodes=' + str(nodes) + ':ppn=' + str(ppn)) # how many resources to ask for (notes = num nodes, ppn = num processors)
print('#PBS -l walltime=' + str(time) + ':00:00') # set the walltime (default to 1 hour)
print()


# cd into working directory

print('cd $PBS_O_WORKDIR')
print()


# Load the necessary modules

print('# load modules')
print('module purge')
print('module load gcc/7.2.1 python/3.6.0-anaconda java/sunjdk_1.8.0 blast mafft/7.304b')
print()


# Commands for this job

print('# insert commands here')
print('command 1')
print('command 2')
print('...')
print()
