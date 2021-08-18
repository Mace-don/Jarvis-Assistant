import requests


class Search1:

    def __init__(self,command):
        #self.logger = logger
        self.command = command

    def ScaleSerpSearch(self):
        query = self.command
        params = {
            'api_key': '7B8F0ED85D804F819D10AF7757727805',
            'q': query
        }
        try:
            api_result = requests.get('https://api.scaleserp.com/search',params).json()
            answer = api_result["answer_box"]["answers"][0]["answer"]
            print(answer)
        except Exception as e:
            pass


A = Search1("president of china")
A.ScaleSerpSearch()