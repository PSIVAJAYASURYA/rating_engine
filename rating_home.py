from utils import MODEL_REGISTRY
import pandas as pd

def calculate_premium(quote):
    """
    Calculate premium based on base rate, ML multiplier, and sum insured
    Returns: (premium, breakdown dict)
    """
    base_rate = 0.01
    sum_insured = quote['coverages']['dwelling']['sum_insured']
    multiplier = 1.0

    if MODEL_REGISTRY:
        model = list(MODEL_REGISTRY.values())[0]
        X = pd.DataFrame([{
            'age': quote['insured']['age'],
            'building_years': 2026 - quote['coverages']['dwelling']['year_built'],
            'sum_insured': sum_insured
        }])
        ml_mult = model.predict(X)[0]
    else:
        ml_mult = 1.0

    premium = base_rate * sum_insured * ml_mult
    breakdown = {
        'base_rate': base_rate,
        'ml_multiplier': ml_mult,
        'premium': premium
    }
    return premium, breakdown

def underwriting_rule(quote):
    """
    Apply simple underwriting rules.
    Returns a dict with status and reason codes.
    """
    if quote['insured']['age'] < 18:
        return {'status': 'DECLINE', 'reason_codes': ['AGE_UNDER_18']}
    return {'status': 'ACCEPT', 'reason_codes': []}
