import pulumi_tailscale as tailscale


# mulvad access
hostnames = [
    "gray",
    "midnight",
    "blue",
    "beam",
]

# Obtain the tailnet name
devices = tailscale.get_devices()
if devices and devices.devices:
    first_device = devices.devices[0]
    tailnet_name = first_device.name.split('.')[1]
else:
    raise ValueError("No devices found in the tailnet")

mulvad_access = {"nodeAttrs": []}
for hostname in hostnames:
    # iOS devices hostname's don't list properly, so we use the full tailnet name instead.
    full_hostname = f"{hostname}.{tailnet_name}.ts.net"
    device = tailscale.get_device(name=full_hostname)
    ip_address = device.addresses[0]  
    mulvad_access["nodeAttrs"].append({"target": [ip_address], "attr": ["mullvad"]})