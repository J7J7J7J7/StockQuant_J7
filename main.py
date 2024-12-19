# main.py
import tushare as ts
import pandas as pd
from SMA import sma_strategy
from backtest import execute_trades

# 设置Tushare的API Token
ts.set_token('0ea225d0e4ddc08ba18ad98e1353443bbde4a087e401b0013ea40162')

# 获取数据函数
def get_stock_data(stock_code, start_date='20220101', end_date='20231231'):
    pro = ts.pro_api()
    df = pro.daily(ts_code=stock_code, start_date=start_date, end_date=end_date)
    print(df.columns)
    df = df[['trade_date', 'close']]  # 保留日期和收盘价
    df['Close'] = df['close']
    df['Date'] = pd.to_datetime(df['trade_date'])  # 将日期转换为datetime
    df = df[['Date', 'Close']]  # 只保留需要的列
    print(df.columns)
    return df

def main():
    # 获取数据
    stock_code = '000001.SZ'  # 选择股票代码
    df = get_stock_data(stock_code)  # 获取股市数据
    # 执行SMA策略
 
    sma_df = sma_strategy(df)  # 使用正确的变量名 df

    # 执行回测
    trade_history = execute_trades(sma_df)  # 传入SMA策略产生的DataFrame

    # 输出交易结果
    # 输出格式:Date Action Price Size Cash Position Asset
    print(trade_history)

if __name__ == "__main__":
    main()

