import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _align_quarterly_to_daily(x, close):
    """Forward-fill sparse Sharadar quarterly/event data to close.index."""
    return _s(x).reindex(_s(close).index).ffill()


def _safe_div(a, b):
    b = _s(b).replace(0, np.nan)
    if np.isscalar(a):
        return a / b
    return _s(a) / b


def _roc(x, periods=1):
    return _s(x).pct_change(periods)


def _z(x, window):
    x = _s(x)
    mean = x.rolling(window, min_periods=max(3, window // 4)).mean()
    std = x.rolling(window, min_periods=max(3, window // 4)).std().replace(0, np.nan)
    return (x - mean) / std


def _slope(x, window):
    x = _s(x)
    idx = np.arange(window, dtype=float)
    denom = ((idx - idx.mean()) ** 2).sum()
    def calc(v):
        return float(((v - np.nanmean(v)) * (idx - idx.mean())).sum() / denom)
    return x.rolling(window, min_periods=window).apply(calc, raw=True)



def cbr_176_cbr_001_netinc_decline_1_accel_1(cbr_151_cbr_001_netinc_decline_1_roc_1):
    feature = _s(cbr_151_cbr_001_netinc_decline_1_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def cbr_177_cbr_007_interest_coverage_stress_252_accel_42(cbr_152_cbr_007_interest_coverage_stress_252_roc_42):
    feature = _s(cbr_152_cbr_007_interest_coverage_stress_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def cbr_178_cbr_013_netinc_decline_1_accel_126(cbr_153_cbr_013_netinc_decline_1_roc_126):
    feature = _s(cbr_153_cbr_013_netinc_decline_1_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def cbr_179_cbr_019_interest_coverage_stress_84_accel_378(cbr_154_cbr_019_interest_coverage_stress_84_roc_378):
    feature = _s(cbr_154_cbr_019_interest_coverage_stress_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def cbr_180_cbr_025_netinc_decline_1_accel_4(cbr_155_cbr_025_netinc_decline_1_roc_4):
    feature = _s(cbr_155_cbr_025_netinc_decline_1_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















CASH_BURN_REGISTRY_3RD_DERIVATIVES = {
    'cbr_176_cbr_001_netinc_decline_1_accel_1': {'inputs': ['cbr_151_cbr_001_netinc_decline_1_roc_1'], 'func': cbr_176_cbr_001_netinc_decline_1_accel_1},
    'cbr_177_cbr_007_interest_coverage_stress_252_accel_42': {'inputs': ['cbr_152_cbr_007_interest_coverage_stress_252_roc_42'], 'func': cbr_177_cbr_007_interest_coverage_stress_252_accel_42},
    'cbr_178_cbr_013_netinc_decline_1_accel_126': {'inputs': ['cbr_153_cbr_013_netinc_decline_1_roc_126'], 'func': cbr_178_cbr_013_netinc_decline_1_accel_126},
    'cbr_179_cbr_019_interest_coverage_stress_84_accel_378': {'inputs': ['cbr_154_cbr_019_interest_coverage_stress_84_roc_378'], 'func': cbr_179_cbr_019_interest_coverage_stress_84_accel_378},
    'cbr_180_cbr_025_netinc_decline_1_accel_4': {'inputs': ['cbr_155_cbr_025_netinc_decline_1_roc_4'], 'func': cbr_180_cbr_025_netinc_decline_1_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def cb_replacement_d3_001(cb_replacement_d2_001):
    feature = _clean(cb_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_001'] = {'inputs': ['cb_replacement_d2_001'], 'func': cb_replacement_d3_001}


def cb_replacement_d3_002(cb_replacement_d2_002):
    feature = _clean(cb_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_002'] = {'inputs': ['cb_replacement_d2_002'], 'func': cb_replacement_d3_002}


def cb_replacement_d3_003(cb_replacement_d2_003):
    feature = _clean(cb_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_003'] = {'inputs': ['cb_replacement_d2_003'], 'func': cb_replacement_d3_003}


def cb_replacement_d3_004(cb_replacement_d2_004):
    feature = _clean(cb_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_004'] = {'inputs': ['cb_replacement_d2_004'], 'func': cb_replacement_d3_004}


def cb_replacement_d3_005(cb_replacement_d2_005):
    feature = _clean(cb_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_005'] = {'inputs': ['cb_replacement_d2_005'], 'func': cb_replacement_d3_005}


def cb_replacement_d3_006(cb_replacement_d2_006):
    feature = _clean(cb_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_006'] = {'inputs': ['cb_replacement_d2_006'], 'func': cb_replacement_d3_006}


def cb_replacement_d3_007(cb_replacement_d2_007):
    feature = _clean(cb_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_007'] = {'inputs': ['cb_replacement_d2_007'], 'func': cb_replacement_d3_007}


def cb_replacement_d3_008(cb_replacement_d2_008):
    feature = _clean(cb_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_008'] = {'inputs': ['cb_replacement_d2_008'], 'func': cb_replacement_d3_008}


def cb_replacement_d3_009(cb_replacement_d2_009):
    feature = _clean(cb_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_009'] = {'inputs': ['cb_replacement_d2_009'], 'func': cb_replacement_d3_009}


def cb_replacement_d3_010(cb_replacement_d2_010):
    feature = _clean(cb_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_010'] = {'inputs': ['cb_replacement_d2_010'], 'func': cb_replacement_d3_010}


def cb_replacement_d3_011(cb_replacement_d2_011):
    feature = _clean(cb_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_011'] = {'inputs': ['cb_replacement_d2_011'], 'func': cb_replacement_d3_011}


def cb_replacement_d3_012(cb_replacement_d2_012):
    feature = _clean(cb_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_012'] = {'inputs': ['cb_replacement_d2_012'], 'func': cb_replacement_d3_012}


def cb_replacement_d3_013(cb_replacement_d2_013):
    feature = _clean(cb_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_013'] = {'inputs': ['cb_replacement_d2_013'], 'func': cb_replacement_d3_013}


def cb_replacement_d3_014(cb_replacement_d2_014):
    feature = _clean(cb_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_014'] = {'inputs': ['cb_replacement_d2_014'], 'func': cb_replacement_d3_014}


def cb_replacement_d3_015(cb_replacement_d2_015):
    feature = _clean(cb_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_015'] = {'inputs': ['cb_replacement_d2_015'], 'func': cb_replacement_d3_015}


def cb_replacement_d3_016(cb_replacement_d2_016):
    feature = _clean(cb_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_016'] = {'inputs': ['cb_replacement_d2_016'], 'func': cb_replacement_d3_016}


def cb_replacement_d3_017(cb_replacement_d2_017):
    feature = _clean(cb_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_017'] = {'inputs': ['cb_replacement_d2_017'], 'func': cb_replacement_d3_017}


def cb_replacement_d3_018(cb_replacement_d2_018):
    feature = _clean(cb_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_018'] = {'inputs': ['cb_replacement_d2_018'], 'func': cb_replacement_d3_018}


def cb_replacement_d3_019(cb_replacement_d2_019):
    feature = _clean(cb_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_019'] = {'inputs': ['cb_replacement_d2_019'], 'func': cb_replacement_d3_019}


def cb_replacement_d3_020(cb_replacement_d2_020):
    feature = _clean(cb_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_020'] = {'inputs': ['cb_replacement_d2_020'], 'func': cb_replacement_d3_020}


def cb_replacement_d3_021(cb_replacement_d2_021):
    feature = _clean(cb_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_021'] = {'inputs': ['cb_replacement_d2_021'], 'func': cb_replacement_d3_021}


def cb_replacement_d3_022(cb_replacement_d2_022):
    feature = _clean(cb_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_022'] = {'inputs': ['cb_replacement_d2_022'], 'func': cb_replacement_d3_022}


def cb_replacement_d3_023(cb_replacement_d2_023):
    feature = _clean(cb_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_023'] = {'inputs': ['cb_replacement_d2_023'], 'func': cb_replacement_d3_023}


def cb_replacement_d3_024(cb_replacement_d2_024):
    feature = _clean(cb_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_024'] = {'inputs': ['cb_replacement_d2_024'], 'func': cb_replacement_d3_024}


def cb_replacement_d3_025(cb_replacement_d2_025):
    feature = _clean(cb_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_025'] = {'inputs': ['cb_replacement_d2_025'], 'func': cb_replacement_d3_025}


def cb_replacement_d3_026(cb_replacement_d2_026):
    feature = _clean(cb_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_026'] = {'inputs': ['cb_replacement_d2_026'], 'func': cb_replacement_d3_026}


def cb_replacement_d3_027(cb_replacement_d2_027):
    feature = _clean(cb_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_027'] = {'inputs': ['cb_replacement_d2_027'], 'func': cb_replacement_d3_027}


def cb_replacement_d3_028(cb_replacement_d2_028):
    feature = _clean(cb_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_028'] = {'inputs': ['cb_replacement_d2_028'], 'func': cb_replacement_d3_028}


def cb_replacement_d3_029(cb_replacement_d2_029):
    feature = _clean(cb_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_029'] = {'inputs': ['cb_replacement_d2_029'], 'func': cb_replacement_d3_029}


def cb_replacement_d3_030(cb_replacement_d2_030):
    feature = _clean(cb_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_030'] = {'inputs': ['cb_replacement_d2_030'], 'func': cb_replacement_d3_030}


def cb_replacement_d3_031(cb_replacement_d2_031):
    feature = _clean(cb_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_031'] = {'inputs': ['cb_replacement_d2_031'], 'func': cb_replacement_d3_031}


def cb_replacement_d3_032(cb_replacement_d2_032):
    feature = _clean(cb_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_032'] = {'inputs': ['cb_replacement_d2_032'], 'func': cb_replacement_d3_032}


def cb_replacement_d3_033(cb_replacement_d2_033):
    feature = _clean(cb_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_033'] = {'inputs': ['cb_replacement_d2_033'], 'func': cb_replacement_d3_033}


def cb_replacement_d3_034(cb_replacement_d2_034):
    feature = _clean(cb_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_034'] = {'inputs': ['cb_replacement_d2_034'], 'func': cb_replacement_d3_034}


def cb_replacement_d3_035(cb_replacement_d2_035):
    feature = _clean(cb_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_035'] = {'inputs': ['cb_replacement_d2_035'], 'func': cb_replacement_d3_035}


def cb_replacement_d3_036(cb_replacement_d2_036):
    feature = _clean(cb_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_036'] = {'inputs': ['cb_replacement_d2_036'], 'func': cb_replacement_d3_036}


def cb_replacement_d3_037(cb_replacement_d2_037):
    feature = _clean(cb_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_037'] = {'inputs': ['cb_replacement_d2_037'], 'func': cb_replacement_d3_037}


def cb_replacement_d3_038(cb_replacement_d2_038):
    feature = _clean(cb_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_038'] = {'inputs': ['cb_replacement_d2_038'], 'func': cb_replacement_d3_038}


def cb_replacement_d3_039(cb_replacement_d2_039):
    feature = _clean(cb_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_039'] = {'inputs': ['cb_replacement_d2_039'], 'func': cb_replacement_d3_039}


def cb_replacement_d3_040(cb_replacement_d2_040):
    feature = _clean(cb_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_040'] = {'inputs': ['cb_replacement_d2_040'], 'func': cb_replacement_d3_040}


def cb_replacement_d3_041(cb_replacement_d2_041):
    feature = _clean(cb_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_041'] = {'inputs': ['cb_replacement_d2_041'], 'func': cb_replacement_d3_041}


def cb_replacement_d3_042(cb_replacement_d2_042):
    feature = _clean(cb_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_042'] = {'inputs': ['cb_replacement_d2_042'], 'func': cb_replacement_d3_042}


def cb_replacement_d3_043(cb_replacement_d2_043):
    feature = _clean(cb_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_043'] = {'inputs': ['cb_replacement_d2_043'], 'func': cb_replacement_d3_043}


def cb_replacement_d3_044(cb_replacement_d2_044):
    feature = _clean(cb_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_044'] = {'inputs': ['cb_replacement_d2_044'], 'func': cb_replacement_d3_044}


def cb_replacement_d3_045(cb_replacement_d2_045):
    feature = _clean(cb_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_045'] = {'inputs': ['cb_replacement_d2_045'], 'func': cb_replacement_d3_045}


def cb_replacement_d3_046(cb_replacement_d2_046):
    feature = _clean(cb_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_046'] = {'inputs': ['cb_replacement_d2_046'], 'func': cb_replacement_d3_046}


def cb_replacement_d3_047(cb_replacement_d2_047):
    feature = _clean(cb_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_047'] = {'inputs': ['cb_replacement_d2_047'], 'func': cb_replacement_d3_047}


def cb_replacement_d3_048(cb_replacement_d2_048):
    feature = _clean(cb_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_048'] = {'inputs': ['cb_replacement_d2_048'], 'func': cb_replacement_d3_048}


def cb_replacement_d3_049(cb_replacement_d2_049):
    feature = _clean(cb_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_049'] = {'inputs': ['cb_replacement_d2_049'], 'func': cb_replacement_d3_049}


def cb_replacement_d3_050(cb_replacement_d2_050):
    feature = _clean(cb_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_050'] = {'inputs': ['cb_replacement_d2_050'], 'func': cb_replacement_d3_050}


def cb_replacement_d3_051(cb_replacement_d2_051):
    feature = _clean(cb_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_051'] = {'inputs': ['cb_replacement_d2_051'], 'func': cb_replacement_d3_051}


def cb_replacement_d3_052(cb_replacement_d2_052):
    feature = _clean(cb_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_052'] = {'inputs': ['cb_replacement_d2_052'], 'func': cb_replacement_d3_052}


def cb_replacement_d3_053(cb_replacement_d2_053):
    feature = _clean(cb_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_053'] = {'inputs': ['cb_replacement_d2_053'], 'func': cb_replacement_d3_053}


def cb_replacement_d3_054(cb_replacement_d2_054):
    feature = _clean(cb_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_054'] = {'inputs': ['cb_replacement_d2_054'], 'func': cb_replacement_d3_054}


def cb_replacement_d3_055(cb_replacement_d2_055):
    feature = _clean(cb_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_055'] = {'inputs': ['cb_replacement_d2_055'], 'func': cb_replacement_d3_055}


def cb_replacement_d3_056(cb_replacement_d2_056):
    feature = _clean(cb_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_056'] = {'inputs': ['cb_replacement_d2_056'], 'func': cb_replacement_d3_056}


def cb_replacement_d3_057(cb_replacement_d2_057):
    feature = _clean(cb_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_057'] = {'inputs': ['cb_replacement_d2_057'], 'func': cb_replacement_d3_057}


def cb_replacement_d3_058(cb_replacement_d2_058):
    feature = _clean(cb_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_058'] = {'inputs': ['cb_replacement_d2_058'], 'func': cb_replacement_d3_058}


def cb_replacement_d3_059(cb_replacement_d2_059):
    feature = _clean(cb_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_059'] = {'inputs': ['cb_replacement_d2_059'], 'func': cb_replacement_d3_059}


def cb_replacement_d3_060(cb_replacement_d2_060):
    feature = _clean(cb_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_060'] = {'inputs': ['cb_replacement_d2_060'], 'func': cb_replacement_d3_060}


def cb_replacement_d3_061(cb_replacement_d2_061):
    feature = _clean(cb_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_061'] = {'inputs': ['cb_replacement_d2_061'], 'func': cb_replacement_d3_061}


def cb_replacement_d3_062(cb_replacement_d2_062):
    feature = _clean(cb_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_062'] = {'inputs': ['cb_replacement_d2_062'], 'func': cb_replacement_d3_062}


def cb_replacement_d3_063(cb_replacement_d2_063):
    feature = _clean(cb_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_063'] = {'inputs': ['cb_replacement_d2_063'], 'func': cb_replacement_d3_063}


def cb_replacement_d3_064(cb_replacement_d2_064):
    feature = _clean(cb_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_064'] = {'inputs': ['cb_replacement_d2_064'], 'func': cb_replacement_d3_064}


def cb_replacement_d3_065(cb_replacement_d2_065):
    feature = _clean(cb_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_065'] = {'inputs': ['cb_replacement_d2_065'], 'func': cb_replacement_d3_065}


def cb_replacement_d3_066(cb_replacement_d2_066):
    feature = _clean(cb_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_066'] = {'inputs': ['cb_replacement_d2_066'], 'func': cb_replacement_d3_066}


def cb_replacement_d3_067(cb_replacement_d2_067):
    feature = _clean(cb_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_067'] = {'inputs': ['cb_replacement_d2_067'], 'func': cb_replacement_d3_067}


def cb_replacement_d3_068(cb_replacement_d2_068):
    feature = _clean(cb_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_068'] = {'inputs': ['cb_replacement_d2_068'], 'func': cb_replacement_d3_068}


def cb_replacement_d3_069(cb_replacement_d2_069):
    feature = _clean(cb_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_069'] = {'inputs': ['cb_replacement_d2_069'], 'func': cb_replacement_d3_069}


def cb_replacement_d3_070(cb_replacement_d2_070):
    feature = _clean(cb_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_070'] = {'inputs': ['cb_replacement_d2_070'], 'func': cb_replacement_d3_070}


def cb_replacement_d3_071(cb_replacement_d2_071):
    feature = _clean(cb_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_071'] = {'inputs': ['cb_replacement_d2_071'], 'func': cb_replacement_d3_071}


def cb_replacement_d3_072(cb_replacement_d2_072):
    feature = _clean(cb_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_072'] = {'inputs': ['cb_replacement_d2_072'], 'func': cb_replacement_d3_072}


def cb_replacement_d3_073(cb_replacement_d2_073):
    feature = _clean(cb_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_073'] = {'inputs': ['cb_replacement_d2_073'], 'func': cb_replacement_d3_073}


def cb_replacement_d3_074(cb_replacement_d2_074):
    feature = _clean(cb_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_074'] = {'inputs': ['cb_replacement_d2_074'], 'func': cb_replacement_d3_074}


def cb_replacement_d3_075(cb_replacement_d2_075):
    feature = _clean(cb_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_075'] = {'inputs': ['cb_replacement_d2_075'], 'func': cb_replacement_d3_075}


def cb_replacement_d3_076(cb_replacement_d2_076):
    feature = _clean(cb_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_076'] = {'inputs': ['cb_replacement_d2_076'], 'func': cb_replacement_d3_076}


def cb_replacement_d3_077(cb_replacement_d2_077):
    feature = _clean(cb_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_077'] = {'inputs': ['cb_replacement_d2_077'], 'func': cb_replacement_d3_077}


def cb_replacement_d3_078(cb_replacement_d2_078):
    feature = _clean(cb_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_078'] = {'inputs': ['cb_replacement_d2_078'], 'func': cb_replacement_d3_078}


def cb_replacement_d3_079(cb_replacement_d2_079):
    feature = _clean(cb_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_079'] = {'inputs': ['cb_replacement_d2_079'], 'func': cb_replacement_d3_079}


def cb_replacement_d3_080(cb_replacement_d2_080):
    feature = _clean(cb_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_080'] = {'inputs': ['cb_replacement_d2_080'], 'func': cb_replacement_d3_080}


def cb_replacement_d3_081(cb_replacement_d2_081):
    feature = _clean(cb_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_081'] = {'inputs': ['cb_replacement_d2_081'], 'func': cb_replacement_d3_081}


def cb_replacement_d3_082(cb_replacement_d2_082):
    feature = _clean(cb_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_082'] = {'inputs': ['cb_replacement_d2_082'], 'func': cb_replacement_d3_082}


def cb_replacement_d3_083(cb_replacement_d2_083):
    feature = _clean(cb_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_083'] = {'inputs': ['cb_replacement_d2_083'], 'func': cb_replacement_d3_083}


def cb_replacement_d3_084(cb_replacement_d2_084):
    feature = _clean(cb_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_084'] = {'inputs': ['cb_replacement_d2_084'], 'func': cb_replacement_d3_084}


def cb_replacement_d3_085(cb_replacement_d2_085):
    feature = _clean(cb_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_085'] = {'inputs': ['cb_replacement_d2_085'], 'func': cb_replacement_d3_085}


def cb_replacement_d3_086(cb_replacement_d2_086):
    feature = _clean(cb_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_086'] = {'inputs': ['cb_replacement_d2_086'], 'func': cb_replacement_d3_086}


def cb_replacement_d3_087(cb_replacement_d2_087):
    feature = _clean(cb_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_087'] = {'inputs': ['cb_replacement_d2_087'], 'func': cb_replacement_d3_087}


def cb_replacement_d3_088(cb_replacement_d2_088):
    feature = _clean(cb_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_088'] = {'inputs': ['cb_replacement_d2_088'], 'func': cb_replacement_d3_088}


def cb_replacement_d3_089(cb_replacement_d2_089):
    feature = _clean(cb_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_089'] = {'inputs': ['cb_replacement_d2_089'], 'func': cb_replacement_d3_089}


def cb_replacement_d3_090(cb_replacement_d2_090):
    feature = _clean(cb_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_090'] = {'inputs': ['cb_replacement_d2_090'], 'func': cb_replacement_d3_090}


def cb_replacement_d3_091(cb_replacement_d2_091):
    feature = _clean(cb_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_091'] = {'inputs': ['cb_replacement_d2_091'], 'func': cb_replacement_d3_091}


def cb_replacement_d3_092(cb_replacement_d2_092):
    feature = _clean(cb_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_092'] = {'inputs': ['cb_replacement_d2_092'], 'func': cb_replacement_d3_092}


def cb_replacement_d3_093(cb_replacement_d2_093):
    feature = _clean(cb_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_093'] = {'inputs': ['cb_replacement_d2_093'], 'func': cb_replacement_d3_093}


def cb_replacement_d3_094(cb_replacement_d2_094):
    feature = _clean(cb_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_094'] = {'inputs': ['cb_replacement_d2_094'], 'func': cb_replacement_d3_094}


def cb_replacement_d3_095(cb_replacement_d2_095):
    feature = _clean(cb_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_095'] = {'inputs': ['cb_replacement_d2_095'], 'func': cb_replacement_d3_095}


def cb_replacement_d3_096(cb_replacement_d2_096):
    feature = _clean(cb_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_096'] = {'inputs': ['cb_replacement_d2_096'], 'func': cb_replacement_d3_096}


def cb_replacement_d3_097(cb_replacement_d2_097):
    feature = _clean(cb_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_097'] = {'inputs': ['cb_replacement_d2_097'], 'func': cb_replacement_d3_097}


def cb_replacement_d3_098(cb_replacement_d2_098):
    feature = _clean(cb_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_098'] = {'inputs': ['cb_replacement_d2_098'], 'func': cb_replacement_d3_098}


def cb_replacement_d3_099(cb_replacement_d2_099):
    feature = _clean(cb_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_099'] = {'inputs': ['cb_replacement_d2_099'], 'func': cb_replacement_d3_099}


def cb_replacement_d3_100(cb_replacement_d2_100):
    feature = _clean(cb_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_100'] = {'inputs': ['cb_replacement_d2_100'], 'func': cb_replacement_d3_100}


def cb_replacement_d3_101(cb_replacement_d2_101):
    feature = _clean(cb_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_101'] = {'inputs': ['cb_replacement_d2_101'], 'func': cb_replacement_d3_101}


def cb_replacement_d3_102(cb_replacement_d2_102):
    feature = _clean(cb_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_102'] = {'inputs': ['cb_replacement_d2_102'], 'func': cb_replacement_d3_102}


def cb_replacement_d3_103(cb_replacement_d2_103):
    feature = _clean(cb_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_103'] = {'inputs': ['cb_replacement_d2_103'], 'func': cb_replacement_d3_103}


def cb_replacement_d3_104(cb_replacement_d2_104):
    feature = _clean(cb_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_104'] = {'inputs': ['cb_replacement_d2_104'], 'func': cb_replacement_d3_104}


def cb_replacement_d3_105(cb_replacement_d2_105):
    feature = _clean(cb_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_105'] = {'inputs': ['cb_replacement_d2_105'], 'func': cb_replacement_d3_105}


def cb_replacement_d3_106(cb_replacement_d2_106):
    feature = _clean(cb_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_106'] = {'inputs': ['cb_replacement_d2_106'], 'func': cb_replacement_d3_106}


def cb_replacement_d3_107(cb_replacement_d2_107):
    feature = _clean(cb_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_107'] = {'inputs': ['cb_replacement_d2_107'], 'func': cb_replacement_d3_107}


def cb_replacement_d3_108(cb_replacement_d2_108):
    feature = _clean(cb_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_108'] = {'inputs': ['cb_replacement_d2_108'], 'func': cb_replacement_d3_108}


def cb_replacement_d3_109(cb_replacement_d2_109):
    feature = _clean(cb_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_109'] = {'inputs': ['cb_replacement_d2_109'], 'func': cb_replacement_d3_109}


def cb_replacement_d3_110(cb_replacement_d2_110):
    feature = _clean(cb_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_110'] = {'inputs': ['cb_replacement_d2_110'], 'func': cb_replacement_d3_110}


def cb_replacement_d3_111(cb_replacement_d2_111):
    feature = _clean(cb_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_111'] = {'inputs': ['cb_replacement_d2_111'], 'func': cb_replacement_d3_111}


def cb_replacement_d3_112(cb_replacement_d2_112):
    feature = _clean(cb_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_112'] = {'inputs': ['cb_replacement_d2_112'], 'func': cb_replacement_d3_112}


def cb_replacement_d3_113(cb_replacement_d2_113):
    feature = _clean(cb_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_113'] = {'inputs': ['cb_replacement_d2_113'], 'func': cb_replacement_d3_113}


def cb_replacement_d3_114(cb_replacement_d2_114):
    feature = _clean(cb_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_114'] = {'inputs': ['cb_replacement_d2_114'], 'func': cb_replacement_d3_114}


def cb_replacement_d3_115(cb_replacement_d2_115):
    feature = _clean(cb_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_115'] = {'inputs': ['cb_replacement_d2_115'], 'func': cb_replacement_d3_115}


def cb_replacement_d3_116(cb_replacement_d2_116):
    feature = _clean(cb_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_116'] = {'inputs': ['cb_replacement_d2_116'], 'func': cb_replacement_d3_116}


def cb_replacement_d3_117(cb_replacement_d2_117):
    feature = _clean(cb_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_117'] = {'inputs': ['cb_replacement_d2_117'], 'func': cb_replacement_d3_117}


def cb_replacement_d3_118(cb_replacement_d2_118):
    feature = _clean(cb_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_118'] = {'inputs': ['cb_replacement_d2_118'], 'func': cb_replacement_d3_118}


def cb_replacement_d3_119(cb_replacement_d2_119):
    feature = _clean(cb_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_119'] = {'inputs': ['cb_replacement_d2_119'], 'func': cb_replacement_d3_119}


def cb_replacement_d3_120(cb_replacement_d2_120):
    feature = _clean(cb_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_120'] = {'inputs': ['cb_replacement_d2_120'], 'func': cb_replacement_d3_120}


def cb_replacement_d3_121(cb_replacement_d2_121):
    feature = _clean(cb_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_121'] = {'inputs': ['cb_replacement_d2_121'], 'func': cb_replacement_d3_121}


def cb_replacement_d3_122(cb_replacement_d2_122):
    feature = _clean(cb_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_122'] = {'inputs': ['cb_replacement_d2_122'], 'func': cb_replacement_d3_122}


def cb_replacement_d3_123(cb_replacement_d2_123):
    feature = _clean(cb_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_123'] = {'inputs': ['cb_replacement_d2_123'], 'func': cb_replacement_d3_123}


def cb_replacement_d3_124(cb_replacement_d2_124):
    feature = _clean(cb_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_124'] = {'inputs': ['cb_replacement_d2_124'], 'func': cb_replacement_d3_124}


def cb_replacement_d3_125(cb_replacement_d2_125):
    feature = _clean(cb_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_125'] = {'inputs': ['cb_replacement_d2_125'], 'func': cb_replacement_d3_125}


def cb_replacement_d3_126(cb_replacement_d2_126):
    feature = _clean(cb_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_126'] = {'inputs': ['cb_replacement_d2_126'], 'func': cb_replacement_d3_126}


def cb_replacement_d3_127(cb_replacement_d2_127):
    feature = _clean(cb_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_127'] = {'inputs': ['cb_replacement_d2_127'], 'func': cb_replacement_d3_127}


def cb_replacement_d3_128(cb_replacement_d2_128):
    feature = _clean(cb_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_128'] = {'inputs': ['cb_replacement_d2_128'], 'func': cb_replacement_d3_128}


def cb_replacement_d3_129(cb_replacement_d2_129):
    feature = _clean(cb_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_129'] = {'inputs': ['cb_replacement_d2_129'], 'func': cb_replacement_d3_129}


def cb_replacement_d3_130(cb_replacement_d2_130):
    feature = _clean(cb_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_130'] = {'inputs': ['cb_replacement_d2_130'], 'func': cb_replacement_d3_130}


def cb_replacement_d3_131(cb_replacement_d2_131):
    feature = _clean(cb_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_131'] = {'inputs': ['cb_replacement_d2_131'], 'func': cb_replacement_d3_131}


def cb_replacement_d3_132(cb_replacement_d2_132):
    feature = _clean(cb_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_132'] = {'inputs': ['cb_replacement_d2_132'], 'func': cb_replacement_d3_132}


def cb_replacement_d3_133(cb_replacement_d2_133):
    feature = _clean(cb_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_133'] = {'inputs': ['cb_replacement_d2_133'], 'func': cb_replacement_d3_133}


def cb_replacement_d3_134(cb_replacement_d2_134):
    feature = _clean(cb_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_134'] = {'inputs': ['cb_replacement_d2_134'], 'func': cb_replacement_d3_134}


def cb_replacement_d3_135(cb_replacement_d2_135):
    feature = _clean(cb_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_135'] = {'inputs': ['cb_replacement_d2_135'], 'func': cb_replacement_d3_135}


def cb_replacement_d3_136(cb_replacement_d2_136):
    feature = _clean(cb_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_136'] = {'inputs': ['cb_replacement_d2_136'], 'func': cb_replacement_d3_136}


def cb_replacement_d3_137(cb_replacement_d2_137):
    feature = _clean(cb_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_137'] = {'inputs': ['cb_replacement_d2_137'], 'func': cb_replacement_d3_137}


def cb_replacement_d3_138(cb_replacement_d2_138):
    feature = _clean(cb_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_138'] = {'inputs': ['cb_replacement_d2_138'], 'func': cb_replacement_d3_138}


def cb_replacement_d3_139(cb_replacement_d2_139):
    feature = _clean(cb_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_139'] = {'inputs': ['cb_replacement_d2_139'], 'func': cb_replacement_d3_139}


def cb_replacement_d3_140(cb_replacement_d2_140):
    feature = _clean(cb_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_140'] = {'inputs': ['cb_replacement_d2_140'], 'func': cb_replacement_d3_140}


def cb_replacement_d3_141(cb_replacement_d2_141):
    feature = _clean(cb_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_141'] = {'inputs': ['cb_replacement_d2_141'], 'func': cb_replacement_d3_141}


def cb_replacement_d3_142(cb_replacement_d2_142):
    feature = _clean(cb_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_142'] = {'inputs': ['cb_replacement_d2_142'], 'func': cb_replacement_d3_142}


def cb_replacement_d3_143(cb_replacement_d2_143):
    feature = _clean(cb_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_143'] = {'inputs': ['cb_replacement_d2_143'], 'func': cb_replacement_d3_143}


def cb_replacement_d3_144(cb_replacement_d2_144):
    feature = _clean(cb_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_144'] = {'inputs': ['cb_replacement_d2_144'], 'func': cb_replacement_d3_144}


def cb_replacement_d3_145(cb_replacement_d2_145):
    feature = _clean(cb_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_145'] = {'inputs': ['cb_replacement_d2_145'], 'func': cb_replacement_d3_145}


def cb_replacement_d3_146(cb_replacement_d2_146):
    feature = _clean(cb_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_146'] = {'inputs': ['cb_replacement_d2_146'], 'func': cb_replacement_d3_146}


def cb_replacement_d3_147(cb_replacement_d2_147):
    feature = _clean(cb_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_147'] = {'inputs': ['cb_replacement_d2_147'], 'func': cb_replacement_d3_147}


def cb_replacement_d3_148(cb_replacement_d2_148):
    feature = _clean(cb_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_148'] = {'inputs': ['cb_replacement_d2_148'], 'func': cb_replacement_d3_148}


def cb_replacement_d3_149(cb_replacement_d2_149):
    feature = _clean(cb_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_149'] = {'inputs': ['cb_replacement_d2_149'], 'func': cb_replacement_d3_149}


def cb_replacement_d3_150(cb_replacement_d2_150):
    feature = _clean(cb_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_150'] = {'inputs': ['cb_replacement_d2_150'], 'func': cb_replacement_d3_150}


def cb_replacement_d3_151(cb_replacement_d2_151):
    feature = _clean(cb_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_151'] = {'inputs': ['cb_replacement_d2_151'], 'func': cb_replacement_d3_151}


def cb_replacement_d3_152(cb_replacement_d2_152):
    feature = _clean(cb_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_152'] = {'inputs': ['cb_replacement_d2_152'], 'func': cb_replacement_d3_152}


def cb_replacement_d3_153(cb_replacement_d2_153):
    feature = _clean(cb_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_153'] = {'inputs': ['cb_replacement_d2_153'], 'func': cb_replacement_d3_153}


def cb_replacement_d3_154(cb_replacement_d2_154):
    feature = _clean(cb_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_154'] = {'inputs': ['cb_replacement_d2_154'], 'func': cb_replacement_d3_154}


def cb_replacement_d3_155(cb_replacement_d2_155):
    feature = _clean(cb_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_155'] = {'inputs': ['cb_replacement_d2_155'], 'func': cb_replacement_d3_155}


def cb_replacement_d3_156(cb_replacement_d2_156):
    feature = _clean(cb_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_156'] = {'inputs': ['cb_replacement_d2_156'], 'func': cb_replacement_d3_156}


def cb_replacement_d3_157(cb_replacement_d2_157):
    feature = _clean(cb_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_157'] = {'inputs': ['cb_replacement_d2_157'], 'func': cb_replacement_d3_157}


def cb_replacement_d3_158(cb_replacement_d2_158):
    feature = _clean(cb_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_158'] = {'inputs': ['cb_replacement_d2_158'], 'func': cb_replacement_d3_158}


def cb_replacement_d3_159(cb_replacement_d2_159):
    feature = _clean(cb_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_159'] = {'inputs': ['cb_replacement_d2_159'], 'func': cb_replacement_d3_159}


def cb_replacement_d3_160(cb_replacement_d2_160):
    feature = _clean(cb_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_160'] = {'inputs': ['cb_replacement_d2_160'], 'func': cb_replacement_d3_160}


def cb_replacement_d3_161(cb_replacement_d2_161):
    feature = _clean(cb_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_161'] = {'inputs': ['cb_replacement_d2_161'], 'func': cb_replacement_d3_161}


def cb_replacement_d3_162(cb_replacement_d2_162):
    feature = _clean(cb_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_162'] = {'inputs': ['cb_replacement_d2_162'], 'func': cb_replacement_d3_162}


def cb_replacement_d3_163(cb_replacement_d2_163):
    feature = _clean(cb_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_163'] = {'inputs': ['cb_replacement_d2_163'], 'func': cb_replacement_d3_163}


def cb_replacement_d3_164(cb_replacement_d2_164):
    feature = _clean(cb_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_164'] = {'inputs': ['cb_replacement_d2_164'], 'func': cb_replacement_d3_164}


def cb_replacement_d3_165(cb_replacement_d2_165):
    feature = _clean(cb_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_165'] = {'inputs': ['cb_replacement_d2_165'], 'func': cb_replacement_d3_165}


def cb_replacement_d3_166(cb_replacement_d2_166):
    feature = _clean(cb_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
CB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cb_replacement_d3_166'] = {'inputs': ['cb_replacement_d2_166'], 'func': cb_replacement_d3_166}


# Third-derivative extensions for repaired first-base features.
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def cbr_base_universe_d3_001_cbr_003_fcf_burn_to_cash_63(cbr_base_universe_d2_001_cbr_003_fcf_burn_to_cash_63):
    return _base_universe_d3(cbr_base_universe_d2_001_cbr_003_fcf_burn_to_cash_63, 1)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_001_cbr_003_fcf_burn_to_cash_63'] = {'inputs': ['cbr_base_universe_d2_001_cbr_003_fcf_burn_to_cash_63'], 'func': cbr_base_universe_d3_001_cbr_003_fcf_burn_to_cash_63}


def cbr_base_universe_d3_002_cbr_004_debt_to_equity_84(cbr_base_universe_d2_002_cbr_004_debt_to_equity_84):
    return _base_universe_d3(cbr_base_universe_d2_002_cbr_004_debt_to_equity_84, 2)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_002_cbr_004_debt_to_equity_84'] = {'inputs': ['cbr_base_universe_d2_002_cbr_004_debt_to_equity_84'], 'func': cbr_base_universe_d3_002_cbr_004_debt_to_equity_84}


def cbr_base_universe_d3_003_cbr_005_debt_to_assets_126(cbr_base_universe_d2_003_cbr_005_debt_to_assets_126):
    return _base_universe_d3(cbr_base_universe_d2_003_cbr_005_debt_to_assets_126, 3)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_003_cbr_005_debt_to_assets_126'] = {'inputs': ['cbr_base_universe_d2_003_cbr_005_debt_to_assets_126'], 'func': cbr_base_universe_d3_003_cbr_005_debt_to_assets_126}


def cbr_base_universe_d3_004_cbr_012_accrual_gap_1260(cbr_base_universe_d2_004_cbr_012_accrual_gap_1260):
    return _base_universe_d3(cbr_base_universe_d2_004_cbr_012_accrual_gap_1260, 4)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_004_cbr_012_accrual_gap_1260'] = {'inputs': ['cbr_base_universe_d2_004_cbr_012_accrual_gap_1260'], 'func': cbr_base_universe_d3_004_cbr_012_accrual_gap_1260}


def cbr_base_universe_d3_005_cbr_016_debt_to_equity_21(cbr_base_universe_d2_005_cbr_016_debt_to_equity_21):
    return _base_universe_d3(cbr_base_universe_d2_005_cbr_016_debt_to_equity_21, 5)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_005_cbr_016_debt_to_equity_21'] = {'inputs': ['cbr_base_universe_d2_005_cbr_016_debt_to_equity_21'], 'func': cbr_base_universe_d3_005_cbr_016_debt_to_equity_21}


def cbr_base_universe_d3_006_cbr_017_debt_to_assets_42(cbr_base_universe_d2_006_cbr_017_debt_to_assets_42):
    return _base_universe_d3(cbr_base_universe_d2_006_cbr_017_debt_to_assets_42, 6)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_006_cbr_017_debt_to_assets_42'] = {'inputs': ['cbr_base_universe_d2_006_cbr_017_debt_to_assets_42'], 'func': cbr_base_universe_d3_006_cbr_017_debt_to_assets_42}


def cbr_base_universe_d3_007_cbr_024_accrual_gap_504(cbr_base_universe_d2_007_cbr_024_accrual_gap_504):
    return _base_universe_d3(cbr_base_universe_d2_007_cbr_024_accrual_gap_504, 7)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_007_cbr_024_accrual_gap_504'] = {'inputs': ['cbr_base_universe_d2_007_cbr_024_accrual_gap_504'], 'func': cbr_base_universe_d3_007_cbr_024_accrual_gap_504}


def cbr_base_universe_d3_008_cbr_027_fcf_burn_to_cash_1260(cbr_base_universe_d2_008_cbr_027_fcf_burn_to_cash_1260):
    return _base_universe_d3(cbr_base_universe_d2_008_cbr_027_fcf_burn_to_cash_1260, 8)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_008_cbr_027_fcf_burn_to_cash_1260'] = {'inputs': ['cbr_base_universe_d2_008_cbr_027_fcf_burn_to_cash_1260'], 'func': cbr_base_universe_d3_008_cbr_027_fcf_burn_to_cash_1260}


def cbr_base_universe_d3_009_cbr_028_debt_to_equity_1512(cbr_base_universe_d2_009_cbr_028_debt_to_equity_1512):
    return _base_universe_d3(cbr_base_universe_d2_009_cbr_028_debt_to_equity_1512, 9)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_009_cbr_028_debt_to_equity_1512'] = {'inputs': ['cbr_base_universe_d2_009_cbr_028_debt_to_equity_1512'], 'func': cbr_base_universe_d3_009_cbr_028_debt_to_equity_1512}


def cbr_base_universe_d3_010_cbr_029_debt_to_assets_63(cbr_base_universe_d2_010_cbr_029_debt_to_assets_63):
    return _base_universe_d3(cbr_base_universe_d2_010_cbr_029_debt_to_assets_63, 10)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_010_cbr_029_debt_to_assets_63'] = {'inputs': ['cbr_base_universe_d2_010_cbr_029_debt_to_assets_63'], 'func': cbr_base_universe_d3_010_cbr_029_debt_to_assets_63}


def cbr_base_universe_d3_011_cbr_031_interest_coverage_stress_21(cbr_base_universe_d2_011_cbr_031_interest_coverage_stress_21):
    return _base_universe_d3(cbr_base_universe_d2_011_cbr_031_interest_coverage_stress_21, 11)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_011_cbr_031_interest_coverage_stress_21'] = {'inputs': ['cbr_base_universe_d2_011_cbr_031_interest_coverage_stress_21'], 'func': cbr_base_universe_d3_011_cbr_031_interest_coverage_stress_21}


def cbr_base_universe_d3_012_cbr_036_accrual_gap_189(cbr_base_universe_d2_012_cbr_036_accrual_gap_189):
    return _base_universe_d3(cbr_base_universe_d2_012_cbr_036_accrual_gap_189, 12)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_012_cbr_036_accrual_gap_189'] = {'inputs': ['cbr_base_universe_d2_012_cbr_036_accrual_gap_189'], 'func': cbr_base_universe_d3_012_cbr_036_accrual_gap_189}


def cbr_base_universe_d3_013_cbr_039_fcf_burn_to_cash_504(cbr_base_universe_d2_013_cbr_039_fcf_burn_to_cash_504):
    return _base_universe_d3(cbr_base_universe_d2_013_cbr_039_fcf_burn_to_cash_504, 13)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_013_cbr_039_fcf_burn_to_cash_504'] = {'inputs': ['cbr_base_universe_d2_013_cbr_039_fcf_burn_to_cash_504'], 'func': cbr_base_universe_d3_013_cbr_039_fcf_burn_to_cash_504}


def cbr_base_universe_d3_014_cbr_040_debt_to_equity_756(cbr_base_universe_d2_014_cbr_040_debt_to_equity_756):
    return _base_universe_d3(cbr_base_universe_d2_014_cbr_040_debt_to_equity_756, 14)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_014_cbr_040_debt_to_equity_756'] = {'inputs': ['cbr_base_universe_d2_014_cbr_040_debt_to_equity_756'], 'func': cbr_base_universe_d3_014_cbr_040_debt_to_equity_756}


def cbr_base_universe_d3_015_cbr_041_debt_to_assets_1008(cbr_base_universe_d2_015_cbr_041_debt_to_assets_1008):
    return _base_universe_d3(cbr_base_universe_d2_015_cbr_041_debt_to_assets_1008, 15)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_015_cbr_041_debt_to_assets_1008'] = {'inputs': ['cbr_base_universe_d2_015_cbr_041_debt_to_assets_1008'], 'func': cbr_base_universe_d3_015_cbr_041_debt_to_assets_1008}


def cbr_base_universe_d3_016_cbr_043_interest_coverage_stress_1512(cbr_base_universe_d2_016_cbr_043_interest_coverage_stress_1512):
    return _base_universe_d3(cbr_base_universe_d2_016_cbr_043_interest_coverage_stress_1512, 16)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_016_cbr_043_interest_coverage_stress_1512'] = {'inputs': ['cbr_base_universe_d2_016_cbr_043_interest_coverage_stress_1512'], 'func': cbr_base_universe_d3_016_cbr_043_interest_coverage_stress_1512}


def cbr_base_universe_d3_017_cbr_048_accrual_gap_63(cbr_base_universe_d2_017_cbr_048_accrual_gap_63):
    return _base_universe_d3(cbr_base_universe_d2_017_cbr_048_accrual_gap_63, 17)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_017_cbr_048_accrual_gap_63'] = {'inputs': ['cbr_base_universe_d2_017_cbr_048_accrual_gap_63'], 'func': cbr_base_universe_d3_017_cbr_048_accrual_gap_63}


def cbr_base_universe_d3_018_cbr_051_fcf_burn_to_cash_189(cbr_base_universe_d2_018_cbr_051_fcf_burn_to_cash_189):
    return _base_universe_d3(cbr_base_universe_d2_018_cbr_051_fcf_burn_to_cash_189, 18)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_018_cbr_051_fcf_burn_to_cash_189'] = {'inputs': ['cbr_base_universe_d2_018_cbr_051_fcf_burn_to_cash_189'], 'func': cbr_base_universe_d3_018_cbr_051_fcf_burn_to_cash_189}


def cbr_base_universe_d3_019_cbr_052_debt_to_equity_252(cbr_base_universe_d2_019_cbr_052_debt_to_equity_252):
    return _base_universe_d3(cbr_base_universe_d2_019_cbr_052_debt_to_equity_252, 19)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_019_cbr_052_debt_to_equity_252'] = {'inputs': ['cbr_base_universe_d2_019_cbr_052_debt_to_equity_252'], 'func': cbr_base_universe_d3_019_cbr_052_debt_to_equity_252}


def cbr_base_universe_d3_020_cbr_053_debt_to_assets_378(cbr_base_universe_d2_020_cbr_053_debt_to_assets_378):
    return _base_universe_d3(cbr_base_universe_d2_020_cbr_053_debt_to_assets_378, 20)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_020_cbr_053_debt_to_assets_378'] = {'inputs': ['cbr_base_universe_d2_020_cbr_053_debt_to_assets_378'], 'func': cbr_base_universe_d3_020_cbr_053_debt_to_assets_378}


def cbr_base_universe_d3_021_cbr_055_interest_coverage_stress_756(cbr_base_universe_d2_021_cbr_055_interest_coverage_stress_756):
    return _base_universe_d3(cbr_base_universe_d2_021_cbr_055_interest_coverage_stress_756, 21)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_021_cbr_055_interest_coverage_stress_756'] = {'inputs': ['cbr_base_universe_d2_021_cbr_055_interest_coverage_stress_756'], 'func': cbr_base_universe_d3_021_cbr_055_interest_coverage_stress_756}


def cbr_base_universe_d3_022_cbr_060_accrual_gap_252(cbr_base_universe_d2_022_cbr_060_accrual_gap_252):
    return _base_universe_d3(cbr_base_universe_d2_022_cbr_060_accrual_gap_252, 22)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_022_cbr_060_accrual_gap_252'] = {'inputs': ['cbr_base_universe_d2_022_cbr_060_accrual_gap_252'], 'func': cbr_base_universe_d3_022_cbr_060_accrual_gap_252}


def cbr_base_universe_d3_023_cbr_basefill_001(cbr_base_universe_d2_023_cbr_basefill_001):
    return _base_universe_d3(cbr_base_universe_d2_023_cbr_basefill_001, 23)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_023_cbr_basefill_001'] = {'inputs': ['cbr_base_universe_d2_023_cbr_basefill_001'], 'func': cbr_base_universe_d3_023_cbr_basefill_001}


def cbr_base_universe_d3_024_cbr_basefill_002(cbr_base_universe_d2_024_cbr_basefill_002):
    return _base_universe_d3(cbr_base_universe_d2_024_cbr_basefill_002, 24)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_024_cbr_basefill_002'] = {'inputs': ['cbr_base_universe_d2_024_cbr_basefill_002'], 'func': cbr_base_universe_d3_024_cbr_basefill_002}


def cbr_base_universe_d3_025_cbr_basefill_006(cbr_base_universe_d2_025_cbr_basefill_006):
    return _base_universe_d3(cbr_base_universe_d2_025_cbr_basefill_006, 25)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_025_cbr_basefill_006'] = {'inputs': ['cbr_base_universe_d2_025_cbr_basefill_006'], 'func': cbr_base_universe_d3_025_cbr_basefill_006}


def cbr_base_universe_d3_026_cbr_basefill_008(cbr_base_universe_d2_026_cbr_basefill_008):
    return _base_universe_d3(cbr_base_universe_d2_026_cbr_basefill_008, 26)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_026_cbr_basefill_008'] = {'inputs': ['cbr_base_universe_d2_026_cbr_basefill_008'], 'func': cbr_base_universe_d3_026_cbr_basefill_008}


def cbr_base_universe_d3_027_cbr_basefill_009(cbr_base_universe_d2_027_cbr_basefill_009):
    return _base_universe_d3(cbr_base_universe_d2_027_cbr_basefill_009, 27)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_027_cbr_basefill_009'] = {'inputs': ['cbr_base_universe_d2_027_cbr_basefill_009'], 'func': cbr_base_universe_d3_027_cbr_basefill_009}


def cbr_base_universe_d3_028_cbr_basefill_010(cbr_base_universe_d2_028_cbr_basefill_010):
    return _base_universe_d3(cbr_base_universe_d2_028_cbr_basefill_010, 28)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_028_cbr_basefill_010'] = {'inputs': ['cbr_base_universe_d2_028_cbr_basefill_010'], 'func': cbr_base_universe_d3_028_cbr_basefill_010}


def cbr_base_universe_d3_029_cbr_basefill_011(cbr_base_universe_d2_029_cbr_basefill_011):
    return _base_universe_d3(cbr_base_universe_d2_029_cbr_basefill_011, 29)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_029_cbr_basefill_011'] = {'inputs': ['cbr_base_universe_d2_029_cbr_basefill_011'], 'func': cbr_base_universe_d3_029_cbr_basefill_011}


def cbr_base_universe_d3_030_cbr_basefill_013(cbr_base_universe_d2_030_cbr_basefill_013):
    return _base_universe_d3(cbr_base_universe_d2_030_cbr_basefill_013, 30)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_030_cbr_basefill_013'] = {'inputs': ['cbr_base_universe_d2_030_cbr_basefill_013'], 'func': cbr_base_universe_d3_030_cbr_basefill_013}


def cbr_base_universe_d3_031_cbr_basefill_014(cbr_base_universe_d2_031_cbr_basefill_014):
    return _base_universe_d3(cbr_base_universe_d2_031_cbr_basefill_014, 31)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_031_cbr_basefill_014'] = {'inputs': ['cbr_base_universe_d2_031_cbr_basefill_014'], 'func': cbr_base_universe_d3_031_cbr_basefill_014}


def cbr_base_universe_d3_032_cbr_basefill_015(cbr_base_universe_d2_032_cbr_basefill_015):
    return _base_universe_d3(cbr_base_universe_d2_032_cbr_basefill_015, 32)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_032_cbr_basefill_015'] = {'inputs': ['cbr_base_universe_d2_032_cbr_basefill_015'], 'func': cbr_base_universe_d3_032_cbr_basefill_015}


def cbr_base_universe_d3_033_cbr_basefill_018(cbr_base_universe_d2_033_cbr_basefill_018):
    return _base_universe_d3(cbr_base_universe_d2_033_cbr_basefill_018, 33)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_033_cbr_basefill_018'] = {'inputs': ['cbr_base_universe_d2_033_cbr_basefill_018'], 'func': cbr_base_universe_d3_033_cbr_basefill_018}


def cbr_base_universe_d3_034_cbr_basefill_020(cbr_base_universe_d2_034_cbr_basefill_020):
    return _base_universe_d3(cbr_base_universe_d2_034_cbr_basefill_020, 34)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_034_cbr_basefill_020'] = {'inputs': ['cbr_base_universe_d2_034_cbr_basefill_020'], 'func': cbr_base_universe_d3_034_cbr_basefill_020}


def cbr_base_universe_d3_035_cbr_basefill_021(cbr_base_universe_d2_035_cbr_basefill_021):
    return _base_universe_d3(cbr_base_universe_d2_035_cbr_basefill_021, 35)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_035_cbr_basefill_021'] = {'inputs': ['cbr_base_universe_d2_035_cbr_basefill_021'], 'func': cbr_base_universe_d3_035_cbr_basefill_021}


def cbr_base_universe_d3_036_cbr_basefill_022(cbr_base_universe_d2_036_cbr_basefill_022):
    return _base_universe_d3(cbr_base_universe_d2_036_cbr_basefill_022, 36)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_036_cbr_basefill_022'] = {'inputs': ['cbr_base_universe_d2_036_cbr_basefill_022'], 'func': cbr_base_universe_d3_036_cbr_basefill_022}


def cbr_base_universe_d3_037_cbr_basefill_023(cbr_base_universe_d2_037_cbr_basefill_023):
    return _base_universe_d3(cbr_base_universe_d2_037_cbr_basefill_023, 37)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_037_cbr_basefill_023'] = {'inputs': ['cbr_base_universe_d2_037_cbr_basefill_023'], 'func': cbr_base_universe_d3_037_cbr_basefill_023}


def cbr_base_universe_d3_038_cbr_basefill_025(cbr_base_universe_d2_038_cbr_basefill_025):
    return _base_universe_d3(cbr_base_universe_d2_038_cbr_basefill_025, 38)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_038_cbr_basefill_025'] = {'inputs': ['cbr_base_universe_d2_038_cbr_basefill_025'], 'func': cbr_base_universe_d3_038_cbr_basefill_025}


def cbr_base_universe_d3_039_cbr_basefill_026(cbr_base_universe_d2_039_cbr_basefill_026):
    return _base_universe_d3(cbr_base_universe_d2_039_cbr_basefill_026, 39)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_039_cbr_basefill_026'] = {'inputs': ['cbr_base_universe_d2_039_cbr_basefill_026'], 'func': cbr_base_universe_d3_039_cbr_basefill_026}


def cbr_base_universe_d3_040_cbr_basefill_030(cbr_base_universe_d2_040_cbr_basefill_030):
    return _base_universe_d3(cbr_base_universe_d2_040_cbr_basefill_030, 40)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_040_cbr_basefill_030'] = {'inputs': ['cbr_base_universe_d2_040_cbr_basefill_030'], 'func': cbr_base_universe_d3_040_cbr_basefill_030}


def cbr_base_universe_d3_041_cbr_basefill_032(cbr_base_universe_d2_041_cbr_basefill_032):
    return _base_universe_d3(cbr_base_universe_d2_041_cbr_basefill_032, 41)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_041_cbr_basefill_032'] = {'inputs': ['cbr_base_universe_d2_041_cbr_basefill_032'], 'func': cbr_base_universe_d3_041_cbr_basefill_032}


def cbr_base_universe_d3_042_cbr_basefill_033(cbr_base_universe_d2_042_cbr_basefill_033):
    return _base_universe_d3(cbr_base_universe_d2_042_cbr_basefill_033, 42)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_042_cbr_basefill_033'] = {'inputs': ['cbr_base_universe_d2_042_cbr_basefill_033'], 'func': cbr_base_universe_d3_042_cbr_basefill_033}


def cbr_base_universe_d3_043_cbr_basefill_034(cbr_base_universe_d2_043_cbr_basefill_034):
    return _base_universe_d3(cbr_base_universe_d2_043_cbr_basefill_034, 43)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_043_cbr_basefill_034'] = {'inputs': ['cbr_base_universe_d2_043_cbr_basefill_034'], 'func': cbr_base_universe_d3_043_cbr_basefill_034}


def cbr_base_universe_d3_044_cbr_basefill_035(cbr_base_universe_d2_044_cbr_basefill_035):
    return _base_universe_d3(cbr_base_universe_d2_044_cbr_basefill_035, 44)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_044_cbr_basefill_035'] = {'inputs': ['cbr_base_universe_d2_044_cbr_basefill_035'], 'func': cbr_base_universe_d3_044_cbr_basefill_035}


def cbr_base_universe_d3_045_cbr_basefill_037(cbr_base_universe_d2_045_cbr_basefill_037):
    return _base_universe_d3(cbr_base_universe_d2_045_cbr_basefill_037, 45)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_045_cbr_basefill_037'] = {'inputs': ['cbr_base_universe_d2_045_cbr_basefill_037'], 'func': cbr_base_universe_d3_045_cbr_basefill_037}


def cbr_base_universe_d3_046_cbr_basefill_038(cbr_base_universe_d2_046_cbr_basefill_038):
    return _base_universe_d3(cbr_base_universe_d2_046_cbr_basefill_038, 46)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_046_cbr_basefill_038'] = {'inputs': ['cbr_base_universe_d2_046_cbr_basefill_038'], 'func': cbr_base_universe_d3_046_cbr_basefill_038}


def cbr_base_universe_d3_047_cbr_basefill_042(cbr_base_universe_d2_047_cbr_basefill_042):
    return _base_universe_d3(cbr_base_universe_d2_047_cbr_basefill_042, 47)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_047_cbr_basefill_042'] = {'inputs': ['cbr_base_universe_d2_047_cbr_basefill_042'], 'func': cbr_base_universe_d3_047_cbr_basefill_042}


def cbr_base_universe_d3_048_cbr_basefill_044(cbr_base_universe_d2_048_cbr_basefill_044):
    return _base_universe_d3(cbr_base_universe_d2_048_cbr_basefill_044, 48)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_048_cbr_basefill_044'] = {'inputs': ['cbr_base_universe_d2_048_cbr_basefill_044'], 'func': cbr_base_universe_d3_048_cbr_basefill_044}


def cbr_base_universe_d3_049_cbr_basefill_045(cbr_base_universe_d2_049_cbr_basefill_045):
    return _base_universe_d3(cbr_base_universe_d2_049_cbr_basefill_045, 49)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_049_cbr_basefill_045'] = {'inputs': ['cbr_base_universe_d2_049_cbr_basefill_045'], 'func': cbr_base_universe_d3_049_cbr_basefill_045}


def cbr_base_universe_d3_050_cbr_basefill_046(cbr_base_universe_d2_050_cbr_basefill_046):
    return _base_universe_d3(cbr_base_universe_d2_050_cbr_basefill_046, 50)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_050_cbr_basefill_046'] = {'inputs': ['cbr_base_universe_d2_050_cbr_basefill_046'], 'func': cbr_base_universe_d3_050_cbr_basefill_046}


def cbr_base_universe_d3_051_cbr_basefill_047(cbr_base_universe_d2_051_cbr_basefill_047):
    return _base_universe_d3(cbr_base_universe_d2_051_cbr_basefill_047, 51)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_051_cbr_basefill_047'] = {'inputs': ['cbr_base_universe_d2_051_cbr_basefill_047'], 'func': cbr_base_universe_d3_051_cbr_basefill_047}


def cbr_base_universe_d3_052_cbr_basefill_049(cbr_base_universe_d2_052_cbr_basefill_049):
    return _base_universe_d3(cbr_base_universe_d2_052_cbr_basefill_049, 52)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_052_cbr_basefill_049'] = {'inputs': ['cbr_base_universe_d2_052_cbr_basefill_049'], 'func': cbr_base_universe_d3_052_cbr_basefill_049}


def cbr_base_universe_d3_053_cbr_basefill_050(cbr_base_universe_d2_053_cbr_basefill_050):
    return _base_universe_d3(cbr_base_universe_d2_053_cbr_basefill_050, 53)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_053_cbr_basefill_050'] = {'inputs': ['cbr_base_universe_d2_053_cbr_basefill_050'], 'func': cbr_base_universe_d3_053_cbr_basefill_050}


def cbr_base_universe_d3_054_cbr_basefill_054(cbr_base_universe_d2_054_cbr_basefill_054):
    return _base_universe_d3(cbr_base_universe_d2_054_cbr_basefill_054, 54)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_054_cbr_basefill_054'] = {'inputs': ['cbr_base_universe_d2_054_cbr_basefill_054'], 'func': cbr_base_universe_d3_054_cbr_basefill_054}


def cbr_base_universe_d3_055_cbr_basefill_056(cbr_base_universe_d2_055_cbr_basefill_056):
    return _base_universe_d3(cbr_base_universe_d2_055_cbr_basefill_056, 55)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_055_cbr_basefill_056'] = {'inputs': ['cbr_base_universe_d2_055_cbr_basefill_056'], 'func': cbr_base_universe_d3_055_cbr_basefill_056}


def cbr_base_universe_d3_056_cbr_basefill_057(cbr_base_universe_d2_056_cbr_basefill_057):
    return _base_universe_d3(cbr_base_universe_d2_056_cbr_basefill_057, 56)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_056_cbr_basefill_057'] = {'inputs': ['cbr_base_universe_d2_056_cbr_basefill_057'], 'func': cbr_base_universe_d3_056_cbr_basefill_057}


def cbr_base_universe_d3_057_cbr_basefill_058(cbr_base_universe_d2_057_cbr_basefill_058):
    return _base_universe_d3(cbr_base_universe_d2_057_cbr_basefill_058, 57)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_057_cbr_basefill_058'] = {'inputs': ['cbr_base_universe_d2_057_cbr_basefill_058'], 'func': cbr_base_universe_d3_057_cbr_basefill_058}


def cbr_base_universe_d3_058_cbr_basefill_059(cbr_base_universe_d2_058_cbr_basefill_059):
    return _base_universe_d3(cbr_base_universe_d2_058_cbr_basefill_059, 58)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_058_cbr_basefill_059'] = {'inputs': ['cbr_base_universe_d2_058_cbr_basefill_059'], 'func': cbr_base_universe_d3_058_cbr_basefill_059}


def cbr_base_universe_d3_059_cbr_basefill_061(cbr_base_universe_d2_059_cbr_basefill_061):
    return _base_universe_d3(cbr_base_universe_d2_059_cbr_basefill_061, 59)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_059_cbr_basefill_061'] = {'inputs': ['cbr_base_universe_d2_059_cbr_basefill_061'], 'func': cbr_base_universe_d3_059_cbr_basefill_061}


def cbr_base_universe_d3_060_cbr_basefill_062(cbr_base_universe_d2_060_cbr_basefill_062):
    return _base_universe_d3(cbr_base_universe_d2_060_cbr_basefill_062, 60)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_060_cbr_basefill_062'] = {'inputs': ['cbr_base_universe_d2_060_cbr_basefill_062'], 'func': cbr_base_universe_d3_060_cbr_basefill_062}


def cbr_base_universe_d3_061_cbr_basefill_063(cbr_base_universe_d2_061_cbr_basefill_063):
    return _base_universe_d3(cbr_base_universe_d2_061_cbr_basefill_063, 61)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_061_cbr_basefill_063'] = {'inputs': ['cbr_base_universe_d2_061_cbr_basefill_063'], 'func': cbr_base_universe_d3_061_cbr_basefill_063}


def cbr_base_universe_d3_062_cbr_basefill_064(cbr_base_universe_d2_062_cbr_basefill_064):
    return _base_universe_d3(cbr_base_universe_d2_062_cbr_basefill_064, 62)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_062_cbr_basefill_064'] = {'inputs': ['cbr_base_universe_d2_062_cbr_basefill_064'], 'func': cbr_base_universe_d3_062_cbr_basefill_064}


def cbr_base_universe_d3_063_cbr_basefill_065(cbr_base_universe_d2_063_cbr_basefill_065):
    return _base_universe_d3(cbr_base_universe_d2_063_cbr_basefill_065, 63)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_063_cbr_basefill_065'] = {'inputs': ['cbr_base_universe_d2_063_cbr_basefill_065'], 'func': cbr_base_universe_d3_063_cbr_basefill_065}


def cbr_base_universe_d3_064_cbr_basefill_066(cbr_base_universe_d2_064_cbr_basefill_066):
    return _base_universe_d3(cbr_base_universe_d2_064_cbr_basefill_066, 64)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_064_cbr_basefill_066'] = {'inputs': ['cbr_base_universe_d2_064_cbr_basefill_066'], 'func': cbr_base_universe_d3_064_cbr_basefill_066}


def cbr_base_universe_d3_065_cbr_basefill_067(cbr_base_universe_d2_065_cbr_basefill_067):
    return _base_universe_d3(cbr_base_universe_d2_065_cbr_basefill_067, 65)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_065_cbr_basefill_067'] = {'inputs': ['cbr_base_universe_d2_065_cbr_basefill_067'], 'func': cbr_base_universe_d3_065_cbr_basefill_067}


def cbr_base_universe_d3_066_cbr_basefill_068(cbr_base_universe_d2_066_cbr_basefill_068):
    return _base_universe_d3(cbr_base_universe_d2_066_cbr_basefill_068, 66)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_066_cbr_basefill_068'] = {'inputs': ['cbr_base_universe_d2_066_cbr_basefill_068'], 'func': cbr_base_universe_d3_066_cbr_basefill_068}


def cbr_base_universe_d3_067_cbr_basefill_069(cbr_base_universe_d2_067_cbr_basefill_069):
    return _base_universe_d3(cbr_base_universe_d2_067_cbr_basefill_069, 67)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_067_cbr_basefill_069'] = {'inputs': ['cbr_base_universe_d2_067_cbr_basefill_069'], 'func': cbr_base_universe_d3_067_cbr_basefill_069}


def cbr_base_universe_d3_068_cbr_basefill_070(cbr_base_universe_d2_068_cbr_basefill_070):
    return _base_universe_d3(cbr_base_universe_d2_068_cbr_basefill_070, 68)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_068_cbr_basefill_070'] = {'inputs': ['cbr_base_universe_d2_068_cbr_basefill_070'], 'func': cbr_base_universe_d3_068_cbr_basefill_070}


def cbr_base_universe_d3_069_cbr_basefill_071(cbr_base_universe_d2_069_cbr_basefill_071):
    return _base_universe_d3(cbr_base_universe_d2_069_cbr_basefill_071, 69)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_069_cbr_basefill_071'] = {'inputs': ['cbr_base_universe_d2_069_cbr_basefill_071'], 'func': cbr_base_universe_d3_069_cbr_basefill_071}


def cbr_base_universe_d3_070_cbr_basefill_072(cbr_base_universe_d2_070_cbr_basefill_072):
    return _base_universe_d3(cbr_base_universe_d2_070_cbr_basefill_072, 70)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_070_cbr_basefill_072'] = {'inputs': ['cbr_base_universe_d2_070_cbr_basefill_072'], 'func': cbr_base_universe_d3_070_cbr_basefill_072}


def cbr_base_universe_d3_071_cbr_basefill_073(cbr_base_universe_d2_071_cbr_basefill_073):
    return _base_universe_d3(cbr_base_universe_d2_071_cbr_basefill_073, 71)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_071_cbr_basefill_073'] = {'inputs': ['cbr_base_universe_d2_071_cbr_basefill_073'], 'func': cbr_base_universe_d3_071_cbr_basefill_073}


def cbr_base_universe_d3_072_cbr_basefill_074(cbr_base_universe_d2_072_cbr_basefill_074):
    return _base_universe_d3(cbr_base_universe_d2_072_cbr_basefill_074, 72)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_072_cbr_basefill_074'] = {'inputs': ['cbr_base_universe_d2_072_cbr_basefill_074'], 'func': cbr_base_universe_d3_072_cbr_basefill_074}


def cbr_base_universe_d3_073_cbr_basefill_075(cbr_base_universe_d2_073_cbr_basefill_075):
    return _base_universe_d3(cbr_base_universe_d2_073_cbr_basefill_075, 73)
CBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cbr_base_universe_d3_073_cbr_basefill_075'] = {'inputs': ['cbr_base_universe_d2_073_cbr_basefill_075'], 'func': cbr_base_universe_d3_073_cbr_basefill_075}
