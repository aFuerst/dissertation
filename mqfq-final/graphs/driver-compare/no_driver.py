import os, sys
sys.path.append("/extra/alfuerst/repos/polymorphic-functions-experiments/experiments/traced")
import run_trace
import traceback

ilu_home = "/extra/alfuerst/repos/iluvatar-faas/src/Ilúvatar"
build_level = "release"
load_type="functions"
prewarm=0
log_level='info'
memory=204800
cores=48
gpus=1
fpd=16
enqueueing="All"
mps=False
queue="mqfq"
gpu_util=95
concurrent_creation=5
gpu_running=1
stat_update=500
allowed_overrun=20
service_average=10.0
environment='gpu1'
hosts_addrs="@../../ansible/vars/host_addresses.yml"
ansible_env_hosts_ini = os.path.join("../../ansible/environments/", environment, "hosts.ini")
host=f"v-{environment}.victor.futuresystems.org"
ITERS=8

def run_bench_load(log_file, results_dir, host, bench_file):
  gen_pth = os.path.join(ilu_home, "target", build_level, "iluvatar_load_gen")
  load_args = [gen_pth, "benchmark", "--out-folder", results_dir, "--port", 8070, "--host", host, "--cold-iters", ITERS, "--warm-iters", ITERS, "--target", "worker", "--function-file", bench_file]
  run_trace.run_cmd(load_args, log_file)

def run_bench(results_dir, use_driver, bench_file="./gpu-benchmark.csv", prefetch=True, extra_args="") -> bool:
  os.makedirs(results_dir, exist_ok=True)
  log_file = os.path.join(results_dir, "orchestration.log")

  with open(log_file, 'w') as log_file_fp:
    try:
      run_trace.rust_build(log_file_fp, build_level, ilu_home)
      run_trace.pre_run_cleanup(log_file_fp, results_dir, build_level, log_level, ilu_home, host, ansible_env_hosts_ini, hosts_addrs)
      run_trace.run_ansible(log_file=log_file_fp, build=build_level, log_level=log_level, ilu_home=ilu_home, 
                  memory=memory, cores=cores, gpus=gpus, fpd=fpd, enqueueing=enqueueing, mps=mps, 
                  queue=queue, prefetch=prefetch, gpu_util=gpu_util, creation=concurrent_creation, 
                  gpu_running=gpu_running, stat_update=stat_update, allowed_overrun=allowed_overrun, 
                  ansible_args=extra_args, service_average=service_average, use_driver=use_driver,
                  ansible_host_file=ansible_env_hosts_ini, hosts_addrs_file=hosts_addrs)
      run_bench_load(log_file, results_dir, host, bench_file)
      run_trace.remote_cleanup(log_file_fp, results_dir, build_level, log_level, ilu_home, host, ansible_env_hosts_ini, hosts_addrs)

      plot_args = ["python3", "../../analyze/plot_resource_usage.py", "-l", os.path.join(results_dir, "worker_worker1.log")]
      run_trace.run_cmd(plot_args, log_file)
    except KeyboardInterrupt:
      run_trace.remote_cleanup(log_file_fp, results_dir, build_level, log_level, ilu_home, host, ansible_env_hosts_ini, hosts_addrs)
      exit(0)
    except Exception as e:
      log_file_fp.write("Exception encountered:\n")
      log_file_fp.write(str(e))
      log_file_fp.write("\n")
      log_file_fp.write(traceback.format_exc())
      log_file_fp.write("\n")
      run_trace.remote_cleanup(log_file_fp, results_dir, build_level, log_level, ilu_home, host, ansible_env_hosts_ini, hosts_addrs)
      raise e

# run_bench("./no_driver/", use_driver=False, bench_file="./gpu-benchmark.csv")
run_bench("./shrunk_driver/", use_driver=True, bench_file="./gpu-benchmark.csv")
run_bench("./no-ttl/", use_driver=True, bench_file="./gpu-benchmark.csv", extra_args="-e mqfq_ttl_sec=0.0")
# run_bench("./shrunk_driver_no_prefetch/", use_driver=True, bench_file="./gpu-benchmark.csv", prefetch=False)
# run_bench("./bypass_driver/", use_driver=True, bench_file="./passthru-driver-gpu-benchmark copy.csv")
# run_bench("./full_driver/", use_driver=True, bench_file="./full-driver-gpu-benchmark.csv")
