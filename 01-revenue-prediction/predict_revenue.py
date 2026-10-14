"""Predict the revenue of property listings with a stacked LightGBM + XGBoost model.

Usage:
    python predict_revenue.py --train train.json --test test.json --out predicted.zip
"""
import argparse
import json
import logging
import zipfile

import numpy as np
import pandas as pd
from lightgbm import LGBMRegressor
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import StackingRegressor
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, RobustScaler
from sklearn.svm import SVR
from xgboost import XGBRegressor

LABEL = "revenue"
NUM_FEATURES = ["lat", "lon", "rooms", "bathrooms", "beds", "min_nights",
                "num_reviews", "rating", "guests"]
CAT_FEATURES = ["room_type", "listing_type", "cancellation"]


def build_pipeline():
    numeric_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", RobustScaler()),
    ])
    categorical_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
        ("encoder", OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1)),
    ])
    preprocessor = ColumnTransformer([
        ("num", numeric_transformer, NUM_FEATURES),
        ("cat", categorical_transformer, CAT_FEATURES),
    ])

    lgb = LGBMRegressor(
        learning_rate=0.02,
        n_estimators=2000,
        max_depth=5,
        colsample_bytree=0.6,
        subsample=0.8,
        random_state=42,
        n_jobs=-1,
    )
    xgb = XGBRegressor(
        learning_rate=0.02,
        n_estimators=1500,
        max_depth=5,
        colsample_bytree=0.7,
        subsample=0.7,
        random_state=42,
        n_jobs=-1,
    )

    # The SVR meta-model sees the base predictions plus the preprocessed features
    stacked_svr = StackingRegressor(
        estimators=[("lgb", lgb), ("xgb", xgb)],
        final_estimator=SVR(C=8, epsilon=0.06),
        passthrough=True,
        n_jobs=-1,
    )

    return Pipeline([
        ("preprocess", preprocessor),
        ("model", stacked_svr),
    ])


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--train", default="train.json")
    parser.add_argument("--test", default="test.json")
    parser.add_argument("--out", default="predicted.zip")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

    logging.info("Loading data")
    train = pd.read_json(args.train)
    test = pd.read_json(args.test)

    X = train[NUM_FEATURES + CAT_FEATURES]
    y = np.log1p(train[LABEL])  # revenue is right-skewed, so the model is fit on log(1 + revenue)

    logging.info("Training on the full training data")
    pipeline = build_pipeline()
    pipeline.fit(X, y)

    logging.info("Predicting on the test data")
    test[LABEL] = np.expm1(pipeline.predict(test[NUM_FEATURES + CAT_FEATURES]))
    predicted = test[[LABEL]].to_dict(orient="records")

    logging.info("Saving predictions to %s", args.out)
    with zipfile.ZipFile(args.out, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.writestr("predicted.json", json.dumps(predicted, indent=2))


if __name__ == "__main__":
    main()
