# XiaomiCloudGalleryDownloader
Download all the images stored in your Xiaomi Cloud account

Found that you can't perform an easy "take out" like you can with a Google account from Xiaomi Cloud so this downloader should help.

Provided as-is as a very simple script to download.

You'll need to sign in to Xiaomi Cloud (i.mi.com) and grab the cookie for one of the requests with a "?" in.

1) Open a web browser
2) Launch dev tools (Chromium browsers either F12 or Ctrl+Shift+I)
3) Open network tab
4) Check preserve log
5) Enter in filter box "status?ts" (no quotes)
6) Back in the new tab, browse to "i.mi.com", sign in if required
7) Go back to dev tools, you should see a request appear for "status?ts=<some extra numbers here>", double-click on it
8) Under the headers tab on the right menu, look under "Request Headers" for the "Cookie" value
9) Copy cookie and paste when prompted for it
10) Provide a path where to save the downloaded files
11) Wait, if you have lots of pictures you may have to do the above a few times, especially if interrupted.


Known issues:
Video files don't seem to play once downloaded.
Most metadata is lost when downloaded.

Requirements:
Python 3.6+
requests module installed (pip install requests)