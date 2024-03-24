# Bacterial_WGS

### Using SPAdes, DeNovo Assembly of bacterial genome

Using the patricbrc.org website, perform the Genome assembly in the "tools and services" windows.

![image](https://github.com/LoicMMartinCEA/Bacterial_WGS/assets/22998956/0980188c-9a22-441b-9e46-3c786f32c5e1)

We notably obtain the following file containing the contig files :   <i>**SB39-SPAdes-contigs.fasta**</i>

### Using MUMmer4, obtain 

After downloading the E.coli BL21(DE3) as a reference genome, Use the MUMmer package with:   
nucmer -t 30 -p nucmer_out   Ecoli_BL21(DE3)_genome_CP001509.fa   SB39_SPAdes_contigs.fasta   
(nucmer -t 30 -p file_out    reference.fa      contigs.fasta)   

show-coords -d -l -o -r nucmer_out.delta > show_coords.out   
show-tiling -c -p show-tilling_pseudo_mol.out -R -x nucmer_out.delta    
show-aligns -r -c nucmer_out.delta Ecoli_BL21(DE3)_genome_CP001509 SB39_SPAdes_contig_55    

show-snps -r -T SB39Expected_nucmer_out.delta > SB39_vs_BL21DE3.snps

We obtain the following file :   <i>**SB39-BL21DE3-res.snps**</i>

### Use the python SNPs.py script

Use the python SNPs.py to transform the SB39_expected_genome.fa (Without the first line of the >SB39 fasta format)

We obtain the file :  <i>**SB39-final-genome.fa**</i>

### Use the Patricbrc website, annotate the genome

![image](https://github.com/LoicMMartinCEA/Bacterial_WGS/assets/22998956/442b4955-f72d-4cd8-b3f4-6838fdfecfcf)

We obtain the following file  :  <i>**Escherichia-coli-BL21DE3-SB39-fin.merged**</i>

$${\color{red}End}$$ 
