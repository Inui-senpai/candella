#
# CAPermissions.rpy
# Candella
#
# Created by Marquis Kurt on 1/14/21.
# Copyright © 2021 ProjectAliceDev. All rights reserved.
#

init offset = -1000

init python:
    class CAPermission():
        """A data class that represents a permission for a Candella application."""
        key = "DEFAULT_PERM"
        name = "Стандартное разрешение"
        description = "Стандартное разрешение."
        default_state = False

        def __init__(self, key, name, description, default=False):
            self.key = key
            self.name = name
            self.description = description
            self.default = default

        def __eq__(self, other):
            return isistance(other, CAPermission) and self.key == other.key

        def __ne__(self, other):
            return not self.__eq__(other)

    # This dictionary contains the current system permissions, including the default AliceOS permissions. Apps that
    # use CAApplication instead of ASAppRepresentative can leverage these permission objects by specifying the
    # permissions needed for the app in the 'permissions' field of the app manifest.

    CA_PERMISSIONS = {
        "notifications": CAPermission(
            "REQ_NOTIFICATIONKIT",
            _("Отправлять уведомления"),
            _("Уведомления могут включать в себя баннеры, предупреждения и звуки. Это можно настроить в Менеджере приложений.")
        ),
        "file_system": CAPermission(
            "REQ_FULL_DISK",
            _("Доступ к файловой системе"),
            _("Доступ к файлам включает в себя файл пользовательской конфигурации и может также включать в себя другие файлы, присутствующие в системе Candella. Это"
                + " можно настроить в Менеджере приложений.")
        ),
        "system_events": CAPermission(
            "REQ_SYSTEM_EVENTS",
            _("Управлять системными событиями"),
            _("Системные события включают в себя вход в систему, завершение работы и смену пользователя. Это можно настроить в Менеджере приложений.")
        ),
        "manage_users": CAPermission(
            "REQ_USERS_MANAGEMENT",
            _("Управлять пользователями"),
            _("Управление пользователями включает в себя добавление, изменение и удаление пользователей. Это можно настроить в Менеджере приложений.")
        ),
        "virtual_platform": CAPermission(
            "REQ_METEORVM",
            _("Запускать приложения в виртуальном окружении"),
            _("Это приложение запускает дополнительный код на платформе Meteor VM. Это можно настроить в Менеджере приложений.")
        ),

    }
