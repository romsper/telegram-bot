import requests

def search_advert(query):
    search_query = query.replace(' ', '+')
    adverts = []

    response = requests.get(
        'http://{HOST}/search?query='
        + search_query
        + '&ignored_props=738&show_count=5&range_rule=815&result_properties=p-2&return_filter=1&schema=json')

    advertItems = response.json()
    advertCount = len(advertItems['answer']['result']['search_result']['documents'])

    for item in range(0, advertCount):
        adverts.append(
            'https://am.ru/' + advertItems['answer']['result']['search_result']['documents'][item]['DOC_ID']['data'])
    return adverts