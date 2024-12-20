import pytest
from typer.testing import CliRunner
from rf_visuals.cli import app

runner = CliRunner()


def test_s2p_file():
    # Create a mock S2P file and test reading from disk
    data = """# Hz S RI R 50
1.0e9 0.707 0.707 0.5 0.5
"""
    with runner.isolated_filesystem():
        with open("test.s2p", "w") as f:
            f.write(data)

        result = runner.invoke(app, ["s2p", "test.s2p"])
        assert result.exit_code == 0
        assert "Loaded S2P file: test.s2p" in result.output
        # You can also add asserts to check for parsed network data info
        # For example, checking if the network parameters are printed as expected.


def test_s2p_stdin():
    # Test reading S2P data from stdin
    data = """# Hz S RI R 50
1.0e9 0.707 0.707 0.5 0.5
"""
    result = runner.invoke(app, ["s2p"], input=data)
    assert result.exit_code == 0
    assert "Loaded S2P file: from stdin" in result.output


def test_s1p_file():
    # Similar test for S1P files
    data = """# Hz S RI R 50
1.0e9 0.5 0.5
"""
    with runner.isolated_filesystem():
        with open("test.s1p", "w") as f:
            f.write(data)

        result = runner.invoke(app, ["s1p", "test.s1p"])
        assert result.exit_code == 0
        assert "Loaded S1P file: test.s1p" in result.output


def test_s1p_stdin():
    # Test reading S1P data from stdin
    data = """# Hz S RI R 50
1.0e9 0.5 0.5
"""
    result = runner.invoke(app, ["s1p"], input=data)
    assert result.exit_code == 0
    assert "Loaded S1P file: from stdin" in result.output
