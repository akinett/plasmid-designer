def find_ori(sequence, window_size=500, step_size=50):
    """
    Identifies a putative origin of replication (ORI) using AT-content analysis.

    The function scans the DNA sequence using a sliding window and selects
    the region with the highest AT content, which is a commonly used heuristic
    for ORI prediction in bacterial genomes.

    Args:
        sequence (str): DNA sequence of the organism
        window_size (int): Size of the sliding window (default: 500 bp)
        step_size (int): Step size for window movement (default: 50 bp)

    Returns:
        str: Candidate ORI sequence
    """

    max_at_content = 0.0
    ori_start = 0

    for i in range(0, len(sequence) - window_size + 1, step_size):
        window = sequence[i:i + window_size]
        at_count = window.count("A") + window.count("T")
        at_content = at_count / window_size

        if at_content > max_at_content:
            max_at_content = at_content
            ori_start = i

    return sequence[ori_start:ori_start + window_size]
