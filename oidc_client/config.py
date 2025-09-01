
# configuration file

# SERVER_META_URL - the client will get all the provider information in this endpoint to setup connection
SERVER_META_URL = 'https://cert.1stadvantage.org/idp/identity/.well-known/openid-configuration'

# registered OIDC client id
CLIENT_ID = 'selfservice-oidc-sso'

# registered OIDC client secret
CLIENT_SECRET = 'TEST CLIENT SECRET'

# scopes
SCOPE = 'openid core_identity'

# to logout upcoming feature:
END_SESSION_ENDPOINT = 'https://cert.1stadvantage.org/idp/identity/connect/endsession'
POST_LOGOUT_REDIRECT = 'https://memberportal-test.1stadvantage.org' 



# the following settings  may be used to do client tests. 
# SERVER_META_URL = 'https://demo.duendesoftware.com/.well-known/openid-configuration'
# CLIENT_ID = 'interactive.confidential'
# CLIENT_SECRET = 'secret'
# SCOPE = 'openid profile email api offline_access'
# END_SESSION_ENDPOINT = 'https://demo.duendesoftware.com/connect/endsession' 

