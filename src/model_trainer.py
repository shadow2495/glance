from sklearn.ensemble import IsolationForest
import pickle

def train_anomaly_model(X_train):
    model = IsolationForest(contamination=0.02, n_estimators=200, random_state=42)
    model.fit(X_train)
    with open('models/trained_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    return model
