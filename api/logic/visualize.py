import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def logic_visualize_transaction(verified, unverified):

    right = datetime.today()
    left = datetime.today() - timedelta(days=30)

    fig = plt.figure()
    
    _v = [(v['tx_date'], v['price']) for v in verified]
    _u = [(u['tx_date'], u['price']) for u in unverified]

    print(_v, _u)
    
    plt.savefig('resources/price.png')
    plt.savefig('resources/price.svg')