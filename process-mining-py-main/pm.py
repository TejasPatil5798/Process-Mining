import os

import pm4py  # version 2.7.4
from pprint import pprint  # pretty printing
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
from pm4py.algo.discovery.inductive import algorithm as inductive_miner
from pm4py.algo.evaluation import algorithm as evaluation
from pm4py.objects.conversion.log import converter as stream_converter
from pm4py.objects.log.importer.xes import importer as xes_import
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.algo.conformance.tokenreplay import algorithm as token_replay


def main():
    # join current file path and log file path
    # returns path to event log file
    # event log file needs to be in the same directory as python file
    file_path = os.path.join(os.path.dirname(__file__), "edited_hh104_labour.xes")

    # 1. read event log
    log = xes_import.apply(file_path)
    log_df = pm4py.convert.convert_to_dataframe(log) #convert log to type DataFrame
    log = pm4py.convert_to_event_log(log)  # convert log to type EventLog

    # 2. print trace structure and event structure
    print("\n2.\n")
    print("TRACE KEYS:")
    print(list(log[0].attributes.keys()))
    print("EVENT KEYS:")
    print(list(log[0][0].keys()))

    # 3. print number of traces
    print("\n3.\n")
    print("Number of traces:", len(log))

    # 4. print number of events
    print("\n4.\n")
    event_stream = stream_converter.apply(
        log, variant=stream_converter.Variants.TO_EVENT_STREAM
    )
    print("Number of events:", len(event_stream))

    # 5. print all the events
    print("\n5.\n")
    print("\n print all the events\n")
    events = log_df.drop_duplicates(subset='concept:name')
    print(events['concept:name'].tolist())

    # 6. print start and end activities of traces, with frequency for each
    print("\n6.\n")
    print("Start activities: ", pm4py.get_start_activities(log))
    print("End activities: ", pm4py.get_end_activities(log))

    # 7. print array
    print("\n7.\n")

    print(log_df[['case:concept:name', 'concept:name', 'lifecycle:transition', 'time:timestamp']])

    # or
    '''for trace in log:
        for event in trace:
            print(
                trace.attributes["concept:name"],
                "\t",
                event["concept:name"],
                "\t",
                event["lifecycle:transition"],
                "\t",
                event["time:timestamp"],
            )'''

    # 8. store traces ending with activity 'end'
    print("\n8.\n")
    filtered_log = pm4py.filter_end_activities(log, ["End"])

    # 9. use alpha miner, inductive miner and heuristics miner
    print("\n9.\n")
    # alpha miner
    a_net, a_initial_marking, a_final_marking = alpha_miner.apply(log)
    af_net, af_initial_marking, af_final_marking = alpha_miner.apply(filtered_log)

    # heuristics miner
    h_net, h_initial_marking, h_final_marking = heuristics_miner.apply(log)
    hf_net, hf_initial_marking, hf_final_marking = heuristics_miner.apply(filtered_log)

    # inductive miner
    # changed in pm4py 2.3.0 - .apply() returns type ProcessTree in inductive_miner
    # inductive_miner.apply() only needs 1 parameter, the log file
    i_net = inductive_miner.apply(log)
    if_net = inductive_miner.apply(filtered_log)

    # convert to PetriNet
    i_net, i_initial_marking, i_final_marking = pm4py.convert_to_petri_net(i_net)
    if_net, if_initial_marking, if_final_marking = pm4py.convert_to_petri_net(if_net)

    # visualize alpha miner (filtered log)
    af_gviz = pn_visualizer.apply(af_net, af_initial_marking, af_final_marking)
    pn_visualizer.view(af_gviz)

    # visualize heuristics miner (filtered log)
    hf_gviz = pn_visualizer.apply(hf_net, hf_initial_marking, hf_final_marking)
    pn_visualizer.view(hf_gviz)

    # visualize inductive miner (filtered log)
    if_gviz = pn_visualizer.apply(if_net, if_initial_marking, if_final_marking)
    pn_visualizer.view(if_gviz)

    # 10. Evaluation
    print("\n10.\n")

    # i. unfiltered log, alpha miner
    i_result = evaluation.apply(log, a_net, a_initial_marking, a_final_marking)

    # ii. filtered log, alpha miner
    ii_result = evaluation.apply(
        filtered_log, af_net, af_initial_marking, af_final_marking
    )

    # iii. unfiltered log, heuristics miner
    iii_result = evaluation.apply(log, h_net, h_initial_marking, h_final_marking)

    # iv. filtered log, heuristics miner
    iv_result = evaluation.apply(
        filtered_log, hf_net, hf_initial_marking, hf_final_marking
    )

    # v. unfiltered log, inductive miner
    v_result = evaluation.apply(log, i_net, i_initial_marking, i_final_marking)

    # vi. filtered log, inductive miner
    vi_result = evaluation.apply(
        filtered_log, if_net, if_initial_marking, if_final_marking
    )

    pprint(i_result)
    pprint(ii_result)
    pprint(iii_result)
    pprint(iv_result)
    pprint(v_result)
    pprint(vi_result)

    # 11. conformance using replay fitness
    print("\n11.\n")
    # use heuristic_miner petri net and filtered log
    replayed_traces = token_replay.apply(
        filtered_log, hf_net, hf_initial_marking, hf_final_marking
    )

    sum = 0
    for dict in replayed_traces:
        if dict['trace_is_fit'] == False:
            sum += 1
    
    print("Number of traces not fit: ", sum)



if __name__ == "__main__":
    main()
