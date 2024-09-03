import os
import smtplib
from datetime import date
from email.mime.text import MIMEText

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from flask import Flask, jsonify

load_dotenv()

app = Flask(__name__)

favorites = os.getenv('FAVORITES').split(',')
cities = os.getenv('CITIES').split(',')
email_address = os.getenv('EMAIL_ADDRESS')
email_password = os.getenv('EMAIL_PASSWORD')
to_emails = os.getenv('TO_EMAILS').split(',')

@app.route('/fotd')
def fotd():
    fotd_data = []
    for city in cities:
        page = requests.get(f'https://www.culvers.com/restaurants/{city}')
        soup = BeautifulSoup(page.text, 'html.parser')
        fotdSection = soup.find("h2", {"class": "RestaurantDetails_containerRestaurantFlavorContentHeading__sLzcV"})
        fotdString = fotdSection.text.strip() if fotdSection else "No Flavor Found"
        fotd_data.append({'city': city, 'flavor': fotdString})

    favorites_data = [item for item in fotd_data if item['flavor'] in favorites]
    others_data = [item for item in fotd_data if item['flavor'] not in favorites]

    email_content = ''
    if len(favorites_data) > 0:
        email_content += 'Favorites:<br>'

        for item in favorites_data:
            email_content += f"<b style='color: green'>{item['city']}: {item['flavor']}</b><br>"
    else:
        email_content += 'No Favorite Flavors Available Today :(<br>'

    email_content += '<br>'

    if len(others_data) > 0:
        email_content += 'Others:<br>'

        for item in others_data:
            email_content += f"{item['city']}: {item['flavor']}<br>"
    else:
        email_content += "No Non-Favorite Flavors Today!! :)<br>"

    today = date.today()
    day = today.day
    suffix = 'th' if 11<=day<=13 else {1:'st',2:'nd',3:'rd'}.get(day%10, 'th')
    subject = f"Culver's Flavor of the Day - {today.strftime('%B')} {day}{suffix}, {today.year}"

    msg = MIMEText(email_content, 'html')
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = ', '.join(to_emails)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_address, email_password)
    server.sendmail(email_address, to_emails, msg.as_string())
    server.quit()

    return jsonify({'message': 'Flavor of the Day email sent successfully'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))