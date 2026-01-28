# Restriction enzyme recognition sequences
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
    Removes all occurrences of restriction enzyme recognition sites
    from the given DNA sequence.

    Args:
        sequence (str): DNA sequence
        enzymes (list): List of enzyme names to remove

    Returns:
        str: Modified DNA sequence
    """
    modified_sequence = sequence

    for enzyme in enzymes:
        site = RESTRICTION_SITE_SEQUENCES.get(enzyme)
        if site:
            modified_sequence = modified_sequence.replace(site, "")

    return modified_sequence
