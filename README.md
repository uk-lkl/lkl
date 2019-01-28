# lkl for Unikraft

This is Unikraft Linux Kernel Library port.

## Update 

```
$ cd linux
$ make -C tools/lkl
$ nm -D tools/lkl/lib/liblkl.so \
  | python ../genexportsyms.py \
  > ../exportsyms.uk
$ echo "lkl_thread_init" >> ../exportsyms.uk
$ git apply ../patches/0001-uk-Avoid-missing-file-include.patch
```
