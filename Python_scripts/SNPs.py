dico = {}

def preprocessing(show_snps_f, show_snps_r):
    """ Extract the first 3 tabs of the snps.file """
    with open(show_snps_f, 'r') as file:
        for line in file:
            tab = line.split()
            if tab[0] not in dico:
                dico[tab[0]] = [tab[1], tab[2]]
    
    with open(show_snps_r, 'w') as file:
        for cle, valeur in dico.items():
            file.write(cle + "\t" + valeur[0] + "\t" + valeur[1] + "\n")
    
def main(r_genome, show_snps_r, f_genome):
    genome = ""
    with open(r_genome, 'r') as file:
        for line in file:
           genome += line.rstrip("\n")
                
    compteur_add = 0
    compteur_del = 0
    liste_genome = list(genome)
    with open(show_snps_r, 'r') as file:
        for line in file:
            tab = line.split()
            nouvel_indice = int(tab[0])-1+compteur_add-compteur_del
            if tab[1] == "." or tab[2] == ".":
                if tab[1] == ".":
                    liste_genome.insert(int(tab[0])-1, tab[2])
                    compteur_add += 1
                if tab[2] == ".":
                    print(str(nouvel_indice) + " / " + str(compteur_add) + " / " + str(compteur_del))
                    liste_genome.pop(nouvel_indice)
                    compteur_del += 1
            else:
                liste_genome[nouvel_indice] = tab[2]
    
    with open(f_genome, 'w') as file:
        for i in range(len(liste_genome)):
            file.write(liste_genome[i])
            if((i+1)%60 == 0):
                file.write("\n")
    
     


# Example usage
reference_genome = "SB39_expected_genome.fa"
final_genome = "SB39_final_genome.fa"
show_snps_file = "SB39_vs_BL21DE3.snps"
show_snps_result = "SB39_vs_BL21DE3_res.snps"

preprocessing(show_snps_file, show_snps_result)
main(reference_genome, show_snps_result, final_genome)
