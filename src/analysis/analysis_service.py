"""
analysis_service.py

Analysis coordination service for BioForge.

Responsibilities:
- Receive analysis requests.
- Coordinate analysis modules.
- Aggregate analysis results.
- Return analysis results to the application controller.

Does not perform:
- GUI operations
- Sequence validation
- File parsing
- Exporting
- History management
- Analysis algorithms
"""

from Bio.Seq import Seq
from src.core.sequence import Sequence

class AnalysisService:
    """
    Coordinates biological analyses.
    """

    # ==========================================================
    # Length
    # ==========================================================

    def get_sequence_length(self,sequence: Sequence) -> int:
        """Coordinate sequence length analysis for a biological sequence."""

        return sequence.length

    # ==========================================================
    # Composition Analysis
    # ==========================================================

    def get_gc_content(self, sequence: Sequence) -> float:
        """Coordinate GC content analysis for a biological sequence."""

        return sequence.gc_content()

    def get_at_content(self, sequence: Sequence) -> float:
        """Coordinate AT content analysis for a biological sequence."""

        return sequence.at_content()

    def get_base_counts(self, sequence: Sequence) -> dict[str, int]:
        """Coordinate nucleotide base count analysis for a biological sequence."""

        return sequence.base_counts()

    def get_molecular_weight(self, sequence: Sequence) -> float:
        """Calculate molecular weight."""

        return sequence.molecular_weight()

    # ==========================================================
    # Sequence Operations
    # ==========================================================

    def get_reverse(self, sequence: Sequence) -> Seq:
        """Coordinate sequence reverse operation."""

        return sequence.reverse()

    def get_complement(self, sequence: Sequence) -> Seq:
        """Coordinate sequence complement operation."""

        return sequence.complement()

    def get_reverse_complement(self, sequence: Sequence) -> Seq:
        """Coordinate sequence reverse complement operation."""

        return sequence.reverse_complement()

    # ==========================================================
    # Gene Expression
    # ==========================================================

    def get_transcribe(self, sequence: Sequence) -> str:
        """Coordinate sequence transcription operation."""

        return sequence.transcribe()

    def get_translate(self, sequence: Sequence) -> tuple[str, int]:
        """Return translated protein and ignored nucleotide count."""

        return sequence.translate()

    # ==========================================================
    # Codon Analysis
    # ==========================================================

    def get_codon_frequency(self, sequence: Sequence) -> dict[str, int]:
        """Coordinate codon frequency analysis for a biological sequence."""

        return sequence.codon_frequency()

    def get_codon_usage(self,sequence: Sequence) -> list[dict[str, str | int]]:
        """Coordinate codon usage analysis for a biological sequence."""

        return sequence.codon_usage()