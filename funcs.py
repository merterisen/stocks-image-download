import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf


def stocks_image_save(stocks:list, start, end, interval='1h', candle_number=20, image_path='images'):

    """
    # Valid intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
    """

    for stock in stocks:

        df = yf.download(stock, start=start, end=end, interval=interval)
        
        count = 0

        for i in range(int((len(df)) / candle_number)):
            
            fig, ax = plt.subplots(figsize=(5,5))
            mpf.plot(df.iloc[count:count+candle_number], ax=ax, type='candle', style='charles')

            plt.axis('off')
            plt.savefig('{}/{}{}.png'.format(image_path, stock, i))
            
            count += candle_number
            fig.visible = False
            plt.close(fig)