"""Coordinator for MHUB data polling and API calls."""
from __future__ import annotations
import logging
from datetime import timedelta
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.helpers import aiohttp_client
from .const import UPDATE_INTERVAL, DEFAULT_PORT

_LOGGER = logging.getLogger(__name__)

class MHUBDataUpdateCoordinator(DataUpdateCoordinator):
    """Manages data and API interaction with MHUB."""

    def __init__(self, hass: HomeAssistant, entry) -> None:
        self.hass = hass
        self.entry = entry
        self.host = entry.data.get("host")
        self.port = entry.data.get("port", DEFAULT_PORT)
        self.base_url = f"http://{self.host}:{self.port}"
        super().__init__(
            hass,
            _LOGGER,
            name="hda_mhub",
            update_interval=timedelta(seconds=UPDATE_INTERVAL),
        )

    async def _async_update_data(self):
        session = aiohttp_client.async_get_clientsession(self.hass)
        try:
            url = f"{self.base_url}/api/data/0/"
            async with session.get(url, timeout=10) as resp:
                data = await resp.json(content_type=None)
                return data.get("data", {})
        except Exception as err:
            raise UpdateFailed(f"Error communicating with MHUB: {err}") from err

    async def async_request(self, path: str):
        session = aiohttp_client.async_get_clientsession(self.hass)
        url = f"{self.base_url}{path}"
        try:
            async with session.get(url, timeout=10) as resp:
                return await resp.text()
        except Exception as err:
            _LOGGER.error("API request failed at %s: %s", url, err)
            raise UpdateFailed(err)
