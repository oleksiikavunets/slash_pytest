import slash


@slash.tag('tags_speed_slash_class')
class Tags(slash.Test):
    method = slash.tag("tags_speed_slash_method")

    @method
    def test_tag_simple(self):
        assert 1 == 0

    @method
    def test_tag_simple1(self):
        assert 1 == 0

    @method
    def test_tag_simple2(self):
        assert 1 == 0

    @method
    def test_tag_simple3(self):
        assert 1 == 0

    @method
    def test_tag_simple4(self):
        assert 1 == 0

    @method
    def test_tag_simple5(self):
        assert 1 == 0

    @method
    def test_tag_simple6(self):
        assert 1 == 0

    @method
    def test_tag_simple7(self):
        assert 1 == 0

    @method
    def test_tag_simple8(self):
        assert 1 == 0

    @method
    def test_tag_simple9(self):
        assert 1 == 0
