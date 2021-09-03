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

extract archive into subfolder of your accounts savedvariables folder
i.e. D:\games\World of Warcraft\_retail_\WTF\Account\401500458#1\SavedVariables\post-savedinstances
right click install.bat, run as administrator
hope keys show up on keys.nastye.xyz
