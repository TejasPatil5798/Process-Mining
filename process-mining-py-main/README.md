# Process mining - Python and pm4py

## Description

This process mining project discovers the process model of an event log using the process mining algorithms **Alpha Miner**, **Heuristics Miner** and **Inductive Miner**.  
After discovering the process models, it performs evaluation, finding it's fitness, precision, generalization and simplicity values.  
Lastly it performs conformance checking using the Replay Fitness method. Conformance checking compares the discovered model with the actual event log to identify possible deviations and potential bottlenecks.  
The event log contains activities of a smart home.

>*This project was made during my Intelligent Systems course in University.*

## How to run

1. The event log file needs to be in the same directory as the python script file.
2. Execute ```py <filename>.py```.

## Results

Alpha Miner Process model  

![Alpha Miner](https://github.com/ChrisTs8920/process-mining-py/blob/main/output/alpha.png?raw=true)

Heuristics Miner Process model  

![Heuristics Miner](https://github.com/ChrisTs8920/process-mining-py/blob/main/output/heuristics.png?raw=true)

Inductive Miner Process model  

![Inductive Miner](https://github.com/ChrisTs8920/process-mining-py/blob/main/output/inductive.png?raw=true)

### Evaluations

| |fitness | precision | generaliztion | simplicity |
|-|--------|-----------|---------------|------------|
| Alpha miner unfiltered log | 0.38 | 0.02 | 0.89 | 1.0 |
| Alpha miner filtered log | 0.66 | 0.02 | 0.89 | 1.0 |
| Heuristic miner unfiltered log | 0.95 | 0.31 | 0.69 | 0.51 |
| Heuristic miner filtered log | 0.94 | 0.31 | 0.71 | 0.52 |
| Inductive miner unfiltered log | 0.98 | 0.15 | 0.87 | 0.64 |
| Inductive miner filtered log  | 0.98 | 0.15 | 0.88 | 0.64 |
