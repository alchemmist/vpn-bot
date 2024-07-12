# VPN bot
A bot to gain access to the WireGuard server

## Run
Let's start by cloning this repository and move into it:
```bash
git clone git@github.com:romanenko-vova/vpn_bot.git
cd vpn_bot
```

Before running create `.env` file and define `TELEGRAM_BOT_TOKEN` variable. For example:
```
# .env

TELEGRAM_BOT_TOKEN=<token_for_your_bot>
```

Then you cun run bot with poetry or Docker:

### Run with Docker
Using docker-compose:
```bash
docker compose build
docker compse up
```

### Run with poetry
```bash
poetry install
poetry run python vpn_bot
```


