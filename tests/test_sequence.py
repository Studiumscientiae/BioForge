"""
test_sequence.py

Unit tests for the BioForge Sequence model.

Responsibilities:
- Verify sequence statistics.
- Verify sequence transformation operations.
- Verify sequence normalization.
- Verify biological sequence behavior.

Does NOT perform:
- GUI testing
- Validation testing
- File parsing
- Service layer testing
"""

import pytest

from src.core.sequence import Sequence


# ==========================================================
# Sequence Statistics
# ==========================================================

def test_sequence_length():
    sequence = Sequence("Test", "ATGC")

    assert sequence.length == 4


def test_gc_content():
    sequence = Sequence("Test", "ATGC")

    assert sequence.gc_content() == pytest.approx(50.0)


def test_at_content():
    sequence = Sequence("Test", "ATGC")

    assert sequence.at_content() == pytest.approx(50.0)


def test_base_counts():
    sequence = Sequence("Test", "ATGC")

    assert sequence.base_counts() == {
        "A": 1,
        "T": 1,
        "G": 1,
        "C": 1,
    }


def test_molecular_weight():
    sequence = Sequence("Test", "ATGC")

    assert sequence.molecular_weight() == pytest.approx(
        1253.8027,
        rel=1e-6,
    )


# ==========================================================
# Sequence Operations
# ==========================================================

def test_reverse():
    sequence = Sequence("Test", "ATGC")

    assert str(sequence.reverse()) == "CGTA"


def test_complement():
    sequence = Sequence("Test", "ATGC")

    assert str(sequence.complement()) == "TACG"


def test_reverse_complement():
    sequence = Sequence("Test", "ATGC")

    assert str(sequence.reverse_complement()) == "GCAT"


# ==========================================================
# Normalization
# ==========================================================

def test_lowercase_sequence_is_normalized():
    sequence = Sequence("Test", "atgc")

    assert str(sequence.sequence) == "ATGC"


# ==========================================================
# Single Nucleotide
# ==========================================================

@pytest.mark.parametrize(
    "base, complement",
    [
        ("A", "T"),
        ("T", "A"),
        ("G", "C"),
        ("C", "G"),
    ],
)
def test_single_nucleotide_operations(base, complement):
    sequence = Sequence("Test", base)

    assert sequence.length == 1
    assert str(sequence.reverse()) == base
    assert str(sequence.complement()) == complement
    assert str(sequence.reverse_complement()) == complement