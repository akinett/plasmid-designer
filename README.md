Plasmid Designer
Overview

This project implements an automated plasmid design pipeline.
Given an input DNA sequence from an unknown organism, the tool:

Detects the origin of replication (ORI) using an AT-rich sliding window approach

Parses a user-provided design file specifying plasmid modifications

Applies restriction site deletions as required

Outputs a functional plasmid sequence compatible with the host organism

Input

Input.Fa – DNA sequence of an unknown organism (test case: pUC19.fa)

Design.txt – user-specified plasmid design instructions

markers.tab – list of possible markers (not mandatory for core logic)

Output

Output.Fa – designed plasmid sequence

ORI Detection

The ORI is identified by scanning the sequence with a sliding window and selecting the region with the highest AT content, a standard method taught in class.

Restriction Site Removal

For the provided pUC19 test case, the EcoRI restriction site (GAATTC) is deleted from the plasmid as specified.
Final output verification confirms the absence of this site.

Testing

Unit tests verify:

ORI detection

Design file parsing

Complete removal of EcoRI from the final plasmid

All tests pass using pytest.

How to Run
python -m src.main


The output plasmid will be written to Output.Fa.