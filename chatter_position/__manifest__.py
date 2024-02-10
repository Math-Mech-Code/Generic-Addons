{
    "name": "Chatter Position",
    "summary": "Chatter Position",
    "version": "15.0.1.0.1",
    "author": "Tanay Goyal",
    "website": "",
    "license": "LGPL-3",
    "category": "Extra Tools",
    "images": ["static/description/images/chatter_position.png"],
    "support": "",
    "depends": ["web", "mail"],
    "data": ["views/res_users.xml", "views/web.xml"],
    "assets": {
        "web.assets_backend": [
            "/chatter_position/static/src/scss/chatter_position.scss",
            "/chatter_position/static/src/scss/attachment_viewer.scss",
            "/chatter_position/static/src/js/form_chatter_position.js",
        ],
        "web.assets_qweb": [
            "/chatter_position/static/src/xml/form_buttons.xml",
        ],
    },
    "installable": True,
    "auto_install": False,
}
