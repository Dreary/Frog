# Frog
Quick bot to post the trophy leaderboard (in a Google spreadsheet) to a specified Discord channel.

## Pre-requisites

1. [Python](https://www.python.org/ftp/python/3.12.4/python-3.12.4-amd64.exe)
2. [Git](https://git-scm.com/downloads)
3. [The trophy rankings spreadsheet](https://docs.google.com/spreadsheets/d/1OFficvfy95HQT-x8JOLJlMW-b3y0CEG0tX9tAGAiORE/edit?gid=0#gid=0), make sure it's visible to the public (top right -> share) 
4. [Google Cloud Console account](https://console.cloud.google.com/welcome/new?authuser=1)
5. Both [Google Drive](https://console.cloud.google.com/apis/library/drive.googleapis.com) + [Google Sheets](https://console.cloud.google.com/apis/library/sheets.googleapis.com) APIs activated (You can click the phrases to go to their respective URLs)

## Installation

1. Clone the repository: `git clone https://github.com/Dreary/Frog`
2. Install dependencies: `pip install discord.py gspread oauth2client wcwidth`
3. Go to Google Cloud Console and create a [service account](https://console.cloud.google.com/iam-admin/serviceaccounts), 
3b. Once this is done select your user and go to the "keys" tab. You'll see an "Add Key" button, select this and select "Create new key". Check the JSON key type and create, this should download your JSON. You can put this anywhere safe as long as you know where it is.
4. Head over to the [Discord Developer portal](https://discord.com/developers/applications) and create a new application, the name can be whatever you want.
5. Go to the 'OAuth2' tab and note down your Client ID.
6. Go to the 'Bot' tab and note down your token.
7. Now we're going to invite the bot to the server, using the url below:
`https://discord.com/api/oauth2/authorize?client_id=replaceme&permissions=549756161088&scope=bot&20applications.commands`
Replace the "replaceme" text after client_id with your Client ID you wrote down earlier. After this, just enter it in your browser and it should ask if you wish to add the bot to the Discord server.

8. Open your JSON file and copy the e-mail at Line 7 (client_id). 
8b. Then open the Google sheet you added to your Drive earlier -> Top right -> Share, then paste the e-mail you copied from the JSON into the text field at the top, then click Done.

9. Open the bot.py file in your chosen IDE and edit the following lines:
- Line 9: Replace "json_file_location_here" with the JSON file location you downloaded in Step 3b.
- Line 11: Edit "sheet_name" with the spreadsheet's name at the top left.
- Line 18: Edit "token_here" with the token you wrote down in step 7.
- Line 19: Edit "channel_id_here" with the channel ID you wish to post to, you can check this by right-clicking the channel name in Discord and selecting "Copy ID".

10. After all this it should be done, type in the following commands to run the bot:
- `cd C:\your discord bot location`
- `python bot.py`