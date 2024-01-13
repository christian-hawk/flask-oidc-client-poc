from oidc_client import create_app

if __name__ == '__main__':
    app = create_app()
    app.debug = True
    app.run(host='0.0.0.0', port=9090, use_reloader=True)

#
# if __name__ == '__main__':
#     app = create_app()
#     app.debug = True
#     app.run(host='0.0.0.0', ssl_context=('cert.pem', 'key.pem'), port=9090, use_reloader=False)

headers = {
'Host' : 'cert.1stadvantage.org',
'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0',
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate, br',
'DNT': '1',
'Sec-GPC': '1',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate'
}