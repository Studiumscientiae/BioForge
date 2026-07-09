"""
fasta_parser.py

FASTA parsing utilities for BioForge.

Responsibilities:
- Read FASTA files
- Parse FASTA files
- Create sequence objects

Does not perform:
- Sequence validation
- Biological analysis
- GUI operations
- File format selection

Performs:
- Opens a FASTA file.
- Reads it line by line.
- Detects headers.
- Handles multi-line sequences.
- Creates Sequence objects.
- Returns a list of parsed sequences.
"""

from src.core.sequence import Sequence

class FASTAParser:
    """
    Parses FASTA files into Sequence objects.
    """

    @staticmethod
    def parse(file_path: str):
        with open(file_path, "r", encoding="utf-8") as file:
            sequences = []

            header = None
            sequence_lines = []

            for line in file:
                line = line.strip()
                if not line:
                    continue

                if line.startswith(">"):

                    if header is not None:
                        sequences.append(
                            Sequence(header, "".join(sequence_lines)))

                    header = line[1:]
                    sequence_lines = []

                else:
                    sequence_lines.append(line)

            if header is not None:
                sequences.append(
                    Sequence(header, "".join(sequence_lines)))

        return sequences