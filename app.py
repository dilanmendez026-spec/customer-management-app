from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.db'
db = SQLAlchemy(app)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'email': self.email}

@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([customer.to_dict() for customer in customers]), 200

@app.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    customer = Customer.query.get(id)
    if customer:
        return jsonify(customer.to_dict()), 200
    return jsonify({'message': 'Customer not found'}), 404

@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.json
    new_customer = Customer(name=data['name'], email=data['email'])
    db.session.add(new_customer)
    db.session.commit()
    return jsonify(new_customer.to_dict()), 201

@app.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    data = request.json
    customer = Customer.query.get(id)
    if customer:
        customer.name = data['name']
        customer.email = data['email']
        db.session.commit()
        return jsonify(customer.to_dict()), 200
    return jsonify({'message': 'Customer not found'}), 404

@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get(id)
    if customer:
        db.session.delete(customer)
        db.session.commit()
        return jsonify({'message': 'Customer deleted'}), 200
    return jsonify({'message': 'Customer not found'}), 404

@app.route('/customers/search', methods=['GET'])
def search_customers():
    query = request.args.get('query')
    customers = Customer.query.filter(Customer.name.contains(query)).all()
    return jsonify([customer.to_dict() for customer in customers]), 200

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)