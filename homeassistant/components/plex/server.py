"""Shared class to maintain Plex server instances."""
import logging

import plexapi.server
from requests import Session

from homeassistant.const import CONF_TOKEN, CONF_URL, CONF_VERIFY_SSL

from .const import DEFAULT_VERIFY_SSL

_LOGGER = logging.getLogger(__package__)


class PlexServer:
    """Manages a single Plex server connection."""

    def __init__(self, server_config):
        """Initialize a Plex server instance."""
        self._plex_server = None
        self._url = server_config.get(CONF_URL)
        self._token = server_config.get(CONF_TOKEN)
        self._verify_ssl = server_config.get(CONF_VERIFY_SSL, DEFAULT_VERIFY_SSL)

    def connect(self):
        """Connect to a Plex server directly, obtaining direct URL if necessary."""

        def _connect_with_url():
            session = None
            if self._url.startswith("https") and not self._verify_ssl:
                session = Session()
                session.verify = False
            self._plex_server = plexapi.server.PlexServer(
                self._url, self._token, session
            )
            _LOGGER.debug("Connected to: %s (%s)", self.friendly_name, self.url_in_use)

        _connect_with_url()

    def clients(self):
        """Pass through clients call to plexapi."""
        return self._plex_server.clients()

    def sessions(self):
        """Pass through sessions call to plexapi."""
        return self._plex_server.sessions()

    @property
    def friendly_name(self):
        """Return name of connected Plex server."""
        return self._plex_server.friendlyName

    @property
    def machine_identifier(self):
        """Return unique identifier of connected Plex server."""
        return self._plex_server.machineIdentifier

    @property
    def url_in_use(self):
        """Return URL used for connected Plex server."""
        return self._plex_server._baseurl  # pylint: disable=W0212
