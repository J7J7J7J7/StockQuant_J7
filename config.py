#config.py

#在下面修改你自己的数据！

stock_code = '000001.SZ'  # 选择股票代码
start_date = '20220101' # 起始回测日期
end_date = '20231231' # 结束回测日期
tushare_Token = 'your tushare Token' #tushare的API Token
strategy = 'Strategy_BollingerBands' #交易策略 选择策略的文件名

#Strategy_SMA
sma_short = '3' # 短期平均线指标
sma_long = '8' # 长期平均线指标

#Strategy_BollingerBands
window = '20' #窗口计算期


def get_stock_code():
    return stock_code

def get_start_date():
    return start_date

def get_end_date():
    return end_date

def get_sma_short():
    return sma_short

def get_sma_long():
    return sma_long

def get_tushare_Token():
    return tushare_Token

def get_strategy():
    return strategy

def get_window():
    return window