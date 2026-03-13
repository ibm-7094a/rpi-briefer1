import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to get the weather forecast for the current day in Fahrenheit
def get_weather(api_key, city):
    # Construct the API request URL for a 1-day weather forecast in Fahrenheit
    url = f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=1&units=imperial"
    response = requests.get(url)
    data = response.json()
    
    # Extract the weather forecast for the current day
    day = data['forecast']['forecastday'][0]  # Get the first day of the forecast, which is today
    date = day['date']
    max_temp = day['day']['maxtemp_f']
    min_temp = day['day']['mintemp_f']
    condition = day['day']['condition']['text']
    forecast = f"{date}: Max Temp: {max_temp}°F, Min Temp: {min_temp}°F, Condition: {condition}\n\n"
    
    return forecast

# Function to get the top news headline
def get_news(api_key):
    # Construct the API request URL for the top news headlines
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    
    # Extract only the top headline from the news articles
    top_headline = data['articles'][0]['title'] if data['articles'] else "No news available"
    return top_headline

# Function to send an email
def send_email(sender_email, sender_password, receiver_email, subject, body):
    # Create a multipart email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Set up the SMTP server, log in, and send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

# Main function
def main():
    # Define your API keys
    weather_api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    news_api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    # Replace 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx' with your actual Weather API key
    # Replace 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' with your actual News API key

    # Define your email credentials
    sender_email = 'xxxxxxxxxx@gmail.com'
    sender_password = 'xxxxxxxxxxxxxxxxx'
    # Replace 'xxxxxxxxxx@gmail.com' with your email address
    # Replace 'xxxxxxxxxxxxxxxxx' with your email password or an app-specific password

    # Define the recipient email address
    receiver_email = 'SMS-NUMBER@provider.com'
    # Replace 'SMS-NUMBER@provider.com' with the correct email address for the SMS gateway

    # Get the weather forecast and the top news headline
    weather = get_weather(weather_api_key, "YOUR-CITY")
    # Replace 'YOUR-CITY' with the city for which you want the weather forecast
    news = get_news(news_api_key)

    # Compose the email subject and body
    subject = "Good Morning, Here's Your Daily Briefing:"
    body = f"\nWeather Forecast for Today:\n\n{weather}\n\nTop News Headline:\n\n{news}"

    # Send the email
    send_email(sender_email, sender_password, receiver_email, subject, body)

# Entry point for the script
if __name__ == "__main__":
    main()
