from pm4py.objects.log.exporter.xes import exporter as xes_exporter
from pm4py.objects.log.obj import EventLog, Trace, Event

# Create an empty event log
log = EventLog()

# Define traces (each trace represents a case/process instance)
trace1 = Trace()
trace1.attributes["concept:name"] = "Case1"
trace1.append(Event({"concept:name": "Start", "time:timestamp": "2024-01-01T12:00:00"}))
trace1.append(Event({"concept:name": "Task A", "time:timestamp": "2024-01-01T12:05:00"}))
trace1.append(Event({"concept:name": "Task B", "time:timestamp": "2024-01-01T12:10:00"}))
trace1.append(Event({"concept:name": "End", "time:timestamp": "2024-01-01T12:15:00"}))

trace2 = Trace()
trace2.attributes["concept:name"] = "Case2"
trace2.append(Event({"concept:name": "Start", "time:timestamp": "2024-01-02T08:00:00"}))
trace2.append(Event({"concept:name": "Task A", "time:timestamp": "2024-01-02T08:10:00"}))
trace2.append(Event({"concept:name": "Task C", "time:timestamp": "2024-01-02T08:20:00"}))
trace2.append(Event({"concept:name": "End", "time:timestamp": "2024-01-02T08:30:00"}))

# Add traces to log
log.append(trace1)
log.append(trace2)

# Save to a file
xes_file_path = "simple_event_log.xes"
xes_exporter.apply(log, xes_file_path)

print(f"Event log saved as {xes_file_path}")
