# Assignment 2 – MapReduce: students per grade category

**Name:** Ankona Mukherjee
**Registration No.:** 202400560

Counts the number of students in each grade category (S, A, B, C, D, E, F) for every
subject, using the previous semester's final exam results as the sample data.

## How it works
| Step | File | What it does |
|---|---|---|
| Map | `mapper.py` | reads `subject,grade` rows, emits `<subject>\|<grade>  1` |
| Shuffle/sort | `run_local.py` | sorts mapper output by key |
| Reduce | `reducer.py` | sums the counts for each `<subject>\|<grade>` key |

`mapper.py` and `reducer.py` read stdin and write stdout, so they also run unchanged on
Hadoop Streaming.

## Data
`data/subject1.csv` ... `data/subject6.csv` hold one row per student with only `subject,grade`
(previous semester final exam results, six subjects). Student identifiers were removed.
Absentees, detentions and malpractice cases (`I`, `DT`, `MP`) are not grade categories and are skipped.
To add a subject, drop another CSV with the same columns into `data/`.

## Run
```bash
python3 run_local.py
```

## Result
```
Subject       S    A    B    C    D    E    F  Total
Subject 1     7   50   65   60   33   21    7    243
Subject 2    19   83   82   76   78   35    5    378
Subject 3    17   36   53   57   44   43   15    265
Subject 4    17   30   44   37   48   57   23    256
Subject 5    13   25   29   36   32   37   15    187
Subject 6     2    2    6    8   13   11    1     43
```
