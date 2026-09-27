import math, collections, zlib, lzma, bz2
seqs={}; name=None
for line in open('seqs.fasta'):
    line=line.strip()
    if line.startswith('>'): name=line[1:].split()[0]; seqs[name]=[]
    elif line: seqs[name].append(line)
seqs={k:''.join(v).upper() for k,v in seqs.items()}
ref=seqs['MN908947.3']
paper={'MN908947.3':(0,1.9570243),'LC542809.1':(4,1.9569197),'MT956915.1':(7,1.9569230),'MW466798.1':(9,1.9569327),'MW294011.1':(19,1.9567058),'MW679505.1':(25,1.9566630),'MW735975.1':(26,1.9565714),'OK546282.1':(32,1.9565675),'OK104651.1':(40,1.9564591),'OL351371.1':(49,1.9562614)}
def H(counts,N):
    return -sum(c/N*math.log2(c/N) for c in counts if c>0)
print('id len ACGT_counts other H_plugin(ACGT only) H_paper nonACGT')
res={}
for k,s in seqs.items():
    c=collections.Counter(s)
    acgt=[c[x] for x in 'ACGT']; N=sum(acgt)
    other={x:v for x,v in c.items() if x not in 'ACGT'}
    h=H(acgt,N)
    # Miller-Madow
    mm=h+(sum(1 for x in acgt if x>0)-1)/(2*N*math.log(2))
    # diffs vs ref (positionwise, if same length)
    subs=collections.Counter()
    if len(s)==len(ref):
        for a,b in zip(ref,s):
            if a!=b and b in 'ACGT': subs[a+'>'+b]+=1
    res[k]=(len(s),acgt,other,h,mm,subs)
    print(k,len(s),acgt,other,round(h,7),paper[k],'MM',round(mm,7),dict(subs))
