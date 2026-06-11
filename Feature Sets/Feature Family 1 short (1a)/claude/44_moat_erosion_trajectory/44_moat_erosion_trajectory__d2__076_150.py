"""moat_erosion_trajectory d2 features 076_150 — 2nd-derivative wrappers.

Each function inlines the corresponding base body and appends .diff().diff() so the output is the second bar-over-bar derivative of the base signal. Helpers, constants, and PIT discipline are identical to the matching __base__076_150.py."""
import numpy as np
import pandas as pd
QDAYS = 63
YDAYS = 252
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260
MDAYS = 21
WDAYS = 5

def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))

def _safe_log_signed(s):
    return np.sign(s) * np.log1p(s.abs())

def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, 'index') else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)

def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)

def _rolling_rank_pct(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)

    def _r(w):
        if np.isnan(w).any():
            return np.nan
        return (np.searchsorted(np.sort(w), w[-1], side='right') - 0.5) / len(w)
    return s.rolling(window, min_periods=min_periods).apply(_r, raw=True)

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

def _streak_above_zero(flag_series, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)

    def _streak(w):
        if np.isnan(w).any():
            return np.nan
        n = 0
        for v in w[::-1]:
            if v > 0:
                n += 1
            else:
                break
        return float(n)
    return flag_series.rolling(window, min_periods=min_periods).apply(_streak, raw=True)

def _max_streak_above_zero(flag_series, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)

    def _ms(w):
        if np.isnan(w).any():
            return np.nan
        best = cur = 0
        for v in w:
            if v > 0:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    return flag_series.rolling(window, min_periods=min_periods).apply(_ms, raw=True)

def _days_since_max(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)

    def _f(w):
        if np.isnan(w).all():
            return np.nan
        return float(len(w) - 1 - int(np.nanargmax(w)))
    return s.rolling(window, min_periods=min_periods).apply(_f, raw=True)

def f44_mert_076_sgna_to_revenue_level_d2(sgna: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(sgna, revenue).diff().diff()

def f44_mert_077_sgna_to_revenue_change_yoy_d2(sgna: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(sgna, revenue).diff(YDAYS).diff().diff()

def f44_mert_078_sgna_to_revenue_change_5y_d2(sgna: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(sgna, revenue).diff(DDAYS_5Y).diff().diff()

def f44_mert_079_sgna_to_revenue_zscore_5y_d2(sgna: pd.Series, revenue: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_div(sgna, revenue), DDAYS_5Y).diff().diff()

def f44_mert_080_sgna_to_revenue_rise_streak_d2(sgna: pd.Series, revenue: pd.Series) -> pd.Series:
    r = _safe_div(sgna, revenue)
    m = r.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (r > m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff().diff()

def f44_mert_081_rnd_to_revenue_level_d2(rnd: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(rnd, revenue).diff().diff()

def f44_mert_082_rnd_to_revenue_change_yoy_d2(rnd: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(rnd, revenue).diff(YDAYS).diff().diff()

def f44_mert_083_rnd_to_revenue_change_5y_d2(rnd: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(rnd, revenue).diff(DDAYS_5Y).diff().diff()

def f44_mert_084_cor_to_revenue_level_d2(cor: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(cor, revenue).diff().diff()

def f44_mert_085_cor_to_revenue_change_5y_d2(cor: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(cor, revenue).diff(DDAYS_5Y).diff().diff()

def f44_mert_086_cor_to_revenue_zscore_5y_d2(cor: pd.Series, revenue: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_div(cor, revenue), DDAYS_5Y).diff().diff()

def f44_mert_087_opex_to_revenue_level_d2(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(opex, revenue).diff().diff()

def f44_mert_088_opex_to_revenue_change_yoy_d2(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(opex, revenue).diff(YDAYS).diff().diff()

def f44_mert_089_opex_to_revenue_change_5y_d2(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(opex, revenue).diff(DDAYS_5Y).diff().diff()

def f44_mert_090_opex_to_revenue_rise_streak_d2(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    r = _safe_div(opex, revenue)
    m = r.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (r > m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff().diff()

def f44_mert_091_cost_compound_rise_score_5y_d2(sgna: pd.Series, cor: pd.Series, opex: pd.Series, revenue: pd.Series) -> pd.Series:
    sg = _safe_div(sgna, revenue)
    co = _safe_div(cor, revenue)
    op = _safe_div(opex, revenue)
    sg_m = sg.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    co_m = co.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    op_m = op.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    flag = ((sg > sg_m) & (co > co_m) & (op > op_m)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).mean().diff().diff()

def f44_mert_092_sga_growth_vs_revenue_growth_diff_5y_d2(sgna: pd.Series, revenue: pd.Series) -> pd.Series:
    return (_safe_log(sgna).diff(DDAYS_5Y) - _safe_log(revenue).diff(DDAYS_5Y)).diff().diff()

def f44_mert_093_cor_growth_vs_revenue_growth_diff_5y_d2(cor: pd.Series, revenue: pd.Series) -> pd.Series:
    return (_safe_log(cor).diff(DDAYS_5Y) - _safe_log(revenue).diff(DDAYS_5Y)).diff().diff()

def f44_mert_094_rnd_growth_vs_revenue_growth_diff_5y_d2(rnd: pd.Series, revenue: pd.Series) -> pd.Series:
    return (_safe_log(rnd).diff(DDAYS_5Y) - _safe_log(revenue).diff(DDAYS_5Y)).diff().diff()

def f44_mert_095_opex_growth_outpacing_revenue_streak_d2(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    flag = (_safe_log(opex).diff(YDAYS) > _safe_log(revenue).diff(YDAYS)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff().diff()

def f44_mert_096_cost_efficiency_decay_score_5y_d2(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    diff = _safe_log(opex).diff(YDAYS) - _safe_log(revenue).diff(YDAYS)
    return diff.rolling(DDAYS_5Y, min_periods=YDAYS).mean().diff().diff()

def f44_mert_097_cost_efficiency_acceleration_decay_5y_d2(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    diff = _safe_log(opex).diff(YDAYS) - _safe_log(revenue).diff(YDAYS)
    return _rolling_slope(diff, DDAYS_5Y).diff().diff()

def f44_mert_098_incremental_cost_per_incremental_revenue_5y_d2(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    dc = opex - opex.shift(DDAYS_5Y)
    dr = revenue - revenue.shift(DDAYS_5Y)
    return _safe_div(dc, dr).diff().diff()

def f44_mert_099_cost_intensity_vs_5y_baseline_d2(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    r = _safe_div(opex, revenue)
    return (r - r.rolling(DDAYS_5Y, min_periods=YDAYS).mean()).diff().diff()

def f44_mert_100_cost_intensity_zscore_5y_d2(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_div(opex, revenue), DDAYS_5Y).diff().diff()

def f44_mert_101_cash_conversion_cycle_days_level_d2(accountsreceivable: pd.Series, inventory: pd.Series, accountspayable: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    ar_days = _safe_div(accountsreceivable, revenue) * 90.0
    inv_days = _safe_div(inventory, cor) * 90.0
    ap_days = _safe_div(accountspayable, cor) * 90.0
    return (ar_days + inv_days - ap_days).diff().diff()

def f44_mert_102_cash_conversion_cycle_change_yoy_d2(accountsreceivable: pd.Series, inventory: pd.Series, accountspayable: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    ar_days = _safe_div(accountsreceivable, revenue) * 90.0
    inv_days = _safe_div(inventory, cor) * 90.0
    ap_days = _safe_div(accountspayable, cor) * 90.0
    return (ar_days + inv_days - ap_days).diff(YDAYS).diff().diff()

def f44_mert_103_cash_conversion_cycle_change_5y_d2(accountsreceivable: pd.Series, inventory: pd.Series, accountspayable: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    ar_days = _safe_div(accountsreceivable, revenue) * 90.0
    inv_days = _safe_div(inventory, cor) * 90.0
    ap_days = _safe_div(accountspayable, cor) * 90.0
    return (ar_days + inv_days - ap_days).diff(DDAYS_5Y).diff().diff()

def f44_mert_104_cash_conversion_cycle_zscore_5y_d2(accountsreceivable: pd.Series, inventory: pd.Series, accountspayable: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    ar_days = _safe_div(accountsreceivable, revenue) * 90.0
    inv_days = _safe_div(inventory, cor) * 90.0
    ap_days = _safe_div(accountspayable, cor) * 90.0
    return _rolling_zscore(ar_days + inv_days - ap_days, DDAYS_5Y).diff().diff()

def f44_mert_105_ar_days_level_d2(accountsreceivable: pd.Series, revenue: pd.Series) -> pd.Series:
    return (_safe_div(accountsreceivable, revenue) * 90.0).diff().diff()

def f44_mert_106_ar_days_change_5y_d2(accountsreceivable: pd.Series, revenue: pd.Series) -> pd.Series:
    return (_safe_div(accountsreceivable, revenue) * 90.0).diff(DDAYS_5Y).diff().diff()

def f44_mert_107_ar_days_zscore_5y_d2(accountsreceivable: pd.Series, revenue: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_div(accountsreceivable, revenue) * 90.0, DDAYS_5Y).diff().diff()

def f44_mert_108_ar_days_rise_streak_d2(accountsreceivable: pd.Series, revenue: pd.Series) -> pd.Series:
    d = _safe_div(accountsreceivable, revenue) * 90.0
    m = d.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (d > m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff().diff()

def f44_mert_109_inv_days_level_d2(inventory: pd.Series, cor: pd.Series) -> pd.Series:
    return (_safe_div(inventory, cor) * 90.0).diff().diff()

def f44_mert_110_inv_days_change_5y_d2(inventory: pd.Series, cor: pd.Series) -> pd.Series:
    return (_safe_div(inventory, cor) * 90.0).diff(DDAYS_5Y).diff().diff()

def f44_mert_111_inv_days_zscore_5y_d2(inventory: pd.Series, cor: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_div(inventory, cor) * 90.0, DDAYS_5Y).diff().diff()

def f44_mert_112_inv_days_rise_streak_d2(inventory: pd.Series, cor: pd.Series) -> pd.Series:
    d = _safe_div(inventory, cor) * 90.0
    m = d.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (d > m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff().diff()

def f44_mert_113_ap_days_level_d2(accountspayable: pd.Series, cor: pd.Series) -> pd.Series:
    return (_safe_div(accountspayable, cor) * 90.0).diff().diff()

def f44_mert_114_ap_days_change_5y_d2(accountspayable: pd.Series, cor: pd.Series) -> pd.Series:
    return (_safe_div(accountspayable, cor) * 90.0).diff(DDAYS_5Y).diff().diff()

def f44_mert_115_ap_days_zscore_5y_d2(accountspayable: pd.Series, cor: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_div(accountspayable, cor) * 90.0, DDAYS_5Y).diff().diff()

def f44_mert_116_working_capital_to_revenue_level_d2(workingcapital: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(workingcapital, revenue).diff().diff()

def f44_mert_117_working_capital_to_revenue_change_5y_d2(workingcapital: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(workingcapital, revenue).diff(DDAYS_5Y).diff().diff()

def f44_mert_118_working_capital_efficiency_decay_5y_d2(workingcapital: pd.Series, revenue: pd.Series) -> pd.Series:
    return _rolling_slope(_safe_div(workingcapital, revenue), DDAYS_5Y).diff().diff()

def f44_mert_119_ccc_above_long_mean_streak_d2(accountsreceivable: pd.Series, inventory: pd.Series, accountspayable: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    ar_days = _safe_div(accountsreceivable, revenue) * 90.0
    inv_days = _safe_div(inventory, cor) * 90.0
    ap_days = _safe_div(accountspayable, cor) * 90.0
    ccc = ar_days + inv_days - ap_days
    m = ccc.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    flag = (ccc > m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff().diff()

def f44_mert_120_ccc_compression_rate_5y_d2(accountsreceivable: pd.Series, inventory: pd.Series, accountspayable: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    ar_days = _safe_div(accountsreceivable, revenue) * 90.0
    inv_days = _safe_div(inventory, cor) * 90.0
    ap_days = _safe_div(accountspayable, cor) * 90.0
    return _rolling_slope(ar_days + inv_days - ap_days, DDAYS_5Y).diff().diff()

def f44_mert_121_fcf_margin_level_d2(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(fcf, revenue).diff().diff()

def f44_mert_122_fcf_margin_change_yoy_d2(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(fcf, revenue).diff(YDAYS).diff().diff()

def f44_mert_123_fcf_margin_change_5y_d2(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(fcf, revenue).diff(DDAYS_5Y).diff().diff()

def f44_mert_124_fcf_margin_zscore_5y_d2(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_div(fcf, revenue), DDAYS_5Y).diff().diff()

def f44_mert_125_fcf_margin_log_distance_to_5y_max_d2(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    fm = _safe_div(fcf, revenue)
    mx = fm.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    return (_safe_log_signed(fm) - _safe_log_signed(mx)).diff().diff()

def f44_mert_126_fcf_margin_decline_streak_d2(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    fm = _safe_div(fcf, revenue)
    m = fm.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (fm < m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff().diff()

def f44_mert_127_fcf_margin_compression_rate_5y_d2(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    return _rolling_slope(_safe_div(fcf, revenue), DDAYS_5Y).diff().diff()

def f44_mert_128_fcf_to_netinc_level_d2(fcf: pd.Series, netinc: pd.Series) -> pd.Series:
    return _safe_div(fcf, netinc).diff().diff()

def f44_mert_129_fcf_to_netinc_change_5y_d2(fcf: pd.Series, netinc: pd.Series) -> pd.Series:
    return _safe_div(fcf, netinc).diff(DDAYS_5Y).diff().diff()

def f44_mert_130_fcf_to_netinc_zscore_5y_d2(fcf: pd.Series, netinc: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_div(fcf, netinc), DDAYS_5Y).diff().diff()

def f44_mert_131_ocf_to_revenue_level_d2(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(ncfo, revenue).diff().diff()

def f44_mert_132_ocf_to_revenue_change_5y_d2(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(ncfo, revenue).diff(DDAYS_5Y).diff().diff()

def f44_mert_133_ocf_to_revenue_zscore_5y_d2(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_div(ncfo, revenue), DDAYS_5Y).diff().diff()

def f44_mert_134_fcf_per_share_change_5y_d2(fcf: pd.Series, shareswadil: pd.Series) -> pd.Series:
    return _safe_log_signed(_safe_div(fcf, shareswadil)).diff(DDAYS_5Y).diff().diff()

def f44_mert_135_fcf_per_share_decline_streak_d2(fcf: pd.Series, shareswadil: pd.Series) -> pd.Series:
    f = _safe_div(fcf, shareswadil)
    m = f.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (f < m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff().diff()

def f44_mert_136_reinvestment_efficiency_proxy_level_d2(capex: pd.Series, fcf: pd.Series) -> pd.Series:
    return _safe_div(capex, fcf).diff().diff()

def f44_mert_137_reinvestment_efficiency_change_5y_d2(capex: pd.Series, fcf: pd.Series) -> pd.Series:
    return _safe_div(capex, fcf).diff(DDAYS_5Y).diff().diff()

def f44_mert_138_capex_intensity_rise_with_fcf_margin_drop_count_5y_d2(capex: pd.Series, fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    capex_int = _safe_div(capex, revenue)
    fcf_m = _safe_div(fcf, revenue)
    flag = ((capex_int.diff(YDAYS) > 0) & (fcf_m.diff(YDAYS) < 0)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum().diff().diff()

def f44_mert_139_fcf_quality_decay_score_5y_d2(fcf: pd.Series, netinc: pd.Series) -> pd.Series:
    q = _safe_div(fcf, netinc)
    return (q - q.rolling(DDAYS_5Y, min_periods=YDAYS).mean()).diff().diff()

def f44_mert_140_fcf_quality_acceleration_decay_5y_d2(fcf: pd.Series, netinc: pd.Series) -> pd.Series:
    return _rolling_slope(_safe_div(fcf, netinc), DDAYS_5Y).diff().diff()

def f44_mert_141_moat_decay_composite_5y_score_d2(gp: pd.Series, opinc: pd.Series, netinc: pd.Series, revenue: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    gm = _safe_div(gp, revenue)
    om = _safe_div(opinc, revenue)
    roic = _safe_div(opinc, debt + equity)
    at = _safe_div(revenue, assets)
    r1 = _rolling_rank_pct(gm, DDAYS_5Y)
    r2 = _rolling_rank_pct(om, DDAYS_5Y)
    r3 = _rolling_rank_pct(roic, DDAYS_5Y)
    r4 = _rolling_rank_pct(at, DDAYS_5Y)
    score = (1.0 - r1 + (1.0 - r2) + (1.0 - r3) + (1.0 - r4)) / 4.0
    return score.rolling(DDAYS_5Y, min_periods=YDAYS).mean().diff().diff()

def f44_mert_142_moat_decay_composite_3y_score_d2(gp: pd.Series, opinc: pd.Series, netinc: pd.Series, revenue: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    gm = _safe_div(gp, revenue)
    om = _safe_div(opinc, revenue)
    roic = _safe_div(opinc, debt + equity)
    at = _safe_div(revenue, assets)
    r1 = _rolling_rank_pct(gm, DDAYS_3Y)
    r2 = _rolling_rank_pct(om, DDAYS_3Y)
    r3 = _rolling_rank_pct(roic, DDAYS_3Y)
    r4 = _rolling_rank_pct(at, DDAYS_3Y)
    score = (1.0 - r1 + (1.0 - r2) + (1.0 - r3) + (1.0 - r4)) / 4.0
    return score.rolling(DDAYS_3Y, min_periods=YDAYS).mean().diff().diff()

def f44_mert_143_multi_metric_compression_breadth_5y_d2(gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series, assets: pd.Series) -> pd.Series:
    series_list = [_safe_div(gp, revenue), _safe_div(opinc, revenue), _safe_div(ebitda, revenue), _safe_div(fcf, revenue), _safe_div(netinc, assets)]
    total = pd.Series(0.0, index=revenue.index)
    valid = pd.Series(True, index=revenue.index)
    for s in series_list:
        m = s.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
        total = total + (s < m).astype(float)
        valid = valid & m.notna()
    return total.where(valid, np.nan).diff().diff()

def f44_mert_144_multi_metric_compression_breadth_3y_d2(gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series, assets: pd.Series) -> pd.Series:
    series_list = [_safe_div(gp, revenue), _safe_div(opinc, revenue), _safe_div(ebitda, revenue), _safe_div(fcf, revenue), _safe_div(netinc, assets)]
    total = pd.Series(0.0, index=revenue.index)
    valid = pd.Series(True, index=revenue.index)
    for s in series_list:
        m = s.rolling(DDAYS_3Y, min_periods=YDAYS).mean()
        total = total + (s < m).astype(float)
        valid = valid & m.notna()
    return total.where(valid, np.nan).diff().diff()

def f44_mert_145_moat_decay_acceleration_5y_d2(gp: pd.Series, opinc: pd.Series, revenue: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    gm = _safe_div(gp, revenue)
    om = _safe_div(opinc, revenue)
    roic = _safe_div(opinc, debt + equity)
    score = (1.0 - _rolling_rank_pct(gm, DDAYS_5Y) + (1.0 - _rolling_rank_pct(om, DDAYS_5Y)) + (1.0 - _rolling_rank_pct(roic, DDAYS_5Y))) / 3.0
    return _rolling_slope(score, DDAYS_5Y).diff().diff()

def f44_mert_146_moat_decay_volatility_5y_d2(gp: pd.Series, opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    avg = (_safe_div(gp, revenue) + _safe_div(opinc, revenue)) / 2.0
    return avg.rolling(DDAYS_5Y, min_periods=YDAYS).std().diff().diff()

def f44_mert_147_moat_decay_inflection_recency_5y_d2(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    gm = _safe_div(gp, revenue)
    slope = _rolling_slope(gm, YDAYS)
    sg = np.sign(slope.fillna(0))
    flip = (sg.diff().abs() > 0).astype(float)

    def _r(w):
        if np.isnan(w).all():
            return np.nan
        nz = np.where(w > 0)[0]
        if len(nz) == 0:
            return float(len(w))
        return float(len(w) - 1 - nz[-1])
    return flip.rolling(DDAYS_5Y, min_periods=YDAYS).apply(_r, raw=True).diff().diff()

def f44_mert_148_composite_f44_mert_distress_score_d2(gp: pd.Series, opinc: pd.Series, fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    gm = _safe_div(gp, revenue)
    om = _safe_div(opinc, revenue)
    fm = _safe_div(fcf, revenue)
    flag = ((gm < gm.rolling(DDAYS_5Y, min_periods=YDAYS).mean()) & (om < om.rolling(DDAYS_5Y, min_periods=YDAYS).mean()) & (fm < fm.rolling(DDAYS_5Y, min_periods=YDAYS).mean())).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).mean().diff().diff()

def f44_mert_149_composite_f44_mert_topping_score_d2(gp: pd.Series, opinc: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, debt: pd.Series, assets: pd.Series) -> pd.Series:
    gm = _safe_div(gp, revenue)
    om = _safe_div(opinc, revenue)
    roic = _safe_div(opinc, debt + equity)
    roe = _safe_div(netinc, equity)
    roa = _safe_div(netinc, assets)
    at = _safe_div(revenue, assets)
    series_list = [gm, om, roic, roe, roa, at]
    total = pd.Series(0.0, index=revenue.index)
    valid = pd.Series(True, index=revenue.index)
    for s in series_list:
        r = _rolling_rank_pct(s, DDAYS_5Y)
        total = total + (1.0 - r)
        valid = valid & r.notna()
    avg = (total / len(series_list)).where(valid, np.nan)
    return avg.rolling(DDAYS_5Y, min_periods=YDAYS).mean().diff().diff()

def f44_mert_150_composite_f44_mert_blowoff_score_d2(gp: pd.Series, opinc: pd.Series, revenue: pd.Series, capex: pd.Series, fcf: pd.Series) -> pd.Series:
    gm = _safe_div(gp, revenue)
    om = _safe_div(opinc, revenue)
    ci = _safe_div(capex, revenue)
    gm_q25 = gm.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.25)
    om_q25 = om.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.25)
    ci_q75 = ci.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.75)
    flag = ((gm <= gm_q25) & (om <= om_q25) & (ci >= ci_q75)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).mean().diff().diff()
MOAT_EROSION_TRAJECTORY_D2_REGISTRY_076_150 = {'f44_mert_076_sgna_to_revenue_level_d2': {'inputs': ['sgna', 'revenue'], 'func': f44_mert_076_sgna_to_revenue_level_d2}, 'f44_mert_077_sgna_to_revenue_change_yoy_d2': {'inputs': ['sgna', 'revenue'], 'func': f44_mert_077_sgna_to_revenue_change_yoy_d2}, 'f44_mert_078_sgna_to_revenue_change_5y_d2': {'inputs': ['sgna', 'revenue'], 'func': f44_mert_078_sgna_to_revenue_change_5y_d2}, 'f44_mert_079_sgna_to_revenue_zscore_5y_d2': {'inputs': ['sgna', 'revenue'], 'func': f44_mert_079_sgna_to_revenue_zscore_5y_d2}, 'f44_mert_080_sgna_to_revenue_rise_streak_d2': {'inputs': ['sgna', 'revenue'], 'func': f44_mert_080_sgna_to_revenue_rise_streak_d2}, 'f44_mert_081_rnd_to_revenue_level_d2': {'inputs': ['rnd', 'revenue'], 'func': f44_mert_081_rnd_to_revenue_level_d2}, 'f44_mert_082_rnd_to_revenue_change_yoy_d2': {'inputs': ['rnd', 'revenue'], 'func': f44_mert_082_rnd_to_revenue_change_yoy_d2}, 'f44_mert_083_rnd_to_revenue_change_5y_d2': {'inputs': ['rnd', 'revenue'], 'func': f44_mert_083_rnd_to_revenue_change_5y_d2}, 'f44_mert_084_cor_to_revenue_level_d2': {'inputs': ['cor', 'revenue'], 'func': f44_mert_084_cor_to_revenue_level_d2}, 'f44_mert_085_cor_to_revenue_change_5y_d2': {'inputs': ['cor', 'revenue'], 'func': f44_mert_085_cor_to_revenue_change_5y_d2}, 'f44_mert_086_cor_to_revenue_zscore_5y_d2': {'inputs': ['cor', 'revenue'], 'func': f44_mert_086_cor_to_revenue_zscore_5y_d2}, 'f44_mert_087_opex_to_revenue_level_d2': {'inputs': ['opex', 'revenue'], 'func': f44_mert_087_opex_to_revenue_level_d2}, 'f44_mert_088_opex_to_revenue_change_yoy_d2': {'inputs': ['opex', 'revenue'], 'func': f44_mert_088_opex_to_revenue_change_yoy_d2}, 'f44_mert_089_opex_to_revenue_change_5y_d2': {'inputs': ['opex', 'revenue'], 'func': f44_mert_089_opex_to_revenue_change_5y_d2}, 'f44_mert_090_opex_to_revenue_rise_streak_d2': {'inputs': ['opex', 'revenue'], 'func': f44_mert_090_opex_to_revenue_rise_streak_d2}, 'f44_mert_091_cost_compound_rise_score_5y_d2': {'inputs': ['sgna', 'cor', 'opex', 'revenue'], 'func': f44_mert_091_cost_compound_rise_score_5y_d2}, 'f44_mert_092_sga_growth_vs_revenue_growth_diff_5y_d2': {'inputs': ['sgna', 'revenue'], 'func': f44_mert_092_sga_growth_vs_revenue_growth_diff_5y_d2}, 'f44_mert_093_cor_growth_vs_revenue_growth_diff_5y_d2': {'inputs': ['cor', 'revenue'], 'func': f44_mert_093_cor_growth_vs_revenue_growth_diff_5y_d2}, 'f44_mert_094_rnd_growth_vs_revenue_growth_diff_5y_d2': {'inputs': ['rnd', 'revenue'], 'func': f44_mert_094_rnd_growth_vs_revenue_growth_diff_5y_d2}, 'f44_mert_095_opex_growth_outpacing_revenue_streak_d2': {'inputs': ['opex', 'revenue'], 'func': f44_mert_095_opex_growth_outpacing_revenue_streak_d2}, 'f44_mert_096_cost_efficiency_decay_score_5y_d2': {'inputs': ['opex', 'revenue'], 'func': f44_mert_096_cost_efficiency_decay_score_5y_d2}, 'f44_mert_097_cost_efficiency_acceleration_decay_5y_d2': {'inputs': ['opex', 'revenue'], 'func': f44_mert_097_cost_efficiency_acceleration_decay_5y_d2}, 'f44_mert_098_incremental_cost_per_incremental_revenue_5y_d2': {'inputs': ['opex', 'revenue'], 'func': f44_mert_098_incremental_cost_per_incremental_revenue_5y_d2}, 'f44_mert_099_cost_intensity_vs_5y_baseline_d2': {'inputs': ['opex', 'revenue'], 'func': f44_mert_099_cost_intensity_vs_5y_baseline_d2}, 'f44_mert_100_cost_intensity_zscore_5y_d2': {'inputs': ['opex', 'revenue'], 'func': f44_mert_100_cost_intensity_zscore_5y_d2}, 'f44_mert_101_cash_conversion_cycle_days_level_d2': {'inputs': ['accountsreceivable', 'inventory', 'accountspayable', 'revenue', 'cor'], 'func': f44_mert_101_cash_conversion_cycle_days_level_d2}, 'f44_mert_102_cash_conversion_cycle_change_yoy_d2': {'inputs': ['accountsreceivable', 'inventory', 'accountspayable', 'revenue', 'cor'], 'func': f44_mert_102_cash_conversion_cycle_change_yoy_d2}, 'f44_mert_103_cash_conversion_cycle_change_5y_d2': {'inputs': ['accountsreceivable', 'inventory', 'accountspayable', 'revenue', 'cor'], 'func': f44_mert_103_cash_conversion_cycle_change_5y_d2}, 'f44_mert_104_cash_conversion_cycle_zscore_5y_d2': {'inputs': ['accountsreceivable', 'inventory', 'accountspayable', 'revenue', 'cor'], 'func': f44_mert_104_cash_conversion_cycle_zscore_5y_d2}, 'f44_mert_105_ar_days_level_d2': {'inputs': ['accountsreceivable', 'revenue'], 'func': f44_mert_105_ar_days_level_d2}, 'f44_mert_106_ar_days_change_5y_d2': {'inputs': ['accountsreceivable', 'revenue'], 'func': f44_mert_106_ar_days_change_5y_d2}, 'f44_mert_107_ar_days_zscore_5y_d2': {'inputs': ['accountsreceivable', 'revenue'], 'func': f44_mert_107_ar_days_zscore_5y_d2}, 'f44_mert_108_ar_days_rise_streak_d2': {'inputs': ['accountsreceivable', 'revenue'], 'func': f44_mert_108_ar_days_rise_streak_d2}, 'f44_mert_109_inv_days_level_d2': {'inputs': ['inventory', 'cor'], 'func': f44_mert_109_inv_days_level_d2}, 'f44_mert_110_inv_days_change_5y_d2': {'inputs': ['inventory', 'cor'], 'func': f44_mert_110_inv_days_change_5y_d2}, 'f44_mert_111_inv_days_zscore_5y_d2': {'inputs': ['inventory', 'cor'], 'func': f44_mert_111_inv_days_zscore_5y_d2}, 'f44_mert_112_inv_days_rise_streak_d2': {'inputs': ['inventory', 'cor'], 'func': f44_mert_112_inv_days_rise_streak_d2}, 'f44_mert_113_ap_days_level_d2': {'inputs': ['accountspayable', 'cor'], 'func': f44_mert_113_ap_days_level_d2}, 'f44_mert_114_ap_days_change_5y_d2': {'inputs': ['accountspayable', 'cor'], 'func': f44_mert_114_ap_days_change_5y_d2}, 'f44_mert_115_ap_days_zscore_5y_d2': {'inputs': ['accountspayable', 'cor'], 'func': f44_mert_115_ap_days_zscore_5y_d2}, 'f44_mert_116_working_capital_to_revenue_level_d2': {'inputs': ['workingcapital', 'revenue'], 'func': f44_mert_116_working_capital_to_revenue_level_d2}, 'f44_mert_117_working_capital_to_revenue_change_5y_d2': {'inputs': ['workingcapital', 'revenue'], 'func': f44_mert_117_working_capital_to_revenue_change_5y_d2}, 'f44_mert_118_working_capital_efficiency_decay_5y_d2': {'inputs': ['workingcapital', 'revenue'], 'func': f44_mert_118_working_capital_efficiency_decay_5y_d2}, 'f44_mert_119_ccc_above_long_mean_streak_d2': {'inputs': ['accountsreceivable', 'inventory', 'accountspayable', 'revenue', 'cor'], 'func': f44_mert_119_ccc_above_long_mean_streak_d2}, 'f44_mert_120_ccc_compression_rate_5y_d2': {'inputs': ['accountsreceivable', 'inventory', 'accountspayable', 'revenue', 'cor'], 'func': f44_mert_120_ccc_compression_rate_5y_d2}, 'f44_mert_121_fcf_margin_level_d2': {'inputs': ['fcf', 'revenue'], 'func': f44_mert_121_fcf_margin_level_d2}, 'f44_mert_122_fcf_margin_change_yoy_d2': {'inputs': ['fcf', 'revenue'], 'func': f44_mert_122_fcf_margin_change_yoy_d2}, 'f44_mert_123_fcf_margin_change_5y_d2': {'inputs': ['fcf', 'revenue'], 'func': f44_mert_123_fcf_margin_change_5y_d2}, 'f44_mert_124_fcf_margin_zscore_5y_d2': {'inputs': ['fcf', 'revenue'], 'func': f44_mert_124_fcf_margin_zscore_5y_d2}, 'f44_mert_125_fcf_margin_log_distance_to_5y_max_d2': {'inputs': ['fcf', 'revenue'], 'func': f44_mert_125_fcf_margin_log_distance_to_5y_max_d2}, 'f44_mert_126_fcf_margin_decline_streak_d2': {'inputs': ['fcf', 'revenue'], 'func': f44_mert_126_fcf_margin_decline_streak_d2}, 'f44_mert_127_fcf_margin_compression_rate_5y_d2': {'inputs': ['fcf', 'revenue'], 'func': f44_mert_127_fcf_margin_compression_rate_5y_d2}, 'f44_mert_128_fcf_to_netinc_level_d2': {'inputs': ['fcf', 'netinc'], 'func': f44_mert_128_fcf_to_netinc_level_d2}, 'f44_mert_129_fcf_to_netinc_change_5y_d2': {'inputs': ['fcf', 'netinc'], 'func': f44_mert_129_fcf_to_netinc_change_5y_d2}, 'f44_mert_130_fcf_to_netinc_zscore_5y_d2': {'inputs': ['fcf', 'netinc'], 'func': f44_mert_130_fcf_to_netinc_zscore_5y_d2}, 'f44_mert_131_ocf_to_revenue_level_d2': {'inputs': ['ncfo', 'revenue'], 'func': f44_mert_131_ocf_to_revenue_level_d2}, 'f44_mert_132_ocf_to_revenue_change_5y_d2': {'inputs': ['ncfo', 'revenue'], 'func': f44_mert_132_ocf_to_revenue_change_5y_d2}, 'f44_mert_133_ocf_to_revenue_zscore_5y_d2': {'inputs': ['ncfo', 'revenue'], 'func': f44_mert_133_ocf_to_revenue_zscore_5y_d2}, 'f44_mert_134_fcf_per_share_change_5y_d2': {'inputs': ['fcf', 'shareswadil'], 'func': f44_mert_134_fcf_per_share_change_5y_d2}, 'f44_mert_135_fcf_per_share_decline_streak_d2': {'inputs': ['fcf', 'shareswadil'], 'func': f44_mert_135_fcf_per_share_decline_streak_d2}, 'f44_mert_136_reinvestment_efficiency_proxy_level_d2': {'inputs': ['capex', 'fcf'], 'func': f44_mert_136_reinvestment_efficiency_proxy_level_d2}, 'f44_mert_137_reinvestment_efficiency_change_5y_d2': {'inputs': ['capex', 'fcf'], 'func': f44_mert_137_reinvestment_efficiency_change_5y_d2}, 'f44_mert_138_capex_intensity_rise_with_fcf_margin_drop_count_5y_d2': {'inputs': ['capex', 'fcf', 'revenue'], 'func': f44_mert_138_capex_intensity_rise_with_fcf_margin_drop_count_5y_d2}, 'f44_mert_139_fcf_quality_decay_score_5y_d2': {'inputs': ['fcf', 'netinc'], 'func': f44_mert_139_fcf_quality_decay_score_5y_d2}, 'f44_mert_140_fcf_quality_acceleration_decay_5y_d2': {'inputs': ['fcf', 'netinc'], 'func': f44_mert_140_fcf_quality_acceleration_decay_5y_d2}, 'f44_mert_141_moat_decay_composite_5y_score_d2': {'inputs': ['gp', 'opinc', 'netinc', 'revenue', 'assets', 'equity', 'debt'], 'func': f44_mert_141_moat_decay_composite_5y_score_d2}, 'f44_mert_142_moat_decay_composite_3y_score_d2': {'inputs': ['gp', 'opinc', 'netinc', 'revenue', 'assets', 'equity', 'debt'], 'func': f44_mert_142_moat_decay_composite_3y_score_d2}, 'f44_mert_143_multi_metric_compression_breadth_5y_d2': {'inputs': ['gp', 'opinc', 'ebitda', 'fcf', 'revenue', 'netinc', 'assets'], 'func': f44_mert_143_multi_metric_compression_breadth_5y_d2}, 'f44_mert_144_multi_metric_compression_breadth_3y_d2': {'inputs': ['gp', 'opinc', 'ebitda', 'fcf', 'revenue', 'netinc', 'assets'], 'func': f44_mert_144_multi_metric_compression_breadth_3y_d2}, 'f44_mert_145_moat_decay_acceleration_5y_d2': {'inputs': ['gp', 'opinc', 'revenue', 'debt', 'equity'], 'func': f44_mert_145_moat_decay_acceleration_5y_d2}, 'f44_mert_146_moat_decay_volatility_5y_d2': {'inputs': ['gp', 'opinc', 'revenue'], 'func': f44_mert_146_moat_decay_volatility_5y_d2}, 'f44_mert_147_moat_decay_inflection_recency_5y_d2': {'inputs': ['gp', 'revenue'], 'func': f44_mert_147_moat_decay_inflection_recency_5y_d2}, 'f44_mert_148_composite_f44_mert_distress_score_d2': {'inputs': ['gp', 'opinc', 'fcf', 'revenue'], 'func': f44_mert_148_composite_f44_mert_distress_score_d2}, 'f44_mert_149_composite_f44_mert_topping_score_d2': {'inputs': ['gp', 'opinc', 'netinc', 'revenue', 'equity', 'debt', 'assets'], 'func': f44_mert_149_composite_f44_mert_topping_score_d2}, 'f44_mert_150_composite_f44_mert_blowoff_score_d2': {'inputs': ['gp', 'opinc', 'revenue', 'capex', 'fcf'], 'func': f44_mert_150_composite_f44_mert_blowoff_score_d2}}
