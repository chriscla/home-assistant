"""Constants for the Plex component."""
DOMAIN = "plex"
NAME_FORMAT = "Plex {}"

DEFAULT_HOST = "localhost"
DEFAULT_PORT = 32400
DEFAULT_SSL = False
DEFAULT_VERIFY_SSL = True

PLATFORMS = ["media_player", "sensor"]
SERVERS = "servers"

PLEX_CONFIG_FILE = "plex.conf"
PLEX_MEDIA_PLAYER_OPTIONS = "plex_mp_options"
PLEX_SERVER_CONFIG = "server_config"

CONF_USE_EPISODE_ART = "use_episode_art"
CONF_SHOW_ALL_CONTROLS = "show_all_controls"
CONF_REMOVE_UNAVAILABLE_CLIENTS = "remove_unavailable_clients"
CONF_CLIENT_REMOVE_INTERVAL = "client_remove_interval"
