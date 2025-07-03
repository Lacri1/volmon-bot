import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from pathlib import Path
import sys

# Add the parent directory to the sys.path to import volmon
sys.path.append(str(Path(__file__).parent.parent))

from volmon.utils.binance_client import BinanceClient
from volmon.utils.chart_generator import create_price_chart # This will be created later

load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
if not TOKEN:
    print("Error: DISCORD_BOT_TOKEN not found in .env file.")
    exit(1)

intents = discord.Intents.default()
intents.message_content = True # Required to read message content

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

binance_client = BinanceClient()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Loaded commands: {[command.name for command in bot.commands]}')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command(name='help')
async def help(ctx):
    help_message = """
**Volmon 봇 명령어:**
`!ping` - 봇이 온라인 상태인지 확인합니다.
`!price <SYMBOL>` - 암호화폐의 현재 가격을 가져옵니다 (예: `!price BTCUSDT`).
`!chart <SYMBOL> [INTERVAL] [LIMIT]` - 암호화폐의 가격 차트를 생성합니다.
    - `<SYMBOL>`: 암호화폐 쌍 (예: `BTCUSDT`).
    - `[INTERVAL]`: 선택 사항. 차트의 시간 간격 (예: `1h`, `4h`, `1d`). 기본값은 `1h`입니다.
    - `[LIMIT]`: 선택 사항. 가져올 캔들스틱의 개수. 기본값은 500입니다.
"""
    await ctx.send(help_message)

@bot.command(name='price')
async def price(ctx, symbol: str):
    try:
        # Use the get_ticker_price from volmon's BinanceClient
        data = binance_client.get_ticker_price(symbol.upper())
        price = float(data['price'])
        await ctx.send(f'The current price of {symbol.upper()} is ${price:,.2f}')
    except Exception as e:
        await ctx.send(f'Could not fetch price for {symbol.upper()}. Error: {e}')

@bot.command(name='chart')
async def chart(ctx, symbol: str, interval: str = '1h', limit: int = 500):
    try:
        # Fetch klines data
        klines = binance_client.get_klines(symbol.upper(), interval, limit=limit)
        if not klines:
            await ctx.send(f'No chart data found for {symbol.upper()} with interval {interval} and limit {limit}.')
            return

        # Generate chart image
        chart_path = create_price_chart(klines, symbol.upper(), interval)
        
        # Send the chart image
        await ctx.send(file=discord.File(chart_path))
        
        # Clean up the generated chart file
        os.remove(chart_path)

    except Exception as e:
        await ctx.send(f'Could not generate chart for {symbol.upper()}. Error: {e}')

def run_bot():
    bot.run(TOKEN)

if __name__ == '__main__':
    run_bot()
