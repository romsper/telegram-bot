import requests

def users_data(query):
    id, username, email, phone = query.split(' ')

    user = {'jsonrpc': '2.0','method': 'upsert','params': {
    'id': int(id),'typeId': 1,'username': username,'email': email,'phone': phone,
    'avatar': 'http://{HOST}/avatar/xs/0/11/0112a7ea1776757cadba7119f4ccf116.jpg',
    'vkId': 123123123,'okId': 123123123},'id': 1}

    r = requests.post('http://{HOST}/create', json=user)

    return r.text