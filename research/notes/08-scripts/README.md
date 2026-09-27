# Section 08 reproduction scripts

Reproduce the Shannon entropies reported in Vopson & Lepadatu (2022), Table I,
and the substitution-spectrum analysis in `paper/sections/08-information.tex`.

    ./fetch_seqs.sh      # downloads seqs.fasta from NCBI (10 genomes)
    python3 analyze.py   # entropies (plug-in, Miller-Madow) vs published values; substitutions vs reference
    python3 analyze2.py  # follow-up analysis used in the section
