#backtest.py

import pandas as pd

'''
Date 日期
Close 收盘价（目前以收盘价作为买入价，以后考虑更新为更加贴合实际的买入价）
Signal 交易信号（1为买入 -1为卖出 0表示不进行新的交易操作）
Signal_Position 仓位 对买入信号：当前剩余现金的比例 对卖出信号：当前持仓市值的比例
'''

def execute_trades(df, commission=0.001, Cash = 100000, Position = 0, output_file="backtest_result.csv"):
    """
    执行回测交易，根据策略的买入卖出信号进行交易。
    注：目前本策略只适用于单只股票交易的情景！！

    参数:
    df (pd.DataFrame): 包含日期、收盘价、交易信号和交易仓位。
    commission (float): 每笔交易的佣金比例，默认为0.1%。
    Cash：初始的现金 100000元
    Position: 初始的仓位 0股
    
    返回:
    pd.DataFrame: 包含每次交易后的资金变化。
    """
    cash = Cash
    position = Position
    trade_history = []
    trade_history.append(['Date','Action','Price','Quantity','Cash','Position','Asset'])  
    # 用于记录每次交易的信息
    '''
    Date 日期
    Action 交易行为（Buy或Sell）
    Price 交易价格 执行交易操作的价格
    Quantity 数量 执行交易的数量（单位：股）
    Cash 当前账户中的现金
    Position 当前账户中的股票持仓数量
    Asset 账户总资产=现金+股票总市值
    '''

    # 遍历每一行数据
    for _, row in df.iterrows():

        signal = row['Signal']  # 策略信号（1为买入，-1为卖出）

        #当交易信号为0时 直接进入下一行数据
        if signal == 0 :
            continue

        price = row['Close']
        signal_position = row['Signal_Position']

        if signal == 1 :  # 买入
            buy_quantity = int( cash * signal_position / price) # 买入的股数量 int
            buy_quantity = buy_quantity // 100 * 100 # 将买入的数量转化为手的倍数，即100股作为最小tick
            trade_cash = (price + commission) * buy_quantity # 用于交易的现金(包含手续费)
            position = position + buy_quantity # 增加对应的持仓数量
            cash = cash - trade_cash # 减少对应的现金
            asset = cash + (position * price)
            trade_history.append([row['Date'], 'Buy', price, buy_quantity, cash, position, asset])

        elif signal == -1 :  # 卖出
            # 卖出所有持仓

            sell_quantity = int( position * signal_position) # 卖出的股数量 int
            sell_quantity = sell_quantity // 100 * 100 # 将卖出的数量转化为手的倍数，即100股作为最小tick
            trade_cash = (price + commission) * sell_quantity # 用于交易的现金(包含手续费)
            position = position - sell_quantity # 减少对应的持仓数量
            cash = cash + trade_cash # 增加对应的现金
            asset = cash + (position * price)
            trade_history.append([row['Date'], 'Sell', price, sell_quantity, cash, position, asset])


    result_df = pd.DataFrame(trade_history[1:], columns = trade_history[0])

    result_df.to_csv(output_file, index = False)
    print(f"Backtest results saved to {output_file}")

    # 将交易记录转换为DataFrame并返回
    return result_df