# File: ipqualityscore_consts.py
#
# Copyright (c) 2021-2025 IPQualityScore.com
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

IPQUALITYSCORE_DOMAIN = "https://ipqualityscore.com"

IPQUALITYSCORE_API_TEST = "https://ipqualityscore.com/api/json/ip/{apikey}/8.8.8.8"
IPQUALITYSCORE_API_URL_CHECKER = "https://ipqualityscore.com/api/json/url/{apikey}/{url}"
IPQUALITYSCORE_API_IP_REPUTATION = "https://ipqualityscore.com/api/json/ip/{apikey}/{ip}"
IPQUALITYSCORE_API_EMAIL_VALIDATION = "https://ipqualityscore.com/api/json/email/{apikey}/{email}"
IPQUALITYSCORE_API_PHONE_VALIDATION = "https://ipqualityscore.com/api/json/phone/{apikey}/{phone}"
IPQUALITYSCORE_API_DARKWEBLEAK = "https://ipqualityscore.com/api/json/leaked/{type}/{apikey}/{data}"

IPQUALITYSCORE_APP_KEY = "app_key"
IPQUALITYSCORE_MESSAGE_QUERY_URL = "Querying URL: {query_url}"
IPQUALITYSCORE_MESSAGE_CONNECTIVITY = "Polling IPQualityScore site ..."
IPQUALITYSCORE_SERVICE_SUCCESS_MESSAGE = "IPQualityScore Service successfully executed."
IPQUALITYSCORE_SUCCESS_CONNECTIVITY_TEST = "Test Connectivity passed"
IPQUALITYSCORE_ERROR_CONNECTIVITY_TEST = "Test Connectivity failed"
IPQUALITYSCORE_MESSAGE_GOT_RESP = "Got response from IPQualityScore"
IPQUALITYSCORE_NO_RESPONSE = "Server did not return a response \
                         for the object queried"
IPQUALITYSCORE_SERVER_CONNECTIVITY_ERROR = "Server connection error"
IPQUALITYSCORE_MESSAGE_CHECK_CONNECTIVITY = "Please check your network connectivity"
IPQUALITYSCORE_SERVER_RETURNED_ERROR_CODE = "Server returned error code: {code}"
IPQUALITYSCORE_ERROR_MESSAGE_OBJECT_QUERIED = "IPQualityScore response didn't \
                                    send expected response"
IPQUALITYSCORE_SERVER_ERROR_RATE_LIMIT = "Query is being rate limited. \
                                     Server returned 509"

ACTION_ID_URL_CHECKER = "check_url"
ACTION_ID_IP_REPUTATION = "ip_reputation"
ACTION_ID_EMAIL_VALIDATION = "email_validation"
ACTION_ID_PHONE_VALIDATION = "phone_validation"
ACTION_ID_DARK_WEB_LEAK = "darkwebleak"

# Constants relating to '_get_error_message_from_exception'
ERROR_CODE_MESSAGE = "Error code unavailable"
ERROR_MESSAGE_UNAVAILABLE = "Error message unavailable. Please check the asset configuration and|or action parameters"
PARSE_ERROR_MESSAGE = "Unable to parse the error message. Please check the asset configuration and|or action parameters"

# Constants relating to '_validate_integer'
VALID_INTEGER_MESSAGE = "Please provide a valid integer value in the {}"
NON_NEGATIVE_INTEGER_MESSAGE = "Please provide a valid non-negative integer value in the {}"
TIMEOUT_KEY = "'timeout' action parameter"
STRICTNESS_KEY = "'strictness' action parameter"
ABUSE_STRICTNESS_KEY = "'abuse_strictness' action parameter"
TRANSACTION_STRICTNESS_KEY = "'transaction_strictness' action parameter"

# Constants relating to 'phone_validation'
PHONE_NUMBER_KEY = "'phone' action parameter"
PHONE_NUMBER_FORMAT_ERROR_MESSAGE = "Please provide valid phone number"
PHONE_REG = r"^\+?[1-9]\d{1,14}$"

# Constants relating to 'darkwebleak'
EMAIL_REG = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}"
EMAIL_FORMAT_ERROR_MESSAGE = "Please provide valid Email"
VALUE_KEY = "'value' action parameter"

# timeout
IPQUALITYSCORE_DEFAULT_TIMEOUT = 30
