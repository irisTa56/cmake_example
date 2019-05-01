import yep

import cmake_example as m

yep.start('out.prof')

assert m.__version__ == '0.0.1'
assert m.add(1, 2) == 3
assert m.subtract(1, 2) == -1
assert m.fib(40) == 102334155

yep.stop()