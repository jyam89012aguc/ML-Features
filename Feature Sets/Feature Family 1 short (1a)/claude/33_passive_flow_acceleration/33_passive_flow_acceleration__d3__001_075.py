"""Auto-generated D3 wrappers from passive_flow_acceleration__base__001_075.py.

Each function inlines the base body and appends .diff() chained 3 time(s)."""
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
    idx = num.index if hasattr(num, 'index') else None
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

def f33_pfac_001_etf_flow_cliff_jump_vs_8q_std_d3(etf_flow: pd.Series) -> pd.Series:
    chg = etf_flow.diff()
    sd = chg.rolling(Y2, min_periods=3).std()
    return (chg / sd.replace(0, np.nan)).diff().diff().diff()

def f33_pfac_002_etf_share_cliff_jump_vs_8q_std_d3(etf_share: pd.Series) -> pd.Series:
    chg = etf_share.diff()
    sd = chg.rolling(Y2, min_periods=3).std()
    return (chg / sd.replace(0, np.nan)).diff().diff().diff()

def f33_pfac_003_etf_flow_structural_break_8q_d3(etf_flow: pd.Series) -> pd.Series:
    return _structural_break_score(etf_flow, Y2).diff().diff().diff()

def f33_pfac_004_etf_share_inflection_smoothed_raw_sign_flip_8q_d3(etf_share: pd.Series) -> pd.Series:
    sl = _rolling_slope(etf_share, Y)
    sm = sl.ewm(span=4, adjust=False, min_periods=2).mean()
    flip = (np.sign(sl - sm) != np.sign((sl - sm).shift(1))).astype(float)
    return flip.rolling(Y2, min_periods=3).sum().diff().diff().diff()

def f33_pfac_005_compound_etf_inflow_inst_count_down_4q_d3(etf_flow: pd.Series, inst_count: pd.Series) -> pd.Series:
    flag = ((etf_flow > 0) & (inst_count.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f33_pfac_006_etf_flow_growth_zscore_16q_d3(etf_flow: pd.Series) -> pd.Series:
    return _rolling_zscore(etf_flow.diff(), Y4).diff().diff().diff()

def f33_pfac_007_etf_flow_4q_chg_vs_16q_std_d3(etf_flow: pd.Series) -> pd.Series:
    chg4 = etf_flow.diff(Y)
    sd = chg4.rolling(Y4, min_periods=6).std()
    return (chg4 / sd.replace(0, np.nan)).diff().diff().diff()

def f33_pfac_008_etf_flow_jerk_zscore_16q_d3(etf_flow: pd.Series) -> pd.Series:
    return _rolling_zscore(etf_flow.diff().diff().diff(), Y4).diff().diff().diff()

def f33_pfac_009_etf_flow_cumulative_excess_above_8q_linear_d3(etf_flow: pd.Series) -> pd.Series:

    def _arc(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        c1, c0 = np.polyfit(x, w, 1)
        resid = w - (c1 * x + c0)
        return float(np.clip(resid, 0, None).sum())
    return etf_flow.rolling(Y2, min_periods=4).apply(_arc, raw=True).diff().diff().diff()

def f33_pfac_010_etf_flow_quadratic_c2_8q_d3(etf_flow: pd.Series) -> pd.Series:
    return _quadratic_c2(etf_flow, Y2).diff().diff().diff()

def f33_pfac_011_etf_flow_inflection_count_d2_positive_8q_d3(etf_flow: pd.Series) -> pd.Series:
    d2 = etf_flow.diff().diff()
    flag = (d2 > 0).astype(float)
    return flag.rolling(Y2, min_periods=3).sum().diff().diff().diff()

def f33_pfac_012_etf_share_exp_fit_r2_8q_d3(etf_share: pd.Series) -> pd.Series:
    ls = _safe_log(etf_share)

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
    return ls.rolling(Y2, min_periods=4).apply(_r2, raw=True).diff().diff().diff()

def f33_pfac_013_etf_share_slope_4q_minus_12q_d3(etf_share: pd.Series) -> pd.Series:
    return (_rolling_slope(etf_share, Y) - _rolling_slope(etf_share, Y3)).diff().diff().diff()

def f33_pfac_014_log_etf_share_x2_regression_r2_d3(etf_share: pd.Series) -> pd.Series:
    ls = _safe_log(etf_share)

    def _r2q(w):
        if np.isnan(w).any() or len(w) < 4:
            return np.nan
        x = np.arange(len(w))
        ss_tot = ((w - w.mean()) ** 2).sum()
        if ss_tot == 0:
            return np.nan
        coef = np.polyfit(x, w, 2)
        pred = np.polyval(coef, x)
        ss_res = ((w - pred) ** 2).sum()
        return 1.0 - ss_res / ss_tot
    return ls.rolling(Y2, min_periods=4).apply(_r2q, raw=True).diff().diff().diff()

def f33_pfac_015_etf_flow_accel_baseline_z_1q_vs_12q_d3(etf_flow: pd.Series) -> pd.Series:
    return _rolling_zscore(etf_flow.diff(), Y3).diff().diff().diff()

def f33_pfac_016_compound_etf_share_up_inst_value_down_4q_d3(etf_share: pd.Series, inst_value: pd.Series) -> pd.Series:
    flag = ((etf_share.diff() > 0) & (inst_value.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f33_pfac_017_compound_etf_inflow_value_flat_4q_d3(etf_flow: pd.Series, inst_value: pd.Series) -> pd.Series:
    flat = inst_value.diff().abs() / inst_value.replace(0, np.nan) < 0.01
    flag = ((etf_flow > 0) & flat).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f33_pfac_018_compound_etf_inflow_inst_shares_down_4q_d3(etf_flow: pd.Series, inst_shares: pd.Series) -> pd.Series:
    flag = ((etf_flow > 0) & (inst_shares.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f33_pfac_019_ratio_largest_etf_flow_jump_to_mean_8q_d3(etf_flow: pd.Series) -> pd.Series:
    chg = etf_flow.diff().abs()
    return _safe_div(chg.rolling(Y2, min_periods=3).max(), chg.rolling(Y2, min_periods=3).mean()).diff().diff().diff()

def f33_pfac_020_quarters_since_etf_flow_last_accelerated_d3(etf_flow: pd.Series) -> pd.Series:
    d2 = etf_flow.diff().diff()
    flag = (d2 > 0).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return (pd.Series(np.arange(len(flag)), index=flag.index) - last).diff().diff().diff()

def f33_pfac_021_etf_flow_recent_4q_minus_prior_4q_d3(etf_flow: pd.Series) -> pd.Series:
    chg = etf_flow.diff()
    a = chg.rolling(Y, min_periods=2).mean()
    b = chg.shift(Y).rolling(Y, min_periods=2).mean()
    return (a - b).diff().diff().diff()

def f33_pfac_022_etf_share_cumulative_excess_above_8q_linear_d3(etf_share: pd.Series) -> pd.Series:

    def _ex(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        c1, c0 = np.polyfit(x, w, 1)
        return float((w - (c1 * x + c0)).sum())
    return etf_share.rolling(Y2, min_periods=4).apply(_ex, raw=True).diff().diff().diff()

def f33_pfac_023_etf_share_arc_area_above_8q_linear_d3(etf_share: pd.Series) -> pd.Series:

    def _arc(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        c1, c0 = np.polyfit(x, w, 1)
        resid = w - (c1 * x + c0)
        return float(np.clip(resid, 0, None).sum())
    return etf_share.rolling(Y2, min_periods=4).apply(_arc, raw=True).diff().diff().diff()

def f33_pfac_024_etf_flow_cliff_count_2sigma_16q_d3(etf_flow: pd.Series) -> pd.Series:
    z = _rolling_zscore(etf_flow.diff(), Y4)
    flag = (z > 2.0).astype(float)
    return flag.rolling(Y4, min_periods=6).sum().diff().diff().diff()

def f33_pfac_025_etf_flow_growth_cv_8q_d3(etf_flow: pd.Series) -> pd.Series:
    chg = etf_flow.diff()
    return _safe_div(chg.rolling(Y2, min_periods=3).std(), chg.rolling(Y2, min_periods=3).mean().abs()).diff().diff().diff()

def f33_pfac_026_etf_to_inst_share_ratio_accel_z_d3(etf_share: pd.Series, inst_shares: pd.Series) -> pd.Series:
    r = _safe_div(etf_share, inst_shares)
    return _rolling_zscore(r.diff(), Y4).diff().diff().diff()

def f33_pfac_027_etf_share_cliff_jump_8q_d3(etf_share: pd.Series) -> pd.Series:
    chg = etf_share.diff()
    sd = chg.rolling(Y2, min_periods=3).std()
    return (chg / sd.replace(0, np.nan)).diff().diff().diff()

def f33_pfac_028_etf_share_structural_break_8q_d3(etf_share: pd.Series) -> pd.Series:
    return _structural_break_score(etf_share, Y2).diff().diff().diff()

def f33_pfac_029_etf_share_to_inst_count_accel_z_d3(etf_share: pd.Series, inst_count: pd.Series) -> pd.Series:
    r = _safe_div(etf_share, inst_count)
    return _rolling_zscore(r.diff(), Y4).diff().diff().diff()

def f33_pfac_030_etf_share_to_inst_count_cliff_8q_d3(etf_share: pd.Series, inst_count: pd.Series) -> pd.Series:
    r = _safe_div(etf_share, inst_count)
    chg = r.diff()
    sd = chg.rolling(Y2, min_periods=3).std()
    return (chg / sd.replace(0, np.nan)).diff().diff().diff()

def f33_pfac_031_etf_share_to_inst_value_accel_z_d3(etf_share: pd.Series, inst_value: pd.Series) -> pd.Series:
    r = _safe_div(etf_share, inst_value)
    return _rolling_zscore(r.diff(), Y4).diff().diff().diff()

def f33_pfac_032_etf_share_to_inst_value_cliff_8q_d3(etf_share: pd.Series, inst_value: pd.Series) -> pd.Series:
    r = _safe_div(etf_share, inst_value)
    chg = r.diff()
    sd = chg.rolling(Y2, min_periods=3).std()
    return (chg / sd.replace(0, np.nan)).diff().diff().diff()

def f33_pfac_033_etf_inflow_to_value_accel_z_d3(etf_flow: pd.Series, inst_value: pd.Series) -> pd.Series:
    r = _safe_div(etf_flow, inst_value)
    return _rolling_zscore(r.diff(), Y4).diff().diff().diff()

def f33_pfac_034_etf_concentration_cliff_8q_d3(etf_share: pd.Series, inst_shares: pd.Series) -> pd.Series:
    r = _safe_div(etf_share, etf_share + inst_shares)
    chg = r.diff()
    sd = chg.rolling(Y2, min_periods=3).std()
    return (chg / sd.replace(0, np.nan)).diff().diff().diff()

def f33_pfac_035_etf_concentration_structural_break_8q_d3(etf_share: pd.Series, inst_shares: pd.Series) -> pd.Series:
    r = _safe_div(etf_share, etf_share + inst_shares)
    return _structural_break_score(r, Y2).diff().diff().diff()

def f33_pfac_036_etf_concentration_inflection_smoothed_raw_sign_flip_8q_d3(etf_share: pd.Series, inst_shares: pd.Series) -> pd.Series:
    r = _safe_div(etf_share, etf_share + inst_shares)
    sl = _rolling_slope(r, Y)
    sm = sl.ewm(span=4, adjust=False, min_periods=2).mean()
    flip = (np.sign(sl - sm) != np.sign((sl - sm).shift(1))).astype(float)
    return flip.rolling(Y2, min_periods=3).sum().diff().diff().diff()

def f33_pfac_037_etf_concentration_exp_fit_r2_8q_d3(etf_share: pd.Series, inst_shares: pd.Series) -> pd.Series:
    lr = _safe_log(_safe_div(etf_share, etf_share + inst_shares))

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
    return lr.rolling(Y2, min_periods=4).apply(_r2, raw=True).diff().diff().diff()

def f33_pfac_038_compound_etf_conc_up_inst_dispersion_up_4q_d3(etf_share: pd.Series, inst_shares: pd.Series, inst_count: pd.Series) -> pd.Series:
    r = _safe_div(etf_share, etf_share + inst_shares)
    disp = _safe_div(inst_shares, inst_count)
    flag = ((r.diff() > 0) & (disp.diff() > 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f33_pfac_039_compound_etf_conc_up_inst_exit_4q_d3(etf_share: pd.Series, inst_shares: pd.Series, inst_count: pd.Series) -> pd.Series:
    r = _safe_div(etf_share, etf_share + inst_shares)
    flag = ((r.diff() > 0) & (inst_count.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f33_pfac_040_etf_concentration_latest_to_8q_max_d3(etf_share: pd.Series, inst_shares: pd.Series) -> pd.Series:
    r = _safe_div(etf_share, etf_share + inst_shares)
    return _safe_div(r, r.rolling(Y2, min_periods=3).max()).diff().diff().diff()

def f33_pfac_041_quarters_since_etf_concentration_accelerated_d3(etf_share: pd.Series, inst_shares: pd.Series) -> pd.Series:
    r = _safe_div(etf_share, etf_share + inst_shares)
    d2 = r.diff().diff()
    flag = (d2 > 0).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return (pd.Series(np.arange(len(flag)), index=flag.index) - last).diff().diff().diff()

def f33_pfac_042_etf_concentration_zscore_8q_cumulative_d3(etf_share: pd.Series, inst_shares: pd.Series) -> pd.Series:
    r = _safe_div(etf_share, etf_share + inst_shares)
    z = _rolling_zscore(r, Y4)
    return z.rolling(Y2, min_periods=3).sum().diff().diff().diff()

def f33_pfac_043_etf_concentration_arc_area_above_8q_linear_d3(etf_share: pd.Series, inst_shares: pd.Series) -> pd.Series:
    r = _safe_div(etf_share, etf_share + inst_shares)

    def _arc(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        c1, c0 = np.polyfit(x, w, 1)
        resid = w - (c1 * x + c0)
        return float(np.clip(resid, 0, None).sum())
    return r.rolling(Y2, min_periods=4).apply(_arc, raw=True).diff().diff().diff()

def f33_pfac_044_etf_concentration_2sigma_jump_count_16q_d3(etf_share: pd.Series, inst_shares: pd.Series) -> pd.Series:
    r = _safe_div(etf_share, etf_share + inst_shares)
    z = _rolling_zscore(r.diff(), Y4)
    flag = (z > 2.0).astype(float)
    return flag.rolling(Y4, min_periods=6).sum().diff().diff().diff()

def f33_pfac_045_log_etf_concentration_slope_4q_minus_12q_d3(etf_share: pd.Series, inst_shares: pd.Series) -> pd.Series:
    lr = _safe_log(_safe_div(etf_share, etf_share + inst_shares))
    return (_rolling_slope(lr, Y) - _rolling_slope(lr, Y3)).diff().diff().diff()

def f33_pfac_046_etf_concentration_4q_chg_to_level_ratio_d3(etf_share: pd.Series, inst_shares: pd.Series) -> pd.Series:
    r = _safe_div(etf_share, etf_share + inst_shares)
    return _safe_div(r.diff(Y), r.abs()).diff().diff().diff()

def f33_pfac_047_d2_log_etf_concentration_z_16q_d3(etf_share: pd.Series, inst_shares: pd.Series) -> pd.Series:
    lr = _safe_log(_safe_div(etf_share, etf_share + inst_shares))
    return _rolling_zscore(lr.diff().diff(), Y4).diff().diff().diff()

def f33_pfac_048_etf_concentration_tail_event_count_4q_d3(etf_share: pd.Series, inst_shares: pd.Series) -> pd.Series:
    r = _safe_div(etf_share, etf_share + inst_shares)
    p = r.rolling(Y4, min_periods=6).quantile(0.95)
    flag = (r >= p).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f33_pfac_049_composite_etf_concentration_accel_4q_d3(etf_share: pd.Series, inst_shares: pd.Series, inst_count: pd.Series) -> pd.Series:
    r = _safe_div(etf_share, etf_share + inst_shares)
    return (_rolling_zscore(r.diff(), Y4) + _rolling_zscore(-inst_count.diff(), Y4)).rolling(Y, min_periods=2).mean().diff().diff().diff()

def f33_pfac_050_etf_concentration_weighted_multi_metric_z_4q_d3(etf_share: pd.Series, inst_shares: pd.Series, inst_value: pd.Series, inst_count: pd.Series) -> pd.Series:
    r = _safe_div(etf_share, etf_share + inst_shares)
    z = _rolling_zscore(r.diff(), Y4) + _rolling_zscore(-inst_value.diff(), Y4) + _rolling_zscore(-inst_count.diff(), Y4)
    return z.rolling(Y, min_periods=2).mean().diff().diff().diff()

def f33_pfac_051_inst_count_cliff_8q_d3(inst_count: pd.Series) -> pd.Series:
    chg = inst_count.diff()
    sd = chg.rolling(Y2, min_periods=3).std()
    return (-chg / sd.replace(0, np.nan)).diff().diff().diff()

def f33_pfac_052_inst_count_zscore_16q_d3(inst_count: pd.Series) -> pd.Series:
    return _rolling_zscore(inst_count.diff(), Y4).diff().diff().diff()

def f33_pfac_053_inst_count_structural_break_8q_d3(inst_count: pd.Series) -> pd.Series:
    return _structural_break_score(inst_count, Y2).diff().diff().diff()

def f33_pfac_054_inst_count_inflection_sign_flip_8q_d3(inst_count: pd.Series) -> pd.Series:
    sl = _rolling_slope(inst_count, Y)
    sm = sl.ewm(span=4, adjust=False, min_periods=2).mean()
    flip = (np.sign(sl - sm) != np.sign((sl - sm).shift(1))).astype(float)
    return flip.rolling(Y2, min_periods=3).sum().diff().diff().diff()

def f33_pfac_055_inst_value_chg_cliff_8q_d3(inst_value: pd.Series) -> pd.Series:
    chg = inst_value.diff()
    sd = chg.rolling(Y2, min_periods=3).std()
    return (-chg / sd.replace(0, np.nan)).diff().diff().diff()

def f33_pfac_056_inst_value_zscore_16q_d3(inst_value: pd.Series) -> pd.Series:
    return _rolling_zscore(inst_value.diff(), Y4).diff().diff().diff()

def f33_pfac_057_inst_value_structural_break_8q_d3(inst_value: pd.Series) -> pd.Series:
    return _structural_break_score(inst_value, Y2).diff().diff().diff()

def f33_pfac_058_inst_shares_chg_cliff_8q_d3(inst_shares: pd.Series) -> pd.Series:
    chg = inst_shares.diff()
    sd = chg.rolling(Y2, min_periods=3).std()
    return (-chg / sd.replace(0, np.nan)).diff().diff().diff()

def f33_pfac_059_inst_shares_zscore_16q_d3(inst_shares: pd.Series) -> pd.Series:
    return _rolling_zscore(inst_shares.diff(), Y4).diff().diff().diff()

def f33_pfac_060_compound_inst_count_down_value_down_4q_d3(inst_count: pd.Series, inst_value: pd.Series) -> pd.Series:
    flag = ((inst_count.diff() < 0) & (inst_value.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f33_pfac_061_compound_inst_count_down_etf_up_4q_d3(inst_count: pd.Series, etf_flow: pd.Series) -> pd.Series:
    flag = ((inst_count.diff() < 0) & (etf_flow > 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f33_pfac_062_compound_inst_value_down_etf_conc_up_4q_d3(inst_value: pd.Series, etf_share: pd.Series, inst_shares: pd.Series) -> pd.Series:
    r = _safe_div(etf_share, etf_share + inst_shares)
    flag = ((inst_value.diff() < 0) & (r.diff() > 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f33_pfac_063_ratio_largest_inst_count_drop_to_mean_8q_d3(inst_count: pd.Series) -> pd.Series:
    chg = inst_count.diff()
    mn = chg.rolling(Y2, min_periods=3).min()
    am = chg.abs().rolling(Y2, min_periods=3).mean()
    return _safe_div(-mn, am).diff().diff().diff()

def f33_pfac_064_quarters_since_inst_count_neg_accel_d3(inst_count: pd.Series) -> pd.Series:
    d2 = inst_count.diff().diff()
    flag = (d2 < 0).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return (pd.Series(np.arange(len(flag)), index=flag.index) - last).diff().diff().diff()

def f33_pfac_065_inst_count_recent_4q_minus_prior_4q_d3(inst_count: pd.Series) -> pd.Series:
    chg = inst_count.diff()
    a = chg.rolling(Y, min_periods=2).mean()
    b = chg.shift(Y).rolling(Y, min_periods=2).mean()
    return (a - b).diff().diff().diff()

def f33_pfac_066_inst_value_4q_chg_to_16q_std_d3(inst_value: pd.Series) -> pd.Series:
    chg4 = inst_value.diff(Y)
    sd = chg4.rolling(Y4, min_periods=6).std()
    return (chg4 / sd.replace(0, np.nan)).diff().diff().diff()

def f33_pfac_067_inst_count_jerk_z_d3(inst_count: pd.Series) -> pd.Series:
    return _rolling_zscore(inst_count.diff().diff().diff(), Y4).diff().diff().diff()

def f33_pfac_068_inst_value_exp_fit_r2_8q_d3(inst_value: pd.Series) -> pd.Series:
    lv = _safe_log(inst_value)

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
    return lv.rolling(Y2, min_periods=4).apply(_r2, raw=True).diff().diff().diff()

def f33_pfac_069_inst_count_below_25pct_16q_fraction_d3(inst_count: pd.Series) -> pd.Series:
    p = inst_count.rolling(Y4, min_periods=6).quantile(0.25)
    flag = (inst_count < p).astype(float)
    return flag.rolling(Y4, min_periods=6).mean().diff().diff().diff()

def f33_pfac_070_inst_value_below_25pct_16q_fraction_d3(inst_value: pd.Series) -> pd.Series:
    p = inst_value.rolling(Y4, min_periods=6).quantile(0.25)
    flag = (inst_value < p).astype(float)
    return flag.rolling(Y4, min_periods=6).mean().diff().diff().diff()

def f33_pfac_071_inst_count_slope_4q_minus_12q_d3(inst_count: pd.Series) -> pd.Series:
    return (_rolling_slope(inst_count, Y) - _rolling_slope(inst_count, Y3)).diff().diff().diff()

def f33_pfac_072_inst_value_slope_4q_minus_12q_d3(inst_value: pd.Series) -> pd.Series:
    return (_rolling_slope(inst_value, Y) - _rolling_slope(inst_value, Y3)).diff().diff().diff()

def f33_pfac_073_compound_triple_deterioration_count_4q_d3(inst_count: pd.Series, inst_value: pd.Series, inst_shares: pd.Series) -> pd.Series:
    flag = ((inst_count.diff() < 0) & (inst_value.diff() < 0) & (inst_shares.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f33_pfac_074_composite_inst_exit_accel_4q_d3(inst_count: pd.Series, inst_value: pd.Series, inst_shares: pd.Series) -> pd.Series:
    z1 = _rolling_zscore(-inst_count.diff(), Y4)
    z2 = _rolling_zscore(-inst_value.diff(), Y4)
    z3 = _rolling_zscore(-inst_shares.diff(), Y4)
    return (z1 + z2 + z3).rolling(Y, min_periods=2).mean().diff().diff().diff()

def f33_pfac_075_composite_inst_vs_etf_divergence_z_4q_d3(etf_share: pd.Series, inst_value: pd.Series) -> pd.Series:
    return (_rolling_zscore(etf_share.diff(), Y4) - _rolling_zscore(inst_value.diff(), Y4)).rolling(Y, min_periods=2).mean().diff().diff().diff()
PASSIVE_FLOW_ACCELERATION_D3_REGISTRY_001_075 = {'f33_pfac_001_etf_flow_cliff_jump_vs_8q_std_d3': {'inputs': ['etf_flow'], 'func': f33_pfac_001_etf_flow_cliff_jump_vs_8q_std_d3}, 'f33_pfac_002_etf_share_cliff_jump_vs_8q_std_d3': {'inputs': ['etf_share'], 'func': f33_pfac_002_etf_share_cliff_jump_vs_8q_std_d3}, 'f33_pfac_003_etf_flow_structural_break_8q_d3': {'inputs': ['etf_flow'], 'func': f33_pfac_003_etf_flow_structural_break_8q_d3}, 'f33_pfac_004_etf_share_inflection_smoothed_raw_sign_flip_8q_d3': {'inputs': ['etf_share'], 'func': f33_pfac_004_etf_share_inflection_smoothed_raw_sign_flip_8q_d3}, 'f33_pfac_005_compound_etf_inflow_inst_count_down_4q_d3': {'inputs': ['etf_flow', 'inst_count'], 'func': f33_pfac_005_compound_etf_inflow_inst_count_down_4q_d3}, 'f33_pfac_006_etf_flow_growth_zscore_16q_d3': {'inputs': ['etf_flow'], 'func': f33_pfac_006_etf_flow_growth_zscore_16q_d3}, 'f33_pfac_007_etf_flow_4q_chg_vs_16q_std_d3': {'inputs': ['etf_flow'], 'func': f33_pfac_007_etf_flow_4q_chg_vs_16q_std_d3}, 'f33_pfac_008_etf_flow_jerk_zscore_16q_d3': {'inputs': ['etf_flow'], 'func': f33_pfac_008_etf_flow_jerk_zscore_16q_d3}, 'f33_pfac_009_etf_flow_cumulative_excess_above_8q_linear_d3': {'inputs': ['etf_flow'], 'func': f33_pfac_009_etf_flow_cumulative_excess_above_8q_linear_d3}, 'f33_pfac_010_etf_flow_quadratic_c2_8q_d3': {'inputs': ['etf_flow'], 'func': f33_pfac_010_etf_flow_quadratic_c2_8q_d3}, 'f33_pfac_011_etf_flow_inflection_count_d2_positive_8q_d3': {'inputs': ['etf_flow'], 'func': f33_pfac_011_etf_flow_inflection_count_d2_positive_8q_d3}, 'f33_pfac_012_etf_share_exp_fit_r2_8q_d3': {'inputs': ['etf_share'], 'func': f33_pfac_012_etf_share_exp_fit_r2_8q_d3}, 'f33_pfac_013_etf_share_slope_4q_minus_12q_d3': {'inputs': ['etf_share'], 'func': f33_pfac_013_etf_share_slope_4q_minus_12q_d3}, 'f33_pfac_014_log_etf_share_x2_regression_r2_d3': {'inputs': ['etf_share'], 'func': f33_pfac_014_log_etf_share_x2_regression_r2_d3}, 'f33_pfac_015_etf_flow_accel_baseline_z_1q_vs_12q_d3': {'inputs': ['etf_flow'], 'func': f33_pfac_015_etf_flow_accel_baseline_z_1q_vs_12q_d3}, 'f33_pfac_016_compound_etf_share_up_inst_value_down_4q_d3': {'inputs': ['etf_share', 'inst_value'], 'func': f33_pfac_016_compound_etf_share_up_inst_value_down_4q_d3}, 'f33_pfac_017_compound_etf_inflow_value_flat_4q_d3': {'inputs': ['etf_flow', 'inst_value'], 'func': f33_pfac_017_compound_etf_inflow_value_flat_4q_d3}, 'f33_pfac_018_compound_etf_inflow_inst_shares_down_4q_d3': {'inputs': ['etf_flow', 'inst_shares'], 'func': f33_pfac_018_compound_etf_inflow_inst_shares_down_4q_d3}, 'f33_pfac_019_ratio_largest_etf_flow_jump_to_mean_8q_d3': {'inputs': ['etf_flow'], 'func': f33_pfac_019_ratio_largest_etf_flow_jump_to_mean_8q_d3}, 'f33_pfac_020_quarters_since_etf_flow_last_accelerated_d3': {'inputs': ['etf_flow'], 'func': f33_pfac_020_quarters_since_etf_flow_last_accelerated_d3}, 'f33_pfac_021_etf_flow_recent_4q_minus_prior_4q_d3': {'inputs': ['etf_flow'], 'func': f33_pfac_021_etf_flow_recent_4q_minus_prior_4q_d3}, 'f33_pfac_022_etf_share_cumulative_excess_above_8q_linear_d3': {'inputs': ['etf_share'], 'func': f33_pfac_022_etf_share_cumulative_excess_above_8q_linear_d3}, 'f33_pfac_023_etf_share_arc_area_above_8q_linear_d3': {'inputs': ['etf_share'], 'func': f33_pfac_023_etf_share_arc_area_above_8q_linear_d3}, 'f33_pfac_024_etf_flow_cliff_count_2sigma_16q_d3': {'inputs': ['etf_flow'], 'func': f33_pfac_024_etf_flow_cliff_count_2sigma_16q_d3}, 'f33_pfac_025_etf_flow_growth_cv_8q_d3': {'inputs': ['etf_flow'], 'func': f33_pfac_025_etf_flow_growth_cv_8q_d3}, 'f33_pfac_026_etf_to_inst_share_ratio_accel_z_d3': {'inputs': ['etf_share', 'inst_shares'], 'func': f33_pfac_026_etf_to_inst_share_ratio_accel_z_d3}, 'f33_pfac_027_etf_share_cliff_jump_8q_d3': {'inputs': ['etf_share'], 'func': f33_pfac_027_etf_share_cliff_jump_8q_d3}, 'f33_pfac_028_etf_share_structural_break_8q_d3': {'inputs': ['etf_share'], 'func': f33_pfac_028_etf_share_structural_break_8q_d3}, 'f33_pfac_029_etf_share_to_inst_count_accel_z_d3': {'inputs': ['etf_share', 'inst_count'], 'func': f33_pfac_029_etf_share_to_inst_count_accel_z_d3}, 'f33_pfac_030_etf_share_to_inst_count_cliff_8q_d3': {'inputs': ['etf_share', 'inst_count'], 'func': f33_pfac_030_etf_share_to_inst_count_cliff_8q_d3}, 'f33_pfac_031_etf_share_to_inst_value_accel_z_d3': {'inputs': ['etf_share', 'inst_value'], 'func': f33_pfac_031_etf_share_to_inst_value_accel_z_d3}, 'f33_pfac_032_etf_share_to_inst_value_cliff_8q_d3': {'inputs': ['etf_share', 'inst_value'], 'func': f33_pfac_032_etf_share_to_inst_value_cliff_8q_d3}, 'f33_pfac_033_etf_inflow_to_value_accel_z_d3': {'inputs': ['etf_flow', 'inst_value'], 'func': f33_pfac_033_etf_inflow_to_value_accel_z_d3}, 'f33_pfac_034_etf_concentration_cliff_8q_d3': {'inputs': ['etf_share', 'inst_shares'], 'func': f33_pfac_034_etf_concentration_cliff_8q_d3}, 'f33_pfac_035_etf_concentration_structural_break_8q_d3': {'inputs': ['etf_share', 'inst_shares'], 'func': f33_pfac_035_etf_concentration_structural_break_8q_d3}, 'f33_pfac_036_etf_concentration_inflection_smoothed_raw_sign_flip_8q_d3': {'inputs': ['etf_share', 'inst_shares'], 'func': f33_pfac_036_etf_concentration_inflection_smoothed_raw_sign_flip_8q_d3}, 'f33_pfac_037_etf_concentration_exp_fit_r2_8q_d3': {'inputs': ['etf_share', 'inst_shares'], 'func': f33_pfac_037_etf_concentration_exp_fit_r2_8q_d3}, 'f33_pfac_038_compound_etf_conc_up_inst_dispersion_up_4q_d3': {'inputs': ['etf_share', 'inst_shares', 'inst_count'], 'func': f33_pfac_038_compound_etf_conc_up_inst_dispersion_up_4q_d3}, 'f33_pfac_039_compound_etf_conc_up_inst_exit_4q_d3': {'inputs': ['etf_share', 'inst_shares', 'inst_count'], 'func': f33_pfac_039_compound_etf_conc_up_inst_exit_4q_d3}, 'f33_pfac_040_etf_concentration_latest_to_8q_max_d3': {'inputs': ['etf_share', 'inst_shares'], 'func': f33_pfac_040_etf_concentration_latest_to_8q_max_d3}, 'f33_pfac_041_quarters_since_etf_concentration_accelerated_d3': {'inputs': ['etf_share', 'inst_shares'], 'func': f33_pfac_041_quarters_since_etf_concentration_accelerated_d3}, 'f33_pfac_042_etf_concentration_zscore_8q_cumulative_d3': {'inputs': ['etf_share', 'inst_shares'], 'func': f33_pfac_042_etf_concentration_zscore_8q_cumulative_d3}, 'f33_pfac_043_etf_concentration_arc_area_above_8q_linear_d3': {'inputs': ['etf_share', 'inst_shares'], 'func': f33_pfac_043_etf_concentration_arc_area_above_8q_linear_d3}, 'f33_pfac_044_etf_concentration_2sigma_jump_count_16q_d3': {'inputs': ['etf_share', 'inst_shares'], 'func': f33_pfac_044_etf_concentration_2sigma_jump_count_16q_d3}, 'f33_pfac_045_log_etf_concentration_slope_4q_minus_12q_d3': {'inputs': ['etf_share', 'inst_shares'], 'func': f33_pfac_045_log_etf_concentration_slope_4q_minus_12q_d3}, 'f33_pfac_046_etf_concentration_4q_chg_to_level_ratio_d3': {'inputs': ['etf_share', 'inst_shares'], 'func': f33_pfac_046_etf_concentration_4q_chg_to_level_ratio_d3}, 'f33_pfac_047_d2_log_etf_concentration_z_16q_d3': {'inputs': ['etf_share', 'inst_shares'], 'func': f33_pfac_047_d2_log_etf_concentration_z_16q_d3}, 'f33_pfac_048_etf_concentration_tail_event_count_4q_d3': {'inputs': ['etf_share', 'inst_shares'], 'func': f33_pfac_048_etf_concentration_tail_event_count_4q_d3}, 'f33_pfac_049_composite_etf_concentration_accel_4q_d3': {'inputs': ['etf_share', 'inst_shares', 'inst_count'], 'func': f33_pfac_049_composite_etf_concentration_accel_4q_d3}, 'f33_pfac_050_etf_concentration_weighted_multi_metric_z_4q_d3': {'inputs': ['etf_share', 'inst_shares', 'inst_value', 'inst_count'], 'func': f33_pfac_050_etf_concentration_weighted_multi_metric_z_4q_d3}, 'f33_pfac_051_inst_count_cliff_8q_d3': {'inputs': ['inst_count'], 'func': f33_pfac_051_inst_count_cliff_8q_d3}, 'f33_pfac_052_inst_count_zscore_16q_d3': {'inputs': ['inst_count'], 'func': f33_pfac_052_inst_count_zscore_16q_d3}, 'f33_pfac_053_inst_count_structural_break_8q_d3': {'inputs': ['inst_count'], 'func': f33_pfac_053_inst_count_structural_break_8q_d3}, 'f33_pfac_054_inst_count_inflection_sign_flip_8q_d3': {'inputs': ['inst_count'], 'func': f33_pfac_054_inst_count_inflection_sign_flip_8q_d3}, 'f33_pfac_055_inst_value_chg_cliff_8q_d3': {'inputs': ['inst_value'], 'func': f33_pfac_055_inst_value_chg_cliff_8q_d3}, 'f33_pfac_056_inst_value_zscore_16q_d3': {'inputs': ['inst_value'], 'func': f33_pfac_056_inst_value_zscore_16q_d3}, 'f33_pfac_057_inst_value_structural_break_8q_d3': {'inputs': ['inst_value'], 'func': f33_pfac_057_inst_value_structural_break_8q_d3}, 'f33_pfac_058_inst_shares_chg_cliff_8q_d3': {'inputs': ['inst_shares'], 'func': f33_pfac_058_inst_shares_chg_cliff_8q_d3}, 'f33_pfac_059_inst_shares_zscore_16q_d3': {'inputs': ['inst_shares'], 'func': f33_pfac_059_inst_shares_zscore_16q_d3}, 'f33_pfac_060_compound_inst_count_down_value_down_4q_d3': {'inputs': ['inst_count', 'inst_value'], 'func': f33_pfac_060_compound_inst_count_down_value_down_4q_d3}, 'f33_pfac_061_compound_inst_count_down_etf_up_4q_d3': {'inputs': ['inst_count', 'etf_flow'], 'func': f33_pfac_061_compound_inst_count_down_etf_up_4q_d3}, 'f33_pfac_062_compound_inst_value_down_etf_conc_up_4q_d3': {'inputs': ['inst_value', 'etf_share', 'inst_shares'], 'func': f33_pfac_062_compound_inst_value_down_etf_conc_up_4q_d3}, 'f33_pfac_063_ratio_largest_inst_count_drop_to_mean_8q_d3': {'inputs': ['inst_count'], 'func': f33_pfac_063_ratio_largest_inst_count_drop_to_mean_8q_d3}, 'f33_pfac_064_quarters_since_inst_count_neg_accel_d3': {'inputs': ['inst_count'], 'func': f33_pfac_064_quarters_since_inst_count_neg_accel_d3}, 'f33_pfac_065_inst_count_recent_4q_minus_prior_4q_d3': {'inputs': ['inst_count'], 'func': f33_pfac_065_inst_count_recent_4q_minus_prior_4q_d3}, 'f33_pfac_066_inst_value_4q_chg_to_16q_std_d3': {'inputs': ['inst_value'], 'func': f33_pfac_066_inst_value_4q_chg_to_16q_std_d3}, 'f33_pfac_067_inst_count_jerk_z_d3': {'inputs': ['inst_count'], 'func': f33_pfac_067_inst_count_jerk_z_d3}, 'f33_pfac_068_inst_value_exp_fit_r2_8q_d3': {'inputs': ['inst_value'], 'func': f33_pfac_068_inst_value_exp_fit_r2_8q_d3}, 'f33_pfac_069_inst_count_below_25pct_16q_fraction_d3': {'inputs': ['inst_count'], 'func': f33_pfac_069_inst_count_below_25pct_16q_fraction_d3}, 'f33_pfac_070_inst_value_below_25pct_16q_fraction_d3': {'inputs': ['inst_value'], 'func': f33_pfac_070_inst_value_below_25pct_16q_fraction_d3}, 'f33_pfac_071_inst_count_slope_4q_minus_12q_d3': {'inputs': ['inst_count'], 'func': f33_pfac_071_inst_count_slope_4q_minus_12q_d3}, 'f33_pfac_072_inst_value_slope_4q_minus_12q_d3': {'inputs': ['inst_value'], 'func': f33_pfac_072_inst_value_slope_4q_minus_12q_d3}, 'f33_pfac_073_compound_triple_deterioration_count_4q_d3': {'inputs': ['inst_count', 'inst_value', 'inst_shares'], 'func': f33_pfac_073_compound_triple_deterioration_count_4q_d3}, 'f33_pfac_074_composite_inst_exit_accel_4q_d3': {'inputs': ['inst_count', 'inst_value', 'inst_shares'], 'func': f33_pfac_074_composite_inst_exit_accel_4q_d3}, 'f33_pfac_075_composite_inst_vs_etf_divergence_z_4q_d3': {'inputs': ['etf_share', 'inst_value'], 'func': f33_pfac_075_composite_inst_vs_etf_divergence_z_4q_d3}}
