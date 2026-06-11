import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)

# ===== folder domain primitives =====
def _f19_revenue_sga_divergence(revenue, sgna, w):
    return revenue.pct_change(periods=w) - sgna.pct_change(periods=w)


def _f19_network_acceleration(revenue, sgna, w):
    rg = revenue.pct_change(periods=w)
    sg = sgna.pct_change(periods=w)
    div = rg - sg
    return div - div.rolling(w, min_periods=max(1, w // 2)).mean()


def _f19_scale_efficiency(revenue, sgna, w):
    r2s = revenue / sgna.replace(0, np.nan)
    return r2s - r2s.rolling(w, min_periods=max(1, w // 2)).mean()


def f19mne_f19_marketplace_network_effects_revsgadiv_raw_21d_slope_v001_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 21)
    base = rd
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_raw_63d_slope_v002_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 63)
    base = rd
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_raw_126d_slope_v003_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 126)
    base = rd
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_raw_189d_slope_v004_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 189)
    base = rd
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_raw_252d_slope_v005_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 252)
    base = rd
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_raw_378d_slope_v006_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 378)
    base = rd
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_rmean_21d_slope_v007_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 21)
    base = _mean(rd, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_rmean_63d_slope_v008_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 63)
    base = _mean(rd, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_rmean_126d_slope_v009_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 126)
    base = _mean(rd, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_rmean_189d_slope_v010_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 189)
    base = _mean(rd, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_rmean_252d_slope_v011_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 252)
    base = _mean(rd, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_rmean_378d_slope_v012_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 378)
    base = _mean(rd, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_rstd_21d_slope_v013_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 21)
    base = _std(rd, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_rstd_63d_slope_v014_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 63)
    base = _std(rd, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_rstd_126d_slope_v015_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 126)
    base = _std(rd, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_rstd_189d_slope_v016_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 189)
    base = _std(rd, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_rstd_252d_slope_v017_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 252)
    base = _std(rd, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_rstd_378d_slope_v018_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 378)
    base = _std(rd, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_z_21d_slope_v019_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 21)
    base = _z(rd, 63)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_z_63d_slope_v020_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 63)
    base = _z(rd, 126)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_z_126d_slope_v021_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 126)
    base = _z(rd, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_z_189d_slope_v022_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 189)
    base = _z(rd, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_z_252d_slope_v023_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 252)
    base = _z(rd, 504)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_z_378d_slope_v024_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 378)
    base = _z(rd, 756)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_diff_21d_slope_v025_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 21)
    base = rd - rd.shift(21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_diff_63d_slope_v026_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 63)
    base = rd - rd.shift(63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_diff_126d_slope_v027_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 126)
    base = rd - rd.shift(126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_diff_189d_slope_v028_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 189)
    base = rd - rd.shift(189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_diff_252d_slope_v029_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 252)
    base = rd - rd.shift(252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_diff_378d_slope_v030_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 378)
    base = rd - rd.shift(378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_raw_21d_slope_v031_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 21)
    base = na
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_raw_63d_slope_v032_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 63)
    base = na
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_raw_126d_slope_v033_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 126)
    base = na
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_raw_189d_slope_v034_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 189)
    base = na
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_raw_252d_slope_v035_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 252)
    base = na
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_raw_378d_slope_v036_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 378)
    base = na
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_rmean_21d_slope_v037_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 21)
    base = _mean(na, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_rmean_63d_slope_v038_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 63)
    base = _mean(na, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_rmean_126d_slope_v039_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 126)
    base = _mean(na, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_rmean_189d_slope_v040_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 189)
    base = _mean(na, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_rmean_252d_slope_v041_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 252)
    base = _mean(na, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_rmean_378d_slope_v042_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 378)
    base = _mean(na, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_z_21d_slope_v043_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 21)
    base = _z(na, 63)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_z_63d_slope_v044_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 63)
    base = _z(na, 126)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_z_126d_slope_v045_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 126)
    base = _z(na, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_z_189d_slope_v046_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 189)
    base = _z(na, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_z_252d_slope_v047_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 252)
    base = _z(na, 504)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_z_378d_slope_v048_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 378)
    base = _z(na, 756)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_sq_21d_slope_v049_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 21)
    base = na * na.abs()
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_sq_63d_slope_v050_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 63)
    base = na * na.abs()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_sq_126d_slope_v051_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 126)
    base = na * na.abs()
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_sq_189d_slope_v052_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 189)
    base = na * na.abs()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_sq_252d_slope_v053_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 252)
    base = na * na.abs()
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_sq_378d_slope_v054_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 378)
    base = na * na.abs()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_absx_21d_slope_v055_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 21)
    base = na.abs() * np.sign(na)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_absx_63d_slope_v056_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 63)
    base = na.abs() * np.sign(na)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_absx_126d_slope_v057_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 126)
    base = na.abs() * np.sign(na)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_absx_189d_slope_v058_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 189)
    base = na.abs() * np.sign(na)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_absx_252d_slope_v059_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 252)
    base = na.abs() * np.sign(na)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_absx_378d_slope_v060_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 378)
    base = na.abs() * np.sign(na)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_raw_21d_slope_v061_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 21)
    base = se
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_raw_63d_slope_v062_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 63)
    base = se
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_raw_126d_slope_v063_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 126)
    base = se
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_raw_189d_slope_v064_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 189)
    base = se
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_raw_252d_slope_v065_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 252)
    base = se
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_raw_378d_slope_v066_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 378)
    base = se
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_rmean_21d_slope_v067_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 21)
    base = _mean(se, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_rmean_63d_slope_v068_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 63)
    base = _mean(se, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_rmean_126d_slope_v069_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 126)
    base = _mean(se, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_rmean_189d_slope_v070_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 189)
    base = _mean(se, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_rmean_252d_slope_v071_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 252)
    base = _mean(se, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_rmean_378d_slope_v072_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 378)
    base = _mean(se, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_z_21d_slope_v073_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 21)
    base = _z(se, 63)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_z_63d_slope_v074_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 63)
    base = _z(se, 126)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_z_126d_slope_v075_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 126)
    base = _z(se, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_z_189d_slope_v076_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 189)
    base = _z(se, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_z_252d_slope_v077_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 252)
    base = _z(se, 504)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_z_378d_slope_v078_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 378)
    base = _z(se, 756)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_sq_21d_slope_v079_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 21)
    base = se * se.abs()
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_sq_63d_slope_v080_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 63)
    base = se * se.abs()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_sq_126d_slope_v081_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 126)
    base = se * se.abs()
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_sq_189d_slope_v082_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 189)
    base = se * se.abs()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_sq_252d_slope_v083_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 252)
    base = se * se.abs()
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_sq_378d_slope_v084_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 378)
    base = se * se.abs()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_rstd_21d_slope_v085_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 21)
    base = _std(se, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_rstd_63d_slope_v086_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 63)
    base = _std(se, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_rstd_126d_slope_v087_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 126)
    base = _std(se, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_rstd_189d_slope_v088_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 189)
    base = _std(se, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_rstd_252d_slope_v089_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 252)
    base = _std(se, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_rstd_378d_slope_v090_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 378)
    base = _std(se, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rdxna_mul_10d_slope_v091_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 10)
    na = _f19_network_acceleration(revenue, sgna, 10)
    base = rd * na
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rdxna_mul_21d_slope_v092_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 21)
    na = _f19_network_acceleration(revenue, sgna, 21)
    base = rd * na
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rdxna_mul_42d_slope_v093_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 42)
    na = _f19_network_acceleration(revenue, sgna, 42)
    base = rd * na
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rdxna_mul_63d_slope_v094_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 63)
    na = _f19_network_acceleration(revenue, sgna, 63)
    base = rd * na
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rdxna_mul_126d_slope_v095_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 126)
    na = _f19_network_acceleration(revenue, sgna, 126)
    base = rd * na
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rdxna_mul_189d_slope_v096_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 189)
    na = _f19_network_acceleration(revenue, sgna, 189)
    base = rd * na
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_napse_sum_10d_slope_v097_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 10)
    se = _f19_scale_efficiency(revenue, sgna, 10)
    base = na + se
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_napse_sum_21d_slope_v098_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 21)
    se = _f19_scale_efficiency(revenue, sgna, 21)
    base = na + se
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_napse_sum_42d_slope_v099_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 42)
    se = _f19_scale_efficiency(revenue, sgna, 42)
    base = na + se
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_napse_sum_63d_slope_v100_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 63)
    se = _f19_scale_efficiency(revenue, sgna, 63)
    base = na + se
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_napse_sum_126d_slope_v101_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 126)
    se = _f19_scale_efficiency(revenue, sgna, 126)
    base = na + se
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_napse_sum_189d_slope_v102_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 189)
    se = _f19_scale_efficiency(revenue, sgna, 189)
    base = na + se
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rdmse_diff_10d_slope_v103_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 10)
    se = _f19_scale_efficiency(revenue, sgna, 10)
    base = rd - se
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rdmse_diff_21d_slope_v104_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 21)
    se = _f19_scale_efficiency(revenue, sgna, 21)
    base = rd - se
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rdmse_diff_42d_slope_v105_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 42)
    se = _f19_scale_efficiency(revenue, sgna, 42)
    base = rd - se
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rdmse_diff_63d_slope_v106_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 63)
    se = _f19_scale_efficiency(revenue, sgna, 63)
    base = rd - se
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rdmse_diff_126d_slope_v107_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 126)
    se = _f19_scale_efficiency(revenue, sgna, 126)
    base = rd - se
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rdmse_diff_189d_slope_v108_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 189)
    se = _f19_scale_efficiency(revenue, sgna, 189)
    base = rd - se
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_opx_10d_slope_v109_signal(revenue, sgna, opex, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 10)
    base = _mean(na, 10) * opex / opex.replace(0, np.nan)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_opx_21d_slope_v110_signal(revenue, sgna, opex, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 21)
    base = _mean(na, 21) * opex / opex.replace(0, np.nan)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_opx_42d_slope_v111_signal(revenue, sgna, opex, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 42)
    base = _mean(na, 42) * opex / opex.replace(0, np.nan)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_opx_63d_slope_v112_signal(revenue, sgna, opex, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 63)
    base = _mean(na, 63) * opex / opex.replace(0, np.nan)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_opx_126d_slope_v113_signal(revenue, sgna, opex, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 126)
    base = _mean(na, 126) * opex / opex.replace(0, np.nan)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_opx_189d_slope_v114_signal(revenue, sgna, opex, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 189)
    base = _mean(na, 189) * opex / opex.replace(0, np.nan)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rd_dsmooth_10d_slope_v115_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 10)
    base = rd.diff(10).rolling(10, min_periods=max(1,10//2)).mean()
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rd_dsmooth_21d_slope_v116_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 21)
    base = rd.diff(21).rolling(21, min_periods=max(1,21//2)).mean()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rd_dsmooth_42d_slope_v117_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 42)
    base = rd.diff(42).rolling(42, min_periods=max(1,42//2)).mean()
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rd_dsmooth_63d_slope_v118_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 63)
    base = rd.diff(63).rolling(63, min_periods=max(1,63//2)).mean()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rd_dsmooth_126d_slope_v119_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 126)
    base = rd.diff(126).rolling(126, min_periods=max(1,126//2)).mean()
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rd_dsmooth_189d_slope_v120_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 189)
    base = rd.diff(189).rolling(189, min_periods=max(1,189//2)).mean()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_ema_10d_slope_v121_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 10)
    base = na.ewm(span=10, min_periods=max(1, 10//2)).mean()
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_ema_21d_slope_v122_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 21)
    base = na.ewm(span=21, min_periods=max(1, 21//2)).mean()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_ema_42d_slope_v123_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 42)
    base = na.ewm(span=42, min_periods=max(1, 42//2)).mean()
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_ema_63d_slope_v124_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 63)
    base = na.ewm(span=63, min_periods=max(1, 63//2)).mean()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_ema_126d_slope_v125_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 126)
    base = na.ewm(span=126, min_periods=max(1, 126//2)).mean()
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_ema_189d_slope_v126_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 189)
    base = na.ewm(span=189, min_periods=max(1, 189//2)).mean()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_se_range_10d_slope_v127_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 10)
    base = se.rolling(10, min_periods=max(1, 10//2)).max() - se.rolling(10, min_periods=max(1, 10//2)).min()
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_se_range_21d_slope_v128_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 21)
    base = se.rolling(21, min_periods=max(1, 21//2)).max() - se.rolling(21, min_periods=max(1, 21//2)).min()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_se_range_42d_slope_v129_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 42)
    base = se.rolling(42, min_periods=max(1, 42//2)).max() - se.rolling(42, min_periods=max(1, 42//2)).min()
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_se_range_63d_slope_v130_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 63)
    base = se.rolling(63, min_periods=max(1, 63//2)).max() - se.rolling(63, min_periods=max(1, 63//2)).min()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_se_range_126d_slope_v131_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 126)
    base = se.rolling(126, min_periods=max(1, 126//2)).max() - se.rolling(126, min_periods=max(1, 126//2)).min()
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_se_range_189d_slope_v132_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 189)
    base = se.rolling(189, min_periods=max(1, 189//2)).max() - se.rolling(189, min_periods=max(1, 189//2)).min()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rd_dmed_10d_slope_v133_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 10)
    base = (rd - rd.rolling(10, min_periods=max(1, 10//2)).median())
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rd_dmed_21d_slope_v134_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 21)
    base = (rd - rd.rolling(21, min_periods=max(1, 21//2)).median())
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rd_dmed_42d_slope_v135_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 42)
    base = (rd - rd.rolling(42, min_periods=max(1, 42//2)).median())
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rd_dmed_63d_slope_v136_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 63)
    base = (rd - rd.rolling(63, min_periods=max(1, 63//2)).median())
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rd_dmed_126d_slope_v137_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 126)
    base = (rd - rd.rolling(126, min_periods=max(1, 126//2)).median())
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rd_dmed_189d_slope_v138_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 189)
    base = (rd - rd.rolling(189, min_periods=max(1, 189//2)).median())
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_iqr_10d_slope_v139_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 10)
    base = na.rolling(10, min_periods=max(1, 10//2)).quantile(0.75) - na.rolling(10, min_periods=max(1, 10//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_iqr_21d_slope_v140_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 21)
    base = na.rolling(21, min_periods=max(1, 21//2)).quantile(0.75) - na.rolling(21, min_periods=max(1, 21//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_iqr_42d_slope_v141_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 42)
    base = na.rolling(42, min_periods=max(1, 42//2)).quantile(0.75) - na.rolling(42, min_periods=max(1, 42//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_iqr_63d_slope_v142_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 63)
    base = na.rolling(63, min_periods=max(1, 63//2)).quantile(0.75) - na.rolling(63, min_periods=max(1, 63//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_iqr_126d_slope_v143_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 126)
    base = na.rolling(126, min_periods=max(1, 126//2)).quantile(0.75) - na.rolling(126, min_periods=max(1, 126//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_iqr_189d_slope_v144_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 189)
    base = na.rolling(189, min_periods=max(1, 189//2)).quantile(0.75) - na.rolling(189, min_periods=max(1, 189//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_se_iqr_10d_slope_v145_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 10)
    base = se.rolling(10, min_periods=max(1, 10//2)).quantile(0.75) - se.rolling(10, min_periods=max(1, 10//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_se_iqr_21d_slope_v146_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 21)
    base = se.rolling(21, min_periods=max(1, 21//2)).quantile(0.75) - se.rolling(21, min_periods=max(1, 21//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_se_iqr_42d_slope_v147_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 42)
    base = se.rolling(42, min_periods=max(1, 42//2)).quantile(0.75) - se.rolling(42, min_periods=max(1, 42//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_se_iqr_63d_slope_v148_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 63)
    base = se.rolling(63, min_periods=max(1, 63//2)).quantile(0.75) - se.rolling(63, min_periods=max(1, 63//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_se_iqr_126d_slope_v149_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 126)
    base = se.rolling(126, min_periods=max(1, 126//2)).quantile(0.75) - se.rolling(126, min_periods=max(1, 126//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_se_iqr_189d_slope_v150_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 189)
    base = se.rolling(189, min_periods=max(1, 189//2)).quantile(0.75) - se.rolling(189, min_periods=max(1, 189//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f19mne_f19_marketplace_network_effects_revsgadiv_raw_21d_slope_v001_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_raw_63d_slope_v002_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_raw_126d_slope_v003_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_raw_189d_slope_v004_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_raw_252d_slope_v005_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_raw_378d_slope_v006_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_rmean_21d_slope_v007_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_rmean_63d_slope_v008_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_rmean_126d_slope_v009_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_rmean_189d_slope_v010_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_rmean_252d_slope_v011_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_rmean_378d_slope_v012_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_rstd_21d_slope_v013_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_rstd_63d_slope_v014_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_rstd_126d_slope_v015_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_rstd_189d_slope_v016_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_rstd_252d_slope_v017_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_rstd_378d_slope_v018_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_z_21d_slope_v019_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_z_63d_slope_v020_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_z_126d_slope_v021_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_z_189d_slope_v022_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_z_252d_slope_v023_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_z_378d_slope_v024_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_diff_21d_slope_v025_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_diff_63d_slope_v026_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_diff_126d_slope_v027_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_diff_189d_slope_v028_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_diff_252d_slope_v029_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_diff_378d_slope_v030_signal,
    f19mne_f19_marketplace_network_effects_netacc_raw_21d_slope_v031_signal,
    f19mne_f19_marketplace_network_effects_netacc_raw_63d_slope_v032_signal,
    f19mne_f19_marketplace_network_effects_netacc_raw_126d_slope_v033_signal,
    f19mne_f19_marketplace_network_effects_netacc_raw_189d_slope_v034_signal,
    f19mne_f19_marketplace_network_effects_netacc_raw_252d_slope_v035_signal,
    f19mne_f19_marketplace_network_effects_netacc_raw_378d_slope_v036_signal,
    f19mne_f19_marketplace_network_effects_netacc_rmean_21d_slope_v037_signal,
    f19mne_f19_marketplace_network_effects_netacc_rmean_63d_slope_v038_signal,
    f19mne_f19_marketplace_network_effects_netacc_rmean_126d_slope_v039_signal,
    f19mne_f19_marketplace_network_effects_netacc_rmean_189d_slope_v040_signal,
    f19mne_f19_marketplace_network_effects_netacc_rmean_252d_slope_v041_signal,
    f19mne_f19_marketplace_network_effects_netacc_rmean_378d_slope_v042_signal,
    f19mne_f19_marketplace_network_effects_netacc_z_21d_slope_v043_signal,
    f19mne_f19_marketplace_network_effects_netacc_z_63d_slope_v044_signal,
    f19mne_f19_marketplace_network_effects_netacc_z_126d_slope_v045_signal,
    f19mne_f19_marketplace_network_effects_netacc_z_189d_slope_v046_signal,
    f19mne_f19_marketplace_network_effects_netacc_z_252d_slope_v047_signal,
    f19mne_f19_marketplace_network_effects_netacc_z_378d_slope_v048_signal,
    f19mne_f19_marketplace_network_effects_netacc_sq_21d_slope_v049_signal,
    f19mne_f19_marketplace_network_effects_netacc_sq_63d_slope_v050_signal,
    f19mne_f19_marketplace_network_effects_netacc_sq_126d_slope_v051_signal,
    f19mne_f19_marketplace_network_effects_netacc_sq_189d_slope_v052_signal,
    f19mne_f19_marketplace_network_effects_netacc_sq_252d_slope_v053_signal,
    f19mne_f19_marketplace_network_effects_netacc_sq_378d_slope_v054_signal,
    f19mne_f19_marketplace_network_effects_netacc_absx_21d_slope_v055_signal,
    f19mne_f19_marketplace_network_effects_netacc_absx_63d_slope_v056_signal,
    f19mne_f19_marketplace_network_effects_netacc_absx_126d_slope_v057_signal,
    f19mne_f19_marketplace_network_effects_netacc_absx_189d_slope_v058_signal,
    f19mne_f19_marketplace_network_effects_netacc_absx_252d_slope_v059_signal,
    f19mne_f19_marketplace_network_effects_netacc_absx_378d_slope_v060_signal,
    f19mne_f19_marketplace_network_effects_scaleff_raw_21d_slope_v061_signal,
    f19mne_f19_marketplace_network_effects_scaleff_raw_63d_slope_v062_signal,
    f19mne_f19_marketplace_network_effects_scaleff_raw_126d_slope_v063_signal,
    f19mne_f19_marketplace_network_effects_scaleff_raw_189d_slope_v064_signal,
    f19mne_f19_marketplace_network_effects_scaleff_raw_252d_slope_v065_signal,
    f19mne_f19_marketplace_network_effects_scaleff_raw_378d_slope_v066_signal,
    f19mne_f19_marketplace_network_effects_scaleff_rmean_21d_slope_v067_signal,
    f19mne_f19_marketplace_network_effects_scaleff_rmean_63d_slope_v068_signal,
    f19mne_f19_marketplace_network_effects_scaleff_rmean_126d_slope_v069_signal,
    f19mne_f19_marketplace_network_effects_scaleff_rmean_189d_slope_v070_signal,
    f19mne_f19_marketplace_network_effects_scaleff_rmean_252d_slope_v071_signal,
    f19mne_f19_marketplace_network_effects_scaleff_rmean_378d_slope_v072_signal,
    f19mne_f19_marketplace_network_effects_scaleff_z_21d_slope_v073_signal,
    f19mne_f19_marketplace_network_effects_scaleff_z_63d_slope_v074_signal,
    f19mne_f19_marketplace_network_effects_scaleff_z_126d_slope_v075_signal,
    f19mne_f19_marketplace_network_effects_scaleff_z_189d_slope_v076_signal,
    f19mne_f19_marketplace_network_effects_scaleff_z_252d_slope_v077_signal,
    f19mne_f19_marketplace_network_effects_scaleff_z_378d_slope_v078_signal,
    f19mne_f19_marketplace_network_effects_scaleff_sq_21d_slope_v079_signal,
    f19mne_f19_marketplace_network_effects_scaleff_sq_63d_slope_v080_signal,
    f19mne_f19_marketplace_network_effects_scaleff_sq_126d_slope_v081_signal,
    f19mne_f19_marketplace_network_effects_scaleff_sq_189d_slope_v082_signal,
    f19mne_f19_marketplace_network_effects_scaleff_sq_252d_slope_v083_signal,
    f19mne_f19_marketplace_network_effects_scaleff_sq_378d_slope_v084_signal,
    f19mne_f19_marketplace_network_effects_scaleff_rstd_21d_slope_v085_signal,
    f19mne_f19_marketplace_network_effects_scaleff_rstd_63d_slope_v086_signal,
    f19mne_f19_marketplace_network_effects_scaleff_rstd_126d_slope_v087_signal,
    f19mne_f19_marketplace_network_effects_scaleff_rstd_189d_slope_v088_signal,
    f19mne_f19_marketplace_network_effects_scaleff_rstd_252d_slope_v089_signal,
    f19mne_f19_marketplace_network_effects_scaleff_rstd_378d_slope_v090_signal,
    f19mne_f19_marketplace_network_effects_rdxna_mul_10d_slope_v091_signal,
    f19mne_f19_marketplace_network_effects_rdxna_mul_21d_slope_v092_signal,
    f19mne_f19_marketplace_network_effects_rdxna_mul_42d_slope_v093_signal,
    f19mne_f19_marketplace_network_effects_rdxna_mul_63d_slope_v094_signal,
    f19mne_f19_marketplace_network_effects_rdxna_mul_126d_slope_v095_signal,
    f19mne_f19_marketplace_network_effects_rdxna_mul_189d_slope_v096_signal,
    f19mne_f19_marketplace_network_effects_napse_sum_10d_slope_v097_signal,
    f19mne_f19_marketplace_network_effects_napse_sum_21d_slope_v098_signal,
    f19mne_f19_marketplace_network_effects_napse_sum_42d_slope_v099_signal,
    f19mne_f19_marketplace_network_effects_napse_sum_63d_slope_v100_signal,
    f19mne_f19_marketplace_network_effects_napse_sum_126d_slope_v101_signal,
    f19mne_f19_marketplace_network_effects_napse_sum_189d_slope_v102_signal,
    f19mne_f19_marketplace_network_effects_rdmse_diff_10d_slope_v103_signal,
    f19mne_f19_marketplace_network_effects_rdmse_diff_21d_slope_v104_signal,
    f19mne_f19_marketplace_network_effects_rdmse_diff_42d_slope_v105_signal,
    f19mne_f19_marketplace_network_effects_rdmse_diff_63d_slope_v106_signal,
    f19mne_f19_marketplace_network_effects_rdmse_diff_126d_slope_v107_signal,
    f19mne_f19_marketplace_network_effects_rdmse_diff_189d_slope_v108_signal,
    f19mne_f19_marketplace_network_effects_na_opx_10d_slope_v109_signal,
    f19mne_f19_marketplace_network_effects_na_opx_21d_slope_v110_signal,
    f19mne_f19_marketplace_network_effects_na_opx_42d_slope_v111_signal,
    f19mne_f19_marketplace_network_effects_na_opx_63d_slope_v112_signal,
    f19mne_f19_marketplace_network_effects_na_opx_126d_slope_v113_signal,
    f19mne_f19_marketplace_network_effects_na_opx_189d_slope_v114_signal,
    f19mne_f19_marketplace_network_effects_rd_dsmooth_10d_slope_v115_signal,
    f19mne_f19_marketplace_network_effects_rd_dsmooth_21d_slope_v116_signal,
    f19mne_f19_marketplace_network_effects_rd_dsmooth_42d_slope_v117_signal,
    f19mne_f19_marketplace_network_effects_rd_dsmooth_63d_slope_v118_signal,
    f19mne_f19_marketplace_network_effects_rd_dsmooth_126d_slope_v119_signal,
    f19mne_f19_marketplace_network_effects_rd_dsmooth_189d_slope_v120_signal,
    f19mne_f19_marketplace_network_effects_na_ema_10d_slope_v121_signal,
    f19mne_f19_marketplace_network_effects_na_ema_21d_slope_v122_signal,
    f19mne_f19_marketplace_network_effects_na_ema_42d_slope_v123_signal,
    f19mne_f19_marketplace_network_effects_na_ema_63d_slope_v124_signal,
    f19mne_f19_marketplace_network_effects_na_ema_126d_slope_v125_signal,
    f19mne_f19_marketplace_network_effects_na_ema_189d_slope_v126_signal,
    f19mne_f19_marketplace_network_effects_se_range_10d_slope_v127_signal,
    f19mne_f19_marketplace_network_effects_se_range_21d_slope_v128_signal,
    f19mne_f19_marketplace_network_effects_se_range_42d_slope_v129_signal,
    f19mne_f19_marketplace_network_effects_se_range_63d_slope_v130_signal,
    f19mne_f19_marketplace_network_effects_se_range_126d_slope_v131_signal,
    f19mne_f19_marketplace_network_effects_se_range_189d_slope_v132_signal,
    f19mne_f19_marketplace_network_effects_rd_dmed_10d_slope_v133_signal,
    f19mne_f19_marketplace_network_effects_rd_dmed_21d_slope_v134_signal,
    f19mne_f19_marketplace_network_effects_rd_dmed_42d_slope_v135_signal,
    f19mne_f19_marketplace_network_effects_rd_dmed_63d_slope_v136_signal,
    f19mne_f19_marketplace_network_effects_rd_dmed_126d_slope_v137_signal,
    f19mne_f19_marketplace_network_effects_rd_dmed_189d_slope_v138_signal,
    f19mne_f19_marketplace_network_effects_na_iqr_10d_slope_v139_signal,
    f19mne_f19_marketplace_network_effects_na_iqr_21d_slope_v140_signal,
    f19mne_f19_marketplace_network_effects_na_iqr_42d_slope_v141_signal,
    f19mne_f19_marketplace_network_effects_na_iqr_63d_slope_v142_signal,
    f19mne_f19_marketplace_network_effects_na_iqr_126d_slope_v143_signal,
    f19mne_f19_marketplace_network_effects_na_iqr_189d_slope_v144_signal,
    f19mne_f19_marketplace_network_effects_se_iqr_10d_slope_v145_signal,
    f19mne_f19_marketplace_network_effects_se_iqr_21d_slope_v146_signal,
    f19mne_f19_marketplace_network_effects_se_iqr_42d_slope_v147_signal,
    f19mne_f19_marketplace_network_effects_se_iqr_63d_slope_v148_signal,
    f19mne_f19_marketplace_network_effects_se_iqr_126d_slope_v149_signal,
    f19mne_f19_marketplace_network_effects_se_iqr_189d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FMARKETPLACE_NETWORK_EFFECTS_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "sgna": sgna, "opex": opex,
        "gp": gp, "workingcapital": workingcapital,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f19_revenue_sga_divergence", "_f19_network_acceleration", "_f19_scale_efficiency",)
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f19_marketplace_network_effects_2nd_derivatives_001_150_claude: {n_features} features pass")
