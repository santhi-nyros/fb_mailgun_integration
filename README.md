# integrate_fb_with_mailgun

Flaskapp  folder is script for getting new leads from facebook page and add lead to mail-gun mail list and sent a mail to lead.
------------------------------------------------------------------------------------
@@Enviroment Setup process@@

First we need to create a virtual enviroment for installing requirment.txt
In python we use following commands for cretaing virtual enviroment
$virtualenv <env_name>

activate the env with following command
$ source <env_name>/bin/activate

Then we need to install all packages on requirment.txt file

$pip install -r requirement.txt

or install one by one

$pip install Flask

$pip install facebookads

so on

---------------------------------------------------------------------------

@@ Key changes in method @@

I have added my sample account keys of facebook and mail-gun for run the script,
Because I don't have permisiions to add webhook to your facebook page.

You need to change those keys with your account keys

Here is the guidelines
-----------------------
flaskapp/hello.py


	def hello_world(formId):
	    # Facebook app keys
	    my_app_id = <YOUR_FB_APP_ID>
	    my_app_secret = <YOUR_FB_APP_SECRET>
	    my_access_token = <YOUR_FB_APP_ACCESS_TOKEN>



flaskapp/hello.py
	def add_list_member(email,name):
		#Mail-gun api keys
		key = <YOUR_MAILGUN_API_KEY>
		domain = <YOUR_MAILGUN_DOMAIN> if it is sandbox domain, It will not sent mail to another mail ids, It's sends only authorized mail ids only.

    def hello_world(formId):
        # Facebook app keys
	my_app_id = <YOUR_FB_APP_ID>
	my_app_secret = <YOUR_FB_APP_SECRET>
	my_access_token = <YOUR_FB_APP_ACCESS_TOKEN>


flaskapp/hello.py

    def add_list_member(email,name):
        #Mail-gun api keys
		key = <YOUR_MAILGUN_API_KEY>
		domain = <YOUR_MAILGUN_DOMAIN>
		If it is sandbox domain, It will not sent mail to another mail ids, It's sends only authorized mail ids only.


Server setup:
     Enviroment settings and keys settings are completed,
     Now you need to add and run these files on your server(ex: AWS, heroku etc)and **you will get url for this app**.


    I have added in heroku for testing purpose.
    My heroku url for this app : https://getfbleadsapp.herokuapp.com

-----------------------------------------------------------------------------

Once you done the setup and run the app successfully, you need to add php app for webhook callback url

Setup and run the php-gettting-started app into your server and made few changes on webhook.php file

Here is the changes what will you make

php-gettting-started/web/webhook.php

changes the verify token what you given while creating webhook on facebook page
I have given 'abc123' in webhook.php


	if ($verify_token == '<YOUR_VERIFY_TOKEN>'){
		echo $challenge;
	}



You will get app url already(look at Server setup) , we need to change this url with your url.

    $auth = curl_init("<YOUR_APP_URL>/".$frm_id);

I have deploy this php app also in heroku and got a url.

I have given that url  while cretation of webhook on my sample page like


	Callback URL
	https://still-scrubland-39984.herokuapp.com/webhook.php

	Verify Token
	abc123

Callback URL: https://still-scrubland-39984.herokuapp.com/webhook.php

Verify Token: abc123


----------------------------------------------------------------------------

Work flow

we created a webhook for leadgen on facebook page with callback_url and Verify Token

when new lead creates that time the callback url fires functionality of webhook.php page

In webhook.php fires the app url with lead_gen data

then the app gets the new lead details and added to mail-gun mail list and send a mail to lead.

This is the working process.

-----------------------------------------------------------------------------


For creating webhook on facebook page refer the following urls,

https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving/v2.8

Follow the video in this url or
Run the follow using curl or graph-api explorer "https://developers.facebook.com/tools/explorer/198409723950483?method=GET&path=&version=v2.8"

curl \
-F "object=page" \
-F "callback_url=https://www.yourcallbackurl.com" \
-F "fields=leadgen" \
-F "verify_token=abc123" \
-F "access_token=<APP_ACCESS_TOKEN>" \
"https://graph.facebook.com/<API_VERSION>/<APP_ID>/subscriptions"


Thankyou.
