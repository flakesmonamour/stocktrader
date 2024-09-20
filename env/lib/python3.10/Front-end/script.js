document.addEventListener('DOMContentLoaded', () => {
    const statusMessage = document.getElementById('status-message');

    // Create Trader
    const traderForm = document.getElementById('trader-form');
    if (traderForm) {
        traderForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const formData = new FormData(event.target);
            const data = Object.fromEntries(formData.entries());

            try {
                const response = await fetch('http://127.0.0.1:5501/create_trader', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data),
                });

                if (response.ok) {
                    const jsonResponse = await response.json();
                    statusMessage.textContent = jsonResponse.message;
                } else {
                    const errorResponse = await response.json();
                    throw new Error(errorResponse.error || 'Error creating trader');
                }
            } catch (error) {
                console.error(error);
                statusMessage.textContent = 'Failed to create trader: ' + error.message;
            }
        });
    } else {
        console.error('Trader form not found');
    }

    // Create Stock
    const stockForm = document.getElementById('stock-form');
    if (stockForm) {
        stockForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const formData = new FormData(event.target);
            const data = Object.fromEntries(formData.entries());

            try {
                const response = await fetch('http://127.0.0.1:5501/create_stock', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data),
                });

                if (response.ok) {
                    const jsonResponse = await response.json();
                    statusMessage.textContent = jsonResponse.message;
                } else {
                    const errorResponse = await response.json();
                    throw new Error(errorResponse.error || 'Error creating stock');
                }
            } catch (error) {
                console.error(error);
                statusMessage.textContent = 'Failed to create stock: ' + error.message;
            }
        });
    } else {
        console.error('Stock form not found');
    }

    // Create Trade
    const tradeForm = document.getElementById('trade-form');
    if (tradeForm) {
        tradeForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const formData = new FormData(event.target);
            const data = Object.fromEntries(formData.entries());

            try {
                const response = await fetch('http://127.0.0.1:5501/create_trade', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data),
                });

                if (response.ok) {
                    const jsonResponse = await response.json();
                    statusMessage.textContent = jsonResponse.message;
                } else {
                    const errorResponse = await response.json();
                    throw new Error(errorResponse.error || 'Error creating trade');
                }
            } catch (error) {
                console.error(error);
                statusMessage.textContent = 'Failed to create trade: ' + error.message;
            }
        });
    } else {
        console.error('Trade form not found');
    }
});
