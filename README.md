My Tailnet ACLs managed with Pulumi.  
First real attempt with Pulumi iac, mostly using it to learn.

## nix direnv setup
 I'm using vscode-server running on a [nixos container](https://github.com/yomaq/nix-config/blob/main/modules/containers/nixos-containers/openvscode-server/nixos.nix) which handles the direnv setup etc, but it can be manually installed as well.

* [install nix](https://github.com/DeterminateSystems/nix-installer):
    * `curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | sh -s -- install`  
* [install direnv](https://github.com/nix-community/nix-direnv)  
* [enable direnv](https://direnv.net/docs/hook.html)  
* [install devenv](https://devenv.sh/getting-started/)
* Then run `direnv allow` in the git directory.

The flake is pinned to nixos-unstable and should pull the most recent updates each time you run `nix flake update`.  
Pulumi esc is now merged! [pull request](https://github.com/NixOS/nixpkgs/pull/316044)

The nix devenv isn't complete, it seems to have issues with the Python pulumi_tailscale provider package.
When you run pulumi, it does appear to use the pulumi_tailscale provider from the pulumi-bin package, but it still seems to think it has to install the provider with pip. So I can't fully get rid of the requirements.txt file.  
With direnv and devenv setup however, you can run `pulumi up` so long as you are in the git directory without needing to install anything project specific manually.

## Pulumi
I am using [Pulumi ESC](https://github.com/pulumi/esc) to manage secrets. 
Currently, it just holds the Tailscale usernames and the Tailscale oauth keys.

## Tailscale ACL

For the Tailscale ACLs themselves, I've split them into a few modules to organize things, and in a couple of them I've tried programmatically generating the ACLs. Specifically the moonlight and mulvad submodules.