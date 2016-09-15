import json
import logging
import requests
import sys
if sys.version_info[0] < 3:
    import urllib
else:
    import urllib.parse as urllib

log = logging.getLogger(__name__)
class FullContact(object):
    def __init__(self, client_id, client_secret, username, password):
        self.base_url = 'http://cabapi.elb.fullcontact.com/'
        self.oauth_token_url = 'http://oauth.elb.fullcontact.com/v3/oauth.makeAccessToken/'
        self.post_endpoints = {
            'abs_get': 'v3/abs.get',
            'account_get': 'v3/account.get',
            'contacts_create': 'v3/contacts.create',
            'contacts_update': 'v3/contacts.update',
            'contacts_get': 'v3/contacts.get',
            'contacts_scroll': 'v3/contacts.scroll',
            'contacts_search': 'v3/contacts.search',
            'contacts_manageTags': 'v3/contacts.manageTags',
            'contacts_uploadPhoto': 'v3/contacts.uploadPhoto',
            'contacts_delete': 'v3/contacts.delete',
            'tags_get': 'v3/tags.get',
            'tags_scroll': 'v3/tags.scroll',
            'tags_create': 'v3/tags.create',
            'tags_update': 'v3/tags.update',
            'tags_delete': 'v3/tags.delete'
        }
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password
        self.scope = "account.read,contacts.write,contacts.read,tags.read,tags.write"

        self.access_token = self.credentials_get()['access_token']
        for endpoint in self.post_endpoints:
            method = lambda endpoint=endpoint, **kwargs: self.api_post(endpoint, **kwargs)
            setattr(self, endpoint, method)
            # print method(endpoint).content
            print method()
            print endpoint

    def credentials_get(self):
        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'username': self.username,
            'password': self.password,
            'scope': self.scope
        }

        r = requests.post(self.oauth_token_url, data=payload)
        return r.json()

    def api_post(self, endpoint, **kwargs):
        """ Makes a FullContact API call
        Formats and submits a request to the specified endpoint, appending
        any key-value pairs passed in kwargs as a url query parameter.
        Args:
            endpoint: shortname of the API endpoint to use.
            strict: if True, throw an error
            **kwargs: a dict of query parameters to append to the request.
        Returns:
            A Requests object containing the result of the API call. Interact
            with the return value of this function as you would with any
            other Requests object.
        Raises:
            KeyError: the specified endpoint was not recognized. Check the
                docs.
            Requests.Exceptions.*: an error was raised by the Requests
                module.
        """
        endpoint = self.base_url + self.post_endpoints[endpoint]
        headers = {"Authorization": "Bearer %s" %self.access_token}
        print kwargs
        if kwargs is not None:
            return requests.post(endpoint, data=json.dumps(kwargs.get('data')), headers=headers)
        return requests.post(endpoint, data=kwargs, headers=headers)



