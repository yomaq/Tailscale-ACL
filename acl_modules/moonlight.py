import pulumi
import pulumi_tailscale as tailscale


conf = pulumi.Config()
user1 = conf.get("user1")
user2 = conf.get("user2")
user3 = conf.get("user3")

# List out users, and the ip addresses of the hosts they should be able to moonlight into without tags
moonlight_access = {
    user2: ["blue",],
    user3: ["purple",]
}

# Ports moonlight uses
MOONLIGHT_PORTS = [
    47984, 47989, 47990, 48010, 47998, 47999, 48000, 48002
]


user_moonlight_access  = {"acls": []}

for user, hostnames in moonlight_access.items():
    for hostname in hostnames:
        device = tailscale.get_device(hostname=hostname)
        ip_address = device.addresses[0] 
        user_moonlight_access["acls"].append({
            "action": "accept",
            "src": [user],
            "dst": [f"{ip_address}:{port}" for port in MOONLIGHT_PORTS],
        })
