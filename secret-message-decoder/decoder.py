import pandas as pd
import requests
from bs4 import BeautifulSoup


def fetch_table_from_doc(url):
    # fetch the GoogleDoc content
    response = requests.get(url)
    content = response.content.decode("utf-8")

    # parse GoogleDoc content with BeautifulSoup library
    soup = BeautifulSoup(content, "html.parser")

    # locate table
    tables = soup.find_all("table")
    if not tables:
        print("No tables found in the document.")
        return None

    # extract the first table
    table_html = str(tables[0])

    # read table using pandas library
    df = pd.read_html(table_html)[0]
    return df


def parse_table_to_grid(df):
    grid_data = []
    for index, row in df.iterrows():
        try:
            x_coord = int(row[0])
            char = str(row[1]).strip()
            y_coord = int(row[2])
            grid_data.append((x_coord, y_coord, char))
        except ValueError as e:
            print(f"skipping invalid row {index}: {row}")

    return grid_data


def print_grid(grid_data):
    if not grid_data:
        print("Grid data is empty. Nothing to display.")
        return

    max_x = max([x for x, y, c in grid_data])
    max_y = max([y for x, y, c in grid_data])

    grid = [[" " for _ in range(max_y + 1)] for _ in range(max_x + 1)]

    for x, y, char in grid_data:
        grid[x][y] = char

    for row in grid:
        print("".join(row))


def display_secret_message(url):
    df = fetch_table_from_doc(url)
    if df is not None:
        grid_data = parse_table_to_grid(df)
        print_grid(grid_data)
    else:
        print("No valid data to display.")


display_secret_message(
    "https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub"
)
