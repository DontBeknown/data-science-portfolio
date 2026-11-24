# Rozene Mokem | Data Science Portfolio

Python notebooks adapted from Computer Engineering coursework at KMUTT. The notebooks include saved results and charts for review on GitHub.

| Project | What it shows |
| --- | --- |
| [Sales Simulation and Order Volume](sales-simulation/) | Monte Carlo inventory comparison and order-volume reporting from an Excel workbook |
| [Advertising Spend and Sales Volume](sales-volume-regression/) | Linear regression, residual checks, and interpretation of model fit |
| [Los Angeles Crime Trends](los-angeles-crime-trends/) | Data validation, weekly KPI aggregation, and visual reporting |
| [Telecom Customer Retention](telecom-customer-retention/) | Kaplan–Meier retention analysis across payment methods |

## Run locally

Use Python 3.12. Run these commands from the repository root on Windows PowerShell.

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python fetch_data.py
.\.venv\Scripts\python run_notebooks.py
```

On macOS or Linux, use `.venv/bin/python` in the last three commands. The download script caches source files in `data/`. The runner executes all notebooks and saves their outputs. To run one notebook, pass its path to `run_notebooks.py`. You can also open the notebooks in VS Code and select the virtual environment as the kernel.
