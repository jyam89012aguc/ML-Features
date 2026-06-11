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



def ecl_176_ecl_001_netinc_decline_1_accel_1(ecl_151_ecl_001_netinc_decline_1_roc_1):
    feature = _s(ecl_151_ecl_001_netinc_decline_1_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def ecl_177_ecl_007_interest_coverage_stress_252_accel_42(ecl_152_ecl_007_interest_coverage_stress_252_roc_42):
    feature = _s(ecl_152_ecl_007_interest_coverage_stress_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def ecl_178_ecl_013_netinc_decline_1_accel_126(ecl_153_ecl_013_netinc_decline_1_roc_126):
    feature = _s(ecl_153_ecl_013_netinc_decline_1_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def ecl_179_ecl_019_interest_coverage_stress_84_accel_378(ecl_154_ecl_019_interest_coverage_stress_84_roc_378):
    feature = _s(ecl_154_ecl_019_interest_coverage_stress_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def ecl_180_ecl_025_netinc_decline_1_accel_4(ecl_155_ecl_025_netinc_decline_1_roc_4):
    feature = _s(ecl_155_ecl_025_netinc_decline_1_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















EARNINGS_COLLAPSE_REGISTRY_3RD_DERIVATIVES = {
    'ecl_176_ecl_001_netinc_decline_1_accel_1': {'inputs': ['ecl_151_ecl_001_netinc_decline_1_roc_1'], 'func': ecl_176_ecl_001_netinc_decline_1_accel_1},
    'ecl_177_ecl_007_interest_coverage_stress_252_accel_42': {'inputs': ['ecl_152_ecl_007_interest_coverage_stress_252_roc_42'], 'func': ecl_177_ecl_007_interest_coverage_stress_252_accel_42},
    'ecl_178_ecl_013_netinc_decline_1_accel_126': {'inputs': ['ecl_153_ecl_013_netinc_decline_1_roc_126'], 'func': ecl_178_ecl_013_netinc_decline_1_accel_126},
    'ecl_179_ecl_019_interest_coverage_stress_84_accel_378': {'inputs': ['ecl_154_ecl_019_interest_coverage_stress_84_roc_378'], 'func': ecl_179_ecl_019_interest_coverage_stress_84_accel_378},
    'ecl_180_ecl_025_netinc_decline_1_accel_4': {'inputs': ['ecl_155_ecl_025_netinc_decline_1_roc_4'], 'func': ecl_180_ecl_025_netinc_decline_1_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def ec_replacement_d3_001(ec_replacement_d2_001):
    feature = _clean(ec_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_001'] = {'inputs': ['ec_replacement_d2_001'], 'func': ec_replacement_d3_001}


def ec_replacement_d3_002(ec_replacement_d2_002):
    feature = _clean(ec_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_002'] = {'inputs': ['ec_replacement_d2_002'], 'func': ec_replacement_d3_002}


def ec_replacement_d3_003(ec_replacement_d2_003):
    feature = _clean(ec_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_003'] = {'inputs': ['ec_replacement_d2_003'], 'func': ec_replacement_d3_003}


def ec_replacement_d3_004(ec_replacement_d2_004):
    feature = _clean(ec_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_004'] = {'inputs': ['ec_replacement_d2_004'], 'func': ec_replacement_d3_004}


def ec_replacement_d3_005(ec_replacement_d2_005):
    feature = _clean(ec_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_005'] = {'inputs': ['ec_replacement_d2_005'], 'func': ec_replacement_d3_005}


def ec_replacement_d3_006(ec_replacement_d2_006):
    feature = _clean(ec_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_006'] = {'inputs': ['ec_replacement_d2_006'], 'func': ec_replacement_d3_006}


def ec_replacement_d3_007(ec_replacement_d2_007):
    feature = _clean(ec_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_007'] = {'inputs': ['ec_replacement_d2_007'], 'func': ec_replacement_d3_007}


def ec_replacement_d3_008(ec_replacement_d2_008):
    feature = _clean(ec_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_008'] = {'inputs': ['ec_replacement_d2_008'], 'func': ec_replacement_d3_008}


def ec_replacement_d3_009(ec_replacement_d2_009):
    feature = _clean(ec_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_009'] = {'inputs': ['ec_replacement_d2_009'], 'func': ec_replacement_d3_009}


def ec_replacement_d3_010(ec_replacement_d2_010):
    feature = _clean(ec_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_010'] = {'inputs': ['ec_replacement_d2_010'], 'func': ec_replacement_d3_010}


def ec_replacement_d3_011(ec_replacement_d2_011):
    feature = _clean(ec_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_011'] = {'inputs': ['ec_replacement_d2_011'], 'func': ec_replacement_d3_011}


def ec_replacement_d3_012(ec_replacement_d2_012):
    feature = _clean(ec_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_012'] = {'inputs': ['ec_replacement_d2_012'], 'func': ec_replacement_d3_012}


def ec_replacement_d3_013(ec_replacement_d2_013):
    feature = _clean(ec_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_013'] = {'inputs': ['ec_replacement_d2_013'], 'func': ec_replacement_d3_013}


def ec_replacement_d3_014(ec_replacement_d2_014):
    feature = _clean(ec_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_014'] = {'inputs': ['ec_replacement_d2_014'], 'func': ec_replacement_d3_014}


def ec_replacement_d3_015(ec_replacement_d2_015):
    feature = _clean(ec_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_015'] = {'inputs': ['ec_replacement_d2_015'], 'func': ec_replacement_d3_015}


def ec_replacement_d3_016(ec_replacement_d2_016):
    feature = _clean(ec_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_016'] = {'inputs': ['ec_replacement_d2_016'], 'func': ec_replacement_d3_016}


def ec_replacement_d3_017(ec_replacement_d2_017):
    feature = _clean(ec_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_017'] = {'inputs': ['ec_replacement_d2_017'], 'func': ec_replacement_d3_017}


def ec_replacement_d3_018(ec_replacement_d2_018):
    feature = _clean(ec_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_018'] = {'inputs': ['ec_replacement_d2_018'], 'func': ec_replacement_d3_018}


def ec_replacement_d3_019(ec_replacement_d2_019):
    feature = _clean(ec_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_019'] = {'inputs': ['ec_replacement_d2_019'], 'func': ec_replacement_d3_019}


def ec_replacement_d3_020(ec_replacement_d2_020):
    feature = _clean(ec_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_020'] = {'inputs': ['ec_replacement_d2_020'], 'func': ec_replacement_d3_020}


def ec_replacement_d3_021(ec_replacement_d2_021):
    feature = _clean(ec_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_021'] = {'inputs': ['ec_replacement_d2_021'], 'func': ec_replacement_d3_021}


def ec_replacement_d3_022(ec_replacement_d2_022):
    feature = _clean(ec_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_022'] = {'inputs': ['ec_replacement_d2_022'], 'func': ec_replacement_d3_022}


def ec_replacement_d3_023(ec_replacement_d2_023):
    feature = _clean(ec_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_023'] = {'inputs': ['ec_replacement_d2_023'], 'func': ec_replacement_d3_023}


def ec_replacement_d3_024(ec_replacement_d2_024):
    feature = _clean(ec_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_024'] = {'inputs': ['ec_replacement_d2_024'], 'func': ec_replacement_d3_024}


def ec_replacement_d3_025(ec_replacement_d2_025):
    feature = _clean(ec_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_025'] = {'inputs': ['ec_replacement_d2_025'], 'func': ec_replacement_d3_025}


def ec_replacement_d3_026(ec_replacement_d2_026):
    feature = _clean(ec_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_026'] = {'inputs': ['ec_replacement_d2_026'], 'func': ec_replacement_d3_026}


def ec_replacement_d3_027(ec_replacement_d2_027):
    feature = _clean(ec_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_027'] = {'inputs': ['ec_replacement_d2_027'], 'func': ec_replacement_d3_027}


def ec_replacement_d3_028(ec_replacement_d2_028):
    feature = _clean(ec_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_028'] = {'inputs': ['ec_replacement_d2_028'], 'func': ec_replacement_d3_028}


def ec_replacement_d3_029(ec_replacement_d2_029):
    feature = _clean(ec_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_029'] = {'inputs': ['ec_replacement_d2_029'], 'func': ec_replacement_d3_029}


def ec_replacement_d3_030(ec_replacement_d2_030):
    feature = _clean(ec_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_030'] = {'inputs': ['ec_replacement_d2_030'], 'func': ec_replacement_d3_030}


def ec_replacement_d3_031(ec_replacement_d2_031):
    feature = _clean(ec_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_031'] = {'inputs': ['ec_replacement_d2_031'], 'func': ec_replacement_d3_031}


def ec_replacement_d3_032(ec_replacement_d2_032):
    feature = _clean(ec_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_032'] = {'inputs': ['ec_replacement_d2_032'], 'func': ec_replacement_d3_032}


def ec_replacement_d3_033(ec_replacement_d2_033):
    feature = _clean(ec_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_033'] = {'inputs': ['ec_replacement_d2_033'], 'func': ec_replacement_d3_033}


def ec_replacement_d3_034(ec_replacement_d2_034):
    feature = _clean(ec_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_034'] = {'inputs': ['ec_replacement_d2_034'], 'func': ec_replacement_d3_034}


def ec_replacement_d3_035(ec_replacement_d2_035):
    feature = _clean(ec_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_035'] = {'inputs': ['ec_replacement_d2_035'], 'func': ec_replacement_d3_035}


def ec_replacement_d3_036(ec_replacement_d2_036):
    feature = _clean(ec_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_036'] = {'inputs': ['ec_replacement_d2_036'], 'func': ec_replacement_d3_036}


def ec_replacement_d3_037(ec_replacement_d2_037):
    feature = _clean(ec_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_037'] = {'inputs': ['ec_replacement_d2_037'], 'func': ec_replacement_d3_037}


def ec_replacement_d3_038(ec_replacement_d2_038):
    feature = _clean(ec_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_038'] = {'inputs': ['ec_replacement_d2_038'], 'func': ec_replacement_d3_038}


def ec_replacement_d3_039(ec_replacement_d2_039):
    feature = _clean(ec_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_039'] = {'inputs': ['ec_replacement_d2_039'], 'func': ec_replacement_d3_039}


def ec_replacement_d3_040(ec_replacement_d2_040):
    feature = _clean(ec_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_040'] = {'inputs': ['ec_replacement_d2_040'], 'func': ec_replacement_d3_040}


def ec_replacement_d3_041(ec_replacement_d2_041):
    feature = _clean(ec_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_041'] = {'inputs': ['ec_replacement_d2_041'], 'func': ec_replacement_d3_041}


def ec_replacement_d3_042(ec_replacement_d2_042):
    feature = _clean(ec_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_042'] = {'inputs': ['ec_replacement_d2_042'], 'func': ec_replacement_d3_042}


def ec_replacement_d3_043(ec_replacement_d2_043):
    feature = _clean(ec_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_043'] = {'inputs': ['ec_replacement_d2_043'], 'func': ec_replacement_d3_043}


def ec_replacement_d3_044(ec_replacement_d2_044):
    feature = _clean(ec_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_044'] = {'inputs': ['ec_replacement_d2_044'], 'func': ec_replacement_d3_044}


def ec_replacement_d3_045(ec_replacement_d2_045):
    feature = _clean(ec_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_045'] = {'inputs': ['ec_replacement_d2_045'], 'func': ec_replacement_d3_045}


def ec_replacement_d3_046(ec_replacement_d2_046):
    feature = _clean(ec_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_046'] = {'inputs': ['ec_replacement_d2_046'], 'func': ec_replacement_d3_046}


def ec_replacement_d3_047(ec_replacement_d2_047):
    feature = _clean(ec_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_047'] = {'inputs': ['ec_replacement_d2_047'], 'func': ec_replacement_d3_047}


def ec_replacement_d3_048(ec_replacement_d2_048):
    feature = _clean(ec_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_048'] = {'inputs': ['ec_replacement_d2_048'], 'func': ec_replacement_d3_048}


def ec_replacement_d3_049(ec_replacement_d2_049):
    feature = _clean(ec_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_049'] = {'inputs': ['ec_replacement_d2_049'], 'func': ec_replacement_d3_049}


def ec_replacement_d3_050(ec_replacement_d2_050):
    feature = _clean(ec_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_050'] = {'inputs': ['ec_replacement_d2_050'], 'func': ec_replacement_d3_050}


def ec_replacement_d3_051(ec_replacement_d2_051):
    feature = _clean(ec_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_051'] = {'inputs': ['ec_replacement_d2_051'], 'func': ec_replacement_d3_051}


def ec_replacement_d3_052(ec_replacement_d2_052):
    feature = _clean(ec_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_052'] = {'inputs': ['ec_replacement_d2_052'], 'func': ec_replacement_d3_052}


def ec_replacement_d3_053(ec_replacement_d2_053):
    feature = _clean(ec_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_053'] = {'inputs': ['ec_replacement_d2_053'], 'func': ec_replacement_d3_053}


def ec_replacement_d3_054(ec_replacement_d2_054):
    feature = _clean(ec_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_054'] = {'inputs': ['ec_replacement_d2_054'], 'func': ec_replacement_d3_054}


def ec_replacement_d3_055(ec_replacement_d2_055):
    feature = _clean(ec_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_055'] = {'inputs': ['ec_replacement_d2_055'], 'func': ec_replacement_d3_055}


def ec_replacement_d3_056(ec_replacement_d2_056):
    feature = _clean(ec_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_056'] = {'inputs': ['ec_replacement_d2_056'], 'func': ec_replacement_d3_056}


def ec_replacement_d3_057(ec_replacement_d2_057):
    feature = _clean(ec_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_057'] = {'inputs': ['ec_replacement_d2_057'], 'func': ec_replacement_d3_057}


def ec_replacement_d3_058(ec_replacement_d2_058):
    feature = _clean(ec_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_058'] = {'inputs': ['ec_replacement_d2_058'], 'func': ec_replacement_d3_058}


def ec_replacement_d3_059(ec_replacement_d2_059):
    feature = _clean(ec_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_059'] = {'inputs': ['ec_replacement_d2_059'], 'func': ec_replacement_d3_059}


def ec_replacement_d3_060(ec_replacement_d2_060):
    feature = _clean(ec_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_060'] = {'inputs': ['ec_replacement_d2_060'], 'func': ec_replacement_d3_060}


def ec_replacement_d3_061(ec_replacement_d2_061):
    feature = _clean(ec_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_061'] = {'inputs': ['ec_replacement_d2_061'], 'func': ec_replacement_d3_061}


def ec_replacement_d3_062(ec_replacement_d2_062):
    feature = _clean(ec_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_062'] = {'inputs': ['ec_replacement_d2_062'], 'func': ec_replacement_d3_062}


def ec_replacement_d3_063(ec_replacement_d2_063):
    feature = _clean(ec_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_063'] = {'inputs': ['ec_replacement_d2_063'], 'func': ec_replacement_d3_063}


def ec_replacement_d3_064(ec_replacement_d2_064):
    feature = _clean(ec_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_064'] = {'inputs': ['ec_replacement_d2_064'], 'func': ec_replacement_d3_064}


def ec_replacement_d3_065(ec_replacement_d2_065):
    feature = _clean(ec_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_065'] = {'inputs': ['ec_replacement_d2_065'], 'func': ec_replacement_d3_065}


def ec_replacement_d3_066(ec_replacement_d2_066):
    feature = _clean(ec_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_066'] = {'inputs': ['ec_replacement_d2_066'], 'func': ec_replacement_d3_066}


def ec_replacement_d3_067(ec_replacement_d2_067):
    feature = _clean(ec_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_067'] = {'inputs': ['ec_replacement_d2_067'], 'func': ec_replacement_d3_067}


def ec_replacement_d3_068(ec_replacement_d2_068):
    feature = _clean(ec_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_068'] = {'inputs': ['ec_replacement_d2_068'], 'func': ec_replacement_d3_068}


def ec_replacement_d3_069(ec_replacement_d2_069):
    feature = _clean(ec_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_069'] = {'inputs': ['ec_replacement_d2_069'], 'func': ec_replacement_d3_069}


def ec_replacement_d3_070(ec_replacement_d2_070):
    feature = _clean(ec_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_070'] = {'inputs': ['ec_replacement_d2_070'], 'func': ec_replacement_d3_070}


def ec_replacement_d3_071(ec_replacement_d2_071):
    feature = _clean(ec_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_071'] = {'inputs': ['ec_replacement_d2_071'], 'func': ec_replacement_d3_071}


def ec_replacement_d3_072(ec_replacement_d2_072):
    feature = _clean(ec_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_072'] = {'inputs': ['ec_replacement_d2_072'], 'func': ec_replacement_d3_072}


def ec_replacement_d3_073(ec_replacement_d2_073):
    feature = _clean(ec_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_073'] = {'inputs': ['ec_replacement_d2_073'], 'func': ec_replacement_d3_073}


def ec_replacement_d3_074(ec_replacement_d2_074):
    feature = _clean(ec_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_074'] = {'inputs': ['ec_replacement_d2_074'], 'func': ec_replacement_d3_074}


def ec_replacement_d3_075(ec_replacement_d2_075):
    feature = _clean(ec_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_075'] = {'inputs': ['ec_replacement_d2_075'], 'func': ec_replacement_d3_075}


def ec_replacement_d3_076(ec_replacement_d2_076):
    feature = _clean(ec_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_076'] = {'inputs': ['ec_replacement_d2_076'], 'func': ec_replacement_d3_076}


def ec_replacement_d3_077(ec_replacement_d2_077):
    feature = _clean(ec_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_077'] = {'inputs': ['ec_replacement_d2_077'], 'func': ec_replacement_d3_077}


def ec_replacement_d3_078(ec_replacement_d2_078):
    feature = _clean(ec_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_078'] = {'inputs': ['ec_replacement_d2_078'], 'func': ec_replacement_d3_078}


def ec_replacement_d3_079(ec_replacement_d2_079):
    feature = _clean(ec_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_079'] = {'inputs': ['ec_replacement_d2_079'], 'func': ec_replacement_d3_079}


def ec_replacement_d3_080(ec_replacement_d2_080):
    feature = _clean(ec_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_080'] = {'inputs': ['ec_replacement_d2_080'], 'func': ec_replacement_d3_080}


def ec_replacement_d3_081(ec_replacement_d2_081):
    feature = _clean(ec_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_081'] = {'inputs': ['ec_replacement_d2_081'], 'func': ec_replacement_d3_081}


def ec_replacement_d3_082(ec_replacement_d2_082):
    feature = _clean(ec_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_082'] = {'inputs': ['ec_replacement_d2_082'], 'func': ec_replacement_d3_082}


def ec_replacement_d3_083(ec_replacement_d2_083):
    feature = _clean(ec_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_083'] = {'inputs': ['ec_replacement_d2_083'], 'func': ec_replacement_d3_083}


def ec_replacement_d3_084(ec_replacement_d2_084):
    feature = _clean(ec_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_084'] = {'inputs': ['ec_replacement_d2_084'], 'func': ec_replacement_d3_084}


def ec_replacement_d3_085(ec_replacement_d2_085):
    feature = _clean(ec_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_085'] = {'inputs': ['ec_replacement_d2_085'], 'func': ec_replacement_d3_085}


def ec_replacement_d3_086(ec_replacement_d2_086):
    feature = _clean(ec_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_086'] = {'inputs': ['ec_replacement_d2_086'], 'func': ec_replacement_d3_086}


def ec_replacement_d3_087(ec_replacement_d2_087):
    feature = _clean(ec_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_087'] = {'inputs': ['ec_replacement_d2_087'], 'func': ec_replacement_d3_087}


def ec_replacement_d3_088(ec_replacement_d2_088):
    feature = _clean(ec_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_088'] = {'inputs': ['ec_replacement_d2_088'], 'func': ec_replacement_d3_088}


def ec_replacement_d3_089(ec_replacement_d2_089):
    feature = _clean(ec_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_089'] = {'inputs': ['ec_replacement_d2_089'], 'func': ec_replacement_d3_089}


def ec_replacement_d3_090(ec_replacement_d2_090):
    feature = _clean(ec_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_090'] = {'inputs': ['ec_replacement_d2_090'], 'func': ec_replacement_d3_090}


def ec_replacement_d3_091(ec_replacement_d2_091):
    feature = _clean(ec_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_091'] = {'inputs': ['ec_replacement_d2_091'], 'func': ec_replacement_d3_091}


def ec_replacement_d3_092(ec_replacement_d2_092):
    feature = _clean(ec_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_092'] = {'inputs': ['ec_replacement_d2_092'], 'func': ec_replacement_d3_092}


def ec_replacement_d3_093(ec_replacement_d2_093):
    feature = _clean(ec_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_093'] = {'inputs': ['ec_replacement_d2_093'], 'func': ec_replacement_d3_093}


def ec_replacement_d3_094(ec_replacement_d2_094):
    feature = _clean(ec_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_094'] = {'inputs': ['ec_replacement_d2_094'], 'func': ec_replacement_d3_094}


def ec_replacement_d3_095(ec_replacement_d2_095):
    feature = _clean(ec_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_095'] = {'inputs': ['ec_replacement_d2_095'], 'func': ec_replacement_d3_095}


def ec_replacement_d3_096(ec_replacement_d2_096):
    feature = _clean(ec_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_096'] = {'inputs': ['ec_replacement_d2_096'], 'func': ec_replacement_d3_096}


def ec_replacement_d3_097(ec_replacement_d2_097):
    feature = _clean(ec_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_097'] = {'inputs': ['ec_replacement_d2_097'], 'func': ec_replacement_d3_097}


def ec_replacement_d3_098(ec_replacement_d2_098):
    feature = _clean(ec_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_098'] = {'inputs': ['ec_replacement_d2_098'], 'func': ec_replacement_d3_098}


def ec_replacement_d3_099(ec_replacement_d2_099):
    feature = _clean(ec_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_099'] = {'inputs': ['ec_replacement_d2_099'], 'func': ec_replacement_d3_099}


def ec_replacement_d3_100(ec_replacement_d2_100):
    feature = _clean(ec_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_100'] = {'inputs': ['ec_replacement_d2_100'], 'func': ec_replacement_d3_100}


def ec_replacement_d3_101(ec_replacement_d2_101):
    feature = _clean(ec_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_101'] = {'inputs': ['ec_replacement_d2_101'], 'func': ec_replacement_d3_101}


def ec_replacement_d3_102(ec_replacement_d2_102):
    feature = _clean(ec_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_102'] = {'inputs': ['ec_replacement_d2_102'], 'func': ec_replacement_d3_102}


def ec_replacement_d3_103(ec_replacement_d2_103):
    feature = _clean(ec_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_103'] = {'inputs': ['ec_replacement_d2_103'], 'func': ec_replacement_d3_103}


def ec_replacement_d3_104(ec_replacement_d2_104):
    feature = _clean(ec_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_104'] = {'inputs': ['ec_replacement_d2_104'], 'func': ec_replacement_d3_104}


def ec_replacement_d3_105(ec_replacement_d2_105):
    feature = _clean(ec_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_105'] = {'inputs': ['ec_replacement_d2_105'], 'func': ec_replacement_d3_105}


def ec_replacement_d3_106(ec_replacement_d2_106):
    feature = _clean(ec_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_106'] = {'inputs': ['ec_replacement_d2_106'], 'func': ec_replacement_d3_106}


def ec_replacement_d3_107(ec_replacement_d2_107):
    feature = _clean(ec_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_107'] = {'inputs': ['ec_replacement_d2_107'], 'func': ec_replacement_d3_107}


def ec_replacement_d3_108(ec_replacement_d2_108):
    feature = _clean(ec_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_108'] = {'inputs': ['ec_replacement_d2_108'], 'func': ec_replacement_d3_108}


def ec_replacement_d3_109(ec_replacement_d2_109):
    feature = _clean(ec_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_109'] = {'inputs': ['ec_replacement_d2_109'], 'func': ec_replacement_d3_109}


def ec_replacement_d3_110(ec_replacement_d2_110):
    feature = _clean(ec_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_110'] = {'inputs': ['ec_replacement_d2_110'], 'func': ec_replacement_d3_110}


def ec_replacement_d3_111(ec_replacement_d2_111):
    feature = _clean(ec_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_111'] = {'inputs': ['ec_replacement_d2_111'], 'func': ec_replacement_d3_111}


def ec_replacement_d3_112(ec_replacement_d2_112):
    feature = _clean(ec_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_112'] = {'inputs': ['ec_replacement_d2_112'], 'func': ec_replacement_d3_112}


def ec_replacement_d3_113(ec_replacement_d2_113):
    feature = _clean(ec_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_113'] = {'inputs': ['ec_replacement_d2_113'], 'func': ec_replacement_d3_113}


def ec_replacement_d3_114(ec_replacement_d2_114):
    feature = _clean(ec_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_114'] = {'inputs': ['ec_replacement_d2_114'], 'func': ec_replacement_d3_114}


def ec_replacement_d3_115(ec_replacement_d2_115):
    feature = _clean(ec_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_115'] = {'inputs': ['ec_replacement_d2_115'], 'func': ec_replacement_d3_115}


def ec_replacement_d3_116(ec_replacement_d2_116):
    feature = _clean(ec_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_116'] = {'inputs': ['ec_replacement_d2_116'], 'func': ec_replacement_d3_116}


def ec_replacement_d3_117(ec_replacement_d2_117):
    feature = _clean(ec_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_117'] = {'inputs': ['ec_replacement_d2_117'], 'func': ec_replacement_d3_117}


def ec_replacement_d3_118(ec_replacement_d2_118):
    feature = _clean(ec_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_118'] = {'inputs': ['ec_replacement_d2_118'], 'func': ec_replacement_d3_118}


def ec_replacement_d3_119(ec_replacement_d2_119):
    feature = _clean(ec_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_119'] = {'inputs': ['ec_replacement_d2_119'], 'func': ec_replacement_d3_119}


def ec_replacement_d3_120(ec_replacement_d2_120):
    feature = _clean(ec_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_120'] = {'inputs': ['ec_replacement_d2_120'], 'func': ec_replacement_d3_120}


def ec_replacement_d3_121(ec_replacement_d2_121):
    feature = _clean(ec_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_121'] = {'inputs': ['ec_replacement_d2_121'], 'func': ec_replacement_d3_121}


def ec_replacement_d3_122(ec_replacement_d2_122):
    feature = _clean(ec_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_122'] = {'inputs': ['ec_replacement_d2_122'], 'func': ec_replacement_d3_122}


def ec_replacement_d3_123(ec_replacement_d2_123):
    feature = _clean(ec_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_123'] = {'inputs': ['ec_replacement_d2_123'], 'func': ec_replacement_d3_123}


def ec_replacement_d3_124(ec_replacement_d2_124):
    feature = _clean(ec_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_124'] = {'inputs': ['ec_replacement_d2_124'], 'func': ec_replacement_d3_124}


def ec_replacement_d3_125(ec_replacement_d2_125):
    feature = _clean(ec_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_125'] = {'inputs': ['ec_replacement_d2_125'], 'func': ec_replacement_d3_125}


def ec_replacement_d3_126(ec_replacement_d2_126):
    feature = _clean(ec_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_126'] = {'inputs': ['ec_replacement_d2_126'], 'func': ec_replacement_d3_126}


def ec_replacement_d3_127(ec_replacement_d2_127):
    feature = _clean(ec_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_127'] = {'inputs': ['ec_replacement_d2_127'], 'func': ec_replacement_d3_127}


def ec_replacement_d3_128(ec_replacement_d2_128):
    feature = _clean(ec_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_128'] = {'inputs': ['ec_replacement_d2_128'], 'func': ec_replacement_d3_128}


def ec_replacement_d3_129(ec_replacement_d2_129):
    feature = _clean(ec_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_129'] = {'inputs': ['ec_replacement_d2_129'], 'func': ec_replacement_d3_129}


def ec_replacement_d3_130(ec_replacement_d2_130):
    feature = _clean(ec_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_130'] = {'inputs': ['ec_replacement_d2_130'], 'func': ec_replacement_d3_130}


def ec_replacement_d3_131(ec_replacement_d2_131):
    feature = _clean(ec_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_131'] = {'inputs': ['ec_replacement_d2_131'], 'func': ec_replacement_d3_131}


def ec_replacement_d3_132(ec_replacement_d2_132):
    feature = _clean(ec_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_132'] = {'inputs': ['ec_replacement_d2_132'], 'func': ec_replacement_d3_132}


def ec_replacement_d3_133(ec_replacement_d2_133):
    feature = _clean(ec_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_133'] = {'inputs': ['ec_replacement_d2_133'], 'func': ec_replacement_d3_133}


def ec_replacement_d3_134(ec_replacement_d2_134):
    feature = _clean(ec_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_134'] = {'inputs': ['ec_replacement_d2_134'], 'func': ec_replacement_d3_134}


def ec_replacement_d3_135(ec_replacement_d2_135):
    feature = _clean(ec_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_135'] = {'inputs': ['ec_replacement_d2_135'], 'func': ec_replacement_d3_135}


def ec_replacement_d3_136(ec_replacement_d2_136):
    feature = _clean(ec_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_136'] = {'inputs': ['ec_replacement_d2_136'], 'func': ec_replacement_d3_136}


def ec_replacement_d3_137(ec_replacement_d2_137):
    feature = _clean(ec_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_137'] = {'inputs': ['ec_replacement_d2_137'], 'func': ec_replacement_d3_137}


def ec_replacement_d3_138(ec_replacement_d2_138):
    feature = _clean(ec_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_138'] = {'inputs': ['ec_replacement_d2_138'], 'func': ec_replacement_d3_138}


def ec_replacement_d3_139(ec_replacement_d2_139):
    feature = _clean(ec_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_139'] = {'inputs': ['ec_replacement_d2_139'], 'func': ec_replacement_d3_139}


def ec_replacement_d3_140(ec_replacement_d2_140):
    feature = _clean(ec_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_140'] = {'inputs': ['ec_replacement_d2_140'], 'func': ec_replacement_d3_140}


def ec_replacement_d3_141(ec_replacement_d2_141):
    feature = _clean(ec_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_141'] = {'inputs': ['ec_replacement_d2_141'], 'func': ec_replacement_d3_141}


def ec_replacement_d3_142(ec_replacement_d2_142):
    feature = _clean(ec_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_142'] = {'inputs': ['ec_replacement_d2_142'], 'func': ec_replacement_d3_142}


def ec_replacement_d3_143(ec_replacement_d2_143):
    feature = _clean(ec_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_143'] = {'inputs': ['ec_replacement_d2_143'], 'func': ec_replacement_d3_143}


def ec_replacement_d3_144(ec_replacement_d2_144):
    feature = _clean(ec_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_144'] = {'inputs': ['ec_replacement_d2_144'], 'func': ec_replacement_d3_144}


def ec_replacement_d3_145(ec_replacement_d2_145):
    feature = _clean(ec_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_145'] = {'inputs': ['ec_replacement_d2_145'], 'func': ec_replacement_d3_145}


def ec_replacement_d3_146(ec_replacement_d2_146):
    feature = _clean(ec_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_146'] = {'inputs': ['ec_replacement_d2_146'], 'func': ec_replacement_d3_146}


def ec_replacement_d3_147(ec_replacement_d2_147):
    feature = _clean(ec_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_147'] = {'inputs': ['ec_replacement_d2_147'], 'func': ec_replacement_d3_147}


def ec_replacement_d3_148(ec_replacement_d2_148):
    feature = _clean(ec_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_148'] = {'inputs': ['ec_replacement_d2_148'], 'func': ec_replacement_d3_148}


def ec_replacement_d3_149(ec_replacement_d2_149):
    feature = _clean(ec_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_149'] = {'inputs': ['ec_replacement_d2_149'], 'func': ec_replacement_d3_149}


def ec_replacement_d3_150(ec_replacement_d2_150):
    feature = _clean(ec_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_150'] = {'inputs': ['ec_replacement_d2_150'], 'func': ec_replacement_d3_150}


def ec_replacement_d3_151(ec_replacement_d2_151):
    feature = _clean(ec_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_151'] = {'inputs': ['ec_replacement_d2_151'], 'func': ec_replacement_d3_151}


def ec_replacement_d3_152(ec_replacement_d2_152):
    feature = _clean(ec_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_152'] = {'inputs': ['ec_replacement_d2_152'], 'func': ec_replacement_d3_152}


def ec_replacement_d3_153(ec_replacement_d2_153):
    feature = _clean(ec_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_153'] = {'inputs': ['ec_replacement_d2_153'], 'func': ec_replacement_d3_153}


def ec_replacement_d3_154(ec_replacement_d2_154):
    feature = _clean(ec_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_154'] = {'inputs': ['ec_replacement_d2_154'], 'func': ec_replacement_d3_154}


def ec_replacement_d3_155(ec_replacement_d2_155):
    feature = _clean(ec_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_155'] = {'inputs': ['ec_replacement_d2_155'], 'func': ec_replacement_d3_155}


def ec_replacement_d3_156(ec_replacement_d2_156):
    feature = _clean(ec_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_156'] = {'inputs': ['ec_replacement_d2_156'], 'func': ec_replacement_d3_156}


def ec_replacement_d3_157(ec_replacement_d2_157):
    feature = _clean(ec_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_157'] = {'inputs': ['ec_replacement_d2_157'], 'func': ec_replacement_d3_157}


def ec_replacement_d3_158(ec_replacement_d2_158):
    feature = _clean(ec_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_158'] = {'inputs': ['ec_replacement_d2_158'], 'func': ec_replacement_d3_158}


def ec_replacement_d3_159(ec_replacement_d2_159):
    feature = _clean(ec_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_159'] = {'inputs': ['ec_replacement_d2_159'], 'func': ec_replacement_d3_159}


def ec_replacement_d3_160(ec_replacement_d2_160):
    feature = _clean(ec_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_160'] = {'inputs': ['ec_replacement_d2_160'], 'func': ec_replacement_d3_160}


def ec_replacement_d3_161(ec_replacement_d2_161):
    feature = _clean(ec_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_161'] = {'inputs': ['ec_replacement_d2_161'], 'func': ec_replacement_d3_161}


def ec_replacement_d3_162(ec_replacement_d2_162):
    feature = _clean(ec_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_162'] = {'inputs': ['ec_replacement_d2_162'], 'func': ec_replacement_d3_162}


def ec_replacement_d3_163(ec_replacement_d2_163):
    feature = _clean(ec_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_163'] = {'inputs': ['ec_replacement_d2_163'], 'func': ec_replacement_d3_163}


def ec_replacement_d3_164(ec_replacement_d2_164):
    feature = _clean(ec_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_164'] = {'inputs': ['ec_replacement_d2_164'], 'func': ec_replacement_d3_164}


def ec_replacement_d3_165(ec_replacement_d2_165):
    feature = _clean(ec_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_165'] = {'inputs': ['ec_replacement_d2_165'], 'func': ec_replacement_d3_165}


def ec_replacement_d3_166(ec_replacement_d2_166):
    feature = _clean(ec_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
EC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ec_replacement_d3_166'] = {'inputs': ['ec_replacement_d2_166'], 'func': ec_replacement_d3_166}


# Third-derivative extensions for repaired first-base features.
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def ecl_base_universe_d3_001_ecl_003_fcf_burn_to_cash_63(ecl_base_universe_d2_001_ecl_003_fcf_burn_to_cash_63):
    return _base_universe_d3(ecl_base_universe_d2_001_ecl_003_fcf_burn_to_cash_63, 1)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_001_ecl_003_fcf_burn_to_cash_63'] = {'inputs': ['ecl_base_universe_d2_001_ecl_003_fcf_burn_to_cash_63'], 'func': ecl_base_universe_d3_001_ecl_003_fcf_burn_to_cash_63}


def ecl_base_universe_d3_002_ecl_004_debt_to_equity_84(ecl_base_universe_d2_002_ecl_004_debt_to_equity_84):
    return _base_universe_d3(ecl_base_universe_d2_002_ecl_004_debt_to_equity_84, 2)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_002_ecl_004_debt_to_equity_84'] = {'inputs': ['ecl_base_universe_d2_002_ecl_004_debt_to_equity_84'], 'func': ecl_base_universe_d3_002_ecl_004_debt_to_equity_84}


def ecl_base_universe_d3_003_ecl_005_debt_to_assets_126(ecl_base_universe_d2_003_ecl_005_debt_to_assets_126):
    return _base_universe_d3(ecl_base_universe_d2_003_ecl_005_debt_to_assets_126, 3)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_003_ecl_005_debt_to_assets_126'] = {'inputs': ['ecl_base_universe_d2_003_ecl_005_debt_to_assets_126'], 'func': ecl_base_universe_d3_003_ecl_005_debt_to_assets_126}


def ecl_base_universe_d3_004_ecl_012_accrual_gap_1260(ecl_base_universe_d2_004_ecl_012_accrual_gap_1260):
    return _base_universe_d3(ecl_base_universe_d2_004_ecl_012_accrual_gap_1260, 4)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_004_ecl_012_accrual_gap_1260'] = {'inputs': ['ecl_base_universe_d2_004_ecl_012_accrual_gap_1260'], 'func': ecl_base_universe_d3_004_ecl_012_accrual_gap_1260}


def ecl_base_universe_d3_005_ecl_016_debt_to_equity_21(ecl_base_universe_d2_005_ecl_016_debt_to_equity_21):
    return _base_universe_d3(ecl_base_universe_d2_005_ecl_016_debt_to_equity_21, 5)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_005_ecl_016_debt_to_equity_21'] = {'inputs': ['ecl_base_universe_d2_005_ecl_016_debt_to_equity_21'], 'func': ecl_base_universe_d3_005_ecl_016_debt_to_equity_21}


def ecl_base_universe_d3_006_ecl_017_debt_to_assets_42(ecl_base_universe_d2_006_ecl_017_debt_to_assets_42):
    return _base_universe_d3(ecl_base_universe_d2_006_ecl_017_debt_to_assets_42, 6)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_006_ecl_017_debt_to_assets_42'] = {'inputs': ['ecl_base_universe_d2_006_ecl_017_debt_to_assets_42'], 'func': ecl_base_universe_d3_006_ecl_017_debt_to_assets_42}


def ecl_base_universe_d3_007_ecl_024_accrual_gap_504(ecl_base_universe_d2_007_ecl_024_accrual_gap_504):
    return _base_universe_d3(ecl_base_universe_d2_007_ecl_024_accrual_gap_504, 7)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_007_ecl_024_accrual_gap_504'] = {'inputs': ['ecl_base_universe_d2_007_ecl_024_accrual_gap_504'], 'func': ecl_base_universe_d3_007_ecl_024_accrual_gap_504}


def ecl_base_universe_d3_008_ecl_027_fcf_burn_to_cash_1260(ecl_base_universe_d2_008_ecl_027_fcf_burn_to_cash_1260):
    return _base_universe_d3(ecl_base_universe_d2_008_ecl_027_fcf_burn_to_cash_1260, 8)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_008_ecl_027_fcf_burn_to_cash_1260'] = {'inputs': ['ecl_base_universe_d2_008_ecl_027_fcf_burn_to_cash_1260'], 'func': ecl_base_universe_d3_008_ecl_027_fcf_burn_to_cash_1260}


def ecl_base_universe_d3_009_ecl_028_debt_to_equity_1512(ecl_base_universe_d2_009_ecl_028_debt_to_equity_1512):
    return _base_universe_d3(ecl_base_universe_d2_009_ecl_028_debt_to_equity_1512, 9)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_009_ecl_028_debt_to_equity_1512'] = {'inputs': ['ecl_base_universe_d2_009_ecl_028_debt_to_equity_1512'], 'func': ecl_base_universe_d3_009_ecl_028_debt_to_equity_1512}


def ecl_base_universe_d3_010_ecl_029_debt_to_assets_63(ecl_base_universe_d2_010_ecl_029_debt_to_assets_63):
    return _base_universe_d3(ecl_base_universe_d2_010_ecl_029_debt_to_assets_63, 10)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_010_ecl_029_debt_to_assets_63'] = {'inputs': ['ecl_base_universe_d2_010_ecl_029_debt_to_assets_63'], 'func': ecl_base_universe_d3_010_ecl_029_debt_to_assets_63}


def ecl_base_universe_d3_011_ecl_031_interest_coverage_stress_21(ecl_base_universe_d2_011_ecl_031_interest_coverage_stress_21):
    return _base_universe_d3(ecl_base_universe_d2_011_ecl_031_interest_coverage_stress_21, 11)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_011_ecl_031_interest_coverage_stress_21'] = {'inputs': ['ecl_base_universe_d2_011_ecl_031_interest_coverage_stress_21'], 'func': ecl_base_universe_d3_011_ecl_031_interest_coverage_stress_21}


def ecl_base_universe_d3_012_ecl_036_accrual_gap_189(ecl_base_universe_d2_012_ecl_036_accrual_gap_189):
    return _base_universe_d3(ecl_base_universe_d2_012_ecl_036_accrual_gap_189, 12)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_012_ecl_036_accrual_gap_189'] = {'inputs': ['ecl_base_universe_d2_012_ecl_036_accrual_gap_189'], 'func': ecl_base_universe_d3_012_ecl_036_accrual_gap_189}


def ecl_base_universe_d3_013_ecl_039_fcf_burn_to_cash_504(ecl_base_universe_d2_013_ecl_039_fcf_burn_to_cash_504):
    return _base_universe_d3(ecl_base_universe_d2_013_ecl_039_fcf_burn_to_cash_504, 13)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_013_ecl_039_fcf_burn_to_cash_504'] = {'inputs': ['ecl_base_universe_d2_013_ecl_039_fcf_burn_to_cash_504'], 'func': ecl_base_universe_d3_013_ecl_039_fcf_burn_to_cash_504}


def ecl_base_universe_d3_014_ecl_040_debt_to_equity_756(ecl_base_universe_d2_014_ecl_040_debt_to_equity_756):
    return _base_universe_d3(ecl_base_universe_d2_014_ecl_040_debt_to_equity_756, 14)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_014_ecl_040_debt_to_equity_756'] = {'inputs': ['ecl_base_universe_d2_014_ecl_040_debt_to_equity_756'], 'func': ecl_base_universe_d3_014_ecl_040_debt_to_equity_756}


def ecl_base_universe_d3_015_ecl_041_debt_to_assets_1008(ecl_base_universe_d2_015_ecl_041_debt_to_assets_1008):
    return _base_universe_d3(ecl_base_universe_d2_015_ecl_041_debt_to_assets_1008, 15)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_015_ecl_041_debt_to_assets_1008'] = {'inputs': ['ecl_base_universe_d2_015_ecl_041_debt_to_assets_1008'], 'func': ecl_base_universe_d3_015_ecl_041_debt_to_assets_1008}


def ecl_base_universe_d3_016_ecl_043_interest_coverage_stress_1512(ecl_base_universe_d2_016_ecl_043_interest_coverage_stress_1512):
    return _base_universe_d3(ecl_base_universe_d2_016_ecl_043_interest_coverage_stress_1512, 16)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_016_ecl_043_interest_coverage_stress_1512'] = {'inputs': ['ecl_base_universe_d2_016_ecl_043_interest_coverage_stress_1512'], 'func': ecl_base_universe_d3_016_ecl_043_interest_coverage_stress_1512}


def ecl_base_universe_d3_017_ecl_048_accrual_gap_63(ecl_base_universe_d2_017_ecl_048_accrual_gap_63):
    return _base_universe_d3(ecl_base_universe_d2_017_ecl_048_accrual_gap_63, 17)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_017_ecl_048_accrual_gap_63'] = {'inputs': ['ecl_base_universe_d2_017_ecl_048_accrual_gap_63'], 'func': ecl_base_universe_d3_017_ecl_048_accrual_gap_63}


def ecl_base_universe_d3_018_ecl_051_fcf_burn_to_cash_189(ecl_base_universe_d2_018_ecl_051_fcf_burn_to_cash_189):
    return _base_universe_d3(ecl_base_universe_d2_018_ecl_051_fcf_burn_to_cash_189, 18)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_018_ecl_051_fcf_burn_to_cash_189'] = {'inputs': ['ecl_base_universe_d2_018_ecl_051_fcf_burn_to_cash_189'], 'func': ecl_base_universe_d3_018_ecl_051_fcf_burn_to_cash_189}


def ecl_base_universe_d3_019_ecl_052_debt_to_equity_252(ecl_base_universe_d2_019_ecl_052_debt_to_equity_252):
    return _base_universe_d3(ecl_base_universe_d2_019_ecl_052_debt_to_equity_252, 19)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_019_ecl_052_debt_to_equity_252'] = {'inputs': ['ecl_base_universe_d2_019_ecl_052_debt_to_equity_252'], 'func': ecl_base_universe_d3_019_ecl_052_debt_to_equity_252}


def ecl_base_universe_d3_020_ecl_053_debt_to_assets_378(ecl_base_universe_d2_020_ecl_053_debt_to_assets_378):
    return _base_universe_d3(ecl_base_universe_d2_020_ecl_053_debt_to_assets_378, 20)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_020_ecl_053_debt_to_assets_378'] = {'inputs': ['ecl_base_universe_d2_020_ecl_053_debt_to_assets_378'], 'func': ecl_base_universe_d3_020_ecl_053_debt_to_assets_378}


def ecl_base_universe_d3_021_ecl_055_interest_coverage_stress_756(ecl_base_universe_d2_021_ecl_055_interest_coverage_stress_756):
    return _base_universe_d3(ecl_base_universe_d2_021_ecl_055_interest_coverage_stress_756, 21)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_021_ecl_055_interest_coverage_stress_756'] = {'inputs': ['ecl_base_universe_d2_021_ecl_055_interest_coverage_stress_756'], 'func': ecl_base_universe_d3_021_ecl_055_interest_coverage_stress_756}


def ecl_base_universe_d3_022_ecl_060_accrual_gap_252(ecl_base_universe_d2_022_ecl_060_accrual_gap_252):
    return _base_universe_d3(ecl_base_universe_d2_022_ecl_060_accrual_gap_252, 22)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_022_ecl_060_accrual_gap_252'] = {'inputs': ['ecl_base_universe_d2_022_ecl_060_accrual_gap_252'], 'func': ecl_base_universe_d3_022_ecl_060_accrual_gap_252}


def ecl_base_universe_d3_023_ecl_basefill_001(ecl_base_universe_d2_023_ecl_basefill_001):
    return _base_universe_d3(ecl_base_universe_d2_023_ecl_basefill_001, 23)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_023_ecl_basefill_001'] = {'inputs': ['ecl_base_universe_d2_023_ecl_basefill_001'], 'func': ecl_base_universe_d3_023_ecl_basefill_001}


def ecl_base_universe_d3_024_ecl_basefill_002(ecl_base_universe_d2_024_ecl_basefill_002):
    return _base_universe_d3(ecl_base_universe_d2_024_ecl_basefill_002, 24)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_024_ecl_basefill_002'] = {'inputs': ['ecl_base_universe_d2_024_ecl_basefill_002'], 'func': ecl_base_universe_d3_024_ecl_basefill_002}


def ecl_base_universe_d3_025_ecl_basefill_006(ecl_base_universe_d2_025_ecl_basefill_006):
    return _base_universe_d3(ecl_base_universe_d2_025_ecl_basefill_006, 25)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_025_ecl_basefill_006'] = {'inputs': ['ecl_base_universe_d2_025_ecl_basefill_006'], 'func': ecl_base_universe_d3_025_ecl_basefill_006}


def ecl_base_universe_d3_026_ecl_basefill_008(ecl_base_universe_d2_026_ecl_basefill_008):
    return _base_universe_d3(ecl_base_universe_d2_026_ecl_basefill_008, 26)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_026_ecl_basefill_008'] = {'inputs': ['ecl_base_universe_d2_026_ecl_basefill_008'], 'func': ecl_base_universe_d3_026_ecl_basefill_008}


def ecl_base_universe_d3_027_ecl_basefill_009(ecl_base_universe_d2_027_ecl_basefill_009):
    return _base_universe_d3(ecl_base_universe_d2_027_ecl_basefill_009, 27)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_027_ecl_basefill_009'] = {'inputs': ['ecl_base_universe_d2_027_ecl_basefill_009'], 'func': ecl_base_universe_d3_027_ecl_basefill_009}


def ecl_base_universe_d3_028_ecl_basefill_010(ecl_base_universe_d2_028_ecl_basefill_010):
    return _base_universe_d3(ecl_base_universe_d2_028_ecl_basefill_010, 28)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_028_ecl_basefill_010'] = {'inputs': ['ecl_base_universe_d2_028_ecl_basefill_010'], 'func': ecl_base_universe_d3_028_ecl_basefill_010}


def ecl_base_universe_d3_029_ecl_basefill_011(ecl_base_universe_d2_029_ecl_basefill_011):
    return _base_universe_d3(ecl_base_universe_d2_029_ecl_basefill_011, 29)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_029_ecl_basefill_011'] = {'inputs': ['ecl_base_universe_d2_029_ecl_basefill_011'], 'func': ecl_base_universe_d3_029_ecl_basefill_011}


def ecl_base_universe_d3_030_ecl_basefill_013(ecl_base_universe_d2_030_ecl_basefill_013):
    return _base_universe_d3(ecl_base_universe_d2_030_ecl_basefill_013, 30)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_030_ecl_basefill_013'] = {'inputs': ['ecl_base_universe_d2_030_ecl_basefill_013'], 'func': ecl_base_universe_d3_030_ecl_basefill_013}


def ecl_base_universe_d3_031_ecl_basefill_014(ecl_base_universe_d2_031_ecl_basefill_014):
    return _base_universe_d3(ecl_base_universe_d2_031_ecl_basefill_014, 31)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_031_ecl_basefill_014'] = {'inputs': ['ecl_base_universe_d2_031_ecl_basefill_014'], 'func': ecl_base_universe_d3_031_ecl_basefill_014}


def ecl_base_universe_d3_032_ecl_basefill_015(ecl_base_universe_d2_032_ecl_basefill_015):
    return _base_universe_d3(ecl_base_universe_d2_032_ecl_basefill_015, 32)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_032_ecl_basefill_015'] = {'inputs': ['ecl_base_universe_d2_032_ecl_basefill_015'], 'func': ecl_base_universe_d3_032_ecl_basefill_015}


def ecl_base_universe_d3_033_ecl_basefill_018(ecl_base_universe_d2_033_ecl_basefill_018):
    return _base_universe_d3(ecl_base_universe_d2_033_ecl_basefill_018, 33)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_033_ecl_basefill_018'] = {'inputs': ['ecl_base_universe_d2_033_ecl_basefill_018'], 'func': ecl_base_universe_d3_033_ecl_basefill_018}


def ecl_base_universe_d3_034_ecl_basefill_020(ecl_base_universe_d2_034_ecl_basefill_020):
    return _base_universe_d3(ecl_base_universe_d2_034_ecl_basefill_020, 34)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_034_ecl_basefill_020'] = {'inputs': ['ecl_base_universe_d2_034_ecl_basefill_020'], 'func': ecl_base_universe_d3_034_ecl_basefill_020}


def ecl_base_universe_d3_035_ecl_basefill_021(ecl_base_universe_d2_035_ecl_basefill_021):
    return _base_universe_d3(ecl_base_universe_d2_035_ecl_basefill_021, 35)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_035_ecl_basefill_021'] = {'inputs': ['ecl_base_universe_d2_035_ecl_basefill_021'], 'func': ecl_base_universe_d3_035_ecl_basefill_021}


def ecl_base_universe_d3_036_ecl_basefill_022(ecl_base_universe_d2_036_ecl_basefill_022):
    return _base_universe_d3(ecl_base_universe_d2_036_ecl_basefill_022, 36)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_036_ecl_basefill_022'] = {'inputs': ['ecl_base_universe_d2_036_ecl_basefill_022'], 'func': ecl_base_universe_d3_036_ecl_basefill_022}


def ecl_base_universe_d3_037_ecl_basefill_023(ecl_base_universe_d2_037_ecl_basefill_023):
    return _base_universe_d3(ecl_base_universe_d2_037_ecl_basefill_023, 37)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_037_ecl_basefill_023'] = {'inputs': ['ecl_base_universe_d2_037_ecl_basefill_023'], 'func': ecl_base_universe_d3_037_ecl_basefill_023}


def ecl_base_universe_d3_038_ecl_basefill_025(ecl_base_universe_d2_038_ecl_basefill_025):
    return _base_universe_d3(ecl_base_universe_d2_038_ecl_basefill_025, 38)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_038_ecl_basefill_025'] = {'inputs': ['ecl_base_universe_d2_038_ecl_basefill_025'], 'func': ecl_base_universe_d3_038_ecl_basefill_025}


def ecl_base_universe_d3_039_ecl_basefill_026(ecl_base_universe_d2_039_ecl_basefill_026):
    return _base_universe_d3(ecl_base_universe_d2_039_ecl_basefill_026, 39)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_039_ecl_basefill_026'] = {'inputs': ['ecl_base_universe_d2_039_ecl_basefill_026'], 'func': ecl_base_universe_d3_039_ecl_basefill_026}


def ecl_base_universe_d3_040_ecl_basefill_030(ecl_base_universe_d2_040_ecl_basefill_030):
    return _base_universe_d3(ecl_base_universe_d2_040_ecl_basefill_030, 40)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_040_ecl_basefill_030'] = {'inputs': ['ecl_base_universe_d2_040_ecl_basefill_030'], 'func': ecl_base_universe_d3_040_ecl_basefill_030}


def ecl_base_universe_d3_041_ecl_basefill_032(ecl_base_universe_d2_041_ecl_basefill_032):
    return _base_universe_d3(ecl_base_universe_d2_041_ecl_basefill_032, 41)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_041_ecl_basefill_032'] = {'inputs': ['ecl_base_universe_d2_041_ecl_basefill_032'], 'func': ecl_base_universe_d3_041_ecl_basefill_032}


def ecl_base_universe_d3_042_ecl_basefill_033(ecl_base_universe_d2_042_ecl_basefill_033):
    return _base_universe_d3(ecl_base_universe_d2_042_ecl_basefill_033, 42)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_042_ecl_basefill_033'] = {'inputs': ['ecl_base_universe_d2_042_ecl_basefill_033'], 'func': ecl_base_universe_d3_042_ecl_basefill_033}


def ecl_base_universe_d3_043_ecl_basefill_034(ecl_base_universe_d2_043_ecl_basefill_034):
    return _base_universe_d3(ecl_base_universe_d2_043_ecl_basefill_034, 43)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_043_ecl_basefill_034'] = {'inputs': ['ecl_base_universe_d2_043_ecl_basefill_034'], 'func': ecl_base_universe_d3_043_ecl_basefill_034}


def ecl_base_universe_d3_044_ecl_basefill_035(ecl_base_universe_d2_044_ecl_basefill_035):
    return _base_universe_d3(ecl_base_universe_d2_044_ecl_basefill_035, 44)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_044_ecl_basefill_035'] = {'inputs': ['ecl_base_universe_d2_044_ecl_basefill_035'], 'func': ecl_base_universe_d3_044_ecl_basefill_035}


def ecl_base_universe_d3_045_ecl_basefill_037(ecl_base_universe_d2_045_ecl_basefill_037):
    return _base_universe_d3(ecl_base_universe_d2_045_ecl_basefill_037, 45)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_045_ecl_basefill_037'] = {'inputs': ['ecl_base_universe_d2_045_ecl_basefill_037'], 'func': ecl_base_universe_d3_045_ecl_basefill_037}


def ecl_base_universe_d3_046_ecl_basefill_038(ecl_base_universe_d2_046_ecl_basefill_038):
    return _base_universe_d3(ecl_base_universe_d2_046_ecl_basefill_038, 46)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_046_ecl_basefill_038'] = {'inputs': ['ecl_base_universe_d2_046_ecl_basefill_038'], 'func': ecl_base_universe_d3_046_ecl_basefill_038}


def ecl_base_universe_d3_047_ecl_basefill_042(ecl_base_universe_d2_047_ecl_basefill_042):
    return _base_universe_d3(ecl_base_universe_d2_047_ecl_basefill_042, 47)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_047_ecl_basefill_042'] = {'inputs': ['ecl_base_universe_d2_047_ecl_basefill_042'], 'func': ecl_base_universe_d3_047_ecl_basefill_042}


def ecl_base_universe_d3_048_ecl_basefill_044(ecl_base_universe_d2_048_ecl_basefill_044):
    return _base_universe_d3(ecl_base_universe_d2_048_ecl_basefill_044, 48)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_048_ecl_basefill_044'] = {'inputs': ['ecl_base_universe_d2_048_ecl_basefill_044'], 'func': ecl_base_universe_d3_048_ecl_basefill_044}


def ecl_base_universe_d3_049_ecl_basefill_045(ecl_base_universe_d2_049_ecl_basefill_045):
    return _base_universe_d3(ecl_base_universe_d2_049_ecl_basefill_045, 49)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_049_ecl_basefill_045'] = {'inputs': ['ecl_base_universe_d2_049_ecl_basefill_045'], 'func': ecl_base_universe_d3_049_ecl_basefill_045}


def ecl_base_universe_d3_050_ecl_basefill_046(ecl_base_universe_d2_050_ecl_basefill_046):
    return _base_universe_d3(ecl_base_universe_d2_050_ecl_basefill_046, 50)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_050_ecl_basefill_046'] = {'inputs': ['ecl_base_universe_d2_050_ecl_basefill_046'], 'func': ecl_base_universe_d3_050_ecl_basefill_046}


def ecl_base_universe_d3_051_ecl_basefill_047(ecl_base_universe_d2_051_ecl_basefill_047):
    return _base_universe_d3(ecl_base_universe_d2_051_ecl_basefill_047, 51)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_051_ecl_basefill_047'] = {'inputs': ['ecl_base_universe_d2_051_ecl_basefill_047'], 'func': ecl_base_universe_d3_051_ecl_basefill_047}


def ecl_base_universe_d3_052_ecl_basefill_049(ecl_base_universe_d2_052_ecl_basefill_049):
    return _base_universe_d3(ecl_base_universe_d2_052_ecl_basefill_049, 52)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_052_ecl_basefill_049'] = {'inputs': ['ecl_base_universe_d2_052_ecl_basefill_049'], 'func': ecl_base_universe_d3_052_ecl_basefill_049}


def ecl_base_universe_d3_053_ecl_basefill_050(ecl_base_universe_d2_053_ecl_basefill_050):
    return _base_universe_d3(ecl_base_universe_d2_053_ecl_basefill_050, 53)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_053_ecl_basefill_050'] = {'inputs': ['ecl_base_universe_d2_053_ecl_basefill_050'], 'func': ecl_base_universe_d3_053_ecl_basefill_050}


def ecl_base_universe_d3_054_ecl_basefill_054(ecl_base_universe_d2_054_ecl_basefill_054):
    return _base_universe_d3(ecl_base_universe_d2_054_ecl_basefill_054, 54)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_054_ecl_basefill_054'] = {'inputs': ['ecl_base_universe_d2_054_ecl_basefill_054'], 'func': ecl_base_universe_d3_054_ecl_basefill_054}


def ecl_base_universe_d3_055_ecl_basefill_056(ecl_base_universe_d2_055_ecl_basefill_056):
    return _base_universe_d3(ecl_base_universe_d2_055_ecl_basefill_056, 55)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_055_ecl_basefill_056'] = {'inputs': ['ecl_base_universe_d2_055_ecl_basefill_056'], 'func': ecl_base_universe_d3_055_ecl_basefill_056}


def ecl_base_universe_d3_056_ecl_basefill_057(ecl_base_universe_d2_056_ecl_basefill_057):
    return _base_universe_d3(ecl_base_universe_d2_056_ecl_basefill_057, 56)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_056_ecl_basefill_057'] = {'inputs': ['ecl_base_universe_d2_056_ecl_basefill_057'], 'func': ecl_base_universe_d3_056_ecl_basefill_057}


def ecl_base_universe_d3_057_ecl_basefill_058(ecl_base_universe_d2_057_ecl_basefill_058):
    return _base_universe_d3(ecl_base_universe_d2_057_ecl_basefill_058, 57)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_057_ecl_basefill_058'] = {'inputs': ['ecl_base_universe_d2_057_ecl_basefill_058'], 'func': ecl_base_universe_d3_057_ecl_basefill_058}


def ecl_base_universe_d3_058_ecl_basefill_059(ecl_base_universe_d2_058_ecl_basefill_059):
    return _base_universe_d3(ecl_base_universe_d2_058_ecl_basefill_059, 58)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_058_ecl_basefill_059'] = {'inputs': ['ecl_base_universe_d2_058_ecl_basefill_059'], 'func': ecl_base_universe_d3_058_ecl_basefill_059}


def ecl_base_universe_d3_059_ecl_basefill_061(ecl_base_universe_d2_059_ecl_basefill_061):
    return _base_universe_d3(ecl_base_universe_d2_059_ecl_basefill_061, 59)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_059_ecl_basefill_061'] = {'inputs': ['ecl_base_universe_d2_059_ecl_basefill_061'], 'func': ecl_base_universe_d3_059_ecl_basefill_061}


def ecl_base_universe_d3_060_ecl_basefill_062(ecl_base_universe_d2_060_ecl_basefill_062):
    return _base_universe_d3(ecl_base_universe_d2_060_ecl_basefill_062, 60)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_060_ecl_basefill_062'] = {'inputs': ['ecl_base_universe_d2_060_ecl_basefill_062'], 'func': ecl_base_universe_d3_060_ecl_basefill_062}


def ecl_base_universe_d3_061_ecl_basefill_063(ecl_base_universe_d2_061_ecl_basefill_063):
    return _base_universe_d3(ecl_base_universe_d2_061_ecl_basefill_063, 61)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_061_ecl_basefill_063'] = {'inputs': ['ecl_base_universe_d2_061_ecl_basefill_063'], 'func': ecl_base_universe_d3_061_ecl_basefill_063}


def ecl_base_universe_d3_062_ecl_basefill_064(ecl_base_universe_d2_062_ecl_basefill_064):
    return _base_universe_d3(ecl_base_universe_d2_062_ecl_basefill_064, 62)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_062_ecl_basefill_064'] = {'inputs': ['ecl_base_universe_d2_062_ecl_basefill_064'], 'func': ecl_base_universe_d3_062_ecl_basefill_064}


def ecl_base_universe_d3_063_ecl_basefill_065(ecl_base_universe_d2_063_ecl_basefill_065):
    return _base_universe_d3(ecl_base_universe_d2_063_ecl_basefill_065, 63)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_063_ecl_basefill_065'] = {'inputs': ['ecl_base_universe_d2_063_ecl_basefill_065'], 'func': ecl_base_universe_d3_063_ecl_basefill_065}


def ecl_base_universe_d3_064_ecl_basefill_066(ecl_base_universe_d2_064_ecl_basefill_066):
    return _base_universe_d3(ecl_base_universe_d2_064_ecl_basefill_066, 64)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_064_ecl_basefill_066'] = {'inputs': ['ecl_base_universe_d2_064_ecl_basefill_066'], 'func': ecl_base_universe_d3_064_ecl_basefill_066}


def ecl_base_universe_d3_065_ecl_basefill_067(ecl_base_universe_d2_065_ecl_basefill_067):
    return _base_universe_d3(ecl_base_universe_d2_065_ecl_basefill_067, 65)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_065_ecl_basefill_067'] = {'inputs': ['ecl_base_universe_d2_065_ecl_basefill_067'], 'func': ecl_base_universe_d3_065_ecl_basefill_067}


def ecl_base_universe_d3_066_ecl_basefill_068(ecl_base_universe_d2_066_ecl_basefill_068):
    return _base_universe_d3(ecl_base_universe_d2_066_ecl_basefill_068, 66)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_066_ecl_basefill_068'] = {'inputs': ['ecl_base_universe_d2_066_ecl_basefill_068'], 'func': ecl_base_universe_d3_066_ecl_basefill_068}


def ecl_base_universe_d3_067_ecl_basefill_069(ecl_base_universe_d2_067_ecl_basefill_069):
    return _base_universe_d3(ecl_base_universe_d2_067_ecl_basefill_069, 67)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_067_ecl_basefill_069'] = {'inputs': ['ecl_base_universe_d2_067_ecl_basefill_069'], 'func': ecl_base_universe_d3_067_ecl_basefill_069}


def ecl_base_universe_d3_068_ecl_basefill_070(ecl_base_universe_d2_068_ecl_basefill_070):
    return _base_universe_d3(ecl_base_universe_d2_068_ecl_basefill_070, 68)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_068_ecl_basefill_070'] = {'inputs': ['ecl_base_universe_d2_068_ecl_basefill_070'], 'func': ecl_base_universe_d3_068_ecl_basefill_070}


def ecl_base_universe_d3_069_ecl_basefill_071(ecl_base_universe_d2_069_ecl_basefill_071):
    return _base_universe_d3(ecl_base_universe_d2_069_ecl_basefill_071, 69)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_069_ecl_basefill_071'] = {'inputs': ['ecl_base_universe_d2_069_ecl_basefill_071'], 'func': ecl_base_universe_d3_069_ecl_basefill_071}


def ecl_base_universe_d3_070_ecl_basefill_072(ecl_base_universe_d2_070_ecl_basefill_072):
    return _base_universe_d3(ecl_base_universe_d2_070_ecl_basefill_072, 70)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_070_ecl_basefill_072'] = {'inputs': ['ecl_base_universe_d2_070_ecl_basefill_072'], 'func': ecl_base_universe_d3_070_ecl_basefill_072}


def ecl_base_universe_d3_071_ecl_basefill_073(ecl_base_universe_d2_071_ecl_basefill_073):
    return _base_universe_d3(ecl_base_universe_d2_071_ecl_basefill_073, 71)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_071_ecl_basefill_073'] = {'inputs': ['ecl_base_universe_d2_071_ecl_basefill_073'], 'func': ecl_base_universe_d3_071_ecl_basefill_073}


def ecl_base_universe_d3_072_ecl_basefill_074(ecl_base_universe_d2_072_ecl_basefill_074):
    return _base_universe_d3(ecl_base_universe_d2_072_ecl_basefill_074, 72)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_072_ecl_basefill_074'] = {'inputs': ['ecl_base_universe_d2_072_ecl_basefill_074'], 'func': ecl_base_universe_d3_072_ecl_basefill_074}


def ecl_base_universe_d3_073_ecl_basefill_075(ecl_base_universe_d2_073_ecl_basefill_075):
    return _base_universe_d3(ecl_base_universe_d2_073_ecl_basefill_075, 73)
ECL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ecl_base_universe_d3_073_ecl_basefill_075'] = {'inputs': ['ecl_base_universe_d2_073_ecl_basefill_075'], 'func': ecl_base_universe_d3_073_ecl_basefill_075}
