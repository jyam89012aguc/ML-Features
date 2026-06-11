import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 acceleration mean 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core00_mean_5d_accel_v001_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_officer_buy_value-insider_officer_sell_value
    base = _mean(series,5)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core01 acceleration mean 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core01_mean_21d_accel_v002_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -insider_tenpct_sell_value
    base = _mean(series,21)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core02 acceleration mean 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core02_mean_63d_accel_v003_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -ten_pct_holder_sell_value
    base = _mean(series,63)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core03 acceleration mean 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core03_mean_126d_accel_v004_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_holdings_post_pct
    base = _mean(series,126)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core04 acceleration mean 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core04_mean_252d_accel_v005_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63), _std(insider_total_shares_owned,252).abs()+1e-9)
    base = _mean(series,252)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core05 acceleration mean 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core05_mean_5d_accel_v006_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63),sharesbas.abs()+1e-9)
    base = _mean(series,5)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core06 acceleration mean 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core06_mean_21d_accel_v007_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,(sharesbas*closeadj).abs()+1e-9)
    base = _mean(series,21)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core07 acceleration mean 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core07_mean_63d_accel_v008_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _corr(insider_holdings_post_pct,_pct_change(closeadj,21),252)
    base = _mean(series,63)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core08 acceleration mean 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core08_mean_126d_accel_v009_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_holdings_post_pct,63),_std(insider_holdings_post_pct,252).abs()+1e-9)
    base = _mean(series,126)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core09 acceleration mean 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core09_mean_252d_accel_v010_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,insider_tenpct_sell_value.abs()+1e-9)
    base = _mean(series,252)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core00 acceleration z 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core00_z_21d_accel_v011_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_officer_buy_value-insider_officer_sell_value
    base = _z(series,21)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core01 acceleration z 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core01_z_63d_accel_v012_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -insider_tenpct_sell_value
    base = _z(series,63)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core02 acceleration z 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core02_z_126d_accel_v013_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -ten_pct_holder_sell_value
    base = _z(series,126)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core03 acceleration z 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core03_z_252d_accel_v014_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_holdings_post_pct
    base = _z(series,252)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core04 acceleration z 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core04_z_5d_accel_v015_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63), _std(insider_total_shares_owned,252).abs()+1e-9)
    base = _z(series,5)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core05 acceleration z 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core05_z_21d_accel_v016_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63),sharesbas.abs()+1e-9)
    base = _z(series,21)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core06 acceleration z 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core06_z_63d_accel_v017_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,(sharesbas*closeadj).abs()+1e-9)
    base = _z(series,63)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core07 acceleration z 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core07_z_126d_accel_v018_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _corr(insider_holdings_post_pct,_pct_change(closeadj,21),252)
    base = _z(series,126)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core08 acceleration z 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core08_z_252d_accel_v019_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_holdings_post_pct,63),_std(insider_holdings_post_pct,252).abs()+1e-9)
    base = _z(series,252)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core09 acceleration z 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core09_z_5d_accel_v020_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,insider_tenpct_sell_value.abs()+1e-9)
    base = _z(series,5)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core00 acceleration rank 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core00_rank_63d_accel_v021_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_officer_buy_value-insider_officer_sell_value
    base = _rank(series,63)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core01 acceleration rank 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core01_rank_126d_accel_v022_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -insider_tenpct_sell_value
    base = _rank(series,126)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core02 acceleration rank 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core02_rank_252d_accel_v023_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -ten_pct_holder_sell_value
    base = _rank(series,252)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core03 acceleration rank 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core03_rank_5d_accel_v024_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_holdings_post_pct
    base = _rank(series,5)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core04 acceleration rank 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core04_rank_21d_accel_v025_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63), _std(insider_total_shares_owned,252).abs()+1e-9)
    base = _rank(series,21)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core05 acceleration rank 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core05_rank_63d_accel_v026_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63),sharesbas.abs()+1e-9)
    base = _rank(series,63)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core06 acceleration rank 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core06_rank_126d_accel_v027_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,(sharesbas*closeadj).abs()+1e-9)
    base = _rank(series,126)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core07 acceleration rank 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core07_rank_252d_accel_v028_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _corr(insider_holdings_post_pct,_pct_change(closeadj,21),252)
    base = _rank(series,252)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core08 acceleration rank 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core08_rank_5d_accel_v029_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_holdings_post_pct,63),_std(insider_holdings_post_pct,252).abs()+1e-9)
    base = _rank(series,5)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core09 acceleration rank 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core09_rank_21d_accel_v030_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,insider_tenpct_sell_value.abs()+1e-9)
    base = _rank(series,21)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core00 acceleration std 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core00_std_126d_accel_v031_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_officer_buy_value-insider_officer_sell_value
    base = _std(series,126)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core01 acceleration std 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core01_std_252d_accel_v032_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -insider_tenpct_sell_value
    base = _std(series,252)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core02 acceleration std 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core02_std_5d_accel_v033_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -ten_pct_holder_sell_value
    base = _std(series,5)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core03 acceleration std 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core03_std_21d_accel_v034_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_holdings_post_pct
    base = _std(series,21)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core04 acceleration std 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core04_std_63d_accel_v035_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63), _std(insider_total_shares_owned,252).abs()+1e-9)
    base = _std(series,63)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core05 acceleration std 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core05_std_126d_accel_v036_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63),sharesbas.abs()+1e-9)
    base = _std(series,126)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core06 acceleration std 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core06_std_252d_accel_v037_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,(sharesbas*closeadj).abs()+1e-9)
    base = _std(series,252)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core07 acceleration std 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core07_std_5d_accel_v038_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _corr(insider_holdings_post_pct,_pct_change(closeadj,21),252)
    base = _std(series,5)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core08 acceleration std 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core08_std_21d_accel_v039_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_holdings_post_pct,63),_std(insider_holdings_post_pct,252).abs()+1e-9)
    base = _std(series,21)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core09 acceleration std 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core09_std_63d_accel_v040_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,insider_tenpct_sell_value.abs()+1e-9)
    base = _std(series,63)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core00 acceleration delta 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core00_delta_252d_accel_v041_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_officer_buy_value-insider_officer_sell_value
    base = _diff(series,252)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core01 acceleration delta 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core01_delta_5d_accel_v042_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -insider_tenpct_sell_value
    base = _diff(series,5)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core02 acceleration delta 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core02_delta_21d_accel_v043_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -ten_pct_holder_sell_value
    base = _diff(series,21)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core03 acceleration delta 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core03_delta_63d_accel_v044_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_holdings_post_pct
    base = _diff(series,63)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core04 acceleration delta 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core04_delta_126d_accel_v045_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63), _std(insider_total_shares_owned,252).abs()+1e-9)
    base = _diff(series,126)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core05 acceleration delta 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core05_delta_252d_accel_v046_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63),sharesbas.abs()+1e-9)
    base = _diff(series,252)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core06 acceleration delta 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core06_delta_5d_accel_v047_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,(sharesbas*closeadj).abs()+1e-9)
    base = _diff(series,5)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core07 acceleration delta 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core07_delta_21d_accel_v048_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _corr(insider_holdings_post_pct,_pct_change(closeadj,21),252)
    base = _diff(series,21)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core08 acceleration delta 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core08_delta_63d_accel_v049_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_holdings_post_pct,63),_std(insider_holdings_post_pct,252).abs()+1e-9)
    base = _diff(series,63)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core09 acceleration delta 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core09_delta_126d_accel_v050_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,insider_tenpct_sell_value.abs()+1e-9)
    base = _diff(series,126)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core00 acceleration pct 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core00_pct_5d_accel_v051_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_officer_buy_value-insider_officer_sell_value
    base = _pct_change(series,5)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core01 acceleration pct 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core01_pct_21d_accel_v052_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -insider_tenpct_sell_value
    base = _pct_change(series,21)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core02 acceleration pct 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core02_pct_63d_accel_v053_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -ten_pct_holder_sell_value
    base = _pct_change(series,63)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core03 acceleration pct 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core03_pct_126d_accel_v054_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_holdings_post_pct
    base = _pct_change(series,126)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core04 acceleration pct 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core04_pct_252d_accel_v055_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63), _std(insider_total_shares_owned,252).abs()+1e-9)
    base = _pct_change(series,252)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core05 acceleration pct 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core05_pct_5d_accel_v056_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63),sharesbas.abs()+1e-9)
    base = _pct_change(series,5)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core06 acceleration pct 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core06_pct_21d_accel_v057_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,(sharesbas*closeadj).abs()+1e-9)
    base = _pct_change(series,21)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core07 acceleration pct 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core07_pct_63d_accel_v058_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _corr(insider_holdings_post_pct,_pct_change(closeadj,21),252)
    base = _pct_change(series,63)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core08 acceleration pct 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core08_pct_126d_accel_v059_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_holdings_post_pct,63),_std(insider_holdings_post_pct,252).abs()+1e-9)
    base = _pct_change(series,126)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core09 acceleration pct 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core09_pct_252d_accel_v060_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,insider_tenpct_sell_value.abs()+1e-9)
    base = _pct_change(series,252)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core00 acceleration ewm 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core00_ewm_21d_accel_v061_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_officer_buy_value-insider_officer_sell_value
    base = _ewm(series,21)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core01 acceleration ewm 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core01_ewm_63d_accel_v062_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -insider_tenpct_sell_value
    base = _ewm(series,63)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core02 acceleration ewm 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core02_ewm_126d_accel_v063_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -ten_pct_holder_sell_value
    base = _ewm(series,126)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core03 acceleration ewm 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core03_ewm_252d_accel_v064_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_holdings_post_pct
    base = _ewm(series,252)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core04 acceleration ewm 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core04_ewm_5d_accel_v065_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63), _std(insider_total_shares_owned,252).abs()+1e-9)
    base = _ewm(series,5)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core05 acceleration ewm 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core05_ewm_21d_accel_v066_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63),sharesbas.abs()+1e-9)
    base = _ewm(series,21)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core06 acceleration ewm 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core06_ewm_63d_accel_v067_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,(sharesbas*closeadj).abs()+1e-9)
    base = _ewm(series,63)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core07 acceleration ewm 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core07_ewm_126d_accel_v068_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _corr(insider_holdings_post_pct,_pct_change(closeadj,21),252)
    base = _ewm(series,126)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core08 acceleration ewm 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core08_ewm_252d_accel_v069_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_holdings_post_pct,63),_std(insider_holdings_post_pct,252).abs()+1e-9)
    base = _ewm(series,252)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core09 acceleration ewm 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core09_ewm_5d_accel_v070_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,insider_tenpct_sell_value.abs()+1e-9)
    base = _ewm(series,5)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core00 acceleration slope 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core00_slope_63d_accel_v071_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_officer_buy_value-insider_officer_sell_value
    base = _slope(series,63)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core01 acceleration slope 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core01_slope_126d_accel_v072_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -insider_tenpct_sell_value
    base = _slope(series,126)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core02 acceleration slope 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core02_slope_252d_accel_v073_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -ten_pct_holder_sell_value
    base = _slope(series,252)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core03 acceleration slope 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core03_slope_5d_accel_v074_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_holdings_post_pct
    base = _slope(series,5)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core04 acceleration slope 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core04_slope_21d_accel_v075_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63), _std(insider_total_shares_owned,252).abs()+1e-9)
    base = _slope(series,21)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core05 acceleration slope 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core05_slope_63d_accel_v076_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63),sharesbas.abs()+1e-9)
    base = _slope(series,63)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core06 acceleration slope 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core06_slope_126d_accel_v077_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,(sharesbas*closeadj).abs()+1e-9)
    base = _slope(series,126)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core07 acceleration slope 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core07_slope_252d_accel_v078_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _corr(insider_holdings_post_pct,_pct_change(closeadj,21),252)
    base = _slope(series,252)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core08 acceleration slope 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core08_slope_5d_accel_v079_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_holdings_post_pct,63),_std(insider_holdings_post_pct,252).abs()+1e-9)
    base = _slope(series,5)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core09 acceleration slope 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core09_slope_21d_accel_v080_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,insider_tenpct_sell_value.abs()+1e-9)
    base = _slope(series,21)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core00 acceleration abs_mean 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core00_abs_mean_126d_accel_v081_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_officer_buy_value-insider_officer_sell_value
    base = _mean(series.abs(),126)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core01 acceleration abs_mean 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core01_abs_mean_252d_accel_v082_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -insider_tenpct_sell_value
    base = _mean(series.abs(),252)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core02 acceleration abs_mean 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core02_abs_mean_5d_accel_v083_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -ten_pct_holder_sell_value
    base = _mean(series.abs(),5)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core03 acceleration abs_mean 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core03_abs_mean_21d_accel_v084_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_holdings_post_pct
    base = _mean(series.abs(),21)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core04 acceleration abs_mean 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core04_abs_mean_63d_accel_v085_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63), _std(insider_total_shares_owned,252).abs()+1e-9)
    base = _mean(series.abs(),63)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core05 acceleration abs_mean 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core05_abs_mean_126d_accel_v086_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63),sharesbas.abs()+1e-9)
    base = _mean(series.abs(),126)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core06 acceleration abs_mean 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core06_abs_mean_252d_accel_v087_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,(sharesbas*closeadj).abs()+1e-9)
    base = _mean(series.abs(),252)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core07 acceleration abs_mean 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core07_abs_mean_5d_accel_v088_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _corr(insider_holdings_post_pct,_pct_change(closeadj,21),252)
    base = _mean(series.abs(),5)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core08 acceleration abs_mean 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core08_abs_mean_21d_accel_v089_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_holdings_post_pct,63),_std(insider_holdings_post_pct,252).abs()+1e-9)
    base = _mean(series.abs(),21)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core09 acceleration abs_mean 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core09_abs_mean_63d_accel_v090_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,insider_tenpct_sell_value.abs()+1e-9)
    base = _mean(series.abs(),63)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core00 acceleration pos_mag 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core00_pos_mag_252d_accel_v091_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_officer_buy_value-insider_officer_sell_value
    base = _mean(series.where(series>0,0),252)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core01 acceleration pos_mag 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core01_pos_mag_5d_accel_v092_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -insider_tenpct_sell_value
    base = _mean(series.where(series>0,0),5)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core02 acceleration pos_mag 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core02_pos_mag_21d_accel_v093_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -ten_pct_holder_sell_value
    base = _mean(series.where(series>0,0),21)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core03 acceleration pos_mag 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core03_pos_mag_63d_accel_v094_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_holdings_post_pct
    base = _mean(series.where(series>0,0),63)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core04 acceleration pos_mag 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core04_pos_mag_126d_accel_v095_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63), _std(insider_total_shares_owned,252).abs()+1e-9)
    base = _mean(series.where(series>0,0),126)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core05 acceleration pos_mag 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core05_pos_mag_252d_accel_v096_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63),sharesbas.abs()+1e-9)
    base = _mean(series.where(series>0,0),252)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core06 acceleration pos_mag 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core06_pos_mag_5d_accel_v097_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,(sharesbas*closeadj).abs()+1e-9)
    base = _mean(series.where(series>0,0),5)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core07 acceleration pos_mag 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core07_pos_mag_21d_accel_v098_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _corr(insider_holdings_post_pct,_pct_change(closeadj,21),252)
    base = _mean(series.where(series>0,0),21)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core08 acceleration pos_mag 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core08_pos_mag_63d_accel_v099_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_holdings_post_pct,63),_std(insider_holdings_post_pct,252).abs()+1e-9)
    base = _mean(series.where(series>0,0),63)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core09 acceleration pos_mag 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core09_pos_mag_126d_accel_v100_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,insider_tenpct_sell_value.abs()+1e-9)
    base = _mean(series.where(series>0,0),126)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core00 acceleration neg_mag2 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core00_neg_mag2_5d_accel_v101_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_officer_buy_value-insider_officer_sell_value
    base = _mean((series.where(series<0,0).abs() ** 2),5)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core01 acceleration neg_mag2 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core01_neg_mag2_21d_accel_v102_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -insider_tenpct_sell_value
    base = _mean((series.where(series<0,0).abs() ** 2),21)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core02 acceleration neg_mag2 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core02_neg_mag2_63d_accel_v103_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -ten_pct_holder_sell_value
    base = _mean((series.where(series<0,0).abs() ** 2),63)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core03 acceleration neg_mag2 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core03_neg_mag2_126d_accel_v104_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_holdings_post_pct
    base = _mean((series.where(series<0,0).abs() ** 2),126)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core04 acceleration neg_mag2 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core04_neg_mag2_252d_accel_v105_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63), _std(insider_total_shares_owned,252).abs()+1e-9)
    base = _mean((series.where(series<0,0).abs() ** 2),252)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core05 acceleration neg_mag2 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core05_neg_mag2_5d_accel_v106_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63),sharesbas.abs()+1e-9)
    base = _mean((series.where(series<0,0).abs() ** 2),5)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core06 acceleration neg_mag2 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core06_neg_mag2_21d_accel_v107_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,(sharesbas*closeadj).abs()+1e-9)
    base = _mean((series.where(series<0,0).abs() ** 2),21)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core07 acceleration neg_mag2 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core07_neg_mag2_63d_accel_v108_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _corr(insider_holdings_post_pct,_pct_change(closeadj,21),252)
    base = _mean((series.where(series<0,0).abs() ** 2),63)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core08 acceleration neg_mag2 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core08_neg_mag2_126d_accel_v109_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_holdings_post_pct,63),_std(insider_holdings_post_pct,252).abs()+1e-9)
    base = _mean((series.where(series<0,0).abs() ** 2),126)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core09 acceleration neg_mag2 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core09_neg_mag2_252d_accel_v110_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,insider_tenpct_sell_value.abs()+1e-9)
    base = _mean((series.where(series<0,0).abs() ** 2),252)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core00 acceleration vol_ratio 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core00_vol_ratio_21d_accel_v111_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_officer_buy_value-insider_officer_sell_value
    base = _safe_div(_std(series,21), _mean(series.abs(),21)+1e-9)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core01 acceleration vol_ratio 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core01_vol_ratio_63d_accel_v112_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -insider_tenpct_sell_value
    base = _safe_div(_std(series,63), _mean(series.abs(),63)+1e-9)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core02 acceleration vol_ratio 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core02_vol_ratio_126d_accel_v113_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -ten_pct_holder_sell_value
    base = _safe_div(_std(series,126), _mean(series.abs(),126)+1e-9)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core03 acceleration vol_ratio 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core03_vol_ratio_252d_accel_v114_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_holdings_post_pct
    base = _safe_div(_std(series,252), _mean(series.abs(),252)+1e-9)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core04 acceleration vol_ratio 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core04_vol_ratio_5d_accel_v115_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63), _std(insider_total_shares_owned,252).abs()+1e-9)
    base = _safe_div(_std(series,5), _mean(series.abs(),5)+1e-9)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core05 acceleration vol_ratio 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core05_vol_ratio_21d_accel_v116_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63),sharesbas.abs()+1e-9)
    base = _safe_div(_std(series,21), _mean(series.abs(),21)+1e-9)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core06 acceleration vol_ratio 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core06_vol_ratio_63d_accel_v117_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,(sharesbas*closeadj).abs()+1e-9)
    base = _safe_div(_std(series,63), _mean(series.abs(),63)+1e-9)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core07 acceleration vol_ratio 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core07_vol_ratio_126d_accel_v118_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _corr(insider_holdings_post_pct,_pct_change(closeadj,21),252)
    base = _safe_div(_std(series,126), _mean(series.abs(),126)+1e-9)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core08 acceleration vol_ratio 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core08_vol_ratio_252d_accel_v119_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_holdings_post_pct,63),_std(insider_holdings_post_pct,252).abs()+1e-9)
    base = _safe_div(_std(series,252), _mean(series.abs(),252)+1e-9)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core09 acceleration vol_ratio 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core09_vol_ratio_5d_accel_v120_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,insider_tenpct_sell_value.abs()+1e-9)
    base = _safe_div(_std(series,5), _mean(series.abs(),5)+1e-9)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core00 acceleration recent_vs_long 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core00_recent_vs_long_63d_accel_v121_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_officer_buy_value-insider_officer_sell_value
    base = _safe_div(_mean(series,63), _mean(series,126)+1e-9)-1.0
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core01 acceleration recent_vs_long 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core01_recent_vs_long_126d_accel_v122_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -insider_tenpct_sell_value
    base = _safe_div(_mean(series,126), _mean(series,252)+1e-9)-1.0
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core02 acceleration recent_vs_long 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core02_recent_vs_long_252d_accel_v123_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -ten_pct_holder_sell_value
    base = _safe_div(_mean(series,252), _mean(series,504)+1e-9)-1.0
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core03 acceleration recent_vs_long 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core03_recent_vs_long_5d_accel_v124_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_holdings_post_pct
    base = _safe_div(_mean(series,5), _mean(series,10)+1e-9)-1.0
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core04 acceleration recent_vs_long 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core04_recent_vs_long_21d_accel_v125_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63), _std(insider_total_shares_owned,252).abs()+1e-9)
    base = _safe_div(_mean(series,21), _mean(series,42)+1e-9)-1.0
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core05 acceleration recent_vs_long 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core05_recent_vs_long_63d_accel_v126_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63),sharesbas.abs()+1e-9)
    base = _safe_div(_mean(series,63), _mean(series,126)+1e-9)-1.0
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core06 acceleration recent_vs_long 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core06_recent_vs_long_126d_accel_v127_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,(sharesbas*closeadj).abs()+1e-9)
    base = _safe_div(_mean(series,126), _mean(series,252)+1e-9)-1.0
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core07 acceleration recent_vs_long 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core07_recent_vs_long_252d_accel_v128_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _corr(insider_holdings_post_pct,_pct_change(closeadj,21),252)
    base = _safe_div(_mean(series,252), _mean(series,504)+1e-9)-1.0
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core08 acceleration recent_vs_long 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core08_recent_vs_long_5d_accel_v129_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_holdings_post_pct,63),_std(insider_holdings_post_pct,252).abs()+1e-9)
    base = _safe_div(_mean(series,5), _mean(series,10)+1e-9)-1.0
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core09 acceleration recent_vs_long 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core09_recent_vs_long_21d_accel_v130_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,insider_tenpct_sell_value.abs()+1e-9)
    base = _safe_div(_mean(series,21), _mean(series,42)+1e-9)-1.0
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core00 acceleration accel 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core00_accel_126d_accel_v131_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_officer_buy_value-insider_officer_sell_value
    base = _diff(_diff(series,42),42)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core01 acceleration accel 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core01_accel_252d_accel_v132_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -insider_tenpct_sell_value
    base = _diff(_diff(series,84),84)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core02 acceleration accel 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core02_accel_5d_accel_v133_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -ten_pct_holder_sell_value
    base = _diff(_diff(series,1),1)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core03 acceleration accel 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core03_accel_21d_accel_v134_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_holdings_post_pct
    base = _diff(_diff(series,7),7)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core04 acceleration accel 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core04_accel_63d_accel_v135_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63), _std(insider_total_shares_owned,252).abs()+1e-9)
    base = _diff(_diff(series,21),21)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core05 acceleration accel 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core05_accel_126d_accel_v136_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63),sharesbas.abs()+1e-9)
    base = _diff(_diff(series,42),42)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core06 acceleration accel 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core06_accel_252d_accel_v137_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,(sharesbas*closeadj).abs()+1e-9)
    base = _diff(_diff(series,84),84)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core07 acceleration accel 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core07_accel_5d_accel_v138_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _corr(insider_holdings_post_pct,_pct_change(closeadj,21),252)
    base = _diff(_diff(series,1),1)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core08 acceleration accel 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core08_accel_21d_accel_v139_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_holdings_post_pct,63),_std(insider_holdings_post_pct,252).abs()+1e-9)
    base = _diff(_diff(series,7),7)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core09 acceleration accel 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core09_accel_63d_accel_v140_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,insider_tenpct_sell_value.abs()+1e-9)
    base = _diff(_diff(series,21),21)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core00 acceleration centered_range 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core00_centered_range_252d_accel_v141_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_officer_buy_value-insider_officer_sell_value
    base = _safe_div(series-_mean(series,252), (_max(series,252)-_min(series,252)).abs()+1e-9)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core01 acceleration centered_range 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core01_centered_range_5d_accel_v142_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -insider_tenpct_sell_value
    base = _safe_div(series-_mean(series,5), (_max(series,5)-_min(series,5)).abs()+1e-9)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core02 acceleration centered_range 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core02_centered_range_21d_accel_v143_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = -ten_pct_holder_sell_value
    base = _safe_div(series-_mean(series,21), (_max(series,21)-_min(series,21)).abs()+1e-9)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core03 acceleration centered_range 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core03_centered_range_63d_accel_v144_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = insider_holdings_post_pct
    base = _safe_div(series-_mean(series,63), (_max(series,63)-_min(series,63)).abs()+1e-9)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core04 acceleration centered_range 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core04_centered_range_126d_accel_v145_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63), _std(insider_total_shares_owned,252).abs()+1e-9)
    base = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core05 acceleration centered_range 252d
def cg_f63_technology_f63_founder_and_operator_conviction_core05_centered_range_252d_accel_v146_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_total_shares_owned,63),sharesbas.abs()+1e-9)
    base = _safe_div(series-_mean(series,252), (_max(series,252)-_min(series,252)).abs()+1e-9)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core06 acceleration centered_range 5d
def cg_f63_technology_f63_founder_and_operator_conviction_core06_centered_range_5d_accel_v147_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,(sharesbas*closeadj).abs()+1e-9)
    base = _safe_div(series-_mean(series,5), (_max(series,5)-_min(series,5)).abs()+1e-9)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

# core07 acceleration centered_range 21d
def cg_f63_technology_f63_founder_and_operator_conviction_core07_centered_range_21d_accel_v148_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _corr(insider_holdings_post_pct,_pct_change(closeadj,21),252)
    base = _safe_div(series-_mean(series,21), (_max(series,21)-_min(series,21)).abs()+1e-9)
    result = _safe_div(_diff(_diff(base,63),5), _std(_diff(base,63),5).abs()+1e-9)
    return _clean(result)

# core08 acceleration centered_range 63d
def cg_f63_technology_f63_founder_and_operator_conviction_core08_centered_range_63d_accel_v149_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(_diff(insider_holdings_post_pct,63),_std(insider_holdings_post_pct,252).abs()+1e-9)
    base = _safe_div(series-_mean(series,63), (_max(series,63)-_min(series,63)).abs()+1e-9)
    result = _safe_div(_diff(_diff(base,21),63), _std(_diff(base,21),63).abs()+1e-9)
    return _clean(result)

# core09 acceleration centered_range 126d
def cg_f63_technology_f63_founder_and_operator_conviction_core09_centered_range_126d_accel_v150_signal(insider_officer_buy_value, insider_officer_sell_value, insider_tenpct_sell_value, ten_pct_holder_sell_value, insider_total_shares_owned, insider_holdings_post_pct, sharesbas, closeadj):
    series = _safe_div(insider_officer_buy_value,insider_tenpct_sell_value.abs()+1e-9)
    base = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    result = _safe_div(_diff(_diff(base,5),21), _std(_diff(base,5),21).abs()+1e-9)
    return _clean(result)

