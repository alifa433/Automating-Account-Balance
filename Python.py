import tronapi

# Replace these values with your specific configuration
full_node_url = 'https://api.trongrid.io'  # Your full node URL
private_key = 'YOUR_HOT_WALLET_PRIVATE_KEY'  # Private key of your hot wallet
user_accounts = ['USER_ACCOUNT_1', 'USER_ACCOUNT_2']  # List of user accounts to consolidate

# Initialize Tron API
tron = tronapi.Tron(full_node=full_node_url)

# Connect to your hot wallet using its private key
hot_wallet = tron.private_key_to_address(private_key)

# Calculate total balance to consolidate
total_balance = 0
for user_account in user_accounts:
    balance = tron.trx.get_balance(user_account)
    total_balance += balance

# Prepare the transaction
transaction = {
    'to_address': hot_wallet,
    'owner_address': user_accounts[0],  # You can choose any user account to initiate the transaction
    'amount': total_balance,
    'private_key': private_key,
}

# Send the consolidation transaction
response = tron.trx.send_transaction(**transaction)

# Check the transaction result
if 'result' in response and response['result']:
    print(f"Consolidation successful. Transaction ID: {response['txid']}")
else:
    print("Consolidation failed. Check for errors.")

# Release resources if needed
# tron.trx.unfreeze_balance(user_account, resource='BANDWIDTH', owner_address=hot_wallet)
