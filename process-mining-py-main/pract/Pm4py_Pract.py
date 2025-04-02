import pm4py

# Load an example event log
log = pm4py.read_xes("pract/simple_event_log.xes")

# Discover the process model using the Inductive Miner
net, initial_marking, final_marking = pm4py.discover_petri_net_inductive(log)

# Visualize the discovered process model
pm4py.view_petri_net(net, initial_marking, final_marking)

# Convert the event log to a DataFrame and display the first few rows
df_log = pm4py.convert_to_dataframe(log)
print(df_log.head())