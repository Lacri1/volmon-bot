# Volmon Bot

Volmon Bot is a Discord bot designed to provide real-time cryptocurrency price information and generate price charts using data from Binance. This project is an extension of the [VolMon](https://github.com/Lacri1/VolMon) project, adding chat bot functionalities.

## Features

*   **`!ping`**: Checks if the bot is online and responsive.
*   **`!price <SYMBOL>`**: Fetches the current price of a specified cryptocurrency pair (e.g., `!price BTCUSDT`).
*   **`!chart <SYMBOL> [INTERVAL] [LIMIT]`**: Generates a price chart for a cryptocurrency.
    *   `<SYMBOL>`: The cryptocurrency pair (e.g., `BTCUSDT`).
    *   `[INTERVAL]`: Optional. The time interval for the candlesticks (e.g., `1h`, `4h`, `1d`). Default is `1h`.
    *   `[LIMIT]`: Optional. The number of candlesticks to fetch for the chart. Default is 500.

## Prerequisites

Before running the bot, ensure you have the following installed:

*   Python 3.8+
*   pip (Python package installer)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Lacri1/volmon-bot.git
    cd volmon-bot
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    ```

3.  **Activate the virtual environment:**
    *   **Windows:**
        ```bash
        .venv\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```bash
        source .venv/bin/activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1.  **Create a `.env` file:**
    Create a file named `.env` in the root directory of the project.

2.  **Add your Discord Bot Token and Binance API Keys:**
    Obtain your Discord Bot Token from the [Discord Developer Portal](https://discord.com/developers/applications) and your Binance API Key and Secret from your Binance account. Add them to your `.env` file as follows:

    ```
    DISCORD_BOT_TOKEN=YOUR_DISCORD_BOT_TOKEN_HERE
    BINANCE_API_KEY=YOUR_BINANCE_API_KEY_HERE
    BINANCE_API_SECRET=YOUR_BINANCE_API_SECRET_HERE
    ```
    *Replace `YOUR_DISCORD_BOT_TOKEN_HERE`, `YOUR_BINANCE_API_KEY_HERE`, and `YOUR_BINANCE_API_SECRET_HERE` with your actual credentials.*

### Discord Bot Setup

To set up your Discord bot, follow these steps:

1.  **Create a New Application:**
    *   Go to the [Discord Developer Portal](https://discord.com/developers/applications).
    *   Click on "New Application" and give it a name (e.g., "Volmon Bot").

2.  **Create a Bot User:**
    *   In your application's settings, navigate to the "Bot" tab on the left sidebar.
    *   Click "Add Bot" and confirm.
    *   Under "Privileged Gateway Intents", enable the **"Message Content Intent"** toggle. This is crucial for the bot to read message content.

3.  **Get Your Bot Token:**
    *   On the "Bot" tab, you will see a "TOKEN" section. Click "Reset Token" if needed, then "Copy" to get your bot's token. This token should be placed in your `.env` file as `DISCORD_BOT_TOKEN`. **Keep this token secret!**

4.  **Generate an OAuth2 URL to Invite Your Bot:**
    *   Navigate to the "OAuth2" -> "URL Generator" tab.
    *   Under "SCOPES", select `bot`.
    *   Under "BOT PERMISSIONS", select the necessary permissions for your bot. At a minimum, you'll need:
        *   `Read Messages/View Channels`
        *   `Send Messages`
        *   `Attach Files` (for sending charts)
    *   Copy the generated URL at the bottom.

5.  **Invite the Bot to Your Server:**
    *   Paste the copied URL into your web browser.
    *   Select the Discord server you want to add the bot to from the dropdown menu.
    *   Click "Authorize" and complete the reCAPTCHA.
    *   Your bot should now appear in your Discord server's member list.

## Usage

1.  **Run the bot:**
    ```bash
    python bot.py
    ```
    The bot should connect to Discord and print a confirmation message in your console.

2.  **Use commands in Discord:**
    Once the bot is online in your server, you can use the commands in any text channel it has access to:
    *   `!ping`
    *   `!price BTCUSDT`
    *   `!chart ETHUSDT 4h`
    *   `!chart BNBUSDT 1d 100`
    *   `!help`

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.