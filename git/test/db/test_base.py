# Copyright (C) 2010, 2011 Sebastian Thiel (byronimo@gmail.com) and contributors
#
# This module is part of GitDB and is released under
# the New BSD License: http://www.opensource.org/licenses/bsd-license.php
from lib import *
from git.db import RefSpec

class TestBase(TestDBBase):

	needs_ro_repo = False

	@with_rw_directory
	def test_basics(self, path):
		self.failUnlessRaises(ValueError, RefSpec, None, None)
		rs = RefSpec(None, "something")
		assert rs.force == False
		assert rs.delete_destination()
		assert rs.source is None
		assert rs.destination == "something"
		
