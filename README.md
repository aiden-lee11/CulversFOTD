# Culver's Flavor of the Day Notifier

This project gathers the "Flavor of the Day" from multiple Culver's locations and sends an email summary each morning. The summary highlights your favorite flavors (if available) and lists other flavors for the day.

## Features

- **Fetch Flavors**: Gathers the "Flavor of the Day" from specified Culver's locations.
- **Email Notifications**: Sends a daily email with the available flavors, highlighting favorites.
- **Customizable**: Easily specify your favorite flavors, target locations, and email recipients via environment variables.

## Setup

### Prerequisites

- Python 3.x
- [Flask](https://flask.palletsprojects.com/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [requests](https://docs.python-requests.org/en/master/)
- [dotenv](https://pypi.org/project/python-dotenv/)
- A Gmail account for sending emails

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/aiden-lee11/CulversFOTD.git
    cd CulversFOTD
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add the following environment variables:
    ```bash
    FAVORITES=flavor1,flavor2,flavor3  # Your favorite flavors
    CITIES=city1,city2,city3  # Culver's city codes (e.g., 'madison', 'chicago')
    EMAIL_ADDRESS=your-email@gmail.com  # Your Gmail address
    EMAIL_PASSWORD=your-email-password  # Your Gmail password
    TO_EMAILS=email1@example.com,email2@example.com  # Recipient email addresses
    ```

### Running the Application

1. Start the Flask server:
    ```bash
    python index.py
    ```

2. The app will run on `http://localhost:8000/fotd`, which will automatically fetch the flavors and send the email.

### Deployment

For production deployment, I used vercel and have left the config file available that triggers a cron job for daily notifications

## Usage

- The application runs daily and sends an email with the available flavors from the specified cities.
- You can access the `/fotd` route to manually trigger the flavor check and email sending.

## License

This project is licensed under the MIT License.
