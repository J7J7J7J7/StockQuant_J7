#dataProcess
import tushare as ts
import pandas as pd

# 获取数据
def get_stock_data(stock_code, start_date='20220101', end_date='20231231'):
    pro = ts.pro_api()
    df = pro.daily(ts_code=stock_code, start_date=start_date, end_date=end_date)
    df = df[['trade_date', 'close']]  # 保留日期和收盘价
    df['Close'] = df['close']
    df['Date'] = pd.to_datetime(df['trade_date'])  # 将日期转换为datetime
    df = df[['Date', 'Close']]  # 只保留需要的列

    #将日期类转换为datetime并排序
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by='Date')
    df['Date'] = df['Date'].dt.strftime('%Y/%m/%d')

    return df