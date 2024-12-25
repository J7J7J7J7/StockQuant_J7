#SMA.py

import pandas as pd
import numpy as np

def SMA_Strategy(df, short_window=3, long_window=8):
    """
    简单移动平均线策略：3日SMA和8日SMA策略
    参数：
    df (pd.DataFrame): 包含日期和收盘价的DataFrame。
    short_window (int): 短期SMA窗口，默认为3。
    long_window (int): 长期SMA窗口，默认为8。
    
    返回：
    pd.DataFrame: 包含每次交易后的资金、持仓情况、交易信号等数据。
    """
    # 计算SMA
    df['SMA_short'] = df['Close'].rolling(window=short_window).mean()  # 3日SMA
    df['SMA_long'] = df['Close'].rolling(window=long_window).mean()  # 8日SMA

    # 初始化信号列
    df.loc[:, 'Signal'] = 0

    # 检查短期SMA是否穿越长期SMA
    # 向上穿越（短期SMA从下穿越上）时生成买入信号
    # 向下穿越（短期SMA从上穿越下）时生成卖出信号
    df['Signal'] = np.where(df['SMA_short'] > df['SMA_long'], 1, -1)

    # 计算SMA的交叉信号，生成买入或卖出信号
    df['Cross'] = df['Signal'].diff()  # 计算信号变化，只有变化时才有交易动作
    
    # 向上穿越时生成买入信号（Signal从-1变为1），向下穿越时生成卖出信号（Signal从1变为-1）
    df['Signal'] = np.where(df['Cross'] == 2, 1, np.where(df['Cross'] == -2, -1, 0))

    # 清除前几个NaN值
    df = df.dropna(subset=['SMA_short', 'SMA_long'])
    
    df.loc[:, 'Signal_Position'] = 1

    # 输出策略信号
    return df[['Date', 'Close', 'Signal', 'Signal_Position']]
    #注：这里的交易仓位默认为1了 以后再优化！！