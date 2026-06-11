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


def f19mne_f19_marketplace_network_effects_revsgadiv_raw_21d_base_v001_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 21)
    base = rd
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_raw_63d_base_v002_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 63)
    base = rd
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_raw_126d_base_v003_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 126)
    base = rd
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_raw_189d_base_v004_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 189)
    base = rd
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_raw_252d_base_v005_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 252)
    base = rd
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_raw_378d_base_v006_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 378)
    base = rd
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_rmean_21d_base_v007_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 21)
    base = _mean(rd, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_rmean_63d_base_v008_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 63)
    base = _mean(rd, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_rmean_126d_base_v009_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 126)
    base = _mean(rd, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_rmean_189d_base_v010_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 189)
    base = _mean(rd, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_rmean_252d_base_v011_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 252)
    base = _mean(rd, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_rmean_378d_base_v012_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 378)
    base = _mean(rd, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_rstd_21d_base_v013_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 21)
    base = _std(rd, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_rstd_63d_base_v014_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 63)
    base = _std(rd, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_rstd_126d_base_v015_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 126)
    base = _std(rd, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_rstd_189d_base_v016_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 189)
    base = _std(rd, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_rstd_252d_base_v017_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 252)
    base = _std(rd, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_rstd_378d_base_v018_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 378)
    base = _std(rd, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_z_21d_base_v019_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 21)
    base = _z(rd, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_z_63d_base_v020_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 63)
    base = _z(rd, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_z_126d_base_v021_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 126)
    base = _z(rd, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_z_189d_base_v022_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 189)
    base = _z(rd, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_z_252d_base_v023_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 252)
    base = _z(rd, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_z_378d_base_v024_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 378)
    base = _z(rd, 756)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_diff_21d_base_v025_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 21)
    base = rd - rd.shift(21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_diff_63d_base_v026_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 63)
    base = rd - rd.shift(63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_diff_126d_base_v027_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 126)
    base = rd - rd.shift(126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_diff_189d_base_v028_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 189)
    base = rd - rd.shift(189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_diff_252d_base_v029_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 252)
    base = rd - rd.shift(252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_revsgadiv_diff_378d_base_v030_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 378)
    base = rd - rd.shift(378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_raw_21d_base_v031_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 21)
    base = na
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_raw_63d_base_v032_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 63)
    base = na
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_raw_126d_base_v033_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 126)
    base = na
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_raw_189d_base_v034_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 189)
    base = na
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_raw_252d_base_v035_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 252)
    base = na
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_raw_378d_base_v036_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 378)
    base = na
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_rmean_21d_base_v037_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 21)
    base = _mean(na, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_rmean_63d_base_v038_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 63)
    base = _mean(na, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_rmean_126d_base_v039_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 126)
    base = _mean(na, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_rmean_189d_base_v040_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 189)
    base = _mean(na, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_rmean_252d_base_v041_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 252)
    base = _mean(na, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_rmean_378d_base_v042_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 378)
    base = _mean(na, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_z_21d_base_v043_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 21)
    base = _z(na, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_z_63d_base_v044_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 63)
    base = _z(na, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_z_126d_base_v045_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 126)
    base = _z(na, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_z_189d_base_v046_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 189)
    base = _z(na, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_z_252d_base_v047_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 252)
    base = _z(na, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_z_378d_base_v048_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 378)
    base = _z(na, 756)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_sq_21d_base_v049_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 21)
    base = na * na.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_sq_63d_base_v050_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 63)
    base = na * na.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_sq_126d_base_v051_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 126)
    base = na * na.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_sq_189d_base_v052_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 189)
    base = na * na.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_sq_252d_base_v053_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 252)
    base = na * na.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_sq_378d_base_v054_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 378)
    base = na * na.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_absx_21d_base_v055_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 21)
    base = na.abs() * np.sign(na)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_absx_63d_base_v056_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 63)
    base = na.abs() * np.sign(na)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_absx_126d_base_v057_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 126)
    base = na.abs() * np.sign(na)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_absx_189d_base_v058_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 189)
    base = na.abs() * np.sign(na)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_absx_252d_base_v059_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 252)
    base = na.abs() * np.sign(na)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_netacc_absx_378d_base_v060_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 378)
    base = na.abs() * np.sign(na)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_raw_21d_base_v061_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 21)
    base = se
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_raw_63d_base_v062_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 63)
    base = se
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_raw_126d_base_v063_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 126)
    base = se
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_raw_189d_base_v064_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 189)
    base = se
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_raw_252d_base_v065_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 252)
    base = se
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_raw_378d_base_v066_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 378)
    base = se
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_rmean_21d_base_v067_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 21)
    base = _mean(se, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_rmean_63d_base_v068_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 63)
    base = _mean(se, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_rmean_126d_base_v069_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 126)
    base = _mean(se, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_rmean_189d_base_v070_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 189)
    base = _mean(se, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_rmean_252d_base_v071_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 252)
    base = _mean(se, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_rmean_378d_base_v072_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 378)
    base = _mean(se, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_z_21d_base_v073_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 21)
    base = _z(se, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_z_63d_base_v074_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 63)
    base = _z(se, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_z_126d_base_v075_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 126)
    base = _z(se, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f19mne_f19_marketplace_network_effects_revsgadiv_raw_21d_base_v001_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_raw_63d_base_v002_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_raw_126d_base_v003_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_raw_189d_base_v004_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_raw_252d_base_v005_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_raw_378d_base_v006_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_rmean_21d_base_v007_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_rmean_63d_base_v008_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_rmean_126d_base_v009_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_rmean_189d_base_v010_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_rmean_252d_base_v011_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_rmean_378d_base_v012_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_rstd_21d_base_v013_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_rstd_63d_base_v014_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_rstd_126d_base_v015_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_rstd_189d_base_v016_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_rstd_252d_base_v017_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_rstd_378d_base_v018_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_z_21d_base_v019_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_z_63d_base_v020_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_z_126d_base_v021_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_z_189d_base_v022_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_z_252d_base_v023_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_z_378d_base_v024_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_diff_21d_base_v025_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_diff_63d_base_v026_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_diff_126d_base_v027_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_diff_189d_base_v028_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_diff_252d_base_v029_signal,
    f19mne_f19_marketplace_network_effects_revsgadiv_diff_378d_base_v030_signal,
    f19mne_f19_marketplace_network_effects_netacc_raw_21d_base_v031_signal,
    f19mne_f19_marketplace_network_effects_netacc_raw_63d_base_v032_signal,
    f19mne_f19_marketplace_network_effects_netacc_raw_126d_base_v033_signal,
    f19mne_f19_marketplace_network_effects_netacc_raw_189d_base_v034_signal,
    f19mne_f19_marketplace_network_effects_netacc_raw_252d_base_v035_signal,
    f19mne_f19_marketplace_network_effects_netacc_raw_378d_base_v036_signal,
    f19mne_f19_marketplace_network_effects_netacc_rmean_21d_base_v037_signal,
    f19mne_f19_marketplace_network_effects_netacc_rmean_63d_base_v038_signal,
    f19mne_f19_marketplace_network_effects_netacc_rmean_126d_base_v039_signal,
    f19mne_f19_marketplace_network_effects_netacc_rmean_189d_base_v040_signal,
    f19mne_f19_marketplace_network_effects_netacc_rmean_252d_base_v041_signal,
    f19mne_f19_marketplace_network_effects_netacc_rmean_378d_base_v042_signal,
    f19mne_f19_marketplace_network_effects_netacc_z_21d_base_v043_signal,
    f19mne_f19_marketplace_network_effects_netacc_z_63d_base_v044_signal,
    f19mne_f19_marketplace_network_effects_netacc_z_126d_base_v045_signal,
    f19mne_f19_marketplace_network_effects_netacc_z_189d_base_v046_signal,
    f19mne_f19_marketplace_network_effects_netacc_z_252d_base_v047_signal,
    f19mne_f19_marketplace_network_effects_netacc_z_378d_base_v048_signal,
    f19mne_f19_marketplace_network_effects_netacc_sq_21d_base_v049_signal,
    f19mne_f19_marketplace_network_effects_netacc_sq_63d_base_v050_signal,
    f19mne_f19_marketplace_network_effects_netacc_sq_126d_base_v051_signal,
    f19mne_f19_marketplace_network_effects_netacc_sq_189d_base_v052_signal,
    f19mne_f19_marketplace_network_effects_netacc_sq_252d_base_v053_signal,
    f19mne_f19_marketplace_network_effects_netacc_sq_378d_base_v054_signal,
    f19mne_f19_marketplace_network_effects_netacc_absx_21d_base_v055_signal,
    f19mne_f19_marketplace_network_effects_netacc_absx_63d_base_v056_signal,
    f19mne_f19_marketplace_network_effects_netacc_absx_126d_base_v057_signal,
    f19mne_f19_marketplace_network_effects_netacc_absx_189d_base_v058_signal,
    f19mne_f19_marketplace_network_effects_netacc_absx_252d_base_v059_signal,
    f19mne_f19_marketplace_network_effects_netacc_absx_378d_base_v060_signal,
    f19mne_f19_marketplace_network_effects_scaleff_raw_21d_base_v061_signal,
    f19mne_f19_marketplace_network_effects_scaleff_raw_63d_base_v062_signal,
    f19mne_f19_marketplace_network_effects_scaleff_raw_126d_base_v063_signal,
    f19mne_f19_marketplace_network_effects_scaleff_raw_189d_base_v064_signal,
    f19mne_f19_marketplace_network_effects_scaleff_raw_252d_base_v065_signal,
    f19mne_f19_marketplace_network_effects_scaleff_raw_378d_base_v066_signal,
    f19mne_f19_marketplace_network_effects_scaleff_rmean_21d_base_v067_signal,
    f19mne_f19_marketplace_network_effects_scaleff_rmean_63d_base_v068_signal,
    f19mne_f19_marketplace_network_effects_scaleff_rmean_126d_base_v069_signal,
    f19mne_f19_marketplace_network_effects_scaleff_rmean_189d_base_v070_signal,
    f19mne_f19_marketplace_network_effects_scaleff_rmean_252d_base_v071_signal,
    f19mne_f19_marketplace_network_effects_scaleff_rmean_378d_base_v072_signal,
    f19mne_f19_marketplace_network_effects_scaleff_z_21d_base_v073_signal,
    f19mne_f19_marketplace_network_effects_scaleff_z_63d_base_v074_signal,
    f19mne_f19_marketplace_network_effects_scaleff_z_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FMARKETPLACE_NETWORK_EFFECTS_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f19_marketplace_network_effects_base_001_075_claude: {n_features} features pass")
