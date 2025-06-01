from helpers import wrangle_backtest

# Step 1: Read the .log file
with open('data/round1.log', 'r') as f:
    log_lines = f.readlines()

# Step 2: Parse log data into DataFrames
trades_df, activity_logs_df, _ = wrangle_backtest(log_lines)

# Step 3: Save the DataFrames as CSV files
activity_logs_df.to_csv('data/activity_logs.csv', index=False)
trades_df.to_csv('data/trades.csv', index=False)

print("✅ CSV files created successfully!")

