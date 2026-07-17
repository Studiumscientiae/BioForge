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

    def __str__(self) -> str:
        """Return string representation of Biological sequence."""

        return (
            f"Sequence Name: {self.name}\n"
            f"Sequence: {self.sequence}\n"
            f"Length: {self.length} bases"
        )

    @ property
    def length(self) -> int:
        """Return the length of a Biological sequence."""

        return len(self.sequence)

    def gc_content(self) -> float:
        """Return GC content as a percentage."""

        return gc_fraction(self.sequence)* 100

    def at_content(self) -> float:
        """Return AT content as a percentage."""

        return (1 - gc_fraction(self.sequence)) * 100

    def base_counts(self) -> dict[str, int]:
        """Return nucleotide counts."""

        return{
            "A": self.sequence.count("A"),
            "T": self.sequence.count("T"),
            "G": self.sequence.count("G"),
            "C": self.sequence.count("C"),
        }

    def molecular_weight(self) -> float:
        """Return the molecular weight of the sequence."""

        return molecular_weight(self.sequence,
                                seq_type="DNA")

    def reverse(self) -> Seq:
        """Return the reversed sequence.
        [read sequence backward]"""

        return self.sequence[::-1]

    def complement(self) -> Seq:
        """Return the complement of the sequence.
        [A⇆T & G⇆C]"""

        return self.sequence.complement()

    def reverse_complement(self) -> Seq:
        """Return the reverse complement of the sequence.
        [Create and read the complement backward]"""

        return self.sequence.reverse_complement()

    def transcribe(self) -> Seq:
        """Return the RNA transcript of the DNA sequence."""

        return str(self.sequence.transcribe())

    def translate(self) -> Seq:
        """Return the protein translated from the DNA sequence."""

        rna = self.sequence.transcribe()
        return str(rna.translate())