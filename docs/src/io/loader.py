"""
loader.py

File loading utilities for BioForge.

Responsibilities:
- Determine the appropriate parser based on file type
- Delegate parsing to the corresponding parser.
- Return parsed Sequence objects.

Does not perform:
- Biological sequence analysis
- Sequence validation
- GUI operations
- File parsing logic
"""

from pathlib import Path
from src.io.fasta_parser import FASTAParser

class Loader:
    """
    Coordinates loading biological sequences.

    The loader selects the appropriate parser based on the file
    extension and returns parsed Sequence objects.
    """

    @staticmethod
    def load(file_path: str):
        """
        Load biological sequences from a supported file.

        Parameters
        ----------
        file_path : str
            Path to the sequence file.

        Returns
        -------
        list[Sequence]
            Parsed biological sequences.

        Raises
        ------
        ValueError
            If the file format is unsupported.
        """

        path = Path(file_path)
        extension= path.suffix.lower()

        if extension in {".fasta", ".fa", ".fna"}:
            return FASTAParser.parse(file_path)

        raise ValueError(
            f"Unsupported file format: {extension}")

