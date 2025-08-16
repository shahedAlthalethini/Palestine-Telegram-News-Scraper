# Telegram Channel Scraper

This project is a Python script designed to scrape messages from specific public Telegram channels within a defined date range. It utilizes the `Telethon` library to interact with the Telegram API and the `pandas` library to organize the scraped data into a clean CSV file.

## Features

-   Scrape messages from multiple public channels simultaneously.
-   Filter messages by a specific date range (start and end dates).
-   Extract the message date, channel name, and full text content.
-   Save the results into a single CSV file, encoded with `utf-8-sig` to properly support special characters and different languages (like Arabic).
-   Leverages asynchronous programming for efficient and fast data fetching.

## Channels to be Scraped

The script is pre-configured to scrape the following news channels:

-   **Al Jazeera - Palestine:** `@AJPalestine`
-   **Misbar:** `@MisbarFC`
-   **Tibian News Agency:** `@tibianps`

## Prerequisites

Before you begin, ensure you have the following:

-   Python 3.8 or newer.
-   An active Telegram account.
-   Telegram API credentials (`api_id` and `api_hash`). You can obtain these by logging into your account at [my.telegram.org](https://my.telegram.org).

## Setup and Installation

Follow these steps to set up the project on your local machine.

1.  **Clone the Repository**
    Clone or download this project to your computer.

2.  **Create a Virtual Environment (Recommended)**
    It is a best practice to use a virtual environment to manage project dependencies.

    ```bash
    # Create the virtual environment
    python -m venv venv

    # Activate the environment
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    venv\Scripts\activate
    ```

3.  **Install Required Libraries**
    Install the necessary Python packages using pip.

    ```bash
    pip install telethon pandas python-dotenv
    ```

4.  **Configure API Credentials**
    Create a file named `.env` in the root directory of the project. Add your Telegram API credentials to this file as follows:

    ```dotenv
    API_ID="YOUR_API_ID"
    API_HASH="YOUR_API_HASH"
    ```
    Replace `"YOUR_API_ID"` and `"YOUR_API_HASH"` with the actual values you obtained from Telegram.

## How to Use

To scrape messages for a specific year (e.g., 2023, 2024, or 2025), you need to modify the `start_date`, `end_date`, and the output filename in the script.

1.  **Open the Python Script**
    Open your script file (e.g., `scraper.py`) in a text editor or IDE.

2.  **Set the Date Range and Output File**
    Locate the date range section in the script. Uncomment the lines for the year you wish to scrape and define a unique output filename for that year.

    **Example for scraping all of 2023:**
    ```python
    # Date range: All of 2023
    start_date = datetime(2023, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
    end_date = datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc)
    output_filename = "telegram_news_2023.csv"
    ```

    **Example for scraping all of 2024:**
    ```python
    # Date range: All of 2024
    start_date = datetime(2024, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
    end_date = datetime(2024, 12, 31, 23, 59, 59, tzinfo=timezone.utc)
    output_filename = "telegram_news_2024.csv"
    ```

    **Example for scraping all of 2025:**
    ```python
    # Date range: All of 2025
    start_date = datetime(2025, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
    end_date = datetime(2025, 12, 31, 23, 59, 59, tzinfo=timezone.utc)
    output_filename = "telegram_news_2025.csv"
    ```
    **Important:** Make sure the `df.to_csv()` function at the end of the script uses your `output_filename` variable:
    ```python
    # Inside the main() function
    df.to_csv(output_filename, index=False, encoding='utf-8-sig')
    print(f"\nDone! Saved {len(df)} messages to {output_filename}")
    ```

3.  **Run the Script**
    Execute the script from your terminal.

    ```bash
    python scraper.py
    ```
    The first time you run the script, `Telethon` will prompt you to log in to your Telegram account. You will need to enter your phone number, the verification code sent to you by Telegram, and your two-factor authentication password (if enabled). A `my_session.session` file will be created to keep you logged in for future runs.

## Output

The script will generate a CSV file (e.g., `telegram_news_2024.csv`) in the project directory. The file will contain the following columns:

-   `date`: The UTC date and time the message was posted.
-   `channel`: The username of the Telegram channel.
-   `text`: The full text content of the message.

### Example CSV Output:

| date                | channel     | text                                        |
| ------------------- | ----------- | ------------------------------------------- |
| 2024-01-15 10:30:11 | AJPalestine | This is an example news update text from... |
| 2024-01-15 11:05:45 | MisbarFC    | A fact-check article about a recent...      |
| 2024-01-16 09:00:23 | tibianps    | Breaking news report on current events...   |

