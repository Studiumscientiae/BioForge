"""
file_writer.py

File writing utilities for BioForge.

Responsibilities:
- Write Sequence objects to files.
- Export sequences in FASTA format.
- Create output files.

Does not perform:
- Sequence validation
- Biological analysis
- File parsing
- GUI operations
"""

from src.core.sequence import Sequence


class FileWriter:
    """
    Writes Sequence objects to supported file formats.
    """

    @staticmethod
    def write_fasta(sequences: list[Sequence], output_path: str):
        """
        Write Sequence objects to a FASTA file.

        Parameters
        ----------
        sequences : list[Sequence]
            Sequences to write.

        output_path : str
            Destination FASTA file.
        """

        with open(output_path, "w", encoding="utf-8") as file:

            for sequence in sequences:
                file.write(f">{sequence.name}\n")
                file.write(f"{sequence.sequence}\n")