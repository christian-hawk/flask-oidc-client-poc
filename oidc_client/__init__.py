from flask import Flask, render_template, redirect, request, session, url_for, jsonify

from authlib.integrations.flask_client import OAuth
from . import logout
from . import config as cfg
from .helpers.setup_logging import setup_logging

oauth = OAuth()



def create_app() -> Flask :
    setup_logging()
    app = Flask(__name__)
    app.logger.info('Flask app factory called')
    app.secret_key = 'dev'

    app.logger.info('Loading client configuration from file...')

    app.config['OP_CLIENT_ID'] = cfg.CLIENT_ID
    app.config['OP_CLIENT_SECRET'] = cfg.CLIENT_SECRET
    
    server_metadata_url = cfg.SERVER_META_URL

    app.logger.info('Metadata will be loaded from %s' % server_metadata_url )
    app.logger.info('Config scope value is %s' % cfg.SCOPE)


    oauth.init_app(app)
    oauth.register(
        'op',
        server_metadata_url= server_metadata_url, ##'http://localhost:9090/temp-server-metadata', 'https://cert.1stadvantage.org/idp/identity/.well-known/openid-configuration',
        client_kwargs={
            'scope': cfg.SCOPE,
            #'code_challenge_method': 'S256'
        },
        # token_endpoint_auth_method='client_secret_post',# cfg.SERVER_TOKEN_AUTH_METHOD
        # user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0'
    )

    # logout as a bp already
    app.register_blueprint(logout.bp)
    # TODO: group endpoints as blueprints

    @app.route('/')
    def index():
        app.logger.info('index called')
        return render_template('index.html')
   

    @app.route('/login')
    def login():
        # authorize redirect to external login
        app.logger.info('login called')
        query_args = {
            'redirect_uri': 'https://memberportal-test.1stadvantage.org/callback',
        }
        response = oauth.op.authorize_redirect(**query_args)
        app.logger.debug('/login authorize_redirect(redirect_uri) url = %s' %
                         response.location)
        return response


    @app.route('/protected-content')
    def protected_content():
        # shows protected content (user info) to authorized ressource owner
        app.logger.info('protected_content called')
        app.logger.debug('/protected-content - cookies = %s' % request.cookies)
        app.logger.debug('/protected-content - session = %s' % session)
        if 'user' in session:
            # shows user
            app.logger.info('user allowed, returning requested content...')
            return session['user']

        app.logger.info('session not allowed, redirecting to login...')
        return redirect(url_for('login'))


    @app.route('/callback')
    def callback():
        app.logger.info('callback called')
        app.logger.info('/callback - received %s - %s' %
                        (request.method, request.query_string))
        # receives callback from OP
        #try:
        if not request.args['code']:
            app.logger.warning('Callback called without code argument, returning 400')
            return {}, 400

       
        token = oauth.op.authorize_access_token()
        app.logger.debug('/callback - token = %s' % token)
        session['id_token'] = token['id_token']
        user = oauth.op.userinfo()
        app.logger.debug('/callback - user = %s' % user)
        session['user'] = user
        # session['id_token'] = token['userinfo']
        app.logger.debug('/callback - cookies = %s' % request.cookies)
        app.logger.debug('/callback - session = %s' % session)

        return redirect('/')

        # except Exception as error:
        #     app.logger.error(str(error))
        #     return {'error': str(error)}, 400
        ...

    @app.route('/temp-server-metadata')
    def temp_server_metadata():
        # replace server metadata url while not accessible
        return jsonify(
        {
            "issuer": "https://coa-ws1-c.onefiserv.net:443/idp/identity",
            "jwks_uri": "https://cert.1stadvantage.org/idp/identity/.well-known/jwks",
            "authorization_endpoint": "https://cert.1stadvantage.org/idp/identity/connect/authorize",
            "token_endpoint": "https://cert.1stadvantage.org/idp/identity/connect/token",
            "userinfo_endpoint": "https://cert.1stadvantage.org/idp/identity/connect/userinfo",
            "end_session_endpoint": "https://cert.1stadvantage.org/idp/identity/connect/endsession",
            "check_session_iframe": "https://cert.1stadvantage.org/idp/identity/connect/checksession",
            "revocation_endpoint": "https://cert.1stadvantage.org/idp/identity/connect/revocation",
            "introspection_endpoint": "https://cert.1stadvantage.org/idp/identity/connect/introspect",
            "frontchannel_logout_supported": True,
            "frontchannel_logout_session_supported": True,
            "scopes_supported": [
                "openid",
                "core_identity",
                "offline_access",
                "identity",
                "subject",
                "request_claims",
                "Alexa",
                "trusted_introspection",
                "trusted_anonymous",
                "one_token_per_subject",
                "subject_notarization",
                "challenge"
            ],
            "claims_supported": [
                "sub",
                "identity://fiserv.com/corillian/claims/coreid"
            ],
            "response_types_supported": [
                "code",
                "token",
                "id_token",
                "id_token token",
                "code id_token",
                "code token",
                "code id_token token"
            ],
            "response_modes_supported": [
                "form_post",
                "query",
                "fragment"
            ],
            "grant_types_supported": [
                "authorization_code",
                "client_credentials",
                "password",
                "refresh_token",
                "implicit",
                "Sterling-Pwd",
                "token-exchange",
                "trusted-request-claims-grant",
                "request-token-grant",
                "sso-request-token-grant",
                "partial-token-exchange",
                "notarization",
                "actor-token-grant",
                "partial-token-exchange"
            ],
            "subject_types_supported": [
                "public"
            ],
            "id_token_signing_alg_values_supported": [
                "RS256"
            ],
            "code_challenge_methods_supported": [
                "plain",
                "S256"
            ],
            "token_endpoint_auth_methods_supported": [
                "client_secret_post",
                "client_secret_basic"
            ]
        })
    return app
