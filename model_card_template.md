# Model Card
Census Bureau Income Prediction
For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Model Type: Classification model using randomforest
Developed By: bchr174-eng (forked from Udacity).
Date: Created as part of a 2024–2026 course cycle.
Version: 1.0.0. 
## Intended Use
Primary Use Case: Predicting whether an individual's annual income exceeds $50,000 based on census data.
Intended Users: Data scientists and DevOps engineers interested in scalable ML deployment via FastAPI and Docker.
Out-of-Scope: This model should not be used for real-world financial decisions or credit scoring, as it is a training project based on historical data. 
## Training Data
Dataset: UCI Census Income Dataset.
Features: 14 characteristics including age, education, marital status, occupation, and race.
Preprocessing: Standard cleaning involved removing whitespace, handling missing values, and one-hot encoding categorical variables.
## Evaluation Data
Metrics: Evaluated using Precision, Recall, and F1-score.
Slicing: Performance is often analyzed across categorical "slices" (e.g., performance by education level or race) to identify potential biases.
## Metrics
This repository provides concrete evaluation results from the current trained model and slice analysis outputs in `slice_output.txt`.
Performance Overview:

Overall test metrics (from model pipeline test split):

    Precision: 0.74 (approx)
    Recall: 0.66 (approx)
    F1-Score: 0.69 (approx)

Slice performance example (from categorical slicing on test data):

    workclass: Private -> Precision 0.7376, Recall 0.6404, F1 0.6856
    race: White -> Precision 0.7404, Recall 0.6373, F1 0.6850
    sex: Male -> Precision 0.7445, Recall 0.6599, F1 0.6997
## Ethical Considerations
Bias: The dataset contains historical data from 1994, which reflects social and economic biases of that era regarding race, gender, and occupation.
Fairness: Using the "Slicing" method is critical for this project to ensure the model does not disproportionately underperform for specific demographic groups.
Privacy: While the data is anonymized, it represents real demographic patterns that should be handled with care to avoid reinforcing stereotypes.
## Caveats and Recommendations
Data Recency: The data is over 30 years old; income thresholds and demographic correlations have shifted significantly since 1994.
Deployment: This model is designed for a FastAPI environment. Ensure that the Pydantic schemas used for inference match the exact feature names and types used during training (including handling hyphens in feature names like education-num).
Continuous Integration: It is recommended to use GitHub Actions for automated testing and DVC (Data Version Control) to track model and data versions. 