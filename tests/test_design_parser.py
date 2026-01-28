import os
from src.design_parser import parse_design_file


def test_design_parser():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    design_path = os.path.join(base_dir, "data", "Design_pUC19.txt")

    design = parse_design_file(design_path)

    # EcoRI is not present in the design file (it is already deleted)
    assert "EcoRI" not in design["restriction_sites"]

    # Other entries should be parsed as markers/features
    assert "AMPICILLIN" in design["markers"]
