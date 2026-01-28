import os
from src.main import read_fasta
from src.ori_finder import find_ori


def test_ori_detection():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    fasta_path = os.path.join(base_dir, "data", "pUC19.fa")

    sequence = read_fasta(fasta_path)
    ori = find_ori(sequence)

    assert ori is not None
    assert len(ori) == 500
    assert (ori.count("A") + ori.count("T")) / len(ori) > 0.5

