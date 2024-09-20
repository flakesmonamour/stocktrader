from flask import Flask, jsonify, request
from flask_cors import CORS
from models.connection import SessionLocal, init_db
from models.trader import Trader
from models.stock import Stock
from models.trade import Trade

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins for development
init_db()

@app.route('/traders', methods=['GET'])
def get_traders():
    session = SessionLocal()
    try:
        traders = Trader.get_all(session)
        return jsonify([{'id': t.id, 'name': t.name} for t in traders])
    except Exception as e:
        app.logger.error(f"Error retrieving traders: {e}", exc_info=True)
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

@app.route('/stocks', methods=['GET'])
def get_stocks():
    session = SessionLocal()
    try:
        stocks = Stock.get_all(session)
        return jsonify([{'id': s.id, 'symbol': s.symbol, 'name': s.name} for s in stocks])
    except Exception as e:
        app.logger.error(f"Error retrieving stocks: {e}", exc_info=True)
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

@app.route('/trades', methods=['GET'])
def get_trades():
    session = SessionLocal()
    try:
        trades = Trade.get_all(session)
        return jsonify([
            {
                'id': t.id,
                'trader_id': t.trader_id,
                'stock_id': t.stock_id,
                'amount': t.amount,
                'price': t.price
            }
            for t in trades
        ])
    except Exception as e:
        app.logger.error(f"Error retrieving trades: {e}", exc_info=True)
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

@app.route('/create_trader', methods=['POST'])
def create_trader():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({"error": "Name is required"}), 400
    
    session = SessionLocal()
    try:
        trader = Trader.create(session, data['name'])
        return jsonify({"message": "Trader created successfully", "id": trader.id}), 201
    except Exception as e:
        app.logger.error(f"Error creating trader: {e}", exc_info=True)
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

@app.route('/create_stock', methods=['POST'])
def create_stock():
    data = request.get_json()
    if not data or 'symbol' not in data or 'name' not in data:
        return jsonify({"error": "Symbol and name are required"}), 400

    session = SessionLocal()
    try:
        stock = Stock.create(session, data['symbol'], data['name'])
        return jsonify({"message": "Stock created successfully", "id": stock.id}), 201
    except Exception as e:
        app.logger.error(f"Error creating stock: {e}", exc_info=True)
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

@app.route('/create_trade', methods=['POST'])
def create_trade():
    data = request.get_json()
    
    if 'trader_id' not in data or 'stock_id' not in data or 'amount' not in data or 'price' not in data:
        return jsonify({"error": "Trader ID, Stock ID, Amount, and Price are required"}), 400

    session = SessionLocal()
    try:
        trade = Trade.create(session, data['trader_id'], data['stock_id'], data['amount'], data['price'])
        return jsonify({"message": "Trade created successfully", "id": trade.id}), 201
    except Exception as e:
        app.logger.error(f"Error creating trade: {e}", exc_info=True)
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

if __name__ == '__main__':
    app.run(debug=True, port=5501)
