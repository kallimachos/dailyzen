import dailyzen

good_url = dailyzen.URL
bad_url = 'http://example.com'


def test_dailyzen():
    assert dailyzen.main(good_url) == 0
    assert dailyzen.main(bad_url) == 1
