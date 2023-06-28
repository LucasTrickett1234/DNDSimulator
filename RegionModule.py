import numpy as np

# regionstatistics
# = dictionary typ
#             - Holds RegionStatistics

STANDARD_LESLIE = [[],
                   [],
                   []]


class Region:
    "Data representation of a given region, used in modelling purposes"

    def init(self, regionstatistics, age=0):
        "Data representation of a given region, used in modelling purposes"
        self.age = age
        self.regionstatistics = regionstatistics

    def growth(self, MIGRATION_FACTOR):
        "Data representation of a given region, used in modelling purposes"
        self.age += 1
        curr_distribution = self.regionstatistics['region_distribution']
        next_distribution = np.multiply(MIGRATION_FACTOR, curr_distribution)
        curr_distribution = next_distribution
