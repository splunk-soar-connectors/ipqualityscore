# File: ipqualityscore_connector.py
#
# Copyright (c) 2021-2023 IPQualityScore.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.

import urllib.parse

# Phantom imports
import phantom.app as phantom
import requests
# Global imports
import simplejson as json
from phantom.action_result import ActionResult
from phantom.base_connector import BaseConnector

# Local imports
from ipqualityscore_consts import *


class IpqualityscoreConnector(BaseConnector):

    def __init__(self):
        super(IpqualityscoreConnector, self).__init__()

    def handle_action(self, param):
        result = None
        action_id = self.get_action_identifier()
        if action_id == ACTION_ID_URL_CHECKER:
            result = self.check_url(param)
        elif action_id == ACTION_ID_IP_REPUTATION:
            result = self.ip_reputation(param)
        elif action_id == ACTION_ID_EMAIL_VALIDATION:
            result = self.email_validation(param)
        elif action_id == phantom.ACTION_ID_TEST_ASSET_CONNECTIVITY:
            result = self.test_asset_connectivity(param)
        return result

    def _get_error_message_from_exception(self, e):
        """ This method is used to get appropriate error messages from the exception.
        :param e: Exception object
        :return: error message
        """
        error_code = None
        error_message = ERROR_MESSAGE_UNAVAILABLE
        self.error_print("Error occurred.", e)

        try:
            if e.args:
                if len(e.args) > 1:
                    error_code = e.args[0]
                    error_message = e.args[1]
                elif len(e.args) == 1:
                    error_code = ERROR_CODE_MESSAGE
                    error_message = e.args[0]
            else:
                error_code = ERROR_CODE_MESSAGE
        except:
            error_code = ERROR_CODE_MESSAGE

        try:
            if error_code in ERROR_CODE_MESSAGE:
                error_text = "Error Message: {0}".format(error_message)
            else:
                error_text = "Error Code: {0}. Error Message: {1}".format(error_code, error_message)
        except:
            self.debug_print(PARSE_ERROR_MESSAGE)
            error_text = PARSE_ERROR_MESSAGE

        return error_text

    def _validate_integer(self, action_result, parameter, key):
        if parameter is not None:
            try:
                if not float(parameter).is_integer():
                    return action_result.set_status(phantom.APP_ERROR, VALID_INTEGER_MESSAGE.format(key)), None

                parameter = int(parameter)
            except:
                return action_result.set_status(phantom.APP_ERROR, VALID_INTEGER_MESSAGE.format(key)), None

            if parameter < 0:
                return action_result.set_status(phantom.APP_ERROR, NON_NEGATIVE_INTEGER_MESSAGE.format(key)), None

        return phantom.APP_SUCCESS, parameter

    def test_asset_connectivity(self, param):
        config = self.get_config()
        app_key = config['apikey']
        self.save_progress(IPQUALITYSCORE_MESSAGE_CONNECTIVITY)
        try:
            response = requests.get(IPQUALITYSCORE_API_TEST.format(apikey=app_key))  # nosemgrep
            # python.requests.best-practice.use-timeout.use-timeout
        except Exception as e:
            err = self._get_error_message_from_exception(e)
            self.debug_print('test_asset_connectivity: {}'.format(err))
            err_msg = '{}. {}. Error Occurred: {}'.format(IPQUALITYSCORE_ERROR_CONNECTIVITY_TEST,
                                                          IPQUALITYSCORE_MESSAGE_CHECK_CONNECTIVITY, err)
            return self.set_status(phantom.APP_ERROR, err_msg)

        if response.status_code == 509:
            self.save_progress(IPQUALITYSCORE_SERVER_ERROR_RATE_LIMIT)
            self.save_progress(IPQUALITYSCORE_ERROR_CONNECTIVITY_TEST)
            return self.set_status(phantom.APP_ERROR)
        if response.status_code != 200:
            self.save_progress('{}. {}'.format(IPQUALITYSCORE_SERVER_RETURNED_ERROR_CODE.
                                               format(code=response.status_code),
                                               IPQUALITYSCORE_MESSAGE_CHECK_CONNECTIVITY))
            self.save_progress(IPQUALITYSCORE_ERROR_CONNECTIVITY_TEST)
            return self.set_status(phantom.APP_ERROR)

        try:
            result = response.json()
        except Exception as e:
            err = self._get_error_message_from_exception(e)
            self.debug_print('Response from server is not a valid JSON {}'.format(err))
            self.save_progress('Response from server is not a valid JSON')
            self.save_progress(IPQUALITYSCORE_ERROR_CONNECTIVITY_TEST)
            return self.set_status(phantom.APP_ERROR)

        if result.get('success'):
            self.save_progress(IPQUALITYSCORE_SUCCESS_CONNECTIVITY_TEST)
            return self.set_status(phantom.APP_SUCCESS)

        self.save_progress(IPQUALITYSCORE_ERROR_CONNECTIVITY_TEST)
        return self.set_status(phantom.APP_ERROR)

    def create_req_url(self, urltype, param, app_key):
        if urltype == "url":
            req_url = IPQUALITYSCORE_API_URL_CHECKER.format(
                apikey=app_key, url=urllib.parse.quote_plus(param['url']))
        elif urltype == "ip":
            req_url = IPQUALITYSCORE_API_IP_REPUTATION.format(
                apikey=app_key, ip=param['ip'])
        elif urltype == "email":
            req_url = IPQUALITYSCORE_API_EMAIL_VALIDATION.format(
                apikey=app_key, email=param['email'])
        else:
            req_url = ''
        # optional parameters
        optional_params = {
            'strictness': param.get('strictness'),
            'user_agent': param.get('user_agent'),
            'user_language': param.get('user_language'),
            'fast': param.get('fast'),
            'mobile': param.get('mobile'),
            'allow_public_access_points': param.get('allow_public_access_points'),
            'lighter_penalties': param.get('lighter_penalties'),
            'transaction_strictness': param.get('transaction_strictness'),
            'timeout': param.get('timeout'),
            'suggest_domain': param.get('suggest_domain'),
            'abuse_strictness': param.get('abuse_strictness'),
        }
        query_string = '&'.join(f'{k}={v}' for k, v in optional_params.items() if v is not None)
        if query_string:
            req_url = "{}?{}".format(req_url, query_string)
        self.debug_print('req_url {}'.format(req_url))
        return req_url

    def check_url(self, param):
        config = self.get_config()
        app_key = config['apikey']
        action_result = self.add_action_result(ActionResult(dict(param)))
        summary = action_result.update_summary({})

        ret_val, _ = self._validate_integer(action_result, param.get('strictness'), STRICTNESS_KEY)
        if phantom.is_fail(ret_val):
            return action_result.get_status()

        self.save_progress(IPQUALITYSCORE_MESSAGE_QUERY_URL, query_url=param['url'])
        try:
            req_url = self.create_req_url('url', param, app_key)
            query_res = requests.get(req_url)  # nosemgrep: python.requests.best-practice.use-timeout.use-timeout
        except Exception as e:
            err = self._get_error_message_from_exception(e)
            self.debug_print('check_url: {}'.format(err))
            return action_result.set_status(phantom.APP_ERROR, '{}{}'.format(IPQUALITYSCORE_SERVER_CONNECTIVITY_ERROR, err))

        action_result.add_debug_data({'response_text': query_res.text if query_res else ''})
        self.debug_print('status_code {}'.format(query_res.status_code))
        if query_res.status_code == 509:
            return action_result.set_status(
                phantom.APP_ERROR,
                IPQUALITYSCORE_SERVER_ERROR_RATE_LIMIT)
        if query_res.status_code != 200:
            return action_result.set_status(
                phantom.APP_ERROR,
                IPQUALITYSCORE_SERVER_RETURNED_ERROR_CODE.
                format(code=query_res.status_code))
        try:
            result = query_res.json()
        except Exception as e:
            err = self._get_error_message_from_exception(e)
            self.debug_print('Response from server is not a valid JSON {}'.format(err))
            return action_result.set_status(
                phantom.APP_ERROR,
                'Response from server is not a valid JSON')

        if 'status_code' in result:
            if result['status_code'] == 200:
                status = result['message']
                action_result.append_to_message(IPQUALITYSCORE_SERVICE_SUCCESS_MESSAGE)
            else:
                status = result['message']
                action_result.append_to_message("URL is unreachable")
        else:
            return action_result.set_status(
                phantom.APP_ERROR,
                IPQUALITYSCORE_ERROR_MESSAGE_OBJECT_QUERIED)

        try:
            status_summary = {}
            if result['success'] is True:
                status_summary['Message'] = result["message"]
                status_summary['Status_Code'] = result["status_code"]
                status = {}
                for key, val in result.items():
                    status[key] = val
            else:
                status_summary['Message'] = result["message"]
                status_summary['Status_Code'] = result["status_code"]
            summary.update(status_summary)
        except Exception as e:
            err = self._get_error_message_from_exception(e)
            return action_result.set_status(
                phantom.APP_ERROR, 'Error populating summary {}'.format(err))

        action_result.add_data(status)
        return action_result.set_status(phantom.APP_SUCCESS)

    def ip_reputation(self, param):
        config = self.get_config()
        app_key = config['apikey']
        action_result = self.add_action_result(ActionResult(dict(param)))
        summary = action_result.update_summary({})

        ret_val, _ = self._validate_integer(action_result, param.get('strictness'), STRICTNESS_KEY)
        if phantom.is_fail(ret_val):
            return action_result.get_status()

        ret_val, _ = self._validate_integer(action_result, param.get('transaction_strictness'),
                                            TRANSACTION_STRICTNESS_KEY)
        if phantom.is_fail(ret_val):
            return action_result.get_status()

        self.save_progress(IPQUALITYSCORE_MESSAGE_QUERY_URL,
                           query_ip=param['ip'])
        try:
            req_url = self.create_req_url('ip', param, app_key)
            query_res = requests.get(req_url)  # nosemgrep: python.requests.best-practice.use-timeout.use-timeout
        except Exception as e:
            err = self._get_error_message_from_exception(e)
            self.debug_print('ip_reputation: {}'.format(err))
            return action_result.set_status(phantom.APP_ERROR, '{}{}'.format(IPQUALITYSCORE_SERVER_CONNECTIVITY_ERROR, err))

        action_result.add_debug_data({'response_text': query_res.text if query_res else ''})
        self.debug_print('status_code {}'.format(query_res.status_code))
        if query_res.status_code == 509:
            return action_result.set_status(
                phantom.APP_ERROR, IPQUALITYSCORE_SERVER_ERROR_RATE_LIMIT)
        if query_res.status_code != 200:
            return action_result.set_status(
                phantom.APP_ERROR, IPQUALITYSCORE_SERVER_RETURNED_ERROR_CODE.
                format(code=query_res.status_code))
        try:
            result = query_res.json()
        except Exception as e:
            err = self._get_error_message_from_exception(e)
            self.debug_print('Response from server is not a valid JSON {}'.format(err))
            return action_result.set_status(
                phantom.APP_ERROR,
                'Response from server is not a valid JSON')

        if result.get('success'):
            status = result['message']
            action_result.append_to_message(
                IPQUALITYSCORE_SERVICE_SUCCESS_MESSAGE)
        else:
            return action_result.set_status(
                phantom.APP_ERROR,
                IPQUALITYSCORE_ERROR_MESSAGE_OBJECT_QUERIED)

        try:
            status_summary = {}
            if result['success'] is True:
                status_summary['Message'] = result["message"]
                status_summary['Status_Code'] = 200
                status = {}
                for key, val in result.items():
                    status[key] = val
            else:
                status_summary['Message'] = result["message"]
                status_summary['Status_Code'] = 500
            summary.update(status_summary)
        except Exception as e:
            err = self._get_error_message_from_exception(e)
            return action_result.set_status(
                phantom.APP_ERROR, 'Error populating summary {}'.format(err))

        action_result.add_data(status)
        return action_result.set_status(phantom.APP_SUCCESS)

    def email_validation(self, param):
        config = self.get_config()
        app_key = config['apikey']
        action_result = self.add_action_result(ActionResult(dict(param)))
        summary = action_result.update_summary({})

        ret_val, _ = self._validate_integer(action_result, param.get('timeout'), TIMEOUT_KEY)
        if phantom.is_fail(ret_val):
            return action_result.get_status()

        ret_val, _ = self._validate_integer(action_result, param.get('strictness'), STRICTNESS_KEY)
        if phantom.is_fail(ret_val):
            return action_result.get_status()

        ret_val, _ = self._validate_integer(action_result, param.get('abuse_strictness'), ABUSE_STRICTNESS_KEY)
        if phantom.is_fail(ret_val):
            return action_result.get_status()

        self.save_progress(IPQUALITYSCORE_MESSAGE_QUERY_URL,
                           query_ip=param['email'])
        try:
            req_url = self.create_req_url('email', param, app_key)
            query_res = requests.get(req_url)  # nosemgrep: python.requests.best-practice.use-timeout.use-timeout
        except Exception as e:
            err = self._get_error_message_from_exception(e)
            self.debug_print('ip_reputation: {}'.format(err))
            return action_result.set_status(phantom.APP_ERROR, '{}{}'.format(IPQUALITYSCORE_SERVER_CONNECTIVITY_ERROR, err))

        action_result.add_debug_data({'response_text': query_res.text if query_res else ''})
        self.debug_print('status_code {}'.format(query_res.status_code))
        if query_res.status_code == 509:
            return action_result.set_status(
                phantom.APP_ERROR,
                IPQUALITYSCORE_SERVER_ERROR_RATE_LIMIT)
        if query_res.status_code != 200:
            return action_result.set_status(
                phantom.APP_ERROR,
                IPQUALITYSCORE_SERVER_RETURNED_ERROR_CODE.
                format(code=query_res.status_code))
        try:
            result = query_res.json()
        except Exception as e:
            err = self._get_error_message_from_exception(e)
            self.debug_print('Response from server is not a valid JSON {}'.format(err))
            return action_result.set_status(
                phantom.APP_ERROR,
                'Response from server is not a valid JSON')

        if result.get('success'):
            status = result['message']
            action_result.append_to_message(
                IPQUALITYSCORE_SERVICE_SUCCESS_MESSAGE)
        else:
            return action_result.set_status(
                phantom.APP_ERROR,
                IPQUALITYSCORE_ERROR_MESSAGE_OBJECT_QUERIED)
        try:
            status_summary = {}
            if result['success'] is True:
                status_summary['Message'] = result["message"]
                status_summary['Status_Code'] = 200
                status = result.copy()
            else:
                status_summary['Message'] = result["message"]
                status_summary['Status_Code'] = 500
            summary.update(status_summary)
        except Exception as e:
            err = self._get_error_message_from_exception(e)
            return action_result.set_status(
                phantom.APP_ERROR, 'Error populating summary {}'.format(err))

        action_result.add_data(status)
        return action_result.set_status(phantom.APP_SUCCESS)


if __name__ == '__main__':

    import argparse
    import sys

    import pudb

    pudb.set_trace()

    argparser = argparse.ArgumentParser()

    argparser.add_argument('input_test_json', help='Input Test JSON file')
    argparser.add_argument('-u', '--username', help='username', required=False)
    argparser.add_argument('-p', '--password', help='password', required=False)
    argparser.add_argument('-v', '--verify', action='store_true', help='verify', required=False, default=False)

    args = argparser.parse_args()
    session_id = None

    username = args.username
    password = args.password
    verify = args.verify

    if username is not None and password is None:
        # User specified a username but not a password, so ask
        import getpass

        password = getpass.getpass("Password: ")

    if username and password:
        try:
            print("Accessing the Login page")
            r = requests.get(BaseConnector._get_phantom_base_url() + "login", verify=verify,
                             timeout=IPQUALITYSCORE_DEFAULT_TIMEOUT)
            csrftoken = r.cookies['csrftoken']

            data = dict()
            data['username'] = username
            data['password'] = password
            data['csrfmiddlewaretoken'] = csrftoken

            headers = dict()
            headers['Cookie'] = 'csrftoken=' + csrftoken
            headers['Referer'] = BaseConnector._get_phantom_base_url()

            print("Logging into Platform to get the session id")
            r2 = requests.post(BaseConnector._get_phantom_base_url(), verify=verify, data=data, headers=headers,
                               timeout=IPQUALITYSCORE_DEFAULT_TIMEOUT)
            session_id = r2.cookies['sessionid']
        except Exception as e:
            print("Unable to get session id from the platform. Error: " + str(e))
            sys.exit(1)

    if len(sys.argv) < 2:
        print("No test json specified as input")
        sys.exit(0)

    with open(args.input_test_json) as f:
        in_json = f.read()
        in_json = json.loads(in_json)
        print(json.dumps(in_json, indent=4))

        connector = IpqualityscoreConnector()
        connector.print_progress_message = True

        if session_id is not None:
            in_json['user_session_token'] = session_id

        ret_val = connector._handle_action(json.dumps(in_json), None)
        print(json.dumps(json.loads(ret_val), indent=4))

    sys.exit(0)
