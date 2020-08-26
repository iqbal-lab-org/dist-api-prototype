# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Neighbour(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, experiment_id=None, distance=None, leaf_id=None):  # noqa: E501
        """Neighbour - a model defined in OpenAPI

        :param experiment_id: The experiment_id of this Neighbour.  # noqa: E501
        :type experiment_id: str
        :param distance: The distance of this Neighbour.  # noqa: E501
        :type distance: int
        :param leaf_id: The leaf_id of this Neighbour.  # noqa: E501
        :type leaf_id: str
        """
        self.openapi_types = {
            'experiment_id': str,
            'distance': int,
            'leaf_id': str
        }

        self.attribute_map = {
            'experiment_id': 'experiment_id',
            'distance': 'distance',
            'leaf_id': 'leaf_id'
        }

        self._experiment_id = experiment_id
        self._distance = distance
        self._leaf_id = leaf_id

    @classmethod
    def from_dict(cls, dikt) -> 'Neighbour':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Neighbour of this Neighbour.  # noqa: E501
        :rtype: Neighbour
        """
        return util.deserialize_model(dikt, cls)

    @property
    def experiment_id(self):
        """Gets the experiment_id of this Neighbour.


        :return: The experiment_id of this Neighbour.
        :rtype: str
        """
        return self._experiment_id

    @experiment_id.setter
    def experiment_id(self, experiment_id):
        """Sets the experiment_id of this Neighbour.


        :param experiment_id: The experiment_id of this Neighbour.
        :type experiment_id: str
        """
        if experiment_id is None:
            raise ValueError("Invalid value for `experiment_id`, must not be `None`")  # noqa: E501

        self._experiment_id = experiment_id

    @property
    def distance(self):
        """Gets the distance of this Neighbour.


        :return: The distance of this Neighbour.
        :rtype: int
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this Neighbour.


        :param distance: The distance of this Neighbour.
        :type distance: int
        """
        if distance is None:
            raise ValueError("Invalid value for `distance`, must not be `None`")  # noqa: E501

        self._distance = distance

    @property
    def leaf_id(self):
        """Gets the leaf_id of this Neighbour.


        :return: The leaf_id of this Neighbour.
        :rtype: str
        """
        return self._leaf_id

    @leaf_id.setter
    def leaf_id(self, leaf_id):
        """Sets the leaf_id of this Neighbour.


        :param leaf_id: The leaf_id of this Neighbour.
        :type leaf_id: str
        """

        self._leaf_id = leaf_id
