import sqlite3
import tempfile
from pathlib import Path

from ai_file_search import check_exact_path, mock_parse, score, search_names


def make_conn():
    conn = sqlite3.connect(":memory:")
    conn.execute(
        """
        CREATE TABLE files (
            name TEXT,
            name_lower TEXT,
            path TEXT,
            is_dir INTEGER,
            ext TEXT,
            size INTEGER,
            mtime REAL
        )
        """
    )
    return conn


def test_score_prefers_exact_name():
    assert score("resume", "resume") >= 1.0


def test_score_handles_typo_tolerance():
    assert score("resume", "resumee") > 0.7
    assert score("resumee", "resume") > 0.7


def test_mock_parse_extracts_keywords_and_extension():
    plan = mock_parse("find my python resume pdf file")
    assert "resume" in plan["keywords"]
    assert ".pdf" in plan["extensions"]
    assert plan["type"] == "any"


def test_search_names_returns_relevant_results():
    conn = make_conn()
    rows = [
        ("resume.pdf", "resume.pdf", "/tmp/resume.pdf", 0, ".pdf", 1024, 1710000000.0),
        ("portfolio.docx", "portfolio.docx", "/tmp/portfolio.docx", 0, ".docx", 2048, 1710000100.0),
        ("Project Notes.txt", "project notes.txt", "/tmp/project notes.txt", 0, ".txt", 512, 1710000200.0),
    ]
    conn.executemany("INSERT INTO files VALUES (?,?,?,?,?,?,?)", rows)
    conn.commit()

    results = search_names(conn, "resume", kind="file", min_score=0.4, limit=10)
    assert results
    assert results[0][1][0] == "resume.pdf"


def test_check_exact_path_accepts_real_file_paths():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / "demo.txt"
        file_path.write_text("hello world", encoding="utf-8")

        assert check_exact_path(str(file_path)) is True
