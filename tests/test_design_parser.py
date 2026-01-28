import os
from src.design_parser import parse_design_file


def test_design_parser():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    design_path = os.path.join(base_dir, "data", "Design_pUC19.txt")

    design = parse_design_file(design_path)

    assert "BamHI" in design["restriction_sites"]
    assert "HindIII" in design["restriction_sites"]
    assert "Ampicillin" in design["markers"]
