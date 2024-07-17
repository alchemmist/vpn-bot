# VPN bot
A bot to gain access to the WireGuard server

# TO-DO
- [ ] Дать возможность админу добавлять премиальных пользователей (с бесплатным доступом)

## Run
Let's start by cloning this repository and move into it:
```bash
git clone git@github.com:romanenko-vova/vpn_bot.git
cd vpn_bot
```

Before running, rename `.env.example` file to `.env` and define `TELEGRAM_BOT_TOKEN` variable.
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


