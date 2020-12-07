{ pkgs ? import <nixpkgs> {} }:

pkgs.python3Packages.buildPythonApplication {
  pname = "flask-adapter";
  src = ./.;
  version = "0.2";
  propagatedBuildInputs = [ pkgs.python3Packages.flask pkgs.python3Packages.flask-cors ];
}