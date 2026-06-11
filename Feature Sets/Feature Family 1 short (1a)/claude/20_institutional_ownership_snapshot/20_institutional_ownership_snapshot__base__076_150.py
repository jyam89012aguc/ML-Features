"""institutional_ownership_snapshot base features 076-150 — Pipeline 1a-inverse short-side blowup family.

Second half of 150 distinct hypotheses; pairs with __base__001_075.py.
Inputs: Sharadar SF3/SF3A institutional aggregates plus SF1 share counts and
quarter-end SEP marketcap/close. Cadence is quarterly. PIT-clean: right-anchored
rolling with explicit min_periods, no centered windows, no .shift(-N).
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


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


def _qoq_pct(s):
    prev = s.shift(1)
    return _safe_div(s - prev, prev.abs())


def _yoy_pct(s):
    prev = s.shift(4)
    return _safe_div(s - prev, prev.abs())


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
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _max_consec_neg_streak(diffs, window):
    def _f(w):
        if np.isnan(w).all():
            return np.nan
        best = 0
        cur = 0
        for v in w:
            if not np.isnan(v) and v < 0:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    return diffs.rolling(window, min_periods=2).apply(_f, raw=True)


def _quarters_since_expanding_max(s):
    def _f(arr):
        last = arr[-1]
        if np.isnan(last):
            return np.nan
        idx = np.nanargmax(arr)
        return float(len(arr) - 1 - idx)
    return s.expanding(min_periods=1).apply(_f, raw=True)


def _consec_neg_streak_current(diffs):
    neg = (diffs < 0).astype(float)
    grp = (neg == 0).cumsum()
    return neg.groupby(grp).cumsum()


def _consec_pos_streak_current(diffs):
    pos = (diffs > 0).astype(float)
    grp = (pos == 0).cumsum()
    return pos.groupby(grp).cumsum()


def _rolling_corr(a, b, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return a.rolling(window, min_periods=min_periods).corr(b)


def _rolling_resid_loglog_slope(num, den, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    ln_num = _safe_log(num)
    ln_den = _safe_log(den)
    def _resid(arr_y, arr_x):
        if np.isnan(arr_y).any() or np.isnan(arr_x).any():
            yv = arr_y; xv = arr_x
            mask = ~(np.isnan(yv) | np.isnan(xv))
            if mask.sum() < min_periods:
                return np.nan
            yv = yv[mask]; xv = xv[mask]
        else:
            yv = arr_y; xv = arr_x
        xm = xv.mean(); ym = yv.mean()
        denom = ((xv - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        b = ((xv - xm) * (yv - ym)).sum() / denom
        a = ym - b * xm
        pred_last = a + b * arr_x[-1]
        return float(arr_y[-1] - pred_last)
    out = pd.Series(np.nan, index=num.index).astype(float)
    yv = ln_num.values
    xv = ln_den.values
    for i in range(len(out)):
        lo = max(0, i - window + 1)
        chunk_y = yv[lo:i + 1]
        chunk_x = xv[lo:i + 1]
        if len(chunk_y) < min_periods:
            continue
        out.iat[i] = _resid(chunk_y, chunk_x)
    return out


# ============================================================
#                    FEATURES 076-150
# ============================================================

def f20_iosp_076_inst_puts_qoq_pct(inst_puts: pd.Series) -> pd.Series:
    """QoQ percent change in institutional puts held."""
    return _qoq_pct(inst_puts)


def f20_iosp_077_inst_calls_yoy_pct(inst_calls: pd.Series) -> pd.Series:
    """YoY percent change in institutional calls held."""
    return _yoy_pct(inst_calls)


def f20_iosp_078_inst_puts_yoy_pct(inst_puts: pd.Series) -> pd.Series:
    """YoY percent change in institutional puts held."""
    return _yoy_pct(inst_puts)


def f20_iosp_079_put_concentration_per_investor(inst_puts: pd.Series, inst_investors: pd.Series) -> pd.Series:
    """Institutional puts divided by investor count — puts per holder."""
    return _safe_div(inst_puts, inst_investors)


def f20_iosp_080_call_concentration_per_investor(inst_calls: pd.Series, inst_investors: pd.Series) -> pd.Series:
    """Institutional calls divided by investor count — calls per holder."""
    return _safe_div(inst_calls, inst_investors)


def f20_iosp_081_options_skew_8q_zscore(inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """8q z-score of institutional put-call skew."""
    skew = _safe_div(inst_puts - inst_calls, inst_puts + inst_calls)
    return _rolling_zscore(skew, 8)


def f20_iosp_082_put_buildup_intensity_4q(inst_puts: pd.Series, inst_units: pd.Series) -> pd.Series:
    """(puts - puts.shift(4)) / |units.shift(4)| — put buildup normalized to units."""
    return _safe_div(inst_puts - inst_puts.shift(4), inst_units.shift(4).abs())


def f20_iosp_083_call_unwinding_intensity_4q(inst_calls: pd.Series, inst_units: pd.Series) -> pd.Series:
    """-(calls - calls.shift(4)) / |units.shift(4)| — call unwinding pressure."""
    return -_safe_div(inst_calls - inst_calls.shift(4), inst_units.shift(4).abs())


def f20_iosp_084_protective_put_intensity(inst_puts: pd.Series, inst_units: pd.Series) -> pd.Series:
    """Puts divided by units — protective hedge intensity."""
    return _safe_div(inst_puts, inst_units)


def f20_iosp_085_options_skew_jerk(inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Second difference of institutional put-call skew — skew jerk."""
    skew = _safe_div(inst_puts - inst_calls, inst_puts + inst_calls)
    return skew.diff().diff()


def f20_iosp_086_peak_inst_units_to_current(inst_units: pd.Series) -> pd.Series:
    """Expanding max of units / current units — overhang vs all-time peak."""
    peak = inst_units.expanding(min_periods=1).max()
    return _safe_div(peak, inst_units)


def f20_iosp_087_drawdown_from_peak_units(inst_units: pd.Series) -> pd.Series:
    """(units - expanding_max) / expanding_max — drawdown of unit ownership from peak."""
    peak = inst_units.expanding(min_periods=1).max()
    return _safe_div(inst_units - peak, peak)


def f20_iosp_088_drawdown_from_peak_investors(inst_investors: pd.Series) -> pd.Series:
    """Drawdown of investor count from expanding max."""
    peak = inst_investors.expanding(min_periods=1).max()
    return _safe_div(inst_investors - peak, peak)


def f20_iosp_089_drawdown_from_peak_value(inst_value: pd.Series) -> pd.Series:
    """Drawdown of institutional value from expanding max."""
    peak = inst_value.expanding(min_periods=1).max()
    return _safe_div(inst_value - peak, peak)


def f20_iosp_090_quarters_since_peak_units(inst_units: pd.Series) -> pd.Series:
    """Quarters since expanding-max of institutional units."""
    return _quarters_since_expanding_max(inst_units)


def f20_iosp_091_quarters_since_peak_investors(inst_investors: pd.Series) -> pd.Series:
    """Quarters since expanding-max of investor count."""
    return _quarters_since_expanding_max(inst_investors)


def f20_iosp_092_quarters_since_peak_value(inst_value: pd.Series) -> pd.Series:
    """Quarters since expanding-max of institutional dollar value."""
    return _quarters_since_expanding_max(inst_value)


def f20_iosp_093_units_share_of_8q_max(inst_units: pd.Series) -> pd.Series:
    """Units divided by 8q rolling max — share of recent peak."""
    rmax = inst_units.rolling(8, min_periods=3).max()
    return _safe_div(inst_units, rmax)


def f20_iosp_094_investors_share_of_8q_max(inst_investors: pd.Series) -> pd.Series:
    """Investor count divided by 8q rolling max — share of recent peak."""
    rmax = inst_investors.rolling(8, min_periods=3).max()
    return _safe_div(inst_investors, rmax)


def f20_iosp_095_consec_quarters_units_decline(inst_units: pd.Series) -> pd.Series:
    """Length of current consecutive QoQ-decline streak in units."""
    return _consec_neg_streak_current(inst_units.diff())


def f20_iosp_096_consec_quarters_investors_decline(inst_investors: pd.Series) -> pd.Series:
    """Length of current consecutive QoQ-decline streak in investor count."""
    return _consec_neg_streak_current(inst_investors.diff())


def f20_iosp_097_abandonment_intensity_4q(inst_investors: pd.Series) -> pd.Series:
    """1 - investors / 4q rolling max — abandonment intensity."""
    rmax = inst_investors.rolling(4, min_periods=2).max()
    return 1.0 - _safe_div(inst_investors, rmax)


def f20_iosp_098_abandonment_intensity_8q(inst_investors: pd.Series) -> pd.Series:
    """1 - investors / 8q rolling max — longer-horizon abandonment intensity."""
    rmax = inst_investors.rolling(8, min_periods=3).max()
    return 1.0 - _safe_div(inst_investors, rmax)


def f20_iosp_099_units_below_4q_avg_persistence_8q(inst_units: pd.Series) -> pd.Series:
    """8q mean of indicator (units < 4q rolling mean)."""
    avg4 = inst_units.rolling(4, min_periods=2).mean()
    flag = (inst_units < avg4).astype(float)
    return flag.rolling(8, min_periods=3).mean()


def f20_iosp_100_investors_below_4q_avg_persistence_8q(inst_investors: pd.Series) -> pd.Series:
    """8q mean of indicator (investors < 4q rolling mean)."""
    avg4 = inst_investors.rolling(4, min_periods=2).mean()
    flag = (inst_investors < avg4).astype(float)
    return flag.rolling(8, min_periods=3).mean()


def f20_iosp_101_units_negative_qoq_count_8q(inst_units: pd.Series) -> pd.Series:
    """Count of negative QoQ units changes over last 8q."""
    flag = (inst_units.diff() < 0).astype(float)
    return flag.rolling(8, min_periods=3).sum()


def f20_iosp_102_investors_negative_qoq_count_8q(inst_investors: pd.Series) -> pd.Series:
    """Count of negative QoQ investor-count changes over last 8q."""
    flag = (inst_investors.diff() < 0).astype(float)
    return flag.rolling(8, min_periods=3).sum()


def f20_iosp_103_units_qoq_negative_ema(inst_units: pd.Series) -> pd.Series:
    """EWM(span=4) of negative QoQ unit diffs (positives clipped to zero)."""
    diffs = inst_units.diff().clip(upper=0.0)
    return diffs.ewm(span=4, adjust=False, min_periods=2).mean()


def f20_iosp_104_dispersion_widening_count_8q(inst_value: pd.Series, inst_investors: pd.Series) -> pd.Series:
    """8q count of bars where avg position value drops AND investor count flat-or-down."""
    avg = _safe_div(inst_value, inst_investors)
    flag = ((avg.diff() < 0) & (inst_investors.diff() <= 0)).astype(float)
    return flag.rolling(8, min_periods=3).sum()


def f20_iosp_105_fast_money_exit_proxy(inst_units: pd.Series, inst_investors: pd.Series) -> pd.Series:
    """Indicator where investors qoq<0 AND units qoq<0 simultaneously."""
    return ((inst_investors.diff() < 0) & (inst_units.diff() < 0)).astype(float)


def f20_iosp_106_consolidating_exit_proxy(inst_units: pd.Series, inst_investors: pd.Series) -> pd.Series:
    """Indicator where investors qoq<0 AND |units qoq pct|<2% — holders leaving without dumping."""
    units_qoq = _qoq_pct(inst_units)
    return ((inst_investors.diff() < 0) & (units_qoq.abs() < 0.02)).astype(float)


def f20_iosp_107_retail_capture_proxy(inst_units: pd.Series, inst_investors: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Indicator where investors qoq>0 AND inst_pct_of_float qoq<0 — incoming holders, falling share."""
    pct = _safe_div(inst_units, sharesbas)
    return ((inst_investors.diff() > 0) & (pct.diff() < 0)).astype(float)


def f20_iosp_108_unit_value_divergence_indicator(inst_units: pd.Series, inst_value: pd.Series) -> pd.Series:
    """1 when sign(units.qoq) ≠ sign(value.qoq) — flow/valuation divergence flag."""
    su = np.sign(inst_units.diff())
    sv = np.sign(inst_value.diff())
    return (su != sv).astype(float)


def f20_iosp_109_holder_loss_rate_4q(inst_investors: pd.Series) -> pd.Series:
    """4q mean of negative QoQ investor changes (positives clipped to zero)."""
    diffs = inst_investors.diff().clip(upper=0.0)
    return diffs.rolling(4, min_periods=2).mean()


def f20_iosp_110_holder_gain_rate_4q(inst_investors: pd.Series) -> pd.Series:
    """4q mean of positive QoQ investor changes (negatives clipped to zero)."""
    diffs = inst_investors.diff().clip(lower=0.0)
    return diffs.rolling(4, min_periods=2).mean()


def f20_iosp_111_inst_value_to_marketcap_qoq_pct(inst_value: pd.Series, marketcap: pd.Series) -> pd.Series:
    """QoQ percent change in inst_value/marketcap ratio."""
    r = _safe_div(inst_value, marketcap)
    return _qoq_pct(r)


def f20_iosp_112_inst_value_to_marketcap_yoy_pct(inst_value: pd.Series, marketcap: pd.Series) -> pd.Series:
    """YoY percent change in inst_value/marketcap ratio."""
    r = _safe_div(inst_value, marketcap)
    return _yoy_pct(r)


def f20_iosp_113_inst_value_to_marketcap_zscore_8q(inst_value: pd.Series, marketcap: pd.Series) -> pd.Series:
    """8q z-score of inst_value/marketcap ratio."""
    r = _safe_div(inst_value, marketcap)
    return _rolling_zscore(r, 8)


def f20_iosp_114_inst_value_marketcap_residual_8q(inst_value: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Last-bar residual of log(inst_value) regressed on log(marketcap) over 8q."""
    return _rolling_resid_loglog_slope(inst_value, marketcap, 8)


def f20_iosp_115_ownership_price_corr_8q(inst_units: pd.Series, close: pd.Series) -> pd.Series:
    """8q rolling correlation between inst_units QoQ and close QoQ."""
    return _rolling_corr(inst_units.diff(), close.diff(), 8)


def f20_iosp_116_ownership_marketcap_corr_4q(inst_units: pd.Series, marketcap: pd.Series) -> pd.Series:
    """4q rolling correlation between inst_units QoQ and marketcap QoQ."""
    return _rolling_corr(inst_units.diff(), marketcap.diff(), 4)


def f20_iosp_117_value_growth_minus_mcap_growth_qoq(inst_value: pd.Series, marketcap: pd.Series) -> pd.Series:
    """inst_value QoQ pct minus marketcap QoQ pct."""
    return _qoq_pct(inst_value) - _qoq_pct(marketcap)


def f20_iosp_118_value_growth_minus_mcap_growth_yoy(inst_value: pd.Series, marketcap: pd.Series) -> pd.Series:
    """inst_value YoY pct minus marketcap YoY pct."""
    return _yoy_pct(inst_value) - _yoy_pct(marketcap)


def f20_iosp_119_implied_price_stale_signal(inst_value: pd.Series, inst_units: pd.Series, close: pd.Series) -> pd.Series:
    """(implied institutional price)/close - 1 — staleness vs market."""
    impl = _safe_div(inst_value, inst_units)
    return _safe_div(impl, close) - 1.0


def f20_iosp_120_implied_price_yoy_pct(inst_value: pd.Series, inst_units: pd.Series) -> pd.Series:
    """YoY percent change in implied institutional price."""
    impl = _safe_div(inst_value, inst_units)
    return _yoy_pct(impl)


def f20_iosp_121_units_normalized_by_mcap_change(inst_units: pd.Series, marketcap: pd.Series) -> pd.Series:
    """inst_units QoQ pct divided by marketcap QoQ pct (eps-safe)."""
    u = _qoq_pct(inst_units)
    m = _qoq_pct(marketcap)
    return _safe_div(u, m + 1.0e-12)


def f20_iosp_122_value_per_investor_to_mcap_per_share(inst_value: pd.Series, inst_investors: pd.Series, marketcap: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """(value/investors) / (marketcap/sharesbas) — per-holder dollar exposure vs per-share price."""
    num = _safe_div(inst_value, inst_investors)
    den = _safe_div(marketcap, sharesbas)
    return _safe_div(num, den)


def f20_iosp_123_inst_pct_zscore_12q(inst_units: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """12q rolling z-score of inst_pct_of_float."""
    pct = _safe_div(inst_units, sharesbas)
    return _rolling_zscore(pct, 12)


def f20_iosp_124_inst_pct_4q_change_pct(inst_units: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """4q (1y) percent change in inst_pct_of_float."""
    pct = _safe_div(inst_units, sharesbas)
    prev = pct.shift(4)
    return _safe_div(pct - prev, prev.abs())


def f20_iosp_125_inst_pct_8q_change_pct(inst_units: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """8q (2y) percent change in inst_pct_of_float."""
    pct = _safe_div(inst_units, sharesbas)
    prev = pct.shift(8)
    return _safe_div(pct - prev, prev.abs())


def f20_iosp_126_inst_value_mcap_share_8q_min(inst_value: pd.Series, marketcap: pd.Series) -> pd.Series:
    """8q rolling min of inst_value/marketcap."""
    r = _safe_div(inst_value, marketcap)
    return r.rolling(8, min_periods=3).min()


def f20_iosp_127_inst_value_mcap_share_8q_max(inst_value: pd.Series, marketcap: pd.Series) -> pd.Series:
    """8q rolling max of inst_value/marketcap."""
    r = _safe_div(inst_value, marketcap)
    return r.rolling(8, min_periods=3).max()


def f20_iosp_128_inst_value_share_collapse_from_8q_max(inst_value: pd.Series, marketcap: pd.Series) -> pd.Series:
    """(val/mcap) / (val/mcap).rolling(8).max() - 1 — drawdown from recent share peak."""
    r = _safe_div(inst_value, marketcap)
    rmax = r.rolling(8, min_periods=3).max()
    return _safe_div(r, rmax) - 1.0


def f20_iosp_129_unit_growth_mcap_growth_divergence_8q(inst_units: pd.Series, marketcap: pd.Series) -> pd.Series:
    """8q mean of indicator (sign(units.qoq) ≠ sign(marketcap.qoq))."""
    su = np.sign(inst_units.diff())
    sm = np.sign(marketcap.diff())
    flag = (su != sm).astype(float)
    return flag.rolling(8, min_periods=3).mean()


def f20_iosp_130_value_growth_mcap_growth_corr_8q(inst_value: pd.Series, marketcap: pd.Series) -> pd.Series:
    """8q rolling correlation between inst_value QoQ and marketcap QoQ."""
    return _rolling_corr(inst_value.diff(), marketcap.diff(), 8)


def f20_iosp_131_inst_units_max_consec_negative_qoq_8q(inst_units: pd.Series) -> pd.Series:
    """Longest consecutive negative-QoQ unit streak inside last 8q."""
    return _max_consec_neg_streak(inst_units.diff(), 8)


def f20_iosp_132_inst_investors_max_consec_negative_qoq_8q(inst_investors: pd.Series) -> pd.Series:
    """Longest consecutive negative-QoQ investor-count streak inside last 8q."""
    return _max_consec_neg_streak(inst_investors.diff(), 8)


def f20_iosp_133_inst_value_max_consec_negative_qoq_8q(inst_value: pd.Series) -> pd.Series:
    """Longest consecutive negative-QoQ inst-value streak inside last 8q."""
    return _max_consec_neg_streak(inst_value.diff(), 8)


def f20_iosp_134_inst_pct_yoy_negative_streak(inst_units: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Consecutive quarters where YoY inst_pct change is negative."""
    pct = _safe_div(inst_units, sharesbas)
    return _consec_neg_streak_current(pct.diff(4))


def f20_iosp_135_inst_pct_qoq_negative_streak(inst_units: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Consecutive quarters where QoQ inst_pct change is negative."""
    pct = _safe_div(inst_units, sharesbas)
    return _consec_neg_streak_current(pct.diff())


def f20_iosp_136_ownership_volatility_units_zscore_12q(inst_units: pd.Series) -> pd.Series:
    """12q std of QoQ pct in units, then z-scored within 24q."""
    qp = _qoq_pct(inst_units)
    vol = qp.rolling(12, min_periods=4).std()
    return _rolling_zscore(vol, 24)


def f20_iosp_137_ownership_volatility_investors_zscore_12q(inst_investors: pd.Series) -> pd.Series:
    """12q std of QoQ pct in investors, then z-scored within 24q."""
    qp = _qoq_pct(inst_investors)
    vol = qp.rolling(12, min_periods=4).std()
    return _rolling_zscore(vol, 24)


def f20_iosp_138_ownership_volatility_value_zscore_12q(inst_value: pd.Series) -> pd.Series:
    """12q std of QoQ pct in inst_value, then z-scored within 24q."""
    qp = _qoq_pct(inst_value)
    vol = qp.rolling(12, min_periods=4).std()
    return _rolling_zscore(vol, 24)


def f20_iosp_139_ownership_cohort_collapse_8q(inst_units: pd.Series, inst_investors: pd.Series, inst_value: pd.Series) -> pd.Series:
    """8q mean of indicator (units.qoq<0 AND investors.qoq<0 AND value.qoq<0)."""
    flag = ((inst_units.diff() < 0) & (inst_investors.diff() < 0) & (inst_value.diff() < 0)).astype(float)
    return flag.rolling(8, min_periods=3).mean()


def f20_iosp_140_options_hedge_buildup_streak(inst_puts: pd.Series) -> pd.Series:
    """Length of current consecutive QoQ-positive streak in inst_puts."""
    return _consec_pos_streak_current(inst_puts.diff())


def f20_iosp_141_options_hedge_acceleration_indicator(inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """1 when puts.qoq.diff()>0 AND skew.diff()>0 — accelerating bearish options posture."""
    skew = _safe_div(inst_puts - inst_calls, inst_puts + inst_calls)
    puts_jerk = inst_puts.diff().diff()
    return ((puts_jerk > 0) & (skew.diff() > 0)).astype(float)


def f20_iosp_142_block_holder_exit_indicator(inst_value: pd.Series, inst_investors: pd.Series) -> pd.Series:
    """1 when avg position value.qoq<0 AND investors.qoq<0 — block holders exiting."""
    avg = _safe_div(inst_value, inst_investors)
    return ((avg.diff() < 0) & (inst_investors.diff() < 0)).astype(float)


def f20_iosp_143_retail_concentration_growth_8q(inst_units: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """-inst_pct_of_float.diff(8) — positive when institutional share has fallen 2y."""
    pct = _safe_div(inst_units, sharesbas)
    return -pct.diff(8)


def f20_iosp_144_retail_concentration_growth_4q(inst_units: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """-inst_pct_of_float.diff(4) — positive when institutional share has fallen 1y."""
    pct = _safe_div(inst_units, sharesbas)
    return -pct.diff(4)


def f20_iosp_145_crowded_then_left_signal(inst_units: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """inst_pct.shift(8) - inst_pct — positive when ownership reduced over 2y."""
    pct = _safe_div(inst_units, sharesbas)
    return pct.shift(8) - pct


def f20_iosp_146_inst_pct_8q_decline_pct(inst_units: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """(inst_pct - inst_pct.shift(8)) / |inst_pct.shift(8)| — 8q normalized change."""
    pct = _safe_div(inst_units, sharesbas)
    prev = pct.shift(8)
    return _safe_div(pct - prev, prev.abs())


def f20_iosp_147_inst_pct_12q_decline_pct(inst_units: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """(inst_pct - inst_pct.shift(12)) / |inst_pct.shift(12)| — 12q normalized change."""
    pct = _safe_div(inst_units, sharesbas)
    prev = pct.shift(12)
    return _safe_div(pct - prev, prev.abs())


def f20_iosp_148_inst_pct_recovery_from_8q_min(inst_units: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """inst_pct / inst_pct.rolling(8).min() - 1 — recovery from recent floor."""
    pct = _safe_div(inst_units, sharesbas)
    rmin = pct.rolling(8, min_periods=3).min()
    return _safe_div(pct, rmin) - 1.0


def f20_iosp_149_structural_under_ownership_alarm(inst_units: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Indicator: inst_pct below 25th percentile of last 8q distribution."""
    pct = _safe_div(inst_units, sharesbas)
    q25 = pct.rolling(8, min_periods=3).quantile(0.25)
    return (pct < q25).astype(float)


def f20_iosp_150_peak_ownership_decay_rate(inst_units: pd.Series) -> pd.Series:
    """(units.rolling(8).max() - units) / units.rolling(8).max() — decay from recent peak."""
    rmax = inst_units.rolling(8, min_periods=3).max()
    return _safe_div(rmax - inst_units, rmax)


# ============================================================
#                        REGISTRY
# ============================================================

INSTITUTIONAL_OWNERSHIP_SNAPSHOT_BASE_REGISTRY_076_150 = {
    "f20_iosp_076_inst_puts_qoq_pct": {"inputs": ["inst_puts"], "func": f20_iosp_076_inst_puts_qoq_pct},
    "f20_iosp_077_inst_calls_yoy_pct": {"inputs": ["inst_calls"], "func": f20_iosp_077_inst_calls_yoy_pct},
    "f20_iosp_078_inst_puts_yoy_pct": {"inputs": ["inst_puts"], "func": f20_iosp_078_inst_puts_yoy_pct},
    "f20_iosp_079_put_concentration_per_investor": {"inputs": ["inst_puts", "inst_investors"], "func": f20_iosp_079_put_concentration_per_investor},
    "f20_iosp_080_call_concentration_per_investor": {"inputs": ["inst_calls", "inst_investors"], "func": f20_iosp_080_call_concentration_per_investor},
    "f20_iosp_081_options_skew_8q_zscore": {"inputs": ["inst_puts", "inst_calls"], "func": f20_iosp_081_options_skew_8q_zscore},
    "f20_iosp_082_put_buildup_intensity_4q": {"inputs": ["inst_puts", "inst_units"], "func": f20_iosp_082_put_buildup_intensity_4q},
    "f20_iosp_083_call_unwinding_intensity_4q": {"inputs": ["inst_calls", "inst_units"], "func": f20_iosp_083_call_unwinding_intensity_4q},
    "f20_iosp_084_protective_put_intensity": {"inputs": ["inst_puts", "inst_units"], "func": f20_iosp_084_protective_put_intensity},
    "f20_iosp_085_options_skew_jerk": {"inputs": ["inst_puts", "inst_calls"], "func": f20_iosp_085_options_skew_jerk},
    "f20_iosp_086_peak_inst_units_to_current": {"inputs": ["inst_units"], "func": f20_iosp_086_peak_inst_units_to_current},
    "f20_iosp_087_drawdown_from_peak_units": {"inputs": ["inst_units"], "func": f20_iosp_087_drawdown_from_peak_units},
    "f20_iosp_088_drawdown_from_peak_investors": {"inputs": ["inst_investors"], "func": f20_iosp_088_drawdown_from_peak_investors},
    "f20_iosp_089_drawdown_from_peak_value": {"inputs": ["inst_value"], "func": f20_iosp_089_drawdown_from_peak_value},
    "f20_iosp_090_quarters_since_peak_units": {"inputs": ["inst_units"], "func": f20_iosp_090_quarters_since_peak_units},
    "f20_iosp_091_quarters_since_peak_investors": {"inputs": ["inst_investors"], "func": f20_iosp_091_quarters_since_peak_investors},
    "f20_iosp_092_quarters_since_peak_value": {"inputs": ["inst_value"], "func": f20_iosp_092_quarters_since_peak_value},
    "f20_iosp_093_units_share_of_8q_max": {"inputs": ["inst_units"], "func": f20_iosp_093_units_share_of_8q_max},
    "f20_iosp_094_investors_share_of_8q_max": {"inputs": ["inst_investors"], "func": f20_iosp_094_investors_share_of_8q_max},
    "f20_iosp_095_consec_quarters_units_decline": {"inputs": ["inst_units"], "func": f20_iosp_095_consec_quarters_units_decline},
    "f20_iosp_096_consec_quarters_investors_decline": {"inputs": ["inst_investors"], "func": f20_iosp_096_consec_quarters_investors_decline},
    "f20_iosp_097_abandonment_intensity_4q": {"inputs": ["inst_investors"], "func": f20_iosp_097_abandonment_intensity_4q},
    "f20_iosp_098_abandonment_intensity_8q": {"inputs": ["inst_investors"], "func": f20_iosp_098_abandonment_intensity_8q},
    "f20_iosp_099_units_below_4q_avg_persistence_8q": {"inputs": ["inst_units"], "func": f20_iosp_099_units_below_4q_avg_persistence_8q},
    "f20_iosp_100_investors_below_4q_avg_persistence_8q": {"inputs": ["inst_investors"], "func": f20_iosp_100_investors_below_4q_avg_persistence_8q},
    "f20_iosp_101_units_negative_qoq_count_8q": {"inputs": ["inst_units"], "func": f20_iosp_101_units_negative_qoq_count_8q},
    "f20_iosp_102_investors_negative_qoq_count_8q": {"inputs": ["inst_investors"], "func": f20_iosp_102_investors_negative_qoq_count_8q},
    "f20_iosp_103_units_qoq_negative_ema": {"inputs": ["inst_units"], "func": f20_iosp_103_units_qoq_negative_ema},
    "f20_iosp_104_dispersion_widening_count_8q": {"inputs": ["inst_value", "inst_investors"], "func": f20_iosp_104_dispersion_widening_count_8q},
    "f20_iosp_105_fast_money_exit_proxy": {"inputs": ["inst_units", "inst_investors"], "func": f20_iosp_105_fast_money_exit_proxy},
    "f20_iosp_106_consolidating_exit_proxy": {"inputs": ["inst_units", "inst_investors"], "func": f20_iosp_106_consolidating_exit_proxy},
    "f20_iosp_107_retail_capture_proxy": {"inputs": ["inst_units", "inst_investors", "sharesbas"], "func": f20_iosp_107_retail_capture_proxy},
    "f20_iosp_108_unit_value_divergence_indicator": {"inputs": ["inst_units", "inst_value"], "func": f20_iosp_108_unit_value_divergence_indicator},
    "f20_iosp_109_holder_loss_rate_4q": {"inputs": ["inst_investors"], "func": f20_iosp_109_holder_loss_rate_4q},
    "f20_iosp_110_holder_gain_rate_4q": {"inputs": ["inst_investors"], "func": f20_iosp_110_holder_gain_rate_4q},
    "f20_iosp_111_inst_value_to_marketcap_qoq_pct": {"inputs": ["inst_value", "marketcap"], "func": f20_iosp_111_inst_value_to_marketcap_qoq_pct},
    "f20_iosp_112_inst_value_to_marketcap_yoy_pct": {"inputs": ["inst_value", "marketcap"], "func": f20_iosp_112_inst_value_to_marketcap_yoy_pct},
    "f20_iosp_113_inst_value_to_marketcap_zscore_8q": {"inputs": ["inst_value", "marketcap"], "func": f20_iosp_113_inst_value_to_marketcap_zscore_8q},
    "f20_iosp_114_inst_value_marketcap_residual_8q": {"inputs": ["inst_value", "marketcap"], "func": f20_iosp_114_inst_value_marketcap_residual_8q},
    "f20_iosp_115_ownership_price_corr_8q": {"inputs": ["inst_units", "close"], "func": f20_iosp_115_ownership_price_corr_8q},
    "f20_iosp_116_ownership_marketcap_corr_4q": {"inputs": ["inst_units", "marketcap"], "func": f20_iosp_116_ownership_marketcap_corr_4q},
    "f20_iosp_117_value_growth_minus_mcap_growth_qoq": {"inputs": ["inst_value", "marketcap"], "func": f20_iosp_117_value_growth_minus_mcap_growth_qoq},
    "f20_iosp_118_value_growth_minus_mcap_growth_yoy": {"inputs": ["inst_value", "marketcap"], "func": f20_iosp_118_value_growth_minus_mcap_growth_yoy},
    "f20_iosp_119_implied_price_stale_signal": {"inputs": ["inst_value", "inst_units", "close"], "func": f20_iosp_119_implied_price_stale_signal},
    "f20_iosp_120_implied_price_yoy_pct": {"inputs": ["inst_value", "inst_units"], "func": f20_iosp_120_implied_price_yoy_pct},
    "f20_iosp_121_units_normalized_by_mcap_change": {"inputs": ["inst_units", "marketcap"], "func": f20_iosp_121_units_normalized_by_mcap_change},
    "f20_iosp_122_value_per_investor_to_mcap_per_share": {"inputs": ["inst_value", "inst_investors", "marketcap", "sharesbas"], "func": f20_iosp_122_value_per_investor_to_mcap_per_share},
    "f20_iosp_123_inst_pct_zscore_12q": {"inputs": ["inst_units", "sharesbas"], "func": f20_iosp_123_inst_pct_zscore_12q},
    "f20_iosp_124_inst_pct_4q_change_pct": {"inputs": ["inst_units", "sharesbas"], "func": f20_iosp_124_inst_pct_4q_change_pct},
    "f20_iosp_125_inst_pct_8q_change_pct": {"inputs": ["inst_units", "sharesbas"], "func": f20_iosp_125_inst_pct_8q_change_pct},
    "f20_iosp_126_inst_value_mcap_share_8q_min": {"inputs": ["inst_value", "marketcap"], "func": f20_iosp_126_inst_value_mcap_share_8q_min},
    "f20_iosp_127_inst_value_mcap_share_8q_max": {"inputs": ["inst_value", "marketcap"], "func": f20_iosp_127_inst_value_mcap_share_8q_max},
    "f20_iosp_128_inst_value_share_collapse_from_8q_max": {"inputs": ["inst_value", "marketcap"], "func": f20_iosp_128_inst_value_share_collapse_from_8q_max},
    "f20_iosp_129_unit_growth_mcap_growth_divergence_8q": {"inputs": ["inst_units", "marketcap"], "func": f20_iosp_129_unit_growth_mcap_growth_divergence_8q},
    "f20_iosp_130_value_growth_mcap_growth_corr_8q": {"inputs": ["inst_value", "marketcap"], "func": f20_iosp_130_value_growth_mcap_growth_corr_8q},
    "f20_iosp_131_inst_units_max_consec_negative_qoq_8q": {"inputs": ["inst_units"], "func": f20_iosp_131_inst_units_max_consec_negative_qoq_8q},
    "f20_iosp_132_inst_investors_max_consec_negative_qoq_8q": {"inputs": ["inst_investors"], "func": f20_iosp_132_inst_investors_max_consec_negative_qoq_8q},
    "f20_iosp_133_inst_value_max_consec_negative_qoq_8q": {"inputs": ["inst_value"], "func": f20_iosp_133_inst_value_max_consec_negative_qoq_8q},
    "f20_iosp_134_inst_pct_yoy_negative_streak": {"inputs": ["inst_units", "sharesbas"], "func": f20_iosp_134_inst_pct_yoy_negative_streak},
    "f20_iosp_135_inst_pct_qoq_negative_streak": {"inputs": ["inst_units", "sharesbas"], "func": f20_iosp_135_inst_pct_qoq_negative_streak},
    "f20_iosp_136_ownership_volatility_units_zscore_12q": {"inputs": ["inst_units"], "func": f20_iosp_136_ownership_volatility_units_zscore_12q},
    "f20_iosp_137_ownership_volatility_investors_zscore_12q": {"inputs": ["inst_investors"], "func": f20_iosp_137_ownership_volatility_investors_zscore_12q},
    "f20_iosp_138_ownership_volatility_value_zscore_12q": {"inputs": ["inst_value"], "func": f20_iosp_138_ownership_volatility_value_zscore_12q},
    "f20_iosp_139_ownership_cohort_collapse_8q": {"inputs": ["inst_units", "inst_investors", "inst_value"], "func": f20_iosp_139_ownership_cohort_collapse_8q},
    "f20_iosp_140_options_hedge_buildup_streak": {"inputs": ["inst_puts"], "func": f20_iosp_140_options_hedge_buildup_streak},
    "f20_iosp_141_options_hedge_acceleration_indicator": {"inputs": ["inst_puts", "inst_calls"], "func": f20_iosp_141_options_hedge_acceleration_indicator},
    "f20_iosp_142_block_holder_exit_indicator": {"inputs": ["inst_value", "inst_investors"], "func": f20_iosp_142_block_holder_exit_indicator},
    "f20_iosp_143_retail_concentration_growth_8q": {"inputs": ["inst_units", "sharesbas"], "func": f20_iosp_143_retail_concentration_growth_8q},
    "f20_iosp_144_retail_concentration_growth_4q": {"inputs": ["inst_units", "sharesbas"], "func": f20_iosp_144_retail_concentration_growth_4q},
    "f20_iosp_145_crowded_then_left_signal": {"inputs": ["inst_units", "sharesbas"], "func": f20_iosp_145_crowded_then_left_signal},
    "f20_iosp_146_inst_pct_8q_decline_pct": {"inputs": ["inst_units", "sharesbas"], "func": f20_iosp_146_inst_pct_8q_decline_pct},
    "f20_iosp_147_inst_pct_12q_decline_pct": {"inputs": ["inst_units", "sharesbas"], "func": f20_iosp_147_inst_pct_12q_decline_pct},
    "f20_iosp_148_inst_pct_recovery_from_8q_min": {"inputs": ["inst_units", "sharesbas"], "func": f20_iosp_148_inst_pct_recovery_from_8q_min},
    "f20_iosp_149_structural_under_ownership_alarm": {"inputs": ["inst_units", "sharesbas"], "func": f20_iosp_149_structural_under_ownership_alarm},
    "f20_iosp_150_peak_ownership_decay_rate": {"inputs": ["inst_units"], "func": f20_iosp_150_peak_ownership_decay_rate},
}
