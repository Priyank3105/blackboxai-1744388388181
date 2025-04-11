from flask import Flask, jsonify, request
from models import db, Goods, UsageRecords, CreditRecords

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)

@app.route('/goods', methods=['POST'])
def add_goods():
    # Logic to add goods
    pass

@app.route('/usage', methods=['POST'])
def record_usage():
    # Logic to record usage
    pass

@app.route('/credit', methods=['POST'])
def record_credit():
    # Logic to record credit
    pass

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
