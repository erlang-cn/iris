# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from iris.test_case import *


class Test(BaseTest):

    def __init__(self):
        BaseTest.__init__(self)
        self.meta = 'This test creates dynamic regions from patterns.'

    def run(self):
        cat1_pattern = Pattern('cat1.png')
        cat2_pattern = Pattern('cat2.png')
        dog1_pattern = Pattern('dog1.png')
        dog2_pattern = Pattern('dog2.png')
        png1 = Pattern('1.png')
        png2 = Pattern('2.png')

        r = create_region_from_patterns(left=png1, right=png2)
        logger.debug('Region x, y, w, h: %s %s %s %s' % (r.x, r.y, r.width, r.height))
        print('Text in URL bar: %s' % r.text(with_image_processing=False))
        assert_equal(self, r.text(with_image_processing=False),
                     ' 127.0.0.1:2000/?current=1&total=1&title=create region',
                     'URL should be equal to %s' % r.text(with_image_processing=False))
        hover(r.find(' 127.0.0.1:2000/?current=1&total=1&title=create region'))

        test_url = self.get_asset_path('test.htm')
        navigate(test_url)
        logger.debug('Navigate to URL: %s' % test_url)
        print('Text in URL bar: %s' % r.text(with_image_processing=False))

        test_string_cat = 'This is a cat'
        r1 = create_region_from_patterns(left=cat1_pattern, right=cat2_pattern)
        region_text = r1.text(with_image_processing=False)
        logger.debug('Region x, y, w, h: %s %s %s %s' % (r1.x, r1.y, r1.width, r1.height))
        print('Text in region: %s' % region_text)
        assert_true(self, test_string_cat in region_text, 'Can find cat text')
        assert_false(self, 'Dog' in region_text, 'Should not find Dog in cat text')

        test_string_dog = 'This is a dog'
        r2 = create_region_from_patterns(left=dog1_pattern, right=dog2_pattern)
        region_text = r2.text(with_image_processing=False)
        logger.debug('Region x, y, w, h: %s %s %s %s' % (r2.x, r2.y, r2.width, r2.height))
        print('Text in region: %s' % region_text)
        assert_true(self, test_string_dog in region_text, 'Can find dog text')
        assert_false(self, 'Cat' in region_text, 'Should not find Cat in dog text')

        navigate('google.com')
        logger.debug('Navigate to URL: google.com')
        logger.debug('Text in URL bar: %s' % r.text(False))

        navigate(test_url)
        logger.debug('Navigate to URL: %s' % test_url)
        print('Text in URL bar: %s' % r.text(False))

        navigate('12345')
        logger.debug('Navigate to URL: 12345')
        print('Text in URL bar: %s' % r.text(False))

        return
