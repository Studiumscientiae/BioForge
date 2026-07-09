"""
validator.py

Validation utilities for BioForge.

Responsibilities:
- Validate biological sequences.
- Determine whether a sequence contains only valid characters.

Does NOT perform:
- Sequence analysis
- File parsing
- User interaction
"""

class Validator:
    """Validates biological sequences."""
    DNA_BASES={"A","T","G","C"}

    @classmethod
    def is_valid_dna(cls,sequence: str) -> bool:
        """
        Check whether a sequence contains only valid DNA bases.

        Parameters
        ----------
        sequence : str
            DNA sequence to validate.

        Returns
        -------
        bool
            True if valid, otherwise False.
        """

        sequence= sequence.upper().strip()

        if not sequence:
            return False

        return all(base in cls.DNA_BASES for base in sequence)

