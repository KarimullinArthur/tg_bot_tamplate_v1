from .client import main_menu
from .admin import main_menu
from .admin.distribution import register_distribution
from .admin.additional_funcs import register_additional_funcs
from .admin.referral_links import register_refferal_links
from .admin.texts_management import register_text_management
from .admin.sponsors import register_sponsors
from .admin.admins_management import register_admins_management
from .backwards import register_back


def register_handlers(dp):
    client.main_menu.register_client_main_menu(dp)
    admin.main_menu.register_admin_panel(dp)
    backwards.register_back(dp)
    admin.distribution.register_distribution(dp)
    admin.additional_funcs.register_additional_funcs(dp)
    admin.referral_links.register_refferal_links(dp)
    admin.texts_management.register_text_management(dp)
    admin.sponsors.register_sponsors(dp)
    admin.admins_management.register_admins_management(dp)
