"""Routing push-button entities for MHUB (16 total)."""
from __future__ import annotations
from homeassistant.components.button import ButtonEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN, ROUTE_OUTPUTS, ROUTE_INPUTS

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    entities = []
    for inp in ROUTE_INPUTS:
        for out in ROUTE_OUTPUTS:
            entities.append(MHUBRouteButton(coordinator, inp, out))
    async_add_entities(entities, True)

class MHUBRouteButton(CoordinatorEntity, ButtonEntity):
    def __init__(self, coordinator, input_id: str, output_id: str):
        super().__init__(coordinator)
        self.input_id = input_id
        self.output_id = output_id
        self._attr_name = f"Route Input {input_id} → Output {output_id.upper()}"
        self._attr_unique_id = f"hda_mhub_btn_{input_id}_{output_id}"

    async def async_press(self) -> None:
        path = f"/api/control/switch/{self.output_id}/{self.input_id}/"
        await self.coordinator.async_request(path)
        await self.coordinator.async_refresh()
