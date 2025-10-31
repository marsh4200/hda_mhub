"""Config flow for HDA MHUB integration."""
from __future__ import annotations
import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN

DATA_SCHEMA = vol.Schema({
    vol.Required("host"): str,
    vol.Optional("port", default=80): int,
})

class MHUBConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_PUSH

    async def async_step_user(self, user_input=None):
        if user_input is None:
            return self.async_show_form(step_id="user", data_schema=DATA_SCHEMA)
        host = user_input["host"].strip()
        port = int(user_input.get("port", 80))
        return self.async_create_entry(title=f"MHUB ({host}:{port})", data={"host": host, "port": port})
