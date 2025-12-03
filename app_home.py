from flask import Flask, request, jsonify
from utils import load_models
from rating_home import calculate_premium, underwriting_rule
import uuid

# Initialize Flask app and load ML models
app = Flask(__name__)
load_models()

# In-memory stores for demonstration (replace with DB in production)
quotes_store = {}
policies_store = {}
claims_store = {}

@app.route('/v1/quote', methods=['POST'])
def quote():
    """
    Accepts a JSON quote request and returns premium and decision.
    """
    data = request.json
    premium, breakdown = calculate_premium(data)
    decision = underwriting_rule(data)
    quote_id = str(uuid.uuid4())

    response = {
        'quote_id': quote_id,
        'premium': premium,
        'breakdown': breakdown,
        'decision': decision
    }
    quotes_store[quote_id] = response
    return jsonify(response)

@app.route('/v1/policy/bind', methods=['POST'])
def bind_policy():
    """
    Bind a policy from an existing quote.
    """
    data = request.json
    quote_id = data.get('quote_id')
    if quote_id not in quotes_store:
        return jsonify({'error': 'invalid quote_id'}), 400

    policy_id = str(uuid.uuid4())
    policies_store[policy_id] = {
        'quote_id': quote_id,
        'status': 'ACTIVE'
    }
    return jsonify({'policy_id': policy_id, 'status': 'ACTIVE'})

@app.route('/v1/claim', methods=['POST'])
def create_claim():
    """
    Create a claim against an existing policy.
    """
    data = request.json
    policy_id = data.get('policy_id')
    if policy_id not in policies_store:
        return jsonify({'error': 'invalid policy_id'}), 400

    claim_id = str(uuid.uuid4())
    claims_store[claim_id] = {
        'policy_id': policy_id,
        'amount': data.get('amount', 0),
        'status': 'OPEN'
    }
    return jsonify({'claim_id': claim_id, 'status': 'OPEN'})

@app.route('/v1/policy/<policy_id>', methods=['GET'])
def get_policy(policy_id):
    """
    Retrieve policy details by policy_id.
    """
    if policy_id not in policies_store:
        return jsonify({'error': 'invalid policy_id'}), 400
    return jsonify(policies_store[policy_id])

@app.route('/v1/claim/<claim_id>', methods=['GET'])
def get_claim(claim_id):
    """
    Retrieve claim details by claim_id.
    """
    if claim_id not in claims_store:
        return jsonify({'error': 'invalid claim_id'}), 400
    return jsonify(claims_store[claim_id])

@app.route('/v1/models', methods=['GET'])
def get_models():
    """
    List all loaded ML models.
    """
    from utils import MODEL_REGISTRY
    return jsonify(list(MODEL_REGISTRY.keys()))

if __name__ == '__main__':
    app.run(debug=True)
