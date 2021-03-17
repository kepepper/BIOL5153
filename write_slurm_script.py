#! /usr/bin/env python3


# Define some variables

job_name = 'Trinity-assembly'

queue = 'comp6'

output = 'Trinity'

nodes = 1 # number of nodes

ppn = 32 # number of processors

time = 6 # this is in hours


print('#SBATCH -J ' + job_name)
print('#SBATCH --partition ' + queue)
print('#SBATCH -o ' + output + '_%j.txt')
print('#SBATCH -e ' + output + '_%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=kepepper@uark.edu')
print('#SBATCH --nodes=' + str(nodes))
print('#SBATCH --ntasks-per-node=' + str(ppn))
print('#SBATCH --time=0' + str(time) + ':00:00')
print()


print('export OMP_NUM_THREADS=32')
print()


print('# load required modules')
print('module load samtools')
print('module load jellyfish')
print('module load bowtie2')
print('module load salmon/0.8.2')
print('module load java')
print()


print("# cd into the directory where you're submitting this script from")
print('cd $SLURM_SUBMIT_DIR')
print()


print('# copy files from storage to scratch')
print('rsync -av RNA-R*.fastq.gz /scratch/$SLURM_JOB_ID')
print()


print('# cd onto the scratch disk to run the job')
print('cd /scratch/$SLURM_JOB_ID/')
print()


print('# run the Trinity assembly')
print('/share/apps/bioinformatics/trinity/trinityrnaseq-v2.11.0/Trinity --seqType fq --left RNA-R1.fastq.gz --right RNA-R2.fastq.gz --CPU 48 --max_memory 250G --trimmomatic --no_normalize_reads --full_cleanup --output trinity_Run2')
print()


print('# copy output files back to storage')
print('rsync -av trinity_Run2 $SLURM_SUBMIT_DIR')
print()
