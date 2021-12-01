# VcPlayer
# Telegram Voice-Chat Bot [PyTGCalls] [![Mentioned in Awesome Telegram Calls](https://awesome.re/mentioned-badge-flat.svg)](https://github.com/tgcalls/awesome-tgcalls)

##           ⇝ Requirements ⇜

### Account requirements
- A Telegram account to use as the music bot, **You cannot use regular bot accounts, as they cannot join voice chats. *It must be a user account.***
- API_ID and API_HASH for that account.
- The account must be an admin of the chat, with _Manage Voice Chats_ and _Delete Messages_ permissions.

### Environment requirements
- Linux-based OS. **You cannot run this on Windows natively, Use WSL**
- Python 3.9 or later.
- ffmpeg package, look below for instructions.


## ⇝ Heroku ⇜

#### Generate String session [IMPORTANT]

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Akshat7678/VcPlayer/)
https://replit.com/@AkshatKumar6/GenerateStringSession#main.py

Send [commands](#commands) to bot to play music.



## Commands
Command | Description
:--- | :---
/help | Show Help Message.
/skip | Skip Any Playing Music.
/play [SONG_NAME] | To Play A Song Using Saavn.<br>Service used can be changed in config (`DEFAULT_SERVICE`).
/play youtube/saavn [SONG_NAME] | To Play A Song Using Specific Service.
/play [with reply to an audio file] | To Play A Song With TG Audio File.
/queue | Check Queue Status.
/delqueue | Deletes Queue List and Playlist.
/playlist [songs name separated by line] | Start Playing Playlist.
/joinvc | Join Voice Chat.
/leavevc | Leave Voice Chat.
/volume [1-200] | Adjust Volume.
/pause | Pause Music.
/resume | Resume Music.
