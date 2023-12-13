# Recources
- [tensorflow/tpu Repository](https://github.com/tensorflow/tpu)
- [tensorflow/tpu Fashionpedia Model](https://github.com/tensorflow/tpu/tree/master/models/official/detection/projects/fashionpedia)
- [Issue: How to run the Fashionpedia inference code? ](https://github.com/tensorflow/tpu/issues/883)

# Error during install pycocotools

sdfa
```
Building wheels for collected packages: pycocotools
  Building wheel for pycocotools (pyproject.toml) ... error
  ERROR: Command errored out with exit status 1:
   command: /usr/bin/python3 /usr/local/lib/python3.6/dist-packages/pip/_vendor/pep517/in_process/_in_process.py build_wheel /tmp/tmpd77k0w6v
       cwd: /tmp/pip-install-gbjsvr9c/pycocotools_6015bbcc1ed54f028a8c86d50970ed47
  Complete output (69 lines):
  running bdist_wheel
  running build
  running build_py
  creating build
  creating build/lib.linux-x86_64-3.6
  creating build/lib.linux-x86_64-3.6/pycocotools
  copying pycocotools/__init__.py -> build/lib.linux-x86_64-3.6/pycocotools
  copying pycocotools/coco.py -> build/lib.linux-x86_64-3.6/pycocotools
  copying pycocotools/mask.py -> build/lib.linux-x86_64-3.6/pycocotools
  copying pycocotools/cocoeval.py -> build/lib.linux-x86_64-3.6/pycocotools
  running build_ext
  skipping 'pycocotools/_mask.c' Cython extension (up-to-date)
  building 'pycocotools._mask' extension
  creating build/temp.linux-x86_64-3.6
  creating build/temp.linux-x86_64-3.6/common
  creating build/temp.linux-x86_64-3.6/pycocotools
  x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -I/usr/include/python3.8/Python.h -fPIC -I/usr/local/lib/python3.6/dist-packages/numpy/core/include -I./common -I/usr/include/python3.6m -c ./common/maskApi.c -o build/temp.linux-x86_64-3.6/./common/maskApi.o -Wno-cpp -Wno-unused-function -std=c99
  cc1: warning: /usr/include/python3.8/Python.h: not a directory
  ./common/maskApi.c: In function 'rleDecode':
  ./common/maskApi.c:46:7: warning: this 'for' clause does not guard... [-Wmisleading-indentation]
         for( k=0; k<R[i].cnts[j]; k++ ) *(M++)=v; v=!v; }}
         ^~~
  ./common/maskApi.c:46:49: note: ...this statement, but the latter is misleadingly indented as if it were guarded by the 'for'
         for( k=0; k<R[i].cnts[j]; k++ ) *(M++)=v; v=!v; }}
                                                   ^
  ./common/maskApi.c: In function 'rleToBbox':
  ./common/maskApi.c:135:32: warning: unused variable 'xp' [-Wunused-variable]
       uint h, w, xs, ys, xe, ye, xp, cc; siz j, m;
                                  ^~
  ./common/maskApi.c: In function 'rleFrPoly':
  ./common/maskApi.c:181:3: warning: this 'for' clause does not guard... [-Wmisleading-indentation]
     for(j=0; j<k; j++) x[j]=(int)(scale*xy[j*2+0]+.5); x[k]=x[0];
     ^~~
  ./common/maskApi.c:181:54: note: ...this statement, but the latter is misleadingly indented as if it were guarded by the 'for'
     for(j=0; j<k; j++) x[j]=(int)(scale*xy[j*2+0]+.5); x[k]=x[0];
                                                        ^
  ./common/maskApi.c:182:3: warning: this 'for' clause does not guard... [-Wmisleading-indentation]
     for(j=0; j<k; j++) y[j]=(int)(scale*xy[j*2+1]+.5); y[k]=y[0];
     ^~~
  ./common/maskApi.c:182:54: note: ...this statement, but the latter is misleadingly indented as if it were guarded by the 'for'
     for(j=0; j<k; j++) y[j]=(int)(scale*xy[j*2+1]+.5); y[k]=y[0];
                                                        ^
  ./common/maskApi.c: In function 'rleToString':
  ./common/maskApi.c:227:7: warning: this 'if' clause does not guard... [-Wmisleading-indentation]
         if(more) c |= 0x20; c+=48; s[p++]=c;
         ^~
  ./common/maskApi.c:227:27: note: ...this statement, but the latter is misleadingly indented as if it were guarded by the 'if'
         if(more) c |= 0x20; c+=48; s[p++]=c;
                             ^
  ./common/maskApi.c: In function 'rleFrString':
  ./common/maskApi.c:235:3: warning: this 'while' clause does not guard... [-Wmisleading-indentation]
     while( s[m] ) m++; cnts=malloc(sizeof(uint)*m); m=0;
     ^~~~~
  ./common/maskApi.c:235:22: note: ...this statement, but the latter is misleadingly indented as if it were guarded by the 'while'
     while( s[m] ) m++; cnts=malloc(sizeof(uint)*m); m=0;
                        ^~~~
  ./common/maskApi.c:243:5: warning: this 'if' clause does not guard... [-Wmisleading-indentation]
       if(m>2) x+=(long) cnts[m-2]; cnts[m++]=(uint) x;
       ^~
  ./common/maskApi.c:243:34: note: ...this statement, but the latter is misleadingly indented as if it were guarded by the 'if'
       if(m>2) x+=(long) cnts[m-2]; cnts[m++]=(uint) x;
                                    ^~~~
  x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -I/usr/include/python3.8/Python.h -fPIC -I/usr/local/lib/python3.6/dist-packages/numpy/core/include -I./common -I/usr/include/python3.6m -c pycocotools/_mask.c -o build/temp.linux-x86_64-3.6/pycocotools/_mask.o -Wno-cpp -Wno-unused-function -std=c99
  cc1: warning: /usr/include/python3.8/Python.h: not a directory
  pycocotools/_mask.c:4:10: fatal error: Python.h: No such file or directory
   #include "Python.h"
            ^~~~~~~~~~
  compilation terminated.
  error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
  ----------------------------------------
  ERROR: Failed building wheel for pycocotools
Failed to build pycocotools
ERROR: Could not build wheels for pycocotools, which is required to install pyproject.toml-based projects
```

### Solution
- `sudo find / -iname 'Python.h'` to find python header. 
- `export CPPFLAGS=-I/usr/include/python3.8/` set compilerflag to point to directory with python.h
- thx to [Stackoverflow Answer](https://stackoverflow.com/a/67000027)
