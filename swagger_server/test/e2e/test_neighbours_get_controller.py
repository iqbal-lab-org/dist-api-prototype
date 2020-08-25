from hypothesis import given

from swagger_server.models import Sample, NeighbourRelationship
from swagger_server.test.strategies import samples, experiment_ids, nearest_leaves


@given(experiment_id=experiment_ids())
def test_getting_neighbours_of_non_existent_sample(experiment_id, get_neighbours):
    assert get_neighbours(experiment_id).status_code == 404


@given(sample=samples())
def test_getting_non_existent_neighbours(sample, create_sample, get_neighbours, sample_graph):
    try:
        create_sample(sample, ensure=True)

        assert get_neighbours(sample.experiment_id).status_code == 404
    finally:
        sample_graph.delete_all()


@given(sample=samples(must_have_neighbours=True), random_leaf=nearest_leaves())
def test_getting_neighbours_of_existing_sample(sample, random_leaf, create_leaf, create_sample, get_neighbours, sample_graph):
    try:
        create_leaf(random_leaf, ensure=True)
        for neighbour in sample.nearest_neighbours:
            neighbour_sample = Sample(neighbour.experiment_id, nearest_leaf_node=random_leaf)
            create_sample(neighbour_sample, ensure=True)

        created = Sample.from_dict(create_sample(sample, ensure=True).json)
        retrieved = [NeighbourRelationship.from_dict(x) for x in get_neighbours(sample.experiment_id, ensure=True).json]

        assert len(created.nearest_neighbours) == len(retrieved)
        for neighbour in created.nearest_neighbours:
            neighbour_relationship = [x for x in retrieved if x.neighbour.experiment_id == neighbour.experiment_id][0]
            assert neighbour_relationship.distance == neighbour.distance
            assert neighbour_relationship.neighbour.leaf_id == random_leaf.leaf_id
    finally:
        sample_graph.delete_all()
