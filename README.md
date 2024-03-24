# Bacterial_WGS

### Using SPAdes, DeNovo Assembly of bacterial genome

Using the patricbrc.org website, perform the Genome assembly in the "tools and services" windows.

![image](https://github.com/LoicMMartinCEA/Bacterial_WGS/assets/22998956/0980188c-9a22-441b-9e46-3c786f32c5e1)

We notably obtain the following file containing the contig files :   $${\color{red}SB39-SPAdes-contigs.fasta}$$

### Using MUMmer4, obtain 

After downloading the E.coli BL21(DE3) as a reference genome, Use the MUMmer package with:
show-coords 

We obtain the following file :   $${\color{red}SB39-BL21DE3-res.snps}$$ 

### Use the python SNPs.py script

Use the python SNPs.py to transform the SB39_expected_genome.fa (Without the first line of the >SB39 fasta format)

We obtain the file :  $${\color{red}SB39-final-genome.fa}$$ 

### Use the Patricbrc website, annotate the genome

![image](https://github.com/LoicMMartinCEA/Bacterial_WGS/assets/22998956/442b4955-f72d-4cd8-b3f4-6838fdfecfcf)

We obtain the following file  :  $${\color{red}Escherichia-coli-BL21DE3-SB39-fin.merged}$$ 
