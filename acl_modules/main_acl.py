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
        # moonlight group can access sunshine servers through moonlight
        {
            "action": "accept",
            "src": ["group:moonlight", "autogroup:shared"],
            "dst": [
                "tag:sunshine:47984",
                "tag:sunshine:47989",
                "tag:sunshine:47990",
                "tag:sunshine:48010",
                "tag:sunshine:47998",
                "tag:sunshine:47999",
                "tag:sunshine:48000",
                "tag:sunshine:48002",
            ],
        },
        # dns server settings
        {
            "action": "accept",
            "src": ["*"],
            "proto": "tcp",
            "dst": ["tag:dnsServer:53"],
        },
        {
            "action": "accept",
            "src": ["*"],
            "proto": "udp",
            "dst": ["tag:dnsServer:53"],
        },
        {
            "action": "accept",
            "src": ["group:admins", "tag:homepage"],
            "proto": "tcp",
            "dst": ["tag:dnsServer:80"],
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
            "dst": ["tag:glances:61208", "tag:glances:8787"],
        },
        # Windows Docker Server
        {
            "action": "accept",
            "src": ["group:admins"],
            "dst": ["tag:windowsindocker:443", "tag:windowsindocker:3389"],
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
            "dst": ["group:admins:443", "group:admins:80", "group:admins:4000"],
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
            "dst": ["tag:pikvm:443"],
        },
        # exit node access
        {
            "action": "accept",
            "src": ["group:admins", "autogroup:shared"],
            "dst": ["autogroup:internet:*"],
        },
    ],
}