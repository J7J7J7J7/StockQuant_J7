#Strategy_BollingerBands.py

import pandas as pd
import numpy as np


def BollingerBands_Strategy(df, window = 20):
    # 计算布林带
    df['Middle_Band'] = df['Close'].rolling(window=window).mean()  # 计算中轨
    df['Std_Dev'] = df['Close'].rolling(window=window).std()  # 计算标准差

    # 计算上轨和下轨
    df['Upper_Band'] = df['Middle_Band'] + (2 * df['Std_Dev'])  # 上轨
    df['Lower_Band'] = df['Middle_Band'] - (2 * df['Std_Dev'])  # 下轨

    # 生成买入信号（价格突破下轨）和卖出信号（价格突破上轨）
    # 生成Signal列，买入信号为1，卖出信号为-1，其它为0
    df['Signal'] = np.where(df['Close'] < df['Lower_Band'], 1, np.where(df['Close'] > df['Upper_Band'], -1, 0))

    #仓位默认为0.5
    df.loc[:, 'Signal_Position'] = 0.5
    
    #返回参数
    return df[['Date', 'Close', 'Signal', 'Signal_Position']]