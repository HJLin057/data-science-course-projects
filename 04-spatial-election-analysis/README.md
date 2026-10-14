# Spatial Analysis of the 2023 Dutch Election

Share of votes for one party (VVD) in 342 Dutch municipalities in the 2023 general election, together with
average income, average house price and population density.

## Method

1. Distributions: all four variables are skewed and fail the Shapiro-Wilk normality test, so they are log-transformed.
2. Choropleth map of the vote share with 5 quantile classes.
3. **Global Moran's I** with rook, queen and k-nearest-neighbour weights, k = 3, 5, 7.
4. **Local Moran's I** to map significant hotspots and coldspots.
5. **Linear regression vs. spatial lag model** (GM_Lag in `spreg`), compared by mean squared error.
6. **Random forest, bagging and SVR**, with the spatial lag of the vote share as a feature. Train/test split by
   province, so no province is in both sets, and 5-fold grid search for the hyperparameters.
7. **Province-wise cross-validation** with the best model and a map of the prediction error per municipality.

All variables are merged into the municipality GeoDataFrame first, so the rows always line up with the spatial weights.

## Results

- Global Moran's I is 0.42 to 0.47, highest with 3 nearest neighbours: municipalities with a similar vote share
  cluster together.
- Adding the spatial lag lowers the mean squared error from 0.0332 for linear regression to 0.0293 for the spatial lag model.
- On provinces not seen in training, SVR is the most accurate of the three regressors:

| Model | Test MSE (log vote share) |
|---|---|
| SVR | **0.0196** |
| Random forest | 0.0217 |
| Bagging | 0.0230 |

- In province-wise cross-validation the median absolute error is 0.11 on the log scale; the map shows where
  the model does worst.

## Files

- `spatial_election_analysis.ipynb`: the analysis with its outputs

## Run

```bash
pip install -r requirements.txt
```

The election data and the municipality boundaries ("Wijk- en buurtkaart 2023" by CBS) are not included in this repository.
