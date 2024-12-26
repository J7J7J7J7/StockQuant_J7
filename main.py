# main.py
import tushare as ts
import pandas as pd
from backtest import execute_trades
import config
import dataProcess
from plot import plot_trading_data

#策略文件
from Strategy.Strategy_SMA import SMA_Strategy
from Strategy.Strategy_BollingerBands import BollingerBands_Strategy

tushare_Token = config.get_tushare_Token() #tushare的API Token
# 设置Tushare的API Token
ts.set_token(tushare_Token)


def main():
    # 获取数据
    stock_code = config.get_stock_code()  # 选择股票代码
    start_date = config.get_start_date() # 起始回测日期
    end_date = config.get_end_date() # 结束回测日期
    sma_short = config.get_sma_short() # 短期平均线指标
    sma_long = config.get_sma_long() # 长期平均线指标
    window = config.get_window() # 窗口时期
    strategy = config.get_strategy() # 选择交易策略


    df = dataProcess.get_stock_data(stock_code, start_date, end_date)  # 获取股市数据

    #进行交易策略的判断
    if strategy == 'Strategy_SMA':
        # 执行SMA策略
        strategy_df = SMA_Strategy(df)  
    
    elif strategy == 'Strategy_BollingerBands':
        # 执行BollingerBands策略
        strategy_df = BollingerBands_Strategy(df)

    # 执行回测
    output_file = f"backtest_{stock_code}_{start_date}_{end_date}_{strategy}.csv"
    trade_history = execute_trades(strategy_df, output_file = output_file)  # 传入SMA策略产生的DataFrame

    #调用plot生成回测图表
    plot_trading_data(trade_history)

    # 输出交易结果
    # 输出格式:Date Action Price Size Cash Position Asset
    print(f"Backtest completed. Results saved to {output_file}")

if __name__ == "__main__":
    main()

