def parse_design_file(design_path):
    """
    Parses the plasmid design file (Design.txt).

    Assignment-specific rule:
    - The EcoRI restriction site is deleted in the pUC19 design.
    - All other entries are treated as markers or plasmid features.
    """

    restriction_sites = []
    markers = []

    with open(design_path, "r") as f:
        for line in f:
            line = line.strip()

            # Skip empty or malformed lines
            if not line or "," not in line:
                continue

            _, value = line.split(",", 1)

            # Normalize to handle whitespace and case inconsistencies
            value = value.strip().upper()

            if value == "ECORI":
                restriction_sites.append("EcoRI")
            else:
                markers.append(value)

    return {
        "restriction_sites": restriction_sites,
        "markers": markers
    }
