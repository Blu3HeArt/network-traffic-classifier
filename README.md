# Network Traffic Classifier

A machine learning project that uses a decision tree to classify synthetic network connections as **normal** or **suspicious**.

The goal is to practice preparing data, training a model, evaluating predictions, and investigating a model's limitations.

## Dataset

The dataset contains 28 invented network connections:

- 14 normal connections
- 14 suspicious connections
- No missing values

Each connection has five input features:

| Feature | Description |
|---|---|
| duration_seconds | Connection duration in seconds |
| bytes_sent | Number of bytes sent |
| bytes_received | Number of bytes received |
| packets_sent | Number of packets sent |
| failed_logins | Number of failed login attempts |

The `label` column contains the category the model learns to predict.

This small, synthetic dataset is for learning. It does not represent the full complexity of real network traffic.

## Tools

- Python
- pandas
- scikit-learn

## How to Run

Keep `netowrk.py` and `network_connections.csv` in the same project folder.

From that folder, create and activate a virtual environment in Linux or WSL:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required packages:

```bash
python -m pip install pandas scikit-learn
```

Run the script:

```bash
python netowrk.py
```

## Model and Training

The project uses a `DecisionTreeClassifier` with:

- `max_depth=3`
- `random_state=42`

The data is split into:

- 21 training examples
- 7 testing examples

The split uses `test_size=0.25`, `random_state=42`, and `stratify=y` to keep the categories approximately balanced.

The model trains only on the training set.

## Results

The model correctly classified all seven held-out test examples, giving a test accuracy of **100%**.

Confusion matrix:

| Actual category | Predicted normal | Predicted suspicious |
|---|---:|---:|
| Normal | 4 | 0 |
| Suspicious | 0 | 3 |

These results describe performance on this particular small test set. They do not establish real-world reliability.

## Learned Decision Rules

The trained tree follows these rules:

1. If bytes received are 3,850 or fewer, predict suspicious.
2. Otherwise, if bytes sent exceed 606,000, predict suspicious.
3. Otherwise, if failed logins exceed 3, predict suspicious.
4. Otherwise, predict normal.

These thresholds came from the training examples. They are not universal security rules.

## Known Limitation: False Alarm

I tested an additional example defined as a legitimate health check:

| Feature | Value |
|---|---:|
| duration_seconds | 2 |
| bytes_sent | 200 |
| bytes_received | 100 |
| packets_sent | 3 |
| failed_logins | 0 |

The model predicted **suspicious**, making this a **false positive**.

The connection received only 100 bytes, so it matched the tree's first rule. The tree stopped there without considering its zero failed logins.

This example shows that a model can achieve perfect accuracy on a small test set while making mistakes on other legitimate traffic. The training data did not adequately represent legitimate connections like this health check.

## What I Learned

- Loading and inspecting CSV data with pandas.
- Separating input features from target labels.
- Splitting data into training and testing sets.
- Training a decision tree classifier.
- Evaluating accuracy and a confusion matrix.
- Making predictions on new examples.
- Inspecting the rules behind predictions.
- Recognizing why a perfect test score does not guarantee a reliable model.

## Possible Improvements

- Collect more varied, reliably labeled examples.
- Include legitimate low-volume connections.
- Evaluate false alarms and missed threats on a larger independent dataset.
- Compare the decision tree with a simple baseline model.

This project is an educational prototype, not a production intrusion detection system.