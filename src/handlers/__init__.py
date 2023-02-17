from .client import main_menu
from .admin import main_menu
from .admin.distribution import register_distribution
from .admin.stat import register_stat
from .backwards import register_back


def register_handlers(dp):
    client.main_menu.register_client_main_menu(dp)
    admin.main_menu.register_admin_panel(dp)
    backwards.register_back(dp)
    admin.distribution.register_distribution(dp)
    admin.stat.register_stat(dp)
