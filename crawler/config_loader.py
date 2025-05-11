import yaml
from crawler.site_config import SiteConfig
from crawler.utils import CONFIG_PATH
from typing import Dict

def load_site_configs(yaml_path=CONFIG_PATH) -> Dict[str, SiteConfig]:
    """
    Load site configurations from a YAML file.
    Args:
        yaml_path (str): Path to the YAML configuration file.
    Returns:
        Dict[str, SiteConfig]: A dictionary mapping filenames to SiteConfig objects.
    """
    with open(yaml_path, 'r') as f:
        raw_data = yaml.safe_load(f)
    
    config_dict = {}
    for filename, cfg in raw_data.items():
        config_dict[filename] = SiteConfig(**cfg)
    return config_dict
