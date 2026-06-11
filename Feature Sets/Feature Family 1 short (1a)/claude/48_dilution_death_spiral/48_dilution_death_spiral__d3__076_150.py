"""dilution_death_spiral d1 features 076-150 — order-3 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


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


def _safe_log(s, eps=1e-12):
    if isinstance(s, pd.Series):
        return np.log(s.where(s > eps, np.nan))
    arr = np.where(s > eps, s, np.nan)
    return np.log(arr)


def _safe_log_abs(s, eps=1e-12):
    if isinstance(s, pd.Series):
        a = s.abs()
        return np.log(a.where(a > eps, np.nan))
    a = np.abs(s)
    return np.log(np.where(a > eps, a, np.nan))


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


def _ttm(s):
    return s.rolling(4, min_periods=1).sum()


def _avg4(s):
    return s.rolling(4, min_periods=1).mean()


def _yoy(s):
    return s - s.shift(4)


def _yoy_pct(s):
    return _safe_div(s - s.shift(4), s.shift(4).abs())


def _qoq(s):
    return s.diff()


def _qoq_pct(s):
    return _safe_div(s.diff(), s.shift(1).abs())


def _consec_true_streak(b):
    b = b.fillna(False).astype(bool).astype(int)
    grp = (b == 0).cumsum()
    return b.groupby(grp).cumsum()


def _max_consec_true_window(b, window):
    b = b.fillna(False).astype(bool).astype(int)

    def _mx(w):
        best = cur = 0
        for v in w:
            if v > 0.5:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return best
    return b.rolling(window, min_periods=1).apply(_mx, raw=True)


def _quarters_since_true(b):
    b = b.fillna(False).astype(bool).astype(int)
    out = np.full(len(b), np.nan)
    last = -1
    for i, v in enumerate(b.values):
        if v > 0.5:
            last = i
            out[i] = 0.0
        elif last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=b.index)


def f48_ddsp_076_price_x_shares_decoupling_d3(marketcap, close, sharesbas):
    return (_safe_log(marketcap) - _safe_log(close * sharesbas)).diff().diff().diff()

def f48_ddsp_077_effective_share_count_proxy_d3(marketcap, close):
    return _safe_div(marketcap, close).diff().diff().diff()

def f48_ddsp_078_effective_share_count_qoq_pct_d3(marketcap, close):
    eff = _safe_div(marketcap, close)
    return _safe_div(eff.diff(), eff.shift(1).abs()).diff().diff().diff()

def f48_ddsp_079_issuance_per_marketcap_qoq_d3(sharesbas, marketcap):
    return _safe_div(sharesbas.diff(), marketcap.shift(1).abs()).diff().diff().diff()

def f48_ddsp_080_issuance_per_marketcap_yoy_d3(sharesbas, marketcap):
    return _safe_div(sharesbas.diff(4), marketcap.shift(4).abs()).diff().diff().diff()

def f48_ddsp_081_equity_dilution_yoy_d3(equity, shareswa):
    return (_yoy_pct(equity) - _yoy_pct(shareswa)).diff().diff().diff()

def f48_ddsp_082_equity_per_share_d3(equity, shareswadil):
    return _safe_div(equity, shareswadil).diff().diff().diff()

def f48_ddsp_083_equity_per_share_qoq_pct_d3(equity, shareswadil):
    eps_ = _safe_div(equity, shareswadil)
    return _safe_div(eps_.diff(), eps_.shift(1).abs()).diff().diff().diff()

def f48_ddsp_084_equity_per_share_yoy_pct_d3(equity, shareswadil):
    eps_ = _safe_div(equity, shareswadil)
    return _safe_div(eps_ - eps_.shift(4), eps_.shift(4).abs()).diff().diff().diff()

def f48_ddsp_085_equity_per_share_drawdown_from_8q_max_d3(equity, shareswadil):
    eps_ = _safe_div(equity, shareswadil)
    rmax = eps_.rolling(8, min_periods=3).max()
    return (_safe_div(eps_, rmax) - 1.0).diff().diff().diff()

def f48_ddsp_086_revenue_per_share_d3(revenue, shareswadil):
    return _safe_div(revenue, shareswadil).diff().diff().diff()

def f48_ddsp_087_revenue_per_share_qoq_pct_d3(revenue, shareswadil):
    rps = _safe_div(revenue, shareswadil)
    return _safe_div(rps.diff(), rps.shift(1).abs()).diff().diff().diff()

def f48_ddsp_088_revenue_per_share_yoy_pct_d3(revenue, shareswadil):
    rps = _safe_div(revenue, shareswadil)
    return _safe_div(rps - rps.shift(4), rps.shift(4).abs()).diff().diff().diff()

def f48_ddsp_089_revenue_per_share_drawdown_from_8q_max_d3(revenue, shareswadil):
    rps = _safe_div(revenue, shareswadil)
    rmax = rps.rolling(8, min_periods=3).max()
    return (_safe_div(rps, rmax) - 1.0).diff().diff().diff()

def f48_ddsp_090_dilution_severity_index_d3(shareswadil, revenue):
    return (_yoy_pct(shareswadil) - _yoy_pct(revenue)).diff().diff().diff()

def f48_ddsp_091_dilution_destroying_rev_per_share_indicator_d3(revenue, shareswadil):
    rps = _safe_div(revenue, shareswadil)
    rps_yoy = _safe_div(rps - rps.shift(4), rps.shift(4).abs())
    swd_yoy = _yoy_pct(shareswadil)
    return ((rps_yoy < 0).fillna(False) & (swd_yoy > 0).fillna(False)).astype(float).diff().diff().diff()

def f48_ddsp_092_log_marketcap_zscore_8q_d3(marketcap):
    return _rolling_zscore(_safe_log(marketcap), 8, min_periods=3).diff().diff().diff()

def f48_ddsp_093_marketcap_per_share_decline_streak_d3(marketcap, sharesbas):
    cur = _safe_div(marketcap, sharesbas.shift(1))
    prev = _safe_div(marketcap, sharesbas).shift(1)
    return _consec_true_streak(cur < prev).diff().diff().diff()

def f48_ddsp_094_spiral_economic_loss_proxy_d3(equity, shareswadil, sharesbas):
    eps_ = _safe_div(equity, shareswadil)
    eps_yoy = _safe_div(eps_ - eps_.shift(4), eps_.shift(4).abs())
    return (eps_yoy * _yoy_pct(sharesbas)).diff().diff().diff()

def f48_ddsp_095_dilution_persistence_with_marketcap_decline_4q_d3(sharesbas, marketcap):
    a = _qoq_pct(sharesbas) > 0
    b = _qoq_pct(marketcap) < 0
    ind = (a.fillna(False) & b.fillna(False)).astype(float)
    return ind.rolling(4, min_periods=2).sum().diff().diff().diff()

def f48_ddsp_096_sharefactor_qoq_change_d3(sharefactor):
    return sharefactor.diff().diff().diff().diff()

def f48_ddsp_097_sharefactor_yoy_change_d3(sharefactor):
    return (sharefactor - sharefactor.shift(4)).diff().diff().diff()

def f48_ddsp_098_sharefactor_reverse_split_indicator_d3(sharefactor):
    return (sharefactor < sharefactor.shift(1) * 0.8).fillna(False).astype(float).diff().diff().diff()

def f48_ddsp_099_sharefactor_split_indicator_d3(sharefactor):
    return (sharefactor > sharefactor.shift(1) * 1.2).fillna(False).astype(float).diff().diff().diff()

def f48_ddsp_100_reverse_split_count_8q_d3(sharefactor):
    ind = (sharefactor < sharefactor.shift(1) * 0.8).fillna(False).astype(float)
    return ind.rolling(8, min_periods=3).sum().diff().diff().diff()

def f48_ddsp_101_reverse_split_count_12q_d3(sharefactor):
    ind = (sharefactor < sharefactor.shift(1) * 0.8).fillna(False).astype(float)
    return ind.rolling(12, min_periods=4).sum().diff().diff().diff()

def f48_ddsp_102_quarters_since_last_reverse_split_d3(sharefactor):
    ind = (sharefactor < sharefactor.shift(1) * 0.8)
    return _quarters_since_true(ind).diff().diff().diff()

def f48_ddsp_103_reverse_split_after_issuance_indicator_d3(sharefactor, sharesbas):
    rs = (sharefactor < sharefactor.shift(1) * 0.8).fillna(False)
    iss = (_yoy_pct(sharesbas).shift(1) > 0.20).fillna(False)
    return (rs & iss).astype(float).diff().diff().diff()

def f48_ddsp_104_reverse_split_followed_by_issuance_indicator_d3(sharefactor, sharesbas):
    rs_lag = (sharefactor < sharefactor.shift(1) * 0.8).shift(4).fillna(False)
    iss = (sharesbas.diff(4) > 0).fillna(False)
    return (rs_lag & iss).astype(float).diff().diff().diff()

def f48_ddsp_105_raw_shares_post_reverse_split_growth_d3(sharesbas, sharefactor):
    num = _safe_div(sharesbas.diff(), sharesbas.shift(1).abs())
    den = _safe_div(sharefactor.diff(), sharefactor.shift(1).abs()) + 1.0
    return _safe_div(num, den).diff().diff().diff()

def f48_ddsp_106_effective_dilution_after_split_d3(sharesbas, sharefactor):
    return (_yoy_pct(sharesbas) + (sharefactor - sharefactor.shift(4)).fillna(0.0) * 0.0).diff().diff().diff()

def f48_ddsp_107_compound_dilution_8q_d3(sharesbas):
    return (_safe_log(sharesbas) - _safe_log(sharesbas.shift(8))).diff().diff().diff()

def f48_ddsp_108_compound_dilution_12q_d3(sharesbas):
    return (_safe_log(sharesbas) - _safe_log(sharesbas.shift(12))).diff().diff().diff()

def f48_ddsp_109_compound_dilution_16q_d3(sharesbas):
    return (_safe_log(sharesbas) - _safe_log(sharesbas.shift(16))).diff().diff().diff()

def f48_ddsp_110_compound_dilution_minus_compound_revenue_growth_8q_d3(sharesbas, revenue):
    return ((_safe_log(sharesbas) - _safe_log(sharesbas.shift(8))) - (_safe_log(revenue) - _safe_log(revenue.shift(8)))).diff().diff().diff()

def f48_ddsp_111_compound_dilution_when_price_falling_8q_d3(sharesbas, close):
    comp = _safe_log(sharesbas) - _safe_log(sharesbas.shift(8))
    return (comp * (_yoy_pct(close) < 0).fillna(False).astype(float)).diff().diff().diff()

def f48_ddsp_112_corporate_action_dilution_proxy_8q_d3(sharefactor, sharesbas):
    rs = (sharefactor < sharefactor.shift(1) * 0.8).fillna(False).astype(float)
    rs_count = rs.rolling(8, min_periods=3).sum()
    big_iss = (_yoy_pct(sharesbas) > 0.20).fillna(False).astype(float)
    return (rs_count + big_iss).diff().diff().diff()

def f48_ddsp_113_share_supply_shock_indicator_d3(sharesbas):
    return (_qoq_pct(sharesbas) > 0.25).fillna(False).astype(float).diff().diff().diff()

def f48_ddsp_114_share_supply_shock_count_12q_d3(sharesbas):
    ind = (_qoq_pct(sharesbas) > 0.25).fillna(False).astype(float)
    return ind.rolling(12, min_periods=4).sum().diff().diff().diff()

def f48_ddsp_115_share_supply_shock_after_drawdown_indicator_d3(sharesbas, close):
    shock = (_qoq_pct(sharesbas) > 0.25).fillna(False).astype(float)
    rmax = close.rolling(4, min_periods=2).max()
    dd = _safe_div(close, rmax) - 1.0
    return (shock * (dd < -0.2).fillna(False).astype(float)).diff().diff().diff()

def f48_ddsp_116_death_spiral_score_d3(sharesbas, close):
    rmax = close.rolling(8, min_periods=3).max()
    dd = _safe_div(close, rmax) - 1.0
    s = _qoq_pct(sharesbas) * (-_qoq_pct(close))
    return s.where(dd < -0.5, 0.0).diff().diff().diff()

def f48_ddsp_117_death_spiral_score_8q_sum_d3(sharesbas, close):
    rmax = close.rolling(8, min_periods=3).max()
    dd = _safe_div(close, rmax) - 1.0
    s = _qoq_pct(sharesbas) * (-_qoq_pct(close))
    ds = s.where(dd < -0.5, 0.0)
    return ds.rolling(8, min_periods=3).sum().diff().diff().diff()

def f48_ddsp_118_death_spiral_score_yoy_d3(sharesbas, close):
    rmax = close.rolling(8, min_periods=3).max()
    dd = _safe_div(close, rmax) - 1.0
    s = _qoq_pct(sharesbas) * (-_qoq_pct(close))
    ds = s.where(dd < -0.5, 0.0)
    return ds.diff(4).diff().diff().diff()

def f48_ddsp_119_death_spiral_active_indicator_d3(sharesbas, close):
    rmax = close.rolling(8, min_periods=3).max()
    dd = _safe_div(close, rmax) - 1.0
    return ((dd < -0.5).fillna(False) & (_yoy_pct(sharesbas) > 0.20).fillna(False)).astype(float).diff().diff().diff()

def f48_ddsp_120_death_spiral_active_count_8q_d3(sharesbas, close):
    rmax = close.rolling(8, min_periods=3).max()
    dd = _safe_div(close, rmax) - 1.0
    ind = ((dd < -0.5).fillna(False) & (_yoy_pct(sharesbas) > 0.20).fillna(False)).astype(float)
    return ind.rolling(8, min_periods=3).sum().diff().diff().diff()

def f48_ddsp_121_death_spiral_active_count_12q_d3(sharesbas, close):
    rmax = close.rolling(8, min_periods=3).max()
    dd = _safe_div(close, rmax) - 1.0
    ind = ((dd < -0.5).fillna(False) & (_yoy_pct(sharesbas) > 0.20).fillna(False)).astype(float)
    return ind.rolling(12, min_periods=4).sum().diff().diff().diff()

def f48_ddsp_122_death_spiral_active_consec_streak_d3(sharesbas, close):
    rmax = close.rolling(8, min_periods=3).max()
    dd = _safe_div(close, rmax) - 1.0
    ind = (dd < -0.5).fillna(False) & (_yoy_pct(sharesbas) > 0.20).fillna(False)
    return _consec_true_streak(ind).diff().diff().diff()

def f48_ddsp_123_spiral_severity_index_d3(sharesbas, close):
    comp = _safe_log(sharesbas) - _safe_log(sharesbas.shift(4))
    rmax = close.rolling(4, min_periods=2).max()
    dd = (_safe_div(close, rmax) - 1.0).abs()
    return (comp * dd).diff().diff().diff()

def f48_ddsp_124_spiral_severity_index_8q_sum_d3(sharesbas, close):
    comp = _safe_log(sharesbas) - _safe_log(sharesbas.shift(4))
    rmax = close.rolling(4, min_periods=2).max()
    dd = (_safe_div(close, rmax) - 1.0).abs()
    sev = comp * dd
    return sev.rolling(8, min_periods=3).sum().diff().diff().diff()

def f48_ddsp_125_spiral_severity_index_zscore_8q_d3(sharesbas, close):
    comp = _safe_log(sharesbas) - _safe_log(sharesbas.shift(4))
    rmax = close.rolling(4, min_periods=2).max()
    dd = (_safe_div(close, rmax) - 1.0).abs()
    sev = comp * dd
    return _rolling_zscore(sev, 8, min_periods=3).diff().diff().diff()

def f48_ddsp_126_spiral_severity_8q_slope_d3(sharesbas, close):
    comp = _safe_log(sharesbas) - _safe_log(sharesbas.shift(4))
    rmax = close.rolling(4, min_periods=2).max()
    dd = (_safe_div(close, rmax) - 1.0).abs()
    sev = comp * dd
    return _rolling_slope(sev, 8, min_periods=3).diff().diff().diff()

def f48_ddsp_127_spiral_breach_of_8q_max_indicator_d3(sharesbas, close):
    comp = _safe_log(sharesbas) - _safe_log(sharesbas.shift(4))
    rmax = close.rolling(4, min_periods=2).max()
    dd = (_safe_div(close, rmax) - 1.0).abs()
    sev = comp * dd
    prior_max = sev.rolling(8, min_periods=3).max().shift(1)
    return (sev > prior_max).fillna(False).astype(float).diff().diff().diff()

def f48_ddsp_128_spiral_persistence_above_median_8q_d3(sharesbas, close):
    comp = _safe_log(sharesbas) - _safe_log(sharesbas.shift(4))
    rmax = close.rolling(4, min_periods=2).max()
    dd = (_safe_div(close, rmax) - 1.0).abs()
    sev = comp * dd
    med = sev.rolling(8, min_periods=3).median()
    ind = (sev > med).fillna(False).astype(float)
    return ind.rolling(8, min_periods=3).mean().diff().diff().diff()

def f48_ddsp_129_dilution_drawdown_co_movement_index_8q_d3(sharesbas, close):
    a = _qoq_pct(close)
    b = -_qoq_pct(sharesbas)
    return a.rolling(8, min_periods=4).corr(b).diff().diff().diff()

def f48_ddsp_130_dilution_drawdown_co_movement_index_12q_d3(sharesbas, close):
    a = _qoq_pct(close)
    b = -_qoq_pct(sharesbas)
    return a.rolling(12, min_periods=5).corr(b).diff().diff().diff()

def f48_ddsp_131_issuance_into_weakness_8q_indicator_d3(sharesbas, close):
    a = _qoq_pct(sharesbas) > 0.02
    b = _qoq_pct(close) < 0
    ind = (a.fillna(False) & b.fillna(False)).astype(float)
    count = ind.rolling(8, min_periods=3).sum()
    return (count >= 4).astype(float).diff().diff().diff()

def f48_ddsp_132_spiral_with_revenue_collapse_indicator_d3(sharesbas, close, revenue):
    rmax = close.rolling(8, min_periods=3).max()
    dd = _safe_div(close, rmax) - 1.0
    active = (dd < -0.5).fillna(False) & (_yoy_pct(sharesbas) > 0.20).fillna(False)
    rev_collapse = (_yoy_pct(revenue) < -0.10).fillna(False)
    return (active & rev_collapse).astype(float).diff().diff().diff()

def f48_ddsp_133_spiral_with_equity_collapse_indicator_d3(sharesbas, close, equity):
    rmax = close.rolling(8, min_periods=3).max()
    dd = _safe_div(close, rmax) - 1.0
    active = (dd < -0.5).fillna(False) & (_yoy_pct(sharesbas) > 0.20).fillna(False)
    eq_collapse = (_yoy_pct(equity) < -0.10).fillna(False)
    return (active & eq_collapse).astype(float).diff().diff().diff()

def f48_ddsp_134_spiral_with_negative_ncfo_indicator_d3(sharesbas, close, ncfo):
    rmax = close.rolling(8, min_periods=3).max()
    dd = _safe_div(close, rmax) - 1.0
    active = (dd < -0.5).fillna(False) & (_yoy_pct(sharesbas) > 0.20).fillna(False)
    neg_cf = (ncfo < 0).fillna(False)
    return (active & neg_cf).astype(float).diff().diff().diff()

def f48_ddsp_135_dilution_velocity_d3(sharesbas):
    y = _yoy_pct(sharesbas)
    return (y - y.shift(4)).diff().diff().diff()

def f48_ddsp_136_dilution_acceleration_d3(sharesbas):
    y = _yoy_pct(sharesbas)
    return (y - y.shift(4)).diff().diff().diff().diff()

def f48_ddsp_137_dilution_jerk_d3(sharesbas):
    y = _yoy_pct(sharesbas)
    return (y - y.shift(4)).diff().diff().diff().diff().diff()

def f48_ddsp_138_dilution_after_50pct_drawdown_indicator_d3(sharesbas, close):
    rmax = close.rolling(8, min_periods=3).max()
    dd = _safe_div(close, rmax) - 1.0
    a = _qoq_pct(sharesbas) > 0.05
    return (a.fillna(False) & (dd < -0.5).fillna(False)).astype(float).diff().diff().diff()

def f48_ddsp_139_dilution_after_80pct_drawdown_indicator_d3(sharesbas, close):
    rmax = close.rolling(8, min_periods=3).max()
    dd = _safe_div(close, rmax) - 1.0
    a = _qoq_pct(sharesbas) > 0.05
    return (a.fillna(False) & (dd < -0.8).fillna(False)).astype(float).diff().diff().diff()

def f48_ddsp_140_dilution_during_marketcap_drawdown_persistence_8q_d3(sharesbas, marketcap):
    rmax = marketcap.rolling(8, min_periods=3).max()
    dd = _safe_div(marketcap, rmax) - 1.0
    a = _qoq_pct(sharesbas) > 0
    ind = (a.fillna(False) & (dd < -0.3).fillna(False)).astype(float)
    return ind.rolling(8, min_periods=3).sum().diff().diff().diff()

def f48_ddsp_141_extreme_dilution_indicator_d3(sharesbas):
    return (_yoy_pct(sharesbas) > 0.50).fillna(False).astype(float).diff().diff().diff()

def f48_ddsp_142_extreme_dilution_count_8q_d3(sharesbas):
    ind = (_yoy_pct(sharesbas) > 0.50).fillna(False).astype(float)
    return ind.rolling(8, min_periods=3).sum().diff().diff().diff()

def f48_ddsp_143_extreme_dilution_count_12q_d3(sharesbas):
    ind = (_yoy_pct(sharesbas) > 0.50).fillna(False).astype(float)
    return ind.rolling(12, min_periods=4).sum().diff().diff().diff()

def f48_ddsp_144_compound_dilution_above_100pct_indicator_8q_d3(sharesbas):
    comp = _safe_log(sharesbas) - _safe_log(sharesbas.shift(8))
    return (comp > np.log(2.0)).fillna(False).astype(float).diff().diff().diff()

def f48_ddsp_145_compound_dilution_above_200pct_indicator_8q_d3(sharesbas):
    comp = _safe_log(sharesbas) - _safe_log(sharesbas.shift(8))
    return (comp > np.log(3.0)).fillna(False).astype(float).diff().diff().diff()

def f48_ddsp_146_compound_dilution_above_500pct_indicator_12q_d3(sharesbas):
    comp = _safe_log(sharesbas) - _safe_log(sharesbas.shift(12))
    return (comp > np.log(6.0)).fillna(False).astype(float).diff().diff().diff()

def f48_ddsp_147_shareholder_destruction_index_d3(equity, shareswadil, sharesbas):
    eps_ = _safe_div(equity, shareswadil)
    rmax = eps_.rolling(8, min_periods=3).max()
    dd = _safe_div(eps_, rmax) - 1.0
    return (dd * _yoy_pct(sharesbas).clip(lower=0)).diff().diff().diff()

def f48_ddsp_148_shareholder_destruction_index_zscore_8q_d3(equity, shareswadil, sharesbas):
    eps_ = _safe_div(equity, shareswadil)
    rmax = eps_.rolling(8, min_periods=3).max()
    dd = _safe_div(eps_, rmax) - 1.0
    idx = dd * _yoy_pct(sharesbas).clip(lower=0)
    return _rolling_zscore(idx, 8, min_periods=3).diff().diff().diff()

def f48_ddsp_149_terminal_dilution_signal_d3(sharesbas, close, revenue, shareswadil):
    rmax = close.rolling(8, min_periods=3).max()
    dd = _safe_div(close, rmax) - 1.0
    rps = _safe_div(revenue, shareswadil)
    rps_yoy = _safe_div(rps - rps.shift(4), rps.shift(4).abs())
    cond1 = (_yoy_pct(sharesbas) > 0.50).fillna(False)
    cond2 = (dd < -0.5).fillna(False)
    cond3 = (rps_yoy < -0.5).fillna(False)
    return (cond1 & cond2 & cond3).astype(float).diff().diff().diff()

def f48_ddsp_150_death_spiral_terminal_indicator_d3(sharesbas, close):
    a = _qoq_pct(sharesbas) > 0.05
    b = _qoq_pct(close) < -0.10
    ind = (a.fillna(False) & b.fillna(False)).astype(int)
    rolled = ind.rolling(3, min_periods=3).sum()
    return (rolled >= 3).astype(float).diff().diff().diff()


DILUTION_DEATH_SPIRAL_D3_REGISTRY_076_150 = {
    "f48_ddsp_076_price_x_shares_decoupling_d3": {"inputs": ["marketcap", "close", "sharesbas"], "func": f48_ddsp_076_price_x_shares_decoupling_d3},
    "f48_ddsp_077_effective_share_count_proxy_d3": {"inputs": ["marketcap", "close"], "func": f48_ddsp_077_effective_share_count_proxy_d3},
    "f48_ddsp_078_effective_share_count_qoq_pct_d3": {"inputs": ["marketcap", "close"], "func": f48_ddsp_078_effective_share_count_qoq_pct_d3},
    "f48_ddsp_079_issuance_per_marketcap_qoq_d3": {"inputs": ["sharesbas", "marketcap"], "func": f48_ddsp_079_issuance_per_marketcap_qoq_d3},
    "f48_ddsp_080_issuance_per_marketcap_yoy_d3": {"inputs": ["sharesbas", "marketcap"], "func": f48_ddsp_080_issuance_per_marketcap_yoy_d3},
    "f48_ddsp_081_equity_dilution_yoy_d3": {"inputs": ["equity", "shareswa"], "func": f48_ddsp_081_equity_dilution_yoy_d3},
    "f48_ddsp_082_equity_per_share_d3": {"inputs": ["equity", "shareswadil"], "func": f48_ddsp_082_equity_per_share_d3},
    "f48_ddsp_083_equity_per_share_qoq_pct_d3": {"inputs": ["equity", "shareswadil"], "func": f48_ddsp_083_equity_per_share_qoq_pct_d3},
    "f48_ddsp_084_equity_per_share_yoy_pct_d3": {"inputs": ["equity", "shareswadil"], "func": f48_ddsp_084_equity_per_share_yoy_pct_d3},
    "f48_ddsp_085_equity_per_share_drawdown_from_8q_max_d3": {"inputs": ["equity", "shareswadil"], "func": f48_ddsp_085_equity_per_share_drawdown_from_8q_max_d3},
    "f48_ddsp_086_revenue_per_share_d3": {"inputs": ["revenue", "shareswadil"], "func": f48_ddsp_086_revenue_per_share_d3},
    "f48_ddsp_087_revenue_per_share_qoq_pct_d3": {"inputs": ["revenue", "shareswadil"], "func": f48_ddsp_087_revenue_per_share_qoq_pct_d3},
    "f48_ddsp_088_revenue_per_share_yoy_pct_d3": {"inputs": ["revenue", "shareswadil"], "func": f48_ddsp_088_revenue_per_share_yoy_pct_d3},
    "f48_ddsp_089_revenue_per_share_drawdown_from_8q_max_d3": {"inputs": ["revenue", "shareswadil"], "func": f48_ddsp_089_revenue_per_share_drawdown_from_8q_max_d3},
    "f48_ddsp_090_dilution_severity_index_d3": {"inputs": ["shareswadil", "revenue"], "func": f48_ddsp_090_dilution_severity_index_d3},
    "f48_ddsp_091_dilution_destroying_rev_per_share_indicator_d3": {"inputs": ["revenue", "shareswadil"], "func": f48_ddsp_091_dilution_destroying_rev_per_share_indicator_d3},
    "f48_ddsp_092_log_marketcap_zscore_8q_d3": {"inputs": ["marketcap"], "func": f48_ddsp_092_log_marketcap_zscore_8q_d3},
    "f48_ddsp_093_marketcap_per_share_decline_streak_d3": {"inputs": ["marketcap", "sharesbas"], "func": f48_ddsp_093_marketcap_per_share_decline_streak_d3},
    "f48_ddsp_094_spiral_economic_loss_proxy_d3": {"inputs": ["equity", "shareswadil", "sharesbas"], "func": f48_ddsp_094_spiral_economic_loss_proxy_d3},
    "f48_ddsp_095_dilution_persistence_with_marketcap_decline_4q_d3": {"inputs": ["sharesbas", "marketcap"], "func": f48_ddsp_095_dilution_persistence_with_marketcap_decline_4q_d3},
    "f48_ddsp_096_sharefactor_qoq_change_d3": {"inputs": ["sharefactor"], "func": f48_ddsp_096_sharefactor_qoq_change_d3},
    "f48_ddsp_097_sharefactor_yoy_change_d3": {"inputs": ["sharefactor"], "func": f48_ddsp_097_sharefactor_yoy_change_d3},
    "f48_ddsp_098_sharefactor_reverse_split_indicator_d3": {"inputs": ["sharefactor"], "func": f48_ddsp_098_sharefactor_reverse_split_indicator_d3},
    "f48_ddsp_099_sharefactor_split_indicator_d3": {"inputs": ["sharefactor"], "func": f48_ddsp_099_sharefactor_split_indicator_d3},
    "f48_ddsp_100_reverse_split_count_8q_d3": {"inputs": ["sharefactor"], "func": f48_ddsp_100_reverse_split_count_8q_d3},
    "f48_ddsp_101_reverse_split_count_12q_d3": {"inputs": ["sharefactor"], "func": f48_ddsp_101_reverse_split_count_12q_d3},
    "f48_ddsp_102_quarters_since_last_reverse_split_d3": {"inputs": ["sharefactor"], "func": f48_ddsp_102_quarters_since_last_reverse_split_d3},
    "f48_ddsp_103_reverse_split_after_issuance_indicator_d3": {"inputs": ["sharefactor", "sharesbas"], "func": f48_ddsp_103_reverse_split_after_issuance_indicator_d3},
    "f48_ddsp_104_reverse_split_followed_by_issuance_indicator_d3": {"inputs": ["sharefactor", "sharesbas"], "func": f48_ddsp_104_reverse_split_followed_by_issuance_indicator_d3},
    "f48_ddsp_105_raw_shares_post_reverse_split_growth_d3": {"inputs": ["sharesbas", "sharefactor"], "func": f48_ddsp_105_raw_shares_post_reverse_split_growth_d3},
    "f48_ddsp_106_effective_dilution_after_split_d3": {"inputs": ["sharesbas", "sharefactor"], "func": f48_ddsp_106_effective_dilution_after_split_d3},
    "f48_ddsp_107_compound_dilution_8q_d3": {"inputs": ["sharesbas"], "func": f48_ddsp_107_compound_dilution_8q_d3},
    "f48_ddsp_108_compound_dilution_12q_d3": {"inputs": ["sharesbas"], "func": f48_ddsp_108_compound_dilution_12q_d3},
    "f48_ddsp_109_compound_dilution_16q_d3": {"inputs": ["sharesbas"], "func": f48_ddsp_109_compound_dilution_16q_d3},
    "f48_ddsp_110_compound_dilution_minus_compound_revenue_growth_8q_d3": {"inputs": ["sharesbas", "revenue"], "func": f48_ddsp_110_compound_dilution_minus_compound_revenue_growth_8q_d3},
    "f48_ddsp_111_compound_dilution_when_price_falling_8q_d3": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_111_compound_dilution_when_price_falling_8q_d3},
    "f48_ddsp_112_corporate_action_dilution_proxy_8q_d3": {"inputs": ["sharefactor", "sharesbas"], "func": f48_ddsp_112_corporate_action_dilution_proxy_8q_d3},
    "f48_ddsp_113_share_supply_shock_indicator_d3": {"inputs": ["sharesbas"], "func": f48_ddsp_113_share_supply_shock_indicator_d3},
    "f48_ddsp_114_share_supply_shock_count_12q_d3": {"inputs": ["sharesbas"], "func": f48_ddsp_114_share_supply_shock_count_12q_d3},
    "f48_ddsp_115_share_supply_shock_after_drawdown_indicator_d3": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_115_share_supply_shock_after_drawdown_indicator_d3},
    "f48_ddsp_116_death_spiral_score_d3": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_116_death_spiral_score_d3},
    "f48_ddsp_117_death_spiral_score_8q_sum_d3": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_117_death_spiral_score_8q_sum_d3},
    "f48_ddsp_118_death_spiral_score_yoy_d3": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_118_death_spiral_score_yoy_d3},
    "f48_ddsp_119_death_spiral_active_indicator_d3": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_119_death_spiral_active_indicator_d3},
    "f48_ddsp_120_death_spiral_active_count_8q_d3": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_120_death_spiral_active_count_8q_d3},
    "f48_ddsp_121_death_spiral_active_count_12q_d3": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_121_death_spiral_active_count_12q_d3},
    "f48_ddsp_122_death_spiral_active_consec_streak_d3": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_122_death_spiral_active_consec_streak_d3},
    "f48_ddsp_123_spiral_severity_index_d3": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_123_spiral_severity_index_d3},
    "f48_ddsp_124_spiral_severity_index_8q_sum_d3": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_124_spiral_severity_index_8q_sum_d3},
    "f48_ddsp_125_spiral_severity_index_zscore_8q_d3": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_125_spiral_severity_index_zscore_8q_d3},
    "f48_ddsp_126_spiral_severity_8q_slope_d3": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_126_spiral_severity_8q_slope_d3},
    "f48_ddsp_127_spiral_breach_of_8q_max_indicator_d3": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_127_spiral_breach_of_8q_max_indicator_d3},
    "f48_ddsp_128_spiral_persistence_above_median_8q_d3": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_128_spiral_persistence_above_median_8q_d3},
    "f48_ddsp_129_dilution_drawdown_co_movement_index_8q_d3": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_129_dilution_drawdown_co_movement_index_8q_d3},
    "f48_ddsp_130_dilution_drawdown_co_movement_index_12q_d3": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_130_dilution_drawdown_co_movement_index_12q_d3},
    "f48_ddsp_131_issuance_into_weakness_8q_indicator_d3": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_131_issuance_into_weakness_8q_indicator_d3},
    "f48_ddsp_132_spiral_with_revenue_collapse_indicator_d3": {"inputs": ["sharesbas", "close", "revenue"], "func": f48_ddsp_132_spiral_with_revenue_collapse_indicator_d3},
    "f48_ddsp_133_spiral_with_equity_collapse_indicator_d3": {"inputs": ["sharesbas", "close", "equity"], "func": f48_ddsp_133_spiral_with_equity_collapse_indicator_d3},
    "f48_ddsp_134_spiral_with_negative_ncfo_indicator_d3": {"inputs": ["sharesbas", "close", "ncfo"], "func": f48_ddsp_134_spiral_with_negative_ncfo_indicator_d3},
    "f48_ddsp_135_dilution_velocity_d3": {"inputs": ["sharesbas"], "func": f48_ddsp_135_dilution_velocity_d3},
    "f48_ddsp_136_dilution_acceleration_d3": {"inputs": ["sharesbas"], "func": f48_ddsp_136_dilution_acceleration_d3},
    "f48_ddsp_137_dilution_jerk_d3": {"inputs": ["sharesbas"], "func": f48_ddsp_137_dilution_jerk_d3},
    "f48_ddsp_138_dilution_after_50pct_drawdown_indicator_d3": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_138_dilution_after_50pct_drawdown_indicator_d3},
    "f48_ddsp_139_dilution_after_80pct_drawdown_indicator_d3": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_139_dilution_after_80pct_drawdown_indicator_d3},
    "f48_ddsp_140_dilution_during_marketcap_drawdown_persistence_8q_d3": {"inputs": ["sharesbas", "marketcap"], "func": f48_ddsp_140_dilution_during_marketcap_drawdown_persistence_8q_d3},
    "f48_ddsp_141_extreme_dilution_indicator_d3": {"inputs": ["sharesbas"], "func": f48_ddsp_141_extreme_dilution_indicator_d3},
    "f48_ddsp_142_extreme_dilution_count_8q_d3": {"inputs": ["sharesbas"], "func": f48_ddsp_142_extreme_dilution_count_8q_d3},
    "f48_ddsp_143_extreme_dilution_count_12q_d3": {"inputs": ["sharesbas"], "func": f48_ddsp_143_extreme_dilution_count_12q_d3},
    "f48_ddsp_144_compound_dilution_above_100pct_indicator_8q_d3": {"inputs": ["sharesbas"], "func": f48_ddsp_144_compound_dilution_above_100pct_indicator_8q_d3},
    "f48_ddsp_145_compound_dilution_above_200pct_indicator_8q_d3": {"inputs": ["sharesbas"], "func": f48_ddsp_145_compound_dilution_above_200pct_indicator_8q_d3},
    "f48_ddsp_146_compound_dilution_above_500pct_indicator_12q_d3": {"inputs": ["sharesbas"], "func": f48_ddsp_146_compound_dilution_above_500pct_indicator_12q_d3},
    "f48_ddsp_147_shareholder_destruction_index_d3": {"inputs": ["equity", "shareswadil", "sharesbas"], "func": f48_ddsp_147_shareholder_destruction_index_d3},
    "f48_ddsp_148_shareholder_destruction_index_zscore_8q_d3": {"inputs": ["equity", "shareswadil", "sharesbas"], "func": f48_ddsp_148_shareholder_destruction_index_zscore_8q_d3},
    "f48_ddsp_149_terminal_dilution_signal_d3": {"inputs": ["sharesbas", "close", "revenue", "shareswadil"], "func": f48_ddsp_149_terminal_dilution_signal_d3},
    "f48_ddsp_150_death_spiral_terminal_indicator_d3": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_150_death_spiral_terminal_indicator_d3},
}
