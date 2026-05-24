from pathlib import Path


def test_index_html_exists():
    index_file = Path("site/index.html")
    assert index_file.exists(), "O arquivo site/index.html deve existir."


def test_index_html_has_expected_text():
    content = Path("site/index.html").read_text(encoding="utf-8")
    assert "Meu primeiro deploy automatizado" in content
    assert "GitHub Actions" in content
    assert "GitHub Pages" in content