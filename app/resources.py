from flask_restx import Resource , Namespace, fields, Api
import json
import os
import time
import subprocess
import sys
from flask_restx import reqparse
from flask import Flask
from my_web_server import WebServerActions
from .api_models import ApiModels
# from flask_cors import cross_origin # Для REACT

ns = Namespace("api/v1")
parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, help='Rate to charge for this resource')

@ns.route("/get_version")
class GetVersion(Resource):
    def get(self):
        '''Метод возвращает актуальную версию микросервиса'''
        return (WebServerActions().version)

"""
@ns.route("/allure_vk_setting")
class AllureVkSettings(Resource):
    def get(self):
        '''Метод возвращает актуальные настройки appsettings '''
        return (WebServerApi().web_config.allure_settings)


@ns.route("/vk_setting")
class VkSettings(Resource):
    @ns.expect(send_vk_model)
    def post(self,**kwargs):
        '''Метод зменяет настройки отправки уведомлений в ВК '''
        WebServerApi().update_allure_config(self.api.payload)
        return 


@ns.route("/generate_allure_report")
class GenerateAllureReport(Resource):
    @ns.expect(allure_report_model)
    def post(self,**kwargs):
        '''Метод изменяет настройки Allure'''
        WebServerApi().update_allure_config(self.api.payload)
        return 


@ns.route("/suite_parameters")
class SuiteParameters(Resource):
    def get(self):
        '''Метод возвращает актуальный набор тестов '''
        return (WebServerApi().web_config.auto_test_variables["SUITES_LIST"])

    @ns.expect(variables_model)
    def post(self,**kwargs):
        '''Метод изменяет набор тестов'''
        WebServerApi().update_variables_config(self.api.payload)
        return 


@ns.route("/test_run_data") 
class TestRunData(Resource):
    def get(self):
        '''Метод возвращает статус выполнения автотестов'''
        with open(os.path.abspath("test_run_data.json"), 'r', encoding='utf-8') as file:
            json_object = json.load(file)
        return json_object


@ns.route("/allure_last_log") 
class AllureLastLog(Resource):
    def get(self):
        '''Метод возвращает cсылку на отчёт о последнем тестировании с сервера Allure'''
        file = os.path.join("allure_resources","report_link_site.txt")
        with open(file) as inf:
                txt_log_link = inf.read()
        return txt_log_link


@ns.route("/run_test")
class RunTest(Resource):
    def get(self):
        '''Метод запускает автотест'''
        file = os.path.join("run_all_tests.bat")
        p = subprocess.run(["cmd.exe", "/c", "start", f"{file}"])
        return 


@ns.route("/test_status")
class TestStatus(Resource):
    def get(self):
        '''Метод проверяет производится ли в данный момент автоматическое тестирование '''
        status_file = TestRunStatus()
        is_running = status_file.config_data["is_running"]
        return is_running


@ns.route("/run_watchdog")
class RunWatchdog(Resource):
    def get(self):
        '''Метод запускает Watchdog '''
        file = os.path.join("watchdog.exe")
        p = subprocess.run(["cmd.exe", "/c", "start", f"{file}"], stdout=sys.stdout)
        return 


@ns.route("/disable_watchdog")
class DisableWatchdog(Resource):
    def get(self):
        '''Метод закрывает Watchdog '''
        close("watchdog")
        return


@ns.route("/status_watchdog")
class StatusWatchdog(Resource):
    def get(self):
        '''Метод возвращает статус выполнения службы Watchdog  '''
        status_watch = WebServerApi().process_exists('watchdog.exe')
        return status_watch


@ns.route("/status_server")
class StatusServer(Resource):
    def get(self):
        '''Метод возвращает статус работы R-Operator Server '''
        service = WebServerApi().get_service('RUBEZH Operator Server')
        if service and service['status'] == 'running':
            return True
        else:
            return False


@ns.route("/test_list") 
class TestList(Resource):
    def get(self):
        '''Метод возвращает актуальный список тестов'''
        file = os.path.join("app","test_list.txt")
        with open(file) as inf:
                txt_log_link = inf.read()
        return txt_log_link


@ns.route("/log_level_list") 
class LogLevelList(Resource):
    def get(self):
        '''Метод возвращает список возможных уровней логирования'''
        return ["FAIL", "WARN", "INFO", "DEBUG", "TRACE"]

@ns.route("/tag_parameters")
class TagParameters(Resource):
    def get(self):
        '''Метод возвращает актуальный набор тегов '''
        return (WebServerApi().web_config.auto_test_variables["INCLUDE_TAGS"])


@ns.route("/log_level")
class LogLevel(Resource):
    def get(self):
        '''Метод возвращает актуальный уровень логирования '''
        return (WebServerApi().web_config.auto_test_variables["LOG_LEVEL"])

    @ns.expect(log_model)
    def post(self,**kwargs):
        '''Метод изменяет набор тестов'''
        WebServerApi().update_variables_config(self.api.payload)
        return
"""