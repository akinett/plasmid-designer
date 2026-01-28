from src.main import read_fasta
from src.ori_finder import find_ori

def test_ori_detection():
    sequence = read_fasta("data/pUC19.fa")
    ori = find_ori(sequence)

    assert ori is not None
    assert len(ori) == 500
    assert (ori.count("A") + ori.count("T")) / len(ori) > 0.5
