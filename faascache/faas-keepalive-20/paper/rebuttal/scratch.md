## Wouldn't tail latency also be a relevant metric to consider, in addition to average latency?

Tail-latency not shown due to space reasons. Primarily dominated by cold-start overheads which we explicitly capture. The number of hot and cold starts explicitly shown in FIGURES XXX can also be used to estimate the tail latencies. 


# Smaller Issues

## The IAT is not properly defined in the paper. Probably means inter-arrival time.

We can define IAT as inter-arrival time on our first use of it.

## In the evaluation section, please provide a summary and explanation of the histogram baseline from the Microsoft paper you cite.

We can put a short summary of the Microsoft paper in section 7.1 when it is mentioned, or in 4.2 with "other caching-based policies".

## Dynamically sized cache not fully discussed until Section 5.2.

We can make this more clear in the introduction portion of the paper.

## I am surprised you bring up the interesting discrepancy in Figure 3 between caching and FaaS keep-alive but then simply say reconciling these differences is future work.

We felt that exploring the inital efficacy of applying caching ideas in FaaS systems merited its own, in-depth, examination.

## There was a lot of repetition in the text about parallels between caching and keep alive, which made me think the authors were looking to fill the 10 page limit.

We chose to emphasize the portion we thought were most important, but can reduce some of them if the committee thinks it is redundant.

## Dynamic adjustment of the cache size is a nice touch in terms of technical contributions, but I wonder how practical it is to compute reuse distances for all jobs.

Fortunately, many sampling-based online techniques can be used for reuse-distance estimation. 

We believe there is a misunderstanding on our usage of the reuse distances. We used them to inform what parameters we varied in our simulation experiments, and find the most interesting combinations. They can provide an insight into the trends of different classes of functions, and can inform expected resource allocations.


## Choosing memory as the primary resource for calculating priority

We chose to focus on memory allocation for several reasons. A single function invocation is generally short lived. Systems like OpenWhisk put a limit on how much memory a function can use, not its CPU allocation. Lastly, the dataset does not contain CPU utulization information, just execution times and memory usage statistics.

## Misc 
- Section 2.1: "and we can that the initialization overhead can as much as 80% of the total running time." broken sentence
- Section 6, typo: "caputred"
- All linecharts have too thin lines, making them difficult to read
- The acronym GDSF appears in 7.1 for the first time without being introduced
- The paper is missing a conclusion
- Paper [44] has been published in USENIX ATC, so please cite accordingly.

Thank you for enumerating the small details, we will fix these accordingly

## The authors propose also an autoscaling mechanism that tunes the memory allocated to containers. It would be great to explain in more detail better how the VM resource deflation happens in more detail.

Memory allocated to a VM can be deflated as described in more detail in [46]. Simply put, the hypervisor can transparently swap out memory or map vCPUs, or the FaaS manager software be notified of the memory change and reduce the size of its cache and reclaim resources that exceed the adjusted limit.

## The experimental methodology in Section 7.2 lacks many important details that may limit the accurate reproduction of the results, e.g., system details, software versions, function execution scenarios of the workloads. 
We can add these details to the paper, and open-source our changes to OpenWhisk if requested.

## How would FaasCache behave if operating at function level, instead of container level?
In OpenWhisk by default, containers and functions are managed together 1:1. i.e. a single function instance runs inside one container. So by managing the allocated containers, we also manage functions. [44] does not describe a similar wrapper for the function invocations, and our simulation uses the values in the dataset directly.
