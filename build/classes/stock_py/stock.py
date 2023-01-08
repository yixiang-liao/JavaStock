import twstock
import matplotlib.pyplot as plt
import csv

def TWstock(stock_id):
    # get該股資料
    stock = twstock.Stock(stock_id)
    
    # 總成交股數
    capacity = stock.capacity[-1]
    # 總成交金額
    turnover = stock.turnover[-1]
    # 開盤價
    open = stock.open[-1]
    # 最高價
    high = stock.high[-1]
    # 最低價
    low = stock.low[-1]
    # 收盤價
    price = stock.price[-1]
    # 漲跌價差
    change = stock.change[-1]
    # 成交筆數
    transaction = stock.transaction[-1]
    
    # 該股當前資料寫入list
    stock_data = [capacity , turnover , open , high , low , price , change , transaction]

    return stock_data

def stock_csv(list):
    # 開啟輸出的 CSV 檔案
    with open('TWstock.csv', 'w', newline='') as csvFile:
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvFile)

        # 1.直接寫出-標題
        writer.writerow(['capacity','turnover','open','high','low','price','change','transaction'])

        # 1.直接寫出-資料
        writer.writerow(list)

def stock_figure(stock_id):
    stockID=twstock.Stock(stock_id)
    stocklist=stockID.fetch_31()
    high_ID=[]
    low_ID=[]
    close_ID=[]
    listy=[]
    for i in stocklist:
        high_ID.append(i.high)
        low_ID.append(i.low)
        close_ID.append(i.close)
        listy.append(i.date.strftime('%m-%d'))

    plt.figure(figsize=[16,9])
    plt.plot(listy,high_ID,'r-.*',lw=2,ms=10,label='High')
    plt.plot(listy,low_ID,'g-.p',lw=2,ms=10,label='low')
    plt.plot(listy,close_ID,'y-.o',lw=2,ms=10,label='close')
    plt.legend(fontsize=16)
    # plt.ylim(300,600)
    title = f'{stock_id} Trend'
    plt.title(title , fontsize=28)
    plt.xlabel('Date',fontsize=20)
    plt.ylabel('Price',fontsize=20)
    plt.grid(color='k',ls=':',lw=1,alpha=0.5)
    plt.savefig("stock.png")
    # plt.show() 

def implement(id):
    stock_csv(TWstock(id))
    stock_figure(id)

implement('2330')