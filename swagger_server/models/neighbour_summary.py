# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class NeighbourSummary(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, experiment_id=None, leaf_id=None):  # noqa: E501
        """NeighbourSummary - a model defined in OpenAPI

        :param experiment_id: The experiment_id of this NeighbourSummary.  # noqa: E501
        :type experiment_id: str
        :param leaf_id: The leaf_id of this NeighbourSummary.  # noqa: E501
        :type leaf_id: str
        """
        self.openapi_types = {
            'experiment_id': str,
            'leaf_id': str
        }

        self.attribute_map = {
            'experiment_id': 'experiment_id',
            'leaf_id': 'leaf_id'
        }

        self._experiment_id = experiment_id
        self._leaf_id = leaf_id

    @classmethod
    def from_dict(cls, dikt) -> 'NeighbourSummary':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NeighbourSummary of this NeighbourSummary.  # noqa: E501
        :rtype: NeighbourSummary
        """
        return util.deserialize_model(dikt, cls)

    @property
    def experiment_id(self):
        """Gets the experiment_id of this NeighbourSummary.


        :return: The experiment_id of this NeighbourSummary.
        :rtype: str
        """
        return self._experiment_id

    @experiment_id.setter
    def experiment_id(self, experiment_id):
        """Sets the experiment_id of this NeighbourSummary.


        :param experiment_id: The experiment_id of this NeighbourSummary.
        :type experiment_id: str
        """
        if experiment_id is None:
            raise ValueError("Invalid value for `experiment_id`, must not be `None`")  # noqa: E501

        self._experiment_id = experiment_id

    @property
    def leaf_id(self):
        """Gets the leaf_id of this NeighbourSummary.


        :return: The leaf_id of this NeighbourSummary.
        :rtype: str
        """
        return self._leaf_id

    @leaf_id.setter
    def leaf_id(self, leaf_id):
        """Sets the leaf_id of this NeighbourSummary.


        :param leaf_id: The leaf_id of this NeighbourSummary.
        :type leaf_id: str
        """
        if leaf_id is None:
            raise ValueError("Invalid value for `leaf_id`, must not be `None`")  # noqa: E501

        self._leaf_id = leaf_id
