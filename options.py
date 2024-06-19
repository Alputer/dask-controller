from dask_gateway_server.options import Options, Integer, Float


def options_handler(options):
    return {
        "worker_cores": options.worker_cores,
        "worker_memory": int(options.worker_memory * 2**30),
    }


c.Backend.DaskGateway.cluster_options = Options(
    Integer("worker_cores", default=1, min=1, max=4, label="Worker Cores"),
    Float("worker_memory", default=1, min=1, max=8, label="Worker Memory (GiB)"),
    handler=options_handler,
)
