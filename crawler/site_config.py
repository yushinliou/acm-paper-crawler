from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class SiteConfig:
    csv: str
    title: str
    href: str
    download_dir: str
    parser: str  # parser name (string)
    headers: Optional[Dict[str, str]] = None
    requires_login: bool = False
    sleep_min: int = 5
    sleep_max: int = 10
