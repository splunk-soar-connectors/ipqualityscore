# IPQualityScore

Publisher: IPQualityScore \
Connector Version: 1.2.0 \
Product Vendor: IPQualityScore \
Product Name: IPQualityScore \
Minimum Product Version: 6.3.0

This app implements IP, URL and Email investigative capabilities utilizing IPQualityScore

### Configuration variables

This table lists the configuration variables required to operate IPQualityScore. These variables are specified when configuring a IPQualityScore asset in Splunk SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**apikey** | required | password | API key |

### Supported Actions

[test connectivity](#action-test-connectivity) - Validates the connectivity by querying IPQualityScore \
[email validation](#action-email-validation) - Queries IPQualityScore's Email Validation API \
[url checker](#action-url-checker) - Queries IPQualityScore's malicious URL scanner API \
[ip reputation](#action-ip-reputation) - Queries IPQualityScore's Proxy and VPN detection API \
[phone validation](#action-phone-validation) - Queries IPQualityScore's Phone Validation API \
[dark web leak](#action-dark-web-leak) - Queries IPQualityScore's Dark Web Leak API

## action: 'test connectivity'

Validates the connectivity by querying IPQualityScore

Type: **test** \
Read only: **True**

#### Action Parameters

No parameters are required for this action

#### Action Output

No Output

## action: 'email validation'

Queries IPQualityScore's Email Validation API

Type: **investigate** \
Read only: **True**

If email information is unavailable in IPQualityScore, only 'email' and 'message' property would be populated. The 'strictness' is an optional parameter to perform (higher number) or ignore (lower number) of additional intelligence checks. The possible values for 'strictness' are 0,1 and 2.

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**email** | required | Email to query for reputation information | string | `email` |
**fast** | optional | Enables or disables SMTP check with the mail service provider | boolean | |
**suggest_domain** | optional | Force analyze if the email address's domain has a typo and should be corrected to a popular mail service | boolean | |
**timeout** | optional | Maximum number of seconds to wait for a reply from a mail service provider | numeric | |
**strictness** | optional | Sets how strictly spam traps and honeypots are detected by system (Possible Values: 0, 1 and 2) | numeric | |
**abuse_strictness** | optional | Set the strictness level for machine learning pattern recognition of abusive email addresses | numeric | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.email | string | `email` | someone@domain.com |
action_result.parameter.fast | boolean | | True False |
action_result.parameter.timeout | numeric | | 2 |
action_result.parameter.suggest_domain | boolean | | True False |
action_result.parameter.strictness | numeric | | 2 |
action_result.parameter.abuse_strictness | numeric | | 2 |
action_result.data.\*.valid | boolean | | True False |
action_result.data.\*.timeout | boolean | | True False |
action_result.data.\*.disposable | boolean | | True False |
action_result.data.\*.first_name | string | | Unknown |
action_result.data.\*.deliverability | string | | high |
action_result.data.\*.smtp_score | numeric | | 3 |
action_result.data.\*.overall_score | numeric | | 3 |
action_result.data.\*.catch_all | boolean | | True False |
action_result.data.\*.generic | boolean | | True False |
action_result.data.\*.common | boolean | | True False |
action_result.data.\*.dns_valid | boolean | | True False |
action_result.data.\*.honeypot | boolean | | True False |
action_result.data.\*.frequent_complainer | boolean | | True False |
action_result.data.\*.suspect | boolean | | True False |
action_result.data.\*.recent_abuse | boolean | | True False |
action_result.data.\*.fraud_score | numeric | | 34 |
action_result.data.\*.leaked | boolean | | True False |
action_result.data.\*.suggested_domain | string | | N/A |
action_result.data.\*.first_seen.human | string | | 1 month ago |
action_result.data.\*.domain_age.human | string | | 1 month ago |
action_result.data.\*.spam_trap_score | string | | none |
action_result.data.\*.sanitized_email | string | | someone@domain.com |
action_result.data.\*.request_id | string | | abc123 |
action_result.status | string | | success failed |
action_result.message | string | | api request completed |
action_result.summary.Message | string | | failure |
action_result.summary.Status_Code | numeric | | 400 |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'url checker'

Queries IPQualityScore's malicious URL scanner API

Type: **investigate** \
Read only: **True**

If URL information is unavailable in IPQualityScore, only 'url' and 'in_database' property would be populated. The 'strictness' is an optional parameter to perform (higher number) or ignore (lower number) of additional intelligence checks. The possible values for 'strictness' are 0,1 and 2.

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**url** | required | URL to query for reputation information | string | `url` `domain` |
**strictness** | optional | How strict should we scan this URL? (Possible Values: 0, 1 and 2) | numeric | |
**fast** | optional | The API will provide quicker response times using lighter checks and analysis when enabled. This setting defaults to "false" | boolean | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.url | string | `url` `domain` | |
action_result.parameter.strictness | numeric | | |
action_result.parameter.fast | boolean | | |
action_result.status | string | | success failed |
action_result.message | string | | |
summary.total_objects | numeric | | |
summary.total_objects_successful | numeric | | |

## action: 'ip reputation'

Queries IPQualityScore's Proxy and VPN detection API

Type: **investigate** \
Read only: **True**

If URL information is unavailable in IPQualityScore, only 'message' and 'status_code' properties would be populated. The 'strictness' is an optional parameter to perform (higher number) or ignore (lower number) of additional intelligence checks. The possible values for 'strictness' are 0,1 and 2.

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**ip** | required | IP to query for reputation information | string | `ip` |
**strictness** | optional | How in depth (strict) do you want this query to be? (Possible Values: 0, 1 and 2) | numeric | |
**user_agent** | optional | Additional checks against bots | string | |
**user_language** | optional | Additional risk evaluation | string | |
**fast** | optional | Certain forensic checks are skipped | boolean | |
**mobile** | optional | Specifies if this lookup should be treated as a mobile device | boolean | |
**allow_public_access_points** | optional | Specifies if this lookup should be treated as a mobile device | boolean | |
**lighter_penalties** | optional | Enable this setting to lower detection rates and Fraud Scores for mixed quality IP addresses | boolean | |
**transaction_strictness** | optional | Adjusts the weights for penalties applied due to irregularities | numeric | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.strictness | numeric | | 3 |
action_result.parameter.user_agent | string | | mozilla |
action_result.parameter.user_language | string | | en |
action_result.parameter.fast | boolean | | True False |
action_result.parameter.mobile | boolean | | True False |
action_result.parameter.allow_public_access_points | boolean | | True False |
action_result.parameter.lighter_penalties | boolean | | True False |
action_result.parameter.transaction_strictness | boolean | | True False |
action_result.parameter.ip | string | `ip` | 1.1.1.1 |
action_result.data.\*.message | string | | Failure. |
action_result.data.\*.success | boolean | | False True |
action_result.data.\*.fraud_score | numeric | | 1213 |
action_result.data.\*.country_code | string | | us |
action_result.data.\*.city | string | | atlanta |
action_result.data.\*.region | string | | northwest |
action_result.data.\*.ISP | string | | comcast |
action_result.data.\*.organization | string | | example.com |
action_result.data.\*.ASN | numeric | | 1231 |
action_result.data.\*.latitude | numeric | | 245 |
action_result.data.\*.longitude | numeric | | 1213 |
action_result.data.\*.is_crawler | boolean | | True False |
action_result.data.\*.timezone | string | | est |
action_result.data.\*.host | string | | hostname.com |
action_result.data.\*.proxy | boolean | | False True |
action_result.data.\*.vpn | boolean | | True False |
action_result.data.\*.tor | boolean | | True False |
action_result.data.\*.active_vpn | boolean | | True False |
action_result.data.\*.active_tor | boolean | | True False |
action_result.data.\*.connection_type | string | | data center |
action_result.data.\*.recent_abuse | boolean | | True False |
action_result.data.\*.abuse_velocity | string | | low |
action_result.data.\*.bot_status | boolean | | True False |
action_result.data.\*.mobile | boolean | | True False |
action_result.data.\*.country_code | string | | us |
action_result.data.\*.fraud_score | numeric | | 1213 |
action_result.data.\*.request_id | string | | low |
action_result.data.\*.operating_system | string | | linux |
action_result.status | string | | success failed |
action_result.summary.Message | string | | failure |
action_result.summary.Status_Code | numeric | | 400 |
action_result.message | string | | api request completed |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'phone validation'

Queries IPQualityScore's Phone Validation API

Type: **investigate** \
Read only: **True**

The IPQS Phone Number Validation API enables you to quickly analyze phone numbers to verify their risk score, country of origin, carrier, validity, owner information, and line connection status. This enables you to verify users, improve chargeback defense, and detect fraudulent activity in real-time. The IPQS Phone Number Validation API can research landline and cellular numbers in over 150 countries to identify invalid phone numbers or malicious users.

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**phone** | required | Phone Number you want to fetch reputation data | numeric | `phone number` `phone` |
**strictness** | optional | How in depth (strict) do you want this reputation check to be? Stricter checks may provide a higher false-positive rate. We recommend starting at "0", the lowest strictness setting, and increasing to "1" or "2" depending on your levels of fraud | numeric | |
**country** | optional | You can optionally provide us with the default country or countries(comma separated) this phone number is suspected to be associated with. Our system will prefer to use a country on this list for verification or will require a country to be specified in the event the phone number is less than 10 digits | string | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.phone | numeric | `phone number` `phone` | |
action_result.parameter.strictness | numeric | | |
action_result.parameter.country | string | | |
action_result.status | string | | success failed |
action_result.data.\*.message | string | | Phone is valid. |
action_result.message | string | | api request completed |
action_result.data.\*.success | boolean | | True False |
action_result.data.\*.formatted | string | | +918886686866 |
action_result.data.\*.local_format | string | | 088866 86866 |
action_result.data.\*.valid | boolean | | True |
action_result.data.\*.fraud_score | numeric | | 0 |
action_result.data.\*.recent_abuse | boolean | | False |
action_result.data.\*.VOIP | boolean | | False |
action_result.data.\*.prepaid | boolean | | False |
action_result.data.\*.risky | boolean | | False |
action_result.data.\*.active | boolean | | True |
action_result.data.\*.carrier | string | | Aircel |
action_result.data.\*.line_type | string | | Wireless |
action_result.data.\*.country | string | | IN |
action_result.data.\*.city | string | | Madhya Pradesh |
action_result.data.\*.zip_code | string | | N/A |
action_result.data.\*.region | string | | India |
action_result.data.\*.dialing_code | numeric | | 91 |
action_result.data.\*.active_status | string | | N/A |
action_result.data.\*.sms_domain | string | | aircel.co.in |
action_result.data.\*.associated_email_addresses.status | string | | No associated emails found. |
action_result.data.\*.associated_email_addresses.emails | string | | xuz@test.com |
action_result.data.\*.user_activity | string | | Disabled for performance. Contact support for further assistance. |
action_result.data.\*.mnc | string | | 801 |
action_result.data.\*.mcc | string | | 405 |
action_result.data.\*.leaked | boolean | | False |
action_result.data.\*.spammer | boolean | | False |
action_result.data.\*.request_id | string | | TbA02W8E1S |
action_result.data.\*.name | string | | N/A |
action_result.data.\*.timezone | string | | Asia/Kolkata |
action_result.data.\*.do_not_call | boolean | | False |
action_result.data.\*.accurate_country_code | boolean | | False |
action_result.data.\*.sms_email | string | | 08886686866@aircel.co.in |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'dark web leak'

Queries IPQualityScore's Dark Web Leak API

Type: **investigate** \
Read only: **True**

Use the leaked data API to search through a wide collection of breached, stolen, and leaked databases from popular websites that have recently suffered data breaches. Look up email addresses, phone numbers, usernames, or passwords. Perform on-demand leaked data searches using our dark web data API.

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**type** | required | Type of data you are submitting | string | |
**value** | required | Indicator Value of the type | string | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.type | string | | |
action_result.parameter.value | string | | |
action_result.status | string | | success failed |
action_result.data.\*.message | string | | Success |
action_result.data.\*.success | boolean | | True False |
action_result.data.\*.request_hash | string | | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161 |
action_result.data.\*.source | string | | Exploit Antipublic |
action_result.data.\*.exposed | boolean | | True False |
action_result.data.\*.first_seen.human | string | | 2 years ago |
action_result.data.\*.plain_text_password | boolean | | True False |
action_result.data.\*.request_id | string | | CosqSQLZsx |
action_result.message | string | | |
summary.total_objects | numeric | | |
summary.total_objects_successful | numeric | | |

______________________________________________________________________

Auto-generated Splunk SOAR Connector documentation.

Copyright 2025 Splunk Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
