from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os

# 1. Initialize FastAPI
app = FastAPI(
    title="Intelligent Network Monitor API",
    description="AI-powered system for detecting network intrusions",
    version="1.0.0"
)

# 2. Load the Model and Encoders (The Brain and the Translator)
# We use absolute paths to ensure it works from any terminal location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'random_forest_brain.pkl')
ENCODER_PATH = os.path.join(BASE_DIR, 'models', 'encoders_dictionary.pkl')

try:
    model = joblib.load(MODEL_PATH)
    encoders = joblib.load(ENCODER_PATH)
    print("✅ AI Brain and Translators loaded successfully!")
except Exception as e:
    print(f"❌ Error loading models: {e}")

# 3. Define the Input Data Schema
class TrafficData(BaseModel):
    # This structure matches the 41 features of NSL-KDD
    # Index 1: protocol_type, 2: service, 3: flag
    features: list

# 4. The Prediction Endpoint
@app.post("/predict")
async def predict_traffic(traffic: TrafficData):
    try:
        data = traffic.features.copy()
        
        # Real-time Translation (Inference Pipeline)
        # Convert text like 'tcp' to the number the AI understands
        data[1] = encoders['protocol_type'].transform([data[1]])[0]
        data[2] = encoders['service'].transform([data[2]])[0]
        data[3] = encoders['flag'].transform([data[3]])[0]

        # Get Prediction
        prediction = model.predict([data])
        
        # Map the result back to human language
        result = "Normal ✅" if prediction[0] == 1 else "Attack ❌"
        status = "safe" if prediction[0] == 1 else "danger"

        return {
            "status": status,
            "prediction": result,
            "threat_level": "Low" if prediction[0] == 1 else "High"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid data format: {str(e)}")

@app.get("/")
def home():
    return {"message": "Welcome to Intelligent Network Monitor API. Use /docs for testing."}