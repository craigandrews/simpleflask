import pytest
import responses
from critics import URL, get_critics, pick_random_critic
from data import expected_result
import json


@responses.activate
def test_all_critics():
    responses.add(responses.GET, URL, json=expected_result, status=200)
    query = get_critics()
    expected = expected_result, expected_result["num_results"]
    assert query == expected


@responses.activate
def test_pick_random_critic():
    responses.add(responses.GET, URL, json=expected_result, status=200)
    random_id = pick_random_critic(id)
    assert random_id != None