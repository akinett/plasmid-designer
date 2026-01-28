# Restriction enzyme recognition sequences
# (as taught in class / standard cloning references)

RESTRICTION_SITE_SEQUENCES = {
    "EcoRI": "GAATTC",
    "BamHI": "GGATCC",
    "HindIII": "AAGCTT",
    "PstI": "CTGCAG",
    "SphI": "GCATGC",
    "SalI": "GTCGAC",
    "XbaI": "TCTAGA",
    "KpnI": "GGTACC",
    "SacI": "GAGCTC",
    "SmaI": "CCCGGG"
}


def remove_restriction_sites(sequence, enzymes):
    """
    Removes specified restriction enzyme recognition sites
    from a DNA sequence.

    Args:
        sequence (str): DNA sequence
        enzymes (list): List of restriction enzyme names to remove

    Returns:
        str: Modified DNA sequence with specified sites deleted
    """

    modified_sequence = sequence

    for enzyme in enzymes:
        site = RESTRICTION_SITE_SEQUENCES.get(enzyme)
        if site:
            modified_sequence = modified_sequence.replace(site, "")

    return modified_sequence
