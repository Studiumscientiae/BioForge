"""
codon_usage_service.py

Service for loading and managing organism-specific codon usage datasets.

Responsibilities:
- Discover available organism datasets
- Load codon usage CSV files
- Cache loaded DataFrames
- Provide access to reference codon usage tables

Does not perform:
- Codon comparison
- Frequency normalization
- Rare codon detection
- CAI or RSCU calculations
"""

from pathlib import Path

import pandas as pd


class CodonUsageService:
    """Service for organism-specific codon usage reference data."""

    def __init__(self):
        """Initialize the codon usage service."""
        self._cache = {}

        # BioForge/
        # ├── src/
        # └── data/
        self._data_dir = (
            Path(__file__).resolve().parents[2]
            / "data"
            / "codon_usage"
        )

    def list_organisms(self) -> list[str]:
        """
        Discover available organism datasets.

        Returns
        -------
        list[str]
            Sorted list of organism names.
        """
        organisms = []

        if not self._data_dir.exists():
            return organisms

        for csv_file in self._data_dir.glob("*.csv"):
            organism = csv_file.stem.replace("_", " ")
            organisms.append(organism)

        return sorted(organisms)

    def load_organism(self, organism: str) -> pd.DataFrame:
        """
        Load an organism's codon usage dataset.

        Uses an in-memory cache to avoid repeated disk access.

        Parameters
        ----------
        organism : str
            Organism name (e.g. 'Homo sapiens').

        Returns
        -------
        pandas.DataFrame
            Codon usage reference table.

        Raises
        ------
        FileNotFoundError
            If the organism dataset cannot be found.
        """

        if organism in self._cache:
            return self._cache[organism]

        filename = organism.replace(" ", "_") + ".csv"
        filepath = self._data_dir / filename

        if not filepath.exists():
            raise FileNotFoundError(
                f"Codon usage dataset not found: {filename}"
            )

        dataframe = pd.read_csv(filepath)

        self._cache[organism] = dataframe

        return dataframe

    def get_dataframe(self, organism: str) -> pd.DataFrame:
        """
        Return the cached DataFrame for an organism.

        Loads the dataset if necessary.
        """
        return self.load_organism(organism)

    def clear_cache(self) -> None:
        """Clear all cached datasets."""
        self._cache.clear()