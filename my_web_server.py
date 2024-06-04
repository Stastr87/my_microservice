
class WebServerActions():
    def __init__(self):
        self.version = None
        self.set_version()


    def set_version(self):
        '''Задает текущую версию микросервиса'''
        self.version = {"Microservice_name": 'My_Microservice',
                        "Microservice_version": '0.1'}



 