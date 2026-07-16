"""
test_validator.py

Unit tests for the BioForge DNA sequence validator.

Responsibilities:
- Verify valid DNA sequence detection.
- Verify invalid DNA sequence rejection.
- Verify input normalization behavior.

Does NOT perform:
- Biological analysis
- GUI testing
- File parsing
- Service layer testing
"""

import pytest

from src.core.validator import Validator


# ==========================================================
# Valid DNA Sequences
# ==========================================================

@pytest.mark.parametrize(
    "sequence",
    [
        "ATGC",
        "atgc",
        "A",
        "T",
        "G",
        "C",
        "AAAAAA",
        "TTTTTT",
        "GGGGGG",
        "CCCCCC",
        "ATATGCGC",
    ],
)
def test_valid_dna_sequences(sequence):
    assert Validator.is_valid_dna(sequence)


# ==========================================================
# Invalid DNA Sequences
# ==========================================================

@pytest.mark.parametrize(
    "sequence",
    [
        "",
        " ",
        "ATGX",
        "ATG1",
        "1234",
        "ATG C",
        "***",
        "RNA",
        "U",
        "ATGU",
    ],
)
def test_invalid_dna_sequences(sequence):
    assert not Validator.is_valid_dna(sequence)