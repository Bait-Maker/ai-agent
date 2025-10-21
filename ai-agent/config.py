from configparser import ConfigParser

config = ConfigParser()

config["FILE"] = {
    "MAX_CHARS": 10000,
}

with open("file_config.ini", "w") as f:
    config.write(f)

    