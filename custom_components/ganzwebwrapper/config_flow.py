"""Adds config flow for GanzWeb Wrapper."""
from __future__ import annotations

import voluptuous as vol
from homeassistant import config_entries

from .const import DOMAIN, LOGGER


class GanzwebwrapperConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for GanzWeb Wrapper."""

    VERSION = 1

    errors = {}
    async def async_step_user(self, user_input: dict | None = None) -> config_entries.FlowResult:
        """Handle a flow initialized by the user."""

        if user_input is not None:
            pass

        return self.async_show_form(
            step_id="user", data_schema=vol.Schema({("host"): str}), errors=errors
        )