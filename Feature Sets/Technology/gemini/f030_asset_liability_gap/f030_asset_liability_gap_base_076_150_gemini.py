import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f030_asset_liability_gap_core75_pct_4q_v076_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_pct_change(_safe_div(assets - liabilities, marketcap), 4))
def cg_f030_asset_liability_gap_core76_pct_4q_v077_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_pct_change(_safe_div(_diff(assets - liabilities, 4), netinc.abs() + 1.0), 4))
def cg_f030_asset_liability_gap_core77_pct_4q_v078_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_pct_change(_safe_div(assets - liabilities, sharesbas), 4))
def cg_f030_asset_liability_gap_core78_pct_4q_v079_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_pct_change(_safe_div(debtt - cashneq, (assets - liabilities).abs() + 1.0), 4))
def cg_f030_asset_liability_gap_core79_pct_4q_v080_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_pct_change(_log((assets - liabilities).clip(lower=1.0)), 4))

# Block 80-89: std 8q
def cg_f030_asset_liability_gap_core80_std_8q_v081_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_std(_safe_div(assets - liabilities, assets), 8))
def cg_f030_asset_liability_gap_core81_std_8q_v082_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_std(_safe_div(assetsc, liabc.abs() + 1.0), 8))
def cg_f030_asset_liability_gap_core82_std_8q_v083_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_std(_safe_div(cashneq + receivables, liabc.abs() + 1.0), 8))
def cg_f030_asset_liability_gap_core83_std_8q_v084_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_std(_safe_div(liabilities, assets), 8))
def cg_f030_asset_liability_gap_core84_std_8q_v085_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_std(_safe_div(assetsc - liabc, assets), 8))
def cg_f030_asset_liability_gap_core85_std_8q_v086_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_std(_safe_div(assets - liabilities, marketcap), 8))
def cg_f030_asset_liability_gap_core86_std_8q_v087_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_std(_safe_div(assets - liabilities, sharesbas), 8))
def cg_f030_asset_liability_gap_core87_std_8q_v088_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_std(_safe_div(debtt - cashneq, (assets - liabilities).abs() + 1.0), 8))
def cg_f030_asset_liability_gap_core88_std_8q_v089_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_std(assets - liabilities, 8))
def cg_f030_asset_liability_gap_core89_std_8q_v090_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_std(_log((assets - liabilities).clip(lower=1.0)), 8))

# Block 90-99: log
def cg_f030_asset_liability_gap_core90_log_v091_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_log((assets - liabilities).clip(lower=1.0)))
def cg_f030_asset_liability_gap_core91_log_v092_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_log(_safe_div(assets - liabilities, assets).abs().clip(lower=0.01)))
def cg_f030_asset_liability_gap_core92_log_v093_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_log(_safe_div(assetsc, liabc.abs() + 1.0).clip(lower=0.01)))
def cg_f030_asset_liability_gap_core93_log_v094_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_log(_safe_div(liabilities, assets).clip(lower=0.01)))
def cg_f030_asset_liability_gap_core94_log_v095_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_log(_safe_div(assets - liabilities, marketcap).abs().clip(lower=0.001)))
def cg_f030_asset_liability_gap_core95_log_v096_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_log(_safe_div(assets - liabilities, sharesbas).abs().clip(lower=0.01)))
def cg_f030_asset_liability_gap_core96_log_v097_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_log(_safe_div(debtt - cashneq, (assets - liabilities).abs() + 1.0).abs().clip(lower=0.01)))
def cg_f030_asset_liability_gap_core97_log_v098_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_log(_safe_div(assetsc - liabc, assets).abs().clip(lower=0.001)))
def cg_f030_asset_liability_gap_core98_log_v099_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_log(_safe_div(cashneq + receivables, liabc.abs() + 1.0).clip(lower=0.01)))
def cg_f030_asset_liability_gap_core99_log_v100_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_log(assets.clip(lower=1.0)))

# Block 100-109: diff 1q
def cg_f030_asset_liability_gap_core100_diff_1q_v101_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_diff(_safe_div(assets - liabilities, assets), 1))
def cg_f030_asset_liability_gap_core101_diff_1q_v102_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_diff(_safe_div(assetsc, liabc.abs() + 1.0), 1))
def cg_f030_asset_liability_gap_core102_diff_1q_v103_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_diff(_safe_div(liabilities, assets), 1))
def cg_f030_asset_liability_gap_core103_diff_1q_v104_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_diff(_safe_div(assets - liabilities, marketcap), 1))
def cg_f030_asset_liability_gap_core104_diff_1q_v105_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_diff(_safe_div(assets - liabilities, sharesbas), 1))
def cg_f030_asset_liability_gap_core105_diff_1q_v106_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_diff(_safe_div(debtt - cashneq, (assets - liabilities).abs() + 1.0), 1))
def cg_f030_asset_liability_gap_core106_diff_1q_v107_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_diff(_safe_div(assetsc - liabc, assets), 1))
def cg_f030_asset_liability_gap_core107_diff_1q_v108_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_diff(assets - liabilities, 1))
def cg_f030_asset_liability_gap_core108_diff_1q_v109_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_diff(_log((assets - liabilities).clip(lower=1.0)), 1))
def cg_f030_asset_liability_gap_core109_diff_1q_v110_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_diff(_safe_div(cashneq + receivables, liabc.abs() + 1.0), 1))

# Block 110-119: slope 4q
def cg_f030_asset_liability_gap_core110_slope_4q_v111_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_slope(_safe_div(assets - liabilities, assets), 4))
def cg_f030_asset_liability_gap_core111_slope_4q_v112_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_slope(_safe_div(assetsc, liabc.abs() + 1.0), 4))
def cg_f030_asset_liability_gap_core112_slope_4q_v113_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_slope(_safe_div(liabilities, assets), 4))
def cg_f030_asset_liability_gap_core113_slope_4q_v114_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_slope(_safe_div(assets - liabilities, marketcap), 4))
def cg_f030_asset_liability_gap_core114_slope_4q_v115_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_slope(_safe_div(assets - liabilities, sharesbas), 4))
def cg_f030_asset_liability_gap_core115_slope_4q_v116_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_slope(_safe_div(debtt - cashneq, (assets - liabilities).abs() + 1.0), 4))
def cg_f030_asset_liability_gap_core116_slope_4q_v117_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_slope(_safe_div(assetsc - liabc, assets), 4))
def cg_f030_asset_liability_gap_core117_slope_4q_v118_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_slope(assets - liabilities, 4))
def cg_f030_asset_liability_gap_core118_slope_4q_v119_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_slope(_log((assets - liabilities).clip(lower=1.0)), 4))
def cg_f030_asset_liability_gap_core119_slope_4q_v120_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_slope(_safe_div(cashneq + receivables, liabc.abs() + 1.0), 4))

# Block 120-129: ewm 8q
def cg_f030_asset_liability_gap_core120_ewm_8q_v121_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_ewm(_safe_div(assets - liabilities, assets), 8))
def cg_f030_asset_liability_gap_core121_ewm_8q_v122_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_ewm(_safe_div(assetsc, liabc.abs() + 1.0), 8))
def cg_f030_asset_liability_gap_core122_ewm_8q_v123_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_ewm(_safe_div(liabilities, assets), 8))
def cg_f030_asset_liability_gap_core123_ewm_8q_v124_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_ewm(_safe_div(assets - liabilities, marketcap), 8))
def cg_f030_asset_liability_gap_core124_ewm_8q_v125_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_ewm(_safe_div(assets - liabilities, sharesbas), 8))
def cg_f030_asset_liability_gap_core125_ewm_8q_v126_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_ewm(_safe_div(debtt - cashneq, (assets - liabilities).abs() + 1.0), 8))
def cg_f030_asset_liability_gap_core126_ewm_8q_v127_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_ewm(_safe_div(assetsc - liabc, assets), 8))
def cg_f030_asset_liability_gap_core127_ewm_8q_v128_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_ewm(assets - liabilities, 8))
def cg_f030_asset_liability_gap_core128_ewm_8q_v129_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_ewm(_log((assets - liabilities).clip(lower=1.0)), 8))
def cg_f030_asset_liability_gap_core129_ewm_8q_v130_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_ewm(_safe_div(cashneq + receivables, liabc.abs() + 1.0), 8))

# Block 130-139: stability 12q
def cg_f030_asset_liability_gap_core130_stability_12q_v131_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    base = _safe_div(assets - liabilities, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f030_asset_liability_gap_core131_stability_12q_v132_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    base = _safe_div(assetsc, liabc.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f030_asset_liability_gap_core132_stability_12q_v133_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    base = _safe_div(liabilities, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f030_asset_liability_gap_core133_stability_12q_v134_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    base = _safe_div(assets - liabilities, marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f030_asset_liability_gap_core134_stability_12q_v135_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    base = _safe_div(assets - liabilities, sharesbas)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f030_asset_liability_gap_core135_stability_12q_v136_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    base = _safe_div(debtt - cashneq, (assets - liabilities).abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f030_asset_liability_gap_core136_stability_12q_v137_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    base = _safe_div(assetsc - liabc, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f030_asset_liability_gap_core137_stability_12q_v138_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    base = assets - liabilities
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f030_asset_liability_gap_core138_stability_12q_v139_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    base = _log((assets - liabilities).clip(lower=1.0))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f030_asset_liability_gap_core139_stability_12q_v140_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    base = _safe_div(cashneq + receivables, liabc.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f030_asset_liability_gap_core140_gap_v141_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(assets - liabilities)
def cg_f030_asset_liability_gap_core141_equity_ratio_v142_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_safe_div(assets - liabilities, assets))
def cg_f030_asset_liability_gap_core142_current_ratio_v143_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_safe_div(assetsc, liabc.abs() + 1.0))
def cg_f030_asset_liability_gap_core143_quick_ratio_v144_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_safe_div(cashneq + receivables, liabc.abs() + 1.0))
def cg_f030_asset_liability_gap_core144_liab_assets_v145_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_safe_div(liabilities, assets))
def cg_f030_asset_liability_gap_core145_wc_assets_v146_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_safe_div(assetsc - liabc, assets))
def cg_f030_asset_liability_gap_core146_gap_mcap_v147_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_safe_div(assets - liabilities, marketcap))
def cg_f030_asset_liability_gap_core147_gap_shares_v148_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_safe_div(assets - liabilities, sharesbas))
def cg_f030_asset_liability_gap_core148_nd_gap_v149_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_safe_div(debtt - cashneq, (assets - liabilities).abs() + 1.0))
def cg_f030_asset_liability_gap_core149_gap_log_v150_signal(assets, liabilities, assetsc, liabc, cashneq, receivables, marketcap, netinc, sharesbas, debtt):
    return _clean(_log((assets - liabilities).clip(lower=1.0)))
