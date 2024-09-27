import pulumi

conf = pulumi.Config()
user1 = conf.get("user1")
user2 = conf.get("user2")
user3 = conf.get("user3")

tags_groups = {
    # Create tags
    "tagOwners": {
        "tag:sunshine": [],
        "tag:dnsServer": [],
        "tag:minecraft": ["tag:container", "autogroup:admin"],
        "tag:ssh": [],
        "tag:pingall": [],
        "tag:syncoidServer": [],
        "tag:syncoidClient": [],
        "tag:container": [],
        "tag:nextcloud": ["tag:container", "autogroup:admin"],
        "tag:pikvm": [],
        "tag:valheim": ["tag:container", "autogroup:admin"],
        "tag:satisfactory": ["tag:container", "autogroup:admin"],
        "tag:palworld": ["tag:container", "autogroup:admin"],
        "tag:ephemeralSshOwner": [],
        "tag:AcceptSSH": ["tag:ephemeralSshOwner", "autogroup:admin"],
        "tag:homepage": [],
        "tag:lockdown": ["tag:container", "autogroup:admin"],
        "tag:teslamate": ["tag:container", "autogroup:admin"],
        "tag:generichttps": ["tag:container", "autogroup:admin"],
        "tag:glances": [],
        "tag:collabora": [],
        "tag:ntfy": [],
        "tag:semaphoreserver": [],
        "tag:semaphoreclient": [],
        "tag:windowsindocker": ["tag:container", "autogroup:admin"],
    },
    # Groups of users.
    "groups": {
        "group:admins": [user1, user2],
        "group:moonlight": [user1, user2, user3],
        "group:minecraft": [user1, user2, user3],
        "group:valhiem": [user1, user2],
        "group:satisfactory": [user1, user2, user3],
        "group:palworld": [user1, user2],
        "group:nextcloud": [user1, user2, user3],
    },
}