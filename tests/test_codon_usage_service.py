from src.services.codon_usage_service import CodonUsageService


def test_list_organisms():
    service = CodonUsageService()

    organisms = service.list_organisms()

    assert "Homo sapiens" in organisms
    assert "Mus musculus" in organisms
    assert "Escherichia coli K12 MG1655" in organisms


def test_load_human_dataset():
    service = CodonUsageService()

    df = service.get_dataframe("Homo sapiens")

    assert not df.empty
    assert "Codon" in df.columns


def test_dataframe_cache():
    service = CodonUsageService()

    df1 = service.get_dataframe("Homo sapiens")
    df2 = service.get_dataframe("Homo sapiens")

    # Should return the same cached object
    assert df1 is df2