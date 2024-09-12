import pulumi
import pulumi_tailscale as tailscale
import json
from acl_modules.main_acl import main_acl
from acl_modules.mulvad import mulvad_access
from acl_modules.ssh import ssh_rules
from acl_modules.tags_groups import tags_groups
from acl_modules.moonlight import user_moonlight_access

# DNS configuration
dns_preferences = tailscale.DnsPreferences("tailnet-dns-preferences", magic_dns=True)

# List all acl modules
acl_modules = [ 
    main_acl,
    mulvad_access,
    user_moonlight_access,
    ssh_rules,
    tags_groups,
]
# define merge function
def merge_dicts(dict1, dict2):
    for key in dict2:
        if key in dict1:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                merge_dicts(dict1[key], dict2[key])
            elif isinstance(dict1[key], list) and isinstance(dict2[key], list):
                dict1[key].extend(dict2[key])
            else:
                dict1[key] = dict2[key]
        else:
            dict1[key] = dict2[key]
# Merge acl_modules into acl_rules
acl_rules = {}
for rules in acl_modules:
    merge_dicts(acl_rules, rules)


### Assemble configuration

# Convert the dictionary to a JSON string
acl_json = json.dumps(acl_rules, indent=4)
# Create the ACL resource
acl = tailscale.Acl("tailnet-acl", acl=acl_json)