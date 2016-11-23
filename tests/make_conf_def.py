#---------------------------------------
# IMPORTS
#---------------------------------------

import test

from pymake import *

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@target
@default_conf({ 'foo': '123' })
def my_target_1(conf):
    test.equal(conf.foo, '123', "conf.foo is incorrect")

@target(conf={ 'foo': '123' })
def my_target_2(conf):
    test.equal(conf.foo, 'xyz', "conf.foo is incorrect")

#---------------------------------------
# SCRIPT
#---------------------------------------

pymake({}              , [ 'my_target_1' ])
pymake({ 'foo': 'xyz' }, [ 'my_target_2' ])

test.success()
