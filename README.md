# wow-keys-thingy

make life easy and run in a venv :)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## server

## client

### build

if you want to redistribute this client to your friends (likely) you can use pyinstaller to compile it into an executable and share that with your friends:

```bash
pyinstaller --onefile --no-console post-savedinstances.py
```

find your executable in the `dist` folder.

### install

#### windows

move files wherever you want them to live, make sure executable, install.bat and config.ini are hand-in-hand like a happy little family.
double-check config.ini values.
run install.bat as admin.
hope keys show up at `server_url` configured in config.ini.
