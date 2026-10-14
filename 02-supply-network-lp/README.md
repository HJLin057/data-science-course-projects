# Minimum-Cost Food Supply Network

A linear program that plans how to buy food and ship it to camps at the lowest total cost while every camp
gets enough nutrition. Part of a team project; this notebook contains the data preparation and the
linear program, which were my part.

## Model

- **Network:** suppliers → ports (sea transport) → warehouses → camps (land transport)
- **Decision variables:** tons per month on every arc, for each of 14 commodities
- **Objective:** procurement + sea transport + land transport + handling at ports and warehouses
- **Constraints:**
  - capacity of every supplier, port and warehouse
  - flow balance: what enters a supplier, port or warehouse also leaves it
  - nutrition: each camp receives its 30-day requirement of 11 nutrients

## Results

- Total cost about **$36.05M** per month, of which procurement is $22.55M, about 62%.
- Checks in the notebook: flow in equals flow out at the port of Djibouti, the corn soya blend delivered equals
  the amount bought, and all 11 nutrient requirements are met for the SOMALI camp.
- The default solver reports the status `optimal_inaccurate`; the checks confirm that the solution is feasible.

## Files

- `supply_network_lp.ipynb`: data preparation, model, solution and checks, with the outputs of the original run

## Run

```bash
pip install -r requirements.txt
```

The data file is not included in this repository.
