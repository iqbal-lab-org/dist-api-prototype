import connexion

from swagger_server.__main__ import get_db
from swagger_server.models import ApiResponse
from swagger_server.models.sample import Sample  # noqa: E501
from swagger_server.orm.DistanceORM import DistanceORM


def distance_post(body):  # noqa: E501
    """distance_post

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        sample = Sample.from_dict(connexion.request.get_json())  # noqa: E501

        within_distance = get_db().query(DistanceORM).filter(
            DistanceORM.s1 == sample.experiment_id and DistanceORM.d < 5
        ).all()

        return ApiResponse(
            type='distance',
            sub_type='nearest-neighbor',
            result={sample.s2: sample.d for sample in within_distance}
        )
