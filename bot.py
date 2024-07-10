import discord
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from wcwidth import wcswidth

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("json_file_location_here", scope)
client = gspread.authorize(creds)
sheet = client.open("sheet_name").sheet1

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TOKEN = 'token_here'
CHANNEL_ID = 'channel_id_here'

@client.event
async def on_ready():
    print(f'Bot is ready. Logged in as {client.user}')
    await post_leaderboard()

def format_cell(content, width):
    """Format a cell to ensure proper width considering wide characters."""
    actual_width = wcswidth(content)
    padding = width - actual_width
    return content + ' ' * padding

async def post_leaderboard():
    channel = client.get_channel(int(CHANNEL_ID))
    
    # Fetch data from Google Sheets
    data = sheet.get_all_values()
    leaderboard_data = data[1:11]  # Assuming the first row is the header

    # Define column widths considering wide characters
    rank_width = 5
    trophy_width = 12
    username_width = 15

    # Format the table
    current_date = datetime.now().strftime("%B %d, 2024")
    title = f"<:mtrophy:1260703894489661481> [MapleAge2] {current_date} Trophy Rankings"
    table_header = f"| {'Rank':<{rank_width}} | {'Trophy Count':<{trophy_width}} | {'Username':<{username_width}} |"
    table_divider = f"|{'-'*(rank_width+2)}|{'-'*(trophy_width+2)}|{'-'*(username_width+2)}|"
    table_rows = [
        f"| {format_cell(str(rank), rank_width)} | {format_cell(row[2], trophy_width)} | {format_cell(row[1], username_width)}"
        for rank, row in enumerate(leaderboard_data, start=1)
    ]

    table = "\n".join([table_header, table_divider] + table_rows)
    
    # Send the message
    await channel.send(f"**{title}**\n```\n{table}\n```")

client.run(TOKEN)