from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([MHUBPowerSwitch(coordinator)], True)

class MHUBPowerSwitch(CoordinatorEntity, SwitchEntity):
    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_name = "MHUB Power"
        self._attr_unique_id = "hda_mhub_power"

    @property
    def is_on(self):
        data = self.coordinator.data or {}
        state = str(data.get("power", "")).lower()
        return state in ["on", "1", "true"]

    async def async_turn_on(self, **kwargs):
        await self.coordinator.async_request("/api/power/1/")
        self.coordinator.data["power"] = True
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs):
        await self.coordinator.async_request("/api/power/0/")
        self.coordinator.data["power"] = False
        self.async_write_ha_state()
