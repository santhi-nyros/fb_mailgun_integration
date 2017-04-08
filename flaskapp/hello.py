from flask import Flask
application = Flask(__name__)

import requests

from facebookads.api import FacebookAdsApi
from facebookads import objects
# from facebookads.adobjects.page import Page
from facebookads.adobjects.leadgenform import LeadgenForm


@application.route('/', defaults={'formId': None})
@application.route('/<formId>')
def hello_world(formId):
    # Facebook app keys
    my_app_id = '<YOUR_FB_APP_ID>'
    my_app_secret = '<YOUR_FB_APP_SECRET>'
    my_access_token = '<YOUR_FB_APP_ACCESS_TOKEN>'

    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

    if formId != None:
        form = LeadgenForm(formId)
        leads = form.get_leads()
        email = leads[0]['field_data'][0]['values'][0]
        name = leads[0]['field_data'][1]['values'][0]

        result = add_list_member(email,name);
        return 'Hello,formId:  {0}, {1}!'.format(formId,result)
    return 'hello Fb world'

def add_list_member(email,name):
    #Mailgu api key
    key = '<YOUR_MAILGUN_API_KEY>'
    domain = '<YOUR_MAILGUN_DOMAIN>'

    # adding lead mail to maillist in mailgun account
    mailList_url = "https://api.mailgun.net/v3/lists/santhi@{0}/members".format(domain)
    result = requests.post(mailList_url, auth=('api', key), data={
        'subscribed': True,
        'address': email,
        'name': name,
        'description': 'testing mail list'
    })

    # sending mail to lead
    request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(domain)
    request = requests.post(request_url, auth=('api', key), data={
        'from': 'santhi.nyros@gmail.com',
        'to': email
        'subject': 'Hello',
        'text': 'Hello {0}, This is a Testing mail from mailgun'.format(name)
    })
    return result


if __name__ == "__main__":
    application.run(host='0.0.0.0')
