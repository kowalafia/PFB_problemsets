#!/usr/bin/env python3

import os, sys



## method: seq_list_from_fastq_file(fastq_filename)
##
##  Extracts the sequence lines from a fastq file and returns a list
##  of the sequence lines
##
##  input parameters:
##
##  fastq_filename :  name of the fastq file (type: string)
##
##  returns seq_list : list of read sequences.
##                    ie.  ["GATCGCATAG", "CGATGCAG", ...]
    
def seq_list_from_fastq_file(fastq_filename):

    seq_list = list()

    ## begin your code
    '''
    
    
    '''
    #fastq = open(fastq_filename, "r") 
    #for line in fastq:
       # print(line) 
     ## end your code

    fastq = open(fastq_filename, "r")
    count = 0
    for line in fastq:
        line = line.rstrip()
        if count == 1:
            seq_list.append(line)
            print("Seq:", line)
        else:
            pass
        if count == 4:
            count = 0
        print("End", count)
        count += 1
        
        
    return seq_list


     

def main():

    progname = sys.argv[0]
    
    usage = "\n\n\tusage: {} filename.fastq num_seqs_show\n\n\n".format(progname)
    
    if len(sys.argv) < 3:
        sys.stderr.write(usage)
        sys.exit(1)

    # capture command-line arguments
    fastq_filename = sys.argv[1]
    num_seqs_show = int(sys.argv[2])

    seq_list = seq_list_from_fastq_file(fastq_filename)

    print(seq_list[0:num_seqs_show])

    sys.exit(0)  # always good practice to indicate worked ok!



if __name__ == '__main__':
    main()
    
