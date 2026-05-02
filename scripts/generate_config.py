"""
Generate V2Ray VMess server configuration.

This script creates:
- config/config.json
- client-info.txt

Usage:
    python3 scripts/generate_config.py
"""

from pathlib import Path
import uuid


ROOT_DIR = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = ROOT_DIR / "config" / "config.template.json"
OUTPUT_CONFIG_PATH = ROOT_DIR / "config" / "config.json"
CLIENT_INFO_PATH = ROOT_DIR / "client-info.txt"

DEFAULT_PORT = 10086


def main() -> None:
    """Generate a UUID and write the V2Ray config file."""
    user_uuid = str(uuid.uuid4())

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    config = template.replace("{{UUID}}", user_uuid)

    OUTPUT_CONFIG_PATH.write_text(config, encoding="utf-8")

    client_info = f"""V2Ray Client Information
========================

Use these values in your Android V2Ray client.

Address / Server:
YOUR_VPS_IP

Port:
{DEFAULT_PORT}

User ID / UUID:
{user_uuid}

Alter ID:
0

Security:
auto

Network:
tcp

Protocol:
vmess

Notes:
- Replace YOUR_VPS_IP with your real VPS IP address.
- Keep this UUID private.
- Make sure TCP port {DEFAULT_PORT} is open on the VPS firewall and provider firewall.
"""

    CLIENT_INFO_PATH.write_text(client_info, encoding="utf-8")

    print("Generated config/config.json")
    print("Generated client-info.txt")
    print()
    print("UUID:", user_uuid)
    print("Port:", DEFAULT_PORT)
    print()
    print("Next:")
    print("1. Replace YOUR_VPS_IP in client-info.txt with your VPS IP.")
    print("2. Run: docker compose up -d")


if __name__ == "__main__":
    main()
