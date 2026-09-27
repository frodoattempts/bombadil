import math, collections, lzma, bz2, zlib
exec(open('analyze.py').read())
order=['MN908947.3','LC542809.1','MT956915.1','MW466798.1','MW294011.1','MW679505.1','MW735975.1','OK546282.1','OK104651.1','OL351371.1']
refc=collections.Counter(ref); N=len(ref); p={b:refc[b]/N for b in 'ACGT'}
print('ref freqs',{b:round(p[b],4) for b in 'ACGT'})
# per-substitution dH (bits) at reference composition
for a in 'ACGT':
    print(a,' '.join(f"{a}>{b}:{math.log2(p[a]/p[b])/N:+.2e}" for b in 'ACGT' if b!=a))
# expected dH per substitution under uniform-random-site, uniform-target null
e=sum(p[a]*sum(math.log2(p[a]/p[b]) for b in 'ACGT' if b!=a)/3 for a in 'ACGT')/N
print('null uniform expected dH per sub', e)
def block_entropy(s,k):
    c=collections.Counter(s[i:i+k] for i in range(len(s)-k+1)); n=sum(c.values())
    return -sum(v/n*math.log2(v/n) for v in c.values())
def compbits(s,f): return len(f(s.encode()))*8/len(s)
for k in order:
    s=seqs[k]
    h1=block_entropy(s,1); h2=block_entropy(s,2)-h1; h3=block_entropy(s,3)-block_entropy(s,2)
    subs=res[k][5]
    down=sum(v for t,v in subs.items() if p[t[0]]<p[t[2]]); up=sum(v for t,v in subs.items() if p[t[0]]>p[t[2]])
    print(k, f"H1={h1:.7f} Hcond2={h2:.6f} Hcond3={h3:.6f} lzma={compbits(s,lambda x: lzma.compress(x,preset=9|lzma.PRESET_EXTREME)):.5f} bz2={compbits(s,lambda x: bz2.compress(x,9)):.5f} zlib={compbits(s,lambda x: zlib.compress(x,9)):.5f} toward_common={down} toward_rare={up}")
