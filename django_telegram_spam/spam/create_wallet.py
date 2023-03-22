from tronpy import Tron
from tronpy.exceptions import AddressNotFound



def create_wallet():
    client = Tron()
    wallet = client.generate_address()
    print("Wallet address:  %s" % wallet['base58check_address'])
    print("Private Key:  %s" % wallet['private_key'])
    print("Private Key:  %s" % wallet['hex_address'])
    print("Private Key:  %s" % wallet['public_key'])
    base58check_address = wallet['base58check_address']
    private_key = wallet['private_key']
    hex_address = wallet['hex_address']
    public_key = wallet['public_key']
    return base58check_address,private_key,hex_address,public_key


def check_balance(address):
    try:
        client = Tron()
        wallet = client.generate_address()
        balance=client.get_account_balance(address)
        return balance
    except AddressNotFound:
        print('Adress not found..!')
        return False
        #return 'Adress not found..!'


