import json
import logging
from datetime import datetime, timedelta

import requests

UPDATEHOUR = 12
RESETHOUR = 3
NAME = "naam"
VALUE = "waarde"
_LOGGER = logging.getLogger(__name__)

class stookalert(object):

    def __init__(self, province):
        self._state = None
        self._alerts = {}
        self._province = province.lower()
        self._last_updated = None

        if self._province is not None: 
            _LOGGER.info(f"Setting up Stookalert for province {province}")
        else:
            _LOGGER.info("Please provide a province name")
    
    @property
    def state(self):
        return self._state

    @property
    def last_updated(self):
        return self._last_updated

    def get_alerts(self):
        alerts = self.request()
        
        if alerts is None:
            return

        for a in alerts:
            province = a.get(NAME, "").lower()
            value = a.get(VALUE, None)

            self._alerts[province] = value

            if province == self._province:
                self._state = value

    def request(self):
        try:            
            response = requests.get(self.get_url(), timeout=10)
            
            self._last_updated = datetime.now()
            json_response = json.loads(response.text)

            return sorted(json_response, key = lambda i: i[NAME]) 
        except requests.exceptions.RequestException:
            _LOGGER.error("Error getting Stookalert data")

    def get_url(self):
        updateDay = datetime.now()

        if updateDay.hour < RESETHOUR:
            updateDay = updateDay - timedelta(days=1)
        elif updateDay.hour < UPDATEHOUR:
            return f"https://www.rivm.nl/media/lml/stookalert/stookalert_noalert.json"

        return f"https://www.rivm.nl/media/lml/stookalert/stookalert_{updateDay.strftime('%Y%m%d')}.json"
