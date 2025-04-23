main_acl = {
    "randomizeClientPort": True,
    # Set acls
    "acls": [
        # Allow Ping ALL
        {
            "action": "accept",
            "src": ["tag:homepage", "group:admins", "tag:pingall"],
            "proto": "icmp",
            "dst": ["*:*"],
        },
        # give nextcloud access to collabora
        {
            "action": "accept",
            "src": ["group:nextcloud", "tag:nextcloud"],
            "dst": ["tag:collabora:9980", "tag:collabora:443"],
        },
        {
            "action": "accept",
            "src": ["tag:collabora"],
            "dst": ["tag:nextcloud:443"],
        },
        # Glances
        {
            "action": "accept",
            "src": ["group:admins", "tag:homepage"],
            "proto": "tcp",
            "dst": ["tag:glances:61208", "tag:glances:8787", "ipset:personal-nix:61208", "ipset:personal-nix:8787"],
        },
        # Windows Docker Server
        {
            "action": "accept",
            "src": ["group:admins"],
            "dst": ["tag:windowsindocker:443", "tag:windowsindocker:3389"],
        },
        # SMB share
        {
            "action": "accept",
            "src": ["group:admins"],
            "dst": ["tag:smb:139", "tag:smb:445"],
        },
        # teslmate server
        {
            "action": "accept",
            "src": ["group:admins", "tag:homepage"],
            "dst": ["tag:teslamate:443"],
        },
        # codeserver
        {
            "action": "accept",
            "src": ["group:admins"],
            "dst": ["group:admins:443", "group:admins:80", "group:admins:4000", "group:admins:8000", "group:admins:18000"],
        },
        # homepage
        {
            "action": "accept",
            "src": ["group:admins", "tag:homepage"],
            "dst": ["tag:generichttps:443", "tag:nextcloud:443"],
        },
        # ntfy
        {
            "action": "accept",
            "src": ["*"],
            "dst": ["tag:ntfy:443"],
        },
        # accept all https
        {
            "action": "accept",
            "src": ["*"],
            "dst": ["tag:acceptAllHttps:443"],
        },
        # accept guest https
        {
            "action": "accept",
            "src": ["*"],
            "dst": ["tag:acceptGuestHttps:443"],
        },
        # ollama
        {
            "action": "accept",
            "src": ["tag:ollama-access", "group:ollama", "tag:homepage", "*",],
            "dst": [ "tag:ollama-server:443"],
        },
        # RuskDesk
        {
            "action": "accept",
            "src": ["group:admins"],
            "dst": [ "tag:rustdesk:21118"],
        },
        # minecraft server
        {
            "action": "accept",
            "src": ["group:minecraft", "autogroup:shared", "tag:sunshine", "tag:homepage"],
            "dst": ["tag:minecraft:19132"],
        },
        # valhiem
        {
            "action": "accept",
            "src": ["group:valhiem", "autogroup:shared", "tag:sunshine"],
            "dst": ["tag:valheim:2456", "tag:valheim:2457"],
        },
        # Allow https access to semaphore
        {
            "action": "accept",
            "src": ["group:admins", "tag:homepage"],
            "dst": ["tag:semaphoreserver:443"],
        },
        # palworld
        {
            "action": "accept",
            "src": ["group:palworld", "autogroup:shared", "tag:sunshine"],
            "dst": ["tag:palworld:8211"],
        },
        # satisfactory
        {
            "action": "accept",
            "src": ["group:satisfactory", "autogroup:shared", "tag:sunshine"],
            "dst": ["tag:satisfactory:7777"],
        },
        # factorio
        {
            "action": "accept",
            "src": ["group:satisfactory", "autogroup:shared", "autogroup:admin", "tag:sunshine"],
            "dst": ["tag:factorio:34197","tag:factorio:443"],
        },
        # nextcloud
        {
            "action": "accept",
            "src": ["group:nextcloud"],
            "dst": ["tag:nextcloud:443"],
        },
        # access to pikvm
        {
            "action": "accept",
            "src": ["group:admins"],
            "dst": ["tag:pikvm:443", "tag:pikvm:80"],
        },
        # exit node access
        {
            "action": "accept",
            "src": ["group:admins", "autogroup:shared"],
            "dst": ["autogroup:internet:*"],
        },
    ],
    "nodeAttrs": [
        {
            # Taildrive to share directories
            "target": ["*"],
            "attr": ["drive:share"],
        },
       {
            # Only admins can access directories
            "target": ["group:admins"],
            "attr": ["drive:access"],
        }
    ],
    "grants": [
        # allow self to read Taildrive from self
        {
            "src": ["autogroup:member"],
            "dst": ["autogroup:self"],
            "app": {
                "tailscale.com/cap/drive": [{
                    "shares": ["*"],
                    "access": "rw"
                }]
            }
        },
        # allow admins to access all shares
        {
            "src": ["group:admins"],
            "dst": ["*"],
            "app": {
                "tailscale.com/cap/drive": [{
                    "shares": ["*"],
                    "access": "rw"
                }]
            }
        },
    #     # AudioBookShelf tsidp groups (feature was only merged 5 days ago, not out yet)
    #     {
    #     "src": ["group:audiobookshelf", "autogroup:shared"],
    #     "dst": ["tag:audiobookshelf"],
    #     "ip":  ["*"],
    #     "app": {
    #         "tailscale.com/cap/tsidp": [
    #         {
    #             "extraClaims": {
    #             "groups": ["user"],
    #             },
    #         }
    #         ]
    #     }
    #     }
    ]
}