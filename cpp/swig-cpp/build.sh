swig -c++ -python example.i
g++ -O2 -fPIC -c example.cxx
g++ -O2 -fPIC -c example_wrap.cxx -I/usr/include/python2.7
g++ -lpython example.o example_wrap.o -o _example.so