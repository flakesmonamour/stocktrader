import click
from sqlalchemy.orm import sessionmaker
from models.connection import engine, init_db
from models.trader import Trader
from models.stock import Stock
from models.trade import Trade

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@click.group()
def cli():
    """Stock Trade Tracker CLI"""
    pass

@cli.command()
def init_db_command():
    """Initialize the database"""
    init_db()
    click.echo("Database initialized!")

@cli.command()
@click.argument('name')
def create_trader(name):
    """Create a new trader"""
    session = SessionLocal()
    trader = Trader.create(session, name)
    click.echo(f"Trader created: {trader}")
    session.close()

@cli.command()
@click.argument('symbol')
@click.argument('name')
def create_stock(symbol, name):
    """Create a new stock"""
    session = SessionLocal()
    stock = Stock.create(session, symbol, name)
    click.echo(f"Stock created: {stock}")
    session.close()

@cli.command()
@click.argument('trader_id', type=int)
@click.argument('stock_id', type=int)
@click.argument('amount', type=float)
@click.argument('price', type=float)
def create_trade(trader_id, stock_id, amount, price):
    """Create a new trade"""
    session = SessionLocal()
    trade = Trade.create(session, trader_id, stock_id, amount, price)
    click.echo(f"Trade created: {trade}")
    session.close()

@cli.command()
def list_traders():
    """List all traders"""
    session = SessionLocal()
    traders = Trader.get_all(session)
    for trader in traders:
        click.echo(trader)
    session.close()

@cli.command()
def list_stocks():
    """List all stocks"""
    session = SessionLocal()
    stocks = Stock.get_all(session)
    for stock in stocks:
        click.echo(stock)
    session.close()

@cli.command()
def list_trades():
    """List all trades"""
    session = SessionLocal()
    trades = Trade.get_all(session)
    for trade in trades:
        click.echo(trade)
    session.close()

@cli.command()
@click.argument('trader_id', type=int)
def delete_trader(trader_id):
    """Delete a trader by ID"""
    session = SessionLocal()
    trader = session.query(Trader).get(trader_id)
    if trader:
        session.delete(trader)
        session.commit()
        click.echo(f"Trader with ID {trader_id} deleted.")
    else:
        click.echo(f"Trader with ID {trader_id} not found.")
    session.close()

@cli.command()
@click.argument('stock_id', type=int)
def delete_stock(stock_id):
    """Delete a stock by ID"""
    session = SessionLocal()
    stock = session.query(Stock).get(stock_id)
    if stock:
        session.delete(stock)
        session.commit()
        click.echo(f"Stock with ID {stock_id} deleted.")
    else:
        click.echo(f"Stock with ID {stock_id} not found.")
    session.close()

@cli.command()
@click.argument('trade_id', type=int)
def delete_trade(trade_id):
    """Delete a trade by ID"""
    session = SessionLocal()
    trade = session.query(Trade).get(trade_id)
    if trade:
        session.delete(trade)
        session.commit()
        click.echo(f"Trade with ID {trade_id} deleted.")
    else:
        click.echo(f"Trade with ID {trade_id} not found.")
    session.close()
    
@cli.command()
def delete_all_traders():
    """Delete all traders"""
    session = SessionLocal()
    traders = Trader.get_all(session)
    
    for trader in traders:
        session.delete(trader)
    
    session.commit()
    click.echo("All traders deleted!")
    session.close()
@cli.command()
def delete_all_stocks():
    """Delete all stocks"""
    session = SessionLocal()
    stocks = Stock.get_all(session)
    
    for stock in stocks:
        session.delete(stock)
    
    session.commit()
    click.echo("All stocks deleted!")
    session.close()

@cli.command()
def delete_all_trades():
    """Delete all trades"""
    session = SessionLocal()
    trades = Trade.get_all(session)
    
    for trade in trades:
        session.delete(trade)
    
    session.commit()
    click.echo("All trades deleted!")
    session.close()

@cli.command()
@click.argument('trade_id', type=int)
@click.argument('trader_id', type=int)
@click.argument('stock_id', type=int)
@click.argument('amount', type=float)
@click.argument('price', type=float)
def update_trade(trade_id, trader_id, stock_id, amount, price):
    """Update a trade"""
    session = SessionLocal()
    try:
        trade = session.query(Trade).get(trade_id)
        if trade:
            trade.trader_id = trader_id
            trade.stock_id = stock_id
            trade.amount = amount
            trade.price = price
            session.commit()
            click.echo(f"Trade updated: {trade}")
        else:
            click.echo(f"No trade found with id {trade_id}")
    finally:
        session.close()

@cli.command()
@click.argument('stock_id', type=int)
@click.argument('symbol')
@click.argument('name')
def update_stock(stock_id, symbol, name):
    """Update an existing stock's symbol and name"""
    session = SessionLocal()
    stock = session.query(Stock).filter(Stock.id == stock_id).first()
    
    if stock:
        stock.symbol = symbol
        stock.name = name
        session.commit()
        click.echo(f"Stock updated: {stock}")
    else:
        click.echo("Stock not found.")
    
    session.close()

@cli.command()
@click.argument('trader_id', type=int)
@click.argument('name')
def update_trader(trader_id, name):
    """Update a trader's name"""
    session = SessionLocal()
    try:
        trader = session.query(Trader).get(trader_id)
        if trader:
            trader.name = name
            session.commit()
            click.echo(f"Trader updated: {trader}")
        else:
            click.echo(f"No trader found with id {trader_id}")
    finally:
        session.close()


if __name__ == "__main__":
    cli()
