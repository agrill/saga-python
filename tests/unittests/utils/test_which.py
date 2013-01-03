
__author__    = "Ole Christian Weidner"
__copyright__ = "Copyright 2012, Ole Christian Weidner"
__license__   = "MIT"

from saga.utils.which import *

def test_which():
    """ Test if 'which' can find things
    """
    assert which('doesnotexistatall') is None
    if os.path.isfile('/usr/bin/date'):
        assert which('date') == '/usr/bin/date'
    if os.path.isfile('/bin/date'):
        assert which('date') == '/bin/date'


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

