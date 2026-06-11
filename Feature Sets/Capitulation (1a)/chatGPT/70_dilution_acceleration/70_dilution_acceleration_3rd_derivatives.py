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



def dla_176_dla_001_netinc_decline_1_accel_1(dla_151_dla_001_netinc_decline_1_roc_1):
    feature = _s(dla_151_dla_001_netinc_decline_1_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def dla_177_dla_007_interest_coverage_stress_252_accel_42(dla_152_dla_007_interest_coverage_stress_252_roc_42):
    feature = _s(dla_152_dla_007_interest_coverage_stress_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def dla_178_dla_013_netinc_decline_1_accel_126(dla_153_dla_013_netinc_decline_1_roc_126):
    feature = _s(dla_153_dla_013_netinc_decline_1_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def dla_179_dla_019_interest_coverage_stress_84_accel_378(dla_154_dla_019_interest_coverage_stress_84_roc_378):
    feature = _s(dla_154_dla_019_interest_coverage_stress_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def dla_180_dla_025_netinc_decline_1_accel_4(dla_155_dla_025_netinc_decline_1_roc_4):
    feature = _s(dla_155_dla_025_netinc_decline_1_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















DILUTION_ACCELERATION_REGISTRY_3RD_DERIVATIVES = {
    'dla_176_dla_001_netinc_decline_1_accel_1': {'inputs': ['dla_151_dla_001_netinc_decline_1_roc_1'], 'func': dla_176_dla_001_netinc_decline_1_accel_1},
    'dla_177_dla_007_interest_coverage_stress_252_accel_42': {'inputs': ['dla_152_dla_007_interest_coverage_stress_252_roc_42'], 'func': dla_177_dla_007_interest_coverage_stress_252_accel_42},
    'dla_178_dla_013_netinc_decline_1_accel_126': {'inputs': ['dla_153_dla_013_netinc_decline_1_roc_126'], 'func': dla_178_dla_013_netinc_decline_1_accel_126},
    'dla_179_dla_019_interest_coverage_stress_84_accel_378': {'inputs': ['dla_154_dla_019_interest_coverage_stress_84_roc_378'], 'func': dla_179_dla_019_interest_coverage_stress_84_accel_378},
    'dla_180_dla_025_netinc_decline_1_accel_4': {'inputs': ['dla_155_dla_025_netinc_decline_1_roc_4'], 'func': dla_180_dla_025_netinc_decline_1_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def da_replacement_d3_001(da_replacement_d2_001):
    feature = _clean(da_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_001'] = {'inputs': ['da_replacement_d2_001'], 'func': da_replacement_d3_001}


def da_replacement_d3_002(da_replacement_d2_002):
    feature = _clean(da_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_002'] = {'inputs': ['da_replacement_d2_002'], 'func': da_replacement_d3_002}


def da_replacement_d3_003(da_replacement_d2_003):
    feature = _clean(da_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_003'] = {'inputs': ['da_replacement_d2_003'], 'func': da_replacement_d3_003}


def da_replacement_d3_004(da_replacement_d2_004):
    feature = _clean(da_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_004'] = {'inputs': ['da_replacement_d2_004'], 'func': da_replacement_d3_004}


def da_replacement_d3_005(da_replacement_d2_005):
    feature = _clean(da_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_005'] = {'inputs': ['da_replacement_d2_005'], 'func': da_replacement_d3_005}


def da_replacement_d3_006(da_replacement_d2_006):
    feature = _clean(da_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_006'] = {'inputs': ['da_replacement_d2_006'], 'func': da_replacement_d3_006}


def da_replacement_d3_007(da_replacement_d2_007):
    feature = _clean(da_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_007'] = {'inputs': ['da_replacement_d2_007'], 'func': da_replacement_d3_007}


def da_replacement_d3_008(da_replacement_d2_008):
    feature = _clean(da_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_008'] = {'inputs': ['da_replacement_d2_008'], 'func': da_replacement_d3_008}


def da_replacement_d3_009(da_replacement_d2_009):
    feature = _clean(da_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_009'] = {'inputs': ['da_replacement_d2_009'], 'func': da_replacement_d3_009}


def da_replacement_d3_010(da_replacement_d2_010):
    feature = _clean(da_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_010'] = {'inputs': ['da_replacement_d2_010'], 'func': da_replacement_d3_010}


def da_replacement_d3_011(da_replacement_d2_011):
    feature = _clean(da_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_011'] = {'inputs': ['da_replacement_d2_011'], 'func': da_replacement_d3_011}


def da_replacement_d3_012(da_replacement_d2_012):
    feature = _clean(da_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_012'] = {'inputs': ['da_replacement_d2_012'], 'func': da_replacement_d3_012}


def da_replacement_d3_013(da_replacement_d2_013):
    feature = _clean(da_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_013'] = {'inputs': ['da_replacement_d2_013'], 'func': da_replacement_d3_013}


def da_replacement_d3_014(da_replacement_d2_014):
    feature = _clean(da_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_014'] = {'inputs': ['da_replacement_d2_014'], 'func': da_replacement_d3_014}


def da_replacement_d3_015(da_replacement_d2_015):
    feature = _clean(da_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_015'] = {'inputs': ['da_replacement_d2_015'], 'func': da_replacement_d3_015}


def da_replacement_d3_016(da_replacement_d2_016):
    feature = _clean(da_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_016'] = {'inputs': ['da_replacement_d2_016'], 'func': da_replacement_d3_016}


def da_replacement_d3_017(da_replacement_d2_017):
    feature = _clean(da_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_017'] = {'inputs': ['da_replacement_d2_017'], 'func': da_replacement_d3_017}


def da_replacement_d3_018(da_replacement_d2_018):
    feature = _clean(da_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_018'] = {'inputs': ['da_replacement_d2_018'], 'func': da_replacement_d3_018}


def da_replacement_d3_019(da_replacement_d2_019):
    feature = _clean(da_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_019'] = {'inputs': ['da_replacement_d2_019'], 'func': da_replacement_d3_019}


def da_replacement_d3_020(da_replacement_d2_020):
    feature = _clean(da_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_020'] = {'inputs': ['da_replacement_d2_020'], 'func': da_replacement_d3_020}


def da_replacement_d3_021(da_replacement_d2_021):
    feature = _clean(da_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_021'] = {'inputs': ['da_replacement_d2_021'], 'func': da_replacement_d3_021}


def da_replacement_d3_022(da_replacement_d2_022):
    feature = _clean(da_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_022'] = {'inputs': ['da_replacement_d2_022'], 'func': da_replacement_d3_022}


def da_replacement_d3_023(da_replacement_d2_023):
    feature = _clean(da_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_023'] = {'inputs': ['da_replacement_d2_023'], 'func': da_replacement_d3_023}


def da_replacement_d3_024(da_replacement_d2_024):
    feature = _clean(da_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_024'] = {'inputs': ['da_replacement_d2_024'], 'func': da_replacement_d3_024}


def da_replacement_d3_025(da_replacement_d2_025):
    feature = _clean(da_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_025'] = {'inputs': ['da_replacement_d2_025'], 'func': da_replacement_d3_025}


def da_replacement_d3_026(da_replacement_d2_026):
    feature = _clean(da_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_026'] = {'inputs': ['da_replacement_d2_026'], 'func': da_replacement_d3_026}


def da_replacement_d3_027(da_replacement_d2_027):
    feature = _clean(da_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_027'] = {'inputs': ['da_replacement_d2_027'], 'func': da_replacement_d3_027}


def da_replacement_d3_028(da_replacement_d2_028):
    feature = _clean(da_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_028'] = {'inputs': ['da_replacement_d2_028'], 'func': da_replacement_d3_028}


def da_replacement_d3_029(da_replacement_d2_029):
    feature = _clean(da_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_029'] = {'inputs': ['da_replacement_d2_029'], 'func': da_replacement_d3_029}


def da_replacement_d3_030(da_replacement_d2_030):
    feature = _clean(da_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_030'] = {'inputs': ['da_replacement_d2_030'], 'func': da_replacement_d3_030}


def da_replacement_d3_031(da_replacement_d2_031):
    feature = _clean(da_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_031'] = {'inputs': ['da_replacement_d2_031'], 'func': da_replacement_d3_031}


def da_replacement_d3_032(da_replacement_d2_032):
    feature = _clean(da_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_032'] = {'inputs': ['da_replacement_d2_032'], 'func': da_replacement_d3_032}


def da_replacement_d3_033(da_replacement_d2_033):
    feature = _clean(da_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_033'] = {'inputs': ['da_replacement_d2_033'], 'func': da_replacement_d3_033}


def da_replacement_d3_034(da_replacement_d2_034):
    feature = _clean(da_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_034'] = {'inputs': ['da_replacement_d2_034'], 'func': da_replacement_d3_034}


def da_replacement_d3_035(da_replacement_d2_035):
    feature = _clean(da_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_035'] = {'inputs': ['da_replacement_d2_035'], 'func': da_replacement_d3_035}


def da_replacement_d3_036(da_replacement_d2_036):
    feature = _clean(da_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_036'] = {'inputs': ['da_replacement_d2_036'], 'func': da_replacement_d3_036}


def da_replacement_d3_037(da_replacement_d2_037):
    feature = _clean(da_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_037'] = {'inputs': ['da_replacement_d2_037'], 'func': da_replacement_d3_037}


def da_replacement_d3_038(da_replacement_d2_038):
    feature = _clean(da_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_038'] = {'inputs': ['da_replacement_d2_038'], 'func': da_replacement_d3_038}


def da_replacement_d3_039(da_replacement_d2_039):
    feature = _clean(da_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_039'] = {'inputs': ['da_replacement_d2_039'], 'func': da_replacement_d3_039}


def da_replacement_d3_040(da_replacement_d2_040):
    feature = _clean(da_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_040'] = {'inputs': ['da_replacement_d2_040'], 'func': da_replacement_d3_040}


def da_replacement_d3_041(da_replacement_d2_041):
    feature = _clean(da_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_041'] = {'inputs': ['da_replacement_d2_041'], 'func': da_replacement_d3_041}


def da_replacement_d3_042(da_replacement_d2_042):
    feature = _clean(da_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_042'] = {'inputs': ['da_replacement_d2_042'], 'func': da_replacement_d3_042}


def da_replacement_d3_043(da_replacement_d2_043):
    feature = _clean(da_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_043'] = {'inputs': ['da_replacement_d2_043'], 'func': da_replacement_d3_043}


def da_replacement_d3_044(da_replacement_d2_044):
    feature = _clean(da_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_044'] = {'inputs': ['da_replacement_d2_044'], 'func': da_replacement_d3_044}


def da_replacement_d3_045(da_replacement_d2_045):
    feature = _clean(da_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_045'] = {'inputs': ['da_replacement_d2_045'], 'func': da_replacement_d3_045}


def da_replacement_d3_046(da_replacement_d2_046):
    feature = _clean(da_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_046'] = {'inputs': ['da_replacement_d2_046'], 'func': da_replacement_d3_046}


def da_replacement_d3_047(da_replacement_d2_047):
    feature = _clean(da_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_047'] = {'inputs': ['da_replacement_d2_047'], 'func': da_replacement_d3_047}


def da_replacement_d3_048(da_replacement_d2_048):
    feature = _clean(da_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_048'] = {'inputs': ['da_replacement_d2_048'], 'func': da_replacement_d3_048}


def da_replacement_d3_049(da_replacement_d2_049):
    feature = _clean(da_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_049'] = {'inputs': ['da_replacement_d2_049'], 'func': da_replacement_d3_049}


def da_replacement_d3_050(da_replacement_d2_050):
    feature = _clean(da_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_050'] = {'inputs': ['da_replacement_d2_050'], 'func': da_replacement_d3_050}


def da_replacement_d3_051(da_replacement_d2_051):
    feature = _clean(da_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_051'] = {'inputs': ['da_replacement_d2_051'], 'func': da_replacement_d3_051}


def da_replacement_d3_052(da_replacement_d2_052):
    feature = _clean(da_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_052'] = {'inputs': ['da_replacement_d2_052'], 'func': da_replacement_d3_052}


def da_replacement_d3_053(da_replacement_d2_053):
    feature = _clean(da_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_053'] = {'inputs': ['da_replacement_d2_053'], 'func': da_replacement_d3_053}


def da_replacement_d3_054(da_replacement_d2_054):
    feature = _clean(da_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_054'] = {'inputs': ['da_replacement_d2_054'], 'func': da_replacement_d3_054}


def da_replacement_d3_055(da_replacement_d2_055):
    feature = _clean(da_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_055'] = {'inputs': ['da_replacement_d2_055'], 'func': da_replacement_d3_055}


def da_replacement_d3_056(da_replacement_d2_056):
    feature = _clean(da_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_056'] = {'inputs': ['da_replacement_d2_056'], 'func': da_replacement_d3_056}


def da_replacement_d3_057(da_replacement_d2_057):
    feature = _clean(da_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_057'] = {'inputs': ['da_replacement_d2_057'], 'func': da_replacement_d3_057}


def da_replacement_d3_058(da_replacement_d2_058):
    feature = _clean(da_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_058'] = {'inputs': ['da_replacement_d2_058'], 'func': da_replacement_d3_058}


def da_replacement_d3_059(da_replacement_d2_059):
    feature = _clean(da_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_059'] = {'inputs': ['da_replacement_d2_059'], 'func': da_replacement_d3_059}


def da_replacement_d3_060(da_replacement_d2_060):
    feature = _clean(da_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_060'] = {'inputs': ['da_replacement_d2_060'], 'func': da_replacement_d3_060}


def da_replacement_d3_061(da_replacement_d2_061):
    feature = _clean(da_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_061'] = {'inputs': ['da_replacement_d2_061'], 'func': da_replacement_d3_061}


def da_replacement_d3_062(da_replacement_d2_062):
    feature = _clean(da_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_062'] = {'inputs': ['da_replacement_d2_062'], 'func': da_replacement_d3_062}


def da_replacement_d3_063(da_replacement_d2_063):
    feature = _clean(da_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_063'] = {'inputs': ['da_replacement_d2_063'], 'func': da_replacement_d3_063}


def da_replacement_d3_064(da_replacement_d2_064):
    feature = _clean(da_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_064'] = {'inputs': ['da_replacement_d2_064'], 'func': da_replacement_d3_064}


def da_replacement_d3_065(da_replacement_d2_065):
    feature = _clean(da_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_065'] = {'inputs': ['da_replacement_d2_065'], 'func': da_replacement_d3_065}


def da_replacement_d3_066(da_replacement_d2_066):
    feature = _clean(da_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_066'] = {'inputs': ['da_replacement_d2_066'], 'func': da_replacement_d3_066}


def da_replacement_d3_067(da_replacement_d2_067):
    feature = _clean(da_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_067'] = {'inputs': ['da_replacement_d2_067'], 'func': da_replacement_d3_067}


def da_replacement_d3_068(da_replacement_d2_068):
    feature = _clean(da_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_068'] = {'inputs': ['da_replacement_d2_068'], 'func': da_replacement_d3_068}


def da_replacement_d3_069(da_replacement_d2_069):
    feature = _clean(da_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_069'] = {'inputs': ['da_replacement_d2_069'], 'func': da_replacement_d3_069}


def da_replacement_d3_070(da_replacement_d2_070):
    feature = _clean(da_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_070'] = {'inputs': ['da_replacement_d2_070'], 'func': da_replacement_d3_070}


def da_replacement_d3_071(da_replacement_d2_071):
    feature = _clean(da_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_071'] = {'inputs': ['da_replacement_d2_071'], 'func': da_replacement_d3_071}


def da_replacement_d3_072(da_replacement_d2_072):
    feature = _clean(da_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_072'] = {'inputs': ['da_replacement_d2_072'], 'func': da_replacement_d3_072}


def da_replacement_d3_073(da_replacement_d2_073):
    feature = _clean(da_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_073'] = {'inputs': ['da_replacement_d2_073'], 'func': da_replacement_d3_073}


def da_replacement_d3_074(da_replacement_d2_074):
    feature = _clean(da_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_074'] = {'inputs': ['da_replacement_d2_074'], 'func': da_replacement_d3_074}


def da_replacement_d3_075(da_replacement_d2_075):
    feature = _clean(da_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_075'] = {'inputs': ['da_replacement_d2_075'], 'func': da_replacement_d3_075}


def da_replacement_d3_076(da_replacement_d2_076):
    feature = _clean(da_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_076'] = {'inputs': ['da_replacement_d2_076'], 'func': da_replacement_d3_076}


def da_replacement_d3_077(da_replacement_d2_077):
    feature = _clean(da_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_077'] = {'inputs': ['da_replacement_d2_077'], 'func': da_replacement_d3_077}


def da_replacement_d3_078(da_replacement_d2_078):
    feature = _clean(da_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_078'] = {'inputs': ['da_replacement_d2_078'], 'func': da_replacement_d3_078}


def da_replacement_d3_079(da_replacement_d2_079):
    feature = _clean(da_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_079'] = {'inputs': ['da_replacement_d2_079'], 'func': da_replacement_d3_079}


def da_replacement_d3_080(da_replacement_d2_080):
    feature = _clean(da_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_080'] = {'inputs': ['da_replacement_d2_080'], 'func': da_replacement_d3_080}


def da_replacement_d3_081(da_replacement_d2_081):
    feature = _clean(da_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_081'] = {'inputs': ['da_replacement_d2_081'], 'func': da_replacement_d3_081}


def da_replacement_d3_082(da_replacement_d2_082):
    feature = _clean(da_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_082'] = {'inputs': ['da_replacement_d2_082'], 'func': da_replacement_d3_082}


def da_replacement_d3_083(da_replacement_d2_083):
    feature = _clean(da_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_083'] = {'inputs': ['da_replacement_d2_083'], 'func': da_replacement_d3_083}


def da_replacement_d3_084(da_replacement_d2_084):
    feature = _clean(da_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_084'] = {'inputs': ['da_replacement_d2_084'], 'func': da_replacement_d3_084}


def da_replacement_d3_085(da_replacement_d2_085):
    feature = _clean(da_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_085'] = {'inputs': ['da_replacement_d2_085'], 'func': da_replacement_d3_085}


def da_replacement_d3_086(da_replacement_d2_086):
    feature = _clean(da_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_086'] = {'inputs': ['da_replacement_d2_086'], 'func': da_replacement_d3_086}


def da_replacement_d3_087(da_replacement_d2_087):
    feature = _clean(da_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_087'] = {'inputs': ['da_replacement_d2_087'], 'func': da_replacement_d3_087}


def da_replacement_d3_088(da_replacement_d2_088):
    feature = _clean(da_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_088'] = {'inputs': ['da_replacement_d2_088'], 'func': da_replacement_d3_088}


def da_replacement_d3_089(da_replacement_d2_089):
    feature = _clean(da_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_089'] = {'inputs': ['da_replacement_d2_089'], 'func': da_replacement_d3_089}


def da_replacement_d3_090(da_replacement_d2_090):
    feature = _clean(da_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_090'] = {'inputs': ['da_replacement_d2_090'], 'func': da_replacement_d3_090}


def da_replacement_d3_091(da_replacement_d2_091):
    feature = _clean(da_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_091'] = {'inputs': ['da_replacement_d2_091'], 'func': da_replacement_d3_091}


def da_replacement_d3_092(da_replacement_d2_092):
    feature = _clean(da_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_092'] = {'inputs': ['da_replacement_d2_092'], 'func': da_replacement_d3_092}


def da_replacement_d3_093(da_replacement_d2_093):
    feature = _clean(da_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_093'] = {'inputs': ['da_replacement_d2_093'], 'func': da_replacement_d3_093}


def da_replacement_d3_094(da_replacement_d2_094):
    feature = _clean(da_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_094'] = {'inputs': ['da_replacement_d2_094'], 'func': da_replacement_d3_094}


def da_replacement_d3_095(da_replacement_d2_095):
    feature = _clean(da_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_095'] = {'inputs': ['da_replacement_d2_095'], 'func': da_replacement_d3_095}


def da_replacement_d3_096(da_replacement_d2_096):
    feature = _clean(da_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_096'] = {'inputs': ['da_replacement_d2_096'], 'func': da_replacement_d3_096}


def da_replacement_d3_097(da_replacement_d2_097):
    feature = _clean(da_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_097'] = {'inputs': ['da_replacement_d2_097'], 'func': da_replacement_d3_097}


def da_replacement_d3_098(da_replacement_d2_098):
    feature = _clean(da_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_098'] = {'inputs': ['da_replacement_d2_098'], 'func': da_replacement_d3_098}


def da_replacement_d3_099(da_replacement_d2_099):
    feature = _clean(da_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_099'] = {'inputs': ['da_replacement_d2_099'], 'func': da_replacement_d3_099}


def da_replacement_d3_100(da_replacement_d2_100):
    feature = _clean(da_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_100'] = {'inputs': ['da_replacement_d2_100'], 'func': da_replacement_d3_100}


def da_replacement_d3_101(da_replacement_d2_101):
    feature = _clean(da_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_101'] = {'inputs': ['da_replacement_d2_101'], 'func': da_replacement_d3_101}


def da_replacement_d3_102(da_replacement_d2_102):
    feature = _clean(da_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_102'] = {'inputs': ['da_replacement_d2_102'], 'func': da_replacement_d3_102}


def da_replacement_d3_103(da_replacement_d2_103):
    feature = _clean(da_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_103'] = {'inputs': ['da_replacement_d2_103'], 'func': da_replacement_d3_103}


def da_replacement_d3_104(da_replacement_d2_104):
    feature = _clean(da_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_104'] = {'inputs': ['da_replacement_d2_104'], 'func': da_replacement_d3_104}


def da_replacement_d3_105(da_replacement_d2_105):
    feature = _clean(da_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_105'] = {'inputs': ['da_replacement_d2_105'], 'func': da_replacement_d3_105}


def da_replacement_d3_106(da_replacement_d2_106):
    feature = _clean(da_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_106'] = {'inputs': ['da_replacement_d2_106'], 'func': da_replacement_d3_106}


def da_replacement_d3_107(da_replacement_d2_107):
    feature = _clean(da_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_107'] = {'inputs': ['da_replacement_d2_107'], 'func': da_replacement_d3_107}


def da_replacement_d3_108(da_replacement_d2_108):
    feature = _clean(da_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_108'] = {'inputs': ['da_replacement_d2_108'], 'func': da_replacement_d3_108}


def da_replacement_d3_109(da_replacement_d2_109):
    feature = _clean(da_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_109'] = {'inputs': ['da_replacement_d2_109'], 'func': da_replacement_d3_109}


def da_replacement_d3_110(da_replacement_d2_110):
    feature = _clean(da_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_110'] = {'inputs': ['da_replacement_d2_110'], 'func': da_replacement_d3_110}


def da_replacement_d3_111(da_replacement_d2_111):
    feature = _clean(da_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_111'] = {'inputs': ['da_replacement_d2_111'], 'func': da_replacement_d3_111}


def da_replacement_d3_112(da_replacement_d2_112):
    feature = _clean(da_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_112'] = {'inputs': ['da_replacement_d2_112'], 'func': da_replacement_d3_112}


def da_replacement_d3_113(da_replacement_d2_113):
    feature = _clean(da_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_113'] = {'inputs': ['da_replacement_d2_113'], 'func': da_replacement_d3_113}


def da_replacement_d3_114(da_replacement_d2_114):
    feature = _clean(da_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_114'] = {'inputs': ['da_replacement_d2_114'], 'func': da_replacement_d3_114}


def da_replacement_d3_115(da_replacement_d2_115):
    feature = _clean(da_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_115'] = {'inputs': ['da_replacement_d2_115'], 'func': da_replacement_d3_115}


def da_replacement_d3_116(da_replacement_d2_116):
    feature = _clean(da_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_116'] = {'inputs': ['da_replacement_d2_116'], 'func': da_replacement_d3_116}


def da_replacement_d3_117(da_replacement_d2_117):
    feature = _clean(da_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_117'] = {'inputs': ['da_replacement_d2_117'], 'func': da_replacement_d3_117}


def da_replacement_d3_118(da_replacement_d2_118):
    feature = _clean(da_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_118'] = {'inputs': ['da_replacement_d2_118'], 'func': da_replacement_d3_118}


def da_replacement_d3_119(da_replacement_d2_119):
    feature = _clean(da_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_119'] = {'inputs': ['da_replacement_d2_119'], 'func': da_replacement_d3_119}


def da_replacement_d3_120(da_replacement_d2_120):
    feature = _clean(da_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_120'] = {'inputs': ['da_replacement_d2_120'], 'func': da_replacement_d3_120}


def da_replacement_d3_121(da_replacement_d2_121):
    feature = _clean(da_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_121'] = {'inputs': ['da_replacement_d2_121'], 'func': da_replacement_d3_121}


def da_replacement_d3_122(da_replacement_d2_122):
    feature = _clean(da_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_122'] = {'inputs': ['da_replacement_d2_122'], 'func': da_replacement_d3_122}


def da_replacement_d3_123(da_replacement_d2_123):
    feature = _clean(da_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_123'] = {'inputs': ['da_replacement_d2_123'], 'func': da_replacement_d3_123}


def da_replacement_d3_124(da_replacement_d2_124):
    feature = _clean(da_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_124'] = {'inputs': ['da_replacement_d2_124'], 'func': da_replacement_d3_124}


def da_replacement_d3_125(da_replacement_d2_125):
    feature = _clean(da_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_125'] = {'inputs': ['da_replacement_d2_125'], 'func': da_replacement_d3_125}


def da_replacement_d3_126(da_replacement_d2_126):
    feature = _clean(da_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_126'] = {'inputs': ['da_replacement_d2_126'], 'func': da_replacement_d3_126}


def da_replacement_d3_127(da_replacement_d2_127):
    feature = _clean(da_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_127'] = {'inputs': ['da_replacement_d2_127'], 'func': da_replacement_d3_127}


def da_replacement_d3_128(da_replacement_d2_128):
    feature = _clean(da_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_128'] = {'inputs': ['da_replacement_d2_128'], 'func': da_replacement_d3_128}


def da_replacement_d3_129(da_replacement_d2_129):
    feature = _clean(da_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_129'] = {'inputs': ['da_replacement_d2_129'], 'func': da_replacement_d3_129}


def da_replacement_d3_130(da_replacement_d2_130):
    feature = _clean(da_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_130'] = {'inputs': ['da_replacement_d2_130'], 'func': da_replacement_d3_130}


def da_replacement_d3_131(da_replacement_d2_131):
    feature = _clean(da_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_131'] = {'inputs': ['da_replacement_d2_131'], 'func': da_replacement_d3_131}


def da_replacement_d3_132(da_replacement_d2_132):
    feature = _clean(da_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_132'] = {'inputs': ['da_replacement_d2_132'], 'func': da_replacement_d3_132}


def da_replacement_d3_133(da_replacement_d2_133):
    feature = _clean(da_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_133'] = {'inputs': ['da_replacement_d2_133'], 'func': da_replacement_d3_133}


def da_replacement_d3_134(da_replacement_d2_134):
    feature = _clean(da_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_134'] = {'inputs': ['da_replacement_d2_134'], 'func': da_replacement_d3_134}


def da_replacement_d3_135(da_replacement_d2_135):
    feature = _clean(da_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_135'] = {'inputs': ['da_replacement_d2_135'], 'func': da_replacement_d3_135}


def da_replacement_d3_136(da_replacement_d2_136):
    feature = _clean(da_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_136'] = {'inputs': ['da_replacement_d2_136'], 'func': da_replacement_d3_136}


def da_replacement_d3_137(da_replacement_d2_137):
    feature = _clean(da_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_137'] = {'inputs': ['da_replacement_d2_137'], 'func': da_replacement_d3_137}


def da_replacement_d3_138(da_replacement_d2_138):
    feature = _clean(da_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_138'] = {'inputs': ['da_replacement_d2_138'], 'func': da_replacement_d3_138}


def da_replacement_d3_139(da_replacement_d2_139):
    feature = _clean(da_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_139'] = {'inputs': ['da_replacement_d2_139'], 'func': da_replacement_d3_139}


def da_replacement_d3_140(da_replacement_d2_140):
    feature = _clean(da_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_140'] = {'inputs': ['da_replacement_d2_140'], 'func': da_replacement_d3_140}


def da_replacement_d3_141(da_replacement_d2_141):
    feature = _clean(da_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_141'] = {'inputs': ['da_replacement_d2_141'], 'func': da_replacement_d3_141}


def da_replacement_d3_142(da_replacement_d2_142):
    feature = _clean(da_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_142'] = {'inputs': ['da_replacement_d2_142'], 'func': da_replacement_d3_142}


def da_replacement_d3_143(da_replacement_d2_143):
    feature = _clean(da_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_143'] = {'inputs': ['da_replacement_d2_143'], 'func': da_replacement_d3_143}


def da_replacement_d3_144(da_replacement_d2_144):
    feature = _clean(da_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_144'] = {'inputs': ['da_replacement_d2_144'], 'func': da_replacement_d3_144}


def da_replacement_d3_145(da_replacement_d2_145):
    feature = _clean(da_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_145'] = {'inputs': ['da_replacement_d2_145'], 'func': da_replacement_d3_145}


def da_replacement_d3_146(da_replacement_d2_146):
    feature = _clean(da_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_146'] = {'inputs': ['da_replacement_d2_146'], 'func': da_replacement_d3_146}


def da_replacement_d3_147(da_replacement_d2_147):
    feature = _clean(da_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_147'] = {'inputs': ['da_replacement_d2_147'], 'func': da_replacement_d3_147}


def da_replacement_d3_148(da_replacement_d2_148):
    feature = _clean(da_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_148'] = {'inputs': ['da_replacement_d2_148'], 'func': da_replacement_d3_148}


def da_replacement_d3_149(da_replacement_d2_149):
    feature = _clean(da_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_149'] = {'inputs': ['da_replacement_d2_149'], 'func': da_replacement_d3_149}


def da_replacement_d3_150(da_replacement_d2_150):
    feature = _clean(da_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_150'] = {'inputs': ['da_replacement_d2_150'], 'func': da_replacement_d3_150}


def da_replacement_d3_151(da_replacement_d2_151):
    feature = _clean(da_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_151'] = {'inputs': ['da_replacement_d2_151'], 'func': da_replacement_d3_151}


def da_replacement_d3_152(da_replacement_d2_152):
    feature = _clean(da_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_152'] = {'inputs': ['da_replacement_d2_152'], 'func': da_replacement_d3_152}


def da_replacement_d3_153(da_replacement_d2_153):
    feature = _clean(da_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_153'] = {'inputs': ['da_replacement_d2_153'], 'func': da_replacement_d3_153}


def da_replacement_d3_154(da_replacement_d2_154):
    feature = _clean(da_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_154'] = {'inputs': ['da_replacement_d2_154'], 'func': da_replacement_d3_154}


def da_replacement_d3_155(da_replacement_d2_155):
    feature = _clean(da_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_155'] = {'inputs': ['da_replacement_d2_155'], 'func': da_replacement_d3_155}


def da_replacement_d3_156(da_replacement_d2_156):
    feature = _clean(da_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_156'] = {'inputs': ['da_replacement_d2_156'], 'func': da_replacement_d3_156}


def da_replacement_d3_157(da_replacement_d2_157):
    feature = _clean(da_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_157'] = {'inputs': ['da_replacement_d2_157'], 'func': da_replacement_d3_157}


def da_replacement_d3_158(da_replacement_d2_158):
    feature = _clean(da_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_158'] = {'inputs': ['da_replacement_d2_158'], 'func': da_replacement_d3_158}


def da_replacement_d3_159(da_replacement_d2_159):
    feature = _clean(da_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_159'] = {'inputs': ['da_replacement_d2_159'], 'func': da_replacement_d3_159}


def da_replacement_d3_160(da_replacement_d2_160):
    feature = _clean(da_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_160'] = {'inputs': ['da_replacement_d2_160'], 'func': da_replacement_d3_160}


def da_replacement_d3_161(da_replacement_d2_161):
    feature = _clean(da_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_161'] = {'inputs': ['da_replacement_d2_161'], 'func': da_replacement_d3_161}


def da_replacement_d3_162(da_replacement_d2_162):
    feature = _clean(da_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_162'] = {'inputs': ['da_replacement_d2_162'], 'func': da_replacement_d3_162}


def da_replacement_d3_163(da_replacement_d2_163):
    feature = _clean(da_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_163'] = {'inputs': ['da_replacement_d2_163'], 'func': da_replacement_d3_163}


def da_replacement_d3_164(da_replacement_d2_164):
    feature = _clean(da_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_164'] = {'inputs': ['da_replacement_d2_164'], 'func': da_replacement_d3_164}


def da_replacement_d3_165(da_replacement_d2_165):
    feature = _clean(da_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_165'] = {'inputs': ['da_replacement_d2_165'], 'func': da_replacement_d3_165}


def da_replacement_d3_166(da_replacement_d2_166):
    feature = _clean(da_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
DA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['da_replacement_d3_166'] = {'inputs': ['da_replacement_d2_166'], 'func': da_replacement_d3_166}


# Third-derivative extensions for repaired first-base features.
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def dla_base_universe_d3_001_dla_003_fcf_burn_to_cash_63(dla_base_universe_d2_001_dla_003_fcf_burn_to_cash_63):
    return _base_universe_d3(dla_base_universe_d2_001_dla_003_fcf_burn_to_cash_63, 1)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_001_dla_003_fcf_burn_to_cash_63'] = {'inputs': ['dla_base_universe_d2_001_dla_003_fcf_burn_to_cash_63'], 'func': dla_base_universe_d3_001_dla_003_fcf_burn_to_cash_63}


def dla_base_universe_d3_002_dla_004_debt_to_equity_84(dla_base_universe_d2_002_dla_004_debt_to_equity_84):
    return _base_universe_d3(dla_base_universe_d2_002_dla_004_debt_to_equity_84, 2)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_002_dla_004_debt_to_equity_84'] = {'inputs': ['dla_base_universe_d2_002_dla_004_debt_to_equity_84'], 'func': dla_base_universe_d3_002_dla_004_debt_to_equity_84}


def dla_base_universe_d3_003_dla_005_debt_to_assets_126(dla_base_universe_d2_003_dla_005_debt_to_assets_126):
    return _base_universe_d3(dla_base_universe_d2_003_dla_005_debt_to_assets_126, 3)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_003_dla_005_debt_to_assets_126'] = {'inputs': ['dla_base_universe_d2_003_dla_005_debt_to_assets_126'], 'func': dla_base_universe_d3_003_dla_005_debt_to_assets_126}


def dla_base_universe_d3_004_dla_012_accrual_gap_1260(dla_base_universe_d2_004_dla_012_accrual_gap_1260):
    return _base_universe_d3(dla_base_universe_d2_004_dla_012_accrual_gap_1260, 4)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_004_dla_012_accrual_gap_1260'] = {'inputs': ['dla_base_universe_d2_004_dla_012_accrual_gap_1260'], 'func': dla_base_universe_d3_004_dla_012_accrual_gap_1260}


def dla_base_universe_d3_005_dla_016_debt_to_equity_21(dla_base_universe_d2_005_dla_016_debt_to_equity_21):
    return _base_universe_d3(dla_base_universe_d2_005_dla_016_debt_to_equity_21, 5)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_005_dla_016_debt_to_equity_21'] = {'inputs': ['dla_base_universe_d2_005_dla_016_debt_to_equity_21'], 'func': dla_base_universe_d3_005_dla_016_debt_to_equity_21}


def dla_base_universe_d3_006_dla_017_debt_to_assets_42(dla_base_universe_d2_006_dla_017_debt_to_assets_42):
    return _base_universe_d3(dla_base_universe_d2_006_dla_017_debt_to_assets_42, 6)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_006_dla_017_debt_to_assets_42'] = {'inputs': ['dla_base_universe_d2_006_dla_017_debt_to_assets_42'], 'func': dla_base_universe_d3_006_dla_017_debt_to_assets_42}


def dla_base_universe_d3_007_dla_024_accrual_gap_504(dla_base_universe_d2_007_dla_024_accrual_gap_504):
    return _base_universe_d3(dla_base_universe_d2_007_dla_024_accrual_gap_504, 7)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_007_dla_024_accrual_gap_504'] = {'inputs': ['dla_base_universe_d2_007_dla_024_accrual_gap_504'], 'func': dla_base_universe_d3_007_dla_024_accrual_gap_504}


def dla_base_universe_d3_008_dla_027_fcf_burn_to_cash_1260(dla_base_universe_d2_008_dla_027_fcf_burn_to_cash_1260):
    return _base_universe_d3(dla_base_universe_d2_008_dla_027_fcf_burn_to_cash_1260, 8)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_008_dla_027_fcf_burn_to_cash_1260'] = {'inputs': ['dla_base_universe_d2_008_dla_027_fcf_burn_to_cash_1260'], 'func': dla_base_universe_d3_008_dla_027_fcf_burn_to_cash_1260}


def dla_base_universe_d3_009_dla_028_debt_to_equity_1512(dla_base_universe_d2_009_dla_028_debt_to_equity_1512):
    return _base_universe_d3(dla_base_universe_d2_009_dla_028_debt_to_equity_1512, 9)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_009_dla_028_debt_to_equity_1512'] = {'inputs': ['dla_base_universe_d2_009_dla_028_debt_to_equity_1512'], 'func': dla_base_universe_d3_009_dla_028_debt_to_equity_1512}


def dla_base_universe_d3_010_dla_029_debt_to_assets_63(dla_base_universe_d2_010_dla_029_debt_to_assets_63):
    return _base_universe_d3(dla_base_universe_d2_010_dla_029_debt_to_assets_63, 10)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_010_dla_029_debt_to_assets_63'] = {'inputs': ['dla_base_universe_d2_010_dla_029_debt_to_assets_63'], 'func': dla_base_universe_d3_010_dla_029_debt_to_assets_63}


def dla_base_universe_d3_011_dla_031_interest_coverage_stress_21(dla_base_universe_d2_011_dla_031_interest_coverage_stress_21):
    return _base_universe_d3(dla_base_universe_d2_011_dla_031_interest_coverage_stress_21, 11)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_011_dla_031_interest_coverage_stress_21'] = {'inputs': ['dla_base_universe_d2_011_dla_031_interest_coverage_stress_21'], 'func': dla_base_universe_d3_011_dla_031_interest_coverage_stress_21}


def dla_base_universe_d3_012_dla_036_accrual_gap_189(dla_base_universe_d2_012_dla_036_accrual_gap_189):
    return _base_universe_d3(dla_base_universe_d2_012_dla_036_accrual_gap_189, 12)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_012_dla_036_accrual_gap_189'] = {'inputs': ['dla_base_universe_d2_012_dla_036_accrual_gap_189'], 'func': dla_base_universe_d3_012_dla_036_accrual_gap_189}


def dla_base_universe_d3_013_dla_039_fcf_burn_to_cash_504(dla_base_universe_d2_013_dla_039_fcf_burn_to_cash_504):
    return _base_universe_d3(dla_base_universe_d2_013_dla_039_fcf_burn_to_cash_504, 13)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_013_dla_039_fcf_burn_to_cash_504'] = {'inputs': ['dla_base_universe_d2_013_dla_039_fcf_burn_to_cash_504'], 'func': dla_base_universe_d3_013_dla_039_fcf_burn_to_cash_504}


def dla_base_universe_d3_014_dla_040_debt_to_equity_756(dla_base_universe_d2_014_dla_040_debt_to_equity_756):
    return _base_universe_d3(dla_base_universe_d2_014_dla_040_debt_to_equity_756, 14)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_014_dla_040_debt_to_equity_756'] = {'inputs': ['dla_base_universe_d2_014_dla_040_debt_to_equity_756'], 'func': dla_base_universe_d3_014_dla_040_debt_to_equity_756}


def dla_base_universe_d3_015_dla_041_debt_to_assets_1008(dla_base_universe_d2_015_dla_041_debt_to_assets_1008):
    return _base_universe_d3(dla_base_universe_d2_015_dla_041_debt_to_assets_1008, 15)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_015_dla_041_debt_to_assets_1008'] = {'inputs': ['dla_base_universe_d2_015_dla_041_debt_to_assets_1008'], 'func': dla_base_universe_d3_015_dla_041_debt_to_assets_1008}


def dla_base_universe_d3_016_dla_043_interest_coverage_stress_1512(dla_base_universe_d2_016_dla_043_interest_coverage_stress_1512):
    return _base_universe_d3(dla_base_universe_d2_016_dla_043_interest_coverage_stress_1512, 16)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_016_dla_043_interest_coverage_stress_1512'] = {'inputs': ['dla_base_universe_d2_016_dla_043_interest_coverage_stress_1512'], 'func': dla_base_universe_d3_016_dla_043_interest_coverage_stress_1512}


def dla_base_universe_d3_017_dla_048_accrual_gap_63(dla_base_universe_d2_017_dla_048_accrual_gap_63):
    return _base_universe_d3(dla_base_universe_d2_017_dla_048_accrual_gap_63, 17)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_017_dla_048_accrual_gap_63'] = {'inputs': ['dla_base_universe_d2_017_dla_048_accrual_gap_63'], 'func': dla_base_universe_d3_017_dla_048_accrual_gap_63}


def dla_base_universe_d3_018_dla_051_fcf_burn_to_cash_189(dla_base_universe_d2_018_dla_051_fcf_burn_to_cash_189):
    return _base_universe_d3(dla_base_universe_d2_018_dla_051_fcf_burn_to_cash_189, 18)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_018_dla_051_fcf_burn_to_cash_189'] = {'inputs': ['dla_base_universe_d2_018_dla_051_fcf_burn_to_cash_189'], 'func': dla_base_universe_d3_018_dla_051_fcf_burn_to_cash_189}


def dla_base_universe_d3_019_dla_052_debt_to_equity_252(dla_base_universe_d2_019_dla_052_debt_to_equity_252):
    return _base_universe_d3(dla_base_universe_d2_019_dla_052_debt_to_equity_252, 19)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_019_dla_052_debt_to_equity_252'] = {'inputs': ['dla_base_universe_d2_019_dla_052_debt_to_equity_252'], 'func': dla_base_universe_d3_019_dla_052_debt_to_equity_252}


def dla_base_universe_d3_020_dla_053_debt_to_assets_378(dla_base_universe_d2_020_dla_053_debt_to_assets_378):
    return _base_universe_d3(dla_base_universe_d2_020_dla_053_debt_to_assets_378, 20)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_020_dla_053_debt_to_assets_378'] = {'inputs': ['dla_base_universe_d2_020_dla_053_debt_to_assets_378'], 'func': dla_base_universe_d3_020_dla_053_debt_to_assets_378}


def dla_base_universe_d3_021_dla_055_interest_coverage_stress_756(dla_base_universe_d2_021_dla_055_interest_coverage_stress_756):
    return _base_universe_d3(dla_base_universe_d2_021_dla_055_interest_coverage_stress_756, 21)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_021_dla_055_interest_coverage_stress_756'] = {'inputs': ['dla_base_universe_d2_021_dla_055_interest_coverage_stress_756'], 'func': dla_base_universe_d3_021_dla_055_interest_coverage_stress_756}


def dla_base_universe_d3_022_dla_060_accrual_gap_252(dla_base_universe_d2_022_dla_060_accrual_gap_252):
    return _base_universe_d3(dla_base_universe_d2_022_dla_060_accrual_gap_252, 22)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_022_dla_060_accrual_gap_252'] = {'inputs': ['dla_base_universe_d2_022_dla_060_accrual_gap_252'], 'func': dla_base_universe_d3_022_dla_060_accrual_gap_252}


def dla_base_universe_d3_023_dla_basefill_001(dla_base_universe_d2_023_dla_basefill_001):
    return _base_universe_d3(dla_base_universe_d2_023_dla_basefill_001, 23)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_023_dla_basefill_001'] = {'inputs': ['dla_base_universe_d2_023_dla_basefill_001'], 'func': dla_base_universe_d3_023_dla_basefill_001}


def dla_base_universe_d3_024_dla_basefill_002(dla_base_universe_d2_024_dla_basefill_002):
    return _base_universe_d3(dla_base_universe_d2_024_dla_basefill_002, 24)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_024_dla_basefill_002'] = {'inputs': ['dla_base_universe_d2_024_dla_basefill_002'], 'func': dla_base_universe_d3_024_dla_basefill_002}


def dla_base_universe_d3_025_dla_basefill_006(dla_base_universe_d2_025_dla_basefill_006):
    return _base_universe_d3(dla_base_universe_d2_025_dla_basefill_006, 25)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_025_dla_basefill_006'] = {'inputs': ['dla_base_universe_d2_025_dla_basefill_006'], 'func': dla_base_universe_d3_025_dla_basefill_006}


def dla_base_universe_d3_026_dla_basefill_008(dla_base_universe_d2_026_dla_basefill_008):
    return _base_universe_d3(dla_base_universe_d2_026_dla_basefill_008, 26)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_026_dla_basefill_008'] = {'inputs': ['dla_base_universe_d2_026_dla_basefill_008'], 'func': dla_base_universe_d3_026_dla_basefill_008}


def dla_base_universe_d3_027_dla_basefill_009(dla_base_universe_d2_027_dla_basefill_009):
    return _base_universe_d3(dla_base_universe_d2_027_dla_basefill_009, 27)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_027_dla_basefill_009'] = {'inputs': ['dla_base_universe_d2_027_dla_basefill_009'], 'func': dla_base_universe_d3_027_dla_basefill_009}


def dla_base_universe_d3_028_dla_basefill_010(dla_base_universe_d2_028_dla_basefill_010):
    return _base_universe_d3(dla_base_universe_d2_028_dla_basefill_010, 28)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_028_dla_basefill_010'] = {'inputs': ['dla_base_universe_d2_028_dla_basefill_010'], 'func': dla_base_universe_d3_028_dla_basefill_010}


def dla_base_universe_d3_029_dla_basefill_011(dla_base_universe_d2_029_dla_basefill_011):
    return _base_universe_d3(dla_base_universe_d2_029_dla_basefill_011, 29)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_029_dla_basefill_011'] = {'inputs': ['dla_base_universe_d2_029_dla_basefill_011'], 'func': dla_base_universe_d3_029_dla_basefill_011}


def dla_base_universe_d3_030_dla_basefill_013(dla_base_universe_d2_030_dla_basefill_013):
    return _base_universe_d3(dla_base_universe_d2_030_dla_basefill_013, 30)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_030_dla_basefill_013'] = {'inputs': ['dla_base_universe_d2_030_dla_basefill_013'], 'func': dla_base_universe_d3_030_dla_basefill_013}


def dla_base_universe_d3_031_dla_basefill_014(dla_base_universe_d2_031_dla_basefill_014):
    return _base_universe_d3(dla_base_universe_d2_031_dla_basefill_014, 31)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_031_dla_basefill_014'] = {'inputs': ['dla_base_universe_d2_031_dla_basefill_014'], 'func': dla_base_universe_d3_031_dla_basefill_014}


def dla_base_universe_d3_032_dla_basefill_015(dla_base_universe_d2_032_dla_basefill_015):
    return _base_universe_d3(dla_base_universe_d2_032_dla_basefill_015, 32)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_032_dla_basefill_015'] = {'inputs': ['dla_base_universe_d2_032_dla_basefill_015'], 'func': dla_base_universe_d3_032_dla_basefill_015}


def dla_base_universe_d3_033_dla_basefill_018(dla_base_universe_d2_033_dla_basefill_018):
    return _base_universe_d3(dla_base_universe_d2_033_dla_basefill_018, 33)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_033_dla_basefill_018'] = {'inputs': ['dla_base_universe_d2_033_dla_basefill_018'], 'func': dla_base_universe_d3_033_dla_basefill_018}


def dla_base_universe_d3_034_dla_basefill_020(dla_base_universe_d2_034_dla_basefill_020):
    return _base_universe_d3(dla_base_universe_d2_034_dla_basefill_020, 34)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_034_dla_basefill_020'] = {'inputs': ['dla_base_universe_d2_034_dla_basefill_020'], 'func': dla_base_universe_d3_034_dla_basefill_020}


def dla_base_universe_d3_035_dla_basefill_021(dla_base_universe_d2_035_dla_basefill_021):
    return _base_universe_d3(dla_base_universe_d2_035_dla_basefill_021, 35)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_035_dla_basefill_021'] = {'inputs': ['dla_base_universe_d2_035_dla_basefill_021'], 'func': dla_base_universe_d3_035_dla_basefill_021}


def dla_base_universe_d3_036_dla_basefill_022(dla_base_universe_d2_036_dla_basefill_022):
    return _base_universe_d3(dla_base_universe_d2_036_dla_basefill_022, 36)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_036_dla_basefill_022'] = {'inputs': ['dla_base_universe_d2_036_dla_basefill_022'], 'func': dla_base_universe_d3_036_dla_basefill_022}


def dla_base_universe_d3_037_dla_basefill_023(dla_base_universe_d2_037_dla_basefill_023):
    return _base_universe_d3(dla_base_universe_d2_037_dla_basefill_023, 37)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_037_dla_basefill_023'] = {'inputs': ['dla_base_universe_d2_037_dla_basefill_023'], 'func': dla_base_universe_d3_037_dla_basefill_023}


def dla_base_universe_d3_038_dla_basefill_025(dla_base_universe_d2_038_dla_basefill_025):
    return _base_universe_d3(dla_base_universe_d2_038_dla_basefill_025, 38)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_038_dla_basefill_025'] = {'inputs': ['dla_base_universe_d2_038_dla_basefill_025'], 'func': dla_base_universe_d3_038_dla_basefill_025}


def dla_base_universe_d3_039_dla_basefill_026(dla_base_universe_d2_039_dla_basefill_026):
    return _base_universe_d3(dla_base_universe_d2_039_dla_basefill_026, 39)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_039_dla_basefill_026'] = {'inputs': ['dla_base_universe_d2_039_dla_basefill_026'], 'func': dla_base_universe_d3_039_dla_basefill_026}


def dla_base_universe_d3_040_dla_basefill_030(dla_base_universe_d2_040_dla_basefill_030):
    return _base_universe_d3(dla_base_universe_d2_040_dla_basefill_030, 40)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_040_dla_basefill_030'] = {'inputs': ['dla_base_universe_d2_040_dla_basefill_030'], 'func': dla_base_universe_d3_040_dla_basefill_030}


def dla_base_universe_d3_041_dla_basefill_032(dla_base_universe_d2_041_dla_basefill_032):
    return _base_universe_d3(dla_base_universe_d2_041_dla_basefill_032, 41)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_041_dla_basefill_032'] = {'inputs': ['dla_base_universe_d2_041_dla_basefill_032'], 'func': dla_base_universe_d3_041_dla_basefill_032}


def dla_base_universe_d3_042_dla_basefill_033(dla_base_universe_d2_042_dla_basefill_033):
    return _base_universe_d3(dla_base_universe_d2_042_dla_basefill_033, 42)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_042_dla_basefill_033'] = {'inputs': ['dla_base_universe_d2_042_dla_basefill_033'], 'func': dla_base_universe_d3_042_dla_basefill_033}


def dla_base_universe_d3_043_dla_basefill_034(dla_base_universe_d2_043_dla_basefill_034):
    return _base_universe_d3(dla_base_universe_d2_043_dla_basefill_034, 43)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_043_dla_basefill_034'] = {'inputs': ['dla_base_universe_d2_043_dla_basefill_034'], 'func': dla_base_universe_d3_043_dla_basefill_034}


def dla_base_universe_d3_044_dla_basefill_035(dla_base_universe_d2_044_dla_basefill_035):
    return _base_universe_d3(dla_base_universe_d2_044_dla_basefill_035, 44)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_044_dla_basefill_035'] = {'inputs': ['dla_base_universe_d2_044_dla_basefill_035'], 'func': dla_base_universe_d3_044_dla_basefill_035}


def dla_base_universe_d3_045_dla_basefill_037(dla_base_universe_d2_045_dla_basefill_037):
    return _base_universe_d3(dla_base_universe_d2_045_dla_basefill_037, 45)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_045_dla_basefill_037'] = {'inputs': ['dla_base_universe_d2_045_dla_basefill_037'], 'func': dla_base_universe_d3_045_dla_basefill_037}


def dla_base_universe_d3_046_dla_basefill_038(dla_base_universe_d2_046_dla_basefill_038):
    return _base_universe_d3(dla_base_universe_d2_046_dla_basefill_038, 46)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_046_dla_basefill_038'] = {'inputs': ['dla_base_universe_d2_046_dla_basefill_038'], 'func': dla_base_universe_d3_046_dla_basefill_038}


def dla_base_universe_d3_047_dla_basefill_042(dla_base_universe_d2_047_dla_basefill_042):
    return _base_universe_d3(dla_base_universe_d2_047_dla_basefill_042, 47)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_047_dla_basefill_042'] = {'inputs': ['dla_base_universe_d2_047_dla_basefill_042'], 'func': dla_base_universe_d3_047_dla_basefill_042}


def dla_base_universe_d3_048_dla_basefill_044(dla_base_universe_d2_048_dla_basefill_044):
    return _base_universe_d3(dla_base_universe_d2_048_dla_basefill_044, 48)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_048_dla_basefill_044'] = {'inputs': ['dla_base_universe_d2_048_dla_basefill_044'], 'func': dla_base_universe_d3_048_dla_basefill_044}


def dla_base_universe_d3_049_dla_basefill_045(dla_base_universe_d2_049_dla_basefill_045):
    return _base_universe_d3(dla_base_universe_d2_049_dla_basefill_045, 49)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_049_dla_basefill_045'] = {'inputs': ['dla_base_universe_d2_049_dla_basefill_045'], 'func': dla_base_universe_d3_049_dla_basefill_045}


def dla_base_universe_d3_050_dla_basefill_046(dla_base_universe_d2_050_dla_basefill_046):
    return _base_universe_d3(dla_base_universe_d2_050_dla_basefill_046, 50)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_050_dla_basefill_046'] = {'inputs': ['dla_base_universe_d2_050_dla_basefill_046'], 'func': dla_base_universe_d3_050_dla_basefill_046}


def dla_base_universe_d3_051_dla_basefill_047(dla_base_universe_d2_051_dla_basefill_047):
    return _base_universe_d3(dla_base_universe_d2_051_dla_basefill_047, 51)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_051_dla_basefill_047'] = {'inputs': ['dla_base_universe_d2_051_dla_basefill_047'], 'func': dla_base_universe_d3_051_dla_basefill_047}


def dla_base_universe_d3_052_dla_basefill_049(dla_base_universe_d2_052_dla_basefill_049):
    return _base_universe_d3(dla_base_universe_d2_052_dla_basefill_049, 52)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_052_dla_basefill_049'] = {'inputs': ['dla_base_universe_d2_052_dla_basefill_049'], 'func': dla_base_universe_d3_052_dla_basefill_049}


def dla_base_universe_d3_053_dla_basefill_050(dla_base_universe_d2_053_dla_basefill_050):
    return _base_universe_d3(dla_base_universe_d2_053_dla_basefill_050, 53)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_053_dla_basefill_050'] = {'inputs': ['dla_base_universe_d2_053_dla_basefill_050'], 'func': dla_base_universe_d3_053_dla_basefill_050}


def dla_base_universe_d3_054_dla_basefill_054(dla_base_universe_d2_054_dla_basefill_054):
    return _base_universe_d3(dla_base_universe_d2_054_dla_basefill_054, 54)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_054_dla_basefill_054'] = {'inputs': ['dla_base_universe_d2_054_dla_basefill_054'], 'func': dla_base_universe_d3_054_dla_basefill_054}


def dla_base_universe_d3_055_dla_basefill_056(dla_base_universe_d2_055_dla_basefill_056):
    return _base_universe_d3(dla_base_universe_d2_055_dla_basefill_056, 55)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_055_dla_basefill_056'] = {'inputs': ['dla_base_universe_d2_055_dla_basefill_056'], 'func': dla_base_universe_d3_055_dla_basefill_056}


def dla_base_universe_d3_056_dla_basefill_057(dla_base_universe_d2_056_dla_basefill_057):
    return _base_universe_d3(dla_base_universe_d2_056_dla_basefill_057, 56)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_056_dla_basefill_057'] = {'inputs': ['dla_base_universe_d2_056_dla_basefill_057'], 'func': dla_base_universe_d3_056_dla_basefill_057}


def dla_base_universe_d3_057_dla_basefill_058(dla_base_universe_d2_057_dla_basefill_058):
    return _base_universe_d3(dla_base_universe_d2_057_dla_basefill_058, 57)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_057_dla_basefill_058'] = {'inputs': ['dla_base_universe_d2_057_dla_basefill_058'], 'func': dla_base_universe_d3_057_dla_basefill_058}


def dla_base_universe_d3_058_dla_basefill_059(dla_base_universe_d2_058_dla_basefill_059):
    return _base_universe_d3(dla_base_universe_d2_058_dla_basefill_059, 58)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_058_dla_basefill_059'] = {'inputs': ['dla_base_universe_d2_058_dla_basefill_059'], 'func': dla_base_universe_d3_058_dla_basefill_059}


def dla_base_universe_d3_059_dla_basefill_061(dla_base_universe_d2_059_dla_basefill_061):
    return _base_universe_d3(dla_base_universe_d2_059_dla_basefill_061, 59)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_059_dla_basefill_061'] = {'inputs': ['dla_base_universe_d2_059_dla_basefill_061'], 'func': dla_base_universe_d3_059_dla_basefill_061}


def dla_base_universe_d3_060_dla_basefill_062(dla_base_universe_d2_060_dla_basefill_062):
    return _base_universe_d3(dla_base_universe_d2_060_dla_basefill_062, 60)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_060_dla_basefill_062'] = {'inputs': ['dla_base_universe_d2_060_dla_basefill_062'], 'func': dla_base_universe_d3_060_dla_basefill_062}


def dla_base_universe_d3_061_dla_basefill_063(dla_base_universe_d2_061_dla_basefill_063):
    return _base_universe_d3(dla_base_universe_d2_061_dla_basefill_063, 61)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_061_dla_basefill_063'] = {'inputs': ['dla_base_universe_d2_061_dla_basefill_063'], 'func': dla_base_universe_d3_061_dla_basefill_063}


def dla_base_universe_d3_062_dla_basefill_064(dla_base_universe_d2_062_dla_basefill_064):
    return _base_universe_d3(dla_base_universe_d2_062_dla_basefill_064, 62)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_062_dla_basefill_064'] = {'inputs': ['dla_base_universe_d2_062_dla_basefill_064'], 'func': dla_base_universe_d3_062_dla_basefill_064}


def dla_base_universe_d3_063_dla_basefill_065(dla_base_universe_d2_063_dla_basefill_065):
    return _base_universe_d3(dla_base_universe_d2_063_dla_basefill_065, 63)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_063_dla_basefill_065'] = {'inputs': ['dla_base_universe_d2_063_dla_basefill_065'], 'func': dla_base_universe_d3_063_dla_basefill_065}


def dla_base_universe_d3_064_dla_basefill_066(dla_base_universe_d2_064_dla_basefill_066):
    return _base_universe_d3(dla_base_universe_d2_064_dla_basefill_066, 64)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_064_dla_basefill_066'] = {'inputs': ['dla_base_universe_d2_064_dla_basefill_066'], 'func': dla_base_universe_d3_064_dla_basefill_066}


def dla_base_universe_d3_065_dla_basefill_067(dla_base_universe_d2_065_dla_basefill_067):
    return _base_universe_d3(dla_base_universe_d2_065_dla_basefill_067, 65)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_065_dla_basefill_067'] = {'inputs': ['dla_base_universe_d2_065_dla_basefill_067'], 'func': dla_base_universe_d3_065_dla_basefill_067}


def dla_base_universe_d3_066_dla_basefill_068(dla_base_universe_d2_066_dla_basefill_068):
    return _base_universe_d3(dla_base_universe_d2_066_dla_basefill_068, 66)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_066_dla_basefill_068'] = {'inputs': ['dla_base_universe_d2_066_dla_basefill_068'], 'func': dla_base_universe_d3_066_dla_basefill_068}


def dla_base_universe_d3_067_dla_basefill_069(dla_base_universe_d2_067_dla_basefill_069):
    return _base_universe_d3(dla_base_universe_d2_067_dla_basefill_069, 67)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_067_dla_basefill_069'] = {'inputs': ['dla_base_universe_d2_067_dla_basefill_069'], 'func': dla_base_universe_d3_067_dla_basefill_069}


def dla_base_universe_d3_068_dla_basefill_070(dla_base_universe_d2_068_dla_basefill_070):
    return _base_universe_d3(dla_base_universe_d2_068_dla_basefill_070, 68)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_068_dla_basefill_070'] = {'inputs': ['dla_base_universe_d2_068_dla_basefill_070'], 'func': dla_base_universe_d3_068_dla_basefill_070}


def dla_base_universe_d3_069_dla_basefill_071(dla_base_universe_d2_069_dla_basefill_071):
    return _base_universe_d3(dla_base_universe_d2_069_dla_basefill_071, 69)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_069_dla_basefill_071'] = {'inputs': ['dla_base_universe_d2_069_dla_basefill_071'], 'func': dla_base_universe_d3_069_dla_basefill_071}


def dla_base_universe_d3_070_dla_basefill_072(dla_base_universe_d2_070_dla_basefill_072):
    return _base_universe_d3(dla_base_universe_d2_070_dla_basefill_072, 70)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_070_dla_basefill_072'] = {'inputs': ['dla_base_universe_d2_070_dla_basefill_072'], 'func': dla_base_universe_d3_070_dla_basefill_072}


def dla_base_universe_d3_071_dla_basefill_073(dla_base_universe_d2_071_dla_basefill_073):
    return _base_universe_d3(dla_base_universe_d2_071_dla_basefill_073, 71)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_071_dla_basefill_073'] = {'inputs': ['dla_base_universe_d2_071_dla_basefill_073'], 'func': dla_base_universe_d3_071_dla_basefill_073}


def dla_base_universe_d3_072_dla_basefill_074(dla_base_universe_d2_072_dla_basefill_074):
    return _base_universe_d3(dla_base_universe_d2_072_dla_basefill_074, 72)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_072_dla_basefill_074'] = {'inputs': ['dla_base_universe_d2_072_dla_basefill_074'], 'func': dla_base_universe_d3_072_dla_basefill_074}


def dla_base_universe_d3_073_dla_basefill_075(dla_base_universe_d2_073_dla_basefill_075):
    return _base_universe_d3(dla_base_universe_d2_073_dla_basefill_075, 73)
DLA_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dla_base_universe_d3_073_dla_basefill_075'] = {'inputs': ['dla_base_universe_d2_073_dla_basefill_075'], 'func': dla_base_universe_d3_073_dla_basefill_075}
