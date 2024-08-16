{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    devenv.url = "github:cachix/devenv";
  };

#   nixConfig = {
#     extra-trusted-public-keys = "devenv.cachix.org-1:w1cLUi8dv3hnoSPGAuibQv+f9TZLr6cv/Hm9XgU50cw=";
#     extra-substituters = "https://devenv.cachix.org";
#   };

  outputs = { self, nixpkgs, devenv, ... } @ inputs:
    let
        system = "x86_64-linux";
        pkgs = nixpkgs.legacyPackages.${system};
    in
    {
        packages.${system}.devenv-up = self.devShells.${system}.default.config.procfileScript;
        devShells.${system}.default = devenv.lib.mkShell {
        inherit inputs pkgs;
            modules = [
                ({ pkgs, config, ... }: {
                packages = with pkgs; [ 
                    pulumi-bin
                    pkgs.python3
                    pulumi-esc
                ];
                enterShell = ''
                    Tailscale ACL
                '';
                })
            ];
        };
    };
}