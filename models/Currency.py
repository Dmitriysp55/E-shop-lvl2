import requests
from datetime import datetime
import os
import xml.etree.ElementTree as ET

class Currency:
    def __init__(self, id, code, nominal, rate):
        self.setId(id)
        self.setCode(code)
        self.setNominal(nominal)
        self.setRate(rate)

    def __str__(self):
        title = '--- Currency ---'
        id = f'Id: {self._id}'
        code = f'Code: {self._code}'
        nominal = f'Nominal: {self._nominal}'
        rate = f'Rate: {self._rate}'
        out = f'\n{title}\n{id}\n{code}\n{nominal}\n{rate}\n'
        return out

    def __repr__(self):
        return str(self)

    def setId(self, id):
        if type(id) is not int:
            raise TypeError('Error: value must be integer')
        if id<=0 or id>1000000:
            raise ValueError("Error: value is not valid")
        self._id = id
    def getId(self):
        return self._id

    def setCode(self, code):
        if type(code) is not str:
            raise TypeError('Error: value must be string')
        if len(code) > 3 or len(code) < 3:
            raise ValueError('Error: currency code must have 3 alphabetic code values')
        self._code = code
    def getCode(self):
        return self._code
    
    def setNominal(self, nominal):
        if type(nominal) is not int:
            raise TypeError('Error: value must be integer')
        self._nominal = nominal
    def getNominal(self):
        return self._nominal

    def setRate(self, rate):
        if type(rate) is not float:
            raise TypeError('Error: value must be integer')
        if rate < 0:
            raise ValueError('Error: value can not be less then 0')
        self._rate = rate
    def getRate(self):
        return self._rate

class CurrencyService:
        
    def __getCurrentDate(self):
        today = datetime.date(datetime.now())
        formated_date = today.strftime('%d.%m.%Y')
        return formated_date

    def getCurrencies(self):
        dir_list = os.listdir('data\\currency-rates')
        today = datetime.date(datetime.now())
        path_to_rates = f'data\\currency-rates\\{today}.xml'
        if os.path.exists(path_to_rates) == False:
            ## delete old date rates ##
            for f in dir_list:
                os.remove(f'data\\currency-rates\\{f}')
            ## create today's rate file
            url = requests.get(f'https://www.bnm.md/en/official_exchange_rates?get_xml=1&date={self.__getCurrentDate()}' )
            content = url.content
            with open(path_to_rates, 'wb') as f:
                f.write(content)
        
        ## Read XML
        tree = ET.parse(path_to_rates)
        root = tree.getroot()
        currency_list = []
        for i in range (len(root)):
            # print(root[i].get('ID'), root[i].find('CharCode').text)
            currency_list.append(Currency(
                        int(root[i].get('ID')),
                        root[i].find('CharCode').text,
                        int(root[i].find('Nominal').text),
                        float(root[i].find('Value').text)
                      ))
                      
        return currency_list