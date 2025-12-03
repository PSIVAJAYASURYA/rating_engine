# utils.py
import os
import joblib

# Global dictionary to hold loaded ML models
MODEL_REGISTRY = {}

def load_models():
    """
    Load all .joblib ML models from the 'models/' directory into MODEL_REGISTRY.
    Keys are the filenames without extension.
    """
    models_dir = 'models'
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)

    for filename in os.listdir(models_dir):
        if filename.endswith('.joblib'):
            model_name = os.path.splitext(filename)[0]
            MODEL_REGISTRY[model_name] = joblib.load(os.path.join(models_dir, filename))
            print(f"Loaded model: {model_name}")
