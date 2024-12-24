import matplotlib.pyplot as plt
import pandas as pd

def plot_trading_data(result_df):
    """
    根据提供的 DataFrame 绘制价格和资产的图表。
    
    Parameters:
        result_df (pd.DataFrame): 包含交易数据的 DataFrame，应该包含 'Date', 'Price', 'Action', 'Asset' 等列
    """
    # 创建一个包含主表和子表的图形
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

    # 主表：绘制价格（Price）和买卖信号
    ax1.plot(result_df['Date'], result_df['Price'], label='Price', color='b', marker='o')
    buy_signals = result_df[result_df['Action'] == 'Buy']
    ax1.scatter(buy_signals['Date'], buy_signals['Price'] - 2, marker='^', color='r', label='Buy Signal', s=100)  # 买入箭头在价格下方
    sell_signals = result_df[result_df['Action'] == 'Sell']
    ax1.scatter(sell_signals['Date'], sell_signals['Price'] + 2, marker='v', color='b', label='Sell Signal', s=100)  # 卖出箭头在价格上方

    ax1.set_title('Price with Buy/Sell Signals', fontsize=16)
    ax1.set_ylabel('Price')
    ax1.legend()
    ax1.grid(True)

    # 子表：绘制资产变化
    ax2.plot(result_df['Date'], result_df['Asset'], label='Asset', color='g', marker='s')

    ax2.set_title('Asset Over Time', fontsize=16)
    ax2.set_ylabel('Asset Value')
    ax2.legend()
    ax2.grid(True)

    # 设置共享的 x 轴（日期）
    ax2.set_xlabel('Date')
    plt.xticks(rotation=45)

    # 自动调整布局
    plt.tight_layout()
    plt.show()
