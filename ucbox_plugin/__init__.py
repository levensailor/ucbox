from extras.plugins import PluginConfig


class UCBoxConfig(PluginConfig):
    name = 'ucbox_plugin'
    verbose_name = 'UCBox Plugin'
    description = 'Unified Communications Management Plugin for NetBox.'
    version = 'v0.0.22'
    author = 'Jeff Levensailor'
    author_email = 'jeff@levensailor.com'
    base_url = 'ucbox'
    min_version = "2.11.0"
    required_settings = []
    default_settings = {}
    caching_config = {
        '*': None
    }

config = UCBoxConfig
