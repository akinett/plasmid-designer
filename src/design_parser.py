# Known restriction enzymes (from class material)
KNOWN_RESTRICTION_ENZYMES = {
    "EcoRI", "BamHI", "HindIII", "PstI", "SphI",
    "SalI", "XbaI", "KpnI", "SacI", "SmaI"
}


def parse_design_file(design_path):
    """
    Parses Design.txt.

    Returns:
        dict with keys:
            - 'restriction_sites'
            - 'markers'
    """

    restriction_sites = []
    markers = []

    with open(design_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or "," not in line:
                continue

            _, value = line.split(",", 1)
            value = value.strip()

            if value in KNOWN_RESTRICTION_ENZYMES:
                restriction_sites.append(value)
            else:
                markers.append(value)

    return {
        "restriction_sites": restriction_sites,
        "markers": markers
    }
