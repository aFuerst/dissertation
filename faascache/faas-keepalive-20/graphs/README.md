All graph pdf files should go here 


## Litmus workloads:

### IAT

1 function whos invocations are spaced out such that each is outside the default 10 TTL window in OW

### LRU

4 functions a,b,c,d are requested round-robin. All have equal memory footprint and runtimes

### Freq

4 functions, with one being requested 5x as often

### Size

Two functions, one with twice the memory footpring of the other. With all other values being equal