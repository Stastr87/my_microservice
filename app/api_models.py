
from flask_restx import fields
from .extensions import api


'''
Файл содержит модели которые отображаются в swagger
'''

class ApiModels():
    version_model = api.model('version_model', {"Microservice_name": fields.String(readonly = True,description = 'Microservice_name'),
                                            "Microservice_version": fields.String(readonly = True,description = 'Microservice_version')})


    allure_report_vk_model = api.model("Allure_vk",
                                   {"ALLURE_HOST": fields.String(readonly = True,description = 'Allure host ip addres'),
                                    "ALLURE_OUTPUT_FOLDER": fields.String(readonly = True,
                                                                          description = 'Allure output folder'),
                                    "GENERATE_ALLURE_REPORT": fields.Boolean(required = True, description = 'Generate allure report'),
                                    "SEND_VK_MESSAGE": fields.Boolean(required = True, description = 'Send VK message')})

    allure_report_model = api.model("Allure",{"GENERATE_ALLURE_REPORT": fields.Boolean(required = True, description = 'Generate allure report')})


    send_vk_model = api.model("Send_vk", {"SEND_VK_MESSAGE": fields.Boolean(required = True, description = 'Send VK message')})

    log_model = api.model("Log_level", {"LOG_LEVEL": fields.String(required = True, description = 'Log level')})

    variables_model = api.model("Variables",
                           {"SUITES_LIST": fields.List(fields.String(),
                                                       required = True, 
                                                       description = 'Test suite list',
                                                       default = []),
                           "INCLUDE_TAGS": fields.List(fields.String(),
                                                       required = True,
                                                       description = 'Test include TAG list',
                                                       default = []),
                           "EXCLUDE_TAGS": fields.List(fields.String(),
                                                       required = True,
                                                       description = 'Test exclude TAG list',
                                                       default = []),
                           "LOG_LEVEL": fields.String(required = True,
                                                       description = 'Test exclude TAG list',
                                                       default = "INFO")})