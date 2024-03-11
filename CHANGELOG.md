# Changelog

## [0.3.1](https://github.com/christian-hawk/flask-oidc-client-poc/compare/v0.3.0...v0.3.1) (2024-03-11)


### Bug Fixes

* **logs:** send logs to stdout ([09faf9b](https://github.com/christian-hawk/flask-oidc-client-poc/commit/09faf9b1f95d74ad85809bf24520c44a1f004920))
* **security:** hardcoded secret_key ([b248eff](https://github.com/christian-hawk/flask-oidc-client-poc/commit/b248eff565633e64b084fbba877062309c748ef2))

## [0.3.0](https://github.com/christian-hawk/flask-oidc-client-poc/compare/v0.2.0...v0.3.0) (2024-03-02)


### Features

* **logging:** setup logging with defaults ([#15](https://github.com/christian-hawk/flask-oidc-client-poc/issues/15)) ([b435920](https://github.com/christian-hawk/flask-oidc-client-poc/commit/b435920ad3da95c99a00cd8d8e200ef639f78346))
* **settings:** load settings from `config.py` file ([#13](https://github.com/christian-hawk/flask-oidc-client-poc/issues/13)) ([9328d27](https://github.com/christian-hawk/flask-oidc-client-poc/commit/9328d276b34b00d5fca619636a287e9771dd17aa))

## [0.2.0](https://github.com/christian-hawk/flask-oidc-client-poc/compare/v0.1.0...v0.2.0) (2024-02-02)


### Features

* **clear_auth_session:** calls session.pop correctly ([93c79ac](https://github.com/christian-hawk/flask-oidc-client-poc/commit/93c79acc18cf6aa1eec393578d31f70b2d4545b8))
* **clear_auth_session:** is callable ([07b8e10](https://github.com/christian-hawk/flask-oidc-client-poc/commit/07b8e1093a96a35726d92b065b559f19fb73f1d8))
* **get_token_hint:** is callable ([c5a1543](https://github.com/christian-hawk/flask-oidc-client-poc/commit/c5a15431c7b903ba7d4bcf0daa8455885e90f4e8))
* **get_token_hint:** return id_token ([236e44b](https://github.com/christian-hawk/flask-oidc-client-poc/commit/236e44b474be320e23ed411657c5ec964ff2579e))
* **is_auth_session:** is callable ([af493ee](https://github.com/christian-hawk/flask-oidc-client-poc/commit/af493eef90620471d8b85003646734c7e3698729))
* **is_auth_session:** return false ([491ae29](https://github.com/christian-hawk/flask-oidc-client-poc/commit/491ae294cb954b249a10d616d75707ecfce4620c))
* **is_auth_session:** return True if session is authn ([49fb2a3](https://github.com/christian-hawk/flask-oidc-client-poc/commit/49fb2a38a512dcb714800579a002eb6b4859e84e))
* **logout:** add logout link in index ([852799a](https://github.com/christian-hawk/flask-oidc-client-poc/commit/852799af7b1ee250f060d6b74b068f30074c6a3c))
* **logout:** add urls to config ([4f716e5](https://github.com/christian-hawk/flask-oidc-client-poc/commit/4f716e5b012394ee5c13f93e0d619ea71c759b29))
* **logout:** clear session ([0c41c7b](https://github.com/christian-hawk/flask-oidc-client-poc/commit/0c41c7b5d7751dbd9b68c6279d00ded72f36ea22))
* **logout:** clear session if auth session ([c9d1cfc](https://github.com/christian-hawk/flask-oidc-client-poc/commit/c9d1cfcc4a91f18bbb3f8f0e4d241ae96dd743d4))
* **logout:** ensure is_authenticated is called ([491c28e](https://github.com/christian-hawk/flask-oidc-client-poc/commit/491c28eaedd74e0f6d64c5e292bf14f25a96de4a))
* **logout:** not get token_hint for unauth session ([2492baa](https://github.com/christian-hawk/flask-oidc-client-poc/commit/2492baa6e80ca07dcd76e554c55eb2c2506b9159))
* **logout:** redirect to end_session with params ([1d71560](https://github.com/christian-hawk/flask-oidc-client-poc/commit/1d715604e76c85920f6b7c2e2e3e8f866b1cffe6))
* **logout:** redirect to index if no auth session ([3a0952d](https://github.com/christian-hawk/flask-oidc-client-poc/commit/3a0952d3f7955723395b11f3480310ebfd04ab9e))
* s adderver runner ([a642d56](https://github.com/christian-hawk/flask-oidc-client-poc/commit/a642d5640e47bf6e85514c5cbb18151ab09c45fa))

## 0.1.0 (2024-01-31)


### Features

* **app-factory:** client factory first commit ([8c7cc59](https://github.com/christian-hawk/flask-oidc-client-poc/commit/8c7cc596d4cde161a7b5ef2c4c52bbdb3abf5e74))
* **templates:** add index template ([fba2f4a](https://github.com/christian-hawk/flask-oidc-client-poc/commit/fba2f4a52d303aac8b508177feb12ae2ac4e7e83))
