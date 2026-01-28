def read_fasta(file_path):
    """
    Reads a FASTA file and returns the DNA sequence as a single string.
    Header lines (starting with '>') are ignored.
    """
    sequence = []

    with open(file_path, "r") as f:
        for line in f:
            if not line.startswith(">"):
                sequence.append(line.strip())

    return "".join(sequence).upper()

def write_fasta(sequence, file_path, header="Designed_Plasmid"):
    """
    Writes a DNA sequence to a FASTA file with line wrapping.
    """
    with open(file_path, "w") as f:
        f.write(f">{header}\n")
        for i in range(0, len(sequence), 70):
            f.write(sequence[i:i+70] + "\n")


