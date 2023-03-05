from tronpy import Tron



def create_wallet():
    client = Tron()
    wallet = client.generate_address()
    print("Wallet address:  %s" % wallet['base58check_address'])
    print("Private Key:  %s" % wallet['private_key'])
