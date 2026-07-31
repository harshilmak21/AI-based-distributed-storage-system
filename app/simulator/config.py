NODE_PROFILES = {
    "healthy" : {
        "free_storage" : (700,1000),
        "cpu_usage" : (5,30),
        "memory_usage": (10,40),
        "latency": (5, 20),
        "bandwidth": (700, 1000),
        "reliability": (98, 100),
        "failure_rate": (0, 2),
        "current_load": (5, 30),
    },
    "busy" : {
        "free_storage" : (300,700),
        "cpu_usage" : (60,95),
        "memory_usage": (60,90),
        "latency": (20, 80),
        "bandwidth": (500, 900),
        "reliability": (95, 99),
        "failure_rate": (1, 5),
        "current_load": (60, 95),
    },
    "nearly_full" : {
        "free_storage" : (100,250),
        "cpu_usage" : (20,60),
        "memory_usage": (30,70),
        "latency": (10, 40),
        "bandwidth": (400, 800),
        "reliability": (96, 99),
        "failure_rate": (1, 4),
        "current_load": (20, 60),
    },  
}
FEATURE_WEIGHTS = {
    "free_storage": 0.25,
    "cpu_usage": 0.20,
    "memory_usage": 0.10,
    "latency": 0.15,
    "bandwidth": 0.10,
    "reliability": 0.10,
    "failure_rate": 0.05,
    "current_load": 0.05,
}

FEATURE_RANGES = {
    "free_storage": (100, 1000),
    "cpu_usage": (5, 95),
    "memory_usage": (10, 90),
    "latency": (5, 80),
    "bandwidth": (400, 1000),
    "reliability": (95, 100),
    "failure_rate": (0, 5),
    "current_load": (5, 95),
}
NODE_CONSTRAINTS = {
    "min_free_storage": 150,     # GB
    "max_cpu_usage": 90,         # %
    "max_memory_usage": 90,      # %
    "max_current_load": 90,      # %
    "max_failure_rate": 4.5      # %
}