[comment]: # "Auto-generated SOAR connector documentation"
# IPQualityScore

Publisher: IPQualityScore  
Connector Version: 1\.0\.2  
Product Vendor: IPQualityScore  
Product Name: IPQualityScore  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 5\.1\.0  

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

If email information is unavailable in IPQualityScore, only 'email' and 'message' property would be populated\. The 'strictness' is an optional parameter to perform \(higher number\) or ignore \(lower number\) of additional intelligence checks\. The possible values for 'strictness' are 0,1 and 2\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**email** |  required  | Email to query for reputation information | string |  `email` 
**fast** |  optional  | Enables or disables SMTP check with the mail service provider | boolean | 
**suggest\_domain** |  optional  | Force analyze if the email address's domain has a typo and should be corrected to a popular mail service | boolean | 
**timeout** |  optional  | Maximum number of seconds to wait for a reply from a mail service provider | numeric | 
**strictness** |  optional  | Sets how strictly spam traps and honeypots are detected by system \(Possible Values\: 0, 1 and 2\) | numeric | 
**abuse\_strictness** |  optional  | Set the strictness level for machine learning pattern recognition of abusive email addresses | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.email | string |  `email` 
action\_result\.parameter\.fast | boolean | 
action\_result\.parameter\.timeout | numeric | 
action\_result\.parameter\.suggest\_domain | boolean | 
action\_result\.parameter\.strictness | numeric | 
action\_result\.parameter\.abuse\_strictness | numeric | 
action\_result\.data\.\*\.valid | boolean | 
action\_result\.data\.\*\.timeout | boolean | 
action\_result\.data\.\*\.disposable | boolean | 
action\_result\.data\.\*\.first\_name | string | 
action\_result\.data\.\*\.deliverability | string | 
action\_result\.data\.\*\.smtp\_score | numeric | 
action\_result\.data\.\*\.overall\_score | numeric | 
action\_result\.data\.\*\.catch\_all | boolean | 
action\_result\.data\.\*\.generic | boolean | 
action\_result\.data\.\*\.common | boolean | 
action\_result\.data\.\*\.dns\_valid | boolean | 
action\_result\.data\.\*\.honeypot | boolean | 
action\_result\.data\.\*\.frequent\_complainer | boolean | 
action\_result\.data\.\*\.suspect | boolean | 
action\_result\.data\.\*\.recent\_abuse | boolean | 
action\_result\.data\.\*\.fraud\_score | numeric | 
action\_result\.data\.\*\.leaked | boolean | 
action\_result\.data\.\*\.suggested\_domain | string | 
action\_result\.data\.\*\.first\_seen\.human | string | 
action\_result\.data\.\*\.domain\_age\.human | string | 
action\_result\.data\.\*\.spam\_trap\_score | string | 
action\_result\.data\.\*\.sanitized\_email | string | 
action\_result\.data\.\*\.request\_id | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.Message | string | 
action\_result\.summary\.Status\_Code | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'url checker'
Queries IPQualityScore's malicious URL scanner API

Type: **investigate**  
Read only: **True**

If URL information is unavailable in IPQualityScore, only 'url' and 'in\_database' property would be populated\. The 'strictness' is an optional parameter to perform \(higher number\) or ignore \(lower number\) of additional intelligence checks\. The possible values for 'strictness' are 0,1 and 2\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**url** |  required  | URL to query for reputation information | string |  `url` 
**strictness** |  optional  | How strict should we scan this URL? \(Possible Values\: 0, 1 and 2\) | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.strictness | numeric | 
action\_result\.parameter\.url | string |  `url` 
action\_result\.data\.\*\.message | string | 
action\_result\.data\.\*\.success | boolean | 
action\_result\.data\.\*\.unsafe | boolean | 
action\_result\.data\.\*\.domain | string | 
action\_result\.data\.\*\.ip\_address | string |  `ip` 
action\_result\.data\.\*\.server | string | 
action\_result\.data\.\*\.content\_type | string | 
action\_result\.data\.\*\.status\_code | numeric | 
action\_result\.data\.\*\.page\_size | numeric | 
action\_result\.data\.\*\.domain\_rank | numeric | 
action\_result\.data\.\*\.dns\_valid | boolean | 
action\_result\.data\.\*\.parking | boolean | 
action\_result\.data\.\*\.spamming | boolean | 
action\_result\.data\.\*\.malware | boolean | 
action\_result\.data\.\*\.phishing | boolean | 
action\_result\.data\.\*\.suspicious | boolean | 
action\_result\.data\.\*\.risk\_score | numeric | 
action\_result\.data\.\*\.request\_id | string | 
action\_result\.status | string | 
action\_result\.summary\.Message | string | 
action\_result\.summary\.Status\_Code | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'ip reputation'
Queries IPQualityScore's Proxy and VPN detection API

Type: **investigate**  
Read only: **True**

If URL information is unavailable in IPQualityScore, only 'message' and 'status\_code' properties would be populated\. The 'strictness' is an optional parameter to perform \(higher number\) or ignore \(lower number\) of additional intelligence checks\. The possible values for 'strictness' are 0,1 and 2\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**ip** |  required  | IP to query for reputation information | string |  `ip` 
**strictness** |  optional  | How in depth \(strict\) do you want this query to be? \(Possible Values\: 0, 1 and 2\) | numeric | 
**user\_agent** |  optional  | Additional checks against bots | string | 
**user\_language** |  optional  | Additional risk evaluation | string | 
**fast** |  optional  | Certain forensic checks are skipped | boolean | 
**mobile** |  optional  | Specifies if this lookup should be treated as a mobile device | boolean | 
**allow\_public\_access\_points** |  optional  | Specifies if this lookup should be treated as a mobile device | boolean | 
**lighter\_penalties** |  optional  | Enable this setting to lower detection rates and Fraud Scores for mixed quality IP addresses | boolean | 
**transaction\_strictness** |  optional  | Adjusts the weights for penalties applied due to irregularities | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.strictness | numeric | 
action\_result\.parameter\.user\_agent | string | 
action\_result\.parameter\.user\_language | string | 
action\_result\.parameter\.fast | boolean | 
action\_result\.parameter\.mobile | boolean | 
action\_result\.parameter\.allow\_public\_access\_points | boolean | 
action\_result\.parameter\.lighter\_penalties | boolean | 
action\_result\.parameter\.transaction\_strictness | boolean | 
action\_result\.parameter\.ip | string |  `ip` 
action\_result\.data\.\*\.message | string | 
action\_result\.data\.\*\.success | boolean | 
action\_result\.data\.\*\.fraud\_score | numeric | 
action\_result\.data\.\*\.country\_code | string | 
action\_result\.data\.\*\.city | string | 
action\_result\.data\.\*\.region | string | 
action\_result\.data\.\*\.ISP | string | 
action\_result\.data\.\*\.organization | string | 
action\_result\.data\.\*\.ASN | numeric | 
action\_result\.data\.\*\.latitude | numeric | 
action\_result\.data\.\*\.longitude | numeric | 
action\_result\.data\.\*\.is\_crawler | boolean | 
action\_result\.data\.\*\.timezone | string | 
action\_result\.data\.\*\.host | string | 
action\_result\.data\.\*\.proxy | boolean | 
action\_result\.data\.\*\.vpn | boolean | 
action\_result\.data\.\*\.tor | boolean | 
action\_result\.data\.\*\.active\_vpn | boolean | 
action\_result\.data\.\*\.active\_tor | boolean | 
action\_result\.data\.\*\.connection\_type | string | 
action\_result\.data\.\*\.recent\_abuse | boolean | 
action\_result\.data\.\*\.abuse\_velocity | string | 
action\_result\.data\.\*\.bot\_status | boolean | 
action\_result\.data\.\*\.mobile | boolean | 
action\_result\.data\.\*\.country\_code | string | 
action\_result\.data\.\*\.fraud\_score | numeric | 
action\_result\.data\.\*\.request\_id | string | 
action\_result\.data\.\*\.operating\_system | string | 
action\_result\.status | string | 
action\_result\.summary\.Message | string | 
action\_result\.summary\.Status\_Code | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 