import sys
import PyPluMA

class KronaCleanPlugin:
    def input(self, filename):
       myfile = open(filename, 'r')
       self.parameters = dict()
       for line in myfile:
           contents = line.strip().split('\t')
           self.parameters[contents[0]] = contents[1]
       self.infile = open(PyPluMA.prefix()+"/"+self.parameters["kronafile"], 'r')
       self.subspecies = PyPluMA.prefix()+"/"+self.parameters["subspecies"]

    def run(self):
       self.lines = []
       omit = ["Rickettsieae", "unclassified Rickettsia", "Rickettsia endosymbiont of Bemisia tabaci","unclassified Candidatus Cardinium","delta/epsilon subdivisions", "Bacteria incertae sedis", "Bacteria candidate phyla", "Sphaerobacteridae","Halothece cluster","Luna cluster","Luna-1 subcluster","Clostridiales Family XVII. Incertae Sedis", "Wolbachieae","Archangiaceae","Chloroflexaceae","Vulgatibacteraceae","Eubacteriales Family XIII. Incertae Sedis","Polyangiaceae","Bacillales Family XI. Incertae Sedis","Roseiflexaceae","Bacillales Family XII. Incertae Sedis","Clostridiales Family XVI. Incertae Sedis","Sandaracinaceae","Myxococcaceae","Labilitrichaceae","Kofleriaceae","Sphaerobacteraceae","Anaeromyxobacteraceae","Sorangiineae incertae sedis","Clostridium botulinum A","ant, tsetse, mealybug, aphid, etc. endosymbionts","ant endosymbionts","Clostridium botulinum B","Clostridium botulinum B1","Strawberry lethal yellows phytoplasma (CPA)","Leptospirillum sp. Group III","Leptospirillum sp. Group I","Yersinia enterocolitica (type O:5)","Clostridium saccharoperbutylacetonicum N1-4","unclassified Candidatus Blochmannia endosymbionts","Buchnera aphidicola (Acyrthosiphon kondoi)","Buchnera aphidicola (Uroleucon ambrosiae)","Buchnera aphidicola (Cinara cedri)","Clostridium botulinum F","Candidatus Hamiltonella defensa","aphid secondary symbionts","Magnetospirillum gryphiswaldense MSR-1","Candidatus Blochmannia vafer","Microcystis aeruginosa PCC 7806","Xanthomonas axonopodis subcluster 9.3","Streptococcus pyogenes serotype M59","Wigglesworthia glossinidia endosymbiont of Glossina morsitans","unclassified Sodalis","unclassified Wolbachia","unclassified Coxiella (in: Bacteria)","unclassified Arsenophonus","unclassified Spiroplasma"]

       subspeciesfile = open(self.subspecies, 'r')
       subspecies = []
       for subline in subspeciesfile:
          subspecies.append(subline.strip())

       cyanobacteria_orders = ["Pseudanabaenales", "Thermostichales", "Synechococcales", "Pleurocapsales", "Chroococcidiopsidales", "Nostocales"]
       gammaproteobacteria_genera = ["Candidatus Thioglobus", "Candidatus Nardonella", "Gallaecimonas", "Candidatus Pseudothioglobus", "Sedimenticola", "Candidatus Reidiella", "Thiolapillus", "Pseudohongiella","Bathymodiolus septemdierum thioautotrophic gill symbiont","Bathymodiolus thermophilus thioautotrophic gill symbiont"]
       betaproteobacteria_genera = ["Candidatus Profftella", "Candidatus Kinetoplastibacterium"]
       alphaproteobacteria_genera = ["Micavibrio"]
       tissierellia_genera = ["Ezakiella","Sedimentibacter"]

       #Deinococcus soli (ex Cha et al. 2016)
       #Kaistella flava (ex Peng et al. 2021)
       #Lysobacter solisilvae (ex Kim et al. 2021)
       #Micromonospora endophytica (Xie et al. 2001) Li et al. 2019
       #Lysobacter solisilvae (ex Woo and Kim 2020)
       #Sphingomonas ginsengisoli An et al. 2013

       citations = {'Deinococcus soli (ex Cha et al. 2016)': 'Deinococcus soli',
             'Kaistella flava (ex Peng et al. 2021)': 'Kaistella flava',
             'Lysobacter solisilvae (ex Kim et al. 2021)': 'Lysobacter solisilvae',
             'Micromonospora endophytica (Xie et al. 2001) Li et al. 2019': 'Micromonospora endophytica',
             'Lysobacter solisilvae (ex Woo and Kim 2020)': 'Lysobacter solisilvae',
             'Sphingomonas ginsengisoli An et al. 2013': 'Sphingomonas ginsengisoli'}

       for line in self.infile:
           contents = line.strip().split('\t')
           newcontents = []
           newline = ""
           for i in range(0, len(contents)):
               if (i != len(contents)-1 and "unclassified" in contents[i] and "sp." in contents[i+1]):
                   pass
               elif (contents[i] in omit):
                   pass
               elif (contents[i] in subspecies):
                   pass
               elif ("complex" in contents[i] or "subgen." in contents[i]):
                   pass
               elif (i != len(contents)-1 and contents[i] == "Enterobacteriaceae incertae sedis" and not contents[i+1].startswith("ant")):
                   pass
               elif (i != len(contents)-1 and ("subsp." in contents[i] or "bv." in contents[i] or "pv." in contents[i] or "biovar" in contents[i] or "serovar" in contents[i])):
                   pass
               else:
                   newcontents.append(contents[i])
           for i in range(0, len(newcontents)):
               if (newcontents[i] == "Candidatus Cyclonatronum"):
                   newcontents[i] = "unclassified Balneolaeota\tunclassified Balneolaeota\tCandidatus Cyclonatronum"
               elif (newcontents[i] == "Isorropodon fossajaponicum symbiont"):
                   newcontents[i] = "unclassified Bacteria\tunclassified Bacteria\tunclassified Bacteria\tunclassified Bacteria\tIsorropodon fossajaponicum symbiont"
               elif (newcontents[i] == "cyanobacterium endosymbiont of Epithemia turgida"):
                   newcontents[i] = "unclassified Cyanobacteria\tunclassified Cyanobacteria\tunclassified Cyanobacteria\tcyanobacterium endosymbiont of Epithemia turgida"
               elif (newcontents[i] in cyanobacteria_orders):
                   newcontents[i] = "unclassified Cyanobacteria\t"+newcontents[i]
               elif (newcontents[i] == "Candidatus Cloacimonas"):
                   newcontents[i] = "unclassified Candidatus Cloacimonates\tunclassified Candidatus Cloacimonates\tunclassified Candidatus Cloacimonates\tCandidatus Cloacimonas"
               elif (newcontents[i] == "Candidatus Vampirococcus"):
                   newcontents[i] = "unclassified Candidatus Omnitrophica\tunclassified Candidatus Omnitrophica\tunclassified Candidatus Omnitrophica\tCandidatus Vampirococcus"
               elif (newcontents[i] == "Methylacidimicrobium"):
                   newcontents[i] = "unclassified Verrucomicrobia incertae sedis\tunclassified Verrucomicrobia incertae sedis\tMethylacidimicrobium"
               elif (newcontents[i] == "Ndongobacter"):
                   newcontents[i] = "unclassified Firmicutes sensu stricto incertae sedis\tunclassified Firmicutes sensu stricto incertae sedis\tNdongobacter"
               elif (newcontents[i] == "Thermobaculum"):
                   newcontents[i] = "unclassified Chloroflexi incertae sedis\tunclassified Chloroflexi incertae sedis\tThermobaculum"
               elif (newcontents[i] == "Vicinamibacteraceae"):
                   newcontents[i] = "unclassified Vicinamibacteria\tVicinamibacteraceae"
               elif (newcontents[i] == "Dehalogenimonas"):
                   newcontents[i] = "unclassified Dehalococcoidia\tunclassified Dehalococcoidia\tDehalogenimonas"
               elif (newcontents[i] == "Rhodothermaceae"):
                   newcontents[i] = "unclassified Bacteroidetes Order II. Incertae sedis\tRhodothermaceae"
               elif (newcontents[i] == "Candidatus Izimaplasma"):
                   newcontents[i] = "unclassified Tenericutes incertae sedis\tunclassified Tenericutes incertae sedis\tCandidatus Izimaplasma"
               elif (newcontents[i] == "Chloracidobacterium"):
                   newcontents[i] = "unclassified Blastocatellia\tunclassified Blastocatellia\tChloracidobacterium"
               elif (newcontents[i] == "endosymbiont \'TC1\' of Trimyema compressum"):
                   newcontents[i] = "unclassified Firmicutes sensu stricto\tunclassified Firmicutes sensu stricto\tunclassified Firmicutes sensu stricto\tendosymbiont \'TC1\' of Trimyema compressum"
               elif (newcontents[i] == "cyanobacterium endosymbiont of Rhopalodia gibberula"):
                   newcontents[i] = "unclassified Cyanobacteria\tunclassified Cyanobacteria\tunclassified Cyanobacteria\tcyanobacterium endosymbiont of Rhopalodia gibberula"
               elif (newcontents[i] == "Abyssogena phaseoliformis symbiont"):
                   newcontents[i] = "unclassified Bacteria\tunclassified Bacteria\tunclassified Bacteria\tunclassified Bacteria\tAbyssogena phaseoliformis symbiont"
               elif (newcontents[i] == "Candidatus Xiphinematobacter"):
                   newcontents[i] = "unclassified Verrucomicrobia Spartobacteria\tunclassified Verrucomicrobia Spartobacteria\tCandidatus Xiphinematobacter"
               elif (newcontents[i] == "Candidatus Saccharimonas"):
                   newcontents[i] = "unclassified Candidatus Saccharibacteria\tunclassified Candidatus Saccharibacteria\tunclassified Candidatus Saccharibacteria\tCandidatus Saccharimonas"
               elif (newcontents[i] == "Candidatus Bipolaricaulis"):
                   newcontents[i] = "unclassified Candidatus Bipolaricaulota\tunclassified Candidatus Bipolaricaulota\tunclassified Candidatus Bipolaricaulota\tCandidatus Bipolaricaulis"
               elif (newcontents[i] in gammaproteobacteria_genera):
                   newcontents[i] = "unclassified Gammaproteobacteria incertae sedis\t"+newcontents[i]
               elif (newcontents[i] in betaproteobacteria_genera):
                   newcontents[i] = "unclassified Betaproteobacteria incertae sedis\t"+newcontents[i]
               elif (newcontents[i] in alphaproteobacteria_genera):
                   newcontents[i] = "unclassified Alphaproteobacteria incertae sedis\t"+newcontents[i]
               elif (newcontents[i] in tissierellia_genera):
                   newcontents[i] = "unclassified Tissierellia incertae sedis\t"+newcontents[i]
               elif (newcontents[i] == "SAR116 cluster"):
                   newcontents[i] = "unclassified Alphaproteobacteria incertae sedis"
               elif (newcontents[i] == "sulfur-oxidizing symbionts"):
                   newcontents[i] = "unclassified Gammaproteobacteria incertae sedis"
               elif (newcontents[i] == "Abyssogena phaseoliformis symbiont"):
                   newcontents[i] = "unclassified Bacteria\tunclassified Bacteria\tAbyssogena phaseoliformis symbiont"
               elif (newcontents[i] == "endosymbiont of unidentified scaly snail isolate Monju"):
                   newcontents[i] = "unclassified Gammaproteobacteria\tunclassified Gammaproteobacteria\tendosymbiont of unidentified scaly snail isolate Monju"
               elif (newcontents[i] == "endosymbiont of Acanthamoeba sp. UWC8"):
                   newcontents[i] = "unclassified Holosporaceae\tendosymbiont of Acanthamoeba sp. UWC8"
               elif (newcontents[i] == "Rickettsiales endosymbiont of Stachyamoeba lipophora"):
                   newcontents[i] = "unclassified Rickettsiales\tRickettsiales endosymbiont of Stachyamoeba lipophora"
               elif (newcontents[i] in citations):
                   newcontents[i] = citations[newcontents[i]]
               elif (newcontents[i] == "Pseudomonas denitrificans (nom. rej.)"):
                   newcontents[i] = "Pseudomonas denitrificans"
               newline += newcontents[i]
               if (i == len(newcontents)-1):
                   newline += "\n"
               else:
                   newline += "\t"
           self.lines.append(newline)

    def output(self, outfile):
      outfile = open(outfile, 'w')
      for line in self.lines:
            outfile.write(line)
