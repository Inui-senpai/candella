#
# ASNotificationAlert.rpy
# Candella
#
# Created by Marquis Kurt on 7/3/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

# MARK: ASNotificationAlert screen entry point
init screen ASNotificationAlert(message, withDetails, onDismissCallback=Return('didDismissAlert')):
    tag ASNotificationAlert
    zorder 200
    modal True

    on "show":
        action [
                Function(SetThumbnailFull),
                FileTakeScreenshot(),
                Function(SetThumbnailOriginal)
                ]

    if ca_supports_blur():
        add FileCurrentScreenshot() at blur
    else:
        add FileCurrentScreenshot():
            blur CABlurType["default"]

    frame at ASDynamicBlurTransition:
        style "ASDynamicBlurFrame"
        xalign 0.5
        yalign 0.5
        xfill True
        yfill True

        has vbox:
            xalign 0.5
            yalign 0.5
            xsize 656
            spacing 16

            text message:
                style "ASNotificationAlertTitle"
            text withDetails:
                style "ASNotificationAlertDetail"

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("ОК") action onDismissCallback:
                    style "ASNotificationAlertAcceptButton"
