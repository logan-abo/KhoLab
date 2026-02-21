import importlib


def test_import_and_version():
    kholab = importlib.import_module("kholab")
    assert hasattr(kholab, "__version__")
