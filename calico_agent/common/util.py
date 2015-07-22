#!/usr/bin/env python
# encoding: utf-8

import os
import sh

CALICOCTL_PATH = os.environ.get('CALICOCTL_PATH', '/usr/bin/calicoctl')
calicoctl = sh.Command(CALICOCTL_PATH).bake(_env=os.environ)
