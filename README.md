# V2Ray VPS Mobile Setup

A simple educational repository for running **V2Ray on a VPS with Docker** and connecting from an Android phone using a V2Ray-compatible client such as v2rayNG.

> Use this project only for lawful privacy, security, and personal networking purposes. Follow the laws and terms of service that apply in your country, VPS provider, and network.

## What This Project Includes

- Docker Compose setup for V2Ray
- VMess TCP server configuration
- Python script to generate a UUID and config file
- Android client setup guide
- Basic firewall and troubleshooting notes

## Repository Structure

```text
v2ray-vps-mobile-setup/
├── README.md
├── LICENSE
├── .gitignore
├── docker-compose.yml
├── config/
│   └── config.template.json
├── scripts/
│   └── generate_config.py
└── docs/
    ├── android-v2rayng-setup.md
    └── troubleshooting.md
```

## Requirements

You need:

- A Linux VPS
- Docker
- Docker Compose plugin
- An open TCP port, default: `10086`
- Android phone with a V2Ray-compatible client

This guide uses a simple VMess TCP setup to keep the configuration beginner-friendly.

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/farshidghaffari/v2ray-vps-mobile-setup.git
cd v2ray-vps-mobile-setup
```

### 2. Generate Server Config

```bash
python3 scripts/generate_config.py
```

This creates:

```text
config/config.json
client-info.txt
```

The `client-info.txt` file contains the values you need for your mobile client.

### 3. Start V2Ray

```bash
docker compose up -d
```

### 4. Check Logs

```bash
docker compose logs -f
```

### 5. Stop V2Ray

```bash
docker compose down
```

## Default Server Settings

| Setting | Value |
|---|---|
| Protocol | VMess |
| Network | TCP |
| Port | 10086 |
| Alter ID | 0 |
| Security | auto |

## Open Firewall Port

If you use UFW:

```bash
sudo ufw allow 10086/tcp
sudo ufw reload
```

If your VPS provider has a cloud firewall, also allow TCP port `10086` there.

## Android Setup

See:

```text
docs/android-v2rayng-setup.md
```

## Useful Commands

Restart:

```bash
docker compose restart
```

View container status:

```bash
docker compose ps
```

Update image:

```bash
docker compose pull
docker compose up -d
```

## Notes

- This starter setup does not include TLS, WebSocket, Nginx, or a domain name.
- For production use, consider adding TLS, a domain, and stricter firewall rules.
- Keep your UUID private.
- Do not publish your real server IP and UUID together.

## Related Links

- Portfolio: https://farshidghaffari.net
- GitHub: https://github.com/farshidghaffari
