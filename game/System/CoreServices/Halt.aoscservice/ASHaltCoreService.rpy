#
# ASHaltCoreService.rpy
# Candella
#
# Created by Marquis Kurt on 7/3/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init 5 python:
    import os
    import logging

    class ASHaltCoreService(CACoreService):

        def __init__(self):
            CACoreService.__init__(self, AS_CORESERVICES_DIR + "Halt.aoscservice/")

        def _write_halt(self, code=""):
            template = """\
Система Candella столкнулась с проблемой, которую не может обработать, и её работа была завершена для предотвращения дальнейшего ущерба.
Вы можете найти данную ошибку в Базе данных ошибок на сайте https://errordb.aliceos.app, чтобы узнать больше информации о ней.

Данное сообщение, как правило, выводится на экран, если система Candella не смогла перезапустить систему по какой-то причине. Вы можете прочитать
файлы логов в нижеуказанной директории, дабы выявить причину возникновения стоп-ошибки.

Файл логов: %s

Код стоп-ошибки: %s
Версия Candella: %s
Сборка версии Candella: %s
Версия Ren'Py: %s
Операционная система хоста: %s
            """ % (
                os.path.join(config.savedir, "candella.log"),
                code,
                AS_SYS_INFO["VERSION"],
                AS_SYS_INFO["BUILD_ID"],
                renpy.version(),
                renpy.platform
            )
            try:
                with open("candella_stop.txt", "w+") as error_file:
                    error_file.write(template)
                renpy.exports.launch_editor([ "candella_stop.txt" ], 1, transient=1)
            except:
                print(template)

        def halt(self, code="", write=False):
            clog.error("Received Stop error code: %s. Halting and restarting.", code)
            try:
                if write:
                    raise Exception
                renpy.call_screen("ASHaltMessage", error=code)
            except renpy.game.UtterRestartException: # If we're restarting, don't write the file.
                return
            except Exception as exception:
                clog.error("Failed to display Stop screen. Reason: %s", exception)
                self._write_halt(code)
                clog.info("Wrote stop file to candella_stop.txt.")
                renpy.quit()


    ASHalt = ASHaltCoreService()
