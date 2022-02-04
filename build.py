#!/usr/bin/env python3
#
import sys
import json

NEW_VERSION = sys.argv[1]


def main() -> None:
    with open("mods.json") as build_file:
        build_data = json.load(build_file)

    modpack_info = {
        "name": "anentiresleeve-pack",
        "version": NEW_VERSION,
        "title": "AnEntireSleeve Modpack",
        "author": "AnEntireSleeve",
        "description": "ModPack with the mods I use and recommend."
        " Mostly UI enhancements and quality of life.",
        "homepage": "https://github.com/rpdelaney/factorio-modpack",
        "factorio_version": "1.1",
        "dependencies": [],
    }

    for mod in build_data:
        modpack_info["dependencies"].append(
            f"{mod['name']} {mod['constraint']} {mod['version']}"
        )

    with open("anentiresleeve-pack/info.json", "w") as info_file:
        info_file.write(json.dumps(modpack_info, indent=4) + "\n")


if __name__ == "__main__":
    main()

# EOF
