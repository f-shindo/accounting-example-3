from web3 import Web3
from decimal import Decimal
import settings

ETH = settings.ETH
POL = settings.POL
GNO = settings.GNO
SDN = settings.SDN


def tx_get(address, chain):
    # rpcを設定
    if chain == 'Ethereum':
        w3 = Web3(Web3.HTTPProvider(ETH))
    elif chain == 'Polygon':
        w3 = Web3(Web3.HTTPProvider(POL))
    elif chain == 'Gnosis':
        w3 = Web3(Web3.HTTPProvider(GNO))
    elif chain == 'Shiden':
        w3 = Web3(Web3.HTTPProvider(SDN))
    else:
        print('error')

    # トランザクションを取得
    txn = w3.eth.get_transaction_count(address)

    return txn
