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
        # Glances
        {
            "action": "accept",
            "src": ["group:admins", "tag:homepage"],
            "proto": "tcp",
            "dst": ["tag:glances:61208", "tag:glances:8787", "ipset:personal-nix:61208", "ipset:personal-nix:8787", "tag:hostserver:61208", "tag:hostserver:8787"],
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
            "dst": ["autogroup:self:443", "autogroup:self:80", "autogroup:self:18000", "autogroup:self:12525"]
        },
        # homepage
        {
            "action": "accept",
            "src": ["group:admins", "tag:homepage"],
            "dst": ["tag:service:443", "tag:adminservice:443"],
        },
        # ntfy
        {
            "action": "accept",
            "src": ["tag:service", "tag:adminservice", "tag:hostserver", "group:admins"],
            "dst": ["tag:ntfy:443"],
        },
        # generichttp
        {
            "action": "accept",
            "src": ["group:admins"],
            "dst": ["tag:generichttp:80"],
        },
        # services https
        {
            "action": "accept",
            "src": ["group:services", "tag:service"],
            "dst": ["tag:service:443"],
        },
        # services https
        {
            "action": "accept",
            "src": ["group:admins"],
            "dst": ["tag:adminservice:443"],
        },
        # accept guest https
        {
            "action": "accept",
            "src": ["autogroup:shared"],
            "dst": ["tag:acceptGuestHttps:443"],
        },
        # ollama
        {
            "action": "accept",
            "src": ["tag:ollama-access", "group:ollama", "tag:homepage", "tag:hostserver"],
            "dst": [ "tag:ollama-server:443"],
        },
        # speaches
        {
            "action": "accept",
            "src": [ "tag:ollama-server", "group:admins", ],
            "dst": [ "tag:speaches:8880" ],
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
            "src": ["group:games", "autogroup:shared", "tag:sunshine", "tag:homepage"],
            "dst": ["tag:minecraft:19132"],
        },
        # valhiem
        {
            "action": "accept",
            "src": ["group:games", "autogroup:shared", "tag:sunshine"],
            "dst": ["tag:valheim:2456", "tag:valheim:2457"],
        },
        # palworld
        {
            "action": "accept",
            "src": ["group:games", "autogroup:shared", "tag:sunshine"],
            "dst": ["tag:palworld:8211"],
        },
        # satisfactory
        {
            "action": "accept",
            "src": ["group:games", "autogroup:shared", "tag:sunshine"],
            "dst": ["tag:satisfactory:7777"],
        },
        # factorio
        {
            "action": "accept",
            "src": ["group:games", "autogroup:shared", "autogroup:admin", "tag:sunshine"],
            "dst": ["tag:factorio:34197","tag:factorio:443"],
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
            "target": ["target:hostserver"],
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
        # tsidp grants
        {
            "src": ["group:admins"],
            "dst": ["tag:tsidp-server"],
            "app": {
                "tailscale.com/cap/tsidp": [
                    {
                    "allow_admin_ui": True,
                    }
                ]
            }
        },
        {
            "src": ["tag:tsidp-client"],
            "dst": ["tag:tsidp-server"],
            "app": {
                "tailscale.com/cap/tsidp": [
                    {
                    "allow_dcr": True,
                    }
                ]
            }
        },
        # generic admin for in tsidp
        {
            "src": ["group:admins"],
            "dst": ["*"],
            "app": {
            "tailscale.com/cap/tsidp": [
                {
                "extraClaims": {
                    "groups": ["admin"]
                },
                "includeInUserInfo": True
                }
            ]
            }
        }
    ]
}