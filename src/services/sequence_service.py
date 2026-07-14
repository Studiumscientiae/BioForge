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


class SequenceService:
    """
    Coordinates sequence processing.
    """

    def validate_sequence(self,name: str,sequence: str) -> Sequence:
        """
        Validate user input and create a Sequence object.
        """

        if not Validator.is_valid_dna(sequence):
            raise ValueError("Invalid DNA sequence.")

        return Sequence(name, sequence)

    def load_sequences(self,file_path: str) -> list[Sequence]:
        """
        Load biological sequences from a supported file.
        """

        return Loader.load(file_path)