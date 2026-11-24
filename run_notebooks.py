"""Execute portfolio notebooks and save their rendered outputs."""

from pathlib import Path
import sys

import nbformat
from nbclient import NotebookClient


ROOT = Path(__file__).resolve().parent


def main():
    notebooks = (
        [Path(name).resolve(strict=True) for name in sys.argv[1:]]
        if len(sys.argv) > 1
        else sorted(ROOT.glob("*/*.ipynb"))
    )
    if not notebooks:
        raise SystemExit("No notebooks found.")
    for path in notebooks:
        notebook = nbformat.read(path, as_version=4)
        nbformat.validate(notebook)
        NotebookClient(notebook, timeout=120, kernel_name="python3").execute(cwd=path.parent)
        temporary = path.with_suffix(".ipynb.tmp")
        nbformat.write(notebook, temporary)
        temporary.replace(path)
        print(f"Executed {path.relative_to(ROOT) if path.is_relative_to(ROOT) else path}", flush=True)


if __name__ == "__main__":
    main()
