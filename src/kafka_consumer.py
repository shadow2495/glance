from kafka import KafkaConsumer
import json, pickle
from src.data_preprocessor import preprocess_logs

consumer = KafkaConsumer(
    'network_logs',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

with open('models/trained_model.pkl', 'rb') as f:
    model = pickle.load(f)

for msg in consumer:
    df, _ = preprocess_logs(pd.DataFrame([msg.value]))
    anomaly = model.predict(df)
    if anomaly[0] == -1:
        print(f"[ALERT] Suspicious event detected: {msg.value}")
