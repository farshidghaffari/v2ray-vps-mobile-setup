# Android v2rayNG Setup

This guide explains how to connect your Android phone to the V2Ray server.

## Requirements

Install a V2Ray-compatible Android client such as **v2rayNG**.

## Manual Configuration

Create a new VMess profile with these values:

| Field | Value |
|---|---|
| Address | Your VPS IP address |
| Port | 10086 |
| User ID / UUID | The UUID inside `client-info.txt` |
| Alter ID | 0 |
| Security | auto |
| Network | tcp |
| Type | none |

## Steps

1. Open v2rayNG.
2. Tap the plus button.
3. Choose manual VMess configuration.
4. Enter the server IP, port, UUID, alterId, security, and network.
5. Save the profile.
6. Select the profile.
7. Tap connect.

## Test Connection

After connecting:

1. Open a browser.
2. Visit an IP check website.
3. Confirm that the IP address is your VPS IP.

## Important Notes

- If it does not connect, check VPS firewall rules.
- Make sure Docker is running.
- Check logs with:

```bash
docker compose logs -f
```

- Make sure the UUID in your phone is exactly the same as `client-info.txt`.
