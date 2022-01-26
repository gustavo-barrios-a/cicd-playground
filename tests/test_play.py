from playground.play import get_json


def test_get_json(mock_response):
    result = get_json("http://fakeurl")
    assert result["mock_key"] == "mock_response"
