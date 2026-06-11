"""Generator for families 57, 58, 59 - compact version.

  57 multi_condition_blowoff_detectors (mcbd)
  58 change_point_regime_transition (cprt)
  59 cross_horizon_term_structure (chts)
"""
import os
PROJECT_ROOT = r"C:\Users\jyama\Desktop\short_technical_features_1b"

COMMON_HELPERS = '''import numpy as np
import pandas as pd

YDAYS = 252; QDAYS = 63; MDAYS = 21; WDAYS = 5
DDAYS_2Y = 504; DDAYS_3Y = 756; DDAYS_5Y = 1260


def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]; wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum(); den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _sma(s, n, mp=None):
    if mp is None: mp = max(n // 3, 2)
    return s.rolling(n, min_periods=mp).mean()


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 3, 2)).mean()


def _log_ret(close):
    return _safe_log(close).diff()


def _rolling_q(s, n, q, min_periods=None):
    if min_periods is None: min_periods = max(n // 3, 10)
    return s.rolling(n, min_periods=min_periods).quantile(q)


def _bars_since_last_event(ind):
    arr = ind.values; nb = len(arr); out = np.full(nb, np.nan, dtype=float); last = -1
    for i in range(nb):
        if not np.isnan(arr[i]) and arr[i] > 0.5:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=ind.index)


def _rsi(close, n=14):
    d = close.diff()
    up = d.clip(lower=0.0); dn = (-d).clip(lower=0.0)
    a = up.ewm(alpha=1.0/n, adjust=False, min_periods=n).mean()
    b = dn.ewm(alpha=1.0/n, adjust=False, min_periods=n).mean().replace(0, np.nan)
    return 100.0 - 100.0 / (1.0 + a / b)


def _obv(close, volume):
    return (np.sign(close.diff()).fillna(0.0) * volume).cumsum()


def _macd(close, fast=12, slow=26):
    return _ema(close, fast) - _ema(close, slow)
'''


def _emit_fn(spec, suffix):
    idx, name, doc, args, body, ret, prefix = spec["idx"], spec["name"], spec["doc"], spec["args"], spec.get("body", ""), spec["ret"], spec["prefix"]
    fname = f"{prefix}_{idx:03d}_{name}{suffix}"
    sig = ", ".join(f"{a}: pd.Series" for a in args)
    tail = {"": "", "_d1": ".diff()", "_d2": ".diff().diff()", "_d3": ".diff().diff().diff()"}[suffix]
    bl = []
    if body.strip():
        for L in body.strip("\n").split("\n"):
            bl.append("    " + L if L.strip() else "")
    chunks = [f"def {fname}({sig}) -> pd.Series:", f'    """{doc}"""']
    if bl: chunks.append("\n".join(bl))
    chunks.append(f"    return ({ret}){tail}")
    return "\n".join(chunks) + "\n"


def _emit_file(family, order, a, b, features, helpers):
    suffix = "" if order == "base" else f"_{order}"
    header = f'"""{family["name"]} {order} {a:03d}-{b:03d} - 1b-technical."""\n'
    sel = [f for f in features if a <= f["idx"] <= b]
    assert len(sel) == (b - a + 1)
    parts = [header, helpers, "\n\n"]
    for sp in sel:
        sp = dict(sp, prefix=f"f{family['num']}_{family['abbr']}")
        parts.append(_emit_fn(sp, suffix))
        parts.append("\n")
    reg = f"{family['name_upper']}_{order.upper()}_REGISTRY_{a:03d}_{b:03d}"
    parts.append(f"\n{reg} = {{\n")
    for sp in sel:
        fname = f"f{family['num']}_{family['abbr']}_{sp['idx']:03d}_{sp['name']}{suffix}"
        ir = "[" + ", ".join(f'"{x}"' for x in sp["args"]) + "]"
        parts.append(f'    "{fname}": {{"inputs": {ir}, "func": {fname}}},\n')
    parts.append("}\n")
    out = os.path.join(PROJECT_ROOT, family["folder"], f"{family['folder']}__{order}__{a:03d}_{b:03d}.py")
    with open(out, "w", encoding="utf-8") as f:
        f.write("".join(parts))
    return out


def emit(family, features, helpers):
    assert len(features) == 150, f"{family['name']}: {len(features)}"
    names = [f"{f['idx']:03d}_{f['name']}" for f in features]
    if len(set(names)) != 150:
        from collections import Counter
        raise AssertionError(f"{family['name']} dups: {[k for k,v in Counter(names).items() if v>1]}")
    paths = []
    for order in ["base", "d1", "d2", "d3"]:
        for (a, b) in [(1, 75), (76, 150)]:
            paths.append(_emit_file(family, order, a, b, features, helpers))
    return paths


# Helper: build feature spec
def _S():
    F = []
    def add(name, doc, args, body, ret):
        F.append({"idx": len(F) + 1, "name": name, "doc": doc, "args": args, "body": body, "ret": ret})
    return F, add


# =========================================================================
# FAMILY 57 - multi_condition_blowoff_detectors (mcbd)
# =========================================================================

F57_META = {"num": "57", "abbr": "mcbd",
            "folder": "57_multi_condition_blowoff_detectors",
            "name": "multi_condition_blowoff_detectors",
            "name_upper": "MULTI_CONDITION_BLOWOFF_DETECTORS"}


def _f57():
    F, add = _S()
    # ---- Block A (1-15): 3+ condition single-bar AND-events at 252d high ----
    common_setup = "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\npos = (close - low) / (high - low).replace(0, np.nan)\nv_avg = volume.rolling(MDAYS, min_periods=10).mean()\nrsi = _rsi(close, 14)\natr_n = _safe_div(_atr(high, low, close, MDAYS), close)\nzatr = _rolling_zscore(atr_n, YDAYS)"
    add("at252h_close_lower30_vol_2x", "At 252d high AND close <30% range AND vol>2x avg.",
        ("high","low","close","volume"), common_setup,
        "((high >= rmax - 1e-12) & (pos < 0.30) & (volume > 2.0 * v_avg)).astype(float).where(v_avg.notna() & pos.notna(), np.nan)")
    add("at252h_close_below_open_higher_high_vol_above_avg",
        "At 252d high AND close<open AND high>prev high AND vol>avg.",
        ("open","high","low","close","volume"), common_setup,
        "((high >= rmax - 1e-12) & (close < open) & (high > high.shift(1)) & (volume > v_avg)).astype(float).where(v_avg.notna(), np.nan)")
    add("at252h_atr_top_decile_rsi_above_70",
        "At 252d high AND ATR-N in top decile AND RSI>70.",
        ("high","low","close"),
        "rmax = close.rolling(YDAYS, min_periods=QDAYS).max()\natr_n = _safe_div(_atr(high, low, close, MDAYS), close)\np90 = atr_n.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\nrsi = _rsi(close, 14)",
        "((close >= rmax - 1e-12) & (atr_n > p90) & (rsi > 70.0)).astype(float).where(p90.notna() & rsi.notna(), np.nan)")
    add("at252h_rsi_above_75_close_pos_top_quintile",
        "At 252d high AND RSI>75 AND close-pos>80% (overdrive bar).",
        ("high","low","close"), common_setup,
        "((high >= rmax - 1e-12) & (rsi > 75.0) & (pos > 0.8)).astype(float).where(rsi.notna() & pos.notna(), np.nan)")
    add("at252h_range_above_2atr_close_bottom_half",
        "At 252d high AND day range>2*ATR AND close in bottom half.",
        ("high","low","close"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\natr = _atr(high, low, close, MDAYS)\nrng = high - low\npos = (close - low) / rng.replace(0, np.nan)",
        "((high >= rmax - 1e-12) & (rng > 2.0 * atr) & (pos < 0.5)).astype(float).where(atr.notna() & pos.notna(), np.nan)")
    add("at252h_open_top_quintile_close_bottom_quintile",
        "At 252d high AND open in top 20% range AND close in bottom 20% (full reversal bar).",
        ("open","high","low","close"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nrng = (high - low).replace(0, np.nan)\nop = (open - low) / rng; cp = (close - low) / rng",
        "((high >= rmax - 1e-12) & (op > 0.8) & (cp < 0.2)).astype(float).where(op.notna() & cp.notna(), np.nan)")
    add("at252h_log_ret_below_neg3pct_vol_above_avg",
        "At 252d high AND single-bar log-return<-3% AND vol>avg.",
        ("close","volume"),
        "rmax = close.rolling(YDAYS, min_periods=QDAYS).max()\nr = _log_ret(close)\nv_avg = volume.rolling(MDAYS, min_periods=10).mean()",
        "((close >= rmax - 1e-12) & (r < -0.03) & (volume > v_avg)).astype(float).where(v_avg.notna() & r.notna(), np.nan)")
    add("at252h_above_bb_upper_close_below_open",
        "At 252d high AND high>BB upper AND close<open (rejection at BB).",
        ("open","high","low","close"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nma = _sma(close, 20); sd = close.rolling(20, min_periods=10).std()\nbb = ma + 2.0 * sd",
        "((high >= rmax - 1e-12) & (high > bb) & (close < open)).astype(float).where(bb.notna(), np.nan)")
    add("at252h_doji_vol_above_avg",
        "At 252d high AND doji bar (body<10% range) AND vol>avg.",
        ("open","high","low","close","volume"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nrng = (high - low).replace(0, np.nan); body = (close - open).abs() / rng\nv_avg = volume.rolling(MDAYS, min_periods=10).mean()",
        "((high >= rmax - 1e-12) & (body < 0.10) & (volume > v_avg)).astype(float).where(body.notna() & v_avg.notna(), np.nan)")
    add("at252h_inside_bar_with_lower_close_lag",
        "Inside bar (prior) at 252d high AND current close < prior close.",
        ("high","low","close"),
        "rmax = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()\ninside = (high.shift(1) <= high.shift(2)) & (low.shift(1) >= low.shift(2))\npah = (high.shift(1) >= rmax - 1e-12)",
        "(inside & pah & (close < close.shift(1))).astype(float).where(inside.notna(), np.nan)")
    add("at252h_gap_up_then_close_below_prev_close",
        "At 252d high AND open>prev close AND close<prev close (failed gap).",
        ("open","high","close"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "((high >= rmax - 1e-12) & (open > close.shift(1)) & (close < close.shift(1))).astype(float).where(rmax.notna(), np.nan)")
    add("at252h_gap_above_prev_high_then_close_below_prev_high",
        "At 252d high AND open>prev high AND close<prev high (true gap fail).",
        ("open","high","close"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "((high >= rmax - 1e-12) & (open > high.shift(1)) & (close < high.shift(1))).astype(float).where(rmax.notna(), np.nan)")
    add("at252h_volume_dryup_new_high",
        "High at 252d max AND vol<0.7*avg (no-demand new high).",
        ("high","volume"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nv_avg = volume.rolling(MDAYS, min_periods=10).mean()",
        "((high >= rmax - 1e-12) & (volume < 0.7 * v_avg)).astype(float).where(v_avg.notna(), np.nan)")
    add("at252h_atr_compression_close_below_open",
        "At 252d high AND ATR-N in bottom-q25 AND close<open.",
        ("open","high","low","close"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\natr_n = _safe_div(_atr(high, low, close, MDAYS), close)\nq25 = atr_n.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)",
        "((high >= rmax - 1e-12) & (atr_n < q25) & (close < open)).astype(float).where(q25.notna(), np.nan)")
    add("recent252h_close_below_sma20_vol_above_avg",
        "Close<SMA20 AND high at 252d max within 5 bars AND vol>avg (breakdown at high).",
        ("close","high","volume"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nrh = (high >= rmax - 1e-12).rolling(WDAYS, min_periods=1).max()\nsma20 = _sma(close, 20)\nv_avg = volume.rolling(MDAYS, min_periods=10).mean()",
        "((rh > 0.5) & (close < sma20) & (volume > v_avg)).astype(float).where(sma20.notna() & v_avg.notna(), np.nan)")

    # ---- Block B (16-30): 2-bar event sequences ----
    add("climax_vol_then_inside_at_high",
        "Bar t-1: vol>2x avg at 252d high; Bar t: inside.",
        ("high","low","volume"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nv_avg = volume.rolling(MDAYS, min_periods=10).mean()\nclimax = (volume.shift(1) > 2.0 * v_avg.shift(1)) & (high.shift(1) >= rmax.shift(1) - 1e-12)\ninside = (high < high.shift(1)) & (low > low.shift(1))",
        "(climax & inside).astype(float).where(v_avg.notna(), np.nan)")
    add("shooting_star_at_high_then_lower_close",
        "Shooting star at 252d high (bar t-1), lower close at t.",
        ("open","high","low","close"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nrng = (high - low).replace(0, np.nan); body = (close - open).abs() / rng\nuw = (high - pd.concat([open, close], axis=1).max(axis=1)) / rng\nshoot = (close < open) & (body < 0.30) & (uw > 0.60) & (high >= rmax - 1e-12)",
        "(shoot.shift(1) & (close < close.shift(1))).astype(float).where(rmax.notna(), np.nan)")
    add("gap_up_at_high_then_gap_down_next_day",
        "Gap up at 252d high (t-1); gap down next day (t).",
        ("open","high","low"),
        "rmax = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()\ng1 = (open.shift(1) > high.shift(2)) & (high.shift(1) >= rmax - 1e-12)\ngd = open < low.shift(1)",
        "(g1 & gd).astype(float).where(rmax.notna(), np.nan)")
    add("bearish_engulf_at_252h_with_volume",
        "Bearish engulf at 252d high AND vol>avg.",
        ("open","high","low","close","volume"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\npup = close.shift(1) > open.shift(1); cdn = close < open\nengulf = (open >= close.shift(1)) & (close <= open.shift(1))\nv_avg = volume.rolling(MDAYS, min_periods=10).mean()",
        "(pup & cdn & engulf & (high.shift(1) >= rmax.shift(1) - 1e-12) & (volume > v_avg)).astype(float).where(v_avg.notna(), np.nan)")
    add("two_lower_closes_after_252h",
        "Bar t-2 at 252d high AND t-1 close<t-2 AND t close<t-1.",
        ("close","high"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nah = (high.shift(2) >= rmax.shift(2) - 1e-12)",
        "(ah & (close.shift(1) < close.shift(2)) & (close < close.shift(1))).astype(float).where(rmax.notna(), np.nan)")
    add("three_lower_highs_after_252h",
        "Bar t-3 at 252d high then t-2,t-1,t all lower highs.",
        ("high",),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nah = (high.shift(3) >= rmax.shift(3) - 1e-12)",
        "(ah & (high.shift(2) < high.shift(3)) & (high.shift(1) < high.shift(2)) & (high < high.shift(1))).astype(float).where(rmax.notna(), np.nan)")
    add("upthrust_after_distribution_2bar",
        "Bar t-1 distribution (open top close bottom); bar t makes 21d-high AND closes below midrange.",
        ("open","high","low","close"),
        "rp = (high.shift(1) - low.shift(1)).replace(0, np.nan)\npop = (open.shift(1) - low.shift(1)) / rp; pcl = (close.shift(1) - low.shift(1)) / rp\ndist = (pop > 0.7) & (pcl < 0.3)\nh21 = high.rolling(MDAYS, min_periods=10).max()\nrng = (high - low).replace(0, np.nan); cp = (close - low) / rng",
        "(dist & (high >= h21 - 1e-12) & (cp < 0.5)).astype(float).where(rp.notna() & rng.notna(), np.nan)")
    add("climax_vol_then_bearish_engulf_at_high",
        "Bar t-1: vol>2x avg at 252d high; bar t: bearish engulf.",
        ("open","high","low","close","volume"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nv_avg = volume.rolling(MDAYS, min_periods=10).mean()\nclimax = (volume.shift(1) > 2.0 * v_avg.shift(1)) & (high.shift(1) >= rmax.shift(1) - 1e-12)\nengulf = (close < open) & (open >= close.shift(1)) & (close <= open.shift(1))",
        "(climax & engulf).astype(float).where(v_avg.notna(), np.nan)")
    add("hanging_man_at_252h_with_volume",
        "Hanging man (small body, long lower wick, body in upper half) at 252d high AND vol>avg.",
        ("open","high","low","close","volume"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nrng = (high - low).replace(0, np.nan); body = (close - open).abs() / rng\nlw = (pd.concat([open, close], axis=1).min(axis=1) - low) / rng\nbt = pd.concat([open, close], axis=1).max(axis=1); bp = (bt - low) / rng\nv_avg = volume.rolling(MDAYS, min_periods=10).mean()",
        "((high >= rmax - 1e-12) & (body < 0.30) & (lw > 0.60) & (bp > 0.7) & (volume > v_avg)).astype(float).where(v_avg.notna() & rng.notna(), np.nan)")
    add("three_white_soldiers_then_red_engulf",
        "3 up bars then bearish-engulf at t.",
        ("open","close"),
        "up3 = (close.shift(3) > open.shift(3)) & (close.shift(2) > open.shift(2)) & (close.shift(1) > open.shift(1))\neg = (close < open) & (open >= close.shift(1)) & (close <= open.shift(1))",
        "(up3 & eg).astype(float).where(open.notna() & close.notna(), np.nan)")
    add("evening_star_at_252h",
        "Evening star at 252d high: up/small/down sequence erasing 1st-bar gains.",
        ("open","high","low","close"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nb1u = close.shift(2) > open.shift(2)\nr2 = (high.shift(1) - low.shift(1)).replace(0, np.nan)\nb2s = (close.shift(1) - open.shift(1)).abs() < 0.3 * r2\nb3d = close < open\ner = close < (open.shift(2) + close.shift(2)) / 2.0\nah = high.shift(2) >= rmax.shift(2) - 1e-12",
        "(b1u & b2s & b3d & er & ah).astype(float).where(r2.notna(), np.nan)")
    add("dark_cloud_cover_at_252h",
        "Dark cloud cover at 252d high.",
        ("open","high","low","close"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\npu = close.shift(1) > open.shift(1); oa = open > close.shift(1)\nmid = (open.shift(1) + close.shift(1)) / 2.0\ncbm = close < mid; su = close > open.shift(1)",
        "(pu & oa & cbm & su & (high >= rmax - 1e-12)).astype(float).where(rmax.notna(), np.nan)")
    add("three_black_crows_at_252h",
        "3 down bars (close<open) each with lower close than prev, at 252d-high context.",
        ("open","close","high"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nd1 = (close.shift(2) < open.shift(2)); d2 = (close.shift(1) < open.shift(1)) & (close.shift(1) < close.shift(2))\nd3 = (close < open) & (close < close.shift(1))\nah = high.shift(3) >= 0.95 * rmax.shift(3)",
        "(d1 & d2 & d3 & ah).astype(float).where(rmax.notna(), np.nan)")
    add("bearish_island_reversal_at_252h",
        "Bar t-3 gap up at 252d high; bar t-1 gap down isolating t-2 as island top.",
        ("open","high","low"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\ngu = (low.shift(3) > high.shift(4)) & (high.shift(3) >= rmax.shift(3) - 1e-12)\ngd = high.shift(1) < low.shift(2)",
        "(gu & gd).astype(float).where(rmax.notna(), np.nan)")
    add("morning_doji_star_at_low_failure",
        "Bar t-2 down at 252d low; bar t-1 doji; bar t up; bar t+1 reverses.",
        ("open","high","low","close"),
        "rmin = low.rolling(YDAYS, min_periods=QDAYS).min()\nb1d = close.shift(3) < open.shift(3)\nr2 = (high.shift(2) - low.shift(2)).replace(0, np.nan)\nb2dj = (close.shift(2) - open.shift(2)).abs() < 0.1 * r2\nb3u = close.shift(1) > open.shift(1)\nat_l = low.shift(3) <= rmin.shift(3) + 1e-12\nfail = close < open.shift(1)",
        "(b1d & b2dj & b3u & at_l & fail).astype(float).where(r2.notna(), np.nan)")

    # ---- Block C (31-45): Volume + range multi-conditions ----
    add("dry_vol_new_high_3_bars",
        "3 bars: each makes new 21d-high AND vol<0.7*avg.",
        ("high","volume"),
        "h21 = high.rolling(MDAYS, min_periods=10).max()\nv_avg = volume.rolling(MDAYS, min_periods=10).mean()\nnd = ((high >= h21 - 1e-12) & (volume < 0.7 * v_avg)).astype(float)",
        "((nd.shift(2) > 0.5) & (nd.shift(1) > 0.5) & (nd > 0.5)).astype(float).where(v_avg.notna(), np.nan)")
    add("vol_climax_narrow_range_breakdown",
        "Bar t-2: vol>3x avg at 252d high. Bar t-1: range<0.5*ATR. Bar t: close<prev low.",
        ("high","low","close","volume"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nv_avg = volume.rolling(MDAYS, min_periods=10).mean()\natr = _atr(high, low, close, MDAYS)\nc2 = (volume.shift(2) > 3.0 * v_avg.shift(2)) & (high.shift(2) >= rmax.shift(2) - 1e-12)\nn1 = (high.shift(1) - low.shift(1)) < 0.5 * atr.shift(1)\nbd = close < low.shift(1)",
        "(c2 & n1 & bd).astype(float).where(v_avg.notna(), np.nan)")
    add("up_close_low_vol_streak_5_at_high",
        "5 bars up-close AND vol<avg AND at 252d high.",
        ("close","volume","high"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nv_avg = volume.rolling(MDAYS, min_periods=10).mean()\nnd = ((close > close.shift(1)) & (volume < v_avg) & (high >= rmax - 1e-12)).astype(float)",
        "((nd.shift(4) > 0.5) & (nd.shift(3) > 0.5) & (nd.shift(2) > 0.5) & (nd.shift(1) > 0.5) & (nd > 0.5)).astype(float).where(v_avg.notna(), np.nan)")
    add("wide_range_distribution_3bars_at_high",
        "3 bars: range>1.5*ATR AND close in bottom half AND at 252d high.",
        ("high","low","close"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\natr = _atr(high, low, close, MDAYS)\nrng = high - low; pos = (close - low) / rng.replace(0, np.nan)\nd = ((rng > 1.5 * atr) & (pos < 0.5) & (high >= rmax - 1e-12)).astype(float)",
        "((d.shift(2) > 0.5) & (d.shift(1) > 0.5) & (d > 0.5)).astype(float).where(atr.notna(), np.nan)")
    add("effort_no_result_at_high",
        "Vol>2x avg AND range<21d-avg-range AND at 252d high.",
        ("high","low","close","volume"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nv_avg = volume.rolling(MDAYS, min_periods=10).mean()\nrng = high - low; ra = rng.rolling(MDAYS, min_periods=10).mean()",
        "((volume > 2.0 * v_avg) & (rng < ra) & (high >= rmax - 1e-12)).astype(float).where(v_avg.notna() & ra.notna(), np.nan)")
    add("vol_above_avg_close_bottom_30_no_new_high",
        "Vol>avg AND close-pos<30% AND high did NOT make 21d-high (distribution day).",
        ("high","low","close","volume"),
        "h21 = high.shift(1).rolling(MDAYS, min_periods=10).max()\nv_avg = volume.rolling(MDAYS, min_periods=10).mean()\npos = (close - low) / (high - low).replace(0, np.nan)",
        "((volume > v_avg) & (pos < 0.30) & (high <= h21 - 1e-12)).astype(float).where(v_avg.notna() & pos.notna(), np.nan)")
    add("low_vol_high_close_no_new_high",
        "Vol<avg AND close-pos>70% AND no new 21d high (no demand at would-be breakout).",
        ("high","low","close","volume"),
        "h21 = high.shift(1).rolling(MDAYS, min_periods=10).max()\nv_avg = volume.rolling(MDAYS, min_periods=10).mean()\npos = (close - low) / (high - low).replace(0, np.nan)",
        "((volume < v_avg) & (pos > 0.70) & (high <= h21 - 1e-12)).astype(float).where(v_avg.notna() & pos.notna(), np.nan)")
    add("vol_3x_no_followthrough_3bars",
        "Bar t-3 vol>3x at 252d high; t-2,t-1,t no new 252d-high.",
        ("high","volume"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nv_avg = volume.rolling(MDAYS, min_periods=10).mean()\nc3 = (volume.shift(3) > 3.0 * v_avg.shift(3)) & (high.shift(3) >= rmax.shift(3) - 1e-12)\nnn = (high.shift(2) < rmax.shift(2) - 1e-12) & (high.shift(1) < rmax.shift(1) - 1e-12) & (high < rmax - 1e-12)",
        "(c3 & nn).astype(float).where(v_avg.notna(), np.nan)")
    add("doji_top_decile_atr_vol_above_avg",
        "Doji AND ATR-N top decile AND vol>avg.",
        ("open","high","low","close","volume"),
        "rng = (high - low).replace(0, np.nan); body = (close - open).abs() / rng\natr_n = _safe_div(_atr(high, low, close, MDAYS), close)\np90 = atr_n.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\nv_avg = volume.rolling(MDAYS, min_periods=10).mean()",
        "((body < 0.10) & (atr_n > p90) & (volume > v_avg)).astype(float).where(body.notna() & p90.notna() & v_avg.notna(), np.nan)")
    add("vol_top_decile_close_pos_below_20_at_high",
        "Vol top decile 252d AND close-pos<20% AND high=252d max (selling climax at top).",
        ("high","low","close","volume"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nvp90 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\npos = (close - low) / (high - low).replace(0, np.nan)",
        "((volume > vp90) & (pos < 0.20) & (high >= rmax - 1e-12)).astype(float).where(vp90.notna() & pos.notna(), np.nan)")
    add("vol_top_range_top_close_below_open",
        "Vol top-decile AND range top-decile AND close<open (wide-range high-vol down bar = distribution).",
        ("open","high","low","close","volume"),
        "vp90 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\nrng = high - low; rp90 = rng.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)",
        "((volume > vp90) & (rng > rp90) & (close < open)).astype(float).where(vp90.notna() & rp90.notna(), np.nan)")
    add("vol_climax_then_2_inside_bars",
        "Bar t-2 vol>3x avg; bars t-1, t both inside.",
        ("high","low","volume"),
        "v_avg = volume.rolling(MDAYS, min_periods=10).mean()\nc = volume.shift(2) > 3.0 * v_avg.shift(2)\ni1 = (high.shift(1) < high.shift(2)) & (low.shift(1) > low.shift(2))\ni0 = (high < high.shift(1)) & (low > low.shift(1))",
        "(c & i1 & i0).astype(float).where(v_avg.notna(), np.nan)")
    add("vol_anomaly_then_gap_down",
        "Vol>3x avg at 252d high; next bar gaps down (open<prev low).",
        ("high","low","open","volume"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nv_avg = volume.rolling(MDAYS, min_periods=10).mean()\nc = (volume.shift(1) > 3.0 * v_avg.shift(1)) & (high.shift(1) >= rmax.shift(1) - 1e-12)",
        "(c & (open < low.shift(1))).astype(float).where(v_avg.notna(), np.nan)")
    add("two_day_vol_burst_lower_2nd_close",
        "Bar t-1 vol>2x up-close at high; bar t vol>2x close<prev close.",
        ("close","volume","high"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nv_avg = volume.rolling(MDAYS, min_periods=10).mean()\nc1 = (volume.shift(1) > 2.0 * v_avg.shift(1)) & (close.shift(1) > close.shift(2)) & (high.shift(1) >= rmax.shift(1) - 1e-12)\nc0 = (volume > 2.0 * v_avg) & (close < close.shift(1))",
        "(c1 & c0).astype(float).where(v_avg.notna(), np.nan)")
    add("hawkes_vol_spike_then_dryup",
        "Vol z>3 at 252d high (t-1); vol z<-1 next bar (t).",
        ("volume","high"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nvz = _rolling_zscore(_safe_log(volume.replace(0, np.nan)), QDAYS)\nsp = (vz.shift(1) > 3.0) & (high.shift(1) >= rmax.shift(1) - 1e-12)\ndr = vz < -1.0",
        "(sp & dr).astype(float).where(vz.notna(), np.nan)")

    # ---- Block D (46-60): RSI + price + vol multi-conditions ----
    add("rsi_above_80_at_252h_atr_z_above_1",
        "RSI>80 AND close=252d max AND ATR-z>1.",
        ("high","low","close"),
        "rsi = _rsi(close, 14); rmax = close.rolling(YDAYS, min_periods=QDAYS).max()\natr_n = _safe_div(_atr(high, low, close, MDAYS), close); zatr = _rolling_zscore(atr_n, YDAYS)",
        "((rsi > 80.0) & (close >= rmax - 1e-12) & (zatr > 1.0)).astype(float).where(rsi.notna() & zatr.notna(), np.nan)")
    add("rsi_overbought_5_consecutive_at_high",
        "5 bars: RSI>70 AND close near 252d max (within 2%).",
        ("close",),
        "rsi = _rsi(close, 14); rmax = close.rolling(YDAYS, min_periods=QDAYS).max()\nob = ((rsi > 70.0) & (close / rmax > 0.98)).astype(float)",
        "((ob.shift(4) > 0.5) & (ob.shift(3) > 0.5) & (ob.shift(2) > 0.5) & (ob.shift(1) > 0.5) & (ob > 0.5)).astype(float).where(rsi.notna(), np.nan)")
    add("rsi_exit_above_70_close_down_vol_above_avg",
        "RSI crosses from>=70 to<70 AND close<open AND vol>avg.",
        ("open","close","volume"),
        "rsi = _rsi(close, 14)\neo = (rsi < 70.0) & (rsi.shift(1) >= 70.0)\nv_avg = volume.rolling(MDAYS, min_periods=10).mean()",
        "(eo & (close < open) & (volume > v_avg)).astype(float).where(rsi.notna() & v_avg.notna(), np.nan)")
    add("rsi_above_75_with_3_lower_highs",
        "RSI>75 AND 3 consecutive lower highs.",
        ("close","high"),
        "rsi = _rsi(close, 14)",
        "((rsi > 75.0) & (high < high.shift(1)) & (high.shift(1) < high.shift(2))).astype(float).where(rsi.notna(), np.nan)")
    add("rsi_above_70_close_pos_below_50_at_high",
        "RSI>70 AND close-pos<50% AND high=252d max (OB reversal candle).",
        ("high","low","close"),
        "rsi = _rsi(close, 14); rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\npos = (close - low) / (high - low).replace(0, np.nan)",
        "((rsi > 70.0) & (pos < 0.5) & (high >= rmax - 1e-12)).astype(float).where(rsi.notna() & pos.notna(), np.nan)")
    add("rsi_above_80_vol_3x_intraday_reversal",
        "RSI>80 AND vol>3x AND close<midrange (parabolic exhaustion).",
        ("high","low","close","volume"),
        "rsi = _rsi(close, 14); v_avg = volume.rolling(MDAYS, min_periods=10).mean()\nmid = (high + low) / 2.0",
        "((rsi > 80.0) & (volume > 3.0 * v_avg) & (close < mid)).astype(float).where(rsi.notna() & v_avg.notna(), np.nan)")
    add("atr_top_decile_close_pos_below_30_at_high",
        "ATR-N top decile AND close-pos<30% AND high=252d max.",
        ("high","low","close"),
        "atr_n = _safe_div(_atr(high, low, close, MDAYS), close); p90 = atr_n.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\npos = (close - low) / (high - low).replace(0, np.nan)\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "((atr_n > p90) & (pos < 0.30) & (high >= rmax - 1e-12)).astype(float).where(p90.notna() & pos.notna(), np.nan)")
    add("atr_compression_then_2x_expansion_at_high",
        "Bar t-1 ATR-N in bottom decile; bar t ATR-N>1.5x prev; at 252d high.",
        ("high","low","close"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\natr_n = _safe_div(_atr(high, low, close, MDAYS), close); p10 = atr_n.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)\nc1 = atr_n.shift(1) < p10.shift(1); ex = atr_n > 1.5 * atr_n.shift(1); ah = high >= rmax - 1e-12",
        "(c1 & ex & ah).astype(float).where(p10.notna(), np.nan)")
    add("vol_z_above_2_rsi_above_70_at_252h",
        "Vol z>2 AND RSI>70 AND high=252d max.",
        ("high","close","volume"),
        "vz = _rolling_zscore(_safe_log(volume.replace(0, np.nan)), YDAYS)\nrsi = _rsi(close, 14)\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "((vz > 2.0) & (rsi > 70.0) & (high >= rmax - 1e-12)).astype(float).where(vz.notna() & rsi.notna(), np.nan)")
    add("dollar_vol_above_p90_close_bottom_quartile_at_high",
        "$-vol>252d p90 AND close-pos<25% AND high=252d max.",
        ("high","low","close","volume"),
        "dv = close * volume; p90 = dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max()\npos = (close - low) / (high - low).replace(0, np.nan)",
        "((dv > p90) & (pos < 0.25) & (high >= rmax - 1e-12)).astype(float).where(p90.notna() & pos.notna(), np.nan)")
    add("rsi_above_70_macd_below_sig_at_high",
        "RSI>70 AND MACD<sig AND close=252d max.",
        ("close","high"),
        "rsi = _rsi(close, 14); macd = _macd(close); sig = macd.ewm(span=9, adjust=False, min_periods=3).mean()\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()",
        "((rsi > 70.0) & (macd < sig) & (close >= rmax - 1e-12)).astype(float).where(rsi.notna() & sig.notna(), np.nan)")
    add("above_bb_upper_rsi_70_close_below_open",
        "Close>BB upper AND RSI>70 AND close<open.",
        ("open","close"),
        "rsi = _rsi(close, 14); ma = _sma(close, 20); sd = close.rolling(20, min_periods=10).std()\nbbu = ma + 2.0 * sd",
        "((close > bbu) & (rsi > 70.0) & (close < open)).astype(float).where(bbu.notna() & rsi.notna(), np.nan)")
    add("mayer_above_2_rsi_70_close_below_open",
        "Mayer>2 AND RSI>70 AND close<open.",
        ("open","close"),
        "rsi = _rsi(close, 14); sma200 = _sma(close, 200); mayer = _safe_div(close, sma200)",
        "((mayer > 2.0) & (rsi > 70.0) & (close < open)).astype(float).where(mayer.notna() & rsi.notna(), np.nan)")
    add("close_sma50_extension_above_15pct_rsi_75",
        "Close/SMA50-1>15% AND RSI>75 (parabolic + extreme OB).",
        ("close",),
        "rsi = _rsi(close, 14); sma50 = _sma(close, 50); ext = _safe_div(close - sma50, sma50)",
        "((ext > 0.15) & (rsi > 75.0)).astype(float).where(ext.notna() & rsi.notna(), np.nan)")
    add("rsi_70_close_below_5d_low_252h_within_5d",
        "RSI>70 AND close<5d-low AND 252d-high within 5 bars (immediate breakdown).",
        ("close","high","low"),
        "rsi = _rsi(close, 14); l5 = low.shift(1).rolling(WDAYS, min_periods=1).min()\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max(); rh = (high >= rmax - 1e-12).shift(WDAYS).rolling(WDAYS, min_periods=1).max()",
        "((rsi > 70.0) & (close < l5) & (rh > 0.5)).astype(float).where(rsi.notna() & l5.notna(), np.nan)")

    # ---- Block E (61-75): Hindenburg-style multi-factor warnings ----
    add("hindenburg_self_proxy_252d",
        "Self-Hindenburg: new 252d-high AND new 252d-low within 21 bars AND vol>avg.",
        ("high","low","volume"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); rmin = low.rolling(YDAYS, min_periods=QDAYS).min()\nnh21 = ((high >= rmax - 1e-12).rolling(MDAYS, min_periods=10).max() > 0.5)\nnl21 = ((low <= rmin + 1e-12).rolling(MDAYS, min_periods=10).max() > 0.5)\nv_avg = volume.rolling(MDAYS, min_periods=10).mean()",
        "(nh21 & nl21 & (volume > v_avg)).astype(float).where(v_avg.notna(), np.nan)")
    add("composite_warning_3of5_topping_count",
        "Count >=3 of 5: RSI>70, MACD<sig, close=252d max, ATR-z>1, close-pos<50%.",
        ("high","low","close"),
        "rsi = _rsi(close, 14); macd = _macd(close); sig = macd.ewm(span=9, adjust=False, min_periods=3).mean()\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()\natr_n = _safe_div(_atr(high, low, close, MDAYS), close); zatr = _rolling_zscore(atr_n, YDAYS)\npos = (close - low) / (high - low).replace(0, np.nan)\ncnt = ((rsi > 70.0).astype(float) + (macd < sig).astype(float) + (close >= rmax - 1e-12).astype(float) + (zatr > 1.0).astype(float) + (pos < 0.5).astype(float))",
        "(cnt >= 3).astype(float).where(rsi.notna() & sig.notna() & zatr.notna() & pos.notna(), np.nan)")
    add("topping_density_3of5_persistence_63d",
        "Fraction of last 63d with 3-of-5 topping count >=3.",
        ("high","low","close"),
        "rsi = _rsi(close, 14); macd = _macd(close); sig = macd.ewm(span=9, adjust=False, min_periods=3).mean()\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()\natr_n = _safe_div(_atr(high, low, close, MDAYS), close); zatr = _rolling_zscore(atr_n, YDAYS)\npos = (close - low) / (high - low).replace(0, np.nan)\ncnt = ((rsi > 70.0).astype(float) + (macd < sig).astype(float) + (close >= rmax - 1e-12).astype(float) + (zatr > 1.0).astype(float) + (pos < 0.5).astype(float))",
        "(cnt >= 3).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()")
    add("five_of_five_topping_indicator",
        "All 5 topping conditions simultaneously.",
        ("high","low","close"),
        "rsi = _rsi(close, 14); macd = _macd(close); sig = macd.ewm(span=9, adjust=False, min_periods=3).mean()\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()\natr_n = _safe_div(_atr(high, low, close, MDAYS), close); zatr = _rolling_zscore(atr_n, YDAYS)\npos = (close - low) / (high - low).replace(0, np.nan)",
        "((rsi > 70.0) & (macd < sig) & (close >= rmax - 1e-12) & (zatr > 1.0) & (pos < 0.5)).astype(float).where(rsi.notna() & sig.notna(), np.nan)")
    add("quadruple_warning_indicator",
        "RSI>75 AND vol>2x AND close<open AND at 252d max.",
        ("open","close","volume","high"),
        "rsi = _rsi(close, 14); v_avg = volume.rolling(MDAYS, min_periods=10).mean()\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "((rsi > 75.0) & (volume > 2.0 * v_avg) & (close < open) & (high >= rmax - 1e-12)).astype(float).where(v_avg.notna() & rsi.notna(), np.nan)")
    add("five_factor_pre_crash_z_composite",
        "z(RSI) + z(vol) + z(atr) + z(close_ext_sma50) + z(MACD-sig) over 252d.",
        ("high","low","close","volume"),
        "rsi = _rsi(close, 14); macd = _macd(close); sig = macd.ewm(span=9, adjust=False, min_periods=3).mean()\natr_n = _safe_div(_atr(high, low, close, MDAYS), close)\nsma50 = _sma(close, 50); ext = _safe_div(close - sma50, sma50)\nz1 = _rolling_zscore(rsi, YDAYS); z2 = _rolling_zscore(_safe_log(volume.replace(0, np.nan)), YDAYS); z3 = _rolling_zscore(atr_n, YDAYS); z4 = _rolling_zscore(ext, YDAYS); z5 = _rolling_zscore(macd - sig, YDAYS)",
        "z1.fillna(0) + z2.fillna(0) + z3.fillna(0) + z4.fillna(0) - z5.fillna(0)")
    add("vol_climax_atr_compression_later",
        "Bar t-5 to t-2 vol climax (>3x avg) AND today ATR<0.5*ATR at climax.",
        ("high","low","close","volume"),
        "v_avg = volume.rolling(MDAYS, min_periods=10).mean(); atr = _atr(high, low, close, MDAYS)\nclimax = (volume > 3.0 * v_avg).astype(float)\ncr = climax.shift(2).rolling(4, min_periods=1).max()\nac = (atr.shift(2) * climax.shift(2)).rolling(4, min_periods=1).max()\ncomp = (atr < 0.5 * ac)",
        "(cr > 0.5).astype(float) * comp.astype(float)")
    add("multi_oscillator_3of3_ob_count_63d",
        "Count of 63d bars with RSI>70 AND Stoch%K>80 AND Williams%R>-20.",
        ("high","low","close"),
        "rsi = _rsi(close, 14)\nhh = high.rolling(14, min_periods=5).max(); ll = low.rolling(14, min_periods=5).min()\nstk = 100.0 * (close - ll) / (hh - ll).replace(0, np.nan)\nwr = -100.0 * (hh - close) / (hh - ll).replace(0, np.nan)\nall3 = ((rsi > 70.0) & (stk > 80.0) & (wr > -20.0)).astype(float).where(rsi.notna(), np.nan)",
        "all3.rolling(QDAYS, min_periods=MDAYS).sum()")
    add("multi_oscillator_ob_decay_indicator",
        "All 3 OB at t-1 but NOT all 3 OB at t (decay).",
        ("high","low","close"),
        "rsi = _rsi(close, 14)\nhh = high.rolling(14, min_periods=5).max(); ll = low.rolling(14, min_periods=5).min()\nstk = 100.0 * (close - ll) / (hh - ll).replace(0, np.nan)\nwr = -100.0 * (hh - close) / (hh - ll).replace(0, np.nan)\nall3 = ((rsi > 70.0) & (stk > 80.0) & (wr > -20.0)).astype(float)",
        "(all3.shift(1) > 0.5).astype(float) * (all3 < 0.5).astype(float)")
    add("close_top_decile_rsi_below_50_at_high",
        "Close in top 10% of 252d range BUT RSI<50 (extreme price/momentum disagreement).",
        ("high","low","close"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); rmin = low.rolling(YDAYS, min_periods=QDAYS).min()\npr = _safe_div(close - rmin, rmax - rmin); rsi = _rsi(close, 14)",
        "((pr > 0.9) & (rsi < 50.0)).astype(float).where(pr.notna() & rsi.notna(), np.nan)")
    add("close_top_decile_macd_negative_at_high",
        "Close top 10% AND MACD<0 AND close=252d max (extreme bearish momentum at top).",
        ("high","low","close"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); rmin = low.rolling(YDAYS, min_periods=QDAYS).min()\npr = _safe_div(close - rmin, rmax - rmin); macd = _macd(close)",
        "((pr > 0.9) & (macd < 0) & (close >= rmax - 1e-12)).astype(float).where(pr.notna() & macd.notna(), np.nan)")
    add("close_sma200_ext_30pct_obv_falling",
        "Close/SMA200>1.3 AND OBV-slope 21d<0 (parabolic + falling OBV).",
        ("close","volume"),
        "sma200 = _sma(close, 200); ext = _safe_div(close - sma200, sma200)\nobv = _obv(close, volume); os = _rolling_slope(obv, MDAYS)",
        "((ext > 0.30) & (os < 0)).astype(float).where(ext.notna() & os.notna(), np.nan)")
    add("five_consecutive_doji_at_high",
        "5 consecutive doji (body/range<15%) at near 252d max.",
        ("open","high","low","close"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nrng = (high - low).replace(0, np.nan); body = (close - open).abs() / rng\ndj = ((body < 0.15) & (high >= 0.98 * rmax)).astype(float)",
        "((dj.shift(4) > 0.5) & (dj.shift(3) > 0.5) & (dj.shift(2) > 0.5) & (dj.shift(1) > 0.5) & (dj > 0.5)).astype(float).where(rng.notna(), np.nan)")
    add("price_z_above_2_dollar_vol_z_below_neg1_at_high",
        "z(close)>2 AND z($-vol)<-1 AND at 252d high (parabolic + low participation).",
        ("close","volume","high"),
        "zc = _rolling_zscore(_safe_log(close), YDAYS); zdv = _rolling_zscore(_safe_log((close * volume).replace(0, np.nan)), YDAYS)\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "((zc > 2.0) & (zdv < -1.0) & (high >= rmax - 1e-12)).astype(float).where(zc.notna() & zdv.notna(), np.nan)")
    add("parabolic_5_up_closes_above_1_5pct",
        "5 consecutive bars with log_ret>1.5% (parabolic acceleration).",
        ("close",),
        "r = _log_ret(close)",
        "((r.shift(4) > 0.015) & (r.shift(3) > 0.015) & (r.shift(2) > 0.015) & (r.shift(1) > 0.015) & (r > 0.015)).astype(float).where(r.notna(), np.nan)")

    return F


def _f57_part2(F):
    def add(name, doc, args, body, ret):
        F.append({"idx": len(F) + 1, "name": name, "doc": doc, "args": args, "body": body, "ret": ret})

    # ---- Block F (76-90): Aftermath events after 252d high ----
    common_aft = "rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); at_max = (high >= rmax - 1e-12).astype(float)\nbars_since = _bars_since_last_event(at_max)"
    add("post252h_count_lower_closes_21d",
        "After 252d high, count of lower-close bars in last 21d.",
        ("close","high"),
        common_aft + "\nlower = (close < close.shift(1)).astype(float)\nin_win = (bars_since <= MDAYS).astype(float)",
        "(lower * in_win).rolling(MDAYS, min_periods=10).sum()")
    add("post252h_count_down_volume_days_21d",
        "After 252d high, count of (close<open, vol>avg) bars in 21d.",
        ("open","close","volume","high"),
        common_aft + "\nv_avg = volume.rolling(MDAYS, min_periods=10).mean()\ndv = ((close < open) & (volume > v_avg)).astype(float)\niw = (bars_since <= MDAYS).astype(float)",
        "(dv * iw).rolling(MDAYS, min_periods=10).sum()")
    add("post252h_max_drawdown_21d",
        "Max drawdown from most recent 252d high within last 21 bars.",
        ("close","high"),
        common_aft + "\npc = close.where(at_max > 0.5).ffill()\ndd = _safe_div(close - pc, pc)\niw = (bars_since <= MDAYS).astype(float)",
        "(dd * iw).rolling(MDAYS, min_periods=10).min()")
    add("post252h_max_drawdown_63d",
        "Max drawdown from most recent 252d high within last 63 bars.",
        ("close","high"),
        common_aft + "\npc = close.where(at_max > 0.5).ffill()\ndd = _safe_div(close - pc, pc)",
        "dd.rolling(QDAYS, min_periods=MDAYS).min()")
    add("post252h_vol_z_change_from_high",
        "Change in vol z from at-high to current.",
        ("volume","high"),
        common_aft + "\nvz = _rolling_zscore(_safe_log(volume.replace(0, np.nan)), YDAYS)\nvz_h = vz.where(at_max > 0.5).ffill()",
        "vz - vz_h")
    add("post252h_atr_z_change_from_high",
        "Change in ATR-z from at-high to current.",
        ("high","low","close"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); at_max = (high >= rmax - 1e-12).astype(float)\natr_n = _safe_div(_atr(high, low, close, MDAYS), close); z = _rolling_zscore(atr_n, YDAYS)\nz_h = z.where(at_max > 0.5).ffill()",
        "z - z_h")
    add("post252h_rsi_change_from_high",
        "Change in RSI from at-high bar to current.",
        ("close","high"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); at_max = (high >= rmax - 1e-12).astype(float)\nrsi = _rsi(close, 14); rsi_h = rsi.where(at_max > 0.5).ffill()",
        "rsi - rsi_h")
    add("post252h_close_below_at_high_close_indicator",
        "Close < close at most-recent 252d high.",
        ("close","high"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); at_max = (high >= rmax - 1e-12).astype(float)\nch = close.where(at_max > 0.5).ffill()",
        "(close < ch).astype(float).where(ch.notna(), np.nan)")
    add("post252h_5pct_loss_indicator",
        "Bars-since-252h>0 AND close < at-high * 0.95.",
        ("close","high"),
        common_aft + "\nch = close.where(at_max > 0.5).ffill()",
        "((bars_since > 0) & (close < ch * 0.95)).astype(float).where(ch.notna(), np.nan)")
    add("post252h_10pct_loss_indicator",
        "Bars-since-252h>0 AND close < at-high * 0.90.",
        ("close","high"),
        common_aft + "\nch = close.where(at_max > 0.5).ffill()",
        "((bars_since > 0) & (close < ch * 0.90)).astype(float).where(ch.notna(), np.nan)")
    add("post252h_recovery_failure_21d_indicator",
        "21d post-252h: max-21d-high < 0.98 * at-high (failed retest).",
        ("high",),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); at_max = (high >= rmax - 1e-12).astype(float)\nbars_since = _bars_since_last_event(at_max)\nhh = high.where(at_max > 0.5).ffill(); h21 = high.rolling(MDAYS, min_periods=10).max()",
        "((bars_since >= MDAYS) & (h21 < hh * 0.98)).astype(float).where(hh.notna(), np.nan)")
    add("post252h_recovery_failure_63d_indicator",
        "63d post-252h: max-63d-high < 0.95 * at-high.",
        ("high",),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); at_max = (high >= rmax - 1e-12).astype(float)\nbars_since = _bars_since_last_event(at_max)\nhh = high.where(at_max > 0.5).ffill(); h63 = high.rolling(QDAYS, min_periods=MDAYS).max()",
        "((bars_since >= QDAYS) & (h63 < hh * 0.95)).astype(float).where(hh.notna(), np.nan)")
    add("post252h_breakdown_below_sma50_21d",
        "Within 21d post-252h, close<SMA50.",
        ("close","high"),
        common_aft + "\nsma50 = _sma(close, 50)",
        "((bars_since > 0) & (bars_since <= MDAYS) & (close < sma50)).astype(float).where(sma50.notna(), np.nan)")
    add("post252h_breakdown_below_sma200_63d",
        "Within 63d post-252h, close<SMA200.",
        ("close","high"),
        common_aft + "\nsma200 = _sma(close, 200)",
        "((bars_since > 0) & (bars_since <= QDAYS) & (close < sma200)).astype(float).where(sma200.notna(), np.nan)")
    add("post252h_first5_avg_lower_close_count",
        "Count of lower-close bars in first 5 bars after a 252d high.",
        ("close","high"),
        common_aft + "\nlower = (close < close.shift(1)).astype(float)\nin_win = ((bars_since >= 0) & (bars_since <= WDAYS)).astype(float)",
        "(lower * in_win).rolling(WDAYS, min_periods=1).sum()")

    # ---- Block G (91-105): MA / crossover events at high ----
    add("close_below_sma50_first_after_252h",
        "Close<SMA50 (cross down) AND most-recent 252h within 21d.",
        ("close","high"),
        "sma50 = _sma(close, 50); rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nam = (high >= rmax - 1e-12).astype(float); bs = _bars_since_last_event(am)\ncd = (close < sma50) & (close.shift(1) >= sma50.shift(1))",
        "(cd & (bs <= MDAYS)).astype(float).where(sma50.notna(), np.nan)")
    add("close_below_sma200_first_after_252h_63d",
        "Close<SMA200 (cross down) within 63d of 252h.",
        ("close","high"),
        "sma200 = _sma(close, 200); rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nam = (high >= rmax - 1e-12).astype(float); bs = _bars_since_last_event(am)\ncd = (close < sma200) & (close.shift(1) >= sma200.shift(1))",
        "(cd & (bs <= QDAYS)).astype(float).where(sma200.notna(), np.nan)")
    add("ema9_below_ema21_at_252h",
        "EMA9 crosses below EMA21 AND at 252d high.",
        ("close","high"),
        "e9 = _ema(close, 9); e21 = _ema(close, 21); rmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "((e9 < e21) & (e9.shift(1) >= e21.shift(1)) & (high >= rmax - 1e-12)).astype(float).where(e21.notna(), np.nan)")
    add("death_cross_sma_within_63d_of_252h",
        "Death cross (SMA50<SMA200) within 63d after a 252h.",
        ("close","high"),
        "sma50 = _sma(close, 50); sma200 = _sma(close, 200)\nd = (sma50 < sma200) & (sma50.shift(1) >= sma200.shift(1))\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nam = (high >= rmax - 1e-12).astype(float); bs = _bars_since_last_event(am)",
        "(d & (bs <= QDAYS)).astype(float).where(sma200.notna() & bs.notna(), np.nan)")
    add("below_all_8_sma_ribbon_after_252h_63d",
        "Close below all 8 SMA ribbon MAs (10..200) AND 252h within 63d.",
        ("close","high"),
        "lens = [10, 20, 30, 50, 80, 100, 150, 200]; mas = pd.concat([_sma(close, n).rename(i) for i, n in enumerate(lens)], axis=1)\nba = (mas.gt(close, axis=0)).all(axis=1).astype(float)\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max(); am = (high >= rmax - 1e-12).astype(float); bs = _bars_since_last_event(am)",
        "(ba & (bs <= QDAYS)).astype(float).where(mas.notna().all(axis=1) & bs.notna(), np.nan)")
    add("ribbon_compression_then_bearish_expansion",
        "Bar t-21: 8-SMA width<252d-q10; bar t: width>2x prior AND short<long (fan down).",
        ("close",),
        "lens = [10, 20, 30, 50, 80, 100, 150, 200]; mas = pd.concat([_sma(close, n).rename(i) for i, n in enumerate(lens)], axis=1)\nw = (mas.max(axis=1) - mas.min(axis=1)) / close.replace(0, np.nan)\np10 = w.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)\nc = w.shift(MDAYS) < p10.shift(MDAYS); ex = w > 2.0 * w.shift(MDAYS)\nfd = mas.iloc[:, 0] < mas.iloc[:, -1]",
        "(c & ex & fd).astype(float).where(p10.notna(), np.nan)")
    add("ema_full_bearish_stack_9_21_55_200",
        "EMA9<21<55<200 (full bearish stack).",
        ("close",),
        "e9 = _ema(close, 9); e21 = _ema(close, 21); e55 = _ema(close, 55); e200 = _ema(close, 200)",
        "((e9 < e21) & (e21 < e55) & (e55 < e200)).astype(float).where(e200.notna(), np.nan)")
    add("bull_to_bear_stack_flip_21d",
        "21d ago: bullish 8-SMA stack; now: bearish 8-SMA stack.",
        ("close",),
        "lens = [10, 20, 30, 50, 80, 100, 150, 200]; mas = pd.concat([_sma(close, n).rename(i) for i, n in enumerate(lens)], axis=1)\ndi = mas.diff(axis=1).iloc[:, 1:]\nbull = (di.lt(0)).all(axis=1).astype(float); bear = (di.gt(0)).all(axis=1).astype(float)",
        "((bull.shift(MDAYS) > 0.5) & (bear > 0.5)).astype(float).where(di.notna().all(axis=1), np.nan)")
    add("close_breaks_atr_trailing_stop_at_high",
        "Close < (max-close-21d - 3*ATR21) AND high made 252h within 5 bars.",
        ("close","high","low"),
        "hh = close.rolling(MDAYS, min_periods=10).max(); atr = _atr(high, low, close, MDAYS)\nstop = hh - 3.0 * atr\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max(); rm = (high >= rmax - 1e-12).rolling(WDAYS, min_periods=1).max()",
        "((close < stop) & (rm > 0.5)).astype(float).where(stop.notna(), np.nan)")
    add("close_breaks_donchian20_lower_at_high",
        "Close<20d low AND high was 252h within 5 bars.",
        ("close","high","low"),
        "l20 = low.shift(1).rolling(20, min_periods=10).min(); rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nrm = (high >= rmax - 1e-12).rolling(WDAYS, min_periods=1).max()",
        "((close < l20) & (rm > 0.5)).astype(float).where(l20.notna(), np.nan)")
    add("close_breaks_supertrend_proxy",
        "Close < (mid - 3*ATR10) AND within 5% of 252d max.",
        ("close","high","low"),
        "atr = _atr(high, low, close, 10); med = (high + low) / 2.0; stop = med - 3.0 * atr\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()",
        "((close < stop) & (close >= 0.95 * rmax)).astype(float).where(stop.notna(), np.nan)")
    add("psar_flip_bearish_proxy",
        "Close < (max-high-21d - 2*ATR21) AND was above 1 bar ago.",
        ("close","high","low"),
        "hh = high.rolling(MDAYS, min_periods=10).max(); atr = _atr(high, low, close, MDAYS); stop = hh - 2.0 * atr",
        "((close < stop) & (close.shift(1) >= stop.shift(1))).astype(float).where(stop.notna(), np.nan)")
    add("close_below_anchored_vwap_from_252h",
        "Close < anchored VWAP from most-recent 252d high.",
        ("close","high","low","volume"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); am = (high >= rmax - 1e-12).astype(float)\ntp = (high + low + close) / 3.0; tpv = tp * volume\naid = am.cumsum()\nnum = tpv.groupby(aid).cumsum(); den = volume.groupby(aid).cumsum()\nvwap = num / den.replace(0, np.nan)",
        "(close < vwap).astype(float).where(vwap.notna(), np.nan)")
    add("close_below_50pct_fib_retracement",
        "Close < 50% Fib from 252d high to 252d low.",
        ("close","high","low"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); rmin = low.rolling(YDAYS, min_periods=QDAYS).min()\nfib = rmax - 0.5 * (rmax - rmin)",
        "(close < fib).astype(float).where(fib.notna(), np.nan)")
    add("close_below_618_fib_retracement",
        "Close < 61.8% Fib retracement (deep retracement = topping confirmed).",
        ("close","high","low"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); rmin = low.rolling(YDAYS, min_periods=QDAYS).min()\nfib = rmax - 0.618 * (rmax - rmin)",
        "(close < fib).astype(float).where(fib.notna(), np.nan)")

    # ---- Block H (106-120): Multi-modal cross-validation ----
    add("price_vs_vol_divergence_3bar_at_high",
        "3 bars: close>prev close AND vol<prev vol AND at 252h.",
        ("close","volume","high"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nud = ((close > close.shift(1)) & (volume < volume.shift(1)) & (high >= rmax - 1e-12)).astype(float)",
        "((ud.shift(2) > 0.5) & (ud.shift(1) > 0.5) & (ud > 0.5)).astype(float).where(rmax.notna(), np.nan)")
    add("close_vs_obv_accel_div_at_high",
        "Close-21d-pct>0 AND OBV-21d-pct<0 AND at 252h.",
        ("close","volume","high"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nobv = _obv(close, volume)\np21 = close.pct_change(MDAYS); o21 = obv.pct_change(MDAYS)",
        "((p21 > 0) & (o21 < 0) & (high >= rmax - 1e-12)).astype(float).where(p21.notna() & o21.notna(), np.nan)")
    add("close_inverse_atr_at_high",
        "Close in 252d top decile AND ATR-N in 252d bottom quartile (complacency at top).",
        ("high","low","close"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); rmin = low.rolling(YDAYS, min_periods=QDAYS).min()\npr = _safe_div(close - rmin, rmax - rmin); atr_n = _safe_div(_atr(high, low, close, MDAYS), close)\nq25 = atr_n.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)",
        "((pr > 0.9) & (atr_n < q25)).astype(float).where(pr.notna() & q25.notna(), np.nan)")
    add("price_z_div_volume_z_count_252d",
        "Count of bars in 252d with close-z>1.5 AND vol-z<-0.5 AND at 252h.",
        ("close","volume","high"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nzc = _rolling_zscore(_safe_log(close), YDAYS); zv = _rolling_zscore(_safe_log(volume.replace(0, np.nan)), YDAYS)\nind = ((zc > 1.5) & (zv < -0.5) & (high >= rmax - 1e-12)).astype(float)",
        "ind.rolling(YDAYS, min_periods=QDAYS).sum()")
    add("intraday_range_top_decile_close_flat",
        "Range/close top decile 252d AND |close-prev|/close<0.5% (churn at top).",
        ("high","low","close"),
        "rng_n = (high - low) / close.replace(0, np.nan); p90 = rng_n.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\nflat = (close - close.shift(1)).abs() / close.replace(0, np.nan) < 0.005",
        "((rng_n > p90) & flat).astype(float).where(p90.notna(), np.nan)")
    add("multi_modal_z_sum_above_3_count_252d",
        "Count of 252d bars where (zc-zobv) + (zc-zmacd) > 3.",
        ("close","volume"),
        "zc = _rolling_zscore(_safe_log(close), YDAYS)\nobv = _obv(close, volume); zo = _rolling_zscore(obv, YDAYS)\nmacd = _macd(close); zm = _rolling_zscore(macd, YDAYS)\ngap = (zc - zo) + (zc - zm)",
        "(gap > 3.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()")
    add("intraday_close_below_open_streak_4_at_high",
        "4 consecutive bars close<open AND each at 252h (relentless intraday selling at top).",
        ("open","close","high"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nda = ((close < open) & (high >= 0.98 * rmax)).astype(float)",
        "((da.shift(3) > 0.5) & (da.shift(2) > 0.5) & (da.shift(1) > 0.5) & (da > 0.5)).astype(float).where(rmax.notna(), np.nan)")
    add("intraday_close_pos_below_30_5bar_at_high",
        "5-bar avg close-pos<30% AND close in 252d top decile (sustained intraday distribution).",
        ("high","low","close"),
        "pos = (close - low) / (high - low).replace(0, np.nan); a5 = pos.rolling(WDAYS, min_periods=3).mean()\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max(); rmin = close.rolling(YDAYS, min_periods=QDAYS).min()\npr = _safe_div(close - rmin, rmax - rmin)",
        "((a5 < 0.30) & (pr > 0.9)).astype(float).where(a5.notna() & pr.notna(), np.nan)")
    add("price_new_high_obv_not_new_high_252d",
        "Close=252d max AND OBV<its 252d max.",
        ("close","volume"),
        "rmax = close.rolling(YDAYS, min_periods=QDAYS).max(); obv = _obv(close, volume); om = obv.rolling(YDAYS, min_periods=QDAYS).max()",
        "((close >= rmax - 1e-12) & (obv < om - 1e-9)).astype(float).where(obv.notna(), np.nan)")
    add("price_new_high_rsi_not_new_high_252d",
        "Close=252d max AND RSI<its 252d max.",
        ("close",),
        "rmax = close.rolling(YDAYS, min_periods=QDAYS).max(); rsi = _rsi(close, 14); rm = rsi.rolling(YDAYS, min_periods=QDAYS).max()",
        "((close >= rmax - 1e-12) & (rsi < rm - 1e-9)).astype(float).where(rsi.notna(), np.nan)")
    add("price_new_high_macd_not_new_high_252d",
        "Close=252d max AND MACD<its 252d max.",
        ("close",),
        "rmax = close.rolling(YDAYS, min_periods=QDAYS).max(); macd = _macd(close); mm = macd.rolling(YDAYS, min_periods=QDAYS).max()",
        "((close >= rmax - 1e-12) & (macd < mm - 1e-9)).astype(float).where(macd.notna(), np.nan)")
    add("triple_non_confirmation_at_252h",
        "Close=252d max AND OBV NOT new high AND RSI NOT new high AND MACD NOT new high.",
        ("close","volume"),
        "rmax = close.rolling(YDAYS, min_periods=QDAYS).max()\nobv = _obv(close, volume); om = obv.rolling(YDAYS, min_periods=QDAYS).max()\nrsi = _rsi(close, 14); rm = rsi.rolling(YDAYS, min_periods=QDAYS).max()\nmacd = _macd(close); mm = macd.rolling(YDAYS, min_periods=QDAYS).max()",
        "((close >= rmax - 1e-12) & (obv < om - 1e-9) & (rsi < rm - 1e-9) & (macd < mm - 1e-9)).astype(float).where(rsi.notna() & macd.notna(), np.nan)")
    add("close_2y_high_3of3_extension",
        "Close=504d max AND close/SMA200>1.5 AND close/SMA50>1.15 AND close/SMA20>1.05.",
        ("close",),
        "r2 = close.rolling(DDAYS_2Y, min_periods=YDAYS).max()\nr200 = _safe_div(close, _sma(close, 200)); r50 = _safe_div(close, _sma(close, 50)); r20 = _safe_div(close, _sma(close, 20))",
        "((close >= r2 - 1e-12) & (r200 > 1.5) & (r50 > 1.15) & (r20 > 1.05)).astype(float).where(r200.notna() & r50.notna() & r20.notna(), np.nan)")
    add("vol_z_3_dollar_vol_z_3_close_below_open",
        "Vol-z>3 AND $-vol-z>3 AND close<open (huge size distribution day).",
        ("open","close","volume"),
        "vz = _rolling_zscore(_safe_log(volume.replace(0, np.nan)), YDAYS); dvz = _rolling_zscore(_safe_log((close * volume).replace(0, np.nan)), YDAYS)",
        "((vz > 3.0) & (dvz > 3.0) & (close < open)).astype(float).where(vz.notna() & dvz.notna(), np.nan)")
    add("vol_2x_intraday_recovery",
        "Vol>2x avg AND (low/open)<-3% AND (close/open)>-0.5% (absorption day).",
        ("open","low","close","volume"),
        "v_avg = volume.rolling(MDAYS, min_periods=10).mean()\nil = _safe_div(low - open, open); ic = _safe_div(close - open, open)",
        "((volume > 2.0 * v_avg) & (il < -0.03) & (ic > -0.005)).astype(float).where(v_avg.notna(), np.nan)")

    # ---- Block I (121-135): Vol structure at high ----
    add("vol_compression_then_5sigma_spike_at_high",
        "Bar t-21: log-vol z<-1; bar t: z>5; both near 252d max.",
        ("close","volume","high"),
        "vz = _rolling_zscore(_safe_log(volume.replace(0, np.nan)), YDAYS)\ncomp = vz.shift(MDAYS) < -1.0; spike = vz > 5.0\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "(comp & spike & (close >= 0.95 * rmax)).astype(float).where(vz.notna(), np.nan)")
    add("vol_max_252d_at_252h",
        "Volume=252d max AND high=252d max.",
        ("volume","high"),
        "rh = high.rolling(YDAYS, min_periods=QDAYS).max(); rv = volume.rolling(YDAYS, min_periods=QDAYS).max()",
        "((volume >= rv - 1) & (high >= rh - 1e-12)).astype(float).where(rh.notna() & rv.notna(), np.nan)")
    add("vol_top_quintile_3of5_at_high",
        "3 of last 5 bars vol in 252d top quintile AND near 252h.",
        ("volume","high"),
        "vp80 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.80); rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nhv = (volume > vp80).astype(float); rh = (high >= 0.98 * rmax)",
        "((hv.rolling(WDAYS, min_periods=3).sum() >= 3) & rh).astype(float).where(vp80.notna() & rmax.notna(), np.nan)")
    add("vol_alternation_high_low_5bars_at_high",
        "Vol alternation H-L-H-L-H pattern AND near 252h.",
        ("volume","high"),
        "v_avg = volume.rolling(MDAYS, min_periods=10).mean(); rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nhi = (volume > v_avg).astype(float)",
        "((hi.shift(4) > 0.5) & (hi.shift(3) < 0.5) & (hi.shift(2) > 0.5) & (hi.shift(1) < 0.5) & (hi > 0.5) & (high >= 0.95 * rmax)).astype(float).where(v_avg.notna(), np.nan)")
    add("vol_skew_above_2_at_252h",
        "21d skew of log-vol>2 AND at 252h.",
        ("volume","high"),
        "lv = _safe_log(volume.replace(0, np.nan)); sk = lv.rolling(MDAYS, min_periods=10).skew()\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "((sk > 2.0) & (high >= rmax - 1e-12)).astype(float).where(sk.notna(), np.nan)")
    add("vol_pareto_alpha_below_2_at_252h",
        "Hill alpha (top 10% vol over 252d)<2 AND at 252h.",
        ("volume","high"),
        "lv = _safe_log(volume.replace(0, np.nan))\ndef _hill(w):\n    v = w[~np.isnan(w)]\n    if v.size < 30: return np.nan\n    v = np.sort(v); k = max(int(0.10 * v.size), 5)\n    if k >= v.size: return np.nan\n    thr = v[v.size - k - 1]; tail = v[v.size - k:]\n    if thr <= 0: return np.nan\n    return float(1.0 / np.mean(np.log(tail / thr)))\nalpha = lv.rolling(YDAYS, min_periods=QDAYS).apply(_hill, raw=True)\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "((alpha < 2.0) & (high >= rmax - 1e-12)).astype(float).where(alpha.notna(), np.nan)")
    add("atr_3consecutive_top_decile_at_252h",
        "3 consecutive bars ATR-N in 252d top decile AND at 252h.",
        ("high","low","close"),
        "atr_n = _safe_div(_atr(high, low, close, MDAYS), close); p90 = atr_n.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max(); ha = (atr_n > p90).astype(float)",
        "((ha.shift(2) > 0.5) & (ha.shift(1) > 0.5) & (ha > 0.5) & (high >= 0.95 * rmax)).astype(float).where(p90.notna() & rmax.notna(), np.nan)")
    add("realized_skew_negative_atr_compression_at_252h",
        "63d realized skew<0 AND ATR-N bottom quartile AND at 252h.",
        ("high","low","close"),
        "r = _log_ret(close); sk = r.rolling(QDAYS, min_periods=MDAYS).skew()\natr_n = _safe_div(_atr(high, low, close, MDAYS), close); q25 = atr_n.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "((sk < 0) & (atr_n < q25) & (high >= rmax - 1e-12)).astype(float).where(sk.notna() & q25.notna(), np.nan)")
    add("realized_kurt_above_5_at_252h",
        "63d excess-kurt>5 AND at 252h (heavy-tail at top).",
        ("close","high"),
        "r = _log_ret(close); kt = r.rolling(QDAYS, min_periods=MDAYS).kurt()\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "((kt > 5.0) & (high >= rmax - 1e-12)).astype(float).where(kt.notna(), np.nan)")
    add("var95_exceeded_at_252h_within_5d",
        "Single-bar loss>252d-VaR95 AND high made 252h within 5 bars.",
        ("close","high"),
        "r = _log_ret(close); v95 = -_rolling_q(r, YDAYS, 0.05)\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max(); rh = (high >= rmax - 1e-12).rolling(WDAYS, min_periods=1).max()",
        "((-r > v95) & (rh > 0.5)).astype(float).where(v95.notna(), np.nan)")
    add("vol_persistence_high_at_252h",
        "AR1 of |r| 252d>0.4 AND at 252h (sticky clustering at top).",
        ("close","high"),
        "absr = _log_ret(close).abs()\ndef _ac(w):\n    x = w[~np.isnan(w)]\n    if x.size < 20: return np.nan\n    a = x[:-1]; b = x[1:]\n    if a.std() == 0 or b.std() == 0: return np.nan\n    return float(np.corrcoef(a, b)[0, 1])\nar1 = absr.rolling(YDAYS, min_periods=QDAYS).apply(_ac, raw=True)\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "((ar1 > 0.4) & (high >= rmax - 1e-12)).astype(float).where(ar1.notna(), np.nan)")
    add("vol_clustering_count_2sigma_3_in_21d_at_252h",
        "Count of bars in 21d with |r|>2sigma>=3 AND at 252h.",
        ("close","high"),
        "r = _log_ret(close); sd = r.rolling(YDAYS, min_periods=QDAYS).std()\nsh = (r.abs() > 2.0 * sd).astype(float); rmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "((sh.rolling(MDAYS, min_periods=10).sum() >= 3) & (high >= rmax - 1e-12)).astype(float).where(sh.notna(), np.nan)")
    add("realized_vol_at_252max_at_close_252max",
        "21d realized vol=252d max AND close=252d max.",
        ("close","high"),
        "r = _log_ret(close); rv = (r ** 2).rolling(MDAYS, min_periods=10).mean()\nrm = rv.rolling(YDAYS, min_periods=QDAYS).max(); rmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "((rv >= rm - 1e-12) & (close >= rmax - 1e-12)).astype(float).where(rm.notna() & rmax.notna(), np.nan)")
    add("overnight_gap_z_above_3_at_252h",
        "Overnight gap z>3 AND at 252h.",
        ("open","close","high"),
        "on = _safe_log(open) - _safe_log(close.shift(1)); z = _rolling_zscore(on, YDAYS); rmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "((z > 3.0) & (high >= rmax - 1e-12)).astype(float).where(z.notna(), np.nan)")
    add("intraday_swing_above_5pct_at_252h",
        "(High-low)/open>5% AND high=252d max.",
        ("open","high","low"),
        "sw = (high - low) / open.replace(0, np.nan); rmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "((sw > 0.05) & (high >= rmax - 1e-12)).astype(float).where(sw.notna(), np.nan)")

    # ---- Block J (136-150): Cumulative event-count features ----
    add("count_3way_warnings_in_252d",
        "Count of 252d bars with RSI>70 AND close=252d max AND vol>avg.",
        ("close","volume","high"),
        "rsi = _rsi(close, 14); rmax = close.rolling(YDAYS, min_periods=QDAYS).max(); v_avg = volume.rolling(MDAYS, min_periods=10).mean()\nind = ((rsi > 70.0) & (close >= rmax - 1e-12) & (volume > v_avg)).astype(float)",
        "ind.rolling(YDAYS, min_periods=QDAYS).sum()")
    add("count_distribution_days_in_252d",
        "Count of distribution days (vol>avg AND close<open AND close bottom 50%) in 252d.",
        ("open","high","low","close","volume"),
        "v_avg = volume.rolling(MDAYS, min_periods=10).mean(); pos = (close - low) / (high - low).replace(0, np.nan)\nind = ((volume > v_avg) & (close < open) & (pos < 0.5)).astype(float)",
        "ind.rolling(YDAYS, min_periods=QDAYS).sum()")
    add("count_topping_candles_in_252d",
        "Count of (shoot-star OR dark-cloud OR bear-engulf) at 252d max.",
        ("open","high","low","close"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); rng = (high - low).replace(0, np.nan); body = (close - open).abs() / rng\nuw = (high - pd.concat([open, close], axis=1).max(axis=1)) / rng\nshoot = (close < open) & (body < 0.30) & (uw > 0.60)\negf = (close < open) & (close.shift(1) > open.shift(1)) & (open >= close.shift(1)) & (close <= open.shift(1))\ndc = (close.shift(1) > open.shift(1)) & (open > close.shift(1)) & (close < (open.shift(1) + close.shift(1)) / 2.0)\ntop = ((shoot | egf | dc) & (high >= rmax - 1e-12)).astype(float)",
        "top.rolling(YDAYS, min_periods=QDAYS).sum()")
    add("count_bullish_no_demand_in_252d",
        "Count of 252d bars with up-close AND vol<0.7avg AND new 21d high.",
        ("close","volume","high"),
        "v_avg = volume.rolling(MDAYS, min_periods=10).mean(); h21 = high.rolling(MDAYS, min_periods=10).max()\nind = ((close > close.shift(1)) & (volume < 0.7 * v_avg) & (high >= h21 - 1e-12)).astype(float)",
        "ind.rolling(YDAYS, min_periods=QDAYS).sum()")
    add("count_bearish_high_vol_at_252max_in_252d",
        "Count of bars with close<open AND vol>2x avg AND at 252d max in 252d.",
        ("open","close","volume","high"),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); v_avg = volume.rolling(MDAYS, min_periods=10).mean()\nind = ((close < open) & (volume > 2.0 * v_avg) & (high >= rmax - 1e-12)).astype(float)",
        "ind.rolling(YDAYS, min_periods=QDAYS).sum()")
    add("composite_topping_event_z_score_252d",
        "z(1d-event count across 5 topping conditions) over 252d.",
        ("open","high","low","close","volume"),
        "rsi = _rsi(close, 14); rmax = close.rolling(YDAYS, min_periods=QDAYS).max(); v_avg = volume.rolling(MDAYS, min_periods=10).mean()\npos = (close - low) / (high - low).replace(0, np.nan)\natr_n = _safe_div(_atr(high, low, close, MDAYS), close); zatr = _rolling_zscore(atr_n, YDAYS)\ncnt = ((rsi > 70.0).astype(float) + (close >= rmax - 1e-12).astype(float) + (volume > v_avg).astype(float) + (pos < 0.5).astype(float) + (zatr > 1.0).astype(float))",
        "_rolling_zscore(cnt, YDAYS)")
    add("days_since_5_topping_conditions",
        "Bars since last bar with all 5 topping conditions (capped 252).",
        ("high","low","close"),
        "rsi = _rsi(close, 14); macd = _macd(close); sig = macd.ewm(span=9, adjust=False, min_periods=3).mean()\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max(); atr_n = _safe_div(_atr(high, low, close, MDAYS), close); zatr = _rolling_zscore(atr_n, YDAYS)\npos = (close - low) / (high - low).replace(0, np.nan)\nev = ((rsi > 70.0) & (macd < sig) & (close >= rmax - 1e-12) & (zatr > 1.0) & (pos < 0.5)).astype(float)",
        "_bars_since_last_event(ev).clip(upper=float(YDAYS))")
    add("blowoff_signature_cluster_density_63d",
        "Fraction of 63d with (close top decile AND vol z>1 AND RSI>70).",
        ("high","low","close","volume"),
        "rmax = close.rolling(YDAYS, min_periods=QDAYS).max(); rmin = close.rolling(YDAYS, min_periods=QDAYS).min()\npr = _safe_div(close - rmin, rmax - rmin)\nvz = _rolling_zscore(_safe_log(volume.replace(0, np.nan)), YDAYS); rsi = _rsi(close, 14)\nind = ((pr > 0.9) & (vz > 1.0) & (rsi > 70.0)).astype(float).where(pr.notna() & vz.notna() & rsi.notna(), np.nan)",
        "ind.rolling(QDAYS, min_periods=MDAYS).mean()")
    add("count_failed_breakouts_at_252h_in_252d",
        "Bar t-3 made 252h; bars t-2,t-1,t all made lower highs - PIT-lagged.",
        ("high",),
        "rmax = high.rolling(YDAYS, min_periods=QDAYS).max()\nah = (high.shift(3) >= rmax.shift(3) - 1e-12).astype(int)\nfail = ah & (high.shift(2) < high.shift(3)) & (high.shift(1) < high.shift(3)) & (high < high.shift(3))",
        "fail.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()")
    add("count_swing_failures_252d",
        "Count of swing-failure patterns (PIT-lagged) in 252d.",
        ("high",),
        "h21 = high.rolling(MDAYS, min_periods=10).max()\nmh = (high.shift(WDAYS) >= h21.shift(WDAYS) - 1e-12).astype(int)\nfail = mh & (high.rolling(WDAYS, min_periods=1).max() < high.shift(WDAYS))",
        "fail.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()")
    add("triple_top_3_peaks_within_63d_at_similar",
        "3 distinct pivot-highs within 63d at levels within 1% of each other.",
        ("high",),
        "p_ph = high.shift(MDAYS // 2).where(high.shift(MDAYS // 2) == high.rolling(MDAYS, min_periods=10).max(), np.nan)\np_arr = p_ph.values; nb = len(p_arr); out = np.full(nb, np.nan, dtype=float); history = []\nfor t in range(nb):\n    if not np.isnan(p_arr[t]):\n        history.append((t, p_arr[t]))\n        recent = [h for h in history if (t - h[0]) <= QDAYS]\n        if len(recent) >= 3:\n            vals = [h[1] for h in recent[-3:]]\n            out[t] = 1.0 if max(vals) - min(vals) < 0.01 * max(vals) else 0.0\n        else:\n            out[t] = 0.0\n    elif t > 0 and not np.isnan(out[t - 1]):\n        out[t] = 0.0\nres = pd.Series(out, index=high.index)",
        "res")
    add("rounding_top_signature_252d",
        "d2(SMA252)<0 AND d1(SMA252)<0 AND price near 252d max.",
        ("close",),
        "sma = _sma(close, 252); d1 = sma.diff(); d2 = sma.diff().diff()",
        "((d2 < 0) & (d1 < 0) & (close >= 0.95 * close.rolling(YDAYS, min_periods=QDAYS).max())).astype(float).where(d2.notna(), np.nan)")
    add("descending_triangle_indicator",
        "Lower highs 21d AND flat low (range<1%) AND close near flat low.",
        ("close","high","low"),
        "lh = (high < high.shift(WDAYS)) & (high.shift(WDAYS) < high.shift(2 * WDAYS))\nlr = low.rolling(MDAYS, min_periods=10).max() - low.rolling(MDAYS, min_periods=10).min()\nfl = lr / close.replace(0, np.nan) < 0.01\nnl = close < low.rolling(MDAYS, min_periods=10).min() * 1.02",
        "(lh & fl & nl).astype(float).where(fl.notna(), np.nan)")
    add("head_shoulders_proxy_3peak",
        "3 peaks in 63d: middle highest, left/right within 5%.",
        ("high",),
        "p_ph = high.shift(MDAYS // 2).where(high.shift(MDAYS // 2) == high.rolling(MDAYS, min_periods=10).max(), np.nan)\np_arr = p_ph.values; nb = len(p_arr); out = np.full(nb, np.nan, dtype=float); history = []\nfor t in range(nb):\n    if not np.isnan(p_arr[t]):\n        history.append((t, p_arr[t]))\n        recent = [h for h in history if (t - h[0]) <= QDAYS]\n        if len(recent) >= 3:\n            l, hp, r = recent[-3][1], recent[-2][1], recent[-1][1]\n            out[t] = 1.0 if (hp > l and hp > r and abs(l - r) / max(l, r, 1e-9) < 0.05) else 0.0\n        else:\n            out[t] = 0.0\n    elif t > 0 and not np.isnan(out[t - 1]):\n        out[t] = 0.0\nres = pd.Series(out, index=high.index)",
        "res")
    add("master_topping_composite_score_252d",
        "z-sum of: distribution-day-count + non-conf count + bearish-candle count + vol-div days + parabolic-accel days over 252d.",
        ("open","high","low","close","volume"),
        "v_avg = volume.rolling(MDAYS, min_periods=10).mean(); pos = (close - low) / (high - low).replace(0, np.nan)\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()\ndd = ((volume > v_avg) & (close < open) & (pos < 0.5)).astype(float)\nobv = _obv(close, volume); om = obv.rolling(YDAYS, min_periods=QDAYS).max()\nnc = ((close >= rmax - 1e-12) & (obv < om - 1e-9)).astype(float)\nrng = (high - low).replace(0, np.nan); body = (close - open).abs() / rng\nuw = (high - pd.concat([open, close], axis=1).max(axis=1)) / rng\nss = ((close < open) & (body < 0.30) & (uw > 0.60) & (high >= rmax - 1e-12)).astype(float)\nvd = ((close > close.shift(1)) & (volume < volume.shift(1)) & (high >= rmax - 1e-12)).astype(float)\nr = _log_ret(close); pa = (r > 0.015).astype(float)\ntot = (dd.rolling(YDAYS, min_periods=QDAYS).sum() + nc.rolling(YDAYS, min_periods=QDAYS).sum() + ss.rolling(YDAYS, min_periods=QDAYS).sum() + vd.rolling(YDAYS, min_periods=QDAYS).sum() + pa.rolling(YDAYS, min_periods=QDAYS).sum())",
        "_rolling_zscore(tot, YDAYS)")
    return F


def f57_features():
    F = _f57()
    return _f57_part2(F)


# =========================================================================
# FAMILY 58 - change_point_regime_transition (cprt)
# CUSUM, Page-Hinkley, Bayesian-online change-point, energy-distance, PELT
# =========================================================================

F58_META = {"num": "58", "abbr": "cprt",
            "folder": "58_change_point_regime_transition",
            "name": "change_point_regime_transition",
            "name_upper": "CHANGE_POINT_REGIME_TRANSITION"}

CPRT_HELPERS = '''
def _cusum_pos(s, n, k=0.0):
    """Positive CUSUM: max running sum of (x - mean - k) over n. Reset at zero."""
    mp = max(n // 3, 20)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 20: return np.nan
        mu = v.mean()
        cs = 0.0; mx = 0.0
        for x in v:
            cs = max(0.0, cs + (x - mu - k))
            if cs > mx: mx = cs
        return float(mx)
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _cusum_neg(s, n, k=0.0):
    """Negative CUSUM: max accumulated decrease."""
    mp = max(n // 3, 20)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 20: return np.nan
        mu = v.mean()
        cs = 0.0; mx = 0.0
        for x in v:
            cs = max(0.0, cs - (x - mu + k))
            if cs > mx: mx = cs
        return float(mx)
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _page_hinkley(s, n, delta=0.0):
    """Page-Hinkley test stat: max(U_t - min(U_t)). Detects upward mean shifts."""
    mp = max(n // 3, 20)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 20: return np.nan
        mu = v.mean()
        u = np.cumsum(v - mu - delta)
        return float((u - np.minimum.accumulate(u)).max())
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _page_hinkley_neg(s, n, delta=0.0):
    mp = max(n // 3, 20)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 20: return np.nan
        mu = v.mean()
        u = np.cumsum(-(v - mu) - delta)
        return float((u - np.minimum.accumulate(u)).max())
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _cusum_variance(s, n):
    """CUSUM on (x - mean)^2 deviations (variance shift detection)."""
    mp = max(n // 3, 20)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 20: return np.nan
        v2 = (v - v.mean()) ** 2; mu = v2.mean()
        cs = 0.0; mx = 0.0
        for x in v2:
            cs = max(0.0, cs + (x - mu))
            if cs > mx: mx = cs
        return float(mx)
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _cumulative_t_stat_max(s, n):
    """Max t-statistic for split point in n-window (Bai-Perron-like for univariate mean)."""
    mp = max(n // 3, 30)
    def _f(w):
        v = w[~np.isnan(w)]
        nv = v.size
        if nv < 30: return np.nan
        best = 0.0
        for k in range(10, nv - 10):
            m1 = v[:k].mean(); m2 = v[k:].mean()
            s1 = v[:k].std(ddof=1); s2 = v[k:].std(ddof=1)
            se = np.sqrt(s1 ** 2 / k + s2 ** 2 / (nv - k))
            if se > 0:
                t = abs(m1 - m2) / se
                if t > best: best = t
        return float(best)
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _energy_distance(s, n):
    """E-statistic for testing equality of distribution between first/second half."""
    mp = max(n // 3, 30)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30: return np.nan
        half = v.size // 2
        a = v[:half]; b = v[half:]
        # E = 2*mean(|a-b|) - mean(|a-a|) - mean(|b-b|)
        if a.size > 40: a = a[::2]
        if b.size > 40: b = b[::2]
        d_ab = np.abs(a[:, None] - b[None, :]).mean()
        d_aa = np.abs(a[:, None] - a[None, :]).mean()
        d_bb = np.abs(b[:, None] - b[None, :]).mean()
        return float(2.0 * d_ab - d_aa - d_bb)
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _bayesian_cp_run_length_mean(s, n, hazard=0.01):
    """Bayesian online change-point: expected run length under conjugate-prior model.

    Approximation: maintain run-length distribution over the last n bars,
    return its mean. Drops sharply when a change is detected.
    """
    mp = max(n // 3, 30)
    def _f(w):
        v = w[~np.isnan(w)]
        nv = v.size
        if nv < 30: return np.nan
        # run-length probabilities
        p = np.array([1.0])  # P(r=0) at start
        mu_prior = 0.0; kappa_prior = 1.0; alpha_prior = 1.0; beta_prior = 1.0
        sums = np.array([0.0]); ssqs = np.array([0.0]); counts = np.array([0.0])
        means = []
        for x in v:
            counts_new = counts + 1
            sums_new = sums + x
            ssqs_new = ssqs + x * x
            mu_post = (kappa_prior * mu_prior + sums_new) / (kappa_prior + counts_new)
            # predictive log-prob (simplified): Gaussian with var depending on counts
            var_post = (beta_prior + 0.5 * (ssqs_new - sums_new ** 2 / np.maximum(counts_new, 1))) / np.maximum(alpha_prior + counts_new / 2, 0.5)
            var_post = np.maximum(var_post, 1e-8)
            # likelihood under each hypothesis
            lik = np.exp(-0.5 * (x - mu_post) ** 2 / var_post) / np.sqrt(2.0 * np.pi * var_post)
            # update run-length: grow + change-point
            grow = p * lik * (1.0 - hazard)
            cp = (p * lik * hazard).sum()
            p = np.concatenate(([cp], grow))
            # update sufficient stats (shift)
            sums = np.concatenate(([0.0], sums + x))
            ssqs = np.concatenate(([0.0], ssqs + x * x))
            counts = np.concatenate(([0.0], counts + 1))
            # normalize
            ps = p.sum()
            if ps > 0: p = p / ps
            # cap memory
            if p.size > 100:
                p = p[-100:]; sums = sums[-100:]; ssqs = ssqs[-100:]; counts = counts[-100:]
            rls = np.arange(p.size, dtype=float)
            means.append(float((rls * p).sum()))
        return means[-1] if means else np.nan
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _variance_ratio_change(s, n_short, n_long):
    """Short-window variance / long-window variance - sharp jump indicates change."""
    mp_s = max(n_short // 3, 10); mp_l = max(n_long // 3, 30)
    sv = s.rolling(n_short, min_periods=mp_s).var()
    lv = s.rolling(n_long, min_periods=mp_l).var()
    return _safe_div(sv, lv)


def _mean_shift_z(s, n_short, n_long):
    """(Short-window mean - long-window mean) / long-window std."""
    mp_s = max(n_short // 3, 10); mp_l = max(n_long // 3, 30)
    sm = s.rolling(n_short, min_periods=mp_s).mean()
    lm = s.rolling(n_long, min_periods=mp_l).mean()
    ls = s.rolling(n_long, min_periods=mp_l).std()
    return _safe_div(sm - lm, ls)
'''


def _f58():
    F, add = _S()
    # ---- Block A (1-15): CUSUM on returns ----
    for h_n, h_w in [("21d", "MDAYS"), ("63d", "QDAYS"), ("252d", "YDAYS")]:
        add(f"cusum_pos_log_ret_{h_n}",
            f"Positive CUSUM of log-returns over {h_n}.",
            ("close",), "r = _log_ret(close)", f"_cusum_pos(r, {h_w})")
        add(f"cusum_neg_log_ret_{h_n}",
            f"Negative CUSUM (downward shift) of log-returns over {h_n}.",
            ("close",), "r = _log_ret(close)", f"_cusum_neg(r, {h_w})")
        add(f"cusum_diff_pos_neg_log_ret_{h_n}",
            f"Pos minus Neg CUSUM over {h_n}.",
            ("close",), "r = _log_ret(close)\nu = _cusum_pos(r, " + h_w + "); d = _cusum_neg(r, " + h_w + ")",
            "u - d")
    for h_n, h_w in [("63d", "QDAYS"), ("252d", "YDAYS")]:
        add(f"cusum_pos_abs_ret_{h_n}",
            f"Pos CUSUM of |r| over {h_n} - vol increase detection.",
            ("close",), "x = _log_ret(close).abs()", f"_cusum_pos(x, {h_w})")
        add(f"cusum_variance_log_ret_{h_n}",
            f"CUSUM on (r - mean)^2 over {h_n} - variance shift.",
            ("close",), "r = _log_ret(close)", f"_cusum_variance(r, {h_w})")
    add("cusum_log_close_252d", "Pos CUSUM of log-close over 252d.",
        ("close",), "lc = _safe_log(close)", "_cusum_pos(lc, YDAYS)")
    add("cusum_log_close_504d", "Pos CUSUM of log-close over 504d.",
        ("close",), "lc = _safe_log(close)", "_cusum_pos(lc, DDAYS_2Y)")

    # ---- Block B (16-30): Page-Hinkley tests ----
    for h_n, h_w in [("63d", "QDAYS"), ("252d", "YDAYS")]:
        add(f"page_hinkley_pos_log_ret_{h_n}",
            f"Page-Hinkley upward-shift stat on log-returns over {h_n}.",
            ("close",), "r = _log_ret(close)", f"_page_hinkley(r, {h_w})")
        add(f"page_hinkley_neg_log_ret_{h_n}",
            f"Page-Hinkley downward-shift stat over {h_n}.",
            ("close",), "r = _log_ret(close)", f"_page_hinkley_neg(r, {h_w})")
        add(f"page_hinkley_pos_abs_ret_{h_n}",
            f"Page-Hinkley on |r| over {h_n} - vol upshift.",
            ("close",), "x = _log_ret(close).abs()", f"_page_hinkley(x, {h_w})")
    add("page_hinkley_log_close_252d", "Page-Hinkley on log-close over 252d.",
        ("close",), "lc = _safe_log(close)", "_page_hinkley(lc, YDAYS)")
    add("page_hinkley_log_close_504d", "Page-Hinkley on log-close over 504d.",
        ("close",), "lc = _safe_log(close)", "_page_hinkley(lc, DDAYS_2Y)")
    add("page_hinkley_delta_001_log_ret_252d",
        "Page-Hinkley with delta=0.001 (more sensitive) over 252d.",
        ("close",), "r = _log_ret(close)", "_page_hinkley(r, YDAYS, 0.001)")
    add("page_hinkley_delta_005_log_ret_252d",
        "Page-Hinkley with delta=0.005 (less sensitive) over 252d.",
        ("close",), "r = _log_ret(close)", "_page_hinkley(r, YDAYS, 0.005)")
    add("page_hinkley_neg_log_close_252d",
        "Page-Hinkley downward on log-close over 252d.",
        ("close",), "lc = _safe_log(close)", "_page_hinkley_neg(lc, YDAYS)")
    add("page_hinkley_neg_log_close_504d",
        "Page-Hinkley downward on log-close over 504d.",
        ("close",), "lc = _safe_log(close)", "_page_hinkley_neg(lc, DDAYS_2Y)")
    add("page_hinkley_diff_pos_neg_log_ret_252d",
        "PH-pos minus PH-neg on log-returns over 252d.",
        ("close",), "r = _log_ret(close)\nu = _page_hinkley(r, YDAYS); d = _page_hinkley_neg(r, YDAYS)",
        "u - d")

    # ---- Block C (31-45): Bai-Perron-like maximum t-stat for split point ----
    add("max_split_t_stat_log_ret_63d",
        "Max t-stat for any split point in 63d window (Bai-Perron-like).",
        ("close",), "r = _log_ret(close)", "_cumulative_t_stat_max(r, QDAYS)")
    add("max_split_t_stat_log_ret_252d", "Max split t-stat over 252d.",
        ("close",), "r = _log_ret(close)", "_cumulative_t_stat_max(r, YDAYS)")
    add("max_split_t_stat_log_ret_504d", "Max split t-stat over 504d.",
        ("close",), "r = _log_ret(close)", "_cumulative_t_stat_max(r, DDAYS_2Y)")
    add("max_split_t_stat_abs_ret_252d", "Max split t-stat on |r| over 252d.",
        ("close",), "x = _log_ret(close).abs()", "_cumulative_t_stat_max(x, YDAYS)")
    add("max_split_t_stat_log_close_252d", "Max split t-stat on log-close over 252d.",
        ("close",), "lc = _safe_log(close)", "_cumulative_t_stat_max(lc, YDAYS)")
    add("max_split_t_stat_log_close_504d", "Max split t-stat on log-close over 504d.",
        ("close",), "lc = _safe_log(close)", "_cumulative_t_stat_max(lc, DDAYS_2Y)")
    add("max_split_t_stat_log_volume_252d", "Max split t-stat on log-volume over 252d.",
        ("volume",), "lv = _safe_log(volume.replace(0, np.nan))", "_cumulative_t_stat_max(lv, YDAYS)")
    add("max_split_t_stat_high_low_range_252d", "Max split t-stat on (high-low)/close over 252d.",
        ("high", "low", "close"), "rng = _safe_div(high - low, close)", "_cumulative_t_stat_max(rng, YDAYS)")
    add("max_split_t_stat_overnight_ret_252d",
        "Max split t-stat on overnight returns over 252d.",
        ("open", "close"), "on = _safe_log(open) - _safe_log(close.shift(1))", "_cumulative_t_stat_max(on, YDAYS)")
    add("max_split_t_stat_dollar_vol_252d",
        "Max split t-stat on log dollar-volume over 252d.",
        ("close", "volume"), "ldv = _safe_log((close * volume).replace(0, np.nan))",
        "_cumulative_t_stat_max(ldv, YDAYS)")
    add("max_split_t_stat_intraday_ret_252d",
        "Max split t-stat on intraday returns over 252d.",
        ("open", "close"), "i = _safe_log(close) - _safe_log(open)", "_cumulative_t_stat_max(i, YDAYS)")
    add("max_split_t_stat_squared_ret_252d",
        "Max split t-stat on r^2 over 252d - variance change.",
        ("close",), "x = _log_ret(close) ** 2", "_cumulative_t_stat_max(x, YDAYS)")
    add("split_t_zscore_log_ret_252d_252d",
        "z-score over 252d of (max split t-stat 252d).",
        ("close",), "r = _log_ret(close)\nt = _cumulative_t_stat_max(r, YDAYS)",
        "_rolling_zscore(t, YDAYS)")
    add("split_t_top_decile_indicator_252d",
        "Indicator: max split t-stat over 252d > 252d-q90.",
        ("close",), "r = _log_ret(close)\nt = _cumulative_t_stat_max(r, YDAYS)\np90 = t.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)",
        "(t > p90).astype(float).where(p90.notna(), np.nan)")
    add("split_t_above_threshold_at_252h_indicator",
        "Max split t-stat > 3.0 (significant) AND close = 252d max.",
        ("close",), "r = _log_ret(close)\nt = _cumulative_t_stat_max(r, YDAYS)\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()",
        "((t > 3.0) & (close >= rmax - 1e-12)).astype(float).where(t.notna(), np.nan)")

    # ---- Block D (46-60): Energy distance (distribution change) ----
    add("energy_distance_log_ret_63d",
        "E-stat (energy distance) between first/second half of 63d log-returns.",
        ("close",), "r = _log_ret(close)", "_energy_distance(r, QDAYS)")
    add("energy_distance_log_ret_252d", "E-stat over 252d.",
        ("close",), "r = _log_ret(close)", "_energy_distance(r, YDAYS)")
    add("energy_distance_log_ret_504d", "E-stat over 504d.",
        ("close",), "r = _log_ret(close)", "_energy_distance(r, DDAYS_2Y)")
    add("energy_distance_abs_log_ret_252d", "E-stat on |r| over 252d - vol distribution change.",
        ("close",), "x = _log_ret(close).abs()", "_energy_distance(x, YDAYS)")
    add("energy_distance_log_volume_252d", "E-stat on log-volume over 252d.",
        ("volume",), "lv = _safe_log(volume.replace(0, np.nan))", "_energy_distance(lv, YDAYS)")
    add("energy_distance_atr_norm_252d", "E-stat on ATR/close over 252d.",
        ("high","low","close"), "an = _safe_div(_atr(high, low, close, MDAYS), close)", "_energy_distance(an, YDAYS)")
    add("energy_distance_overnight_ret_252d", "E-stat on overnight returns over 252d.",
        ("open","close"), "on = _safe_log(open) - _safe_log(close.shift(1))", "_energy_distance(on, YDAYS)")
    add("energy_distance_close_pos_in_range_252d", "E-stat on intraday close-position over 252d.",
        ("high","low","close"), "p = (close - low) / (high - low).replace(0, np.nan)", "_energy_distance(p, YDAYS)")
    add("energy_distance_log_close_504d", "E-stat on log-close over 504d.",
        ("close",), "lc = _safe_log(close)", "_energy_distance(lc, DDAYS_2Y)")
    add("energy_distance_squared_log_ret_252d",
        "E-stat on r^2 over 252d.",
        ("close",), "x = _log_ret(close) ** 2", "_energy_distance(x, YDAYS)")
    add("energy_distance_zscore_252d",
        "z-score over 252d of 63d-energy-distance.",
        ("close",), "r = _log_ret(close)\ne = _energy_distance(r, QDAYS)",
        "_rolling_zscore(e, YDAYS)")
    add("energy_distance_above_p90_indicator_252d",
        "Indicator: E-stat 63d above 252d-p90.",
        ("close",), "r = _log_ret(close)\ne = _energy_distance(r, QDAYS)\np90 = e.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)",
        "(e > p90).astype(float).where(p90.notna(), np.nan)")
    add("energy_distance_at_252h_indicator",
        "E-stat in top quartile AND close = 252d max.",
        ("close",), "r = _log_ret(close)\ne = _energy_distance(r, QDAYS)\np75 = e.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()",
        "((e > p75) & (close >= rmax - 1e-12)).astype(float).where(p75.notna(), np.nan)")
    add("energy_distance_acceleration_21d",
        "21-bar change in 63d-energy-distance.",
        ("close",), "r = _log_ret(close)\ne = _energy_distance(r, QDAYS)",
        "e - e.shift(MDAYS)")
    add("energy_distance_change_z_252d",
        "z-score of (current - prior 21-bar) E-stat over 252d.",
        ("close",), "r = _log_ret(close)\ne = _energy_distance(r, QDAYS)\nch = e - e.shift(MDAYS)",
        "_rolling_zscore(ch, YDAYS)")

    # ---- Block E (61-75): Bayesian online change-point ----
    add("bcp_run_length_mean_log_ret_252d",
        "Bayesian online change-point: expected run-length over 252d log-returns.",
        ("close",), "r = _log_ret(close)", "_bayesian_cp_run_length_mean(r, YDAYS, 0.01)")
    add("bcp_run_length_mean_log_ret_504d",
        "BOCP expected run-length over 504d.",
        ("close",), "r = _log_ret(close)", "_bayesian_cp_run_length_mean(r, DDAYS_2Y, 0.01)")
    add("bcp_run_length_mean_log_close_252d",
        "BOCP on log-close over 252d.",
        ("close",), "lc = _safe_log(close)", "_bayesian_cp_run_length_mean(lc, YDAYS, 0.01)")
    add("bcp_run_length_mean_abs_ret_252d",
        "BOCP on |r| over 252d.",
        ("close",), "x = _log_ret(close).abs()", "_bayesian_cp_run_length_mean(x, YDAYS, 0.01)")
    add("bcp_run_length_drop_pct_21d",
        "% drop in BOCP-run-length over 21d (sharp drop = change).",
        ("close",), "r = _log_ret(close)\nb = _bayesian_cp_run_length_mean(r, YDAYS, 0.01)",
        "_safe_div(b - b.shift(MDAYS), b.shift(MDAYS))")
    add("bcp_run_length_z_252d",
        "z-score of BOCP run-length over 252d.",
        ("close",), "r = _log_ret(close)\nb = _bayesian_cp_run_length_mean(r, YDAYS, 0.01)",
        "_rolling_zscore(b, YDAYS)")
    add("bcp_run_length_low_at_252h_indicator",
        "BOCP run-length < 252d-q25 AND close = 252d max (change detected at top).",
        ("close",), "r = _log_ret(close)\nb = _bayesian_cp_run_length_mean(r, YDAYS, 0.01)\nq25 = b.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()",
        "((b < q25) & (close >= rmax - 1e-12)).astype(float).where(q25.notna(), np.nan)")
    add("bcp_high_hazard_log_ret_252d",
        "BOCP with hazard=0.05 (more change-prone) on log-returns over 252d.",
        ("close",), "r = _log_ret(close)", "_bayesian_cp_run_length_mean(r, YDAYS, 0.05)")
    add("bcp_low_hazard_log_ret_252d",
        "BOCP with hazard=0.002 (less change-prone) on log-returns over 252d.",
        ("close",), "r = _log_ret(close)", "_bayesian_cp_run_length_mean(r, YDAYS, 0.002)")
    add("bcp_run_length_high_vs_low_hazard_diff_252d",
        "BOCP(hazard=0.002) - BOCP(hazard=0.05) - sensitivity to hazard prior.",
        ("close",), "r = _log_ret(close)\nl = _bayesian_cp_run_length_mean(r, YDAYS, 0.002)\nh = _bayesian_cp_run_length_mean(r, YDAYS, 0.05)",
        "l - h")
    add("bcp_run_length_change_speed_5d",
        "5-bar change in BOCP run-length over 252d window.",
        ("close",), "r = _log_ret(close)\nb = _bayesian_cp_run_length_mean(r, YDAYS, 0.01)",
        "b - b.shift(WDAYS)")
    add("bcp_run_length_low_persistence_63d",
        "Fraction of last 63d where BOCP run-length < 252d-q25.",
        ("close",), "r = _log_ret(close)\nb = _bayesian_cp_run_length_mean(r, YDAYS, 0.01)\nq25 = b.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)\nind = (b < q25).astype(float).where(q25.notna(), np.nan)",
        "ind.rolling(QDAYS, min_periods=MDAYS).mean()")
    add("bcp_minus_long_term_mean_run_length_252d",
        "BOCP run-length minus 504d-mean of BOCP - deviation from baseline.",
        ("close",), "r = _log_ret(close)\nb = _bayesian_cp_run_length_mean(r, YDAYS, 0.01)\nbm = b.rolling(DDAYS_2Y, min_periods=YDAYS).mean()",
        "b - bm")
    add("bcp_run_length_at_252d_min_indicator",
        "Indicator: BOCP run-length is at 252d minimum (fresh change detected).",
        ("close",), "r = _log_ret(close)\nb = _bayesian_cp_run_length_mean(r, YDAYS, 0.01)\nmn = b.rolling(YDAYS, min_periods=QDAYS).min()",
        "(b <= mn + 1e-9).astype(float).where(b.notna(), np.nan)")
    add("bcp_run_length_acceleration_d2_252d",
        "2nd-order diff of BOCP run-length over 252d.",
        ("close",), "r = _log_ret(close)\nb = _bayesian_cp_run_length_mean(r, YDAYS, 0.01)",
        "b.diff().diff()")

    return F


def _f58_part2(F):
    def add(name, doc, args, body, ret):
        F.append({"idx": len(F) + 1, "name": name, "doc": doc, "args": args, "body": body, "ret": ret})

    # ---- Block F (76-90): variance-ratio change indicators ----
    for s_n, s_w, l_n, l_w in [("21d","MDAYS","252d","YDAYS"), ("63d","QDAYS","252d","YDAYS"),
                                ("21d","MDAYS","504d","DDAYS_2Y"), ("63d","QDAYS","504d","DDAYS_2Y")]:
        add(f"variance_ratio_{s_n}_over_{l_n}_log_ret",
            f"Var({s_n}r) / Var({l_n}r) - sharp value increase = change.",
            ("close",), "r = _log_ret(close)", f"_variance_ratio_change(r, {s_w}, {l_w})")
    for s_n, s_w, l_n, l_w in [("21d","MDAYS","252d","YDAYS"), ("63d","QDAYS","252d","YDAYS")]:
        add(f"variance_ratio_{s_n}_over_{l_n}_abs_ret",
            f"Var-ratio of |r| - vol-regime change.",
            ("close",), "x = _log_ret(close).abs()", f"_variance_ratio_change(x, {s_w}, {l_w})")
    add("mean_shift_z_21d_over_252d_log_ret",
        "(21d-mean - 252d-mean)/252d-std - mean-shift z-score.",
        ("close",), "r = _log_ret(close)", "_mean_shift_z(r, MDAYS, YDAYS)")
    add("mean_shift_z_63d_over_252d_log_ret",
        "Mean shift z 63d vs 252d.",
        ("close",), "r = _log_ret(close)", "_mean_shift_z(r, QDAYS, YDAYS)")
    add("mean_shift_z_21d_over_504d_log_ret",
        "Mean shift z 21d vs 504d.",
        ("close",), "r = _log_ret(close)", "_mean_shift_z(r, MDAYS, DDAYS_2Y)")
    add("mean_shift_z_neg_21d_over_252d_log_ret",
        "Negative mean shift z (downward) 21d vs 252d.",
        ("close",), "r = _log_ret(close)", "-_mean_shift_z(r, MDAYS, YDAYS)")
    add("variance_ratio_acceleration_21d",
        "21-bar change in variance ratio 21d/252d.",
        ("close",), "r = _log_ret(close)\nvr = _variance_ratio_change(r, MDAYS, YDAYS)",
        "vr - vr.shift(MDAYS)")
    add("variance_ratio_above_3_indicator",
        "Indicator: variance ratio 21d/252d > 3 (vol regime change).",
        ("close",), "r = _log_ret(close)\nvr = _variance_ratio_change(r, MDAYS, YDAYS)",
        "(vr > 3.0).astype(float).where(vr.notna(), np.nan)")
    add("variance_ratio_at_252h_indicator",
        "Variance ratio 21d/252d > 252d-p90 AND close = 252d max.",
        ("close",), "r = _log_ret(close)\nvr = _variance_ratio_change(r, MDAYS, YDAYS)\np90 = vr.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()",
        "((vr > p90) & (close >= rmax - 1e-12)).astype(float).where(p90.notna(), np.nan)")

    # ---- Block G (91-105): regime indicators using rolling statistics ----
    add("mean_log_ret_sign_flip_recent_21d_vs_252d",
        "Sign(21d mean) != Sign(252d mean) - regime sign flip indicator.",
        ("close",), "r = _log_ret(close)\nm21 = r.rolling(MDAYS, min_periods=10).mean(); m252 = r.rolling(YDAYS, min_periods=QDAYS).mean()",
        "(np.sign(m21) != np.sign(m252)).astype(float).where(m21.notna() & m252.notna(), np.nan)")
    add("vol_regime_sign_flip_recent_21d_vs_252d",
        "Sign(21d - 252d realized vol) flips - vol regime shift.",
        ("close",), "r = _log_ret(close)\nrv21 = (r ** 2).rolling(MDAYS, min_periods=10).mean(); rv252 = (r ** 2).rolling(YDAYS, min_periods=QDAYS).mean()\ndiff = rv21 - rv252",
        "((diff > 0) != (diff.shift(1) > 0)).astype(float).where(diff.notna() & diff.shift(1).notna(), np.nan)")
    add("rsi_regime_below_50_break_after_above_70_indicator",
        "RSI drops below 50 within 21 bars after being above 70 - momentum regime break.",
        ("close",), "rsi = _rsi(close, 14)\nob = (rsi > 70.0).astype(float)\nob21 = ob.shift(WDAYS).rolling(MDAYS, min_periods=5).max()\nb50 = (rsi < 50.0).astype(float)",
        "((ob21 > 0.5) & (b50 > 0.5)).astype(float).where(rsi.notna(), np.nan)")
    add("trend_break_close_to_sma200_from_above_indicator",
        "Close crosses below SMA200 (price-trend regime break).",
        ("close",), "sma = _sma(close, 200)\ncd = (close < sma) & (close.shift(1) >= sma.shift(1))",
        "cd.astype(float).where(sma.notna(), np.nan)")
    add("trend_break_close_to_sma50_from_above_indicator",
        "Close crosses below SMA50 (medium trend break).",
        ("close",), "sma = _sma(close, 50)\ncd = (close < sma) & (close.shift(1) >= sma.shift(1))",
        "cd.astype(float).where(sma.notna(), np.nan)")
    add("trend_break_sma50_to_sma200_below_indicator",
        "SMA50 crosses below SMA200 (Death Cross - long-term trend regime break).",
        ("close",), "s50 = _sma(close, 50); s200 = _sma(close, 200)\ncd = (s50 < s200) & (s50.shift(1) >= s200.shift(1))",
        "cd.astype(float).where(s200.notna(), np.nan)")
    add("regime_break_count_in_252d",
        "Count of bars in 252d where (SMA50 cross SMA200 OR close cross SMA200).",
        ("close",), "s50 = _sma(close, 50); s200 = _sma(close, 200)\ndc = ((s50 < s200) & (s50.shift(1) >= s200.shift(1))).astype(float)\ncd = ((close < s200) & (close.shift(1) >= s200.shift(1))).astype(float)\ncomb = (dc.fillna(0) + cd.fillna(0)).clip(upper=1.0)",
        "comb.rolling(YDAYS, min_periods=QDAYS).sum()")
    add("regime_break_days_since_last_252d_capped",
        "Bars since last regime break (close cross SMA200) capped at 252.",
        ("close",), "sma = _sma(close, 200)\ncd = ((close < sma) & (close.shift(1) >= sma.shift(1))).astype(float)",
        "_bars_since_last_event(cd).clip(upper=float(YDAYS))")
    add("rolling_t_test_z_recent_vs_baseline_252d",
        "Welch-t-z for (21d mean) vs (252d-21d mean) over 252d.",
        ("close",), "r = _log_ret(close)\n"
        "def _wt(w):\n    v = w[~np.isnan(w)]\n    if v.size < 60: return np.nan\n    a = v[-MDAYS:]; b = v[:-MDAYS]\n    sa = a.std(ddof=1); sb = b.std(ddof=1)\n    se = np.sqrt(sa ** 2 / a.size + sb ** 2 / b.size)\n    if se <= 0: return np.nan\n    return float((a.mean() - b.mean()) / se)\nres = r.rolling(YDAYS, min_periods=QDAYS).apply(_wt, raw=True)",
        "res")
    add("rolling_f_test_recent_vs_baseline_var_252d",
        "F-stat (21d-var) / (252d-21d var) over 252d.",
        ("close",), "r = _log_ret(close)\n"
        "def _ft(w):\n    v = w[~np.isnan(w)]\n    if v.size < 60: return np.nan\n    a = v[-MDAYS:]; b = v[:-MDAYS]\n    sa = a.var(ddof=1); sb = b.var(ddof=1)\n    if sb <= 0: return np.nan\n    return float(sa / sb)\nres = r.rolling(YDAYS, min_periods=QDAYS).apply(_ft, raw=True)",
        "res")
    add("rolling_ks_recent_vs_baseline_dist_252d",
        "KS distance between (21d) and (252d-21d) distributions of log-returns.",
        ("close",), "r = _log_ret(close)\n"
        "def _ks(w):\n    v = w[~np.isnan(w)]\n    if v.size < 60: return np.nan\n    a = np.sort(v[-MDAYS:]); b = np.sort(v[:-MDAYS])\n    all_v = np.union1d(a, b)\n    ca = np.searchsorted(a, all_v, side='right') / a.size\n    cb = np.searchsorted(b, all_v, side='right') / b.size\n    return float(np.max(np.abs(ca - cb)))\nres = r.rolling(YDAYS, min_periods=QDAYS).apply(_ks, raw=True)",
        "res")
    add("rolling_mann_whitney_u_z_252d",
        "Mann-Whitney U z-stat for (21d) vs (252d-21d) over 252d.",
        ("close",), "r = _log_ret(close)\n"
        "def _mw(w):\n    v = w[~np.isnan(w)]\n    if v.size < 60: return np.nan\n    a = v[-MDAYS:]; b = v[:-MDAYS]\n    ranks = pd.Series(np.concatenate([a, b])).rank().values\n    R1 = ranks[:a.size].sum()\n    n1 = a.size; n2 = b.size\n    U = R1 - n1 * (n1 + 1) / 2.0\n    mu = n1 * n2 / 2.0; sd = np.sqrt(n1 * n2 * (n1 + n2 + 1) / 12.0)\n    if sd <= 0: return np.nan\n    return float((U - mu) / sd)\nres = r.rolling(YDAYS, min_periods=QDAYS).apply(_mw, raw=True)",
        "res")
    add("rolling_distribution_skew_change_recent_vs_baseline_252d",
        "Skew(21d) minus skew(252d-21d) over 252d.",
        ("close",), "r = _log_ret(close)\n"
        "def _sk(w):\n    v = w[~np.isnan(w)]\n    if v.size < 60: return np.nan\n    a = v[-MDAYS:]; b = v[:-MDAYS]\n    if a.std(ddof=1) == 0 or b.std(ddof=1) == 0: return np.nan\n    ska = ((a - a.mean()) ** 3).mean() / a.std(ddof=1) ** 3\n    skb = ((b - b.mean()) ** 3).mean() / b.std(ddof=1) ** 3\n    return float(ska - skb)\nres = r.rolling(YDAYS, min_periods=QDAYS).apply(_sk, raw=True)",
        "res")
    add("rolling_distribution_kurt_change_recent_vs_baseline_252d",
        "Excess-kurt(21d) minus excess-kurt(252d-21d) over 252d.",
        ("close",), "r = _log_ret(close)\n"
        "def _kt(w):\n    v = w[~np.isnan(w)]\n    if v.size < 60: return np.nan\n    a = v[-MDAYS:]; b = v[:-MDAYS]\n    if a.std(ddof=1) == 0 or b.std(ddof=1) == 0: return np.nan\n    ka = ((a - a.mean()) ** 4).mean() / a.std(ddof=1) ** 4 - 3\n    kb = ((b - b.mean()) ** 4).mean() / b.std(ddof=1) ** 4 - 3\n    return float(ka - kb)\nres = r.rolling(YDAYS, min_periods=QDAYS).apply(_kt, raw=True)",
        "res")

    # ---- Block H (106-120): structural breaks in price level / trend slope ----
    add("trend_slope_break_chow_proxy_252d",
        "Max F-stat (Chow-test proxy) testing slope-break in linear-regression of log-close vs time.",
        ("close",), "lc = _safe_log(close)\n"
        "def _ch(w):\n    v = w[~np.isnan(w)]\n    nv = v.size\n    if nv < 60: return np.nan\n    x = np.arange(nv, dtype=float)\n    best = 0.0\n    for k in range(20, nv - 20):\n        x1, y1 = x[:k], v[:k]; x2, y2 = x[k:], v[k:]\n        s1 = np.polyfit(x1, y1, 1)[0]; s2 = np.polyfit(x2, y2, 1)[0]\n        if abs(s1 - s2) > best: best = abs(s1 - s2)\n    return float(best)\nres = lc.rolling(YDAYS, min_periods=QDAYS).apply(_ch, raw=True)",
        "res")
    add("trend_slope_recent_vs_baseline_252d",
        "Slope(21d log-close) minus slope(252d-21d log-close).",
        ("close",), "lc = _safe_log(close)\n"
        "def _ds(w):\n    v = w[~np.isnan(w)]\n    if v.size < 60: return np.nan\n    x = np.arange(v.size, dtype=float)\n    s_rec = np.polyfit(x[-MDAYS:], v[-MDAYS:], 1)[0]\n    s_base = np.polyfit(x[:-MDAYS], v[:-MDAYS], 1)[0]\n    return float(s_rec - s_base)\nres = lc.rolling(YDAYS, min_periods=QDAYS).apply(_ds, raw=True)",
        "res")
    add("trend_slope_zscore_change_252d",
        "z-score of (21d slope - 252d-21d slope) over 252d.",
        ("close",), "lc = _safe_log(close)\n"
        "def _ds(w):\n    v = w[~np.isnan(w)]\n    if v.size < 60: return np.nan\n    x = np.arange(v.size, dtype=float)\n    s_rec = np.polyfit(x[-MDAYS:], v[-MDAYS:], 1)[0]\n    s_base = np.polyfit(x[:-MDAYS], v[:-MDAYS], 1)[0]\n    return float(s_rec - s_base)\nch = lc.rolling(YDAYS, min_periods=QDAYS).apply(_ds, raw=True)",
        "_rolling_zscore(ch, YDAYS)")
    add("trend_slope_sign_flip_recent_vs_baseline_indicator",
        "Sign(21d slope) != sign(252d-21d slope) - trend-direction regime flip.",
        ("close",), "lc = _safe_log(close)\n"
        "def _ds(w):\n    v = w[~np.isnan(w)]\n    if v.size < 60: return np.nan\n    x = np.arange(v.size, dtype=float)\n    s_rec = np.polyfit(x[-MDAYS:], v[-MDAYS:], 1)[0]\n    s_base = np.polyfit(x[:-MDAYS], v[:-MDAYS], 1)[0]\n    return 1.0 if (s_rec * s_base < 0) else 0.0\nres = lc.rolling(YDAYS, min_periods=QDAYS).apply(_ds, raw=True)",
        "res")
    add("trend_break_count_252d",
        "Count of bars in 252d where (trend-slope sign flip in 21d vs 252d-21d).",
        ("close",), "lc = _safe_log(close)\n"
        "def _ds(w):\n    v = w[~np.isnan(w)]\n    if v.size < 60: return np.nan\n    x = np.arange(v.size, dtype=float)\n    s_rec = np.polyfit(x[-MDAYS:], v[-MDAYS:], 1)[0]\n    s_base = np.polyfit(x[:-MDAYS], v[:-MDAYS], 1)[0]\n    return 1.0 if (s_rec * s_base < 0) else 0.0\nev = lc.rolling(YDAYS, min_periods=QDAYS).apply(_ds, raw=True)",
        "ev.rolling(YDAYS, min_periods=QDAYS).sum()")
    add("trend_curvature_change_indicator",
        "Sign change of 2nd derivative of SMA63 (concavity flip) - regime curvature change.",
        ("close",), "s = _sma(close, 63); d2 = s.diff().diff()\nsgn = np.sign(d2)",
        "((sgn != sgn.shift(1)) & (sgn != 0)).astype(float).where(d2.notna(), np.nan)")
    add("trend_curvature_change_count_252d",
        "Count of curvature flips of SMA63 in 252d.",
        ("close",), "s = _sma(close, 63); d2 = s.diff().diff()\nsgn = np.sign(d2)\nev = ((sgn != sgn.shift(1)) & (sgn != 0)).astype(float).where(d2.notna(), np.nan)",
        "ev.rolling(YDAYS, min_periods=QDAYS).sum()")
    add("structural_break_quandt_andrews_proxy_252d",
        "Sup-F (max F-stat) for breakpoint detection on log-close trend regression over 252d.",
        ("close",), "lc = _safe_log(close)\n"
        "def _qa(w):\n    v = w[~np.isnan(w)]\n    nv = v.size\n    if nv < 60: return np.nan\n    x = np.arange(nv, dtype=float)\n    rss_full = np.sum((v - (np.polyval(np.polyfit(x, v, 1), x))) ** 2)\n    best_f = 0.0\n    for k in range(20, nv - 20):\n        x1, y1 = x[:k], v[:k]; x2, y2 = x[k:], v[k:]\n        rss1 = np.sum((y1 - np.polyval(np.polyfit(x1, y1, 1), x1)) ** 2)\n        rss2 = np.sum((y2 - np.polyval(np.polyfit(x2, y2, 1), x2)) ** 2)\n        if rss1 + rss2 > 0:\n            f = ((rss_full - rss1 - rss2) / 2.0) / ((rss1 + rss2) / (nv - 4))\n            if f > best_f: best_f = f\n    return float(best_f)\nres = lc.rolling(YDAYS, min_periods=QDAYS).apply(_qa, raw=True)",
        "res")
    add("regime_shift_intensity_composite_252d",
        "Z-sum of: CUSUM-pos, PH-pos, max-split-t, E-stat over 252d.",
        ("close",), "r = _log_ret(close)\nu = _cusum_pos(r, YDAYS); ph = _page_hinkley(r, YDAYS); t = _cumulative_t_stat_max(r, YDAYS); e = _energy_distance(r, YDAYS)\nz = _rolling_zscore(u, YDAYS) + _rolling_zscore(ph, YDAYS) + _rolling_zscore(t, YDAYS) + _rolling_zscore(e, YDAYS)",
        "z")
    add("regime_shift_intensity_above_p90_at_252h_indicator",
        "Regime-shift intensity composite > 252d-p90 AND close = 252d max.",
        ("close",), "r = _log_ret(close)\nu = _cusum_pos(r, YDAYS); ph = _page_hinkley(r, YDAYS); t = _cumulative_t_stat_max(r, YDAYS); e = _energy_distance(r, YDAYS)\nz = (_rolling_zscore(u, YDAYS) + _rolling_zscore(ph, YDAYS) + _rolling_zscore(t, YDAYS) + _rolling_zscore(e, YDAYS))\np90 = z.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()",
        "((z > p90) & (close >= rmax - 1e-12)).astype(float).where(p90.notna(), np.nan)")

    # ---- Block I (121-135): change-points on multiple data streams ----
    add("cp_intensity_overnight_ret_252d",
        "Page-Hinkley on overnight log-returns over 252d.",
        ("open","close"), "on = _safe_log(open) - _safe_log(close.shift(1))", "_page_hinkley(on, YDAYS)")
    add("cp_intensity_intraday_ret_252d",
        "Page-Hinkley on intraday returns over 252d.",
        ("open","close"), "i = _safe_log(close) - _safe_log(open)", "_page_hinkley(i, YDAYS)")
    add("cp_intensity_log_volume_252d",
        "Page-Hinkley on log-volume over 252d (volume regime change).",
        ("volume",), "lv = _safe_log(volume.replace(0, np.nan))", "_page_hinkley(lv, YDAYS)")
    add("cp_intensity_log_dollar_volume_252d",
        "Page-Hinkley on log dollar-volume over 252d.",
        ("close","volume"), "ldv = _safe_log((close * volume).replace(0, np.nan))", "_page_hinkley(ldv, YDAYS)")
    add("cp_intensity_high_low_range_252d",
        "Page-Hinkley on (high-low)/close over 252d (range regime change).",
        ("high","low","close"), "rn = _safe_div(high - low, close)", "_page_hinkley(rn, YDAYS)")
    add("cp_intensity_close_pos_in_range_252d",
        "Page-Hinkley on intraday close-position over 252d.",
        ("high","low","close"), "p = (close - low) / (high - low).replace(0, np.nan)", "_page_hinkley(p, YDAYS)")
    add("cp_intensity_log_atr_norm_252d",
        "Page-Hinkley on log(ATR/close) over 252d.",
        ("high","low","close"), "an = _safe_log(_safe_div(_atr(high, low, close, MDAYS), close))", "_page_hinkley(an, YDAYS)")
    add("cp_intensity_rsi_14_252d",
        "Page-Hinkley on RSI14 over 252d.",
        ("close",), "rsi = _rsi(close, 14)", "_page_hinkley(rsi, YDAYS)")
    add("cp_intensity_macd_252d",
        "Page-Hinkley on MACD line over 252d.",
        ("close",), "m = _macd(close)", "_page_hinkley(m, YDAYS)")
    add("cp_intensity_obv_252d",
        "Page-Hinkley on OBV over 252d.",
        ("close","volume"), "o = _obv(close, volume)", "_page_hinkley(o, YDAYS)")
    add("cp_intensity_cross_stream_consensus_252d",
        "Sum of z(PH) across {ret, abs-ret, vol, range, RSI, MACD, OBV} - cross-stream change consensus.",
        ("high","low","close","volume"),
        "r = _log_ret(close); x = r.abs()\nlv = _safe_log(volume.replace(0, np.nan)); rn = _safe_div(high - low, close)\nrsi = _rsi(close, 14); m = _macd(close); o = _obv(close, volume)\nz1 = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS); z2 = _rolling_zscore(_page_hinkley(x, YDAYS), YDAYS)\nz3 = _rolling_zscore(_page_hinkley(lv, YDAYS), YDAYS); z4 = _rolling_zscore(_page_hinkley(rn, YDAYS), YDAYS)\nz5 = _rolling_zscore(_page_hinkley(rsi, YDAYS), YDAYS); z6 = _rolling_zscore(_page_hinkley(m, YDAYS), YDAYS); z7 = _rolling_zscore(_page_hinkley(o, YDAYS), YDAYS)",
        "z1.fillna(0) + z2.fillna(0) + z3.fillna(0) + z4.fillna(0) + z5.fillna(0) + z6.fillna(0) + z7.fillna(0)")
    add("cp_intensity_at_252h_volume_indicator",
        "PH(log-vol)>252d-p90 AND close=252d max (volume regime change at top).",
        ("close","volume","high"),
        "lv = _safe_log(volume.replace(0, np.nan))\nph = _page_hinkley(lv, YDAYS); p90 = ph.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "((ph > p90) & (high >= rmax - 1e-12)).astype(float).where(p90.notna(), np.nan)")
    add("cp_intensity_at_252h_atr_indicator",
        "PH(log-ATR)>252d-p90 AND close=252d max (vol regime change at top).",
        ("close","high","low"),
        "an = _safe_log(_safe_div(_atr(high, low, close, MDAYS), close))\nph = _page_hinkley(an, YDAYS); p90 = ph.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "((ph > p90) & (high >= rmax - 1e-12)).astype(float).where(p90.notna(), np.nan)")
    add("cp_intensity_at_252h_rsi_indicator",
        "PH(RSI14)>252d-p90 AND close=252d max.",
        ("close","high"),
        "rsi = _rsi(close, 14)\nph = _page_hinkley(rsi, YDAYS); p90 = ph.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "((ph > p90) & (high >= rmax - 1e-12)).astype(float).where(p90.notna(), np.nan)")
    add("cp_simultaneous_3_streams_at_252h_indicator",
        ">=3 streams (PH on r, |r|, vol, RSI, MACD) all in their respective 252d-top-decile AND at 252h.",
        ("close","volume","high"),
        "r = _log_ret(close); x = r.abs(); lv = _safe_log(volume.replace(0, np.nan)); rsi = _rsi(close, 14); m = _macd(close)\np1 = _page_hinkley(r, YDAYS); p2 = _page_hinkley(x, YDAYS); p3 = _page_hinkley(lv, YDAYS); p4 = _page_hinkley(rsi, YDAYS); p5 = _page_hinkley(m, YDAYS)\nq1 = p1.rolling(YDAYS, min_periods=QDAYS).quantile(0.90); q2 = p2.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\nq3 = p3.rolling(YDAYS, min_periods=QDAYS).quantile(0.90); q4 = p4.rolling(YDAYS, min_periods=QDAYS).quantile(0.90); q5 = p5.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\ncnt = ((p1 > q1).astype(float) + (p2 > q2).astype(float) + (p3 > q3).astype(float) + (p4 > q4).astype(float) + (p5 > q5).astype(float))\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "((cnt >= 3) & (high >= rmax - 1e-12)).astype(float).where(q1.notna() & q2.notna() & q3.notna(), np.nan)")

    # ---- Block J (136-150): composites and persistence of regime shifts ----
    add("regime_shift_persistence_density_63d",
        "Fraction of last 63d where regime-shift intensity > 252d-mean.",
        ("close",), "r = _log_ret(close)\nz = _rolling_zscore(_cusum_pos(r, YDAYS), YDAYS) + _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)\nmu = z.rolling(YDAYS, min_periods=QDAYS).mean()\nind = (z > mu).astype(float).where(mu.notna(), np.nan)",
        "ind.rolling(QDAYS, min_periods=MDAYS).mean()")
    add("regime_shift_bars_since_last_z_above_2_capped_252",
        "Bars since regime-shift intensity z>2 (capped 252).",
        ("close",), "r = _log_ret(close)\nz = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)\nev = (z > 2.0).astype(float).where(z.notna(), np.nan)",
        "_bars_since_last_event(ev).clip(upper=float(YDAYS))")
    add("regime_shift_count_z_above_2_in_252d",
        "Count of bars in 252d where regime-shift z>2.",
        ("close",), "r = _log_ret(close)\nz = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)\nev = (z > 2.0).astype(float).where(z.notna(), np.nan)",
        "ev.rolling(YDAYS, min_periods=QDAYS).sum()")
    add("regime_shift_count_at_252h_in_252d",
        "Count of bars in 252d with regime-shift z>2 AND close=252d max.",
        ("close",), "r = _log_ret(close)\nz = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()\nev = ((z > 2.0) & (close >= rmax - 1e-12)).astype(float).where(z.notna(), np.nan)",
        "ev.rolling(YDAYS, min_periods=QDAYS).sum()")
    add("regime_shift_acceleration_252d",
        "21-bar diff of regime-shift intensity z.",
        ("close",), "r = _log_ret(close)\nz = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)",
        "z - z.shift(MDAYS)")
    add("regime_shift_volatility_in_intensity_252d",
        "63d std of regime-shift intensity z over 252d - regime-of-regime-changes volatility.",
        ("close",), "r = _log_ret(close)\nz = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)",
        "z.rolling(QDAYS, min_periods=MDAYS).std()")
    add("recent_regime_shift_intensity_minus_long_term_252d",
        "21d-mean regime-shift z minus 504d-mean regime-shift z.",
        ("close",), "r = _log_ret(close)\nz = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)\nm21 = z.rolling(MDAYS, min_periods=10).mean(); m504 = z.rolling(DDAYS_2Y, min_periods=YDAYS).mean()",
        "m21 - m504")
    add("regime_shift_clustering_pair_count_252d",
        "Count of consecutive-bar pairs with regime-shift z>2 in last 252d.",
        ("close",), "r = _log_ret(close)\nz = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)\nev = (z > 2.0).astype(float).where(z.notna(), np.nan)\npair = (ev * ev.shift(1)).fillna(0.0)",
        "pair.rolling(YDAYS, min_periods=QDAYS).sum()")
    add("cusum_pos_above_p90_persistence_63d",
        "Fraction of last 63d with CUSUM-pos > 252d-p90.",
        ("close",), "r = _log_ret(close)\nu = _cusum_pos(r, YDAYS); p90 = u.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\nind = (u > p90).astype(float).where(p90.notna(), np.nan)",
        "ind.rolling(QDAYS, min_periods=MDAYS).mean()")
    add("cumulative_change_metric_diff_pos_neg_252d",
        "Sum of pos-CUSUM minus sum of neg-CUSUM over 252d window - directional regime sum.",
        ("close",), "r = _log_ret(close)\nu = _cusum_pos(r, YDAYS); d = _cusum_neg(r, YDAYS)",
        "u.rolling(YDAYS, min_periods=QDAYS).sum() - d.rolling(YDAYS, min_periods=QDAYS).sum()")
    add("regime_shift_at_252h_composite_score",
        "Z-sum of (CUSUM-pos + Page-Hinkley + max-split-t + E-stat) restricted to bars at 252d high.",
        ("close",), "r = _log_ret(close)\nz = (_rolling_zscore(_cusum_pos(r, YDAYS), YDAYS) + _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS) + _rolling_zscore(_cumulative_t_stat_max(r, YDAYS), YDAYS) + _rolling_zscore(_energy_distance(r, YDAYS), YDAYS))\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()",
        "z.where(close >= rmax - 1e-12, np.nan)")
    add("regime_shift_max_z_in_63d",
        "Max regime-shift z observed in last 63d.",
        ("close",), "r = _log_ret(close)\nz = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)",
        "z.rolling(QDAYS, min_periods=MDAYS).max()")
    add("regime_shift_z_above_3_indicator",
        "Regime-shift intensity z > 3 (very strong change signal).",
        ("close",), "r = _log_ret(close)\nz = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)",
        "(z > 3.0).astype(float).where(z.notna(), np.nan)")
    add("regime_shift_z_above_3_at_252h_indicator",
        "Regime-shift z > 3 AND close = 252d max.",
        ("close",), "r = _log_ret(close)\nz = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()",
        "((z > 3.0) & (close >= rmax - 1e-12)).astype(float).where(z.notna(), np.nan)")
    add("regime_shift_in_overnight_ret_at_252h_indicator",
        "PH on overnight returns > 252d-p90 AND close = 252d max.",
        ("open","close","high"),
        "on = _safe_log(open) - _safe_log(close.shift(1))\nph = _page_hinkley(on, YDAYS); p90 = ph.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "((ph > p90) & (high >= rmax - 1e-12)).astype(float).where(p90.notna(), np.nan)")
    add("regime_shift_in_intraday_ret_at_252h_indicator",
        "PH on intraday returns > 252d-p90 AND close = 252d max.",
        ("open","close","high"),
        "i = _safe_log(close) - _safe_log(open)\nph = _page_hinkley(i, YDAYS); p90 = ph.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "((ph > p90) & (high >= rmax - 1e-12)).astype(float).where(p90.notna(), np.nan)")
    add("regime_shift_in_macd_at_252h_indicator",
        "PH on MACD > 252d-p90 AND close = 252d max.",
        ("close","high"),
        "m = _macd(close)\nph = _page_hinkley(m, YDAYS); p90 = ph.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "((ph > p90) & (high >= rmax - 1e-12)).astype(float).where(p90.notna(), np.nan)")
    add("regime_shift_in_obv_at_252h_indicator",
        "PH on OBV > 252d-p90 AND close = 252d max.",
        ("close","volume","high"),
        "o = _obv(close, volume)\nph = _page_hinkley(o, YDAYS); p90 = ph.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\nrmax = high.rolling(YDAYS, min_periods=QDAYS).max()",
        "((ph > p90) & (high >= rmax - 1e-12)).astype(float).where(p90.notna(), np.nan)")
    add("regime_break_count_negative_cusum_252d",
        "Count of bars in 252d where neg-CUSUM > 252d-p90 (downward-shift events).",
        ("close",),
        "r = _log_ret(close)\nd = _cusum_neg(r, YDAYS); p90 = d.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\nev = (d > p90).astype(float).where(p90.notna(), np.nan)",
        "ev.rolling(YDAYS, min_periods=QDAYS).sum()")
    add("max_split_t_stat_minus_baseline_504d",
        "Max-split-t-stat 252d minus its 504d-mean - relative regime-change intensity.",
        ("close",),
        "r = _log_ret(close)\nt = _cumulative_t_stat_max(r, YDAYS); bm = t.rolling(DDAYS_2Y, min_periods=YDAYS).mean()",
        "t - bm")
    add("regime_shift_z_above_4_indicator",
        "Regime-shift z > 4 (extreme change event).",
        ("close",),
        "r = _log_ret(close)\nz = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)",
        "(z > 4.0).astype(float).where(z.notna(), np.nan)")
    add("regime_shift_recent_decay_indicator",
        "Regime-shift z was >2 in last 21 bars BUT now <0.5 (event aftermath).",
        ("close",),
        "r = _log_ret(close)\nz = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)\nhigh_recent = (z > 2.0).astype(float).rolling(MDAYS, min_periods=5).max()",
        "((high_recent > 0.5) & (z < 0.5)).astype(float).where(z.notna(), np.nan)")
    add("regime_shift_consistency_3of3_streams_252d",
        "All 3 streams (PH on r, |r|, log-vol) above their 252d-medians simultaneously.",
        ("close","volume"),
        "r = _log_ret(close); x = r.abs(); lv = _safe_log(volume.replace(0, np.nan))\nph1 = _page_hinkley(r, YDAYS); ph2 = _page_hinkley(x, YDAYS); ph3 = _page_hinkley(lv, YDAYS)\nm1 = ph1.rolling(YDAYS, min_periods=QDAYS).median(); m2 = ph2.rolling(YDAYS, min_periods=QDAYS).median(); m3 = ph3.rolling(YDAYS, min_periods=QDAYS).median()",
        "((ph1 > m1) & (ph2 > m2) & (ph3 > m3)).astype(float).where(m1.notna() & m2.notna() & m3.notna(), np.nan)")
    add("regime_shift_amplitude_max_in_504d",
        "Max regime-shift z observed in trailing 504d.",
        ("close",),
        "r = _log_ret(close)\nz = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)",
        "z.rolling(DDAYS_2Y, min_periods=YDAYS).max()")
    add("master_regime_break_composite_252d",
        "Average z-rank of: CUSUM, PH, max-split-t, E-stat, BOCP-inverted, var-ratio, mean-shift over 252d.",
        ("close",), "r = _log_ret(close)\nz1 = _rolling_zscore(_cusum_pos(r, YDAYS), YDAYS); z2 = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)\nz3 = _rolling_zscore(_cumulative_t_stat_max(r, YDAYS), YDAYS); z4 = _rolling_zscore(_energy_distance(r, YDAYS), YDAYS)\nz5 = -_rolling_zscore(_bayesian_cp_run_length_mean(r, YDAYS, 0.01), YDAYS)\nz6 = _rolling_zscore(_variance_ratio_change(r, MDAYS, YDAYS), YDAYS)\nz7 = _rolling_zscore(_mean_shift_z(r, MDAYS, YDAYS), YDAYS)",
        "(z1.fillna(0) + z2.fillna(0) + z3.fillna(0) + z4.fillna(0) + z5.fillna(0) + z6.fillna(0) + z7.fillna(0)) / 7.0")
    return F


def f58_features():
    F = _f58()
    return _f58_part2(F)


# =========================================================================
# FAMILY 59 - cross_horizon_term_structure (chts)
# Term-structure slopes/curvatures across multiple horizons for various metrics
# =========================================================================

F59_META = {"num": "59", "abbr": "chts",
            "folder": "59_cross_horizon_term_structure",
            "name": "cross_horizon_term_structure",
            "name_upper": "CROSS_HORIZON_TERM_STRUCTURE"}

CHTS_HELPERS = '''
def _drawdown_log_n(close, n):
    mp = max(n // 3, 20)
    lc = _safe_log(close)
    def _md(w):
        v = w[~np.isnan(w)]
        if v.size < 10: return np.nan
        cm = np.maximum.accumulate(v)
        return float((v - cm).min())
    return lc.rolling(n, min_periods=mp).apply(_md, raw=True)


def _sharpe_n(close, n):
    r = _log_ret(close)
    mp = max(n // 3, 10)
    mu = r.rolling(n, min_periods=mp).mean()
    sd = r.rolling(n, min_periods=mp).std()
    return _safe_div(mu, sd)


def _sortino_n(close, n):
    r = _log_ret(close)
    mp = max(n // 3, 10)
    mu = r.rolling(n, min_periods=mp).mean()
    neg = (-r).clip(lower=0.0)
    dd = np.sqrt((neg ** 2).rolling(n, min_periods=mp).mean())
    return _safe_div(mu, dd)


def _acf_lag1_n(s, n):
    mp = max(n // 3, 10)
    def _ac(w):
        x = w[~np.isnan(w)]
        if x.size < 20: return np.nan
        a = x[:-1]; b = x[1:]
        if a.std() == 0 or b.std() == 0: return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    return s.rolling(n, min_periods=mp).apply(_ac, raw=True)


def _amihud_n(close, volume, n):
    r = _log_ret(close).abs()
    dv = (close * volume).replace(0, np.nan)
    return _safe_div(r, dv).rolling(n, min_periods=max(n // 3, 10)).mean()


def _ts_slope(h_short, h_med, h_long):
    """Log-log slope of (metric @ h_short, h_med, h_long). Inputs are Series of metric values at each horizon."""
    df = pd.concat([h_short.rename("a"), h_med.rename("b"), h_long.rename("c")], axis=1)
    x = np.log(np.array([21.0, 63.0, 252.0]))
    xm = x.mean(); sxx = ((x - xm) ** 2).sum()
    def _sl(row):
        if np.isnan(row).any(): return np.nan
        y = np.log(np.maximum(row, 1e-12))
        ym = y.mean()
        return float(((x - xm) * (y - ym)).sum() / sxx) if sxx > 0 else np.nan
    vals = df.values
    out = np.array([_sl(vals[i]) for i in range(len(vals))], dtype=float)
    return pd.Series(out, index=df.index)


def _ts_convexity(h_short, h_med, h_long):
    """h_short - 2*h_med + h_long (curvature)."""
    return h_short - 2.0 * h_med + h_long


def _ts_inversion(h_short, h_med, h_long):
    """Sign of (h_short - h_long) - inversion indicator."""
    return np.sign(h_short - h_long)
'''


def _f59():
    F, add = _S()
    # ---- Block A (1-10): Volatility term-structure ----
    add("vol_ts_21d_value", "Realized vol 21d.",
        ("close",), "r = _log_ret(close)", "r.rolling(MDAYS, min_periods=10).std()")
    add("vol_ts_63d_value", "Realized vol 63d.",
        ("close",), "r = _log_ret(close)", "r.rolling(QDAYS, min_periods=MDAYS).std()")
    add("vol_ts_252d_value", "Realized vol 252d.",
        ("close",), "r = _log_ret(close)", "r.rolling(YDAYS, min_periods=QDAYS).std()")
    add("vol_ts_short_minus_long_21d_252d",
        "Vol(21d) - Vol(252d) - level-shift indicator.",
        ("close",), "r = _log_ret(close)\nv21 = r.rolling(MDAYS, min_periods=10).std(); v252 = r.rolling(YDAYS, min_periods=QDAYS).std()",
        "v21 - v252")
    add("vol_ts_ratio_21d_252d",
        "Vol(21d) / Vol(252d).",
        ("close",), "r = _log_ret(close)\nv21 = r.rolling(MDAYS, min_periods=10).std(); v252 = r.rolling(YDAYS, min_periods=QDAYS).std()",
        "_safe_div(v21, v252)")
    add("vol_ts_log_slope_21_63_252",
        "Log-log slope of vol term-structure.",
        ("close",), "r = _log_ret(close)\nv1 = r.rolling(MDAYS, min_periods=10).std(); v2 = r.rolling(QDAYS, min_periods=MDAYS).std(); v3 = r.rolling(YDAYS, min_periods=QDAYS).std()",
        "_ts_slope(v1, v2, v3)")
    add("vol_ts_convexity_21_63_252",
        "Convexity: V21 - 2*V63 + V252.",
        ("close",), "r = _log_ret(close)\nv1 = r.rolling(MDAYS, min_periods=10).std(); v2 = r.rolling(QDAYS, min_periods=MDAYS).std(); v3 = r.rolling(YDAYS, min_periods=QDAYS).std()",
        "_ts_convexity(v1, v2, v3)")
    add("vol_ts_inversion_sign_indicator",
        "Sign(V21 - V252) - +1 = inverted (short>long vol).",
        ("close",), "r = _log_ret(close)\nv21 = r.rolling(MDAYS, min_periods=10).std(); v252 = r.rolling(YDAYS, min_periods=QDAYS).std()",
        "np.sign(v21 - v252)")
    add("vol_ts_inversion_indicator_at_high",
        "Vol inversion (V21>V252) AND close = 252d max.",
        ("close",), "r = _log_ret(close)\nv21 = r.rolling(MDAYS, min_periods=10).std(); v252 = r.rolling(YDAYS, min_periods=QDAYS).std()\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()",
        "((v21 > v252) & (close >= rmax - 1e-12)).astype(float).where(v252.notna(), np.nan)")
    add("vol_ts_slope_z_252d",
        "z-score of vol-TS log-log slope over 252d.",
        ("close",), "r = _log_ret(close)\nv1 = r.rolling(MDAYS, min_periods=10).std(); v2 = r.rolling(QDAYS, min_periods=MDAYS).std(); v3 = r.rolling(YDAYS, min_periods=QDAYS).std()\nsl = _ts_slope(v1, v2, v3)",
        "_rolling_zscore(sl, YDAYS)")

    # ---- Block B (11-20): Sharpe term-structure ----
    add("sharpe_ts_21d_value", "Daily Sharpe 21d.", ("close",), "", "_sharpe_n(close, MDAYS)")
    add("sharpe_ts_63d_value", "Daily Sharpe 63d.", ("close",), "", "_sharpe_n(close, QDAYS)")
    add("sharpe_ts_252d_value", "Daily Sharpe 252d.", ("close",), "", "_sharpe_n(close, YDAYS)")
    add("sharpe_ts_short_minus_long_21d_252d", "Sharpe(21) - Sharpe(252).",
        ("close",), "", "_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS)")
    add("sharpe_ts_ratio_21d_252d", "Sharpe(21) / Sharpe(252).",
        ("close",), "", "_safe_div(_sharpe_n(close, MDAYS), _sharpe_n(close, YDAYS))")
    add("sharpe_ts_convexity_21_63_252",
        "Sharpe convexity S(21)-2*S(63)+S(252).",
        ("close",), "s1 = _sharpe_n(close, MDAYS); s2 = _sharpe_n(close, QDAYS); s3 = _sharpe_n(close, YDAYS)",
        "_ts_convexity(s1, s2, s3)")
    add("sharpe_ts_inversion_sign", "Sign(Sharpe21 - Sharpe252).",
        ("close",), "", "np.sign(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS))")
    add("sharpe_ts_degradation_indicator",
        "Sharpe(21) < 0 AND Sharpe(252) > 0 (short-term degradation while long is positive).",
        ("close",), "s1 = _sharpe_n(close, MDAYS); s3 = _sharpe_n(close, YDAYS)",
        "((s1 < 0) & (s3 > 0)).astype(float).where(s1.notna() & s3.notna(), np.nan)")
    add("sharpe_ts_degradation_at_252h_indicator",
        "Sharpe degradation AND close = 252d max.",
        ("close",), "s1 = _sharpe_n(close, MDAYS); s3 = _sharpe_n(close, YDAYS)\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()",
        "((s1 < 0) & (s3 > 0) & (close >= rmax - 1e-12)).astype(float).where(s1.notna() & s3.notna(), np.nan)")
    add("sharpe_ts_short_drop_z_252d",
        "z-score of (Sharpe(21) - Sharpe(252)) over 252d.",
        ("close",), "diff = _sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS)",
        "_rolling_zscore(diff, YDAYS)")

    # ---- Block C (21-30): Sortino term-structure ----
    add("sortino_ts_21d_value", "Sortino 21d.", ("close",), "", "_sortino_n(close, MDAYS)")
    add("sortino_ts_63d_value", "Sortino 63d.", ("close",), "", "_sortino_n(close, QDAYS)")
    add("sortino_ts_252d_value", "Sortino 252d.", ("close",), "", "_sortino_n(close, YDAYS)")
    add("sortino_ts_short_minus_long", "Sortino(21) - Sortino(252).",
        ("close",), "", "_sortino_n(close, MDAYS) - _sortino_n(close, YDAYS)")
    add("sortino_ts_ratio_21_252", "Sortino(21) / Sortino(252).",
        ("close",), "", "_safe_div(_sortino_n(close, MDAYS), _sortino_n(close, YDAYS))")
    add("sortino_ts_convexity_21_63_252",
        "Sortino convexity.",
        ("close",), "s1 = _sortino_n(close, MDAYS); s2 = _sortino_n(close, QDAYS); s3 = _sortino_n(close, YDAYS)",
        "_ts_convexity(s1, s2, s3)")
    add("sortino_ts_inversion_sign", "Sign(Sortino21 - Sortino252).",
        ("close",), "", "np.sign(_sortino_n(close, MDAYS) - _sortino_n(close, YDAYS))")
    add("sortino_ts_degradation_indicator",
        "Sortino(21) < 0 AND Sortino(252) > 0.",
        ("close",), "s1 = _sortino_n(close, MDAYS); s3 = _sortino_n(close, YDAYS)",
        "((s1 < 0) & (s3 > 0)).astype(float).where(s1.notna() & s3.notna(), np.nan)")
    add("sortino_ts_degradation_at_252h",
        "Sortino degradation AND at 252d max.",
        ("close",), "s1 = _sortino_n(close, MDAYS); s3 = _sortino_n(close, YDAYS)\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()",
        "((s1 < 0) & (s3 > 0) & (close >= rmax - 1e-12)).astype(float).where(s1.notna() & s3.notna(), np.nan)")
    add("sortino_ts_drop_z_252d",
        "z-score of Sortino(21)-Sortino(252) over 252d.",
        ("close",), "diff = _sortino_n(close, MDAYS) - _sortino_n(close, YDAYS)",
        "_rolling_zscore(diff, YDAYS)")

    # ---- Block D (31-40): Max-drawdown term-structure ----
    add("max_dd_21d_value", "Max DD 21d (negative log value).",
        ("close",), "", "_drawdown_log_n(close, MDAYS)")
    add("max_dd_63d_value", "Max DD 63d.", ("close",), "", "_drawdown_log_n(close, QDAYS)")
    add("max_dd_252d_value", "Max DD 252d.", ("close",), "", "_drawdown_log_n(close, YDAYS)")
    add("max_dd_504d_value", "Max DD 504d.", ("close",), "", "_drawdown_log_n(close, DDAYS_2Y)")
    add("max_dd_ts_ratio_21_252", "|MaxDD21| / |MaxDD252|.",
        ("close",), "d1 = -_drawdown_log_n(close, MDAYS); d3 = -_drawdown_log_n(close, YDAYS)",
        "_safe_div(d1, d3)")
    add("max_dd_ts_ratio_63_252", "|MaxDD63| / |MaxDD252|.",
        ("close",), "d2 = -_drawdown_log_n(close, QDAYS); d3 = -_drawdown_log_n(close, YDAYS)",
        "_safe_div(d2, d3)")
    add("max_dd_ts_short_minus_long_252_504",
        "|MaxDD252| - |MaxDD504| - recent DD severity vs long-term.",
        ("close",), "d3 = -_drawdown_log_n(close, YDAYS); d4 = -_drawdown_log_n(close, DDAYS_2Y)",
        "d3 - d4")
    add("max_dd_ts_convexity_21_63_252",
        "MaxDD convexity (DD21 - 2*DD63 + DD252) - on magnitude.",
        ("close",), "d1 = -_drawdown_log_n(close, MDAYS); d2 = -_drawdown_log_n(close, QDAYS); d3 = -_drawdown_log_n(close, YDAYS)",
        "_ts_convexity(d1, d2, d3)")
    add("max_dd_acceleration_21d_252d",
        "(|MaxDD21| - |MaxDD63|) - acceleration of drawdown.",
        ("close",), "d1 = -_drawdown_log_n(close, MDAYS); d2 = -_drawdown_log_n(close, QDAYS)",
        "d1 - d2")
    add("max_dd_ratio_above_1_5_indicator",
        "|MaxDD21| / |MaxDD252| > 1.5 (recent DD bigger than long-term - acute stress).",
        ("close",), "d1 = -_drawdown_log_n(close, MDAYS); d3 = -_drawdown_log_n(close, YDAYS); r = _safe_div(d1, d3)",
        "(r > 1.5).astype(float).where(r.notna(), np.nan)")

    # ---- Block E (41-50): Skew term-structure ----
    add("skew_ts_21d_value", "Skew of log-returns 21d.",
        ("close",), "r = _log_ret(close)", "r.rolling(MDAYS, min_periods=10).skew()")
    add("skew_ts_63d_value", "Skew 63d.",
        ("close",), "r = _log_ret(close)", "r.rolling(QDAYS, min_periods=MDAYS).skew()")
    add("skew_ts_252d_value", "Skew 252d.",
        ("close",), "r = _log_ret(close)", "r.rolling(YDAYS, min_periods=QDAYS).skew()")
    add("skew_ts_short_minus_long", "Skew(21) - Skew(252).",
        ("close",), "r = _log_ret(close)", "r.rolling(MDAYS, min_periods=10).skew() - r.rolling(YDAYS, min_periods=QDAYS).skew()")
    add("skew_ts_convexity_21_63_252",
        "Skew convexity S(21) - 2*S(63) + S(252).",
        ("close",), "r = _log_ret(close)\ns1 = r.rolling(MDAYS, min_periods=10).skew(); s2 = r.rolling(QDAYS, min_periods=MDAYS).skew(); s3 = r.rolling(YDAYS, min_periods=QDAYS).skew()",
        "_ts_convexity(s1, s2, s3)")
    add("skew_ts_inversion_sign",
        "Sign(Skew21 - Skew252) - skew regime alignment.",
        ("close",), "r = _log_ret(close)",
        "np.sign(r.rolling(MDAYS, min_periods=10).skew() - r.rolling(YDAYS, min_periods=QDAYS).skew())")
    add("skew_ts_sign_flip_indicator",
        "Skew(21)<0 AND Skew(252)>0 (recent negative skew while long-term positive).",
        ("close",), "r = _log_ret(close)\ns1 = r.rolling(MDAYS, min_periods=10).skew(); s3 = r.rolling(YDAYS, min_periods=QDAYS).skew()",
        "((s1 < 0) & (s3 > 0)).astype(float).where(s1.notna() & s3.notna(), np.nan)")
    add("skew_ts_sign_flip_at_252h_indicator",
        "Skew sign-flip AND close = 252d max.",
        ("close",), "r = _log_ret(close)\ns1 = r.rolling(MDAYS, min_periods=10).skew(); s3 = r.rolling(YDAYS, min_periods=QDAYS).skew()\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()",
        "((s1 < 0) & (s3 > 0) & (close >= rmax - 1e-12)).astype(float).where(s1.notna() & s3.notna(), np.nan)")
    add("skew_ts_log_slope",
        "Log-log slope of |skew| TS.",
        ("close",), "r = _log_ret(close)\ns1 = r.rolling(MDAYS, min_periods=10).skew().abs() + 1e-6\ns2 = r.rolling(QDAYS, min_periods=MDAYS).skew().abs() + 1e-6\ns3 = r.rolling(YDAYS, min_periods=QDAYS).skew().abs() + 1e-6",
        "_ts_slope(s1, s2, s3)")
    add("skew_ts_drop_z_252d",
        "z-score of (Skew21 - Skew252) over 252d.",
        ("close",), "r = _log_ret(close)\ndiff = r.rolling(MDAYS, min_periods=10).skew() - r.rolling(YDAYS, min_periods=QDAYS).skew()",
        "_rolling_zscore(diff, YDAYS)")

    # ---- Block F (51-60): Kurt term-structure ----
    add("kurt_ts_21d_value", "Excess kurt 21d.",
        ("close",), "r = _log_ret(close)", "r.rolling(MDAYS, min_periods=10).kurt()")
    add("kurt_ts_63d_value", "Excess kurt 63d.",
        ("close",), "r = _log_ret(close)", "r.rolling(QDAYS, min_periods=MDAYS).kurt()")
    add("kurt_ts_252d_value", "Excess kurt 252d.",
        ("close",), "r = _log_ret(close)", "r.rolling(YDAYS, min_periods=QDAYS).kurt()")
    add("kurt_ts_short_minus_long", "Kurt(21) - Kurt(252).",
        ("close",), "r = _log_ret(close)", "r.rolling(MDAYS, min_periods=10).kurt() - r.rolling(YDAYS, min_periods=QDAYS).kurt()")
    add("kurt_ts_ratio_21_252", "Kurt(21) / Kurt(252).",
        ("close",), "r = _log_ret(close)", "_safe_div(r.rolling(MDAYS, min_periods=10).kurt(), r.rolling(YDAYS, min_periods=QDAYS).kurt())")
    add("kurt_ts_convexity",
        "Kurt convexity.",
        ("close",), "r = _log_ret(close)\nk1 = r.rolling(MDAYS, min_periods=10).kurt(); k2 = r.rolling(QDAYS, min_periods=MDAYS).kurt(); k3 = r.rolling(YDAYS, min_periods=QDAYS).kurt()",
        "_ts_convexity(k1, k2, k3)")
    add("kurt_ts_above_5_at_short",
        "Kurt(21) > 5 indicator (recent fat tails).",
        ("close",), "r = _log_ret(close)\nk = r.rolling(MDAYS, min_periods=10).kurt()",
        "(k > 5.0).astype(float).where(k.notna(), np.nan)")
    add("kurt_ts_above_5_at_short_AND_at_252h",
        "Recent kurt>5 AND close = 252d max (heavy tails forming at top).",
        ("close",), "r = _log_ret(close)\nk = r.rolling(MDAYS, min_periods=10).kurt()\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()",
        "((k > 5.0) & (close >= rmax - 1e-12)).astype(float).where(k.notna(), np.nan)")
    add("kurt_ts_log_slope",
        "Log-log slope of |kurt|+1 TS.",
        ("close",), "r = _log_ret(close)\nk1 = (r.rolling(MDAYS, min_periods=10).kurt().abs() + 1.0); k2 = (r.rolling(QDAYS, min_periods=MDAYS).kurt().abs() + 1.0); k3 = (r.rolling(YDAYS, min_periods=QDAYS).kurt().abs() + 1.0)",
        "_ts_slope(k1, k2, k3)")
    add("kurt_ts_drop_z_252d",
        "z-score of (Kurt21 - Kurt252) over 252d.",
        ("close",), "r = _log_ret(close)\ndiff = r.rolling(MDAYS, min_periods=10).kurt() - r.rolling(YDAYS, min_periods=QDAYS).kurt()",
        "_rolling_zscore(diff, YDAYS)")

    # ---- Block G (61-70): ACF persistence term-structure ----
    add("acf_lag1_ts_21d_value_log_ret",
        "ACF(1) of log-returns 21d.",
        ("close",), "r = _log_ret(close)", "_acf_lag1_n(r, MDAYS)")
    add("acf_lag1_ts_63d_value_log_ret",
        "ACF(1) of log-returns 63d.",
        ("close",), "r = _log_ret(close)", "_acf_lag1_n(r, QDAYS)")
    add("acf_lag1_ts_252d_value_log_ret",
        "ACF(1) of log-returns 252d.",
        ("close",), "r = _log_ret(close)", "_acf_lag1_n(r, YDAYS)")
    add("acf_lag1_ts_short_minus_long_log_ret", "ACF(21) - ACF(252).",
        ("close",), "r = _log_ret(close)", "_acf_lag1_n(r, MDAYS) - _acf_lag1_n(r, YDAYS)")
    add("acf_lag1_ts_convexity_log_ret",
        "ACF convexity (a21 - 2*a63 + a252) over log-returns.",
        ("close",), "r = _log_ret(close)\na1 = _acf_lag1_n(r, MDAYS); a2 = _acf_lag1_n(r, QDAYS); a3 = _acf_lag1_n(r, YDAYS)",
        "_ts_convexity(a1, a2, a3)")
    add("acf_lag1_ts_21d_abs_ret", "ACF(1) of |r| 21d (vol clustering).",
        ("close",), "x = _log_ret(close).abs()", "_acf_lag1_n(x, MDAYS)")
    add("acf_lag1_ts_63d_abs_ret", "ACF(1) of |r| 63d.",
        ("close",), "x = _log_ret(close).abs()", "_acf_lag1_n(x, QDAYS)")
    add("acf_lag1_ts_252d_abs_ret", "ACF(1) of |r| 252d.",
        ("close",), "x = _log_ret(close).abs()", "_acf_lag1_n(x, YDAYS)")
    add("acf_lag1_ts_short_minus_long_abs_ret",
        "ACF21(|r|) - ACF252(|r|).",
        ("close",), "x = _log_ret(close).abs()", "_acf_lag1_n(x, MDAYS) - _acf_lag1_n(x, YDAYS)")
    add("acf_lag1_ts_drop_z_252d_log_ret",
        "z-score of (ACF21 - ACF252) over 252d.",
        ("close",), "r = _log_ret(close)\ndiff = _acf_lag1_n(r, MDAYS) - _acf_lag1_n(r, YDAYS)",
        "_rolling_zscore(diff, YDAYS)")

    # ---- Block H (71-80): Amihud liquidity term-structure ----
    add("amihud_ts_21d_value", "Amihud illiquidity 21d.",
        ("close","volume"), "", "_amihud_n(close, volume, MDAYS)")
    add("amihud_ts_63d_value", "Amihud illiquidity 63d.",
        ("close","volume"), "", "_amihud_n(close, volume, QDAYS)")
    add("amihud_ts_252d_value", "Amihud illiquidity 252d.",
        ("close","volume"), "", "_amihud_n(close, volume, YDAYS)")
    add("amihud_ts_short_minus_long_21_252", "Amihud(21) - Amihud(252).",
        ("close","volume"), "", "_amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS)")
    add("amihud_ts_ratio_21_252", "Amihud(21) / Amihud(252) - liquidity-regime shift.",
        ("close","volume"), "", "_safe_div(_amihud_n(close, volume, MDAYS), _amihud_n(close, volume, YDAYS))")
    add("amihud_ts_log_slope_21_63_252",
        "Log-log slope of Amihud TS.",
        ("close","volume"), "a1 = _amihud_n(close, volume, MDAYS); a2 = _amihud_n(close, volume, QDAYS); a3 = _amihud_n(close, volume, YDAYS)",
        "_ts_slope(a1, a2, a3)")
    add("amihud_ts_convexity",
        "Amihud convexity.",
        ("close","volume"), "a1 = _amihud_n(close, volume, MDAYS); a2 = _amihud_n(close, volume, QDAYS); a3 = _amihud_n(close, volume, YDAYS)",
        "_ts_convexity(a1, a2, a3)")
    add("amihud_ts_ratio_above_2_indicator",
        "Amihud(21)/Amihud(252) > 2 (liquidity drying up).",
        ("close","volume"), "rt = _safe_div(_amihud_n(close, volume, MDAYS), _amihud_n(close, volume, YDAYS))",
        "(rt > 2.0).astype(float).where(rt.notna(), np.nan)")
    add("amihud_ts_at_252h_above_2_indicator",
        "Amihud ratio > 2 AND close = 252d max (illiquid at top).",
        ("close","volume"), "rt = _safe_div(_amihud_n(close, volume, MDAYS), _amihud_n(close, volume, YDAYS))\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()",
        "((rt > 2.0) & (close >= rmax - 1e-12)).astype(float).where(rt.notna(), np.nan)")
    add("amihud_ts_drop_z_252d",
        "z-score of (Amihud21 - Amihud252) over 252d.",
        ("close","volume"), "diff = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS)",
        "_rolling_zscore(diff, YDAYS)")

    # ---- Block I (81-90): Volume regime term-structure ----
    add("log_vol_ts_21d_mean", "Mean log-volume 21d.",
        ("volume",), "lv = _safe_log(volume.replace(0, np.nan))", "lv.rolling(MDAYS, min_periods=10).mean()")
    add("log_vol_ts_63d_mean", "Mean log-volume 63d.",
        ("volume",), "lv = _safe_log(volume.replace(0, np.nan))", "lv.rolling(QDAYS, min_periods=MDAYS).mean()")
    add("log_vol_ts_252d_mean", "Mean log-volume 252d.",
        ("volume",), "lv = _safe_log(volume.replace(0, np.nan))", "lv.rolling(YDAYS, min_periods=QDAYS).mean()")
    add("log_vol_ts_short_minus_long_21_252", "log_vol(21)-log_vol(252) - volume regime shift.",
        ("volume",), "lv = _safe_log(volume.replace(0, np.nan))", "lv.rolling(MDAYS, min_periods=10).mean() - lv.rolling(YDAYS, min_periods=QDAYS).mean()")
    add("log_vol_ts_convexity",
        "Vol convexity.",
        ("volume",), "lv = _safe_log(volume.replace(0, np.nan))\nv1 = lv.rolling(MDAYS, min_periods=10).mean(); v2 = lv.rolling(QDAYS, min_periods=MDAYS).mean(); v3 = lv.rolling(YDAYS, min_periods=QDAYS).mean()",
        "_ts_convexity(v1, v2, v3)")
    add("log_vol_ts_inversion_sign",
        "Sign(logvol21-logvol252) - volume regime direction.",
        ("volume",), "lv = _safe_log(volume.replace(0, np.nan))",
        "np.sign(lv.rolling(MDAYS, min_periods=10).mean() - lv.rolling(YDAYS, min_periods=QDAYS).mean())")
    add("log_vol_std_ts_21d", "Std log-volume 21d.",
        ("volume",), "lv = _safe_log(volume.replace(0, np.nan))", "lv.rolling(MDAYS, min_periods=10).std()")
    add("log_vol_std_ts_252d", "Std log-volume 252d.",
        ("volume",), "lv = _safe_log(volume.replace(0, np.nan))", "lv.rolling(YDAYS, min_periods=QDAYS).std()")
    add("log_vol_std_ts_short_minus_long_21_252",
        "Vol-of-vol short minus long.",
        ("volume",), "lv = _safe_log(volume.replace(0, np.nan))", "lv.rolling(MDAYS, min_periods=10).std() - lv.rolling(YDAYS, min_periods=QDAYS).std()")
    add("log_vol_ts_drop_z_252d",
        "z-score of (logvol21 - logvol252) over 252d.",
        ("volume",), "lv = _safe_log(volume.replace(0, np.nan))\ndiff = lv.rolling(MDAYS, min_periods=10).mean() - lv.rolling(YDAYS, min_periods=QDAYS).mean()",
        "_rolling_zscore(diff, YDAYS)")

    # ---- Block J (91-100): Hurst persistence term-structure ----
    add("hurst_simple_ts_63d", "Simple R/S Hurst 63d.",
        ("close",),
        "r = _log_ret(close)\ndef _h(w):\n    v = w[~np.isnan(w)]\n    if v.size < 40: return np.nan\n    chunks = [c for c in [8, 16, 32] if c <= v.size // 2]\n    if len(chunks) < 2: return np.nan\n    rs = []\n    for c in chunks:\n        u = (v.size // c) * c\n        sub = v[:u].reshape(-1, c); mu = sub.mean(axis=1, keepdims=True)\n        cs = (sub - mu).cumsum(axis=1); rng = cs.max(axis=1) - cs.min(axis=1)\n        sd = sub.std(axis=1, ddof=1); ok = sd > 0\n        if ok.sum() > 0:\n            rs.append(float((rng[ok] / sd[ok]).mean()))\n    if len(rs) < 2: return np.nan\n    x = np.log(np.array(chunks[:len(rs)], dtype=float)); y = np.log(np.array(rs, dtype=float))\n    return float(np.polyfit(x, y, 1)[0])\nres = r.rolling(QDAYS, min_periods=MDAYS).apply(_h, raw=True)",
        "res")
    add("hurst_simple_ts_252d", "Simple R/S Hurst 252d.",
        ("close",),
        "r = _log_ret(close)\ndef _h(w):\n    v = w[~np.isnan(w)]\n    if v.size < 60: return np.nan\n    chunks = [c for c in [8, 16, 32, 64] if c <= v.size // 2]\n    if len(chunks) < 3: return np.nan\n    rs = []\n    for c in chunks:\n        u = (v.size // c) * c\n        sub = v[:u].reshape(-1, c); mu = sub.mean(axis=1, keepdims=True)\n        cs = (sub - mu).cumsum(axis=1); rng = cs.max(axis=1) - cs.min(axis=1)\n        sd = sub.std(axis=1, ddof=1); ok = sd > 0\n        if ok.sum() > 0:\n            rs.append(float((rng[ok] / sd[ok]).mean()))\n    if len(rs) < 3: return np.nan\n    x = np.log(np.array(chunks[:len(rs)], dtype=float)); y = np.log(np.array(rs, dtype=float))\n    return float(np.polyfit(x, y, 1)[0])\nres = r.rolling(YDAYS, min_periods=QDAYS).apply(_h, raw=True)",
        "res")
    add("hurst_ts_short_minus_long_63_252",
        "Hurst(63) - Hurst(252).",
        ("close",),
        "r = _log_ret(close)\ndef _hr(w, c_max):\n    v = w[~np.isnan(w)]\n    if v.size < 40: return np.nan\n    chunks = [c for c in [8, 16, 32, 64] if c <= v.size // 2]\n    if len(chunks) < 2: return np.nan\n    rs = []\n    for c in chunks:\n        u = (v.size // c) * c\n        sub = v[:u].reshape(-1, c); mu = sub.mean(axis=1, keepdims=True)\n        cs = (sub - mu).cumsum(axis=1); rng = cs.max(axis=1) - cs.min(axis=1)\n        sd = sub.std(axis=1, ddof=1); ok = sd > 0\n        if ok.sum() > 0:\n            rs.append(float((rng[ok] / sd[ok]).mean()))\n    if len(rs) < 2: return np.nan\n    x = np.log(np.array(chunks[:len(rs)], dtype=float)); y = np.log(np.array(rs, dtype=float))\n    return float(np.polyfit(x, y, 1)[0])\nh63 = r.rolling(QDAYS, min_periods=MDAYS).apply(lambda w: _hr(w, 32), raw=True)\nh252 = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _hr(w, 64), raw=True)",
        "h63 - h252")
    add("hurst_ts_drop_below_half_indicator",
        "Hurst(63) < 0.5 AND Hurst(252) > 0.5 (recent anti-persistent while long trend).",
        ("close",),
        "r = _log_ret(close)\ndef _hr(w):\n    v = w[~np.isnan(w)]\n    if v.size < 40: return np.nan\n    chunks = [c for c in [8, 16, 32, 64] if c <= v.size // 2]\n    if len(chunks) < 2: return np.nan\n    rs = []\n    for c in chunks:\n        u = (v.size // c) * c\n        sub = v[:u].reshape(-1, c); mu = sub.mean(axis=1, keepdims=True)\n        cs = (sub - mu).cumsum(axis=1); rng = cs.max(axis=1) - cs.min(axis=1)\n        sd = sub.std(axis=1, ddof=1); ok = sd > 0\n        if ok.sum() > 0:\n            rs.append(float((rng[ok] / sd[ok]).mean()))\n    if len(rs) < 2: return np.nan\n    x = np.log(np.array(chunks[:len(rs)], dtype=float)); y = np.log(np.array(rs, dtype=float))\n    return float(np.polyfit(x, y, 1)[0])\nh63 = r.rolling(QDAYS, min_periods=MDAYS).apply(_hr, raw=True); h252 = r.rolling(YDAYS, min_periods=QDAYS).apply(_hr, raw=True)",
        "((h63 < 0.5) & (h252 > 0.5)).astype(float).where(h63.notna() & h252.notna(), np.nan)")
    add("hurst_ts_at_252h_drop_indicator",
        "Hurst(63)<0.5 AND H(252)>0.5 AND at 252d max.",
        ("close",),
        "r = _log_ret(close)\ndef _hr(w):\n    v = w[~np.isnan(w)]\n    if v.size < 40: return np.nan\n    chunks = [c for c in [8, 16, 32, 64] if c <= v.size // 2]\n    if len(chunks) < 2: return np.nan\n    rs = []\n    for c in chunks:\n        u = (v.size // c) * c\n        sub = v[:u].reshape(-1, c); mu = sub.mean(axis=1, keepdims=True)\n        cs = (sub - mu).cumsum(axis=1); rng = cs.max(axis=1) - cs.min(axis=1)\n        sd = sub.std(axis=1, ddof=1); ok = sd > 0\n        if ok.sum() > 0:\n            rs.append(float((rng[ok] / sd[ok]).mean()))\n    if len(rs) < 2: return np.nan\n    x = np.log(np.array(chunks[:len(rs)], dtype=float)); y = np.log(np.array(rs, dtype=float))\n    return float(np.polyfit(x, y, 1)[0])\nh63 = r.rolling(QDAYS, min_periods=MDAYS).apply(_hr, raw=True); h252 = r.rolling(YDAYS, min_periods=QDAYS).apply(_hr, raw=True)\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()",
        "((h63 < 0.5) & (h252 > 0.5) & (close >= rmax - 1e-12)).astype(float).where(h63.notna() & h252.notna(), np.nan)")
    add("trend_slope_log_close_ts_21d", "Slope log-close 21d.",
        ("close",), "lc = _safe_log(close)", "_rolling_slope(lc, MDAYS)")
    add("trend_slope_log_close_ts_63d", "Slope log-close 63d.",
        ("close",), "lc = _safe_log(close)", "_rolling_slope(lc, QDAYS)")
    add("trend_slope_log_close_ts_252d", "Slope log-close 252d.",
        ("close",), "lc = _safe_log(close)", "_rolling_slope(lc, YDAYS)")
    add("trend_slope_short_minus_long_log_close",
        "Slope(21) - Slope(252) on log-close.",
        ("close",), "lc = _safe_log(close)", "_rolling_slope(lc, MDAYS) - _rolling_slope(lc, YDAYS)")
    add("trend_slope_sign_flip_indicator",
        "Sign(slope_21) != Sign(slope_252) on log-close.",
        ("close",), "lc = _safe_log(close)\ns1 = _rolling_slope(lc, MDAYS); s2 = _rolling_slope(lc, YDAYS)",
        "(np.sign(s1) != np.sign(s2)).astype(float).where(s1.notna() & s2.notna(), np.nan)")

    # ---- Block K (101-110): Cross-horizon composite scores ----
    add("ts_negative_alignment_score_252d",
        "Sum of: Sharpe(21)<0, Sortino(21)<0, |MaxDD21|/|MaxDD252|>1, slope21<slope252.",
        ("close",), "s1 = _sharpe_n(close, MDAYS); so1 = _sortino_n(close, MDAYS)\nd1 = -_drawdown_log_n(close, MDAYS); d3 = -_drawdown_log_n(close, YDAYS); rd = _safe_div(d1, d3)\nlc = _safe_log(close); sl1 = _rolling_slope(lc, MDAYS); sl3 = _rolling_slope(lc, YDAYS)",
        "((s1 < 0).astype(float) + (so1 < 0).astype(float) + (rd > 1.0).astype(float) + (sl1 < sl3).astype(float))")
    add("ts_negative_alignment_at_252h_indicator",
        "TS negative-alignment score = 4 AND close = 252d max.",
        ("close",), "s1 = _sharpe_n(close, MDAYS); so1 = _sortino_n(close, MDAYS)\nd1 = -_drawdown_log_n(close, MDAYS); d3 = -_drawdown_log_n(close, YDAYS); rd = _safe_div(d1, d3)\nlc = _safe_log(close); sl1 = _rolling_slope(lc, MDAYS); sl3 = _rolling_slope(lc, YDAYS)\ncnt = ((s1 < 0).astype(float) + (so1 < 0).astype(float) + (rd > 1.0).astype(float) + (sl1 < sl3).astype(float))\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()",
        "((cnt >= 4) & (close >= rmax - 1e-12)).astype(float).where(s1.notna() & so1.notna(), np.nan)")
    add("ts_inversion_count_at_high_252d",
        "Count of bars in 252d with (vol-TS inverted) AND (close=252d max).",
        ("close",), "r = _log_ret(close)\nv21 = r.rolling(MDAYS, min_periods=10).std(); v252 = r.rolling(YDAYS, min_periods=QDAYS).std()\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()\nev = ((v21 > v252) & (close >= rmax - 1e-12)).astype(float).where(v252.notna(), np.nan)",
        "ev.rolling(YDAYS, min_periods=QDAYS).sum()")
    add("ts_skew_kurt_alignment_bearish_indicator",
        "Skew(21)<-0.5 AND Kurt(21)>5 AND Sharpe(21)<0 - bearish distributional triple.",
        ("close",), "r = _log_ret(close)\nsk = r.rolling(MDAYS, min_periods=10).skew(); kt = r.rolling(MDAYS, min_periods=10).kurt(); sh = _sharpe_n(close, MDAYS)",
        "((sk < -0.5) & (kt > 5.0) & (sh < 0)).astype(float).where(sk.notna() & kt.notna() & sh.notna(), np.nan)")
    add("ts_multi_horizon_drawdown_ratio_increase_indicator",
        "MaxDD21/MaxDD63 AND MaxDD63/MaxDD252 both > 1 (DD accelerating across horizons).",
        ("close",), "d1 = -_drawdown_log_n(close, MDAYS); d2 = -_drawdown_log_n(close, QDAYS); d3 = -_drawdown_log_n(close, YDAYS)",
        "((_safe_div(d1, d2) > 1.0) & (_safe_div(d2, d3) > 1.0)).astype(float).where(d3.notna(), np.nan)")
    add("ts_liquidity_volatility_inverse_indicator",
        "Amihud(21)/Amihud(252) > 1.5 AND Vol(21)/Vol(252) > 1.5 - liquidity collapse + vol expansion.",
        ("close","volume"), "ar = _safe_div(_amihud_n(close, volume, MDAYS), _amihud_n(close, volume, YDAYS))\nr = _log_ret(close); vr = _safe_div(r.rolling(MDAYS, min_periods=10).std(), r.rolling(YDAYS, min_periods=QDAYS).std())",
        "((ar > 1.5) & (vr > 1.5)).astype(float).where(ar.notna() & vr.notna(), np.nan)")
    add("ts_average_z_score_5_metrics_252d",
        "Mean of z-scores of TS slopes for: vol, sharpe, sortino, skew, kurt over 252d.",
        ("close",), "r = _log_ret(close)\nv1 = r.rolling(MDAYS, min_periods=10).std(); v2 = r.rolling(QDAYS, min_periods=MDAYS).std(); v3 = r.rolling(YDAYS, min_periods=QDAYS).std()\nvs = _ts_slope(v1, v2, v3)\nzv = _rolling_zscore(vs, YDAYS)\nss = _sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS); zs = _rolling_zscore(ss, YDAYS)\nso = _sortino_n(close, MDAYS) - _sortino_n(close, YDAYS); zo = _rolling_zscore(so, YDAYS)\nsk = r.rolling(MDAYS, min_periods=10).skew() - r.rolling(YDAYS, min_periods=QDAYS).skew(); zk = _rolling_zscore(sk, YDAYS)\nkt = r.rolling(MDAYS, min_periods=10).kurt() - r.rolling(YDAYS, min_periods=QDAYS).kurt(); zt = _rolling_zscore(kt, YDAYS)",
        "(zv.fillna(0) + zs.fillna(0) + zo.fillna(0) + zk.fillna(0) + zt.fillna(0)) / 5.0")
    add("ts_term_structure_shape_change_speed_21d",
        "21-bar change in vol-TS log-slope.",
        ("close",), "r = _log_ret(close)\nv1 = r.rolling(MDAYS, min_periods=10).std(); v2 = r.rolling(QDAYS, min_periods=MDAYS).std(); v3 = r.rolling(YDAYS, min_periods=QDAYS).std()\nsl = _ts_slope(v1, v2, v3)",
        "sl - sl.shift(MDAYS)")
    add("ts_vol_amihud_combined_z_252d",
        "z(vol-TS-short minus long) + z(amihud-TS-short minus long).",
        ("close","volume"), "r = _log_ret(close)\nvd = r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std()\nad = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS)",
        "_rolling_zscore(vd, YDAYS).fillna(0) + _rolling_zscore(ad, YDAYS).fillna(0)")
    add("ts_inversion_persistence_63d",
        "Fraction of last 63d with (V21 > V252) inversion.",
        ("close",), "r = _log_ret(close)\nv21 = r.rolling(MDAYS, min_periods=10).std(); v252 = r.rolling(YDAYS, min_periods=QDAYS).std()",
        "(v21 > v252).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()")

    # ---- Block L (111-120): Cross-stream term-structures ----
    add("rsi_ts_21d", "RSI14 mean over 21d.",
        ("close",), "rsi = _rsi(close, 14)", "rsi.rolling(MDAYS, min_periods=10).mean()")
    add("rsi_ts_63d", "RSI14 mean over 63d.",
        ("close",), "rsi = _rsi(close, 14)", "rsi.rolling(QDAYS, min_periods=MDAYS).mean()")
    add("rsi_ts_252d", "RSI14 mean over 252d.",
        ("close",), "rsi = _rsi(close, 14)", "rsi.rolling(YDAYS, min_periods=QDAYS).mean()")
    add("rsi_ts_short_minus_long_drop",
        "RSI(21) - RSI(252).",
        ("close",), "rsi = _rsi(close, 14)", "rsi.rolling(MDAYS, min_periods=10).mean() - rsi.rolling(YDAYS, min_periods=QDAYS).mean()")
    add("rsi_ts_above_70_short_below_70_long_indicator",
        "RSI21>70 AND RSI252<70 (recent OB on top of cool long-term).",
        ("close",), "rsi = _rsi(close, 14)\nra = rsi.rolling(MDAYS, min_periods=10).mean(); rl = rsi.rolling(YDAYS, min_periods=QDAYS).mean()",
        "((ra > 70.0) & (rl < 70.0)).astype(float).where(ra.notna() & rl.notna(), np.nan)")
    add("macd_ts_21d", "MACD-line mean 21d.",
        ("close",), "m = _macd(close)", "m.rolling(MDAYS, min_periods=10).mean()")
    add("macd_ts_252d", "MACD-line mean 252d.",
        ("close",), "m = _macd(close)", "m.rolling(YDAYS, min_periods=QDAYS).mean()")
    add("macd_ts_short_minus_long",
        "MACD(21d-mean) - MACD(252d-mean).",
        ("close",), "m = _macd(close)", "m.rolling(MDAYS, min_periods=10).mean() - m.rolling(YDAYS, min_periods=QDAYS).mean()")
    add("obv_pct_change_ts_21d_minus_252d",
        "OBV-21d-pct-change - OBV-252d-pct-change.",
        ("close","volume"), "o = _obv(close, volume)", "o.pct_change(MDAYS) - o.pct_change(YDAYS)")
    add("range_norm_ts_21d_minus_252d",
        "Mean (H-L)/close 21d - mean 252d.",
        ("high","low","close"), "rn = _safe_div(high - low, close)", "rn.rolling(MDAYS, min_periods=10).mean() - rn.rolling(YDAYS, min_periods=QDAYS).mean()")

    # ---- Block M (121-130): Term-structure interactions ----
    add("vol_AND_amihud_AND_skew_TS_all_inverted_indicator",
        "Vol inversion AND Amihud inversion AND Skew inversion all bearish.",
        ("close","volume"), "r = _log_ret(close)\nv21 = r.rolling(MDAYS, min_periods=10).std(); v252 = r.rolling(YDAYS, min_periods=QDAYS).std()\na21 = _amihud_n(close, volume, MDAYS); a252 = _amihud_n(close, volume, YDAYS)\nsk21 = r.rolling(MDAYS, min_periods=10).skew(); sk252 = r.rolling(YDAYS, min_periods=QDAYS).skew()",
        "((v21 > v252) & (a21 > a252) & (sk21 < sk252)).astype(float).where(v252.notna() & a252.notna() & sk252.notna(), np.nan)")
    add("ts_inversion_count_3of5_at_252h_indicator",
        ">=3 of 5 TS inversions (vol, amihud, sharpe-drop, sortino-drop, skew-drop) AND close=252d max.",
        ("close","volume"), "r = _log_ret(close)\ni_v = (r.rolling(MDAYS, min_periods=10).std() > r.rolling(YDAYS, min_periods=QDAYS).std()).astype(float)\ni_a = (_amihud_n(close, volume, MDAYS) > _amihud_n(close, volume, YDAYS)).astype(float)\ni_s = (_sharpe_n(close, MDAYS) < _sharpe_n(close, YDAYS)).astype(float)\ni_so = (_sortino_n(close, MDAYS) < _sortino_n(close, YDAYS)).astype(float)\ni_sk = (r.rolling(MDAYS, min_periods=10).skew() < r.rolling(YDAYS, min_periods=QDAYS).skew()).astype(float)\ncnt = i_v + i_a + i_s + i_so + i_sk\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()",
        "((cnt >= 3) & (close >= rmax - 1e-12)).astype(float)")
    add("ts_inversion_count_4of5_indicator",
        ">=4 of 5 TS inversions simultaneously.",
        ("close","volume"), "r = _log_ret(close)\ni_v = (r.rolling(MDAYS, min_periods=10).std() > r.rolling(YDAYS, min_periods=QDAYS).std()).astype(float)\ni_a = (_amihud_n(close, volume, MDAYS) > _amihud_n(close, volume, YDAYS)).astype(float)\ni_s = (_sharpe_n(close, MDAYS) < _sharpe_n(close, YDAYS)).astype(float)\ni_so = (_sortino_n(close, MDAYS) < _sortino_n(close, YDAYS)).astype(float)\ni_sk = (r.rolling(MDAYS, min_periods=10).skew() < r.rolling(YDAYS, min_periods=QDAYS).skew()).astype(float)",
        "((i_v + i_a + i_s + i_so + i_sk) >= 4).astype(float).where(i_v.notna() & i_a.notna(), np.nan)")
    add("ts_inversion_count_all_5_indicator",
        "All 5 TS inversions simultaneously (extreme regime alignment).",
        ("close","volume"), "r = _log_ret(close)\ni_v = (r.rolling(MDAYS, min_periods=10).std() > r.rolling(YDAYS, min_periods=QDAYS).std()).astype(float)\ni_a = (_amihud_n(close, volume, MDAYS) > _amihud_n(close, volume, YDAYS)).astype(float)\ni_s = (_sharpe_n(close, MDAYS) < _sharpe_n(close, YDAYS)).astype(float)\ni_so = (_sortino_n(close, MDAYS) < _sortino_n(close, YDAYS)).astype(float)\ni_sk = (r.rolling(MDAYS, min_periods=10).skew() < r.rolling(YDAYS, min_periods=QDAYS).skew()).astype(float)",
        "((i_v + i_a + i_s + i_so + i_sk) >= 5).astype(float).where(i_v.notna() & i_a.notna(), np.nan)")
    add("ts_inversion_persistence_3of5_63d",
        "Fraction of last 63d with >=3 of 5 TS inversions.",
        ("close","volume"), "r = _log_ret(close)\ni_v = (r.rolling(MDAYS, min_periods=10).std() > r.rolling(YDAYS, min_periods=QDAYS).std()).astype(float)\ni_a = (_amihud_n(close, volume, MDAYS) > _amihud_n(close, volume, YDAYS)).astype(float)\ni_s = (_sharpe_n(close, MDAYS) < _sharpe_n(close, YDAYS)).astype(float)\ni_so = (_sortino_n(close, MDAYS) < _sortino_n(close, YDAYS)).astype(float)\ni_sk = (r.rolling(MDAYS, min_periods=10).skew() < r.rolling(YDAYS, min_periods=QDAYS).skew()).astype(float)\ncnt = i_v + i_a + i_s + i_so + i_sk\nind = (cnt >= 3).astype(float).where(i_v.notna() & i_a.notna(), np.nan)",
        "ind.rolling(QDAYS, min_periods=MDAYS).mean()")
    add("ts_4y_drawdown_ratio_252_vs_504",
        "MaxDD(252) / MaxDD(504) - recent drawdown depth vs 2yr baseline.",
        ("close",), "", "_safe_div(_drawdown_log_n(close, YDAYS), _drawdown_log_n(close, DDAYS_2Y))")
    add("ts_vol_at_high_relative_to_vol_at_low_252d",
        "Mean vol when close in top decile / mean vol when close in bottom decile over 252d.",
        ("close",), "r = _log_ret(close); v = r.rolling(MDAYS, min_periods=10).std()\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max(); rmin = close.rolling(YDAYS, min_periods=QDAYS).min()\npr = _safe_div(close - rmin, rmax - rmin)\nvh = v.where(pr > 0.9, np.nan); vl = v.where(pr < 0.1, np.nan)\nmh = vh.rolling(YDAYS, min_periods=QDAYS).mean(); ml = vl.rolling(YDAYS, min_periods=QDAYS).mean()",
        "_safe_div(mh, ml)")
    add("ts_sharpe_decay_rate_252d",
        "(Sharpe(252) - Sharpe(63)) / 63 - per-bar decay rate of Sharpe with horizon.",
        ("close",), "s3 = _sharpe_n(close, YDAYS); s2 = _sharpe_n(close, QDAYS)",
        "(s3 - s2) / float(QDAYS)")
    add("ts_drawdown_acceleration_index_252d",
        "(MaxDD21/MaxDD252) / (MaxDD63/MaxDD252) - acceleration ratio.",
        ("close",), "d1 = -_drawdown_log_n(close, MDAYS); d2 = -_drawdown_log_n(close, QDAYS); d3 = -_drawdown_log_n(close, YDAYS)\nr1 = _safe_div(d1, d3); r2 = _safe_div(d2, d3)",
        "_safe_div(r1, r2)")
    add("ts_distress_signal_composite_252d",
        "Z-sum of: vol-TS-shift + amihud-TS-shift + sharpe-degradation + skew-drop + DD-accel.",
        ("close","volume"), "r = _log_ret(close)\nvd = r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(); zv = _rolling_zscore(vd, YDAYS)\nad = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS); za = _rolling_zscore(ad, YDAYS)\nsd = -(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS)); zs = _rolling_zscore(sd, YDAYS)\nskd = -(r.rolling(MDAYS, min_periods=10).skew() - r.rolling(YDAYS, min_periods=QDAYS).skew()); zk = _rolling_zscore(skd, YDAYS)\nd1 = -_drawdown_log_n(close, MDAYS); d3 = -_drawdown_log_n(close, YDAYS); dr = _safe_div(d1, d3); zd = _rolling_zscore(dr, YDAYS)",
        "zv.fillna(0) + za.fillna(0) + zs.fillna(0) + zk.fillna(0) + zd.fillna(0)")

    # ---- Block N (131-140): Composite TS scores ----
    add("ts_distress_composite_above_p90_indicator",
        "TS distress composite > 252d-p90 indicator.",
        ("close","volume"), "r = _log_ret(close)\nvd = r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(); zv = _rolling_zscore(vd, YDAYS)\nad = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS); za = _rolling_zscore(ad, YDAYS)\nsd = -(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS)); zs = _rolling_zscore(sd, YDAYS)\nz = zv.fillna(0) + za.fillna(0) + zs.fillna(0)\np90 = z.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)",
        "(z > p90).astype(float).where(p90.notna(), np.nan)")
    add("ts_distress_composite_at_252h_indicator",
        "TS distress composite > 252d-p90 AND close = 252d max.",
        ("close","volume"), "r = _log_ret(close)\nvd = r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(); zv = _rolling_zscore(vd, YDAYS)\nad = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS); za = _rolling_zscore(ad, YDAYS)\nsd = -(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS)); zs = _rolling_zscore(sd, YDAYS)\nz = zv.fillna(0) + za.fillna(0) + zs.fillna(0)\np90 = z.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()",
        "((z > p90) & (close >= rmax - 1e-12)).astype(float).where(p90.notna(), np.nan)")
    add("ts_distress_persistence_63d",
        "Fraction of last 63d with TS distress > 252d-mean.",
        ("close","volume"), "r = _log_ret(close)\nvd = r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(); zv = _rolling_zscore(vd, YDAYS)\nad = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS); za = _rolling_zscore(ad, YDAYS)\nsd = -(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS)); zs = _rolling_zscore(sd, YDAYS)\nz = zv.fillna(0) + za.fillna(0) + zs.fillna(0); mu = z.rolling(YDAYS, min_periods=QDAYS).mean()\nind = (z > mu).astype(float).where(mu.notna(), np.nan)",
        "ind.rolling(QDAYS, min_periods=MDAYS).mean()")
    add("ts_distress_acceleration_21d",
        "21-bar change in TS distress composite.",
        ("close","volume"), "r = _log_ret(close)\nvd = r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(); zv = _rolling_zscore(vd, YDAYS)\nad = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS); za = _rolling_zscore(ad, YDAYS)\nsd = -(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS)); zs = _rolling_zscore(sd, YDAYS)\nz = zv.fillna(0) + za.fillna(0) + zs.fillna(0)",
        "z - z.shift(MDAYS)")
    add("ts_distress_max_in_63d",
        "Max TS distress in last 63d.",
        ("close","volume"), "r = _log_ret(close)\nvd = r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(); zv = _rolling_zscore(vd, YDAYS)\nad = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS); za = _rolling_zscore(ad, YDAYS)\nsd = -(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS)); zs = _rolling_zscore(sd, YDAYS)\nz = zv.fillna(0) + za.fillna(0) + zs.fillna(0)",
        "z.rolling(QDAYS, min_periods=MDAYS).max()")
    add("ts_distress_bars_since_above_p90_capped",
        "Bars since TS distress was last >252d-p90 (capped 252).",
        ("close","volume"), "r = _log_ret(close)\nvd = r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(); zv = _rolling_zscore(vd, YDAYS)\nad = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS); za = _rolling_zscore(ad, YDAYS)\nsd = -(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS)); zs = _rolling_zscore(sd, YDAYS)\nz = zv.fillna(0) + za.fillna(0) + zs.fillna(0); p90 = z.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\nev = (z > p90).astype(float).where(p90.notna(), np.nan)",
        "_bars_since_last_event(ev).clip(upper=float(YDAYS))")
    add("ts_distress_count_above_p90_in_252d",
        "Count of bars in 252d with TS distress > 252d-p90.",
        ("close","volume"), "r = _log_ret(close)\nvd = r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(); zv = _rolling_zscore(vd, YDAYS)\nad = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS); za = _rolling_zscore(ad, YDAYS)\nsd = -(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS)); zs = _rolling_zscore(sd, YDAYS)\nz = zv.fillna(0) + za.fillna(0) + zs.fillna(0); p90 = z.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\nev = (z > p90).astype(float).where(p90.notna(), np.nan)",
        "ev.rolling(YDAYS, min_periods=QDAYS).sum()")
    add("ts_distress_count_at_high_in_252d",
        "Count of bars in 252d where TS distress > 252d-p90 AND close=252d max.",
        ("close","volume"), "r = _log_ret(close)\nvd = r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(); zv = _rolling_zscore(vd, YDAYS)\nad = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS); za = _rolling_zscore(ad, YDAYS)\nsd = -(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS)); zs = _rolling_zscore(sd, YDAYS)\nz = zv.fillna(0) + za.fillna(0) + zs.fillna(0); p90 = z.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()\nev = ((z > p90) & (close >= rmax - 1e-12)).astype(float)",
        "ev.rolling(YDAYS, min_periods=QDAYS).sum()")
    add("ts_distress_minus_long_term_mean_504d",
        "TS distress composite minus 504d-mean of itself.",
        ("close","volume"), "r = _log_ret(close)\nvd = r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(); zv = _rolling_zscore(vd, YDAYS)\nad = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS); za = _rolling_zscore(ad, YDAYS)\nsd = -(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS)); zs = _rolling_zscore(sd, YDAYS)\nz = zv.fillna(0) + za.fillna(0) + zs.fillna(0); mu = z.rolling(DDAYS_2Y, min_periods=YDAYS).mean()",
        "z - mu")
    add("ts_inversion_intensity_composite_z_score",
        "z-sum of TS-inversion counts: vol, amihud, sharpe (each as 21d minus 252d).",
        ("close","volume"), "r = _log_ret(close)\ni1 = r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std()\ni2 = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS)\ni3 = -(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS))",
        "_rolling_zscore(i1, YDAYS).fillna(0) + _rolling_zscore(i2, YDAYS).fillna(0) + _rolling_zscore(i3, YDAYS).fillna(0)")

    # ---- Block O (141-150): Master scores ----
    add("master_term_structure_inversion_score_252d",
        "z-sum of TS-inversion magnitudes across vol/amihud/sharpe/sortino/skew over 252d.",
        ("close","volume"), "r = _log_ret(close)\nz1 = _rolling_zscore(r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(), YDAYS)\nz2 = _rolling_zscore(_amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS), YDAYS)\nz3 = -_rolling_zscore(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS), YDAYS)\nz4 = -_rolling_zscore(_sortino_n(close, MDAYS) - _sortino_n(close, YDAYS), YDAYS)\nz5 = -_rolling_zscore(r.rolling(MDAYS, min_periods=10).skew() - r.rolling(YDAYS, min_periods=QDAYS).skew(), YDAYS)",
        "z1.fillna(0) + z2.fillna(0) + z3.fillna(0) + z4.fillna(0) + z5.fillna(0)")
    add("master_ts_inversion_at_252h_indicator",
        "Master TS-inversion score > 252d-p90 AND close=252d max.",
        ("close","volume"), "r = _log_ret(close)\nz = (_rolling_zscore(r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(), YDAYS).fillna(0)\n+ _rolling_zscore(_amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS), YDAYS).fillna(0)\n- _rolling_zscore(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS), YDAYS).fillna(0))\np90 = z.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()",
        "((z > p90) & (close >= rmax - 1e-12)).astype(float).where(p90.notna(), np.nan)")
    add("ts_compound_blowoff_risk_score_252d",
        "Mayer*MasterTSInversion - extension * regime-fragility composite.",
        ("close","volume"), "mayer = _safe_div(close, _sma(close, 200))\nr = _log_ret(close)\nz = (_rolling_zscore(r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(), YDAYS).fillna(0)\n+ _rolling_zscore(_amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS), YDAYS).fillna(0))",
        "mayer * z")
    add("ts_compound_blowoff_at_252h_above_p90_indicator",
        "Compound blowoff risk > 252d-p90 AND close = 252d max.",
        ("close","volume"), "mayer = _safe_div(close, _sma(close, 200))\nr = _log_ret(close)\nz = (_rolling_zscore(r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(), YDAYS).fillna(0)\n+ _rolling_zscore(_amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS), YDAYS).fillna(0))\ncomp = mayer * z\np90 = comp.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()",
        "((comp > p90) & (close >= rmax - 1e-12)).astype(float).where(p90.notna(), np.nan)")
    add("ts_5horizon_vol_dispersion_252d",
        "Std of vol across horizons {5,21,63,126,252} - vol disagreement across horizons.",
        ("close",), "r = _log_ret(close)\nv5 = r.rolling(5, min_periods=3).std(); v21 = r.rolling(MDAYS, min_periods=10).std(); v63 = r.rolling(QDAYS, min_periods=MDAYS).std(); v126 = r.rolling(126, min_periods=QDAYS).std(); v252 = r.rolling(YDAYS, min_periods=QDAYS).std()\ndf = pd.concat([v5.rename('a'), v21.rename('b'), v63.rename('c'), v126.rename('d'), v252.rename('e')], axis=1)",
        "df.std(axis=1)")
    add("ts_5horizon_vol_max_minus_min_252d",
        "Range of vol across 5 horizons.",
        ("close",), "r = _log_ret(close)\nv5 = r.rolling(5, min_periods=3).std(); v21 = r.rolling(MDAYS, min_periods=10).std(); v63 = r.rolling(QDAYS, min_periods=MDAYS).std(); v126 = r.rolling(126, min_periods=QDAYS).std(); v252 = r.rolling(YDAYS, min_periods=QDAYS).std()\ndf = pd.concat([v5.rename('a'), v21.rename('b'), v63.rename('c'), v126.rename('d'), v252.rename('e')], axis=1)",
        "df.max(axis=1) - df.min(axis=1)")
    add("ts_5horizon_close_position_range",
        "Range of (close/SMA_n - 1) across n in {20, 50, 100, 200} - extension dispersion.",
        ("close",), "e1 = _safe_div(close, _sma(close, 20)) - 1.0; e2 = _safe_div(close, _sma(close, 50)) - 1.0; e3 = _safe_div(close, _sma(close, 100)) - 1.0; e4 = _safe_div(close, _sma(close, 200)) - 1.0\ndf = pd.concat([e1.rename('a'), e2.rename('b'), e3.rename('c'), e4.rename('d')], axis=1)",
        "df.max(axis=1) - df.min(axis=1)")
    add("ts_blowoff_imminence_composite_score_252d",
        "Combined: Mayer * (vol-TS-shift z + amihud-TS-shift z) * (close/252d-max).",
        ("close","volume"), "mayer = _safe_div(close, _sma(close, 200))\nr = _log_ret(close)\nz1 = _rolling_zscore(r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(), YDAYS)\nz2 = _rolling_zscore(_amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS), YDAYS)\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max(); ratio = _safe_div(close, rmax)",
        "mayer * (z1.fillna(0) + z2.fillna(0)) * ratio")
    add("ts_extreme_alignment_4metrics_at_252h_indicator",
        "Vol-TS shift, Amihud shift, Sharpe drop, Skew drop all simultaneously in top-quartile AND close=252d max.",
        ("close","volume"), "r = _log_ret(close)\nz1 = _rolling_zscore(r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(), YDAYS)\nz2 = _rolling_zscore(_amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS), YDAYS)\nz3 = -_rolling_zscore(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS), YDAYS)\nz4 = -_rolling_zscore(r.rolling(MDAYS, min_periods=10).skew() - r.rolling(YDAYS, min_periods=QDAYS).skew(), YDAYS)\nrmax = close.rolling(YDAYS, min_periods=QDAYS).max()",
        "((z1 > 0.674) & (z2 > 0.674) & (z3 > 0.674) & (z4 > 0.674) & (close >= rmax - 1e-12)).astype(float).where(z1.notna() & z2.notna() & z3.notna() & z4.notna(), np.nan)")
    add("master_ts_term_structure_signature_score_252d",
        "Z-sum of 7 TS shifts: vol, amihud, sharpe, sortino, skew, kurt, slope - master TS regime score.",
        ("close","volume"), "r = _log_ret(close)\nz1 = _rolling_zscore(r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(), YDAYS)\nz2 = _rolling_zscore(_amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS), YDAYS)\nz3 = -_rolling_zscore(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS), YDAYS)\nz4 = -_rolling_zscore(_sortino_n(close, MDAYS) - _sortino_n(close, YDAYS), YDAYS)\nz5 = -_rolling_zscore(r.rolling(MDAYS, min_periods=10).skew() - r.rolling(YDAYS, min_periods=QDAYS).skew(), YDAYS)\nz6 = _rolling_zscore(r.rolling(MDAYS, min_periods=10).kurt() - r.rolling(YDAYS, min_periods=QDAYS).kurt(), YDAYS)\nlc = _safe_log(close); z7 = -_rolling_zscore(_rolling_slope(lc, MDAYS) - _rolling_slope(lc, YDAYS), YDAYS)",
        "z1.fillna(0) + z2.fillna(0) + z3.fillna(0) + z4.fillna(0) + z5.fillna(0) + z6.fillna(0) + z7.fillna(0)")

    return F


def f59_features():
    return _f59()


def main():
    fams = [(F57_META, f57_features(), COMMON_HELPERS),
            (F58_META, f58_features(), COMMON_HELPERS + CPRT_HELPERS),
            (F59_META, f59_features(), COMMON_HELPERS + CHTS_HELPERS)]
    for meta, feats, hh in fams:
        print(f"  {meta['name']}: {len(feats)} features")
        if len(feats) != 150:
            print(f"  ERROR: {meta['name']} has {len(feats)} != 150")
            return
        emit(meta, feats, hh)
    print("OK")


if __name__ == "__main__":
    main()
