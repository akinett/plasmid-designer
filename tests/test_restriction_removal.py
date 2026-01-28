import os
from src.main import read_fasta
from src.restriction_tools import remove_restriction_sites


def test_ecori_removal():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    fasta_path = os.path.join(base_dir, "data", "pUC19.fa")

    sequence = read_fasta(fasta_path)
    modified = remove_restriction_sites(sequence, ["EcoRI"])

    assert "GAATTC" not in modified
