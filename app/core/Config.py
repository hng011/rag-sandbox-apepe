import yaml
from pathlib import Path
import os
import json
import re

class Config:
    def __init__(self, env_type: str):
        self.__config_file=env_type
     
    def get_env(self) -> dict:            
        with open(Path(__file__).parent.parent.parent / "config" / f"{self.__config_file}.yaml") as r:
            config = json.dumps(yaml.safe_load(r), indent=4)
            
            # regex helper
            expr = r"\$\{(.+?)\}"
            
            # find
            matches = re.findall(expr, config)
            
            # substitute
            for match in matches:
                config = re.sub(r"\$\{%s\}" % match, os.getenv(match), config)
                
            config = json.loads(config) 
            if isinstance(config, dict):
                return config
            else:
                raise TypeError("config prop is not a dict, false thinking")