# Forecasting Daily Patient Arrivals at an Emergency Department

Daily arrivals at an emergency department from 1 January 2014, forecast 7 and 30 days ahead.

## Method

1. Autocorrelation and partial autocorrelation of the series.
2. STL decomposition into trend, seasonal and residual parts with periods of 7, 30 and 365 days.
   The 365-day period leaves residuals that look like random noise, so it is preferred.
3. Three forecasting methods:
   - **Exponential smoothing** with additive trend and multiplicative weekly seasonality
   - **ARIMA**: all 125 combinations of p, d, q from 0 to 4 are tried; the order with the lowest MAPE on a
     validation window is refit on the training and validation data
   - **KNN regression** on the 5 previous days, with the number of neighbours chosen by grid search with
     time-ordered cross-validation
4. Accuracy on the last 7 or 30 days, measured by the mean absolute percentage error (MAPE).

## Results

| Method | MAPE, 7 days | MAPE, 30 days |
|---|---|---|
| Exponential smoothing | **4.7%** | **10.3%** |
| ARIMA (4,1,4) and (2,1,3) | 7.1% | 11.3% |
| KNN regression | 7.6% | 12.7% |

Exponential smoothing is the most accurate on both horizons. Each horizon is tested on one window only,
so the ranking is indicative.

## Files

- `ed_arrivals_forecasting.ipynb`: the analysis, with the outputs of the original run

## Run

```bash
pip install -r requirements.txt
```

The data file is not included in this repository.

The function that builds the lagged features for KNN is adapted from course material. The pandas
conversion in the KNN plot was debugged with help from ChatGPT.
