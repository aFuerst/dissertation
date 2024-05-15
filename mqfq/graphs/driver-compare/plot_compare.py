import json
import os
import numpy as np
import pandas as pd
import math
from collections import defaultdict
import matplotlib as mpl
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
mpl.rcParams.update({'font.size': 14})
mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
mpl.use('Agg')
cmap="Dark2"
mpl.rcParams['image.cmap'] = cmap
plt.rcParams['image.cmap'] = cmap
mpl.rc('image', cmap=cmap)
cmap = plt.get_cmap(cmap)

def paper_name(name: str):
  name = name.replace("rodinia-", "")
  name = name.replace("pyhpc-", "")
  name = name.replace("onnx-", "")
  name = name.replace("_", " ")
  name = name.replace("torch", "pytorch")
  name = name.title()
  name = name.replace("Pytorch", "PyTorch")
  name = name.replace("Rnn", "RNN")
  name = name.replace("Cupy", "FFT")
  return name

with open("./no_driver/worker_function_benchmarks.json") as f:
  no_driver_data = json.load(f)["data"]

with open("./full_driver/worker_function_benchmarks.json") as f:
  driver_data = json.load(f)["data"]

with open("./shrunk_driver/worker_function_benchmarks.json") as f:
  shrunk_driver_data = json.load(f)["data"]

with open("./shrunk_driver_no_prefetch/worker_function_benchmarks.json") as f:
  shrunk_driver_no_prefetch_data = json.load(f)["data"]

with open("./bypass_driver/worker_function_benchmarks.json") as f:
  bypass_driver_data = json.load(f)["data"]

with open("./no-ttl/worker_function_benchmarks.json") as f:
  no_ttl_data = json.load(f)["data"]

US_TO_SEC =  1_000_000.0

ordered = sorted(no_driver_data.keys())

plot_data = defaultdict(list)

for i, image in enumerate(ordered):
  no_driver_gpu_warm = np.mean(no_driver_data[image]["resource_data"]["gpu"]["warm_results_sec"]) # / US_TO_SEC
  plot_data["no_driver_plot"].append(no_driver_gpu_warm)
  plot_data["no_driver_pts"].append(i)

  driver_gpu_warm = np.mean(driver_data[image]["resource_data"]["gpu"]["warm_results_sec"]) # / US_TO_SEC
  pt = (driver_gpu_warm-no_driver_gpu_warm) / no_driver_gpu_warm
  pt *= 100.0
  plot_data["driver_plot"].append( driver_gpu_warm )
  plot_data["driver_plot_pct"].append(max(pt, 0.0))
  plot_data["driver_pts"].append(i)

  if image in shrunk_driver_data:
    shrunk_driver_gpu_warm = np.mean(shrunk_driver_data[image]["resource_data"]["gpu"]["warm_results_sec"]) # / US_TO_SEC
    pt = (shrunk_driver_gpu_warm-no_driver_gpu_warm) / no_driver_gpu_warm
    pt *= 100.0
    plot_data["shrunk_min"].append(max(0.0, min(shrunk_driver_data[image]["resource_data"]["gpu"]["warm_results_sec"])))
    plot_data["shrunk_max"].append(max(0.0, max(shrunk_driver_data[image]["resource_data"]["gpu"]["warm_results_sec"])))
    plot_data["shrunk_plot"].append( shrunk_driver_gpu_warm )
    plot_data["shrunk_plot_pct"].append(max(pt, 0.0))
    plot_data["shrunk_pts"].append(i)

  if image in shrunk_driver_no_prefetch_data:
    shrunk_driver_gpu_warm = np.mean(shrunk_driver_no_prefetch_data[image]["resource_data"]["gpu"]["warm_results_sec"]) # / US_TO_SEC
    pt = (shrunk_driver_gpu_warm-no_driver_gpu_warm) / no_driver_gpu_warm
    pt *= 100.0
    plot_data["shrunk_nopre_min"].append(max(0.0, min(shrunk_driver_no_prefetch_data[image]["resource_data"]["gpu"]["warm_results_sec"])))
    plot_data["shrunk_nopre_max"].append(max(0.0, max(shrunk_driver_no_prefetch_data[image]["resource_data"]["gpu"]["warm_results_sec"])))
    plot_data["shrunk_nopre_plot"].append( shrunk_driver_gpu_warm )
    plot_data["shrunk_nopre_plot_pct"].append(max(pt, 0.0))
    plot_data["shrunk_nopre_pts"].append(i)

  no_ttl_gpu_warm = np.mean(no_ttl_data[image]["resource_data"]["gpu"]["warm_results_sec"]) # / US_TO_SEC
  pt = (no_ttl_gpu_warm-no_driver_gpu_warm) / no_driver_gpu_warm
  pt *= 100.0
  plot_data["no_ttl_plot"].append( no_ttl_gpu_warm )
  plot_data["no_ttl_plot_pct"].append( max(pt, 0.0) )
  plot_data["no_ttl_pts"].append(i)

  bypass_driver_gpu_warm = np.mean(bypass_driver_data[image]["resource_data"]["gpu"]["warm_results_sec"]) # / US_TO_SEC
  pt = (bypass_driver_gpu_warm-no_driver_gpu_warm) / no_driver_gpu_warm
  pt *= 100.0
  plot_data["bypass_plot"].append( bypass_driver_gpu_warm )
  plot_data["bypass_plot_pct"].append( max(pt, 0.0) )
  plot_data["bypass_pts"].append(i)

#########################################################################################################
  
fig, ax = plt.subplots()
plt.tight_layout()
fig.set_size_inches(5, 3)
lines = []

# pts = list(range(len(driver_plot)))
pts = np.arange(len(plot_data["no_driver_pts"]))
ax.bar(x=np.array(plot_data["no_driver_pts"])-0.2, height=plot_data["no_driver_plot"], color="black", label="No Shim", width=0.3)
# ax.scatter(x=pts, y=driver_plot, color="red", marker="*", label="Driver")
# ax.bar(x=np.array(plot_data["shrunk_nopre_pts"]), height=plot_data["shrunk_nopre_plot"], color="darkgray", label="Shim; No Prefetch", width=0.2)
ax.bar(x=np.array(plot_data["shrunk_pts"])+0.2, height=plot_data["shrunk_plot"], color="silver", label="Shim", width=0.3)
# ax.scatter(x=pts, y=bypass_plot, color="yellow", marker='^', label="Passthrough Driver")
ax.set_ylabel("Exec Time (Sec)")

ax2 = ax.twinx()
COLOR="red"
ax2.scatter(x=np.array(plot_data["shrunk_pts"]), y=1+np.array(plot_data["shrunk_plot_pct"])/100.0, color=COLOR, marker='*', label="Overhead")
ax2.set_ylabel("Function Overhead")
ax2.yaxis.label.set_color(COLOR)
ax2.tick_params(axis='y', colors=COLOR)
ax2.set_ylim(1.0, None)

ax.legend()
# ax.set_yscale("log")
ax.set_xticks(pts)
ax.set_xticklabels(map(paper_name, ordered), rotation=90)
save_fname = os.path.join(f"exec_time")
plt.savefig(save_fname+".png", bbox_inches="tight")
plt.savefig(save_fname+".pdf", bbox_inches="tight")
plt.close(fig)

#########################################################################################################

fig, ax = plt.subplots()
plt.tight_layout()
fig.set_size_inches(5, 3)
lines = []

pts = list(range(max([len(plot_data["driver_pts"])])))
ax.scatter(x=plot_data["driver_pts"], y=plot_data["driver_plot_pct"], color="red", marker="v", label="Driver")
ax.scatter(x=plot_data["shrunk_pts"], y=plot_data["shrunk_plot_pct"], color="deepskyblue", marker='*', label="Shrunk Driver")
# ax.scatter(x=plot_data["shrunk_pts"], y=plot_data["shrunk_max"], color="navy", marker='*', label="Shrunk Driver Max")
# ax.scatter(x=plot_data["shrunk_pts"], y=plot_data["shrunk_min"], color="aqua", marker='*', label="Shrunk Driver Min")
ax.scatter(x=plot_data["shrunk_nopre_pts"], y=plot_data["shrunk_nopre_plot_pct"], color="tab:green", marker='.', label="Shrunk; No Prefetch")
ax.scatter(x=plot_data["bypass_pts"], y=plot_data["bypass_plot_pct"], color="pink", marker='^', label="Passthrough Driver")
ax.scatter(x=plot_data["no_ttl_pts"], y=plot_data["no_ttl_plot_pct"], color="purple", marker='^', label="No TLL Driver")

ax.set_ylabel("Exec Time Increase %")
ax.legend(loc=(1,0))
# ax.tick_params(
#     axis='x',          # changes apply to the x-axis
#     which='both',      # both major and minor ticks are affected
#     bottom=False,      # ticks along the bottom edge are off
#     top=False,         # ticks along the top edge are off
#     labelbottom=False) # labels along the bottom edge are off

ax.set_yscale("log")
ax.set_xticks(pts)
ax.set_xticklabels(map(paper_name, ordered), rotation=90)
save_fname = os.path.join(f"exec_increase.png")
plt.savefig(save_fname, bbox_inches="tight")
plt.close(fig)

