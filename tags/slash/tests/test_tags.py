import slash


@slash.tag('REGRESSION')
class Tags(slash.Test):
    # tag created earlier
    earlier_created_tag = slash.tag('earlier created tag')
    smoke = slash.tag('smoke')

    # tagging by simple decorator
    @slash.tag('simple')
    @smoke
    def test_tag_simple(self):
        assert 1 == 0

    # tag has value
    @slash.tag('tagname', 'tagvalue')
    @smoke
    def test_tag_has_value(self):
        assert 1 == 0

    @earlier_created_tag
    def test_earlier_created_tag(self):
        assert 1 == 0
