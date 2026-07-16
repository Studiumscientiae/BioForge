"""
test_analysis_service.py

Unit tests for the BioForge AnalysisService.

Responsibilities:
- Verify analysis request coordination.
- Verify analysis result forwarding.
- Verify integration with the Sequence model.

Does NOT perform:
- Biological analysis implementation
- GUI testing
- Sequence validation
- File parsing
"""

import pytest

from src.analysis.analysis_service import AnalysisService
from src.core.sequence import Sequence


@pytest.fixture
def service():
    return AnalysisService()


@pytest.fixture
def sequence():
    return Sequence("Test", "ATGC")


# ==========================================================
# Statistics
# ==========================================================

def test_get_sequence_length(service, sequence):
    assert service.get_sequence_length(sequence) == 4


def test_get_gc_content(service, sequence):
    assert service.get_gc_content(sequence) == pytest.approx(50.0)


def test_get_at_content(service, sequence):
    assert service.get_at_content(sequence) == pytest.approx(50.0)


def test_get_base_counts(service, sequence):
    assert service.get_base_counts(sequence) == {
        "A": 1,
        "T": 1,
        "G": 1,
        "C": 1,
    }


def test_get_molecular_weight(service, sequence):
    assert service.get_molecular_weight(sequence) == pytest.approx(
        1253.8027,
        rel=1e-6,
    )


# ==========================================================
# Sequence Operations
# ==========================================================

def test_get_reverse(service, sequence):
    assert str(service.get_reverse(sequence)) == "CGTA"


def test_get_complement(service, sequence):
    assert str(service.get_complement(sequence)) == "TACG"


def test_get_reverse_complement(service, sequence):
    assert str(service.get_reverse_complement(sequence)) == "GCAT"