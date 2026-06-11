# Capitulation Feature Build — Handoff

PIT Feature Pipeline / Capitulation track. Phase 1 = characterization of
10x+ winners at their absolute multi-year low. No forward-looking inputs.

---

## 1. AGENT PERMISSIONS NOTE

Paste this once at the start of an agent session so it can run unattended.

```
PERMISSIONS FOR THIS SESSION

You may, without asking per-action:
- Read any file in the working directory and subdirectories
- Create new files and folders in the working directory
- Edit files YOU created in this session
- Run Python (python, python3) to syntax-check and smoke-test generated files
- Run shell commands limited to: mkdir, ls/dir, ast.parse checks, pip install
  of standard scientific packages (pandas, numpy, scipy)
- Access the internet ONLY to look up library/API documentation

You may NOT, without explicit approval:
- Edit or delete any file you did not create this session
- Touch any .duckdb file or anything under the silver DB path
- Touch any file matching 00_pipeline_config.py or the existing 01x/02/03 scripts
- Run any script that connects to a database
- Delete or overwrite existing feature folders

If a file already exists, STOP and ask before overwriting.
Default to "allow for this session" for the permitted actions above.
```

---

## 2. FEATURE-BUILD PROMPT (per folder)

Substitute `[FOLDER_NAME]` from the list in section 3.

```
Fill folder: [FOLDER_NAME]

Task: Generate ML features for this folder's domain ONLY. No overlap with
other folders. This folder measures ONE capitulation dimension. Stay strictly
inside it.
Asset class: US equities. Data: daily OHLCV + Sharadar fundamentals/ownership/
insiders/corporate actions.
Target: capitulation — the absolute multi-year low. Point of maximum distress/
exhaustion. Features measure how a (ticker, date) looks at or near a true
bottom. NOT forward return. All market caps.
Use: characterization of known capitulation points + later anomaly scoring
(isolation forest / autoencoder). No supervised target yet.

Output exactly 4 Python files. File names must include the folder name:
1. [FOLDER_NAME]_base_001_075.py   (75 features)
2. [FOLDER_NAME]_base_076_150.py   (75 features)
3. [FOLDER_NAME]_2nd_derivatives.py (25 features: rate of change of base
   features — captures acceleration of decline/distress)
4. [FOLDER_NAME]_3rd_derivatives.py (25 features: rate of change of 2nd
   derivatives — captures exhaustion/inflection of that acceleration)

All function names prefixed with the folder abbreviation.
All registry dict names include the folder name.
Example for folder volume_blowoff:
  - functions: vb_001_volume_spike_ratio, vb_002_...
  - registry: VOLUME_BLOWOFF_REGISTRY_001_075

Rules:
- Each feature = standalone function taking pandas Series (close, high, low,
  open, volume, or fundamental/ownership names like revenue, netinc, fcf,
  equity, debt, assets, insider_buys, insider_sells, inst_holders, etc.)
- Each function returns a pandas Series
- Each file ends with a registry dict: {name: {inputs: [...], func: fn}}
- Trading days: 252/yr, 63/qtr, 21/mo, 5/wk
- Features computed at a candidate date looking BACKWARD only. No forward-
  looking windows, no peak-after-date, no recovery information. Capitulation
  must be knowable at time t.
- INPUT DISCIPLINE: SEP-domain folders (families 01-59) take ONLY price/volume
  inputs (close, high, low, open, volume). No fundamental or ownership inputs
  in a SEP folder. Fundamental folders (60-100) may take fundamental/ownership
  inputs. Do not smear valuation or fundamental features into price folders.
- Quarterly inputs (Sharadar fundamentals/ownership) must be forward-filled
  to the daily index before use, and aligned to the close Series index.
  State the alignment explicitly in a helper at the top of the file.
- Include utility helpers at top of each file
- Every file must pass ast.parse(), under 75KB
- Do NOT curate, filter, or rank features. Generate volume. ML decides
  significance.
- No README, no markdown, no explanations. Files only.
```

---

## 3. THE 100 FEATURE FAMILIES

Each line: number, `folder_name`, prefix, scope.
Folder name is used directly as `[FOLDER_NAME]`.
Naming: folder `01_drawdown_depth` -> functions `dd_001_...`, registry
`DRAWDOWN_DEPTH_REGISTRY_001_075`.

### SEP — drawdown geometry (01-14) — price/volume inputs only
```
01  01_drawdown_depth          dd    decline magnitude vs trailing highs (1/3/5y, ATH)
02  02_drawdown_duration       ddur  time in drawdown, days since high
03  03_drawdown_shape          dsh   convexity/concavity of the decline path
04  04_drawdown_velocity       dvel  speed of decline, slope of fall
05  05_underwater_curve        uw    area/depth of underwater equity curve
06  06_low_proximity           lp    closeness to trailing min, new-low frequency
07  07_peak_to_trough          ptt   peak-trough ratios, recovery-fraction-so-far
08  08_decline_streaks         dstk  consecutive down days/weeks/months
09  09_price_compression       pcmp  price range narrowing near the low
10  10_trough_clustering       tcl   density of local minima, repeated bottoms
11  11_decline_path_entropy    dpe   smooth-vs-jagged structure of the fall
12  12_high_water_distance     hwd   distance/time from prior all-time high
13  13_drawdown_acceleration   dacc  whether the decline is speeding up
14  14_recovery_failure        rfl   failed bounces, lower-highs within drawdown
```

### SEP — volume structure (15-24) — price/volume inputs only
```
15  15_volume_blowoff          vb    volume spikes vs trailing median
16  16_volume_persistence      vp    sustained elevated volume, multi-day
17  17_volume_climax           vcx   single-day extreme volume events
18  18_volume_dryup            vdry  volume collapse / exhaustion of selling
19  19_volume_trend            vtr   directional drift in volume over weeks
20  20_up_down_volume          udv   volume on down days vs up days
21  21_volume_concentration    vcc   share of volume in worst N days
22  22_volume_price_divergence vpd   volume rising while price falls
23  23_dollar_volume_shock     dvs   dollar-volume spikes, turnover extremes
24  24_volume_distribution     vds   skew/kurtosis of volume distribution
```

### SEP — momentum & exhaustion (25-35) — price/volume inputs only
```
25  25_momentum_decay          mdc   trailing return decay across horizons
26  26_rsi_extremes            rsi   oversold readings, depth/duration
27  27_momentum_exhaustion     mex   loss of downside momentum, deceleration
28  28_return_distribution     rds   skew/kurtosis/tails of trailing returns
29  29_consecutive_loss        ccl   max loss streaks, cumulative streak loss
30  30_relative_strength       rst   price vs own moving averages
31  31_oscillator_extremes     osc   stochastic/williams extreme readings
32  32_momentum_divergence     mdv   price new low without momentum new low
33  33_trend_breakdown         tbd   moving-average crossovers, trend loss
34  34_velocity_inflection     vif   sign change in price velocity
35  35_capitulation_thrust     cth   sharp final-leg-down thrust signatures
```

### SEP — volatility & range (36-45) — price/volume inputs only
```
36  36_volatility_spike        vsp   realized vol spikes vs baseline
37  37_range_expansion         rex   true-range expansion near the low
38  38_volatility_regime       vrg   vol clustering, regime shift detection
39  39_intraday_range          idr   high-low spread behavior daily
40  40_close_location          clv   close position within daily range
41  41_range_compression       rcp   range collapse after expansion
42  42_volatility_of_volatility vov  instability of the volatility itself
43  43_downside_deviation      dsd   semi-variance, downside-only dispersion
44  44_atr_normalized_move     atr   moves measured in ATR units
45  45_panic_bar_signatures    pbs   wide-range / long-tail bar patterns
```

### SEP — gap & price action (46-52) — price/volume inputs only
```
46  46_gap_structure           gap   overnight gap frequency/magnitude
47  47_gap_down_clustering     gdc   clustered down-gaps, gap streaks
48  48_open_close_dynamics     ocd   open-to-close vs close-to-open behavior
49  49_reversal_patterns       rev   intraday reversal bar signatures
50  50_failed_breakdown        fbd   undercut-and-reclaim of prior lows
51  51_shadow_wick_analysis    swk   upper/lower wick ratios at lows
52  52_bar_morphology          bmf   candlestick body/range structural stats
```

### SEP — liquidity & microstructure (53-59) — price/volume inputs only
```
53  53_liquidity_collapse      lqc   illiquidity spikes (Amihud), bid-ask proxy
54  54_turnover_ratio          tnv   volume/shares-outstanding extremes
55  55_price_level_distress    pld   absolute price level, sub-$1/$5 flags
56  56_zero_volume_days        zvd   no-trade days, stale-price frequency
57  57_spread_proxy            spr   high-low spread illiquidity estimators
58  58_trading_intensity       tin   trade-frequency proxies over windows
59  59_market_impact_proxy     mip   return-per-dollar-volume sensitivity
```

### SF1 — fundamental distress (60-76) — fundamental inputs
```
60  60_earnings_collapse       ecl   netinc decline, loss onset, magnitude
61  61_revenue_deterioration   rvd   revenue contraction, growth reversal
62  62_margin_compression      mgc   gross/operating/net margin erosion
63  63_cash_burn               cbr   fcf negative, cash runway depletion
64  64_liquidity_distress      lqd   current/quick ratio collapse
65  65_leverage_stress         lvs   debt/equity, debt/assets escalation
66  66_interest_coverage       icv   EBIT/interest deterioration
67  67_working_capital_drain   wcd   working capital depletion trend
68  68_asset_quality           aqy   writedowns, asset base contraction
69  69_equity_erosion          eqe   retained earnings/book value decline
70  70_dilution_acceleration   dla   share count growth, secondary issuance
71  71_accruals_quality        acq   accruals vs cash earnings divergence
72  72_solvency_scores         slv   Altman-Z / Piotroski composites
73  73_earnings_volatility     evl   instability/variance of earnings series
74  74_fundamental_momentum    fmo   QoQ trend in core metrics
75  75_guidance_distress       gds   estimate-vs-actual gaps, miss severity
76  76_balance_sheet_decay     bsd   multi-quarter balance-sheet deterioration
```

### DAILY/METRICS — valuation collapse (77-82) — valuation inputs
```
77  77_valuation_collapse      vcl   PE/PB/PS compression to extremes
78  78_marketcap_destruction   mcd   market-cap decline magnitude/speed
79  79_ev_distortion           evd   enterprise-value vs equity-value gaps
80  80_yield_distress          yld   dividend/earnings yield spikes
81  81_valuation_vs_history    vvh   multiples vs own trailing range
82  82_valuation_vs_peers      vvp   multiples vs sector/industry medians *
```

### SF2 — insider behavior (83-90) — insider inputs
```
83  83_insider_buy_cluster     ibc   multiple insiders buying within window
84  84_insider_buy_size        ibs   dollar magnitude of insider purchases
85  85_insider_role_weight     irw   CEO/CFO vs director weighting
86  86_insider_buy_sell_ratio  ibr   net buy/sell balance over windows
87  87_insider_timing          itm   insider activity vs drawdown depth
88  88_insider_transaction_freq itf  frequency/acceleration of insider trades
89  89_insider_conviction      icn   purchase size vs insider's prior holdings
90  90_insider_silence         isl   absence/withdrawal of insider activity
```

### SF3 — institutional ownership (91-95) — ownership inputs
```
91  91_institutional_exit      iex   QoQ decline in institutional holders
92  92_ownership_concentration ocn   HHI / top-holder concentration shifts
93  93_institutional_bottom_fish ibf new/increasing large positions at lows
94  94_holder_count_dynamics   hcd   breadth of institutional holder base *
95  95_forced_selling_proxy    fsp   small-institution liquidation signatures
```

### ACTIONS/EVENTS — corporate actions (96-100) — event inputs
```
96  96_dividend_distress       dvd   dividend cuts, suspensions, omissions
97  97_reverse_split_signal    rss   reverse splits, late-stage distress flags
98  98_corporate_event_density ced   8-K / event filing frequency spikes
99  99_going_concern_flags     gcf   going-concern language, audit warnings
100 100_listing_status_risk    lsr   exchange-tier risk, delisting proximity
```

`*` = cross-sectional. Families 82 and 94 need universe-wide peer/sector
medians, not a single ticker's Series. Handle with the cross-sectional
prompt in section 4, or pass a precomputed sector-median Series as an input.

### Build order
- Families 01-59: SEP-only, no dependency. Build first.
- Families 60-100: require SF1/SF2/SF3/DAILY/METRICS/ACTIONS/EVENTS loaded.
  Confirm SF2 and SF3 are in the silver DB before starting 83-95.
- Sparse-data caveat: families 83-100 are event/quarterly driven. Their
  2nd/3rd derivative files will be largely zero/sparse on a daily index.
  Expected. ML decides.

---

## 4. STREAMLINING PROMPTS

### 4a. Batch driver — multiple folders per session
```
Process feature folders in order from the master list. For EACH folder:
1. Create the folder if missing. If it exists with files, SKIP and report.
2. Generate the 4 files per the feature-build prompt.
3. Run ast.parse() on each file. If it fails, fix and re-check.
4. Confirm each file is under 75KB and the registry dict count matches
   (75/75/25/25).
5. Report: folder name, 4 filenames, total feature count, pass/fail.
Do folders N through M. Do not stop on a single failure — log it and continue.
Produce a final summary table of all folders processed.
```

### 4b. Validation / QA pass on existing folders
```
Validate every feature folder in the working directory. For each .py file:
- ast.parse() must pass
- file under 75KB
- every function returns a pandas Series (check return statements)
- registry dict exists, name matches folder, entry count is correct
- every registry func reference points to a defined function
- every input name is a plausible OHLCV or Sharadar field
- SEP folders (01-59) use ONLY close/high/low/open/volume inputs
- no forward-looking window (no negative shift, no .iloc[i+...], no
  peak-after-date logic)
Output a defect table: file, check, status, line. Do not edit anything —
report only.
```

### 4c. Cross-sectional folders (82, 94)
```
Fill folder [FOLDER_NAME]. This is a CROSS-SECTIONAL family — features
compare a ticker against its sector/industry peers.
Function signature: each function takes the ticker's own Series PLUS a
peer-median Series of the same daily index (peer_median_<field>).
All other rules from the standard feature-build prompt apply.
Document the peer-median input contract in a helper at the top of each file.
```

### 4d. Master registry aggregator
```
Scan every feature folder. Import each registry dict. Build one master
registry: capitulation_master_registry.py that imports and merges all
folder registries into MASTER_CAPITULATION_REGISTRY = {...}.
Detect and report: duplicate feature names across folders, name collisions,
missing functions. Do not silently overwrite — report collisions and stop.
File must pass ast.parse().
```

### 4e. Smoke-test harness
```
Write capitulation_smoke_test.py that:
- loads the master registry
- builds a synthetic OHLCV DataFrame (300 rows, random walk) plus synthetic
  Sharadar fields
- runs every registered feature function once
- catches and logs exceptions per feature (name, error)
- reports: total features, passed, failed, all-NaN output, constant output
Output a results table. This is a wiring check, not a correctness check.
Do not connect to any database.
```

### 4f. Redundancy report (post-build, pre-modeling)
```
Write capitulation_correlation_report.py that, given a feature matrix
parquet, computes the pairwise correlation of all features, flags pairs
with |corr| > 0.95, and writes a report grouping near-duplicate features.
Do not delete features — report only. ML / feature selection decides.
```

---

## 5. OPEN ITEMS — confirm before building 60-100

1. SF2 (insiders) and SF3 (institutions): loaded in the silver DB? If not,
   families 83-95 (13 families) cannot be built.
2. Quarterly-to-daily alignment: forward-fill is assumed in the prompt.
   Confirm that matches your silver DB layout.
3. The 10x+ winner population row count — determines whether per-cap-segment
   characterization is statistically meaningful or whole-population only.
