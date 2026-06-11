"""passive_flow_acceleration base features 076-150 — Pipeline 1a-inverse short-side blowup family.

Continued. Theme: ETF-vs-inst divergence/decoupling, put/call & derivatives
positioning acceleration, composite multi-metric passive-flow acceleration.
"""
import numpy as np
import pandas as pd

Q = 1
Y = 4
Y2 = 8
Y3 = 12
Y4 = 16


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


def _quadratic_c2(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 2, 3)
    def _c2(w):
        if np.isnan(w).any() or len(w) < 3:
            return np.nan
        x = np.arange(len(w))
        try:
            c2, _, _ = np.polyfit(x, w, 2)
            return float(c2)
        except Exception:
            return np.nan
    return s.rolling(n, min_periods=min_periods).apply(_c2, raw=True)


def _structural_break_score(s, n):
    return _rolling_slope(s, n) - _rolling_slope(s.shift(n), n)


# ============================================================
#                  FEATURES 076-150
# ============================================================

def f33_pfac_076_etf_share_inst_value_correlation_8q(etf_share: pd.Series, inst_value: pd.Series) -> pd.Series:
    """Rolling 8Q correlation of etf_share vs inst_value — decoupling when correlation falls."""
    return etf_share.rolling(Y2, min_periods=3).corr(inst_value)


def f33_pfac_077_etf_share_inst_count_correlation_8q(etf_share: pd.Series, inst_count: pd.Series) -> pd.Series:
    """Rolling 8Q correlation of etf_share vs inst_count."""
    return etf_share.rolling(Y2, min_periods=3).corr(inst_count)


def f33_pfac_078_etf_inflow_inst_outflow_simultaneity_count_8q(etf_flow: pd.Series, inst_value: pd.Series) -> pd.Series:
    """Count of 8Q with ETF inflow AND inst_value outflow on same Q."""
    flag = ((etf_flow > 0) & (inst_value.diff() < 0)).astype(float)
    return flag.rolling(Y2, min_periods=3).sum()


def f33_pfac_079_etf_vs_inst_slope_spread_4q(etf_share: pd.Series, inst_value: pd.Series) -> pd.Series:
    """4Q etf_share slope minus 4Q inst_value slope (normalized by their means)."""
    e = _rolling_slope(etf_share, Y) / etf_share.rolling(Y, min_periods=2).mean().replace(0, np.nan)
    i = _rolling_slope(inst_value, Y) / inst_value.rolling(Y, min_periods=2).mean().replace(0, np.nan)
    return e - i


def f33_pfac_080_etf_vs_inst_slope_spread_12q(etf_share: pd.Series, inst_value: pd.Series) -> pd.Series:
    """Same as 079 over 12Q windows."""
    e = _rolling_slope(etf_share, Y3) / etf_share.rolling(Y3, min_periods=4).mean().replace(0, np.nan)
    i = _rolling_slope(inst_value, Y3) / inst_value.rolling(Y3, min_periods=4).mean().replace(0, np.nan)
    return e - i


def f33_pfac_081_acceleration_of_etf_minus_inst_ratio_16q(etf_share: pd.Series, inst_value: pd.Series) -> pd.Series:
    """Z-score of (etf_share - inst_value/inst_value.max) 1Q chg over 16Q."""
    rel_inst = _safe_div(inst_value, inst_value.rolling(Y4, min_periods=6).max())
    spread = etf_share - rel_inst
    return _rolling_zscore(spread.diff(), Y4)


def f33_pfac_082_d2_etf_concentration_vs_d2_inst_concentration(etf_share: pd.Series, inst_shares: pd.Series, inst_value: pd.Series, inst_count: pd.Series) -> pd.Series:
    """d2(etf_share/(etf_share+inst_shares)) minus d2(inst_value/inst_count) — passive-active accel spread."""
    etf_conc = _safe_div(etf_share, etf_share + inst_shares)
    inst_conc = _safe_div(inst_value, inst_count)
    return etf_conc.diff().diff() - inst_conc.diff().diff()


def f33_pfac_083_compound_etf_gain_2sigma_inst_loss_2sigma_4q(etf_flow: pd.Series, inst_value: pd.Series) -> pd.Series:
    """Count 4Q with etf_flow z>2 AND inst_value chg z<-2 — joint extreme divergence."""
    z_e = _rolling_zscore(etf_flow, Y4)
    z_i = _rolling_zscore(inst_value.diff(), Y4)
    flag = ((z_e > 2.0) & (z_i < -2.0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f33_pfac_084_spread_cumulative_integral_8q(etf_share: pd.Series, inst_value: pd.Series) -> pd.Series:
    """Cumulative sum over 8Q of (z(etf_share) - z(inst_value))."""
    z_e = _rolling_zscore(etf_share, Y4)
    z_i = _rolling_zscore(inst_value, Y4)
    return (z_e - z_i).rolling(Y2, min_periods=3).sum()


def f33_pfac_085_spread_tail_event_count_16q(etf_share: pd.Series, inst_value: pd.Series) -> pd.Series:
    """Count of last 16Q with (z(etf_share)-z(inst_value)) > 95th-pct of 16Q dist."""
    z_e = _rolling_zscore(etf_share, Y4)
    z_i = _rolling_zscore(inst_value, Y4)
    sp = z_e - z_i
    p = sp.rolling(Y4, min_periods=6).quantile(0.95)
    flag = (sp >= p).astype(float)
    return flag.rolling(Y4, min_periods=6).sum()


def f33_pfac_086_spread_quadratic_c2_8q(etf_share: pd.Series, inst_value: pd.Series) -> pd.Series:
    """Quadratic c2 of (etf_share - inst_value normalized) over 8Q."""
    rel_inst = _safe_div(inst_value, inst_value.rolling(Y4, min_periods=6).max())
    spread = etf_share - rel_inst
    return _quadratic_c2(spread, Y2)


def f33_pfac_087_spread_inflection_count_8q(etf_share: pd.Series, inst_value: pd.Series) -> pd.Series:
    """Count of bars in 8Q where 2nd diff of (etf_share - inst_value normalized) is positive."""
    rel_inst = _safe_div(inst_value, inst_value.rolling(Y4, min_periods=6).max())
    spread = etf_share - rel_inst
    d2 = spread.diff().diff()
    flag = (d2 > 0).astype(float)
    return flag.rolling(Y2, min_periods=3).sum()


def f33_pfac_088_spread_structural_break_8q(etf_share: pd.Series, inst_value: pd.Series) -> pd.Series:
    """8Q recent vs prior slope of (etf_share - inst_value normalized)."""
    rel_inst = _safe_div(inst_value, inst_value.rolling(Y4, min_periods=6).max())
    spread = etf_share - rel_inst
    return _structural_break_score(spread, Y2)


def f33_pfac_089_spread_arc_area_8q(etf_share: pd.Series, inst_value: pd.Series) -> pd.Series:
    """Arc area of spread above 8Q linear fit."""
    rel_inst = _safe_div(inst_value, inst_value.rolling(Y4, min_periods=6).max())
    spread = etf_share - rel_inst
    def _arc(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        c1, c0 = np.polyfit(x, w, 1)
        resid = w - (c1 * x + c0)
        return float(np.clip(resid, 0, None).sum())
    return spread.rolling(Y2, min_periods=4).apply(_arc, raw=True)


def f33_pfac_090_log_spread_slope_4q_minus_12q(etf_share: pd.Series, inst_value: pd.Series) -> pd.Series:
    """Log(spread+1) 4Q slope minus 12Q slope."""
    rel_inst = _safe_div(inst_value, inst_value.rolling(Y4, min_periods=6).max())
    spread = (etf_share - rel_inst + 1.0).clip(lower=1e-6)
    ls = _safe_log(spread)
    return _rolling_slope(ls, Y) - _rolling_slope(ls, Y3)


def f33_pfac_091_spread_latest_to_16q_max(etf_share: pd.Series, inst_value: pd.Series) -> pd.Series:
    """Current spread / 16Q max spread."""
    rel_inst = _safe_div(inst_value, inst_value.rolling(Y4, min_periods=6).max())
    spread = etf_share - rel_inst
    return _safe_div(spread, spread.rolling(Y4, min_periods=6).max())


def f33_pfac_092_quarters_since_spread_accelerated(etf_share: pd.Series, inst_value: pd.Series) -> pd.Series:
    """Quarters since spread d2 last crossed above zero."""
    rel_inst = _safe_div(inst_value, inst_value.rolling(Y4, min_periods=6).max())
    spread = etf_share - rel_inst
    d2 = spread.diff().diff()
    flag = (d2 > 0).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return pd.Series(np.arange(len(flag)), index=flag.index) - last


def f33_pfac_093_spread_weighted_composite_z_4q(etf_share: pd.Series, inst_value: pd.Series, inst_count: pd.Series) -> pd.Series:
    """Mean 4Q of (z(etf_share chg) - z(inst_value chg) - z(inst_count chg))."""
    z = _rolling_zscore(etf_share.diff(), Y4) - _rolling_zscore(inst_value.diff(), Y4) - _rolling_zscore(inst_count.diff(), Y4)
    return z.rolling(Y, min_periods=2).mean()


def f33_pfac_094_spread_cliff_count_16q(etf_share: pd.Series, inst_value: pd.Series) -> pd.Series:
    """Count of 1Q spread changes with z>2 over 16Q."""
    rel_inst = _safe_div(inst_value, inst_value.rolling(Y4, min_periods=6).max())
    spread = etf_share - rel_inst
    z = _rolling_zscore(spread.diff(), Y4)
    flag = (z > 2.0).astype(float)
    return flag.rolling(Y4, min_periods=6).sum()


def f33_pfac_095_ratio_inst_loss_to_etf_gain_4q(inst_value: pd.Series, etf_flow: pd.Series) -> pd.Series:
    """Sum 4Q of |inst_value loss| / sum 4Q of etf_flow gain."""
    inst_loss = (-inst_value.diff()).clip(lower=0).rolling(Y, min_periods=2).sum()
    etf_gain = etf_flow.clip(lower=0).rolling(Y, min_periods=2).sum()
    return _safe_div(inst_loss, etf_gain)


def f33_pfac_096_passive_to_active_ratio_accel_16q(etf_share: pd.Series, inst_shares: pd.Series) -> pd.Series:
    """Z-score of 1Q chg in etf_share/inst_shares over 16Q."""
    r = _safe_div(etf_share, inst_shares)
    return _rolling_zscore(r.diff(), Y4)


def f33_pfac_097_compound_spread_divergence_inst_count_down_4q(etf_share: pd.Series, inst_value: pd.Series, inst_count: pd.Series) -> pd.Series:
    """Count 4Q with spread rising (etf up + inst flat or down) AND inst_count down."""
    flag = ((etf_share.diff() > 0) & (inst_value.diff() <= 0) & (inst_count.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f33_pfac_098_d2_spread_z_16q(etf_share: pd.Series, inst_value: pd.Series) -> pd.Series:
    """Z-score of 2nd diff of (etf_share - inst_value normalized) over 16Q."""
    rel_inst = _safe_div(inst_value, inst_value.rolling(Y4, min_periods=6).max())
    spread = etf_share - rel_inst
    return _rolling_zscore(spread.diff().diff(), Y4)


def f33_pfac_099_composite_spread_divergence_accel_8q(etf_share: pd.Series, inst_value: pd.Series) -> pd.Series:
    """Cumulative sum 8Q of z(spread chg) — sustained divergence acceleration."""
    rel_inst = _safe_div(inst_value, inst_value.rolling(Y4, min_periods=6).max())
    spread = etf_share - rel_inst
    return _rolling_zscore(spread.diff(), Y4).rolling(Y2, min_periods=3).sum()


def f33_pfac_100_composite_spread_divergence_escalation_4q(etf_share: pd.Series, inst_value: pd.Series, inst_count: pd.Series) -> pd.Series:
    """Mean 4Q of (z(etf_share chg) + z(-inst_value chg) + z(-inst_count chg)) divided by 16Q std."""
    z = _rolling_zscore(etf_share.diff(), Y4) + _rolling_zscore(-inst_value.diff(), Y4) + _rolling_zscore(-inst_count.diff(), Y4)
    return _safe_div(z.rolling(Y, min_periods=2).mean(), z.rolling(Y4, min_periods=6).std())


def f33_pfac_101_inst_puts_cliff_8q(inst_puts: pd.Series) -> pd.Series:
    """1Q jump in inst_puts / 8Q std — put positioning cliff."""
    chg = inst_puts.diff()
    sd = chg.rolling(Y2, min_periods=3).std()
    return chg / sd.replace(0, np.nan)


def f33_pfac_102_inst_puts_zscore_16q(inst_puts: pd.Series) -> pd.Series:
    """Z-score of 1Q inst_puts change over 16Q."""
    return _rolling_zscore(inst_puts.diff(), Y4)


def f33_pfac_103_inst_calls_cliff_8q(inst_calls: pd.Series) -> pd.Series:
    """1Q jump in inst_calls / 8Q std."""
    chg = inst_calls.diff()
    sd = chg.rolling(Y2, min_periods=3).std()
    return chg / sd.replace(0, np.nan)


def f33_pfac_104_inst_calls_zscore_16q(inst_calls: pd.Series) -> pd.Series:
    """Z-score of 1Q inst_calls change over 16Q."""
    return _rolling_zscore(inst_calls.diff(), Y4)


def f33_pfac_105_put_call_ratio_accel_z_16q(inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Z-score of 1Q chg in inst_puts/inst_calls over 16Q."""
    r = _safe_div(inst_puts, inst_calls)
    return _rolling_zscore(r.diff(), Y4)


def f33_pfac_106_put_call_cliff_jump_8q(inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """1Q jump in put/call ratio / 8Q std."""
    r = _safe_div(inst_puts, inst_calls)
    chg = r.diff()
    sd = chg.rolling(Y2, min_periods=3).std()
    return chg / sd.replace(0, np.nan)


def f33_pfac_107_put_call_structural_break_8q(inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Put/call 8Q recent vs prior slope."""
    r = _safe_div(inst_puts, inst_calls)
    return _structural_break_score(r, Y2)


def f33_pfac_108_compound_puts_up_calls_down_4q(inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Count 4Q with puts rising AND calls falling — bearish positioning shift."""
    flag = ((inst_puts.diff() > 0) & (inst_calls.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f33_pfac_109_compound_puts_up_inst_count_down_4q(inst_puts: pd.Series, inst_count: pd.Series) -> pd.Series:
    """Count 4Q with puts rising AND inst_count falling — bearish bets while active exits."""
    flag = ((inst_puts.diff() > 0) & (inst_count.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f33_pfac_110_puts_to_inst_count_accel_z(inst_puts: pd.Series, inst_count: pd.Series) -> pd.Series:
    """Z-score of 1Q chg in puts/inst_count — put concentration per institution."""
    r = _safe_div(inst_puts, inst_count)
    return _rolling_zscore(r.diff(), Y4)


def f33_pfac_111_calls_to_inst_count_accel_z(inst_calls: pd.Series, inst_count: pd.Series) -> pd.Series:
    """Z-score of 1Q chg in calls/inst_count."""
    r = _safe_div(inst_calls, inst_count)
    return _rolling_zscore(r.diff(), Y4)


def f33_pfac_112_d2_log_put_call_z_16q(inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Z-score of 2nd diff of log(put/call) over 16Q."""
    lr = _safe_log(_safe_div(inst_puts, inst_calls))
    return _rolling_zscore(lr.diff().diff(), Y4)


def f33_pfac_113_put_call_cumulative_z_8q(inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Cumulative sum 8Q of put/call z-score (vs 16Q dist) — sustained elevation."""
    r = _safe_div(inst_puts, inst_calls)
    return _rolling_zscore(r, Y4).rolling(Y2, min_periods=3).sum()


def f33_pfac_114_put_call_inflection_sign_flip_8q(inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Sign-flip count of put/call slope vs EMA-smoothed slope over 8Q."""
    r = _safe_div(inst_puts, inst_calls)
    sl = _rolling_slope(r, Y)
    sm = sl.ewm(span=4, adjust=False, min_periods=2).mean()
    flip = (np.sign(sl - sm) != np.sign((sl - sm).shift(1))).astype(float)
    return flip.rolling(Y2, min_periods=3).sum()


def f33_pfac_115_put_call_exp_fit_r2_8q(inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """R² of log(put/call) linear fit over 8Q."""
    lr = _safe_log(_safe_div(inst_puts, inst_calls))
    def _r2(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        ss_tot = ((w - w.mean()) ** 2).sum()
        if ss_tot == 0:
            return np.nan
        c1, c0 = np.polyfit(x, w, 1)
        pred = c1 * x + c0
        ss_res = ((w - pred) ** 2).sum()
        return 1.0 - ss_res / ss_tot
    return lr.rolling(Y2, min_periods=4).apply(_r2, raw=True)


def f33_pfac_116_put_call_latest_to_16q_max(inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Current put/call / 16Q max — proximity to peak bearish positioning."""
    r = _safe_div(inst_puts, inst_calls)
    return _safe_div(r, r.rolling(Y4, min_periods=6).max())


def f33_pfac_117_quarters_since_put_call_accelerated(inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Quarters since put/call d2 last crossed above zero."""
    r = _safe_div(inst_puts, inst_calls)
    d2 = r.diff().diff()
    flag = (d2 > 0).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return pd.Series(np.arange(len(flag)), index=flag.index) - last


def f33_pfac_118_put_call_2sigma_count_16q(inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Count of 1Q put/call changes with z>2 over 16Q."""
    r = _safe_div(inst_puts, inst_calls)
    z = _rolling_zscore(r.diff(), Y4)
    flag = (z > 2.0).astype(float)
    return flag.rolling(Y4, min_periods=6).sum()


def f33_pfac_119_compound_high_put_call_etf_flow_down_4q(inst_puts: pd.Series, inst_calls: pd.Series, etf_flow: pd.Series) -> pd.Series:
    """Count 4Q with put/call > 16Q-75th-pct AND etf_flow negative."""
    r = _safe_div(inst_puts, inst_calls)
    p = r.rolling(Y4, min_periods=6).quantile(0.75)
    flag = ((r >= p) & (etf_flow < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f33_pfac_120_compound_high_put_call_inst_value_down_4q(inst_puts: pd.Series, inst_calls: pd.Series, inst_value: pd.Series) -> pd.Series:
    """Count 4Q with put/call > 16Q-75th-pct AND inst_value declining."""
    r = _safe_div(inst_puts, inst_calls)
    p = r.rolling(Y4, min_periods=6).quantile(0.75)
    flag = ((r >= p) & (inst_value.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f33_pfac_121_put_call_slope_4q_minus_12q(inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Put/call 4Q slope minus 12Q slope."""
    r = _safe_div(inst_puts, inst_calls)
    return _rolling_slope(r, Y) - _rolling_slope(r, Y3)


def f33_pfac_122_composite_derivative_stress_accel_4q(inst_puts: pd.Series, inst_calls: pd.Series, inst_count: pd.Series) -> pd.Series:
    """Mean 4Q of (z(put/call chg) + z(-inst_count chg)) — derivatives stress acceleration."""
    r = _safe_div(inst_puts, inst_calls)
    return (_rolling_zscore(r.diff(), Y4) + _rolling_zscore(-inst_count.diff(), Y4)).rolling(Y, min_periods=2).mean()


def f33_pfac_123_d2_put_call_spread_z(inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Z-score of 2nd diff of (inst_puts - inst_calls) over 16Q."""
    sp = inst_puts - inst_calls
    return _rolling_zscore(sp.diff().diff(), Y4)


def f33_pfac_124_put_call_arc_area_above_8q_linear(inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Arc area of put/call ratio above 8Q linear fit."""
    r = _safe_div(inst_puts, inst_calls)
    def _arc(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        c1, c0 = np.polyfit(x, w, 1)
        resid = w - (c1 * x + c0)
        return float(np.clip(resid, 0, None).sum())
    return r.rolling(Y2, min_periods=4).apply(_arc, raw=True)


def f33_pfac_125_composite_derivatives_positioning_accel_4q(inst_puts: pd.Series, inst_calls: pd.Series, inst_count: pd.Series, inst_value: pd.Series) -> pd.Series:
    """Mean 4Q of (z(put/call chg) + z(-inst_count chg) + z(-inst_value chg))."""
    r = _safe_div(inst_puts, inst_calls)
    z = _rolling_zscore(r.diff(), Y4) + _rolling_zscore(-inst_count.diff(), Y4) + _rolling_zscore(-inst_value.diff(), Y4)
    return z.rolling(Y, min_periods=2).mean()


def f33_pfac_126_multimetric_accel_coincidence_count_4q(etf_share: pd.Series, inst_value: pd.Series, inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Count 4Q with etf_share d2>0 AND inst_value d2<0 AND put/call d2>0 — triple coincidence."""
    pc = _safe_div(inst_puts, inst_calls)
    flag = ((etf_share.diff().diff() > 0) & (inst_value.diff().diff() < 0) & (pc.diff().diff() > 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f33_pfac_127_compound_etf_conc_up_inst_exit_put_call_up_4q(etf_share: pd.Series, inst_shares: pd.Series, inst_count: pd.Series, inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Count 4Q with etf-concentration rising AND inst_count falling AND put/call rising."""
    ec = _safe_div(etf_share, etf_share + inst_shares)
    pc = _safe_div(inst_puts, inst_calls)
    flag = ((ec.diff() > 0) & (inst_count.diff() < 0) & (pc.diff() > 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f33_pfac_128_weighted_composite_z_etf_inst_putcall_4q(etf_share: pd.Series, inst_value: pd.Series, inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Mean 4Q of (z(etf_share chg) + z(-inst_value chg) + z(put/call chg))."""
    pc = _safe_div(inst_puts, inst_calls)
    z = _rolling_zscore(etf_share.diff(), Y4) + _rolling_zscore(-inst_value.diff(), Y4) + _rolling_zscore(pc.diff(), Y4)
    return z.rolling(Y, min_periods=2).mean()


def f33_pfac_129_composite_stress_accel_4q(etf_share: pd.Series, inst_value: pd.Series, inst_count: pd.Series) -> pd.Series:
    """Sum 4Q of (z(etf_share chg) + z(-inst_value chg) + z(-inst_count chg))."""
    z = _rolling_zscore(etf_share.diff(), Y4) + _rolling_zscore(-inst_value.diff(), Y4) + _rolling_zscore(-inst_count.diff(), Y4)
    return z.rolling(Y, min_periods=2).sum()


def f33_pfac_130_variance_explained_by_passive_flow_accel_8q(etf_share: pd.Series, inst_value: pd.Series) -> pd.Series:
    """8Q variance of etf_share-vs-inst_value spread / 16Q variance — short-vs-long concentration."""
    rel_inst = _safe_div(inst_value, inst_value.rolling(Y4, min_periods=6).max())
    spread = etf_share - rel_inst
    return _safe_div(spread.rolling(Y2, min_periods=3).var(), spread.rolling(Y4, min_periods=6).var())


def f33_pfac_131_multivariate_accel_outlier_z_4q(etf_share: pd.Series, inst_value: pd.Series, inst_count: pd.Series, inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Sum of squared z-scores across 5 metrics, averaged over 4Q."""
    pc = _safe_div(inst_puts, inst_calls)
    z = (
        _rolling_zscore(etf_share.diff(), Y4) ** 2
        + _rolling_zscore(inst_value.diff(), Y4) ** 2
        + _rolling_zscore(inst_count.diff(), Y4) ** 2
        + _rolling_zscore(pc.diff(), Y4) ** 2
    )
    return z.rolling(Y, min_periods=2).mean()


def f33_pfac_132_cumulative_passive_flow_accel_index_8q(etf_share: pd.Series, inst_value: pd.Series, inst_count: pd.Series) -> pd.Series:
    """Cumulative sum 8Q of composite z-score (etf up + inst down)."""
    z = _rolling_zscore(etf_share.diff(), Y4) + _rolling_zscore(-inst_value.diff(), Y4) + _rolling_zscore(-inst_count.diff(), Y4)
    return z.rolling(Y2, min_periods=3).sum()


def f33_pfac_133_compound_passive_bearish_to_16q_baseline(etf_share: pd.Series, inst_value: pd.Series, inst_count: pd.Series) -> pd.Series:
    """4Q compound-passive-bearish count / 16Q baseline count."""
    flag = ((etf_share.diff() > 0) & (inst_value.diff() < 0) & (inst_count.diff() < 0)).astype(float)
    return _safe_div(flag.rolling(Y, min_periods=2).sum(), flag.rolling(Y4, min_periods=6).sum())


def f33_pfac_134_acceleration_phase_indicator_8q(etf_share: pd.Series, inst_shares: pd.Series) -> pd.Series:
    """Fraction of last 8Q where etf-concentration d2 > 0 — probability of acceleration phase."""
    r = _safe_div(etf_share, etf_share + inst_shares)
    d2 = r.diff().diff()
    flag = (d2 > 0).astype(float)
    return flag.rolling(Y2, min_periods=3).mean()


def f33_pfac_135_inflection_composite_4q(etf_share: pd.Series, inst_value: pd.Series, inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Sum 4Q of indicators where d2 of {etf_share, inst_value, put/call} changed sign."""
    pc = _safe_div(inst_puts, inst_calls)
    f1 = (np.sign(etf_share.diff().diff()) != np.sign(etf_share.diff().diff().shift(1))).astype(float)
    f2 = (np.sign(inst_value.diff().diff()) != np.sign(inst_value.diff().diff().shift(1))).astype(float)
    f3 = (np.sign(pc.diff().diff()) != np.sign(pc.diff().diff().shift(1))).astype(float)
    return (f1 + f2 + f3).rolling(Y, min_periods=2).sum()


def f33_pfac_136_quadratic_fit_composite_8q(etf_share: pd.Series, inst_value: pd.Series) -> pd.Series:
    """Mean of quadratic c2 of etf_share and -inst_value over 8Q."""
    return (_quadratic_c2(etf_share, Y2) + _quadratic_c2(-inst_value, Y2)) / 2.0


def f33_pfac_137_structural_break_composite_8q(etf_share: pd.Series, inst_value: pd.Series, inst_count: pd.Series) -> pd.Series:
    """Sum of structural-break scores across etf_share, -inst_value, -inst_count over 8Q."""
    return _structural_break_score(etf_share, Y2) + _structural_break_score(-inst_value, Y2) + _structural_break_score(-inst_count, Y2)


def f33_pfac_138_composite_jerk_index_4q(etf_share: pd.Series, inst_value: pd.Series, inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Mean 4Q of |3rd diff| across etf_share, inst_value, put/call."""
    pc = _safe_div(inst_puts, inst_calls)
    j = (etf_share.diff().diff().diff().abs() + inst_value.diff().diff().diff().abs() + pc.diff().diff().diff().abs()) / 3.0
    return j.rolling(Y, min_periods=2).mean()


def f33_pfac_139_cliff_edge_composite_count_4q(etf_share: pd.Series, inst_value: pd.Series, inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Count 4Q where any metric (etf_share/inst_value/put-call) has |1Q chg z|>2."""
    pc = _safe_div(inst_puts, inst_calls)
    z1 = _rolling_zscore(etf_share.diff(), Y4).abs()
    z2 = _rolling_zscore(inst_value.diff(), Y4).abs()
    z3 = _rolling_zscore(pc.diff(), Y4).abs()
    flag = ((z1 > 2.0) | (z2 > 2.0) | (z3 > 2.0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f33_pfac_140_passive_flow_vs_inst_flow_spread_4q(etf_flow: pd.Series, inst_value: pd.Series) -> pd.Series:
    """Mean 4Q of (etf_flow / |etf_flow|.rolling-mean - (-inst_value chg)/(|inst_value chg|).rolling-mean)."""
    e_norm = _safe_div(etf_flow, etf_flow.abs().rolling(Y, min_periods=2).mean())
    i_norm = _safe_div(-inst_value.diff(), inst_value.diff().abs().rolling(Y, min_periods=2).mean())
    return (e_norm - i_norm).rolling(Y, min_periods=2).mean()


def f33_pfac_141_composite_vs_self_baseline_8q(etf_share: pd.Series, inst_shares: pd.Series) -> pd.Series:
    """(Current etf-concentration z) - (mean 8Q z) — deviation from short-term baseline."""
    r = _safe_div(etf_share, etf_share + inst_shares)
    z = _rolling_zscore(r, Y4)
    return z - z.rolling(Y2, min_periods=3).mean()


def f33_pfac_142_accel_regime_change_count_16q(etf_share: pd.Series, inst_shares: pd.Series) -> pd.Series:
    """Count of sign changes of etf-concentration 4Q slope inside last 16Q."""
    r = _safe_div(etf_share, etf_share + inst_shares)
    sl = _rolling_slope(r, Y)
    flip = (np.sign(sl) != np.sign(sl.shift(1))).astype(float)
    return flip.rolling(Y4, min_periods=6).sum()


def f33_pfac_143_weighted_composite_metric_accel_4q(etf_share: pd.Series, inst_value: pd.Series, inst_count: pd.Series, inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Sum 4Q of (0.3*z(etf_share chg) + 0.3*z(-inst_value chg) + 0.2*z(-inst_count chg) + 0.2*z(put/call chg))."""
    pc = _safe_div(inst_puts, inst_calls)
    z = (
        0.3 * _rolling_zscore(etf_share.diff(), Y4)
        + 0.3 * _rolling_zscore(-inst_value.diff(), Y4)
        + 0.2 * _rolling_zscore(-inst_count.diff(), Y4)
        + 0.2 * _rolling_zscore(pc.diff(), Y4)
    )
    return z.rolling(Y, min_periods=2).sum()


def f33_pfac_144_dispersion_accel_metrics_4q(etf_share: pd.Series, inst_value: pd.Series, inst_count: pd.Series, inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Std across 4Q means of z-scores across passive-flow metrics."""
    pc = _safe_div(inst_puts, inst_calls)
    z1 = _rolling_zscore(etf_share.diff(), Y4).rolling(Y, min_periods=2).mean()
    z2 = _rolling_zscore(-inst_value.diff(), Y4).rolling(Y, min_periods=2).mean()
    z3 = _rolling_zscore(-inst_count.diff(), Y4).rolling(Y, min_periods=2).mean()
    z4 = _rolling_zscore(pc.diff(), Y4).rolling(Y, min_periods=2).mean()
    return pd.concat([z1, z2, z3, z4], axis=1).std(axis=1)


def f33_pfac_145_coincidence_index_z2_across_metrics_4q(etf_share: pd.Series, inst_value: pd.Series, inst_count: pd.Series, inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Count 4Q where ALL of {etf z>2, -inst_value z>2, -inst_count z>2, put-call z>2} hold."""
    pc = _safe_div(inst_puts, inst_calls)
    z1 = _rolling_zscore(etf_share.diff(), Y4)
    z2 = _rolling_zscore(-inst_value.diff(), Y4)
    z3 = _rolling_zscore(-inst_count.diff(), Y4)
    z4 = _rolling_zscore(pc.diff(), Y4)
    flag = ((z1 > 2.0) & (z2 > 2.0) & (z3 > 2.0) & (z4 > 2.0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f33_pfac_146_composite_passive_flow_escalation_4q(etf_share: pd.Series, inst_value: pd.Series, inst_count: pd.Series) -> pd.Series:
    """Mean 4Q of composite z divided by 16Q std — escalation rate."""
    z = _rolling_zscore(etf_share.diff(), Y4) + _rolling_zscore(-inst_value.diff(), Y4) + _rolling_zscore(-inst_count.diff(), Y4)
    return _safe_div(z.rolling(Y, min_periods=2).mean(), z.rolling(Y4, min_periods=6).std())


def f33_pfac_147_terminal_passive_flow_warning_composite_4q(etf_share: pd.Series, inst_value: pd.Series, inst_count: pd.Series, inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Sum 4Q of indicator (etf_share d2>0 AND inst_value d2<0 AND inst_count d2<0 AND put-call d2>0)."""
    pc = _safe_div(inst_puts, inst_calls)
    f = ((etf_share.diff().diff() > 0) & (inst_value.diff().diff() < 0) & (inst_count.diff().diff() < 0) & (pc.diff().diff() > 0)).astype(float)
    return f.rolling(Y, min_periods=2).sum()


def f33_pfac_148_cliff_edge_probability_8q(etf_share: pd.Series, inst_value: pd.Series, inst_count: pd.Series) -> pd.Series:
    """Fraction of last 8Q bars where any of {etf_share, -inst_value, -inst_count} chg z > 2."""
    z1 = _rolling_zscore(etf_share.diff(), Y4)
    z2 = _rolling_zscore(-inst_value.diff(), Y4)
    z3 = _rolling_zscore(-inst_count.diff(), Y4)
    flag = ((z1 > 2.0) | (z2 > 2.0) | (z3 > 2.0)).astype(float)
    return flag.rolling(Y2, min_periods=3).mean()


def f33_pfac_149_terminal_state_composite_score_4q(etf_share: pd.Series, inst_value: pd.Series, inst_count: pd.Series, inst_shares: pd.Series, inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Mean 4Q of sum of indicators (etf_share up + inst_value down + inst_count down + inst_shares down + put/call up)."""
    pc = _safe_div(inst_puts, inst_calls)
    score = (
        (etf_share.diff() > 0).astype(float)
        + (inst_value.diff() < 0).astype(float)
        + (inst_count.diff() < 0).astype(float)
        + (inst_shares.diff() < 0).astype(float)
        + (pc.diff() > 0).astype(float)
    )
    return score.rolling(Y, min_periods=2).mean()


def f33_pfac_150_final_passive_flow_accel_composite_8q(etf_share: pd.Series, etf_flow: pd.Series, inst_value: pd.Series, inst_count: pd.Series, inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """Mean 8Q of (z(etf_share chg) + z(etf_flow) + z(-inst_value chg) + z(-inst_count chg) + z(put/call chg))."""
    pc = _safe_div(inst_puts, inst_calls)
    z = (
        _rolling_zscore(etf_share.diff(), Y4)
        + _rolling_zscore(etf_flow, Y4)
        + _rolling_zscore(-inst_value.diff(), Y4)
        + _rolling_zscore(-inst_count.diff(), Y4)
        + _rolling_zscore(pc.diff(), Y4)
    )
    return z.rolling(Y2, min_periods=3).mean()


# ============================================================
#                        REGISTRY
# ============================================================

PASSIVE_FLOW_ACCELERATION_BASE_REGISTRY_076_150 = {
    "f33_pfac_076_etf_share_inst_value_correlation_8q": {"inputs": ["etf_share", "inst_value"], "func": f33_pfac_076_etf_share_inst_value_correlation_8q},
    "f33_pfac_077_etf_share_inst_count_correlation_8q": {"inputs": ["etf_share", "inst_count"], "func": f33_pfac_077_etf_share_inst_count_correlation_8q},
    "f33_pfac_078_etf_inflow_inst_outflow_simultaneity_count_8q": {"inputs": ["etf_flow", "inst_value"], "func": f33_pfac_078_etf_inflow_inst_outflow_simultaneity_count_8q},
    "f33_pfac_079_etf_vs_inst_slope_spread_4q": {"inputs": ["etf_share", "inst_value"], "func": f33_pfac_079_etf_vs_inst_slope_spread_4q},
    "f33_pfac_080_etf_vs_inst_slope_spread_12q": {"inputs": ["etf_share", "inst_value"], "func": f33_pfac_080_etf_vs_inst_slope_spread_12q},
    "f33_pfac_081_acceleration_of_etf_minus_inst_ratio_16q": {"inputs": ["etf_share", "inst_value"], "func": f33_pfac_081_acceleration_of_etf_minus_inst_ratio_16q},
    "f33_pfac_082_d2_etf_concentration_vs_d2_inst_concentration": {"inputs": ["etf_share", "inst_shares", "inst_value", "inst_count"], "func": f33_pfac_082_d2_etf_concentration_vs_d2_inst_concentration},
    "f33_pfac_083_compound_etf_gain_2sigma_inst_loss_2sigma_4q": {"inputs": ["etf_flow", "inst_value"], "func": f33_pfac_083_compound_etf_gain_2sigma_inst_loss_2sigma_4q},
    "f33_pfac_084_spread_cumulative_integral_8q": {"inputs": ["etf_share", "inst_value"], "func": f33_pfac_084_spread_cumulative_integral_8q},
    "f33_pfac_085_spread_tail_event_count_16q": {"inputs": ["etf_share", "inst_value"], "func": f33_pfac_085_spread_tail_event_count_16q},
    "f33_pfac_086_spread_quadratic_c2_8q": {"inputs": ["etf_share", "inst_value"], "func": f33_pfac_086_spread_quadratic_c2_8q},
    "f33_pfac_087_spread_inflection_count_8q": {"inputs": ["etf_share", "inst_value"], "func": f33_pfac_087_spread_inflection_count_8q},
    "f33_pfac_088_spread_structural_break_8q": {"inputs": ["etf_share", "inst_value"], "func": f33_pfac_088_spread_structural_break_8q},
    "f33_pfac_089_spread_arc_area_8q": {"inputs": ["etf_share", "inst_value"], "func": f33_pfac_089_spread_arc_area_8q},
    "f33_pfac_090_log_spread_slope_4q_minus_12q": {"inputs": ["etf_share", "inst_value"], "func": f33_pfac_090_log_spread_slope_4q_minus_12q},
    "f33_pfac_091_spread_latest_to_16q_max": {"inputs": ["etf_share", "inst_value"], "func": f33_pfac_091_spread_latest_to_16q_max},
    "f33_pfac_092_quarters_since_spread_accelerated": {"inputs": ["etf_share", "inst_value"], "func": f33_pfac_092_quarters_since_spread_accelerated},
    "f33_pfac_093_spread_weighted_composite_z_4q": {"inputs": ["etf_share", "inst_value", "inst_count"], "func": f33_pfac_093_spread_weighted_composite_z_4q},
    "f33_pfac_094_spread_cliff_count_16q": {"inputs": ["etf_share", "inst_value"], "func": f33_pfac_094_spread_cliff_count_16q},
    "f33_pfac_095_ratio_inst_loss_to_etf_gain_4q": {"inputs": ["inst_value", "etf_flow"], "func": f33_pfac_095_ratio_inst_loss_to_etf_gain_4q},
    "f33_pfac_096_passive_to_active_ratio_accel_16q": {"inputs": ["etf_share", "inst_shares"], "func": f33_pfac_096_passive_to_active_ratio_accel_16q},
    "f33_pfac_097_compound_spread_divergence_inst_count_down_4q": {"inputs": ["etf_share", "inst_value", "inst_count"], "func": f33_pfac_097_compound_spread_divergence_inst_count_down_4q},
    "f33_pfac_098_d2_spread_z_16q": {"inputs": ["etf_share", "inst_value"], "func": f33_pfac_098_d2_spread_z_16q},
    "f33_pfac_099_composite_spread_divergence_accel_8q": {"inputs": ["etf_share", "inst_value"], "func": f33_pfac_099_composite_spread_divergence_accel_8q},
    "f33_pfac_100_composite_spread_divergence_escalation_4q": {"inputs": ["etf_share", "inst_value", "inst_count"], "func": f33_pfac_100_composite_spread_divergence_escalation_4q},
    "f33_pfac_101_inst_puts_cliff_8q": {"inputs": ["inst_puts"], "func": f33_pfac_101_inst_puts_cliff_8q},
    "f33_pfac_102_inst_puts_zscore_16q": {"inputs": ["inst_puts"], "func": f33_pfac_102_inst_puts_zscore_16q},
    "f33_pfac_103_inst_calls_cliff_8q": {"inputs": ["inst_calls"], "func": f33_pfac_103_inst_calls_cliff_8q},
    "f33_pfac_104_inst_calls_zscore_16q": {"inputs": ["inst_calls"], "func": f33_pfac_104_inst_calls_zscore_16q},
    "f33_pfac_105_put_call_ratio_accel_z_16q": {"inputs": ["inst_puts", "inst_calls"], "func": f33_pfac_105_put_call_ratio_accel_z_16q},
    "f33_pfac_106_put_call_cliff_jump_8q": {"inputs": ["inst_puts", "inst_calls"], "func": f33_pfac_106_put_call_cliff_jump_8q},
    "f33_pfac_107_put_call_structural_break_8q": {"inputs": ["inst_puts", "inst_calls"], "func": f33_pfac_107_put_call_structural_break_8q},
    "f33_pfac_108_compound_puts_up_calls_down_4q": {"inputs": ["inst_puts", "inst_calls"], "func": f33_pfac_108_compound_puts_up_calls_down_4q},
    "f33_pfac_109_compound_puts_up_inst_count_down_4q": {"inputs": ["inst_puts", "inst_count"], "func": f33_pfac_109_compound_puts_up_inst_count_down_4q},
    "f33_pfac_110_puts_to_inst_count_accel_z": {"inputs": ["inst_puts", "inst_count"], "func": f33_pfac_110_puts_to_inst_count_accel_z},
    "f33_pfac_111_calls_to_inst_count_accel_z": {"inputs": ["inst_calls", "inst_count"], "func": f33_pfac_111_calls_to_inst_count_accel_z},
    "f33_pfac_112_d2_log_put_call_z_16q": {"inputs": ["inst_puts", "inst_calls"], "func": f33_pfac_112_d2_log_put_call_z_16q},
    "f33_pfac_113_put_call_cumulative_z_8q": {"inputs": ["inst_puts", "inst_calls"], "func": f33_pfac_113_put_call_cumulative_z_8q},
    "f33_pfac_114_put_call_inflection_sign_flip_8q": {"inputs": ["inst_puts", "inst_calls"], "func": f33_pfac_114_put_call_inflection_sign_flip_8q},
    "f33_pfac_115_put_call_exp_fit_r2_8q": {"inputs": ["inst_puts", "inst_calls"], "func": f33_pfac_115_put_call_exp_fit_r2_8q},
    "f33_pfac_116_put_call_latest_to_16q_max": {"inputs": ["inst_puts", "inst_calls"], "func": f33_pfac_116_put_call_latest_to_16q_max},
    "f33_pfac_117_quarters_since_put_call_accelerated": {"inputs": ["inst_puts", "inst_calls"], "func": f33_pfac_117_quarters_since_put_call_accelerated},
    "f33_pfac_118_put_call_2sigma_count_16q": {"inputs": ["inst_puts", "inst_calls"], "func": f33_pfac_118_put_call_2sigma_count_16q},
    "f33_pfac_119_compound_high_put_call_etf_flow_down_4q": {"inputs": ["inst_puts", "inst_calls", "etf_flow"], "func": f33_pfac_119_compound_high_put_call_etf_flow_down_4q},
    "f33_pfac_120_compound_high_put_call_inst_value_down_4q": {"inputs": ["inst_puts", "inst_calls", "inst_value"], "func": f33_pfac_120_compound_high_put_call_inst_value_down_4q},
    "f33_pfac_121_put_call_slope_4q_minus_12q": {"inputs": ["inst_puts", "inst_calls"], "func": f33_pfac_121_put_call_slope_4q_minus_12q},
    "f33_pfac_122_composite_derivative_stress_accel_4q": {"inputs": ["inst_puts", "inst_calls", "inst_count"], "func": f33_pfac_122_composite_derivative_stress_accel_4q},
    "f33_pfac_123_d2_put_call_spread_z": {"inputs": ["inst_puts", "inst_calls"], "func": f33_pfac_123_d2_put_call_spread_z},
    "f33_pfac_124_put_call_arc_area_above_8q_linear": {"inputs": ["inst_puts", "inst_calls"], "func": f33_pfac_124_put_call_arc_area_above_8q_linear},
    "f33_pfac_125_composite_derivatives_positioning_accel_4q": {"inputs": ["inst_puts", "inst_calls", "inst_count", "inst_value"], "func": f33_pfac_125_composite_derivatives_positioning_accel_4q},
    "f33_pfac_126_multimetric_accel_coincidence_count_4q": {"inputs": ["etf_share", "inst_value", "inst_puts", "inst_calls"], "func": f33_pfac_126_multimetric_accel_coincidence_count_4q},
    "f33_pfac_127_compound_etf_conc_up_inst_exit_put_call_up_4q": {"inputs": ["etf_share", "inst_shares", "inst_count", "inst_puts", "inst_calls"], "func": f33_pfac_127_compound_etf_conc_up_inst_exit_put_call_up_4q},
    "f33_pfac_128_weighted_composite_z_etf_inst_putcall_4q": {"inputs": ["etf_share", "inst_value", "inst_puts", "inst_calls"], "func": f33_pfac_128_weighted_composite_z_etf_inst_putcall_4q},
    "f33_pfac_129_composite_stress_accel_4q": {"inputs": ["etf_share", "inst_value", "inst_count"], "func": f33_pfac_129_composite_stress_accel_4q},
    "f33_pfac_130_variance_explained_by_passive_flow_accel_8q": {"inputs": ["etf_share", "inst_value"], "func": f33_pfac_130_variance_explained_by_passive_flow_accel_8q},
    "f33_pfac_131_multivariate_accel_outlier_z_4q": {"inputs": ["etf_share", "inst_value", "inst_count", "inst_puts", "inst_calls"], "func": f33_pfac_131_multivariate_accel_outlier_z_4q},
    "f33_pfac_132_cumulative_passive_flow_accel_index_8q": {"inputs": ["etf_share", "inst_value", "inst_count"], "func": f33_pfac_132_cumulative_passive_flow_accel_index_8q},
    "f33_pfac_133_compound_passive_bearish_to_16q_baseline": {"inputs": ["etf_share", "inst_value", "inst_count"], "func": f33_pfac_133_compound_passive_bearish_to_16q_baseline},
    "f33_pfac_134_acceleration_phase_indicator_8q": {"inputs": ["etf_share", "inst_shares"], "func": f33_pfac_134_acceleration_phase_indicator_8q},
    "f33_pfac_135_inflection_composite_4q": {"inputs": ["etf_share", "inst_value", "inst_puts", "inst_calls"], "func": f33_pfac_135_inflection_composite_4q},
    "f33_pfac_136_quadratic_fit_composite_8q": {"inputs": ["etf_share", "inst_value"], "func": f33_pfac_136_quadratic_fit_composite_8q},
    "f33_pfac_137_structural_break_composite_8q": {"inputs": ["etf_share", "inst_value", "inst_count"], "func": f33_pfac_137_structural_break_composite_8q},
    "f33_pfac_138_composite_jerk_index_4q": {"inputs": ["etf_share", "inst_value", "inst_puts", "inst_calls"], "func": f33_pfac_138_composite_jerk_index_4q},
    "f33_pfac_139_cliff_edge_composite_count_4q": {"inputs": ["etf_share", "inst_value", "inst_puts", "inst_calls"], "func": f33_pfac_139_cliff_edge_composite_count_4q},
    "f33_pfac_140_passive_flow_vs_inst_flow_spread_4q": {"inputs": ["etf_flow", "inst_value"], "func": f33_pfac_140_passive_flow_vs_inst_flow_spread_4q},
    "f33_pfac_141_composite_vs_self_baseline_8q": {"inputs": ["etf_share", "inst_shares"], "func": f33_pfac_141_composite_vs_self_baseline_8q},
    "f33_pfac_142_accel_regime_change_count_16q": {"inputs": ["etf_share", "inst_shares"], "func": f33_pfac_142_accel_regime_change_count_16q},
    "f33_pfac_143_weighted_composite_metric_accel_4q": {"inputs": ["etf_share", "inst_value", "inst_count", "inst_puts", "inst_calls"], "func": f33_pfac_143_weighted_composite_metric_accel_4q},
    "f33_pfac_144_dispersion_accel_metrics_4q": {"inputs": ["etf_share", "inst_value", "inst_count", "inst_puts", "inst_calls"], "func": f33_pfac_144_dispersion_accel_metrics_4q},
    "f33_pfac_145_coincidence_index_z2_across_metrics_4q": {"inputs": ["etf_share", "inst_value", "inst_count", "inst_puts", "inst_calls"], "func": f33_pfac_145_coincidence_index_z2_across_metrics_4q},
    "f33_pfac_146_composite_passive_flow_escalation_4q": {"inputs": ["etf_share", "inst_value", "inst_count"], "func": f33_pfac_146_composite_passive_flow_escalation_4q},
    "f33_pfac_147_terminal_passive_flow_warning_composite_4q": {"inputs": ["etf_share", "inst_value", "inst_count", "inst_puts", "inst_calls"], "func": f33_pfac_147_terminal_passive_flow_warning_composite_4q},
    "f33_pfac_148_cliff_edge_probability_8q": {"inputs": ["etf_share", "inst_value", "inst_count"], "func": f33_pfac_148_cliff_edge_probability_8q},
    "f33_pfac_149_terminal_state_composite_score_4q": {"inputs": ["etf_share", "inst_value", "inst_count", "inst_shares", "inst_puts", "inst_calls"], "func": f33_pfac_149_terminal_state_composite_score_4q},
    "f33_pfac_150_final_passive_flow_accel_composite_8q": {"inputs": ["etf_share", "etf_flow", "inst_value", "inst_count", "inst_puts", "inst_calls"], "func": f33_pfac_150_final_passive_flow_accel_composite_8q},
}
