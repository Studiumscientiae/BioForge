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

from src.core.sequence import Sequence

class AnalysisService:
    """
    Coordinates biological analyses.
    """

    def sequence_length(self,sequence: Sequence) -> int:
        """Coordinate sequence length analysis for a biological sequence."""

        return sequence.length

    def base_counts(self, sequence: Sequence) -> dict[str, int]:
        """Coordinate nucleotide base count analysis for a biological sequence."""

        return sequence.base_counts()

    def gc_content(self, sequence: Sequence) -> float:
        """Coordinate GC content analysis for a biological sequence."""

        return sequence.gc_content()

    def molecular_weight(self, sequence: Sequence) -> float:
        """Calculate molecular weight."""

        return sequence.molecular_weight()