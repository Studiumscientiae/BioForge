"""
sequence_service.py

Application service for sequence processing.

Responsibilities:
- Validate DNA sequences.
- Create Sequence domain objects.
- Load sequences from supported file formats.

Does not perform:
- Biological analysis
- GUI operations
- File format parsing logic
- Data exporting
- History management
"""

from src.core.sequence import Sequence
from src.core.validator import Validator
from src.io.loader import Loader

def process_sequence(name: str, sequence: str) -> Sequence:
    """
    Process a biological sequence
    Parameters
    ----------
    name : str
        Name of the sequence.

    sequence : str
        DNA sequence provided by the user.

    Returns
    -------
    Sequence
        A Sequence object if validation succeeds.

    Raises
    ------
    ValueError
        If the DNA sequence is invalid.
    """

    if not Validator.is_valid_dna(sequence):
        raise ValueError("Invalid DNA sequence.")

    return Sequence(name,sequence)

def load_sequences(file_path: str):
    """
    Load biological sequences from a supported file.

    Parameters
    ----------
    file_path : str
        Path to the sequence file.

    Returns
    -------
    list[Sequence]
        Parsed Sequence objects.
    """

    return Loader.load(file_path)