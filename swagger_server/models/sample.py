# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.nearest_leaf import NearestLeaf
from swagger_server.models.neighbour import Neighbour
from swagger_server import util

from swagger_server.models.nearest_leaf import NearestLeaf  # noqa: E501
from swagger_server.models.neighbour import Neighbour  # noqa: E501

class Sample(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, experiment_id=None, nearest_neighbours=None, nearest_leaf_node=None):  # noqa: E501
        """Sample - a model defined in OpenAPI

        :param experiment_id: The experiment_id of this Sample.  # noqa: E501
        :type experiment_id: str
        :param nearest_neighbours: The nearest_neighbours of this Sample.  # noqa: E501
        :type nearest_neighbours: List[Neighbour]
        :param nearest_leaf_node: The nearest_leaf_node of this Sample.  # noqa: E501
        :type nearest_leaf_node: NearestLeaf
        """
        self.openapi_types = {
            'experiment_id': str,
            'nearest_neighbours': List[Neighbour],
            'nearest_leaf_node': NearestLeaf
        }

        self.attribute_map = {
            'experiment_id': 'experiment_id',
            'nearest_neighbours': 'nearest-neighbours',
            'nearest_leaf_node': 'nearest-leaf-node'
        }

        self._experiment_id = experiment_id
        self._nearest_neighbours = nearest_neighbours
        self._nearest_leaf_node = nearest_leaf_node

    @classmethod
    def from_dict(cls, dikt) -> 'Sample':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Sample of this Sample.  # noqa: E501
        :rtype: Sample
        """
        return util.deserialize_model(dikt, cls)

    @property
    def experiment_id(self):
        """Gets the experiment_id of this Sample.


        :return: The experiment_id of this Sample.
        :rtype: str
        """
        return self._experiment_id

    @experiment_id.setter
    def experiment_id(self, experiment_id):
        """Sets the experiment_id of this Sample.


        :param experiment_id: The experiment_id of this Sample.
        :type experiment_id: str
        """
        if experiment_id is None:
            raise ValueError("Invalid value for `experiment_id`, must not be `None`")  # noqa: E501

        self._experiment_id = experiment_id

    @property
    def nearest_neighbours(self):
        """Gets the nearest_neighbours of this Sample.


        :return: The nearest_neighbours of this Sample.
        :rtype: List[Neighbour]
        """
        return self._nearest_neighbours

    @nearest_neighbours.setter
    def nearest_neighbours(self, nearest_neighbours):
        """Sets the nearest_neighbours of this Sample.


        :param nearest_neighbours: The nearest_neighbours of this Sample.
        :type nearest_neighbours: List[Neighbour]
        """

        self._nearest_neighbours = nearest_neighbours

    @property
    def nearest_leaf_node(self):
        """Gets the nearest_leaf_node of this Sample.


        :return: The nearest_leaf_node of this Sample.
        :rtype: NearestLeaf
        """
        return self._nearest_leaf_node

    @nearest_leaf_node.setter
    def nearest_leaf_node(self, nearest_leaf_node):
        """Sets the nearest_leaf_node of this Sample.


        :param nearest_leaf_node: The nearest_leaf_node of this Sample.
        :type nearest_leaf_node: NearestLeaf
        """

        self._nearest_leaf_node = nearest_leaf_node
