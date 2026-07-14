"""
sequence.py

Defines the core Sequence object used throughout BioForge.

Responsibilities:
- Store biological sequence data.
- Normalize sequence format.
- Provide basic metadata such as length.

Non-responsibilities:
- Validation
- Biological analysis
- File parsing
- Reporting
"""

from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction, molecular_weight

class Sequence:

    def __init__(self,name: str,sequence: str):
        self.name= name
        self.sequence= Seq(sequence.upper().strip())

    @ property
    def length(self) -> int:
        """Return the length of a Biological sequence."""

        return len(self.sequence)

    def base_counts(self) -> dict[str, int]:
        """Return nucleotide counts."""

        return{
            "A": self.sequence.count("A"),
            "T": self.sequence.count("T"),
            "G": self.sequence.count("G"),
            "C": self.sequence.count("C"),
        }

    def gc_content(self) -> float:
        """Return GC content as a percentage."""

        return gc_fraction(self.sequence)* 100

    def molecular_weight(self) -> float:
        """Return the molecular weight of the sequence."""

        return molecular_weight(self.sequence,
                                seq_type="DNA")

    def __str__(self) -> str:
        """Return string representation of Biological sequence."""

        return(
            f"Sequence Name: {self.name}\n"
            f"Sequence: {self.sequence}\n"
            f"Length: {self.length} bases"
        )
