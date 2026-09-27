#!/bin/sh
# Fetch the ten SARS-CoV-2 genomes of Vopson & Lepadatu (2022), Table I, from NCBI.
ids=MN908947.3,LC542809.1,MT956915.1,MW466798.1,MW294011.1,MW679505.1,MW735975.1,OK546282.1,OK104651.1,OL351371.1
curl -sS "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=$ids&rettype=fasta&retmode=text" -o seqs.fasta
