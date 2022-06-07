import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_key = "I0DNP6YEJHDIE5K3"
news_api_Key = "1415c3416b9d499ea2efe2bd5d3e1912"
#https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=I0DNP6YEJHDIE5K3


stock_parameters={
        "function": "TIME_SERIES_DAILY",
        "symbol": "TSLA",
        "apikey": "I0DNP6YEJHDIE5K3"

}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
stock_data= response.json()

friday_stock_day = stock_data["Time Series (Daily)"]["2022-05-25"]["4. close"]
saturday_stock = stock_data["Time Series (Daily)"]["2022-05-26"]["4. close"]

#To get the closing difference and percentage
closing_diff=(float(saturday_stock) -float(friday_stock_day))
percentage = (closing_diff/float(saturday_stock)) * 100


#To get three articles about Telsa
news_parameters={
        "q": "Telsa",
        "apiKey":news_api_Key,
        "qinTitle": COMPANY_NAME

}
if percentage < 5:
    response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
    response.raise_for_status()
    #print(resposnse.status_code)
    news_data= response.json()

    stock_article_slice=(news_data["articles"][0:3])
    print(stock_article_slice)
    #print(stock_article_slice['title'])

    all_3_articles= []
    for article in stock_article_slice:
        all_articles = f"Headline:{article['title']},\nBrief: {article['description']}"
        print(all_articles)
        all_3_articles.append(all_articles)

    for article in all_3_articles:
        client = Client(account_sid, auth_token, http_client=proxy_client)
        message = client.messages.create(body=article,
                                         from_="YOUR TWILIO VIRTUAL NUMBER",
                                         to="YOUR TWILIO VERIFIED REAL NUMBER"
                                         )
        print(message.status)

#Or
#formatted_articles_list = [f"Headline:{stock_article_slice['title']}: \nBrief:{stock_article_slice['description']}"
# for articles in stock_article_slice]
#print(formatted_articles_list)

# for articles in stock_articles:
#     if percentage > 0.05:
#         print(articles)
#     print("Get News")


#if this the first using twilio for sms loolk at the rain alert on how to properly set up for proxy users











    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint:

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
   #https: // newsapi.org / v2 / everything?q = Tesla & apiKey = 1415c3416b9d499ea2efe2bd5d3e1912
    #https: // newsapi.org / v2 / everything?q = keyword & apiKey = 1415c3416b9d499ea2efe2bd5d3e1912


    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio.
#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""