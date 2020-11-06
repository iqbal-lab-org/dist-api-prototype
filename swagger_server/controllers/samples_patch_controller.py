import connexion

from swagger_server.db import get_db
from swagger_server.exceptions import NotFound
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.sample import Sample  # noqa: E501
from swagger_server.ogm.mappers import SampleNode


def samples_id_patch(id, sample=None):  # noqa: E501
    """samples_id_patch

    Update a sample based on its ID. # noqa: E501

    :param id: 
    :type id: str
    :param sample: New sample data
    :type sample: dict | bytes

    :rtype: Sample
    """
    if connexion.request.is_json:
        sample = Sample.from_dict(connexion.request.get_json())  # noqa: E501

    sample_graph = get_db()

    try:
        node = SampleNode.update(id, sample_graph, new_id=sample.experiment_id)
    except NotFound:
        return Error(404, 'Not found'), 404
    else:
        model = node.to_model()
        return model, 200, {'location': model.experiment_id}
