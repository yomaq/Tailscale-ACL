{
  description = "Development environment with Pulumi";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-25.11";
  };

  outputs = { self, nixpkgs }:
    let
      systems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
      
      forAllSystems = f: builtins.listToAttrs (map (system: { name = system; value = f system; }) systems);
      
      packagesFor = system: import nixpkgs {
        inherit system;
        config = {};
        overlays = [];
      };
    in
    {
      devShells = forAllSystems (system:
        let
          pkgs = packagesFor system;
        in
        {
          default = pkgs.mkShell {
            packages = with pkgs; [
              pulumi-bin
                (pkgs.python3.withPackages (python-pkgs: [
                    python313Packages.pulumi
                ]))
              pulumi
              pulumi-esc
            ];
          };
        }
      );
    };
}