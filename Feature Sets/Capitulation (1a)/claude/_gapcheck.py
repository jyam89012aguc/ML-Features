"""Content gap audit for folders 26-50: checks whether each folder's feature
code actually references the canonical indicators for its domain. Reports
which well-known indicators are PRESENT vs MISSING. Read-only."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# folder -> {canonical concept: [keyword aliases to grep, case-insensitive]}
CHECK = {
    "01_drawdown_depth": {
        "max drawdown": ["max_drawdown", "maxdd", "max_dd"],
        "average drawdown": ["avg_drawdown", "mean_drawdown", "average_dd", "avg_dd"],
        "conditional DaR / tail drawdown": ["cdar", "conditional_drawdown", "tail_drawdown"],
        "drawdown deviation": ["drawdown_dev", "dd_deviation", "dd_std", "drawdown_std"],
        "drawdown from ATH": ["ath", "all_time", "expanding"],
    },
    "02_drawdown_duration": {
        "days underwater": ["underwater", "days_below", "time_below"],
        "days since high": ["days_since", "since_high", "time_since"],
        "recovery time": ["recovery", "time_to_recover", "recover"],
        "longest drawdown": ["longest", "max_duration", "max_underwater"],
        "fraction of time underwater": ["frac", "fraction", "pct_time"],
    },
    "03_drawdown_shape": {
        "convexity/concavity": ["convex", "concav"],
        "curvature": ["curvature", "curv"],
        "linear-fit residual / R2": ["residual", "r2", "r_squared", "rmse"],
        "decline concentration": ["first_third", "front_load", "third", "concentration"],
    },
    "04_drawdown_velocity": {
        "decline slope": ["slope", "ols"],
        "decline speed/rate": ["velocity", "veloc", "rate", "speed"],
        "worst N-day drop": ["worst", "min_return", "fastest"],
        "ATR-normalized speed": ["atr"],
    },
    "05_underwater_curve": {
        "Ulcer Index": ["ulcer"], "pain index": ["pain"],
        "underwater area/integral": ["area", "integral", "auc"],
        "Martin ratio / UPI": ["martin", "upi"],
        "average underwater depth": ["avg_depth", "mean_depth", "average_depth"],
        "max underwater duration": ["duration", "sustained", "longest"],
    },
    "06_low_proximity": {
        "distance above trailing low": ["above_low", "dist_low", "from_low", "to_low"],
        "new-low flags/counts": ["new_low", "newlow"],
        "stochastic position in range": ["stoch", "range_pos", "pct_rank"],
        "near-low frequency": ["near_low", "touch", "within"],
    },
    "07_peak_to_trough": {
        "peak-trough ratio": ["peak", "trough", "ptt"],
        "recovery fraction so far": ["recovery", "retrace", "retracement"],
        "swing amplitude": ["swing", "amplitude", "leg"],
    },
    "08_decline_streaks": {
        "consecutive down days": ["consec", "streak", "down_day"],
        "down weeks/months": ["week", "month"],
        "streak severity": ["severity", "cum_loss", "streak_loss"],
        "lower-low streak": ["lower_low", "new_low"],
    },
    "09_price_compression": {
        "range narrowing/contraction": ["narrow", "compress", "contract"],
        "Bollinger Band width": ["bollinger", "bb_width", "band_width"],
        "squeeze (BB/Keltner)": ["squeeze", "keltner"],
        "NR7/NR4": ["nr7", "nr4"], "inside bar": ["inside_bar"],
    },
    "10_trough_clustering": {
        "local minima density": ["local_min", "minima", "trough"],
        "double/triple bottom": ["double", "triple", "bottom"],
        "support retest": ["retest", "support", "revisit"],
        "trough spacing": ["spacing", "gap_between", "cluster"],
    },
    "11_decline_path_entropy": {
        "Shannon entropy": ["entropy", "shannon"],
        "sign-change rate": ["sign_change", "sign_flip", "zero_cross"],
        "path efficiency": ["efficiency", "path_eff", "directional"],
        "fractal dimension": ["fractal", "higuchi"],
        "Hurst exponent": ["hurst"], "permutation entropy": ["permutation"],
    },
    "12_high_water_distance": {
        "distance from ATH high-water mark": ["ath", "high_water", "hwm"],
        "time since ATH": ["days_since", "since_high", "staleness", "age"],
        "regain multiple required": ["regain", "recovery_multiple", "required", "to_recover"],
    },
    "13_drawdown_acceleration": {
        "drawdown 2nd derivative": ["accel", "second_deriv", "2nd"],
        "decline speeding up": ["speeding", "speed_up", "increasing"],
        "drawdown jerk": ["jerk", "third_deriv"],
        "velocity change": ["velocity", "slope"],
    },
    "14_recovery_failure": {
        "failed bounce": ["failed", "fail", "failed_bounce"],
        "lower highs in drawdown": ["lower_high"],
        "bounce magnitude": ["bounce", "rally", "rebound"],
        "recovery rollover/relapse": ["rollover", "relapse", "fade"],
    },
    "15_volume_blowoff": {
        "relative volume (RVOL)": ["rvol", "relative_vol", "rel_volume"],
        "volume z-score": ["zscore", "z_score"],
        "volume spike vs median": ["spike", "vs_median", "ratio"],
        "volume multiples 3x/5x": ["3x", "5x", "mult"],
        "volume percentile rank": ["pct_rank", "percentile"],
    },
    "16_volume_persistence": {
        "sustained elevated volume": ["sustain", "persist", "elevated"],
        "consecutive high-volume days": ["consec", "streak", "count"],
        "multi-day volume aggregate": ["multi_day", "days_above"],
        "volume above MA duration": ["above_ma", "above_avg"],
    },
    "17_volume_climax": {
        "climax volume": ["climax"],
        "single-day extreme volume": ["single", "extreme", "max_vol"],
        "3x-10x volume spike": ["3x", "5x", "10x", "spike"],
        "churn / effort-vs-result": ["churn", "effort"],
    },
    "18_volume_dryup": {
        "volume dry-up": ["dryup", "dry_up", "dry"],
        "volume collapse/contraction": ["collapse", "contract"],
        "low-volume readings": ["low_vol", "quiet"],
        "volume vs trailing minimum": ["min", "trough"],
    },
    "19_volume_trend": {
        "volume slope/trend": ["slope", "trend"],
        "volume oscillator": ["vol_osc", "volume_osc", "oscillator"],
        "volume moving average": ["volume_ma", "vol_ma", "vol_sma", "vol_ema"],
        "ease of movement (EMV)": ["ease", "emv"],
        "volume RSI": ["volume_rsi", "vol_rsi"],
    },
    "20_up_down_volume": {
        "On-Balance Volume (OBV)": ["obv", "on_balance"],
        "up/down volume ratio": ["up_down", "updown", "up_vol", "down_vol"],
        "Negative Volume Index": ["nvi", "negative_volume"],
        "Positive Volume Index": ["pvi", "positive_volume"],
        "up vs down volume": ["up_volume", "down_volume"],
    },
    "21_volume_concentration": {
        "volume concentration": ["concentration", "concentr"],
        "Gini / Herfindahl of volume": ["gini", "herfindahl", "hhi"],
        "share of volume in worst days": ["worst", "share", "top_n", "topn"],
        "volume entropy": ["entropy"],
    },
    "22_volume_price_divergence": {
        "Accumulation/Distribution Line": ["accum", "ad_line", "adl", "distribution"],
        "Chaikin Money Flow": ["chaikin", "cmf"],
        "Chaikin Oscillator": ["chaikin_osc", "chaikin_oscillator"],
        "OBV divergence": ["obv"],
        "Volume Price Trend (VPT)": ["vpt", "volume_price_trend"],
        "Force Index": ["force_index", "force"],
        "Money Flow Index": ["money_flow", "mfi"],
        "Twiggs Money Flow": ["twiggs"],
    },
    "23_dollar_volume_shock": {
        "dollar volume": ["dollar_vol", "dollar_volume", "dvol"],
        "turnover": ["turnover"], "VWAP": ["vwap"],
        "Amihud illiquidity": ["amihud", "illiquid"],
        "dollar-volume spike/shock": ["spike", "shock", "zscore"],
    },
    "24_volume_distribution": {
        "volume skew": ["skew"], "volume kurtosis": ["kurt"],
        "volume percentile/rank": ["percentile", "pct_rank", "rank"],
        "volume entropy": ["entropy"],
        "volume distribution tails": ["tail", "quantile"],
    },
    "25_momentum_decay": {
        "rate of change (ROC)": ["roc", "rate_of_change"],
        "multi-horizon momentum": ["momentum", "horizon", "mom_"],
        "return decay/fade": ["decay", "fade"],
        "momentum half-life": ["half_life", "halflife"],
        "trailing return": ["trailing_return", "ret_", "_return_"],
    },
    "26_rsi_extremes": {
        "Wilder RSI": ["rsi14", "rsi_14", "rsi("], "Connors RSI": ["connors", "crsi"],
        "StochRSI": ["stochrsi", "stoch_rsi"], "Laguerre RSI": ["laguerre"],
        "Cutler RSI": ["cutler"], "smoothed/EMA RSI": ["smoothed_rsi", "ema_rsi"],
        "RSI of RSI": ["rsi_of_rsi", "double_rsi"],
    },
    "27_momentum_exhaustion": {
        "rate of change": ["roc", "rate_of_change"], "MACD histogram": ["macd"],
        "deceleration": ["decel", "exhaust"], "efficiency ratio": ["efficiency", "kaufman"],
        "TD/DeMark sequential": ["td_seq", "demark", "sequential"],
        "momentum slope": ["slope", "second_deriv", "accel"],
    },
    "28_return_distribution": {
        "skew": ["skew"], "kurtosis": ["kurt"], "tail ratio": ["tail"],
        "VaR/CVaR": ["cvar", "_var_", "value_at_risk", "expected_shortfall"],
        "Jarque-Bera": ["jarque"], "Hurst": ["hurst"], "entropy": ["entropy"],
        "autocorrelation": ["autocorr", "acf"], "downside/semi": ["downside", "semi"],
    },
    "29_consecutive_loss": {
        "loss streak": ["streak", "consec"], "cumulative streak loss": ["cum", "cumulative"],
        "max drawdown run": ["max_loss", "worst"],
    },
    "30_relative_strength": {
        "price vs SMA": ["sma", "_ma_"], "price vs EMA": ["ema"],
        "Mansfield RS": ["mansfield"], "DEMA/TEMA": ["dema", "tema"],
        "Hull MA": ["hull", "hma"], "MA ribbon": ["ribbon"],
    },
    "31_oscillator_extremes": {
        "Stochastic": ["stoch"], "Williams %R": ["williams"], "CCI": ["cci"],
        "Ultimate Oscillator": ["ultimate"], "Awesome Oscillator": ["awesome"],
        "Chande CMO": ["cmo", "chande"], "TRIX": ["trix"], "Fisher Transform": ["fisher"],
        "DPO": ["dpo", "detrended"], "PPO": ["ppo"], "Aroon": ["aroon"],
        "KST": ["kst", "know_sure"], "Coppock": ["coppock"], "MFI": ["mfi", "money_flow"],
        "Stoch Momentum Index": ["smi"], "Schaff": ["schaff"], "Klinger": ["klinger"],
        "RVI": ["rvi", "relative_vigor"],
    },
    "32_momentum_divergence": {
        "regular divergence": ["regular", "divergence", "diverg"],
        "hidden divergence": ["hidden"], "RSI divergence": ["rsi"],
        "MACD divergence": ["macd"], "OBV divergence": ["obv"],
        "price-momentum new-low": ["new_low", "lower_low"],
    },
    "33_trend_breakdown": {
        "ADX": ["adx"], "DMI/DI": ["dmi", "di_plus", "di_minus", "directional"],
        "MA crossover": ["cross", "golden", "death"], "Parabolic SAR": ["sar", "parabolic"],
        "Supertrend": ["supertrend"], "Aroon": ["aroon"], "Ichimoku": ["ichimoku"],
        "trendline break": ["trendline", "breakdown"],
    },
    "34_velocity_inflection": {
        "velocity": ["velocity", "veloc"], "acceleration": ["accel"],
        "sign change": ["sign_change", "sign_flip", "zero_cross"],
        "inflection": ["inflection", "inflect"], "2nd derivative": ["second_deriv", "curvature"],
    },
    "35_capitulation_thrust": {
        "thrust magnitude": ["thrust"], "sigma/zscore day": ["sigma", "zscore"],
        "90% down day": ["90", "ninety", "down_day"], "selling climax": ["climax", "capitul"],
        "wide-range bar": ["wide_range", "wide_bar"], "key reversal": ["key_reversal", "reversal"],
        "gap-down thrust": ["gap"],
    },
    "36_volatility_spike": {
        "realized vol": ["realized", "rvol", "close_to_close"], "ATR": ["atr"],
        "Parkinson": ["parkinson"], "Garman-Klass": ["garman"],
        "Rogers-Satchell": ["rogers"], "Yang-Zhang": ["yang"],
        "EWMA vol": ["ewma", "ewm_vol"], "vol spike ratio": ["spike", "ratio"],
    },
    "37_range_expansion": {
        "true range": ["true_range", "atr"], "range expansion": ["expansion", "expand"],
        "NR7/WR7": ["nr7", "wr7", "narrow_range", "wide_range"],
        "inside/outside bar": ["inside_bar", "outside_bar"],
    },
    "38_volatility_regime": {
        "vol clustering": ["cluster"], "regime shift": ["regime", "shift"],
        "GARCH-style persistence": ["garch", "persist"], "vol autocorr": ["autocorr"],
        "high/low vol state": ["state", "high_vol", "low_vol"],
    },
    "39_intraday_range": {
        "high-low range": ["high_low", "hl_range", "_range"],
        "range vs price": ["range_pct", "norm_range"], "range trend": ["range_trend", "range_slope"],
    },
    "40_close_location": {
        "close location value": ["clv", "close_location"],
        "close position in range": ["close_pos", "position_in_range", "close_in_range"],
        "Williams accum/dist": ["williams_ad", "accum"],
    },
    "41_range_compression": {
        "range contraction": ["compress", "contract", "narrow"],
        "NR7": ["nr7", "nr4"], "Bollinger/Keltner squeeze": ["squeeze", "bollinger", "keltner"],
        "coiling": ["coil"],
    },
    "42_volatility_of_volatility": {
        "std of vol": ["std_of", "vov"], "CV of vol": ["cv_"],
        "vol range": ["range"], "vol-of-vol ratio": ["ratio"],
    },
    "43_downside_deviation": {
        "semi-deviation": ["semi", "downside"], "Sortino-style": ["sortino"],
        "downside vs upside": ["upside", "asymmetr"], "target semivariance": ["target"],
    },
    "44_atr_normalized_move": {
        "ATR": ["atr"], "move in ATR units": ["atr_unit", "atr_mult", "in_atr", "_per_atr"],
        "ATR-normalized return": ["atr_norm", "norm_atr"],
    },
    "45_panic_bar_signatures": {
        "wide-range bar": ["wide_range", "wide_bar"], "long tail/wick": ["wick", "tail", "shadow"],
        "marubozu": ["marubozu"], "climax bar": ["climax"], "outside bar": ["outside"],
        "key reversal bar": ["key_reversal"],
    },
    "46_gap_structure": {
        "gap up/down": ["gap_up", "gap_down"], "gap magnitude": ["gap_mag", "gap_size", "gap_pct"],
        "gap frequency": ["gap_freq", "gap_count"], "common/breakaway/exhaustion": ["breakaway", "exhaustion", "common_gap"],
        "gap fill": ["gap_fill", "filled"],
    },
    "47_gap_down_clustering": {
        "gap-down cluster": ["cluster", "gap_down"], "gap streak": ["streak", "consec"],
        "island reversal": ["island"], "gap density": ["density", "freq"],
    },
    "48_open_close_dynamics": {
        "open-to-close": ["open_to_close", "open_close", "intraday_ret"],
        "close-to-open": ["close_to_open", "overnight"],
        "overnight vs intraday": ["overnight", "intraday"],
    },
    "49_reversal_patterns": {
        "hammer": ["hammer"], "engulfing": ["engulf"], "piercing line": ["piercing"],
        "morning star": ["morning_star", "morning"], "bullish harami": ["harami"],
        "tweezer bottom": ["tweezer"], "doji": ["doji"], "dragonfly doji": ["dragonfly"],
        "three white soldiers": ["soldiers", "three_white"],
        "abandoned baby": ["abandoned"], "bullish kicker": ["kicker"],
        "belt hold": ["belt"], "three inside up": ["three_inside"],
        "three outside up": ["three_outside"], "key/outside reversal": ["key_reversal", "outside_day"],
    },
    "50_failed_breakdown": {
        "undercut & reclaim": ["undercut", "reclaim"], "false breakdown": ["false", "failed"],
        "Wyckoff spring": ["spring"], "bear trap": ["bear_trap", "trap"],
        "support retest": ["retest", "support"],
    },
}

for folder, concepts in CHECK.items():
    fdir = os.path.join(ROOT, folder)
    if not os.path.isdir(fdir):
        print(f"\n[{folder}]  (folder missing)")
        continue
    blob = ""
    for fn in os.listdir(fdir):
        if fn.endswith(".py"):
            blob += open(os.path.join(fdir, fn), encoding="utf-8").read().lower()
    missing = [c for c, kws in concepts.items() if not any(k in blob for k in kws)]
    present = [c for c in concepts if c not in missing]
    tag = "OK" if not missing else f"GAPS({len(missing)})"
    print(f"\n[{folder}]  {tag}")
    print(f"   present: {', '.join(present) if present else '(none)'}")
    if missing:
        print(f"   MISSING: {', '.join(missing)}")
