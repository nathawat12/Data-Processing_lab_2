# OOP Data Processing Lab

## Lab Overview

This lab changes data-processing code from a procedural style to Object-Oriented Programming (OOP).
We use classes to load CSV data, filter rows, calculate values, store tables, and join two tables using a common column.

- **Commit 3:** Create the `Table` class with `filter()` and `aggregate()`.
- **Commit 4:** Add the `DB` class and `Table.join()` to combine city and country data.

## Project Structure

```text
oop_data_processing_lab/
├── README.md                   # Project information and instructions
├── Cities.csv                  # City, country, location and temperature data
├── Countries.csv               # Country, population, EU and coastline data
├── commit3_data_processing.py  # Completed Commit 3 starter code
├── data_processing.py          # Completed Commit 4 starter code (final version)
└── test_data_processing.py     # Optional local checks
```

## Design Overview

### DataLoader

- `base_path`: Folder where the CSV files are stored.
- `load_csv(filename)`: Reads a CSV file using `csv.DictReader()` and returns a list of dictionaries. Each dictionary is one row.

### Table

- `table_name`: The name of the table.
- `table`: A list of dictionaries that holds the data.
- `__init__(table_name, table)`: Creates a new table object.
- `filter(condition)`: Returns a new table containing rows that satisfy the condition.
- `aggregate(operation, column)`: Collects the values in a column, converts numeric values from strings to floats, and applies a function such as average, minimum, maximum, or count.
- `join(other_table, key)`: Returns a new table combining two tables where their values under the shared key match. In this lab, the key is `country`.
- `__str__()`: Shows a table's name and data when printed. (Commit 4)

### DB (Commit 4)

- `tables`: A list of `Table` objects in the database.
- `insert(table)`: Adds a table to the list.
- `search(table_name)`: Finds a table by name; returns `None` if no table is found.

## How to Test and Run

1. Install Python 3 on your computer.
2. Open this project folder in VS Code.
3. Open Terminal in VS Code.
4. To run Commit 3:

   ```bash
   python3 commit3_data_processing.py
   ```

5. To run Commit 4:

   ```bash
   python3 data_processing.py
   ```

6. For optional local checks:

   ```bash
   python3 -m unittest -v test_data_processing.py
   ```

No extra Python packages are required.

The Commit 4 script should show the following values among its results:
- Average temperature for Italian cities: about `13.4747`
- Number of countries with coastline: `29`
- Minimum / maximum temperature for cities in EU countries without coastlines: `4.54` / `10.34`

## GitHub Submission

The assignment asks for **two commits**. Do the following in your own GitHub repository:

1. First, put `commit3_data_processing.py`, `Cities.csv` and this `README.md` into the repository and commit with a message such as `Complete Commit 3 OOP Table class`.
2. Next, add `data_processing.py`, `Countries.csv`, the updated `README.md`, and the optional tests. Commit with a message such as `Complete Commit 4 database and join`.
3. Push your commits to GitHub and submit **the repository link** in Google Classroom.

**Note:** Your instructor's Commit 3 and Commit 4 starter scripts both use the name `data_processing.py`. We keep the Commit 3 version as `commit3_data_processing.py` here so that you can inspect and run both versions side by side. In your own commit history, you can instead use `data_processing.py` for Commit 3 and update the same file in Commit 4, as the assignment intends.

## Data Sources

CSV files use the same European city/country data shown in the lab examples. Datasets were copied from public data published in the `vikasgupta1812/datasets` GitHub repository, consistent with the Stanford CS102 example dataset.

- https://raw.githubusercontent.com/vikasgupta1812/datasets/master/Cities.csv
- https://raw.githubusercontent.com/vikasgupta1812/datasets/master/Countries.csv

Instructor starter code:
- Commit 3: https://gist.github.com/parujr/acdbe501e3a327d6297c46ee726c0242
- Commit 4: https://gist.github.com/parujr/fce6082cce20fdf11f4e21e753e1cd0a
