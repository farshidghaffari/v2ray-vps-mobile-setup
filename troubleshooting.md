# Troubleshooting

## Container does not start

Check logs:

```bash
docker compose logs -f
```

Check config file exists:

```bash
ls -la config/config.json
```

If it does not exist, run:

```bash
python3 scripts/generate_config.py
```

## Android client cannot connect

Check these items:

- VPS IP is correct
- TCP port `10086` is open
- VPS provider firewall allows port `10086`
- Local Linux firewall allows port `10086`
- UUID is copied correctly
- Protocol is VMess
- Network is TCP
- Alter ID is 0

## Check if Docker is running

```bash
docker ps
```

## Restart service

```bash
docker compose restart
```

## Change port

1. Edit `config/config.template.json`
2. Edit `docker-compose.yml`
3. Regenerate config
4. Open the new firewall port
5. Restart Docker Compose
