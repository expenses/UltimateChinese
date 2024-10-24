{
  description = "Flake utils demo";

  inputs.flake-utils.url = "github:numtide/flake-utils";
  inputs.hsk-3-0 = {
    url = "github:krmanik/HSK-3.0";
    flake = false;
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
    hsk-3-0
  }:
    flake-utils.lib.eachDefaultSystem (
      system: let
        pkgs = nixpkgs.legacyPackages.${system};
      in
        with pkgs; {
          devShells.anki-editing = mkShell {
            buildInputs = [
              (python3.withPackages (ps: [
                (ps.toPythonModule anki)
                ps.ipython ps.pypinyin ps.jieba
              ]))
            ];
          };
          packages = {
            default = "${hsk-3-0}/README.md";
          };
        }
    );
}
