import sys

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from call_mainwindow import MyMainWindow


if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MyMainWindow()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
