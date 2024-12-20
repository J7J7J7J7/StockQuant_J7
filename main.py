# main.py
import tushare as ts
import pandas as pd
from SMA import sma_strategy
from backtest import execute_trades
import config

tushare_Token = config.get_tushare_Token() #tushare的API Token
# 设置Tushare的API Token
ts.set_token(tushare_Token)

# 获取数据函数
def get_stock_data(stock_code, start_date='20220101', end_date='20231231'):
    pro = ts.pro_api()
    df = pro.daily(ts_code=stock_code, start_date=start_date, end_date=end_date)
    df = df[['trade_date', 'close']]  # 保留日期和收盘价
    df['Close'] = df['close']
    df['Date'] = pd.to_datetime(df['trade_date'])  # 将日期转换为datetime
    df = df[['Date', 'Close']]  # 只保留需要的列
    return df

def main():
    # 获取数据
    stock_code = config.get_stock_code()  # 选择股票代码
    start_date = config.get_start_date() # 起始回测日期
    end_date = config.get_end_date() # 结束回测日期
    sma_short = config.get_sma_short() # 短期平均线指标
    sma_long = config.get_sma_long() # 长期平均线指标
    df = get_stock_data(stock_code, start_date, end_date)  # 获取股市数据

    #将日期类转换为datetime并排序
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by='Date')
    df['Date'] = df['Date'].dt.strftime('%Y/%m/%d')

    # 执行SMA策略
 
    sma_df = sma_strategy(df)  # 使用正确的变量名 df

    # 执行回测
    output_file = f"backtest_{stock_code}_{start_date}_{end_date}.csv"
    trade_history = execute_trades(sma_df, output_file = output_file)  # 传入SMA策略产生的DataFrame

    # 输出交易结果
    # 输出格式:Date Action Price Size Cash Position Asset
    print(f"Backtest completed. Results saved to {output_file}")

if __name__ == "__main__":
    main()

