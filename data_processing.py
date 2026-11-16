

import csv
from pathlib import Path


class DataLoader:
    """Load a CSV file into a list of dictionaries."""

    def __init__(self, base_path=None):
        if base_path is None:
            self.base_path = Path(__file__).parent.resolve()
        else:
            self.base_path = Path(base_path)

    def load_csv(self, filename):
        filepath = self.base_path / filename
        data = []

        with filepath.open(encoding="utf-8", newline="") as f:
            rows = csv.DictReader(f)
            for row in rows:
                data.append(dict(row))

        return data


class DB:
    """A simple database that keeps a list of Table objects."""

    def __init__(self):
        self.tables = []

    def insert(self, table):
        """Add a table to the database."""
        self.tables.append(table)

    def search(self, table_name):
        """Find a table by name. Return None when it does not exist."""
        for table in self.tables:
            if table.table_name == table_name:
                return table
        return None


class Table:
    """Store rows and support filter, aggregate and join."""

    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def filter(self, condition):
        """Return a new Table containing only matching rows."""
        filtered_rows = []
        for row in self.table:
            if condition(row):
                filtered_rows.append(row)
        return Table(self.table_name + "_filtered", filtered_rows)

    def aggregate(self, operation, column):
        """Apply an operation to a column, converting numbers from CSV."""
        values = []
        for row in self.table:
            values.append(row[column])

        try:
            numbers = [float(value) for value in values]
            return operation(numbers)
        except ValueError:
            return operation(values)

    def join(self, other_table, key):
        """Combine rows from two tables when they have the same key value."""
        joined_rows = []
        for row1 in self.table:
            for row2 in other_table.table:
                if row1[key] == row2[key]:
                    new_row = row1.copy()
                    new_row.update(row2)
                    joined_rows.append(new_row)

        new_name = self.table_name + "_" + other_table.table_name + "_joined"
        return Table(new_name, joined_rows)

    def __str__(self):
        return self.table_name + ":" + str(self.table)


if __name__ == "__main__":
    loader = DataLoader()
    cities = loader.load_csv("Cities.csv")
    table1 = Table("cities", cities)
    countries = loader.load_csv("Countries.csv")
    table2 = Table("countries", countries)

    my_DB = DB()
    my_DB.insert(table1)
    my_DB.insert(table2)

    my_table1 = my_DB.search("cities")
    print("List all cities in Italy:")
    my_table1_filtered = my_table1.filter(lambda x: x["country"] == "Italy")
    print(my_table1_filtered)
    print()

    print("Average temperature for all cities in Italy:")
    print(my_table1_filtered.aggregate(lambda x: sum(x) / len(x), "temperature"))
    print()

    my_table2 = my_DB.search("countries")
    print("List all non-EU countries:")
    my_table2_filtered = my_table2.filter(lambda x: x["EU"] == "no")
    print(my_table2_filtered)
    print()

    print("Number of countries that have coastline:")
    print(
        my_table2.filter(lambda x: x["coastline"] == "yes")
        .aggregate(lambda x: len(x), "coastline")
    )
    print()

    my_table3 = my_table1.join(my_table2, "country")
    print("First 5 entries of the joined table (cities and countries):")
    for item in my_table3.table[:5]:
        print(item)
    print()

    print("Cities whose temperatures are below 5.0 in non-EU countries:")
    my_table3_filtered = my_table3.filter(lambda x: x["EU"] == "no").filter(
        lambda x: float(x["temperature"]) < 5.0
    )
    print(my_table3_filtered.table)
    print()

    print("The min and max temperatures for cities in EU countries that do not have coastlines")
    my_table3_filtered = my_table3.filter(lambda x: x["EU"] == "yes").filter(
        lambda x: x["coastline"] == "no"
    )
    print("Min temp:", my_table3_filtered.aggregate(lambda x: min(x), "temperature"))
    print("Max temp:", my_table3_filtered.aggregate(lambda x: max(x), "temperature"))
    print()
