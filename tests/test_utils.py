

from app.utils import to_usd

def test_to_usd():
    assert to_usd(6.679) == "$6.68"
