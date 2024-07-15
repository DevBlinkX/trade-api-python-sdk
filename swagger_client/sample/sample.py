from swagger_client.api import DefaultApi
from swagger_client.api import ChartApi
from swagger_client.api import LimitApi
from swagger_client.api import LoginApi
from swagger_client.api import MarketDataApi
from swagger_client.api import OrderControllerApi
from swagger_client.api import PositionControllerApi
from swagger_client.api import ReportApi
from swagger_client.api import TradeBookApi
from swagger_client.api import TradeDetailsApi

if __name__ == "__main__":
    loginAPI = DefaultApi()
    login_body = {
        "userId": "SAMPLE1",
        "password": "sample@123",
        "mobileNumber": "1234567890"
    }

    api_key = "SAMPLE_API_KEY"
    login_response_body, login_status_code, login_headers = loginAPI.login_normal_login_post(login_body, api_key)
    print("login response: " + str(login_response_body))
    accessToken = login_response_body.to_dict()["data"]["accessToken"]

    # print(self.deserialize(response_body, LoginResponse))
    # print(dir(response_body))
    # access_token = json.load(response_body)
    # print("data: " + str(response_body))
    # print("accessToken: " + access_token)

    # intraday candle chart
    chartAPI = ChartApi()

    intraday_body = {
        "data": {
            "exchangeInstrumentID": "22",
            "exchange": "NSE",
            "startTime": "Mar 14 2024 150000",
            "endTime": "Mar 14 2024 161500"
        }
    }

    intraday_response_body, intraday_status_code, intraday_headers = chartAPI.intraday(intraday_body, accessToken,
                                                                                       api_key)

    print("intraday response: " + str(intraday_response_body))

    # sparkline
    sparkline_body = {
        "data": {
            "instruments": [
                {
                    "exchange": "NSE",
                    "exchangeInstrumentID": "6364"
                }
            ]
        }
    }

    sparkline_response_body = chartAPI.spark_line(sparkline_body, accessToken, api_key)

    print("sparkline response: " + str(sparkline_response_body))

    # history candle
    history_response_body = chartAPI.historical_data(
        accessToken,
        api_key,
        "UNIONBANK",
        "1D",
        "785244",
        "9777",
        "200",
        "NSE",
        "10753"
    )[0]

    print("history response: " + str(history_response_body))

    # funds
    limitAPI = LimitApi()

    funds_response_body = limitAPI.fund_view(accessToken, api_key)[0]

    print("funds response: " + str(funds_response_body))

    # profile
    loginAPI = LoginApi()

    profile_body = {"data": {}, "appID": "1"}

    profileAPI = loginAPI.get_profile(profile_body, accessToken, api_key)

    print("profile response: " + str(profileAPI))

    # quotes
    marketAPI = MarketDataApi()

    quotes_body = {
        "data": {
            "instruments": [
                {
                    "exchange": "NSE",
                    "exchangeInstrumentID": "22"
                }
            ]
        }
    }

    quotes_response_body = marketAPI.get_quote(quotes_body, accessToken, api_key)

    print("quotes response: " + str(quotes_response_body))

    # place order
    orderAPI = OrderControllerApi()

    brokerage_body = {
        "symbol": "ACC-EQ",
        "exc": "NSE",
        "product": "NRML",
        "triggerPrice": "",
        "price": "3000",
        "qty": "100",
        "instrument": "",
        "orderAction": "BUY",
        "excToken": "25"
    }

    brokerage_response_body = orderAPI.brokerage_charges(
        brokerage_body,
        "DGB101",
        accessToken,
        api_key,
        "WEB"
    )

    print("brokerage response: " + str(brokerage_response_body))

    place_order_body = {
        "symbol": "NATIONALUM-EQ",
        "excToken": "6364",
        "ordAction": "Buy",
        "ordValidity": "DAY",
        "ordType": "LIMIT",
        "prdType": "NORMAL",
        "qty": 5,
        "triggerPrice": 0,
        "limitPrice": 192.55,
        "disQty": 0,
        "instrument": "STK",
        "exc": "NSE",
        "lotSize": 0,
        "amo": False,
        "build": "MOB",
        "boStpLoss": 0,
        "boTgtPrice": 0,
        "trailingSL": 0
    }

    place_order_response_body = orderAPI.place_order(place_order_body, "DGB101", "WEB", accessToken, api_key)[0]

    print("place response: " + str(place_order_response_body))

    orderId = place_order_response_body.to_dict()["data"]["ord_id"]

    # modify order
    modify_order_body = {
        "triggerPrice": 0,
        "ordType": "LIMIT",
        "prdType": "CASH",
        "instrument": "STK",
        "exc": "NSE",
        "qty": 10,
        "lotSize": 0,
        "symbol": "NATIONALUM-EQ",
        "ordId": f"{orderId}",
        "ordAction": "BUY",
        "limitPrice": 192.55,
        "disQty": 0,
        "ordValidity": "DAY",
        "tradedQty": 0,
        "ordValidityDays": 0,
        "exchangeToken": "13528",
        "amo": True
    }

    modify_order_response_body = orderAPI.modify_order(modify_order_body, "DBG101", "WEB", accessToken, api_key)[0]

    print("modify response: " + str(modify_order_response_body))

    # cancel order
    cancel_order_body = {
        "symbol": "NATIONALUM-EQ",
        "ordId": f"{orderId}",
        "exc": "NSE"
    }

    cancel_order_response_body = orderAPI.cancel_order(cancel_order_body, "DBG101", "WEB", accessToken, api_key)

    print("cancel order response: " + str(cancel_order_response_body))

    # todo exit orders

    # todo convert positions

    # todo holdings

    # position book
    positionAPI = PositionControllerApi()

    position_book_response_body = positionAPI.get_position_book("net", "DBG101", "WEB", accessToken, api_key)[0]

    print("position response: " + str(position_book_response_body))

    # profit and loss
    reportAPI = ReportApi()

    p_and_l_body = {
        "data": {
            "fromDate": "",
            "months": "10",
            "fy": "",
            "segment": "equity",
            "toDate": "",
            "days": ""
        },
        "appID": "1"
    }

    p_and_l_response_body = reportAPI.profit_loss_report(p_and_l_body, accessToken, api_key)

    print("profit and loss response: " + str(p_and_l_response_body))

    # order book
    bookAPI = TradeBookApi()

    order_book_response_body = bookAPI.get_order_book("DBG101", "WEB", accessToken, api_key)[0]

    print("order book response: " + str(order_book_response_body))

    trade_book_response_body = bookAPI.trade_book("DBG101", "WEB", accessToken, api_key)[0]

    print("trade book response: " + str(trade_book_response_body))

    # trade details
    tradeDetailsAPI = TradeDetailsApi()

    details_body = {
        "ordId": f"{orderId}"
    }

    # trade_details_response_body = tradeDetailsAPI.trade_details_using_order_id(details_body, accessToken, api_key)

    # order_details_response_body = tradeDetailsAPI.order_details(details_body, accessToken, api_key)

    # order_history_response_body = tradeDetailsAPI.order_history(accessToken, api_key)
