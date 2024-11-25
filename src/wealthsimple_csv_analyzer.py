import pandas as pd
import matplotlib.pyplot as plt
import glob

def load_csv(file_paths):
    """
    Loads and combines CSV file(s) into a single DataFrame.
    
    Parameters:
    file_paths (list or str): List of paths to the CSV files, or a file pattern (e.g., 'statements/*.csv').
    
    Returns:
    pd.DataFrame: Combined DataFrame containing data from all CSV files.
    """
    # If file_paths is a string pattern (e.g., 'statements/*.csv'), use glob to get file paths
    if isinstance(file_paths, str):
        file_paths = glob.glob(file_paths)
    
    # Load all CSV files and concatenate into a single DataFrame
    all_data = []
    for file in file_paths:
        df = pd.read_csv(file)
        all_data.append(df)
    
    # Combine all DataFrames into one
    combined_df = pd.concat(all_data, ignore_index=True)
    
    return combined_df


def calculate_net_gain_loss(file_paths):
    """
    Calculates the net gain or loss from multiple CSV files based on the 'amount' column.
    
    Parameters:
    file_paths (list or str): List of paths to the CSV files, or a file pattern (e.g., 'statements/*.csv').
    
    Returns:
    float: The net gain or loss.
    """
    # Load all files into a single DataFrame
    combined_df = load_csv(file_paths)
    
    # Calculate the net gain/loss by summing the 'amount' column
    net_gain_loss = combined_df['amount'].sum()
    
    return float(net_gain_loss)


def balance_graphing(file_path):
    """
    Graphs the account balance over time from a CSV file.
    
    Parameters:
    file_path (str): Path to the CSV file.
    """
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Convert the 'date' column to datetime for proper plotting
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Drop rows with invalid dates
    df = df.dropna(subset=['date'])

    # Sort by date to ensure proper chronological plotting
    df = df.sort_values(by='date')

    # Plot the balance over time
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['balance'], marker='o', linestyle='-', color='b', label='Account Balance')

    # Adding labels and title
    plt.title('Account Balance Over Time', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Balance (CAD)', fontsize=12)
    plt.grid(True)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def amount_graphing(file_path):
    """
    Graphs the transaction amounts over time from a CSV file.
    
    Parameters:
    file_path (str): Path to the CSV file.
    """
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Convert the 'date' column to datetime for proper plotting
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Drop rows with invalid dates
    df = df.dropna(subset=['date'])

    # Sort by date to ensure proper chronological plotting
    df = df.sort_values(by='date')

    # Plot the transaction amounts over time with conditional coloring
    colors = ['red' if amount < 0 else 'black' for amount in df['amount']]

    plt.figure(figsize=(10, 6))
    plt.bar(df['date'], df['amount'], color=colors, label='Transaction Amounts')

    # Adding labels and title
    plt.title('Transaction Amounts Over Time', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Amount (CAD)', fontsize=12)
    plt.grid(True, axis='y')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Examples, subject to change
def main():
    monthly_statements = ['monthly-statement-transactions-HQ4BPK105CAD-2024-09-01.csv', 'monthly-statement-transactions-HQ4BPK105CAD-2024-10-01.csv']
    net = calculate_net_gain_loss(monthly_statements )
    print(f"Net Gain/Loss: {net}")

    balance_graphing('monthly-statement-transactions-HQ4BPK105CAD-2024-09-01.csv')
    amount_graphing('monthly-statement-transactions-HQ4BPK105CAD-2024-09-01.csv')

if __name__ == "__main__":
    main()
