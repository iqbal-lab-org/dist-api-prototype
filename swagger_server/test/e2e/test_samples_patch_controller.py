from hypothesis import given

from swagger_server.models import Sample
from swagger_server.test.strategies import samples


@given(sample=samples())
def test_patching_non_existent_samples(sample, patch_sample):
    assert patch_sample(sample.experiment_id, sample).status_code == 404


@given(sample=samples(), new_sample=samples())
def test_patching_samples(sample, new_sample, patch_sample, create_sample, create_leaf, get_resource, sample_graph):
    try:
        if sample.nearest_leaf_node:
            create_leaf(sample.nearest_leaf_node, ensure=True)
        if sample.nearest_neighbours:
            for neighbour in sample._nearest_neighbours:
                create_sample(neighbour, ensure=True)
        create_sample(sample, ensure=True)

        response = patch_sample(sample.experiment_id, new_sample)
        patched = Sample.from_dict(response.json)

        assert response.status_code == 200
        assert patched.experiment_id == new_sample.experiment_id
        assert patched.nearest_leaf_node == sample.nearest_leaf_node
        if sample.nearest_neighbours:
            for neighbour in patched.nearest_neighbours:
                assert neighbour in sample.nearest_neighbours
        else:
            assert not patched.nearest_neighbours

        from_location_header = Sample.from_dict(get_resource(response.location, ensure=True).json)
        assert from_location_header == patched
    finally:
        sample_graph.delete_all()