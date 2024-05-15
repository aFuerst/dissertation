Our sincere thanks goes to all reviewers for their genuinely insightful, helpful, and positive comments. 

# Common/Major Concerns

## Underwhelming performance 
For our workload traces, the inter-arrival-time and reuse distance is low enough that only a small fraction (30\%) of the server memory is used as a "pure cache". The rest is used for running functions. These traces thus naturally represent the worst case for caching performance: the _max_ performance penalty with no caching is also small (~2\% in Figure 5.1). With other workloads with higher reuse distances where caching/keep-alive really matters (Figs 7 and 8), FaasCache increases warm-starts by more than 2x. 

## Caching Analogy Discrepancies 
The major difference (duplicate items) doesn't make a difference as far as evictions are concerned: multiple instantiations of the same function are identical in terms of their reuse potential, so both randomly and  LRU-based eviction perform identically. The discrepancy wrt hit-ratio curves (Figure 3) does not affect FaasCache because dynamic reprovisioning is currently coarse-grained. Nevertheless it is 

## Narrow Problem 
Two recent talks at SoCC and OSDI 2020 by FaaS providers point to reducing or avoiding cold-start overheads as the key challenges in the serverless space. https://whova.com/embedded/session/sccs_202010/1270305/?view=#  https://www.amazon.science/conferences-and-events/osdi-2020

## Sensitivity analysis
Sensitivity analysis is a major part of our future work. However, doing so in a way faithful to workload characteristics is challenging, because mixing of different function types (aka traffic classes) is a relatively recent development even in object caching (Footprint Descriptors, CONEXT 2018). 

## Main insight ("keep-alive==object caching") not surprising. Applies existing caching techniques directly. 
Much to our surprise, this obvious insight is not found anywhere, and we want to make this observation public. Showing the effectiveness of standard caching techniques is one of our major contributions: it shows that developing yet another class of specialized solutions for FaaS is not necessary. 

## Impact of increasing FaaS system memory on other services 
Allocating more resources to FaaS systems could possibly impact other services, and is a good topic for future research. The cache provisioning techniques we describe can be used for systematically examining the memory vs. latency tradeoffs and allow cloud providers to "right size" their function caches. 

## Stateless FaaS Invocations / Function Reusability 
OpenWhisk, Azure [44], AWS Lambda/firecracker [51], all keep functions warm for improving latency and utilization. 

## Dynamic Provisioning
Granularity [B]: The *entire* function cache size is adjusted based on reuse-distances of all functions: this is not done at a per-function level. 

Feasibility [D]: The Azure paper [44] shows that workload prediction can/is used for functions, in the same way as temporal locality is the backbone of data caching systems.  


# Review B

## Additional load instead of size reduction
We presented evaluation of the "inverse" problem only because it is easier to run the same exact workload, whereas scaling workloads up requires some more assumptions (such as whether all function invocations increase proportionally, etc.).

# Reviewer C 

## Section 7.1 is done with simulation while 7.2 and 7.3 are OpenWhisk
Yes 

## Why is explicit initalization (line 2--6 in Fig 2) not common ?
We are confused too: perhaps users/developers can't be bothered with making simple changes for the sake of performance? Also, explicit initalization is not uniformly supported across FaaS platforms. 

# Review D 

## Termination policy puts container eviction on the critical path. 
A similar design tradeoff is found in in caching systems such as the page cache. Containers are reclaimed by a separate thread, and enough free resources are kept to avoid critical-path reclamation. 

## OpenWhisk TTL under high utilization
LRU is used

## Clarify whether cold-start refers to initializing or launching a container (or both)? 
Cold-start refers to both container start and application initialization. Enhancing the keep-alive targets avoiding both steps.

## Use for computing reuse distances? Trace as useful representation of the future?
The Microsoft trace shows that workload prediciton can indeed be used for functions (please see Figures 4 and 6 in [44]), in the same way as temporal locality is the backbone of data caching systems. 

## Tail Latency 
We can provide data for the tail latency for all the OpenWhisk experiments. For trace-driven results, the latency increase due to cold-starts is deterministic and can also be shown 

# Review G

## How would OpenWhisk without TTL perform? 
We compare against such resource-conserving policies by using LRU and other algorithms. 

##  Function level instead of container level
Since eviction priorities are per-function, FaasCache already has a function-level approach. 

# Figures 5 do not match perfectly with those in Figure 6
Hit-ratios (Fig 6) are deceptive because they don't take into account size and frequency differences. 

# System overhead
The extra overhead was negligible (~0.1\%): we will include the results in Appendix. 

## Section 7.2 lacks many important details
We will be sure to include more system and experimental details in the Appendix. 


## The motivation would strengthen if the authors included more details regarding support for explicit initialization found in [36] and other repos, and provide quantitative results regarding the workload diversity and dynamism.
This is a great idea, but as [44] gets into lightly, functions vary significantly on multiple attributes, including size, IAT, execution time, etc. We did some cursory analysis of the trace and found most functions have a noticable difference between their average and maximum execution times, suggesting app initialization time exists. A thorough sensitivity analysis of the dataset to examine workload diversity would be its own effort and we chose to start with this paper instead.
