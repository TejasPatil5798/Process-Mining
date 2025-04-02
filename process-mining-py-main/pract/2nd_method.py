import os
import pm4py
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.algo.filtering.log.variants import variants_filter

# Load the event log
log_path = os.path.join("pract/simple_event_log.xes")
log = xes_importer.apply(log_path)

# Filter the log to keep only the top 10 variants
filtered_log = variants_filter.filter_variants_top_k(log, 10)

# Discover Petri net using Heuristic Miner
heu_net = heuristics_miner.apply_heu(filtered_log, parameters={
    heuristics_miner.Variants.CLASSIC.value.Parameters.DEPENDENCY_THRESH: 0.5,
    heuristics_miner.Variants.CLASSIC.value.Parameters.MIN_DFG_OCCURRENCES: 1
})
net, initial_marking, final_marking = heuristics_miner.apply(filtered_log)

# Visualize the discovered Petri net from Heuristic Miner
gviz = pn_visualizer.apply(net, initial_marking, final_marking, variant=pn_visualizer.Variants.FREQUENCY)
pn_visualizer.view(gviz)

# Discover Petri net using Alpha Miner
net_alpha, initial_marking_alpha, final_marking_alpha = alpha_miner.apply(filtered_log)

# Visualize the discovered Petri net from Alpha Miner
gviz_alpha = pn_visualizer.apply(net_alpha, initial_marking_alpha, final_marking_alpha)
pn_visualizer.view(gviz_alpha)