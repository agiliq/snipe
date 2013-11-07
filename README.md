Snipe - A better screenshot tool:
=================================

Design goals:
-------------

1. Should be fast
2. Should allow just enough annotation capabilities
3. Integrates *only* with dropbox.
4. For ubuntu only (At least for now.)

Backstory:
----------

I remember the good days of skitch (before it was acquired by evernote, and turned into crapware.) I want to take a screenshot, add a callout, upload and then have the url to my image already loaded in my clipboard. Linux has shutter, but its not the same thing.

1. Too slow to be used all the time
2. Editing has too many menu choices
3. Upload ui has too many choices, doesn't integrate with dropbox.

`snipe` hopes to make a more usable screenshot tool.

Install:
--------

    sudo apt-get install pyqt4-dev-tools libqt4-dev
    git clone https://github.com/agiliq/snipe.git
    pip install -e .
    snipe
