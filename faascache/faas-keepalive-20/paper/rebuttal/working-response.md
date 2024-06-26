ASPLOS 2021 Paper #1225 Reviews and Comments
===========================================================================
Paper #1225 FaasCache: Keeping Serverless Computing Alive With Greedy-Dual
Caching
 
 
> Review #1225A
> ===========================================================================
> 
> Is this paper thought provoking?
> --------------------------------
> 3. Strong but narrow appeal. Thought provoking only for people already
>    working in this particular topic.

_FaaS is a growing share of the cloud workload market, and has applicability in many areas of research. Including virtualization, resource manangement, scheduling, and systems design._

> Is this paper convincing?
> -------------------------
> 2. Good. The evidence is not bullet-proof but is acceptable for papers in
>    the area.
> 
> Paper Summary
> -------------
> Current Functions as a Service solutions do not offer low-latency processing because they require the initialization of code and data dependencies before they can start executing. This paper's insight is that these FaaS cold-start issues is equivalent to object caching (i.e., a warm function is equivalent to a cache hit, and the termination of a function is equivalent to evicting an object from a cache).
> 
> As a result of this insight, the paper studies the different existing caching algorithms in the context of FaaS platforms. Moreover, the paper builds on the Greedy-Dual approach to implement a keep-alive policy that is aware of the frequency and recency of invocations of different functions, and their initialization overheads.

_This is an accurate summary of the paper snd it's results. It misses the minor detail that current FAAS offerings have a short fixed-time window that code is kept warm for._

> Comments for Authors
> --------------------
> Thank you for your submission to ASPLOS. I've enjoyed reading your extended abstract, which is tackling an interesting problem.

_We are glad you enjoyed it!_

> I've found your key insight (i.e., addressing FaaS cold-starts as object caching) interesting, but I do think it would be good to also discuss several key differences between the two problem domains:
> 1.Traditional FaaS are stateless, and thus can be utilized by cloud computing providers to fill up available resources by co-locating functions next to long-running high-priority service tasks. FaasCache departs from this approach, and transforms functions into sort of stateful units of computations that maintain code and data across invocations. This might cause significant cluster scheduling challenges for cloud provides because high-priority service jobs might not have resources available to be scaled-up, and the scheduler would have to collaborate with FaaSCache to evict functions.

_Current FAAS offerings keep functions warm for a short period an they can serve multiple invocations. It is an assumption on the customer that their code can operate in a stateless manner. The cluster or FAAS manager still reserves the right to collect function memory if pressure increases, and can still maintain a high cache-hit ratio under pressure._

> 2. It is great that the extended abstract discusses the performance vs. resource allocation trade-off, but in my opinion this is a 3-way trade-off: performance of FaaS vs. resource efficiency vs. performance of other types of tasks. This work could be much stronger if it were to build on the cache analogy to study how these caching algorithm affect the overall resource utilization, and response time in clusters in which FaaS are co-located with service and batch jobs.

_We agree with this insight that allocating more resources to FAAS systems could possibly impact other services, and is a good topic for future research._

> 3. In my opinion, the extended abstract would be stronger if it were to also briefly discuss the subtle properties of the problem space that make regular caching algorithms unsuitable.

_We believe this is addressed in the abstract in section 5.5, as we comment that LRU and LFU do not take into consideration function memory size and startup cost._

> Review #1225F
> ===========================================================================
> 
> Is this paper thought provoking?
> --------------------------------
> 2. Moderately thought-provoking to a wide audience. Many conference
>    attendees will be glad that they saw this paper.
> 
> Is this paper convincing?
> -------------------------
> 2. Good. The evidence is not bullet-proof but is acceptable for papers in
>    the area.
> 
> Paper Summary
> -------------
> * This paper targets keeping the functions alive and warm after they have finished execution, which can alleviate the cold-start overhead. 
> * The primary insight is that the resource management of functions is equivalent to object caching. 
> * The proposed keep-alive policy is based on Greedy-Dual-Size Frequency object caching.
> * This work implements the proposed caching-based techniques in a popular FaaS platform, OpenWhisk.
> * Experimental results show that the proposed techniques can reduce the average server size by more than 30% while reducing cold-start overheads by 3×, improving application-latency by 6×, and reducing system load to run 2× more.

_A thorough and accurate summary._

> Comments for Authors
> --------------------
> I like the caching analogy that makes this work easy to understand. In general, the idea of this paper is simple and easy to implement. However, experimental results show that the proposed techniques indeed works. I'd like to know more details.

_More detail on the impact of the implemented techniques? Experiemnts with different workloads or FAAS system setups?_
TODO: this

> Review #1225E
> ===========================================================================
> 
> R2 Overall Merit
> ----------------
> B. OK paper, but I will not champion it
> 
> Is this paper thought provoking?
> --------------------------------
> 3. Strong but narrow appeal. Thought provoking only for people already
>    working in this particular topic.
> 
> Is this paper convincing?
> -------------------------
> 2. Good. The evidence is not bullet-proof but is acceptable for papers in
>    the area.
> 
> Paper Summary
> -------------
> Paper tackles the problem of keeping serverless/FaaS (function as a service) containers alive in order to reduce latency by applying caching techniques.  They use hit-ratio curves to determine the ideal size of servers required for handling FaaS workloads, and develop a new vertical autoscaling approach that dynamically adapts server size based on the workload characteristics.
> Key insight:  FaaS keep-alive is an object caching problem.  
> Shortcomings:  Resource provisioning portion of the paper does not take into account the scheduling interactions in a cluster of machines.

_We acknowledge that the paper does not consider the impact on larger cluster scheduling, but see it as a good area for future research._

> Comments for Authors
> --------------------
> Using a cache to keep containers around for FaaS execution is indeed a good insight, though not terribly surprising.  Nonetheless I appreciated the nice background on object caching and how his is applied to FaaS.

_We are glad you enjoyed the background and application sections._

> The priority calculation is intuitively simple and captures container initialization cost, last use, use frequency, and a scalar size dimension.  Since size is scalar (and you discuss how to normalize a multidimensional vector to a scalar), I do wonder if you are potentially stranding resources.  For instance, your algorithm may choose to evict memory-hungry containers in favor of containers that are very CPU hungry (thus stranding resources to containers that could be cached that are the inverse--  memory hungry but use little CPU).

_We chose to focus on memory allocation for several reasons. A single function invocation is generally short lived. Systems like OpenWhisk put a limit on how much memory a function can use, not its CPU allocation. Lastly, the dataset does not contain CPU utulization information, just execution times and memory usage statistics._ 

> The dynamic resource provisioning portion of the paper doesn't discuss or take into account cluster-level scheduling, and I found this to be a shortcoming.  The containers that schedule on a machine are vast and I'm not sure how you can pick the subset used to provision a server?  I suppose a sample could be used to determine the provisioning of all servers in a cluster.

_We agree that changing the memory model for FAAS systems will impact the larger cluster resource scheduling and worth future research. The Azure dataset would provide a good palce to start to understand resource requirements for managing large numbers of FaaS functions and executions over time._

> Please run a spellcheck on the paper.  Numerous misspellings.

_Understood, will do. Our apologies._

> Review #1225C
> ===========================================================================
> 
> R2 Overall Merit
> ----------------
> B. OK paper, but I will not champion it
> 
> Is this paper thought provoking?
> --------------------------------
> 4. Weak. May provoke some new thoughts, but not many (even for people
>    already working in this topic).

_We are proposing treating the allocation and de-allocation of FAAS executions as a cache problem. Using this insight future research can tailor existing cache ideas to the FAAS domain to improve resource efficiency._

> Is this paper convincing?
> -------------------------
> 2. Good. The evidence is not bullet-proof but is acceptable for papers in
>    the area.
> 
> Paper Summary
> -------------
> This paper proposes a caching approach to improve startup latency for serverless functions by identifying the most beneficial functions to keep warm, taking into account function attributes like the frequency of invocation and the function resource footprint. The key contribution is the FaasCache system, which implements a Greedy-Dual keep-alive policy, statically provisions VM resources for serverless functions based on hit-ratio curves derived from re-use distances, and also uses this information to dynamically scale VM resources.
> 
> Comments for Authors
> --------------------
> Strengths: 
> - Important problem of keeping the right serverless function containers alive to reduce startup times.
> - Evaluation compares to recently published state of the art policy and achieves higher performance.

> Weaknesses:
> - The main insight of the paper ("treat function keep-alive as an object caching problem") is not particularly surprising. This paper is mostly about applying existing techniques developed for caching directly to the challenge of selecting which functions to keep alive. While this is an important problem and the authors propose a good approach, I wish there was more technical depth to the paper that goes beyond applying existing techniques.
> There was a lot of repetition in the text about parallels between caching and keep alive, which made me think the authors were looking to fill the 10 page limit.

_We chose to emphasize the portion we thought were most important, but can reduce some of them if the committee thinks it is redundant._

> Dynamic adjustment of the cache size is a nice touch in terms of technical contributions, but I wonder how practical it is to compute reuse distances for all jobs.

_We believe there is a misunderstanding on our usage of the reuse distances. We used them to inform what parameters we varied in our simulation experiments, and find the most interesting combinations. They can provide an insight into the trends of different classes of functions, and can inform expected resource allocations._ 

> The paper would also benefit from some sensitivity analysis, e.g. as we sweep the cold and warm startup time and the ratio between them, how does this affect the impact that the keep alive policy has on end-to-end application performance? 

TODO:

> Comments/questions:
> - I am surprised you bring up the interesting discrepancy in Figure 3 between caching and FaaS keep-alive but then simply say reconciling these differences is future work.

_We felt that exploring the inital efficacy of applying caching ideas in FaaS systems merited its own, in-depth, examination._

> - I like that you support a dynamically sized cache. I didn't realize this until Section 5.2 though.  I went back to the introduction and saw you had briefly mentioned "dynamic server sizing"  but it was not clear to me what "server" sizing you were referring to, as this could refer to sizing the server running the serverless function itself. I would find it more clear if you said the FaaScache size.

_We can make this more clear in the introduction portion of the paper._

> - In the evaluation section, please provide a summary and explanation of the histogram baseline from the Microsoft paper you cite.

_We can put a short summary of the Microsoft paper in section 7.1 when it is mentioned, or in 4.2 with "other caching-based policies"._

> Questions for Authors
> ---------------------
> - If I understood correctly, "explicit intialization" is code such as lines 2-6 in Figure 2, which deals with importing packages and such. Why is this not common in general? I'm confused.

_While importing packages in Python usually happens on initialization, it is not guaranteed. Also expensive setup, such as an S3 connection, downloading model weights, or more are often done after user code is started. This happens in many of the examples in FunctionBench._

_The significant difference between average and maximum runtime from the Azure trace supports this pattern also exists in production systems._ -> (but not in paper)

> - Can you state more explicitly which part of the evaluation are done in a real system vs. simulation? I assume Section 7.1 is done with simulation while 7.2 and 7.3 are experiments in the real system -- can you confirm? 

_Section 7.2 was with a real OpenWhisk system, the other two were in-solico._

> - Do you consider how the impact of your caching policy may change by considering different cold vs. warm start startup times? A sensitivity study would be insightful here.

_We did consider this. If the cold vs warm times were essentially the same, then the system would lose some effectiveness. We did some analysis on the Azure trace looking for warm vs cold disparities, but did not include this in the final paper._

> Review #1225D
> ===========================================================================
> 
> R2 Overall Merit
> ----------------
> B. OK paper, but I will not champion it
> 
> Is this paper thought provoking?
> --------------------------------
> 3. Strong but narrow appeal. Thought provoking only for people already
>    working in this particular topic.
> 
> Is this paper convincing?
> -------------------------
> 2. Good. The evidence is not bullet-proof but is acceptable for papers in
>    the area.
> 
> Paper Summary
> -------------
> Problem:
> - The cold start effect of containers in FaaS can account up to 80% of their total runtime.
> - Existing approaches to reduce frequent cold starts are very basic, relying on static keep-alive timeouts.
> 
> Insights:
> - Simple, obvious, effective: deciding which containers to keep alive is like a cache replacement problem. So let's apply effective cache replacement techniques.
> - Classical caching policies such as LRU are not a great fit because they do not consider object sizes (in this case, container resource requirements and different startup cost) and thus are not a great fit. Greedy-Dual-Size-Frequency caching, though, takes different "sizes" into account, hence is a good option.
> 
> Contributions:
> - Making the key observation of parallel between well-studied caching techniques and decision on when to freeze ("evict") containers 
> - Development of a caching-based technique to decide on when a container is paused, demonstrating the effectiveness of the idea
> 
> Shortcomings:
> - Parts of the evaluation are confusing and not sufficiently explanatory.
> 
> Comments for Authors
> --------------------
> I like the paper's idea, which is simple and very intuitive, and hence convincing. The paper formulates the problem well, and draws an effective analogy of keep-alive policies to cache eviction and cache provisioning policies.
> 
> Although generally well-written, there is a terminology confusion in section 2 between the terms "initialization time", "launching" a container, and "cold-start". In most places, initialization and cold-start are referred to as different time components, but at places in the prose the two are conflated (e.g., "initializing the function by importing libraries and other data dependencies, function execution thus incurs a significant “cold-start” penalty"). In most places it seems that cold-start refers just to launching a container. However, the presence of table 1 as well as the fact that initialization is an order of magnitude costlier than launching (~100ms) makes me think you are probably referring to both by cold-start. In general, that was a significant source of confusion for me.

_We can improve the verbiage of the paper to remove the confusion. In general "cold-start" refers to needing to create a new container and run user init code. Both can cause variations depending on the chosen runtime and needed libraries and dependencies._

> Design:
> - Faascache's container termination policy puts container eviction on the critical path ("Containers are terminated only if there are insufficient resources to launch a new container and if existing warm containers cannot be used."). I was wondering whether a slightly more proactive approach could further improve performance?

_The deactivation of terminated containers happens on a differnt thread than the critical path in OpenWhisk. But there is still overhead from sorting the items in the cache and sending shutdown signals. This insight is worth more investigation._

> - In the case of static server provisioning (S5.1), I could not understand the practical use of computing reuse distances of a trace. Is it reasonable to expect that a given trace of function invocations on a server is representative of the future? I would expect invocations to wildly change over time, especially given that a given server in a datacenter is in the general case hosting functions of different, completely independent services with independent temporal activity patterns.

_The number of executions over time, as taken from the Azure trace is rather cyclic and can be predicted on a coarse-grained level. The reuse distance helps demonstrate how FaaS doesn't align exactly with traditional caching, rather than a consistent baseline for predicting all future resource needs._

PRATEEK: Say that azure paper ALSO makes use of this and is true based on some FIGURE In their own paper. Other papers also do this etc. See my comments. 

> Evaluation:
> - I quite enjoyed reading this paper, until I reached the evaluation. Section 7.1 seems to show that the absolute impact on performance is really in the 1-2% ballpark.
> After a very nicely structured paper and an abstract and intro preparing the reader to see how 2-3x improvements are achieved, the reader reaches the first result in the evaluation and realizes these numbers refer to optimizing a 1-2% of the total runtime, which is quite disappointing. However, the following section (7.2) presents additional, more promising results which the authors claim result "in a 6× reduction in the application latency". Which presented results show this 6x reduction? How is this huge discrepancy in performance improvement between 7.1 and 7.2 explained? I am not sure if this is an evaluation issue or explanation/structure issue, but in any case it indicates something that needs to be improved in the paper.

TODO: SPEND GOOD TIME ON THIS!!!!!!!!!!

> - Wouldn't tail latency also be a relevant metric to consider, in addition to average latency?

_Tail latency would likely follow the cold-start ratio, but would be an interesting metric for confirmation._

PRATEEK: Tail-latency not shown due to space reasons. Primarily dominated by cold-start overheads which we explicitly capture. The number of hot and cold starts explicitly shown in FIGURES XXX can also be used to estimate the tail latencies. 

> - Under high utilization, where termination of a container before the 10min TTL is over, what does OpenWhisk do in terms of victim container selection to free resources? Is it LRU? Or does OpenWhisk just drop a request that can't be buffered long enough until a 10min TTL of a previously invoked function expires?

_OpenWhisk reverts to LRU under resource constraints_

> Misc: 
> - Section 2.1: "and we can that the initialization overhead can as much as 80% of the total running time." broken sentence
> - Section 6, typo: "caputred"
> - All linecharts have too thin lines, making them difficult to read
> - The acronym GDSF appears in 7.1 for the first time without being introduced
> - The paper is missing a conclusion
> - Paper [44] has been published in USENIX ATC, so please cite accordingly.

_Thank you for enumerating the small details, we will fix these accordingly_

> Questions for Authors
> ---------------------
> - Can you please clarify whether cold-start refers to initializing or launching a container (or both)? Do keep-alive approaches target initialization, launching, or both latencies?

_Cold-start refers to both container start and application initialization._

> - Please address the questions under "Design" and "Evaluation" above.

TODO: evaluation

> Review #1225B
> ===========================================================================
> 
> R2 Overall Merit
> ----------------
> B. OK paper, but I will not champion it
> 
> Is this paper thought provoking?
> --------------------------------
> 3. Strong but narrow appeal. Thought provoking only for people already
>    working in this particular topic.
> 
> Is this paper convincing?
> -------------------------
> 2. Good. The evidence is not bullet-proof but is acceptable for papers in
>    the area.
> 
> Paper Summary
> -------------
> The paper tackles the cold start problem in FaaS cloud environments. The authors correctly point out that cold start, i.e., the time to instantiate a new container for a function can account for a significant fraction of the task's overall execution time, and hence it makes sense to try to reduce it. They make an analogy between cold start and cache misses, and present a set of caching and resource provisioning techniques to determine whether to keep a container alive or not, and how many resources to allocate to it.

_This is an accurate summary except for one minor detail. We are not reducing the cold start time, only trying to avoid cold starts in general._

PRATEEK: Not sure this is worth rebuting, ignore. 

> Comments for Authors
> --------------------
> This is an interesting problem, and I enjoyed the analogy between FaaS cold starts and cache misses. The authors did a good job motivating the problem, and the caching policy they have used makes sense. It is also good that they have considered the resource provisioning implications of serverless, and have designed a couple simple policies to address static and dynamic demands. 

> I'm also glad to see a real system implementation using a representative serverless framework like OpenWhisk. 

_We are glad you enjoyed the paper and implementation detail._

PRATEEK: No need to respond to compliments. 

> That being said the actual observation that cold starts are similar to cache misses is not fundamentally new. Papers like Catalyzer [ASPLOS'20], Lin et al. "Mitigating Cold Starts in Serverless Platforms: A Pool-Based Approach", 2020, and several others have made similar observations. Even though they may not use the same caching policies used here, the benefits are similar. 

_We are not the first to attempt to reduce the number of cold starts, but are the first to apply strictly caching ideas as a way to reduce cold starts. The Azure paper [44] attempts to reduce cold starts by predict incoming requests for rare functions. In comparison, our system works on both rare and frequent functions._

> Also, with respect to the resource provisioning policies, it would be great if the paper clarified what the system assumes about a given application; i.e., has it seen the application before in order to determine its allocation, or is that done online? For the dynamic resource provisioning, given how short lived FaaS functions are, does it make sense to adjust their resources at runtime, or should you just use what you learned from one function invocation to better manage future invocations of similar/same functions? Some more insights on these decisions would add to the paper's contributions. 

_In the simulations we use the memory usage recorded in the Azure trace, and for OpenWhisk we determine the optimal runtimes for the various functions across a series of memory sizes._
_In OW the memory allocation of a function is known ahead of time, but in Azure it is not._
_Adjusting the allocated physical memory to a function would be an interesting topic, as it would impact code runtime._
TODO: more?

> It's good that you can reduce the used server size with your provisioning techniques, but it would be more useful to show these benefits as added load the same server can support (this should account for any contention between concurrently-invoked functions).

_We can bring this up more in the paper. This can be shown in Figure 8, where FaasCache is able to server more requests than unmodified OpenWhisk._

> Questions for Authors
> ---------------------
> Instead of reduction in server size, can you frame your provisioning benefits as additional accommodated load? I find that a much more useful metric.

_We can bring this up more in the paper. This can be shown in Figure 8, where FaasCache is able to server more requests than unmodified OpenWhisk._

PRATEEK: Please merge mine. 

> Review #1225G
> ===========================================================================
> 
> R2 Overall Merit
> ----------------
> C. Weak paper: some flaws, but I will not fight strongly against it

_:(_

> Is this paper thought provoking?
> --------------------------------
> 3. Strong but narrow appeal. Thought provoking only for people already
>    working in this particular topic.
> 
> Is this paper convincing?
> -------------------------
> 3. Marginal. The paper presents weak evidence to demonstrate its main
>    claims.
> 
> Paper Summary
> -------------
> Problem
> - This paper targets the problem of the cold-start overhead (due to initializing code and fetching data dependencies) in serverless computing.
> - The paper addresses the cold-start overhead by keeping functions alive (or cached/warm, after their execution has finished)
> 
> Key insights
> - The key insight of the paper is that the resource management of functions (keep-alive) is analogous to caching. Hence, the paper proposes to leverage the principles and techniques of caching and apply them to serverless computing.
> 
> Key scientific and technical contributions
> - The paper proposes FaasCache that computes a priority for each container based on the cold-start overhead and resource footprint, and terminates, i.e., it evicts from the "cache", the container with the lowest priority.

> - The paper explores keep-alive policies at server level, based on well-known caching policies. It also leverages concepts such as reuse distances and miss-ratio curves to determine the ideal size of servers required for handling FaaS workloads, and develops a vertical autoscaling approach that dynamically adapts server size based on the workload characteristics.

> - The keep-alive caching policies take into consideration: resource footprint, access frequency, initialization cost, and execution latency of functions. 

> - The proposed FaaSCache system is evaluated with a simulator and is implemented in OpenWhisk.


> Shortcomings
> - The novelty of the paper is limited as it simply applies caching policies to address the cold-start overheads.

PRATEEK: Maybe mention the recent SoCC keynote by ricardo bianchini and the OSDI amazon talk, both which say that reducing the cold-start overheads is one of the KEY PRACTICAL challenges in FaaS, as seen in the largest cloud providers in the real world. 

> - The paper's approach is based on the assumption that containers that have finished their execution will still occupy system resources. This is in contrast to [44] that states that FaaS frameworks are often implemented on top of services that charge by the time resources are allocated.

_Both our system and [44] accept the trade-off of using more memory to keep functions alive longer. [44] uses a preictive method and eagerly revokes memory. We differ from them in that our approach is effective for all frequencies of functions, not just the rarest 25%. We are able to achieve equal or better cold-start %s that [44] with the same amount of allocated memory. As shown in figures 5-6_

> - The evaluation lacks information for experimental reproducibility and is primarily based on trace-driven simulations. The real system evaluation lacks important results such as the overhead of the proposed caching policies, and comparison with state-of-the-art approaches.

_We do not analyze the overhead cost of maintaining and sorting metadata, but could add it to the paper._

> Comments for Authors
> --------------------
> This paper targets the very important problem of cold start overheads in the context of FaaS/serverless computing which has gained a lot of traction recently. Many recent works try to mitigate the cold-start overheads from various angles, from low-level OS mechanisms up to resource managers. This paper makes a very interesting case for reducing cold-start overheads by applying caching. The paper is well-written, easy to follow, and interesting to read. In addition, the advantages and the limitations of the proposed techniques are discussed as well. 

_Thank you for the positive comments_

> However, the main reason that prevents me from giving a higher score is the lack of novelty. The key insight is by itself important, but the employed techniques are all well-known and have been extensively discussed in the literature (caching policies, reuse distances, hit/miss ratio curves, memory hot-unplug). The calculation of priorities for containers seems to be the only novel part here.

TODO: not sure how to respond

> Another important issue that arises is related to the basic assumption of the paper that states that containers that have finished their execution will still occupy system resources, so applying caching mechanisms should make sense. However, this is in contrast to a state-of-the-art publication [44] that states that FaaS frameworks are often implemented on top of services that charge by the time resources are allocated, and this is why FaaS frameworks typically free resources after a fixed period of inactivity. In addition, by freeing proactively resources, FaaS frameworks create an opportunity for running best-effort jobs on the spare resources, increasing the utilization of the servers (a common approach for cloud providers that has been extensively studied and applied). It would be great if the authors discussed in the paper whether the FaasCache assumption is relevant in FaaS installations and what are the implications/limitations of their approach. Perhaps an approach that combines a small cache with prefetching would be more practical.

TODO

> Section 3 provided motivation results from FaaS benchmarks. The motivation would strengthen if the authors included more details regarding support for explicit initialization found in [36] and other repos, and provide quantitative results regarding the workload diversity and dynamism.

_We can add analysis of the [44] dataset showing the significant difference between average and maximum function executions. Giving credence to the notion of explicit initialization being on the critical path._

> FaasCache operates at container level. However, the number of alive containers in the system can be extremely high. It would be great to discuss the implications and tradeoffs of tracking priorities only at function level.

_In OpenWhisk by default, containers and functions are managed together 1:1. I.e. a single functions runs inside one container. So by managing the allocated containers, we also manage functions. [44] does not describe a similar wrapper for the function invocations, and our simulation uses the values in the dataset directly._

> The authors propose also an autoscaling mechanism that tunes the memory allocated to containers. It would be great to explain in more detail better how the VM resource deflation happens in more detail.

_Memory allocated to a VM can be deflated as described in more detail in [46]. Simply put, the hypervisor can transparently swap out memory or map vCPUs, or the FaaS manager software be notified of the memory change and reduce the size of its cache and reclaim resources that exceed the adjusted limit._

> The experimental methodology in Section 7.2 lacks many important details that may limit the accurate reproduction of the results, e.g., system details, software versions, function execution scenarios of the workloads. 

_We can add these details to the paper, and open-source our changes to OpenWhisk if requested._

> The evaluation section should clearly distinguish those results that are based on simulator and those that are based on the real system.

_We can clarify that section 7.2 is a real system and 7.1 and 7.3 are simulation-based._

> The real system experiments only compare FaasCache with vanilla OpenWhisk. It would be great if the authors in the real system experiments compared FaasCache at least with LRU (to actually show what is the benefit of removing the TTL restriction of conservative policies that destroy containers after a fixed time period of inactivity) and [44]. In addition, the real system evaluation lacks results on the overhead (performance and memory due to metadata) of the proposed caching policies.

_OpenWhisk uses LRU as a fallback during resource-constrained times. The experiments in section 7.2 cause one such scenario, thus the large numer of dropped requests by OW._
_We can analyze the overhead of the metadata management and add the details to the paper._

> The results in Figure 5 show the percentage increase due to cold-starts with respect to total execution time. The results show that beyond 40 GBs of cache (or server memory when no cache is used) the difference in overheads is very small. It would be great to discuss what is the typical value assumed for caches and for server memory when running such workloads. 

TODO: do we even have this kind information? It wasn't in the azure paper.

PRATEEK: This is extremely interesting. WHAT DOES THE MS AZURE PAPER say that the "keep-alive" size is? Because FaaS workloads have different memory and computing overheads because of initialization and very different application architectures, this comparison is non-trivial and should make for a great separate paper. 

> The results of TTL in Figures 5 do not match perfectly with those in Figure 6. In Figure 6, TTL performs similarly to the caching techniques. However, this behavior is not depicted in Figure 5 that shows the percentage increase of execution time due to cold starts. While the authors acknowledge the existence of such discrepancies, it would be great to discuss in more detail the reasons.

_Figures 5a-5c factor in function cold and warm execution time. While TTL may result in a similar number of cold starts, FaaSCache also optimizes for few cold hits on expensive startup code. So it does better on improving execution time. We can discuss this more substantially in the paper._

> The IAT is not properly defined in the paper. Probably means inter-arrival time.

_We can define IAT as inter-arrival time on our first use of it._

> Questions for Authors
> ---------------------
> Please explain whether the FaasCache assumption (i.e., containers that have finished their execution can still occupy physical resources) is valid for public/private FaaS installations and what are the implications/limitations in resource management from the FaaS provider point of view that seeks to increase the system utilization with other/best-effort jobs.

_Functions are kept warm for several minutes for possible reuse in both public and private FaaS, so we see no reason why keeping their resources loaded for longer changes this scenario_
_We could do some analysis on optimal scenarios, but the FaaS provider can choose what cold-start ratio they are willing to accept (dynamic memory) and/or if they just want a fixed allocation_
TODO: Am I understanding this correctly?


> How would FaasCache behave if operating at function level, instead of container level?

_In OpenWhisk by default, containers and functions are managed together 1:1. I.e. a single functions runs inside one container. So by managing the allocated containers, we also manage functions. [44] does not describe a similar wrapper for the function invocations, and our simulation uses the values in the dataset directly._

> How would OpenWhisk without TTL perform i.e., an approach that does not evict containers until the physical resources (or a predefined amount of them) are filled up compared to FaasCache?

_OW resorts to LRU eviction when it needs to reclaim memory on-demand. So the results for this will look like the LRU results in graphs 5-6_

PRATEEK: Use mine. Really about resource-conserving i think. 
