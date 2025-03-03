import csv
import os

# Function to read exchange rates from a CSV file
def read_exchange_rates(filename):
    exchange_rates = {}
    currency_labels = {}

    try:
        with open(filename, 'r', encoding='utf-8-sig', errors='replace') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip the first row (header)

            for row in reader:
                if len(row) < 3:  # Ensure the row contains enough data
                    continue
                
                currency_code = row[0].strip().upper()  # Extract currency code (e.g., USD)
                currency_name = row[1].strip()  # Extract currency full name

                try:
                    exchange_rate = float(row[2])  # Convert exchange rate to float
                    exchange_rates[currency_code] = exchange_rate
                    currency_labels[currency_code] = currency_name  # Store full name
                except ValueError:
                    print(f"Skipping invalid exchange rate for {currency_code}: {row[2]}")  # Handle conversion error

    except FileNotFoundError:
        print("Error: The file 'currency.csv' was not found.")
        exit()

    return exchange_rates, currency_labels

# Function to perform currency conversion
def convert_currency(amount, target_currency, exchange_rates):
    return amount * exchange_rates.get(target_currency, None)

# Main program execution
def main():
    filename = "currency.csv"
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, filename)

    exchange_rates, currency_labels = read_exchange_rates(file_path)

    if not exchange_rates:
        print("No exchange rates available.")
        return

    try:
        usd_amount = float(input("How much dollar do you have? "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    target_currency = input("What currency do you want to have? ").strip().upper()

    if target_currency in exchange_rates:
        converted_amount = convert_currency(usd_amount, target_currency, exchange_rates)
        currency_name = currency_labels.get(target_currency, target_currency)  # Get full name if available
        
        print(f"\nDollar: {usd_amount} USD")
        print(f"{currency_name}: {converted_amount:.2f}")  # Display with 2 decimal places
    else:
        print("Currency not found in exchange rates.")

if __name__ == "__main__":
    main()