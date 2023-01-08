import twstock
import requests

def line_notify(stock_id):
    stock = twstock.Stock(stock_id)
    token = "0Jd7r1iFnhlHQphuJYNW8faeBel1Rts4PmvMMqQHwKo"
    message = ""
    message += f'今日{stock_id}股票資訊：'
    message += f'\n\t總成交股數(單位:股):{stock.capacity[-1]}'
    message += f'\n\t總成交金額(單位:元):{stock.turnover[-1]}'
    message += f'\n\t開盤價:{stock.open[-1]}'
    message += f'\n\t最高價:{stock.high[-1]}'
    message += f'\n\t最低價:{stock.low[-1]}'
    message += f'\n\t收盤價:{stock.price[-1]}'
    message += f'\n\t漲跌價差:{stock.change[-1]}'
    message += f'\n\t成交筆數:{stock.transaction[-1]}'

    # line notify所需資料
    line_url = "https://notify-api.line.me/api/notify"
    line_header = {
        "Authorization": 'Bearer ' + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    line_data = {
        "message": message
    }

    x = requests.post(url=line_url, headers=line_header, data=line_data)
    print(x.status_code)