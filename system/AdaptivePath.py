import pathlib
import configparser
import os

root = os.path.dirname(os.path.abspath(__file__))
config = configparser.ConfigParser()
path = pathlib.Path(root)
path = path/"user_data"/"test"/"models"
for model_dir in path.iterdir():
    model_config = model_dir/"config.ini"
    config.read(model_config, encoding="utf-8")
    for p in config["PATHS"]:
        config.set("PATHS", p, str(pathlib.Path(root/model_dir/config["PATHS"][p].split("\\")[-1])))
    config.write(open(model_config, "w"))
