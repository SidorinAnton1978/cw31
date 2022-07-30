import pytest

import app


class TestApi:

    @pytest.fixture
    def app_instance(self):
        return app

    def test_foo(self):
        assert 1 == 1
