# Revenue Prediction for Property Listings

Predicts the revenue of property listings from their location, size, reviews and booking rules.
Ranked **12th of 135** participants on the hidden test set.

## Features

- **Numeric:** latitude, longitude, rooms, bathrooms, beds, minimum nights, number of reviews, rating, guests
- **Categorical:** room type, listing type, cancellation policy

## Model

1. Median imputation and robust scaling for numeric features; ordinal encoding for categorical features.
2. The target is `log(1 + revenue)`, because revenue is strongly right-skewed. Predictions are transformed back.
3. A stacking ensemble: LightGBM and XGBoost as base models, an SVR as the meta-model. The SVR sees the
   base predictions and the preprocessed features (`passthrough=True`).
4. The final model is trained on all training data.

## Files

- `predict_revenue.py`: training and prediction

## Run

```bash
pip install -r requirements.txt
```

```bash
python predict_revenue.py --train train.json --test test.json --out predicted.zip
```

The data files are not included in this repository.
