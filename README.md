# KiteConnect CLI
A simple cli tool to obtain access token

### Installation
```bash
pip install kiteconnect-cli
```

### Usage
Assuming the redirect url path as `authorized`

```bash
kiteconnect-cli API_KEY API_SECRET authorized --port 8000
```

Spins up the web browser for login, Fill in the credentials and submit. Access token will be displayed on the browser window as well as in the command line