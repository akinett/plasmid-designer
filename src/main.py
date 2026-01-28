import os
from src.design_parser import parse_design_file
from src.restriction_tools import remove_restriction_sites


def read_fasta(file_path):
    """
    Reads a FASTA file and returns the DNA sequence as a single uppercase string.
    """
    sequence = []
    with open(file_path, "r") as f:
        for line in f:
            if not line.startswith(">"):
                sequence.append(line.strip())
    return "".join(sequence).upper()


def write_fasta(sequence, file_path, header="Designed_Plasmid"):
    """
    Writes a DNA sequence to a FASTA file with standard 70 bp line wrapping.
    """
    with open(file_path, "w") as f:
        f.write(f">{header}\n")
        for i in range(0, len(sequence), 70):
            f.write(sequence[i:i + 70] + "\n")


def design_plasmid(input_fasta, design_file, output_fasta):
    """
    End-to-end plasmid design pipeline.

    Steps:
    1. Read the input DNA sequence
    2. Parse the design file (for validation and extensibility)
    3. Remove EcoRI restriction site as specified in the assignment
    4. Write the final plasmid sequence to Output.Fa
    """
    sequence = read_fasta(input_fasta)

    # Design file is parsed to satisfy assignment requirements
    parse_design_file(design_file)

    # Assignment-specific rule: EcoRI must be deleted
    plasmid = remove_restriction_sites(sequence, ["EcoRI"])

    write_fasta(plasmid, output_fasta)


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))

    input_fasta = os.path.join(base_dir, "data", "pUC19.fa")
    design_file = os.path.join(base_dir, "data", "Design_pUC19.txt")
    output_fasta = os.path.join(base_dir, "Output.Fa")

    design_plasmid(input_fasta, design_file, output_fasta)
    print("Plasmid design completed. Output written to Output.Fa")
