import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from dateutil import parser

def logic_visualize_transaction(verified, unverified):

    sns.set_theme(context='notebook', style='darkgrid')
    sns.set_palette('rainbow')

    fig = plt.figure()
    
    v_prices = [v['price'] for v in reversed(verified)]
    v_dates = [parser.parse(v['tx_date']) for v in reversed(verified)]
    u_prices = [u['price'] for u in reversed(unverified)]
    u_dates = [parser.parse(u['tx_date']) for u in reversed(unverified)]

    plt.plot([dt.strftime('%m-%d-%y') for dt in v_dates], v_prices, label='Verified Transactions')
    plt.plot([dt.strftime('%m-%d-%y') for dt in u_dates], u_prices, label='Unverified Transactions')
    plt.gca().xaxis.set_tick_params(rotation = 60)  
    plt.title('Transactions in the Last Month')
    plt.ylabel('Transaction Prices')
    plt.legend()
    
    fig.set_size_inches((12,8))
    plt.savefig('resources/price.png')
    plt.savefig('resources/price.svg')
    print('saved figures in resources.')