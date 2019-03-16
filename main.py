from Seq import Sequence
from Seq import sequence_class_as_function
import matplotlib.pyplot as pl

# importing the files and making an instance of them for later use in code
file_1 = open('genome_01.dat', 'r')
gen1 = file_1.read()
information, sequence = gen1.split("\n")
genome1 = Sequence(information, sequence)

file_2 = open('genome_02.dat', 'r')
gen2 = file_2.read()
information, sequence = gen2.split("\n")
genome2 = Sequence(information, sequence)

# Task 1 - create some instances
dna1 = Sequence('I am DNA 1\n', 'AATTCCGG')
dna2 = Sequence('I am DNA 2\n', 'TTCCGGAA')
dna3 = Sequence('I am DNA 3\n', 'AATTCCGG')  # for later use
dna4 = Sequence('I am DNA 4\n', 'aatcccgg')  # for later use - notice the lower case does not matter
print(dna1)
print(dna1.information, dna1.sequence)
print(dna2.information, dna2.sequence)

# Task 2 - length of the sequence
print('The sample instance, dna1, has the dna sequence length of :')
dna1.length()

# Task 3 - evaluating if the sample sequence is dna
evaluation = dna1.is_dna()
print('the sample instance is DNA:', evaluation)
print('If this value is "True" the code will not run again to evaluate if the sequence is a DNA:', dna1.dna_flag)

# Task 4 - evaluating if two sequences from two strings are equal AND if the second
# one is another sequence from the class we defined
equality = dna1.__eq__(dna3)
print('The two instances (dna1 and dna3) are both Sequence and equal:', equality)
equality = dna1.__eq__(dna2)
print('The two instances (dna1 and dna2) are both Sequence and equal:', equality)

# Task 5 - creating a complement for the dna sequence
print('For our next test, take a look at this:\nThis is dna1:\n', dna1.sequence)
print('And this is dna1\'s complement:\n', dna1.complement())
print('And this is dna2:\n', dna2.sequence)
print('With it\'s complement:\n', dna2.complement())

# Task 6 - Finding the first non-matching pair of bases
print('Looking for non-matching pair in dna1 and dna3, result is:', dna1.first_non_matching_bases(dna3))
print('Comparing dna1 and dna4 in the same way, first non-matching pair is in: ', dna1.first_non_matching_bases(dna4))

# Task 7 - using a function to somehow mimic the class
new_sequence, length_of_sequence = sequence_class_as_function('genome_01.dat')
print('The new instance:', new_sequence)
print('Length of the new sequence (genome1):', length_of_sequence)

# Task 8 - Create a list of genes from the first genome
genes_from_genome1 = genome1.the_gene_separator()
print('The genes from genome1 in memory:\n', genes_from_genome1)
print('For example the first genome_1\'s gene sequence is :', genes_from_genome1[0].sequence)

# Task 9 - Creating a histogram of gene length
length_genes_from_genome1 = []
for i in range(0, len(genes_from_genome1)):
    length_genes_from_genome1.append(len(genes_from_genome1[i].sequence))
fig = pl.hist(length_genes_from_genome1, bins=100, rwidth=0.4)
pl.title('Gene length histogram')
pl.xlabel('Length of genes')
pl.ylabel('Number of occurrences')
pl.savefig('histogram.png')
pl.show()

# Task 10 - Swap mutation and plot
y = genome1.swap_mutation(genome2)
x = length_genes_from_genome1
print(x)
print(y)
pl.scatter(x, y)
pl.title('Mutations per gene length')
pl.xlabel('Length of genes')
pl.ylabel('Number of mutations')
pl.savefig('scatter.png')
pl.show()

# Task 11 - check the __init__ method - sequence part attribute, and dna4 example
#  - it works if you check these.

# Task 12 - the double underscore before the attributes help with the private fields
# e.g. __information for the information part of the sequences
# then with the use of @property to define getters (simply, calling the private fields from within the class
# by a method built in the class which gives us access to a private field) we can call them. And with the help of
# @x.setters we can set values to private fields, which are not accessible without these methods.
