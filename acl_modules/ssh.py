ssh_rules = {
    "ssh": [
        {
            "action": "check",
            "src": ["group:admins"],
            "dst": ["tag:ssh"],
            "users": ["autogroup:nonroot"],
            "checkPeriod": "20h",
        },
        {
            "action": "check",
            "src": ["group:admins"],
            "dst": ["tag:container"],
            "users": ["root", "autogroup:nonroot"],
            "checkPeriod": "20h",
        },
        {
            "action": "check",
            "src": ["autogroup:member"],
            "dst": ["autogroup:self"],
            "users": ["autogroup:nonroot"],
            "checkPeriod": "20h",
        },
        {
            "action": "accept",
            "src": ["tag:syncoidServer"],
            "dst": ["tag:syncoidClient"],
            "users": ["syncoid"],
        },
        {
            "action": "accept",
            "src": ["group:admins"],
            "dst": ["tag:AcceptSSH"],
            "users": ["root", "autogroup:nonroot"],
        },
    ],
    "acls": [
        {
            "action": "accept",
            "src": ["group:admins"],
            "dst": ["*:22"],
        },
        {
            "action": "accept",
            "src": ["tag:semaphoreserver"],
            "dst": ["tag:semaphoreclient:22"],
        },
        {
            "action": "accept",
            "src": ["tag:syncoidServer"],
            "dst": ["tag:syncoidClient:22"],
        },
    ],
}