async def async_setup_entry(hass: HomeAssistant, config: ConfigEntry) -> bool:
    """Set up the MyHOME component."""
    hass.data[DOMAIN] = {}

    if DOMAIN not in config:
        return True

    LOGGER.error("configuration.yaml not supported for this component!")

    return False