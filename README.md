# Flask OIDC Client POC

Test RP to be used as POC

## Setup
Please notice that this is intented to be used initialy as a POC: configs may have sensisitive data for other context.

### Setup client
Edit the `config.py` file:

- `SERVER_META_URL` - the client will get all the provider information in this endpoint to setup connection
- `CLIENT_ID` -  client id provided by OP
- `CLIENT_SECRET` - client secret provided by OP
- `SCOPE` - scopes to be used, separated by spaces

### Setup Server

1. Place your certificates at `/etc/ssl` folder
2. Edit `ssl_certificate` and `ssl_certificate_key` in `./conf/nginx.conf`.
Please notice that `/etc/ssl` will be mapped to `/etc/nginx/certs/`, so you need to use the second one in your configuration.

## Starting Server
Make sure you have a recent Docker installed, in the project root, run:
`docker compose up --build`
Access your localhost or servername

## Stopping Server
`docker compose down`

## Logging
`sudo docker compose logs --follow` to follow with live logging

