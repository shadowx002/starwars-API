#import sys
#sys.path.append('/home/shadow/velo01/StarWarsAPI')

from resources.base import ResourceBase
from utils.fetch_data import hit_url
from typing import Dict

_urls = []


class Planet(ResourceBase):
    """
    Planet class related functionality
    """

    def __init__(self) -> None:
        super().__init__()
        self.relative_url = "/api/planets"

    def get_count(self):
        print("Getting count...")
        complete_url = self.home_url + self.relative_url
        print(f"Fetching data from {complete_url}")
        response = hit_url(complete_url)
        print("Data fetched successfully")
        data = response.json()
        count = data.get("count")
        #breakpoint()
        return count

    def get_sample_data(self, id_ : int = 1) -> Dict:
        """

        Args:
            id_: sample id of the resource

        Returns:
            data (dict): output data from API endpoint

        """

        absolute_url = self.home_url + self.relative_url + f"/{id_}"
        response = hit_url(absolute_url)
        data = response.json()
        return data

    def get_urls(self):
        global _urls
        complete_url = self.home_url + self.relative_url
        response = hit_url(complete_url)
        data = response.json()
        all_data = data.get("results")
        for x in all_data:
            _urls.append(x.get("url"))
        return _urls