import json
import re
from lomond.persist import persist
from HQApi import HQApi, HQWebSocket

api = HQApi(proxy="https://163.172.220.221:8888")
ws = HQWebSocket(api, demo=True, proxy="https://163.172.220.221:8888")
websocket = ws.get()

for msg in persist(websocket):
    if msg.name == "text":
        data = json.loads(re.sub(r"[\x00-\x1f\x7f-\x9f]", "", msg.text))
        if data["type"] != "interaction":
            exit()