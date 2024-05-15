# Various figs from OW explanation

The number at the begining of graph is the number of user threads in Locust

## 30min-compare

Traces run for 30 minutes with each load balancer.
`boundedceil` set to 1.5.

## overload-compare

The random forwarding load balancer with different `boundedceil` values set.
Having `warm` at the end means the graph only shows warm invokes, otherwise includes cold.

## 30min-bursty

2 already popular functions are given bursty periods with 4x frequency their normal

## ow-ttl

results that include running the OW Sharding LB with TTL eager eviction backend

## scaling

Users created every 10 and 20 seconds respectively (in file name).
Mark placed where last user was added.
New invoker created when function pushed across all invokers.
At least 1 minute in between each.
