let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-unstable";
  pkgs = import nixpkgs { config = {}; overlays = []; };
in
pkgs.mkShell {
  packages = with pkgs; [
    pulumi-bin
    pkgs.python3
    pulumi-esc
    # pulumi
    # pulumiPackages.pulumi-language-python
    # python311Packages.pulumi
    # (import ./nixpkgs/pulumi-esc.nix { inherit (pkgs) lib buildGoModule fetchFromGitHub; }) #pulumi-esc
  ];
}




