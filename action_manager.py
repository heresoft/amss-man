import threading
import Modules.azure_server
import configparser
import time


class ActionManager:
    def __init__(self, status_update_callback):
        self.status_callback = status_update_callback
        self.config = configparser.ConfigParser()
        self.config.read('server.ini')
        self.az: Modules.azure_server.AzureServer = None
        self.start_service_thread = None
        self.end_service_thread = None
        self.status_test_thread = None

    def start_service(self):
        self.start_service_thread = threading.Thread(target=self._start_service_internal)
        self.start_service_thread.start()

    def _start_service_internal(self):
        # This is the function that actually does stuff for the start of the service
        self.status_callback("Loading Azure module")
        self.az = Modules.azure_server.AzureServer(self.config['azure_server'])
        self.az.start(self.status_callback)

    def start_sermon(self):
        print("monkeys")

    def _start_sermon_internal(self):
        print("monkeys")

    def end_sermon(self):
        print("monkeys")

    def _end_sermon_internal(self):
        print("Monkeys have really stopped")

    def end_service(self):
        self.end_service_thread = threading.Thread(target=self._end_service_internal)
        self.end_service_thread.start()

    def _end_service_internal(self):
        if self.az:
            self.az.stop(self.status_callback)

    def status_test(self):
        print(threading.get_ident())
        self.status_test_thread = threading.Thread(target=self._status_test_internal)
        self.status_test_thread.start()

    def _status_test_internal(self):
        print(threading.get_ident())
        self.status_callback("Test step 1")
        time.sleep(2)
        self.status_callback("Test step 1")
        time.sleep(2)
        self.status_callback("Test step 1")
        time.sleep(2)
        self.status_callback("Test step 1")