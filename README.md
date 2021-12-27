# adventofcode
https://adventofcode.com/

## Requirements
This project requires [Python 3.10](https://docs.python.org/3/whatsnew/3.10.html) as well as [Poetry](https://python-poetry.org/).

## Setup
```bash
poetry install
```

## Usage
### Generate skeletons
```bash
poetry run skeleton 2021 1
```

### Solve puzzles
```bash
poetry run solve 2021 1
```

```bash
year=2021
for day in {1..25}
do
    poetry run solve $year $day
done
```

### Time puzzles
```bash
poetry run timeit 2021 1
```

```bash
year=2021
for day in {1..25}
do
    poetry run timeit $year $day
done
```