from elasticsearch import Elasticsearch


class DataFetcher:

    def __init__(self, ip="15.236.56.178", port="9200", index="original", urlSuffixe="/_search"):
        self.ip = ip
        self.port = port
        self.index = index
        self.urlSuffixe = urlSuffixe
        full_path = self.ip + ":" + self.port
        self.elastic = Elasticsearch(full_path)
        self.search_param = {}

    def fetchFromElastic(self):
        return self.elastic.search(index=self.index, body="")

    def format(self, data):
        return

    def setFilter(self, filters):
        pass

    def setDefaultFilter(self):
        self.search_param = {
            "query": {
                "terms": {
                    "_id": [1234, 42]
                }
            }
        }

    def setIndex(self, index):
        self.index = index
