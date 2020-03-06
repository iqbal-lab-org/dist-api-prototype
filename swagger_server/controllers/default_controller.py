import connexion
import six

from swagger_server.models.sample import Sample  # noqa: E501
from swagger_server import util


def distance_post(body):  # noqa: E501
    """distance_post

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Sample.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
