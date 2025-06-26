import pulumi
import pulumi_tailscale as tailscale

conf = pulumi.Config()
user1 = conf.get("user1")
user2 = conf.get("user2")
user3 = conf.get("user3")

def get_tailscale_ip(hostname):
    device = tailscale.get_device(hostname=hostname)
    return device.addresses[0]

def generate_ipsets(create_ipsets):
    updated_ipsets = {}
    for name, entries in create_ipsets.items():
        updated_entries = []
        for entry in entries:
            if entry.startswith("add host:"):
                hostname = entry.split(":")[1].strip()
                ip_address = get_tailscale_ip(hostname)
                updated_entries.append(f"add {ip_address}")
            else:
                updated_entries.append(entry)
        updated_ipsets[name] = updated_entries
    return updated_ipsets



create_ipsets = {
    "ipset:personal-nix": [
        "add host:wsl",
    ],
}
tags_groups = {
    # Create tags
    "tagOwners": {
        "tag:sunshine": [],
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
        "tag:factorio": ["tag:container", "autogroup:admin"],
        "tag:palworld": ["tag:container", "autogroup:admin"],
        "tag:ephemeralSshOwner": [],
        "tag:AcceptSSH": ["tag:ephemeralSshOwner", "autogroup:admin"],
        "tag:homepage": [],
        "tag:lockdown": ["tag:container", "autogroup:admin"],
        "tag:teslamate": ["tag:container", "autogroup:admin"],
        "tag:generichttps": ["tag:container", "autogroup:admin"],
        "tag:glances": [],
        "tag:collabora": [],
        "tag:audiobookshelf": [],
        "tag:smb": [],
        "tag:ntfy": [],
        "tag:acceptAllHttps": [],
        "tag:acceptGuestHttps": [],
        "tag:semaphoreserver": [],
        "tag:semaphoreclient": [],
        "tag:rustdesk": [],
        "tag:windowsindocker": ["tag:container", "autogroup:admin"],
        "tag:ollama-server": ["tag:container", "autogroup:admin"],
        "tag:ollama-access": ["tag:container", "autogroup:admin"],
        "tag:speaches": ["tag:container", "autogroup:admin"],
    },
    # Groups of users.
    "groups": {
        "group:admins": [user1, user2],
        "group:moonlight": [user1, user2, user3],
        "group:minecraft": [user1, user2, user3],
        "group:valhiem": [user1, user2],
        "group:satisfactory": [user1, user2, user3],
        "group:factorio": [user1, user2, user3],
        "group:palworld": [user1, user2],
        "group:nextcloud": [user1, user2, user3],
        "group:ollama": [user1, user2, user3],
        "group:audiobookshelf": [ user3 ],
    },
    # ipsets, groups of computers
    "ipsets": generate_ipsets(create_ipsets)
}
