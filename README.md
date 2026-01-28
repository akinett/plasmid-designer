# Plasmid Designer

## Overview

This project implements an automated plasmid design pipeline in Python.
Given a DNA sequence from an unknown organism, the tool generates a
functional plasmid sequence compatible with the host organism.

The pipeline performs the following steps:

- Detects the origin of replication (ORI) using an AT-rich sliding window approach  
- Parses a user-provided design file describing plasmid features  
- Applies restriction site deletions as specified  
- Outputs the final plasmid sequence in FASTA format  

---

## Input

- **Input.Fa**  
  DNA sequence of an unknown organism  
  *(Test case used: `pUC19.fa`)*

- **Design.txt**  
  User-defined plasmid design instructions

- **markers.tab**  
  List of possible markers (provided for reference; not required for core logic)

---

## Output

- **Output.Fa**  
  Designed plasmid DNA sequence in FASTA format

---

## ORI Detection

The origin of replication (ORI) is identified by scanning the DNA sequence
with a sliding window and selecting the region with the highest AT content.
This AT-rich heuristic is a standard method taught in class for bacterial
ORI prediction.

---

## Restriction Site Removal

For the provided pUC19 test case, the EcoRI restriction site  
(**GAATTC**) is deleted from the plasmid, as specified in the assignment.

The final output is verified to confirm the complete absence of the EcoRI
recognition sequence.

---

## Testing

Unit tests are implemented using **pytest** to verify:

- Correct ORI detection  
- Proper parsing of the design file  
- Complete removal of the EcoRI restriction site  

All tests pass successfully.

To run tests:

```bash
python -m pytest
