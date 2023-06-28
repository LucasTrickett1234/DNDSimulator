import numpy as np
from RegionModule import Region


class World:
    """
    Incorporates multiple Region Modules, models ties, relations, trading...

    :param regions
    :param relations_map: Nodal grpah expressing interregional relationships
                          Govern population change, resource trading, war

    :method add_region:
    :method remove_region: Remove region to world instance
    :method war_characteristic: Models war between countries (countries that
                                are included dtermined from relations_map)
    """

    def init(self):
        self.regions = dict()
        self.relations_map = [[]]

    def get_region_id(self, name):
        """
        Returns the id associated with a given region
        - Returns NoneType if region doesn't exist

        :param name: Name of queied region
        """
        # for region_inst in

    def add_region(self, name, intraregion_data, interregional_data):
        """
        WorldClass method: Add region alongside any external metadata

        :param string name: Region name
        :param Region region_meta: Region Data as defined in RegionModule file
        :param dict ext_data: Relationship score (x) for region (x: -1 to 1)
                               bidirectional, type is {'region_id1': x, ...}
        """

        region_inst = dict()
        region_inst['name'] = name
        region_inst['intraregional'] = intraregion_data
        region_inst['interregional'] = interregional_data

        region_id = id(region_inst)
        self.regions[region_id] = region_inst

        self.update_relations()

    def remove_region(self, region_id: int):
        """
        WorldClass method: Add region alongside any external metadata

        :param string name: Region name
        :param Region region_meta: Region Data as defined in RegionModule file
        :param dict ext_data: Relationship score (x) for region (x: -1 to 1)
                               bidirectional, type is {'region_id1': x, ...}
        """

        self.regions.pop(region_id)
        self.update_relations()

    def update_relations(self):
        """
        Alot of math relies on

        :param string name: Region name
        :param Region region_meta: Region Data as defined in RegionModule file
        :param dict relations: Relationship score (x) for region (x: -1 to 1)
                               structure follows {'region_id1': x, ...}
        """

    def war_characteristic(self, region_id1, region_id2):
        """
        Effects of war (propagating to resources, population growth, gdp...)
        - Countries join if

        :param string name: Region name
        :param int region_id1: Region Data as defined in RegionModule file
        :param dict relations: Relationship score (x) for region (x: -1 to 1)
                               structure follows {'region_id1': x, ...}
        """
