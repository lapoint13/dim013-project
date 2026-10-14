# dim013-project

Load and clean sample data from CSV files with pandas.

## Installation

```bash
git clone https://github.com/lapoint13/dim013-project.git
cd dim013-project
python -m venv .venv
source .venv/bin/activate        # Git Bash on Windows: source .venv/Scripts/activate
pip install -r requirements.txt
```

## Usage

```bash
python -m src.load_data data/raw/sample.csv
```

Prints the first rows of the CSV file.

## Project structure

```
dim013-project/
├── data/
│   ├── raw/          # original data, never edited
│   └── processed/    # cleaned data
├── notebooks/        # exploration
├── src/              # source code
└── tests/            # tests
```

## Contributing

Create a branch, commit with Conventional Commits, open a pull request.
