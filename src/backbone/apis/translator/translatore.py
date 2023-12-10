import json
import os
from pathlib import Path

current_dir = os.path.dirname(__file__)
root_path_ = Path(current_dir).parent.parent.absolute()


def _get_lan(type, lan='fa'):
    json_load = json.loads(Path(root_path_.joinpath(f'apis/translator/phrases/{type}/{lan}.json')).read_text(
        encoding="utf-8"))
    return json_load


def translate(*, phrase, type, lan='fa'):
    lan = _get_lan(type, lan=lan)
    return lan[phrase]
