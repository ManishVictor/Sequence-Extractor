
with open("curatedheaders.csv","r") as file1:
    read1=file1.readlines()
with open("allseqorfspurified.txt","r") as file2:#use the sequencepurifier.py # use single line fasta file
    read2=file2.readlines()
for i in range(len(read1)):
    split1=read1[i].split("\n")
    header=split1[0]
    print (header)
    for j in range(len(read2)):
        split2=read2[j].split("\n")
        if(split2[0]==header):
            with open("sequence.txt","a") as file4:
                file4.write(header+"\n"+read2[j+1])