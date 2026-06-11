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
def _f11_intangibles_growth(intangibles, w):
    return intangibles.pct_change(periods=w)


def _f11_asset_growth_pulse(assets, w):
    g = assets.pct_change(periods=w)
    return g - g.rolling(w, min_periods=max(1, w // 2)).mean()


def _f11_acquisition_pulse(intangibles, assets, w):
    ig = intangibles.pct_change(periods=w)
    ag = assets.pct_change(periods=w)
    return (ig - ag)



def f11sba_f11_small_bank_acquisition_signature_intgrowmean_63d_63_base_v076_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 63)
    result = _mean(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_intgrowmean_126d_21_base_v077_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 126)
    result = _mean(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_intgrowmean_126d_63_base_v078_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 126)
    result = _mean(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_intgrowmean_252d_21_base_v079_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 252)
    result = _mean(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_intgrowmean_252d_63_base_v080_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 252)
    result = _mean(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_assetpulsestd_21d_21_base_v081_signal(assets, closeadj):
    g = _f11_asset_growth_pulse(assets, 21)
    result = _std(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_assetpulsestd_21d_63_base_v082_signal(assets, closeadj):
    g = _f11_asset_growth_pulse(assets, 21)
    result = _std(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_assetpulsestd_42d_21_base_v083_signal(assets, closeadj):
    g = _f11_asset_growth_pulse(assets, 42)
    result = _std(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_assetpulsestd_42d_63_base_v084_signal(assets, closeadj):
    g = _f11_asset_growth_pulse(assets, 42)
    result = _std(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_assetpulsestd_63d_21_base_v085_signal(assets, closeadj):
    g = _f11_asset_growth_pulse(assets, 63)
    result = _std(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_assetpulsestd_63d_63_base_v086_signal(assets, closeadj):
    g = _f11_asset_growth_pulse(assets, 63)
    result = _std(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_assetpulsestd_126d_21_base_v087_signal(assets, closeadj):
    g = _f11_asset_growth_pulse(assets, 126)
    result = _std(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_assetpulsestd_126d_63_base_v088_signal(assets, closeadj):
    g = _f11_asset_growth_pulse(assets, 126)
    result = _std(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_assetpulsestd_252d_21_base_v089_signal(assets, closeadj):
    g = _f11_asset_growth_pulse(assets, 252)
    result = _std(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_assetpulsestd_252d_63_base_v090_signal(assets, closeadj):
    g = _f11_asset_growth_pulse(assets, 252)
    result = _std(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsez_21d_63_base_v091_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 21)
    result = _z(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsez_21d_126_base_v092_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 21)
    result = _z(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsez_42d_63_base_v093_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 42)
    result = _z(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsez_42d_126_base_v094_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 42)
    result = _z(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsez_63d_63_base_v095_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 63)
    result = _z(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsez_63d_126_base_v096_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 63)
    result = _z(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsez_126d_63_base_v097_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 126)
    result = _z(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsez_126d_126_base_v098_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 126)
    result = _z(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsez_252d_63_base_v099_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 252)
    result = _z(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsez_252d_126_base_v100_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 252)
    result = _z(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_intgrowsq_5d_base_v101_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 5)
    result = (g * g.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_intgrowsq_10d_base_v102_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 10)
    result = (g * g.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_intgrowsq_21d_base_v103_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 21)
    result = (g * g.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_intgrowsq_42d_base_v104_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 42)
    result = (g * g.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_intgrowsq_63d_base_v105_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 63)
    result = (g * g.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_intgrowsq_126d_base_v106_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 126)
    result = (g * g.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_intgrowsq_189d_base_v107_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 189)
    result = (g * g.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_intgrowsq_252d_base_v108_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 252)
    result = (g * g.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_intgrowsq_378d_base_v109_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 378)
    result = (g * g.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_intgrowsq_504d_base_v110_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 504)
    result = (g * g.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_assetpulsezl_21d_126_base_v111_signal(assets, closeadj):
    g = _f11_asset_growth_pulse(assets, 21)
    result = _z(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_assetpulsezl_21d_252_base_v112_signal(assets, closeadj):
    g = _f11_asset_growth_pulse(assets, 21)
    result = _z(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_assetpulsezl_42d_126_base_v113_signal(assets, closeadj):
    g = _f11_asset_growth_pulse(assets, 42)
    result = _z(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_assetpulsezl_42d_252_base_v114_signal(assets, closeadj):
    g = _f11_asset_growth_pulse(assets, 42)
    result = _z(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_assetpulsezl_63d_126_base_v115_signal(assets, closeadj):
    g = _f11_asset_growth_pulse(assets, 63)
    result = _z(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_assetpulsezl_63d_252_base_v116_signal(assets, closeadj):
    g = _f11_asset_growth_pulse(assets, 63)
    result = _z(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_assetpulsezl_126d_126_base_v117_signal(assets, closeadj):
    g = _f11_asset_growth_pulse(assets, 126)
    result = _z(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_assetpulsezl_126d_252_base_v118_signal(assets, closeadj):
    g = _f11_asset_growth_pulse(assets, 126)
    result = _z(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_assetpulsezl_252d_126_base_v119_signal(assets, closeadj):
    g = _f11_asset_growth_pulse(assets, 252)
    result = _z(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_assetpulsezl_252d_252_base_v120_signal(assets, closeadj):
    g = _f11_asset_growth_pulse(assets, 252)
    result = _z(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsesum_21d_21_base_v121_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 21)
    result = g.rolling(21, min_periods=max(1, 21 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsesum_21d_63_base_v122_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 21)
    result = g.rolling(63, min_periods=max(1, 63 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsesum_42d_21_base_v123_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 42)
    result = g.rolling(21, min_periods=max(1, 21 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsesum_42d_63_base_v124_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 42)
    result = g.rolling(63, min_periods=max(1, 63 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsesum_63d_21_base_v125_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 63)
    result = g.rolling(21, min_periods=max(1, 21 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsesum_63d_63_base_v126_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 63)
    result = g.rolling(63, min_periods=max(1, 63 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsesum_126d_21_base_v127_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 126)
    result = g.rolling(21, min_periods=max(1, 21 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsesum_126d_63_base_v128_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 126)
    result = g.rolling(63, min_periods=max(1, 63 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsesum_252d_21_base_v129_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 252)
    result = g.rolling(21, min_periods=max(1, 21 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsesum_252d_63_base_v130_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 252)
    result = g.rolling(63, min_periods=max(1, 63 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_intgrowsign_5d_base_v131_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 5)
    result = np.sign(g) * closeadj + g * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_intgrowsign_10d_base_v132_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 10)
    result = np.sign(g) * closeadj + g * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_intgrowsign_21d_base_v133_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 21)
    result = np.sign(g) * closeadj + g * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_intgrowsign_42d_base_v134_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 42)
    result = np.sign(g) * closeadj + g * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_intgrowsign_63d_base_v135_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 63)
    result = np.sign(g) * closeadj + g * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_intgrowsign_126d_base_v136_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 126)
    result = np.sign(g) * closeadj + g * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_intgrowsign_189d_base_v137_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 189)
    result = np.sign(g) * closeadj + g * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_intgrowsign_252d_base_v138_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 252)
    result = np.sign(g) * closeadj + g * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_intgrowsign_378d_base_v139_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 378)
    result = np.sign(g) * closeadj + g * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_intgrowsign_504d_base_v140_signal(intangibles, closeadj):
    g = _f11_intangibles_growth(intangibles, 504)
    result = np.sign(g) * closeadj + g * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsec2_5d_base_v141_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 5)
    result = g * closeadj.pow(2.0) / 1e2
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsec2_10d_base_v142_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 10)
    result = g * closeadj.pow(2.0) / 1e2
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsec2_21d_base_v143_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 21)
    result = g * closeadj.pow(2.0) / 1e2
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsec2_42d_base_v144_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 42)
    result = g * closeadj.pow(2.0) / 1e2
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsec2_63d_base_v145_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 63)
    result = g * closeadj.pow(2.0) / 1e2
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsec2_126d_base_v146_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 126)
    result = g * closeadj.pow(2.0) / 1e2
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsec2_189d_base_v147_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 189)
    result = g * closeadj.pow(2.0) / 1e2
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsec2_252d_base_v148_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 252)
    result = g * closeadj.pow(2.0) / 1e2
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsec2_378d_base_v149_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 378)
    result = g * closeadj.pow(2.0) / 1e2
    return result.replace([np.inf, -np.inf], np.nan)


def f11sba_f11_small_bank_acquisition_signature_acqpulsec2_504d_base_v150_signal(intangibles, assets, closeadj):
    g = _f11_acquisition_pulse(intangibles, assets, 504)
    result = g * closeadj.pow(2.0) / 1e2
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f11sba_f11_small_bank_acquisition_signature_intgrowmean_63d_63_base_v076_signal,
    f11sba_f11_small_bank_acquisition_signature_intgrowmean_126d_21_base_v077_signal,
    f11sba_f11_small_bank_acquisition_signature_intgrowmean_126d_63_base_v078_signal,
    f11sba_f11_small_bank_acquisition_signature_intgrowmean_252d_21_base_v079_signal,
    f11sba_f11_small_bank_acquisition_signature_intgrowmean_252d_63_base_v080_signal,
    f11sba_f11_small_bank_acquisition_signature_assetpulsestd_21d_21_base_v081_signal,
    f11sba_f11_small_bank_acquisition_signature_assetpulsestd_21d_63_base_v082_signal,
    f11sba_f11_small_bank_acquisition_signature_assetpulsestd_42d_21_base_v083_signal,
    f11sba_f11_small_bank_acquisition_signature_assetpulsestd_42d_63_base_v084_signal,
    f11sba_f11_small_bank_acquisition_signature_assetpulsestd_63d_21_base_v085_signal,
    f11sba_f11_small_bank_acquisition_signature_assetpulsestd_63d_63_base_v086_signal,
    f11sba_f11_small_bank_acquisition_signature_assetpulsestd_126d_21_base_v087_signal,
    f11sba_f11_small_bank_acquisition_signature_assetpulsestd_126d_63_base_v088_signal,
    f11sba_f11_small_bank_acquisition_signature_assetpulsestd_252d_21_base_v089_signal,
    f11sba_f11_small_bank_acquisition_signature_assetpulsestd_252d_63_base_v090_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsez_21d_63_base_v091_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsez_21d_126_base_v092_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsez_42d_63_base_v093_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsez_42d_126_base_v094_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsez_63d_63_base_v095_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsez_63d_126_base_v096_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsez_126d_63_base_v097_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsez_126d_126_base_v098_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsez_252d_63_base_v099_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsez_252d_126_base_v100_signal,
    f11sba_f11_small_bank_acquisition_signature_intgrowsq_5d_base_v101_signal,
    f11sba_f11_small_bank_acquisition_signature_intgrowsq_10d_base_v102_signal,
    f11sba_f11_small_bank_acquisition_signature_intgrowsq_21d_base_v103_signal,
    f11sba_f11_small_bank_acquisition_signature_intgrowsq_42d_base_v104_signal,
    f11sba_f11_small_bank_acquisition_signature_intgrowsq_63d_base_v105_signal,
    f11sba_f11_small_bank_acquisition_signature_intgrowsq_126d_base_v106_signal,
    f11sba_f11_small_bank_acquisition_signature_intgrowsq_189d_base_v107_signal,
    f11sba_f11_small_bank_acquisition_signature_intgrowsq_252d_base_v108_signal,
    f11sba_f11_small_bank_acquisition_signature_intgrowsq_378d_base_v109_signal,
    f11sba_f11_small_bank_acquisition_signature_intgrowsq_504d_base_v110_signal,
    f11sba_f11_small_bank_acquisition_signature_assetpulsezl_21d_126_base_v111_signal,
    f11sba_f11_small_bank_acquisition_signature_assetpulsezl_21d_252_base_v112_signal,
    f11sba_f11_small_bank_acquisition_signature_assetpulsezl_42d_126_base_v113_signal,
    f11sba_f11_small_bank_acquisition_signature_assetpulsezl_42d_252_base_v114_signal,
    f11sba_f11_small_bank_acquisition_signature_assetpulsezl_63d_126_base_v115_signal,
    f11sba_f11_small_bank_acquisition_signature_assetpulsezl_63d_252_base_v116_signal,
    f11sba_f11_small_bank_acquisition_signature_assetpulsezl_126d_126_base_v117_signal,
    f11sba_f11_small_bank_acquisition_signature_assetpulsezl_126d_252_base_v118_signal,
    f11sba_f11_small_bank_acquisition_signature_assetpulsezl_252d_126_base_v119_signal,
    f11sba_f11_small_bank_acquisition_signature_assetpulsezl_252d_252_base_v120_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsesum_21d_21_base_v121_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsesum_21d_63_base_v122_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsesum_42d_21_base_v123_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsesum_42d_63_base_v124_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsesum_63d_21_base_v125_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsesum_63d_63_base_v126_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsesum_126d_21_base_v127_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsesum_126d_63_base_v128_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsesum_252d_21_base_v129_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsesum_252d_63_base_v130_signal,
    f11sba_f11_small_bank_acquisition_signature_intgrowsign_5d_base_v131_signal,
    f11sba_f11_small_bank_acquisition_signature_intgrowsign_10d_base_v132_signal,
    f11sba_f11_small_bank_acquisition_signature_intgrowsign_21d_base_v133_signal,
    f11sba_f11_small_bank_acquisition_signature_intgrowsign_42d_base_v134_signal,
    f11sba_f11_small_bank_acquisition_signature_intgrowsign_63d_base_v135_signal,
    f11sba_f11_small_bank_acquisition_signature_intgrowsign_126d_base_v136_signal,
    f11sba_f11_small_bank_acquisition_signature_intgrowsign_189d_base_v137_signal,
    f11sba_f11_small_bank_acquisition_signature_intgrowsign_252d_base_v138_signal,
    f11sba_f11_small_bank_acquisition_signature_intgrowsign_378d_base_v139_signal,
    f11sba_f11_small_bank_acquisition_signature_intgrowsign_504d_base_v140_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsec2_5d_base_v141_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsec2_10d_base_v142_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsec2_21d_base_v143_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsec2_42d_base_v144_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsec2_63d_base_v145_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsec2_126d_base_v146_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsec2_189d_base_v147_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsec2_252d_base_v148_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsec2_378d_base_v149_signal,
    f11sba_f11_small_bank_acquisition_signature_acqpulsec2_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F11_SMALL_BANK_ACQUISITION_SIGNATURE_REGISTRY_076_150 = REGISTRY


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
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f11_intangibles_growth", "_f11_asset_growth_pulse", "_f11_acquisition_pulse")
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
    print(f"OK small_bank_acquisition_signature_base_076_150_claude: {n_features} features pass")
