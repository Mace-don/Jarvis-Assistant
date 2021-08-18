from googlesearch import search
import webbrowser


def Search(query):
    url = list(search(query,num_results=1))
    return url[0]
