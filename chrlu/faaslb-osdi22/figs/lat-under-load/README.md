Plots of functions being run under load.
Were created by slowly increasing the number of requestor threads while only having 1 invoker available.

The `./all/` directory includes all data points.
The `./filtered/` directory only includes points taken at a load < 10.

I'm pretty sure the greater than load 10 points were mostly subjected to being stuck in the OW queue due to insufficient memory to run them on the invoker.
There is no way to filter out those functions that spent time queueing vs those that did not.
