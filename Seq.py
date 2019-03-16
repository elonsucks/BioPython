def sequence_class_as_function(filename):
    """a function that inputs 'filename' and opens the file reading ASCII
    file format, then creates a new instance and returns both instance
    and the length of it's sequence"""
    file = open(filename, 'r', encoding='ASCII')
    file = file.read()
    new_inf, new_seq = file.split('\n')
    sequence_new = Sequence(new_inf, new_seq)
    return sequence_new, len(sequence_new.sequence)


class Sequence:
    """Create a class object, with attributes of information (date and time, basically
    the first line of file) and the sequence (the rest of the file)
    """

    def __init__(self, information, sequence):
        """defining attributes of the sequences in this class, dna_flag is used
        later to assess if the sequence has been checked for being a valid dna or not,
        so that it won't be tested again --- this method is case insensitive due to
        the .upper() following the sequence.
        Also the fields are private with the double underscore"""
        self.__information = information
        self.__sequence = sequence.upper()
        self.dna_flag = False

    @property
    def sequence(self):
        """__sequence GETTER, can access the private field sequence with this"""
        return self.__sequence

    @property
    def information(self):
        """__information GETTER, can access the private field information with this"""
        return self.__information

    @sequence.setter
    def sequence(self, sequence):
        """here we can set value to sequence which is a private field"""
        self.__sequence = sequence.upper()

    @information.setter
    def information(self, information):
        """here we can set value to information which is a private field"""
        self.__information = information

    def length(self):
        """defines the length of the DNA bases (characters in the string) """
        print(len(self.__sequence))

    def is_dna(self):
        """checks if the dna is assessed to be a valid dna, and if it has not been checked,
        it is analysed by comparing bases with ATCG """
        global evaluation
        if not self.dna_flag:
            for i in self.__sequence:
                if i not in ['A', 'C', 'T', 'G']:
                    evaluation = False
                else:
                    evaluation = True
        self.dna_flag = True
        return evaluation

    def __eq__(self, other):
        """checks if the other instance is a class Sequence instance then
        checks if the dna string attached to it is equal with dna sequence in self"""
        if isinstance(other, self.__class__) and other.__sequence == self.__sequence:
            return True
        else:
            return False

    def complement(self):
        """this method creates the complement (meaning replacing A with T, and so on...)
        and gives the new sequence out as an output"""
        new_sequence = ""
        for i in self.__sequence:
            if i == 'A':
                new_sequence = new_sequence + "T"
            elif i == 'C':
                new_sequence = new_sequence + "G"
            elif i == 'G':
                new_sequence = new_sequence + "C"
            elif i == 'T':
                new_sequence = new_sequence + "A"
        return new_sequence

    def first_non_matching_bases(self, other):
        """This method finds the first pair of non-matching bases and returns it, and if non were found
        returns -1 as to say the sequences are identical, also if the sequences are not of the
        same size it raises the error saying 'cannot compare sequences of different lengths' """
        check = []
        if len(self.__sequence) == len(other.__sequence):
            for i in range(0, len(self.__sequence)):
                if self.__sequence[i] != other.__sequence[i]:
                    check.append(i)
            if len(check) == 0:
                return -1
            else:
                return check[0]
        else:
            raise Exception('cannot compare sequences of different lengths')

    def the_gene_separator(self):
        """separates the genome into the genes that are sliced by
        "AAAAAAAAAATTTTTTTTTTTT" separator and returns instances
        created by the genes as sequences"""
        sub_genome = []
        strings = self.__sequence.split("AAAAAAAAAATTTTTTTTTT")
        for i in range(0, len(strings)):
            sub_genome.append(Sequence(self.__information, strings[i]))
        return sub_genome

    def swap_mutation(self, other):
        """checks for swap mutations in the given sequences and returns the
        value as the number of mutations"""
        gene_list_1 = self.the_gene_separator()
        gene_list_2 = other.the_gene_separator()
        swap_counter = 0
        list_swap_counter = []
        for i in range(len(gene_list_1)):
            for j in range(len(gene_list_1[i].__sequence)):
                if gene_list_1[i].sequence[j] != gene_list_2[i].__sequence[j]:
                    swap_counter = swap_counter + 1
            list_swap_counter.append(swap_counter)
            swap_counter = 0
        return list_swap_counter
