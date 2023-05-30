[comment]: # "Auto-generated SOAR connector documentation"
# IPQualityScore

Publisher: IPQualityScore  
Connector Version: 1.1.0  
Product Vendor: IPQualityScore  
Product Name: IPQualityScore  
Product Version Supported (regex): ".\*"  
Minimum Product Version: 5.5.0  

This app implements IP, URL and Email investigative capabilities utilizing IPQualityScore

### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a IPQualityScore asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**apikey** |  required  | password | API key

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validates the connectivity by querying IPQualityScore  
[email validation](#action-email-validation) - Queries IPQualityScore's Email Validation API  
[url checker](#action-url-checker) - Queries IPQualityScore's malicious URL scanner API  
[ip reputation](#action-ip-reputation) - Queries IPQualityScore's Proxy and VPN detection API  

## action: 'test connectivity'
Validates the connectivity by querying IPQualityScore

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'email validation'
Queries IPQualityScore's Email Validation API

Type: **investigate**  
Read only: **True**

If email information is unavailable in IPQualityScore, only 'email' and 'message' property would be populated. The 'strictness' is an optional parameter to perform (higher number) or ignore (lower number) of additional intelligence checks. The possible values for 'strictness' are 0,1 and 2.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**email** |  required  | Email to query for reputation information | string |  `email` 
**fast** |  optional  | Enables or disables SMTP check with the mail service provider | boolean | 
**suggest_domain** |  optional  | Force analyze if the email address's domain has a typo and should be corrected to a popular mail service | boolean | 
**timeout** |  optional  | Maximum number of seconds to wait for a reply from a mail service provider | numeric | 
**strictness** |  optional  | Sets how strictly spam traps and honeypots are detected by system (Possible Values: 0, 1 and 2) | numeric | 
**abuse_strictness** |  optional  | Set the strictness level for machine learning pattern recognition of abusive email addresses | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.email | string |  `email`  |   someone@domain.com 
action_result.parameter.fast | boolean |  |   True  False 
action_result.parameter.timeout | numeric |  |   2 
action_result.parameter.suggest_domain | boolean |  |   True  False 
action_result.parameter.strictness | numeric |  |   2 
action_result.parameter.abuse_strictness | numeric |  |   2 
action_result.data.\*.valid | boolean |  |   True  False 
action_result.data.\*.timeout | boolean |  |   True  False 
action_result.data.\*.disposable | boolean |  |   True  False 
action_result.data.\*.first_name | string |  |   Unknown 
action_result.data.\*.deliverability | string |  |   high 
action_result.data.\*.smtp_score | numeric |  |   3 
action_result.data.\*.overall_score | numeric |  |   3 
action_result.data.\*.catch_all | boolean |  |   True  False 
action_result.data.\*.generic | boolean |  |   True  False 
action_result.data.\*.common | boolean |  |   True  False 
action_result.data.\*.dns_valid | boolean |  |   True  False 
action_result.data.\*.honeypot | boolean |  |   True  False 
action_result.data.\*.frequent_complainer | boolean |  |   True  False 
action_result.data.\*.suspect | boolean |  |   True  False 
action_result.data.\*.recent_abuse | boolean |  |   True  False 
action_result.data.\*.fraud_score | numeric |  |   34 
action_result.data.\*.leaked | boolean |  |   True  False 
action_result.data.\*.suggested_domain | string |  |   N/A 
action_result.data.\*.first_seen.human | string |  |   1 month ago 
action_result.data.\*.domain_age.human | string |  |   1 month ago 
action_result.data.\*.spam_trap_score | string |  |   none 
action_result.data.\*.sanitized_email | string |  |   someone@domain.com 
action_result.data.\*.request_id | string |  |   abc123 
action_result.status | string |  |   success  failed 
action_result.message | string |  |   api request completed 
action_result.summary.Message | string |  |   failure 
action_result.summary.Status_Code | numeric |  |   400 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'url checker'
Queries IPQualityScore's malicious URL scanner API

Type: **investigate**  
Read only: **True**

If URL information is unavailable in IPQualityScore, only 'url' and 'in_database' property would be populated. The 'strictness' is an optional parameter to perform (higher number) or ignore (lower number) of additional intelligence checks. The possible values for 'strictness' are 0,1 and 2.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**url** |  required  | URL to query for reputation information | string |  `url` 
**strictness** |  optional  | How strict should we scan this URL? (Possible Values: 0, 1 and 2) | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.strictness | numeric |  |   2 
action_result.parameter.url | string |  `url`  |   http://www.splunk.com 
action_result.data.\*.message | string |  |   Failure. 
action_result.data.\*.success | boolean |  |   False  True 
action_result.data.\*.unsafe | boolean |  |   True  False 
action_result.data.\*.domain | string |  |   splunk.com 
action_result.data.\*.ip_address | string |  `ip`  |   8.8.8.8 
action_result.data.\*.server | string |  |   gws 
action_result.data.\*.content_type | string |  |   text/html 
action_result.data.\*.status_code | numeric |  |   200 
action_result.data.\*.page_size | numeric |  |   100 
action_result.data.\*.domain_rank | numeric |  |   245 
action_result.data.\*.dns_valid | boolean |  |   True  False 
action_result.data.\*.parking | boolean |  |   True  False 
action_result.data.\*.spamming | boolean |  |   True  False 
action_result.data.\*.malware | boolean |  |   True  False 
action_result.data.\*.phishing | boolean |  |   True  False 
action_result.data.\*.suspicious | boolean |  |   True  False 
action_result.data.\*.risk_score | numeric |  |   3 
action_result.data.\*.request_id | string |  |   abc123 
action_result.status | string |  |   success  failed 
action_result.summary.Message | string |  |   failure 
action_result.summary.Status_Code | numeric |  |   400 
action_result.message | string |  |   api request completed 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'ip reputation'
Queries IPQualityScore's Proxy and VPN detection API

Type: **investigate**  
Read only: **True**

If URL information is unavailable in IPQualityScore, only 'message' and 'status_code' properties would be populated. The 'strictness' is an optional parameter to perform (higher number) or ignore (lower number) of additional intelligence checks. The possible values for 'strictness' are 0,1 and 2.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**ip** |  required  | IP to query for reputation information | string |  `ip` 
**strictness** |  optional  | How in depth (strict) do you want this query to be? (Possible Values: 0, 1 and 2) | numeric | 
**user_agent** |  optional  | Additional checks against bots | string | 
**user_language** |  optional  | Additional risk evaluation | string | 
**fast** |  optional  | Certain forensic checks are skipped | boolean | 
**mobile** |  optional  | Specifies if this lookup should be treated as a mobile device | boolean | 
**allow_public_access_points** |  optional  | Specifies if this lookup should be treated as a mobile device | boolean | 
**lighter_penalties** |  optional  | Enable this setting to lower detection rates and Fraud Scores for mixed quality IP addresses | boolean | 
**transaction_strictness** |  optional  | Adjusts the weights for penalties applied due to irregularities | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.strictness | numeric |  |   3 
action_result.parameter.user_agent | string |  |   mozilla 
action_result.parameter.user_language | string |  |   en 
action_result.parameter.fast | boolean |  |   True  False 
action_result.parameter.mobile | boolean |  |   True  False 
action_result.parameter.allow_public_access_points | boolean |  |   True  False 
action_result.parameter.lighter_penalties | boolean |  |   True  False 
action_result.parameter.transaction_strictness | boolean |  |   True  False 
action_result.parameter.ip | string |  `ip`  |   1.1.1.1 
action_result.data.\*.message | string |  |   Failure. 
action_result.data.\*.success | boolean |  |   False  True 
action_result.data.\*.fraud_score | numeric |  |   1213 
action_result.data.\*.country_code | string |  |   us 
action_result.data.\*.city | string |  |   atlanta 
action_result.data.\*.region | string |  |   northwest 
action_result.data.\*.ISP | string |  |   comcast 
action_result.data.\*.organization | string |  |   splunk.com 
action_result.data.\*.ASN | numeric |  |   1231 
action_result.data.\*.latitude | numeric |  |   245 
action_result.data.\*.longitude | numeric |  |   1213 
action_result.data.\*.is_crawler | boolean |  |   True  False 
action_result.data.\*.timezone | string |  |   est 
action_result.data.\*.host | string |  |   hostname.com 
action_result.data.\*.proxy | boolean |  |   False  True 
action_result.data.\*.vpn | boolean |  |   True  False 
action_result.data.\*.tor | boolean |  |   True  False 
action_result.data.\*.active_vpn | boolean |  |   True  False 
action_result.data.\*.active_tor | boolean |  |   True  False 
action_result.data.\*.connection_type | string |  |   data center 
action_result.data.\*.recent_abuse | boolean |  |   True  False 
action_result.data.\*.abuse_velocity | string |  |   low 
action_result.data.\*.bot_status | boolean |  |   True  False 
action_result.data.\*.mobile | boolean |  |   True  False 
action_result.data.\*.country_code | string |  |   us 
action_result.data.\*.fraud_score | numeric |  |   1213 
action_result.data.\*.request_id | string |  |   low 
action_result.data.\*.operating_system | string |  |   linux 
action_result.status | string |  |   success  failed 
action_result.summary.Message | string |  |   failure 
action_result.summary.Status_Code | numeric |  |   400 
action_result.message | string |  |   api request completed 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 