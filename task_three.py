"""
1. TODO - import all resource classes here
2. TODO - get count of each resource
3. TODO - get singular resource URL from each resource
    - for example,
    - hit plural URL of starships and that will list all starships data
    - iterate on each starship data and capture singular URLs
    - all_starship_data = data.get("results")
    - you will iterate on `all_starship_data`,
4. TODO - pull data from random 3 "singular" resource URLs
    - utilize`utils` package to produce random 3 numbers from resource ids
    - and pull data for them
5. TODO - convert the script into CLI application
6. TODO - pretty print output (from pprint import pprint)
"""
from resources.films import Film
from resources.characters import Character
from resources.planets import Planet
from resources.species import Species
from resources.starships import Starship
from resources.vehicles import Vehicle

from models.datamodels.characters import Character_
from models.datamodels.films import Film_
from models.datamodels.planets import Planet_
from models.datamodels.starships import Starship_
from models.datamodels.vehicles import Vehicle_
from models.datamodels.species import Species_
from pprint import PrettyPrinter


if __name__ == "__main__":
    pp = PrettyPrinter(indent=4)

    # character info
    character_count = Character().get_count()
    character_data = Character().get_sample_data()
    pp.pprint(character_data)
    character_data = Character_(**character_data)
    character_urls = Character().get_urls()
    pp.pprint(character_urls)

    # film info
    film_count = Film().get_count()
    film_data = Film().get_sample_data()
    film_data = Film_(**film_data)
    film_urls = Film().get_urls()

    # planet info
    planet_count = Planet().get_count()
    planet_data = Planet().get_sample_data()
    planet_data = Planet_(**planet_data)
    planet_urls = Planet().get_urls()

    # species info
    species_count = Species().get_count()
    species_data = Species().get_sample_data()
    species_data = Species_(**species_data)
    species_urls = Species().get_urls()

    # vehicle info
    vehicle_count = Vehicle().get_count()
    # passing id_ = 4 as 1,2,3 are not present
    vehicle_data = Vehicle().get_sample_data(4)
    try:
        vehicle_data = Vehicle_(**vehicle_data)
    except TypeError:
        pass
    vehicle_urls = Vehicle().get_urls()

    # starship info
    starship_count = Starship().get_count()
    # passing id_ = 5 as 1,2,3,4 are not present
    starship_data = Starship().get_sample_data(5)
    try:
        starship_data = Starship_(**starship_data)
    except TypeError:
        pass
    starship_urls = Starship().get_urls()

    breakpoint()

