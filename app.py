from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Initialize FastAPI
app = FastAPI()

# Define input data schema
class InputData(BaseModel):
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

    def Encode(self):
        endcoded_data = []

        # encode atrr
        endcoded_data.append(self.SeniorCitizen)
        endcoded_data.append(encoder["Partner"].transform([self.Partner])[0])
        endcoded_data.append(encoder["Dependents"].transform([self.Dependents])[0])
        endcoded_data.append(self.tenure)
        endcoded_data.append(encoder["OnlineSecurity"].transform([self.OnlineSecurity])[0])
        endcoded_data.append(encoder["OnlineBackup"].transform([self.OnlineBackup])[0])
        endcoded_data.append(encoder["DeviceProtection"].transform([self.DeviceProtection])[0])
        endcoded_data.append(encoder["TechSupport"].transform([self.TechSupport])[0])
        endcoded_data.append(encoder["Contract"].transform([self.Contract])[0])
        endcoded_data.append(encoder["PaperlessBilling"].transform([self.PaperlessBilling])[0])
        endcoded_data.append(encoder["PaymentMethod"].transform([self.PaymentMethod])[0])
        endcoded_data.append(self.MonthlyCharges)
        endcoded_data.append(self.TotalCharges)

        return np.array([endcoded_data])
    

encoder = joblib.load('label_encoder.joblib')
model = joblib.load('Random-Forest.joblib')

# Define model prediction endpoint
@app.post("/predict")
async def predict(data: InputData):
    prediction  = model.predict(data.Encode())
    if prediction[0] == 0:
        response = 'Not Churn'
    else:
        response = 'Churn'

    return {"prediction": response}
