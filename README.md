My Tailnet ACLs managed with Pulumi.  
First real attempt with Pulumi iac, mostly using it to learn.

## nix devShell setup

* install nix (with flakes enabled):
    * `curl -sSf -L https://install.lix.systems/lix | sh -s -- install`  
* Then run `nix develop` in the directory.

The flake is pinned to nixos-stable and should pull the most recent updates each time you run `nix flake update`.  
Pulumi esc is now merged! [pull request](https://github.com/NixOS/nixpkgs/pull/316044)  
The nix dev shell isn't complete, it seems to have issues with the Python pulumi_tailscale provider package.  
When you run pulumi, it does appear to use the pulumi_tailscale provider from the pulumi-bin package, but it still seems to think it has to install the provider with pip. So I can't fully get rid of the requirements.txt file.  

## Pulumi
I am using [Pulumi ESC](https://github.com/pulumi/esc) to manage secrets. 
Currently, it just holds the Tailscale usernames and the Tailscale oauth keys.

## Tailscale ACL

For the Tailscale ACLs themselves, I've split them into a few modules to organize things, and in a couple of them I've tried programmatically generating the ACLs. Specifically the moonlight and mulvad submodules.