import urllib.request,json
from .models import Quote


# getting the quotes base url

base_url = None


def configure_request(app):
    global base_url

    base_url = app.config["QUOTES_API_URL"]


def get_quotes():
    '''
    Function that gets json response to our url request
    '''

    # get_quotes_url = base_url.format()

    with urllib.request.urlopen('http://quotes.stormconsultancy.co.uk/random.json') as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)
        quote_results= None
        quote_results=get_quotes_response
        quotes_results = process_results(get_quotes_response)

    return quotes_results


def process_results(quotes_list):
    '''
    Function that processes the quotes result and transform them to a list of Objects
    Args:
        quotes_list: A list of dictionaries that contain quote details
    Returns:
        quote_results: A list of quote objects
    '''

    quote_results = []

    quote=quotes_list
    author=quotes_list
    quote_dict=Quote(quote,author)
    quote_results.append(quote_dict.quote)


    return quote_results