#
# ASPermissionDefinitions.rpy
# Candella
#
# Created by Marquis Kurt on 1/14/21.
# Copyright © 2019-2021 ProjectAliceDev. All rights reserved.
#

init offset = -1000

# MARK: OS permissions definitions

define AS_REQUIRES_NOTIFICATIONKIT = "REQ_NOTIFICATIONKIT"
define AS_REQUIRES_FULL_DISK_ACCESS = "REQ_FULL_DISK"
define AS_REQUIRES_SYSTEM_EVENTS = "REQ_SYSTEM_EVENTS"


# MARK: OS permissions strings

define AS_REQUIRE_NOTIFKIT_NAME = _("Отправлять уведомления")
define AS_REQUIRE_NOTIFKIT_DESC = _("Уведомления могут включать в себя баннеры, предупреждения и звуки. Это можно настроить в Менеджере приложений.")
define AS_REQUIRE_FDA_NAME = _("Доступ к файлам")
define AS_REQUIRE_FDA_DESC = _("Доступ к файлам может включать в себя вашу Домашнюю папку и директорию вашей установленной копии Candella. Это можно настроить в Менеджере приложений.")
define AS_REQUIRE_SYSEV_NAME = _("Управлять настройками Candella")
define AS_REQUIRE_SYSEV_DESC = _("Доступ к настройкам может включать в себя параметры специальных возможностей, системные события и её конфигурацию. Это можно настроить в Менеджере приложений.")

# MARK: OS permissions enumerations

define AS_REQUIRE_PERMS_NAME = {
    AS_REQUIRES_NOTIFICATIONKIT: AS_REQUIRE_NOTIFKIT_NAME,
    AS_REQUIRES_FULL_DISK_ACCESS: AS_REQUIRE_FDA_NAME,
    AS_REQUIRES_SYSTEM_EVENTS: AS_REQUIRE_SYSEV_NAME
}

define AS_REQUIRE_PERMS_DESC = {
    AS_REQUIRES_NOTIFICATIONKIT: AS_REQUIRE_NOTIFKIT_DESC,
    AS_REQUIRES_FULL_DISK_ACCESS: AS_REQUIRE_FDA_DESC,
    AS_REQUIRES_SYSTEM_EVENTS: AS_REQUIRE_SYSEV_DESC
}