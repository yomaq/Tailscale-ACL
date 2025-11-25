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
    ],
}
tags_groups = {
    # Create tags
    "tagOwners": {
        # owner tags
        "tag:container": [],
        "tag:ephemeralSshOwner": [],
        # generic tags
        "tag:ssh": [],
        "tag:pingall": [],
        "tag:AcceptSSH": ["tag:ephemeralSshOwner", "autogroup:admin"],
        "tag:lockdown": ["tag:container", "autogroup:admin"],
        "tag:generichttp": ["tag:container", "autogroup:admin"],
        "tag:acceptGuestHttps": [],
        "tag:smb": [],
        "tag:service": [],
        "tag:adminservice": [],
        "tag:hostserver": [],
        # core server tags
        "tag:syncoidServer": [],
        "tag:syncoidClient": [],
        "tag:pikvm": [],
        "tag:homepage": [],
        "tag:glances": [],
        "tag:ntfy": [],
        "tag:tsidp-client": [],
        "tag:tsidp-server": [],
        # server tags
        "tag:sunshine": [],
        "tag:teslamate": ["tag:container", "autogroup:admin"],
        "tag:rustdesk": [],
        "tag:windowsindocker": ["tag:container", "autogroup:admin"],
        "tag:ollama-server": ["tag:container", "autogroup:admin"],
        "tag:ollama-access": ["tag:container", "autogroup:admin"],
        "tag:speaches": ["tag:container", "autogroup:admin"],
        # game servers
        "tag:valheim": ["tag:container", "autogroup:admin"],
        "tag:satisfactory": ["tag:container", "autogroup:admin"],
        "tag:factorio": ["tag:container", "autogroup:admin"],
        "tag:palworld": ["tag:container", "autogroup:admin"],
        "tag:minecraft": ["tag:container", "autogroup:admin"],
    },
    # Groups of users.
    "groups": {
        "group:admins": [user1, user2],
        "group:games": [user1, user2, user3],
        "group:services": [user1, user2, user3],
        "group:ollama": [user1, user2],
    },
    # ipsets, groups of computers
    "ipsets": generate_ipsets(create_ipsets)
}
