# Setup Venv
## Mac/Linux
```
$ mkdir myproject
$ cd myproject
$ python3 -m venv .venv
```

## Windows
```
> mkdir myproject
> cd myproject
> py -3 -m venv .venv
```

# Activate Venv
## Mac/Linux
```
$ . .venv/bin/activate
```

## Windows
```
> .venv\Scripts\activate
```

# Instal Packages
```
pip install -r requirements.txt
```

# Run Application
```
flask --app webapp/main run
```

# View Application
Navigate to `127.0.0.1:5000` in your web browser.