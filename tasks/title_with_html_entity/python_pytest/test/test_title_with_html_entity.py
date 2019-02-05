import pytest


@pytest.mark.usefixtures("setup")
class Test:
    def test_verify_title(self):
        title_actual = self.driver.title.encode('ascii', 'xmlcharrefreplace')
        title_expected = 'Blog Tool, Publishing Platform, and CMS &#8212; WordPress'
        assert title_expected == title_actual
