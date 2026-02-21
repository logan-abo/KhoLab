# KhoLab

KhoLab — prototype in Python, later ported to Julia.

Quickstart (Python prototype)

- Create a virtual environment and activate it.

Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -U pip
pip install -r requirements-dev.txt
```

macOS / Linux:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements-dev.txt
```

- Run tests:

```bash
pytest
```

- Run CLI:

```bash
python -m kholab --version
```

Project structure

- `src/kholab/`: Python package for the prototype.
- `tests/`: pytest tests.
- `julia/`: placeholder for later Julia rewrite.

Next steps

- Initialize Git and push to a remote (optional).
- Add more package modules, docs, and examples.
