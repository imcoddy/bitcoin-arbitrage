# Copyright (C) 2013, Maxime Biais <maxime@biais.org>

from .market import Market, TradeException
import time
import base64
import hmac
import urllib.request
import urllib.parse
import urllib.error
import urllib.request
import urllib.error
import urllib.parse
import hashlib
import sys
import json
import config
from lib.exchange import exchange
from lib.settings import OKCOIN_API_URL

class PrivateOkCoinCNY(Market):
    okcoin = None

    def __init__(self,OKCOIN_API_KEY, OKCOIN_SECRET_TOKEN):
        super().__init__()
        self.okcoin = exchange(OKCOIN_API_URL, OKCOIN_API_KEY, OKCOIN_SECRET_TOKEN, 'okcoin')

        self.currency = "CNY"
        self.get_info()

    def _buy(self, amount, price):
        """Create a buy limit order"""
        response = self.okcoin.buy(amount, price)
        if "error_code" in response:
            print(response)
            return False
            raise TradeException(response["error"])

    def _sell(self, amount, price):
        """Create a sell limit order"""
        response = self.okcoin.sell(amount, price)
        if "error_code" in response:
            return False
            raise TradeException(response["error"])

    def get_info(self):
        """Get balance"""
        response = self.okcoin.accountInfo()
        if "error_code" in response:
            raise TradeException(response["error"])
        if response:
            self.btc_balance = float(response['info']['funds']['free']['btc'])
            self.cny_balance = float(response['info']['funds']['free']['cny'])
