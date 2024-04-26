import pandas as pd 
import numpy as np
class finance:
    def __init__(self) -> None:
        self.companyName = ['聯電','陽明','南僑','長榮','台灣大']
    def __dataRead(self):
        """
        檔案來源
        data -> 聯電
        data1 -> 陽明
        data2 -> 南僑
        data3 -> 長榮
        data4 -> 台灣大
        """
        data = pd.read_csv("./data.csv"); 
        data1 = pd.read_csv("./data1.csv"); 
        data2 = pd.read_csv("./data2.csv"); 
        data3 = pd.read_csv("./data3.csv"); 
        data4 = pd.read_csv("./data4.csv");
        all_data = [data,data1,data2,data3,data4]
        all_buy = [] ; all_percent = []
        self.data=all_data ; self.allBuy = all_buy ; self.allPercent = all_percent

    def __buyStock(self):
        """計算題目要求前的前置作業"""
        for i in self.data:
            price = i[i['年月']=="2020/1/1"]['最高價(元)'].values[0]
            quantity = 1
            self.allBuy.append(price*quantity)
        # 算比重
        for i in self.allBuy:
            self.allPercent.append(round(i/sum(self.allBuy),4))
        print("五家公司各購買一張的價格及比重如下");print("-"*50)
        for i in range(0,5):
            print(f"{self.companyName[i]}價格：{self.allBuy[i]}")
            print(f"{self.companyName[i]}比重：{self.allPercent[i]}")
            print("-"*50)

    def __getStockAllPrice(self):
        """得取所有股票每月收盤價"""
        self.all_buy = [[],[],[],[],[]] ; index = 0
        for i in self.data:
            self.all_buy[index].extend(i['收盤價(元)'].values.tolist()[1:])
            index += 1
        print(self.all_buy)
        return self.all_buy

    def calculate(self):
        """計算題目要求"""
        # 假設我用最高價在 2020/1 在五家公司各購買1張
        self.__dataRead() ; self.__buyStock();
        stock_prices = self.__getStockAllPrice();
        # 將五隻股票每個月的收盤價組合成一個列表
        portfolio_values = np.array(stock_prices)

        # 計算每個月底的投資組合報酬率
        monthly_returns = self.__calculate_monthly_returns(portfolio_values)

        # 計算每個月底的投資組合風險
        monthly_risk = self.__calculate_monthly_risk(monthly_returns)

        # 輸出結果
        print("每個月底的投資組合報酬率：", monthly_returns)
        print("每個月底的投資組合風險（標準差）：", monthly_risk)
        

    def __calculate_monthly_returns(self,portfolio_values):
        """
        計算每個月底的投資組合報酬率
        """
        total_portfolio_values = np.sum(portfolio_values, axis=0)
        monthly_returns = []
        for i in range(1, len(total_portfolio_values)):
            returns = (total_portfolio_values[i] - total_portfolio_values[i-1]) / total_portfolio_values[i-1]
            monthly_returns.append(returns)
        return monthly_returns

    def __calculate_monthly_risk(self,monthly_returns):
        """
        計算每個月底的投資組合風險（標準差）
        """
        monthly_risks = np.std(monthly_returns)
        print(monthly_risks)
        return monthly_risks


if __name__== "__main__":
    finance().calculate()