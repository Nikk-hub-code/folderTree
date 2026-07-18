from pathlib import Path

from folderTree.config import Config
from folderTree.scanner.ignore import IgnoreEngine


def test_default_ignore():
    engine = IgnoreEngine(Config())

    assert engine.should_ignore(Path(".git"))
    assert engine.should_ignore(Path("__pycache__"))
    assert engine.should_ignore(Path("dist"))
    assert not engine.should_ignore(Path("src"))