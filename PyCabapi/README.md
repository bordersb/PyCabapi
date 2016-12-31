# FullContact Python CabAPI Client

Contact creation, updation, deletion, etc. for FullContact address books.


## Installation

```
pip install Cabapi.py
```

1. Register a new application with FullContact via [https://alpha.fullcontact.com/apps](https://alpha.fullcontact.com/apps).

2. Copy the "Client ID" and "Client Secret" to use in your FullContact Req Object



3. Run the program

  ```
  python

  >>> from cabapi import FullContact
  fc = FullContact({client_id}, {client_secret}, {username}, {password})
  ```
*****************************************************************
example commands:

  ```
>>> f.account_get()
{}
<Response [200]>
f.account_get().content

>>> f.account_get().content
{}
'{"account":{"accountId": .....
             }}'
```
All three of these commands will return the same data object.

```
>>> contact = {'contact':
                    {'contactData':
                             {'name':
                                  {'givenName':'John','familyName':'Belushi'}}}}


>>> f.contacts_create(data=contact).content
#or
>>>fc.contacts_get(data={'contactIds': ['XXXX']}).content
#or
>>> blah = {'searchQuery': 'John'}
>>> fc.contacts_search(data=blah).content

'{"contact":{"contactData":{"name":{"givenName":"John","familyName":"Belushi"}},
"contactId":"XXXX","etag":"XXXXXXX","created":"2016-09-15T17:25:01.409Z","updated":"2016-09-15T17:25:01.409Z","contactMetadata":{}}}\n'
```


```
>>> fc.contacts_delete(data={'contactId': 'XXXX',
                         'etag': 'XXXXXXX'}).content
''
```
