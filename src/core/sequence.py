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
from collections import Counter
from Bio.Data import CodonTable

# ==========================================================
# Amino Acid Metadata
# ==========================================================

AMINO_ACID_NAMES = {
    "A": "Alanine",
    "R": "Arginine",
    "N": "Asparagine",
    "D": "Aspartic acid",
    "C": "Cysteine",
    "Q": "Glutamine",
    "E": "Glutamic acid",
    "G": "Glycine",
    "H": "Histidine",
    "I": "Isoleucine",
    "L": "Leucine",
    "K": "Lysine",
    "M": "Methionine",
    "F": "Phenylalanine",
    "P": "Proline",
    "S": "Serine",
    "T": "Threonine",
    "W": "Tryptophan",
    "Y": "Tyrosine",
    "V": "Valine",
    "*": "Stop"
}

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

    def _codons(self) -> list[str]:
        """
        Split the DNA sequence into complete codons.

        Returns:
            list[str]: List of complete 3-base codons.

        Notes:
            Any trailing bases that do not form a complete codon
            are ignored.
        """
        return [
            str(self.sequence[i:i + 3])
            for i in range(0, len(self.sequence) - 2, 3)
        ]

    @property
    def codon_count(self) -> int:
        """Return the total number of complete codons."""

        return len(self._codons())

    def transcribe(self) -> str:
        """Return the RNA transcript of the DNA sequence."""

        return str(self.sequence.transcribe())

    def translate(self) -> tuple[str, int]:
        """
        Translate the DNA sequence into a protein.

        Returns
        -------
        tuple[str, int]
            (
                translated protein sequence,
                number of ignored trailing nucleotides
            )
        """

        remainder = self.length % 3

        dna = self.sequence

        if remainder:
            dna = dna[:-remainder]

        protein = dna.transcribe().translate()

        return str(protein), remainder

    def codon_frequency(self) -> dict[str, int]:
        """
            Count the frequency of each codon in the DNA sequence.

            Returns:
                dict[str, int]: Dictionary mapping codons to their counts.
            """

        return dict(Counter(self._codons()))

    def codon_relative_frequency(self) -> dict[str, float]:
        """
        Return the relative frequency of each codon
        as occurrences per thousand (‰).

        Formula
        -------
        (count / total_codons) × 1000
        """

        frequency = self.codon_frequency()

        total_codons = sum(frequency.values())

        if total_codons == 0:
            return {}

        return {
            codon: (count / total_codons) * 1000
            for codon, count in frequency.items()
        }

    def codon_usage(self) -> list[dict[str, str | int]]:
        """
        Return codon usage statistics for the sequence.

        Each record contains:

        - DNA codon
        - Amino acid symbol
        - Amino acid name
        - Observed count
        """

        table = CodonTable.standard_dna_table
        frequency = self.codon_frequency()
        relative_frequency = self.codon_relative_frequency()

        usage = []

        for codon in sorted(frequency):
            count = frequency[codon]
            amino_acid = table.forward_table.get(codon, "*")

            usage.append({
                "codon": codon,
                "amino_acid": amino_acid,
                "amino_acid_name": AMINO_ACID_NAMES[amino_acid],
                "count": count,
                "sequence_frequency": relative_frequency[codon],
            })

        return usage