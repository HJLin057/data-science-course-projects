# Data Science Course Projects

Projects from my MSc in Data Science, cleaned up for reading on GitHub. Each folder has its own README with
the method, the results and how to run it. Two were team projects; their folders contain my part only.

| Project | What it does | Result | Main tools |
|---|---|---|---|
| [01 Revenue prediction](01-revenue-prediction) | Predicts the revenue of property listings with a stacked LightGBM + XGBoost model | Ranked 12th of 135 participants | scikit-learn, LightGBM, XGBoost |
| [02 Supply network optimisation](02-supply-network-lp) | Linear program for the cheapest food supply network that meets nutrition requirements (team project, my part) | Lowest-cost plan of about $36.05M per month | cvxpy, pandas |
| [03 Emergency department forecasting](03-ed-arrivals-forecasting) | Forecasts daily patient arrivals with exponential smoothing, ARIMA and KNN | Test MAPE 4.7% for 7 days with exponential smoothing | sktime, statsmodels, scikit-learn |
| [04 Spatial election analysis](04-spatial-election-analysis) | Spatial autocorrelation and spatial regression of the 2023 Dutch election results | Moran's I up to 0.47; best test MSE 0.0196 with SVR | GeoPandas, PySAL, scikit-learn |
| [05 Image processing](05-image-processing) | Gaussian blur in the spatial and frequency domain, colour segmentation, retinal vessel segmentation | Dice score 0.77 for retinal vessels | scikit-image, SciPy |
| [06 Stereotype classification](06-gender-bias-nlp) | Fine-tunes multilingual DistilBERT on LLM-generated Dutch sentences (group project, my part) | Test F1 0.778, rising to 0.806 after extra pre-training | Hugging Face Transformers, PyTorch |

Datasets are not included. Each README says where the data comes from.

My MSc thesis on deepfake face detection is in a separate repository:
[Master_Thesis_DSS](https://github.com/HJLin057/Master_Thesis_DSS)
