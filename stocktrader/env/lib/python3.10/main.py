from models.trader import Trader
from models.connection import get_session  # Now it should import correctly

def main():
    session = next(get_session())  # Use next to get the session from the generator
    # Example usage
    trader = Trader.create(session, "John Doe")
    print(trader)

    # Fetching all traders
    all_traders = Trader.get_all(session)
    print("All Traders:", all_traders)

if __name__ == "__main__":
    main()
