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



def mgc_176_mgc_001_netinc_decline_1_accel_1(mgc_151_mgc_001_netinc_decline_1_roc_1):
    feature = _s(mgc_151_mgc_001_netinc_decline_1_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def mgc_177_mgc_007_interest_coverage_stress_252_accel_42(mgc_152_mgc_007_interest_coverage_stress_252_roc_42):
    feature = _s(mgc_152_mgc_007_interest_coverage_stress_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def mgc_178_mgc_013_netinc_decline_1_accel_126(mgc_153_mgc_013_netinc_decline_1_roc_126):
    feature = _s(mgc_153_mgc_013_netinc_decline_1_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def mgc_179_mgc_019_interest_coverage_stress_84_accel_378(mgc_154_mgc_019_interest_coverage_stress_84_roc_378):
    feature = _s(mgc_154_mgc_019_interest_coverage_stress_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def mgc_180_mgc_025_netinc_decline_1_accel_4(mgc_155_mgc_025_netinc_decline_1_roc_4):
    feature = _s(mgc_155_mgc_025_netinc_decline_1_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















MARGIN_COMPRESSION_REGISTRY_3RD_DERIVATIVES = {
    'mgc_176_mgc_001_netinc_decline_1_accel_1': {'inputs': ['mgc_151_mgc_001_netinc_decline_1_roc_1'], 'func': mgc_176_mgc_001_netinc_decline_1_accel_1},
    'mgc_177_mgc_007_interest_coverage_stress_252_accel_42': {'inputs': ['mgc_152_mgc_007_interest_coverage_stress_252_roc_42'], 'func': mgc_177_mgc_007_interest_coverage_stress_252_accel_42},
    'mgc_178_mgc_013_netinc_decline_1_accel_126': {'inputs': ['mgc_153_mgc_013_netinc_decline_1_roc_126'], 'func': mgc_178_mgc_013_netinc_decline_1_accel_126},
    'mgc_179_mgc_019_interest_coverage_stress_84_accel_378': {'inputs': ['mgc_154_mgc_019_interest_coverage_stress_84_roc_378'], 'func': mgc_179_mgc_019_interest_coverage_stress_84_accel_378},
    'mgc_180_mgc_025_netinc_decline_1_accel_4': {'inputs': ['mgc_155_mgc_025_netinc_decline_1_roc_4'], 'func': mgc_180_mgc_025_netinc_decline_1_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def mc_replacement_d3_001(mc_replacement_d2_001):
    feature = _clean(mc_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_001'] = {'inputs': ['mc_replacement_d2_001'], 'func': mc_replacement_d3_001}


def mc_replacement_d3_002(mc_replacement_d2_002):
    feature = _clean(mc_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_002'] = {'inputs': ['mc_replacement_d2_002'], 'func': mc_replacement_d3_002}


def mc_replacement_d3_003(mc_replacement_d2_003):
    feature = _clean(mc_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_003'] = {'inputs': ['mc_replacement_d2_003'], 'func': mc_replacement_d3_003}


def mc_replacement_d3_004(mc_replacement_d2_004):
    feature = _clean(mc_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_004'] = {'inputs': ['mc_replacement_d2_004'], 'func': mc_replacement_d3_004}


def mc_replacement_d3_005(mc_replacement_d2_005):
    feature = _clean(mc_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_005'] = {'inputs': ['mc_replacement_d2_005'], 'func': mc_replacement_d3_005}


def mc_replacement_d3_006(mc_replacement_d2_006):
    feature = _clean(mc_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_006'] = {'inputs': ['mc_replacement_d2_006'], 'func': mc_replacement_d3_006}


def mc_replacement_d3_007(mc_replacement_d2_007):
    feature = _clean(mc_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_007'] = {'inputs': ['mc_replacement_d2_007'], 'func': mc_replacement_d3_007}


def mc_replacement_d3_008(mc_replacement_d2_008):
    feature = _clean(mc_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_008'] = {'inputs': ['mc_replacement_d2_008'], 'func': mc_replacement_d3_008}


def mc_replacement_d3_009(mc_replacement_d2_009):
    feature = _clean(mc_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_009'] = {'inputs': ['mc_replacement_d2_009'], 'func': mc_replacement_d3_009}


def mc_replacement_d3_010(mc_replacement_d2_010):
    feature = _clean(mc_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_010'] = {'inputs': ['mc_replacement_d2_010'], 'func': mc_replacement_d3_010}


def mc_replacement_d3_011(mc_replacement_d2_011):
    feature = _clean(mc_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_011'] = {'inputs': ['mc_replacement_d2_011'], 'func': mc_replacement_d3_011}


def mc_replacement_d3_012(mc_replacement_d2_012):
    feature = _clean(mc_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_012'] = {'inputs': ['mc_replacement_d2_012'], 'func': mc_replacement_d3_012}


def mc_replacement_d3_013(mc_replacement_d2_013):
    feature = _clean(mc_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_013'] = {'inputs': ['mc_replacement_d2_013'], 'func': mc_replacement_d3_013}


def mc_replacement_d3_014(mc_replacement_d2_014):
    feature = _clean(mc_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_014'] = {'inputs': ['mc_replacement_d2_014'], 'func': mc_replacement_d3_014}


def mc_replacement_d3_015(mc_replacement_d2_015):
    feature = _clean(mc_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_015'] = {'inputs': ['mc_replacement_d2_015'], 'func': mc_replacement_d3_015}


def mc_replacement_d3_016(mc_replacement_d2_016):
    feature = _clean(mc_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_016'] = {'inputs': ['mc_replacement_d2_016'], 'func': mc_replacement_d3_016}


def mc_replacement_d3_017(mc_replacement_d2_017):
    feature = _clean(mc_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_017'] = {'inputs': ['mc_replacement_d2_017'], 'func': mc_replacement_d3_017}


def mc_replacement_d3_018(mc_replacement_d2_018):
    feature = _clean(mc_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_018'] = {'inputs': ['mc_replacement_d2_018'], 'func': mc_replacement_d3_018}


def mc_replacement_d3_019(mc_replacement_d2_019):
    feature = _clean(mc_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_019'] = {'inputs': ['mc_replacement_d2_019'], 'func': mc_replacement_d3_019}


def mc_replacement_d3_020(mc_replacement_d2_020):
    feature = _clean(mc_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_020'] = {'inputs': ['mc_replacement_d2_020'], 'func': mc_replacement_d3_020}


def mc_replacement_d3_021(mc_replacement_d2_021):
    feature = _clean(mc_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_021'] = {'inputs': ['mc_replacement_d2_021'], 'func': mc_replacement_d3_021}


def mc_replacement_d3_022(mc_replacement_d2_022):
    feature = _clean(mc_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_022'] = {'inputs': ['mc_replacement_d2_022'], 'func': mc_replacement_d3_022}


def mc_replacement_d3_023(mc_replacement_d2_023):
    feature = _clean(mc_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_023'] = {'inputs': ['mc_replacement_d2_023'], 'func': mc_replacement_d3_023}


def mc_replacement_d3_024(mc_replacement_d2_024):
    feature = _clean(mc_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_024'] = {'inputs': ['mc_replacement_d2_024'], 'func': mc_replacement_d3_024}


def mc_replacement_d3_025(mc_replacement_d2_025):
    feature = _clean(mc_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_025'] = {'inputs': ['mc_replacement_d2_025'], 'func': mc_replacement_d3_025}


def mc_replacement_d3_026(mc_replacement_d2_026):
    feature = _clean(mc_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_026'] = {'inputs': ['mc_replacement_d2_026'], 'func': mc_replacement_d3_026}


def mc_replacement_d3_027(mc_replacement_d2_027):
    feature = _clean(mc_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_027'] = {'inputs': ['mc_replacement_d2_027'], 'func': mc_replacement_d3_027}


def mc_replacement_d3_028(mc_replacement_d2_028):
    feature = _clean(mc_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_028'] = {'inputs': ['mc_replacement_d2_028'], 'func': mc_replacement_d3_028}


def mc_replacement_d3_029(mc_replacement_d2_029):
    feature = _clean(mc_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_029'] = {'inputs': ['mc_replacement_d2_029'], 'func': mc_replacement_d3_029}


def mc_replacement_d3_030(mc_replacement_d2_030):
    feature = _clean(mc_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_030'] = {'inputs': ['mc_replacement_d2_030'], 'func': mc_replacement_d3_030}


def mc_replacement_d3_031(mc_replacement_d2_031):
    feature = _clean(mc_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_031'] = {'inputs': ['mc_replacement_d2_031'], 'func': mc_replacement_d3_031}


def mc_replacement_d3_032(mc_replacement_d2_032):
    feature = _clean(mc_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_032'] = {'inputs': ['mc_replacement_d2_032'], 'func': mc_replacement_d3_032}


def mc_replacement_d3_033(mc_replacement_d2_033):
    feature = _clean(mc_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_033'] = {'inputs': ['mc_replacement_d2_033'], 'func': mc_replacement_d3_033}


def mc_replacement_d3_034(mc_replacement_d2_034):
    feature = _clean(mc_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_034'] = {'inputs': ['mc_replacement_d2_034'], 'func': mc_replacement_d3_034}


def mc_replacement_d3_035(mc_replacement_d2_035):
    feature = _clean(mc_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_035'] = {'inputs': ['mc_replacement_d2_035'], 'func': mc_replacement_d3_035}


def mc_replacement_d3_036(mc_replacement_d2_036):
    feature = _clean(mc_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_036'] = {'inputs': ['mc_replacement_d2_036'], 'func': mc_replacement_d3_036}


def mc_replacement_d3_037(mc_replacement_d2_037):
    feature = _clean(mc_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_037'] = {'inputs': ['mc_replacement_d2_037'], 'func': mc_replacement_d3_037}


def mc_replacement_d3_038(mc_replacement_d2_038):
    feature = _clean(mc_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_038'] = {'inputs': ['mc_replacement_d2_038'], 'func': mc_replacement_d3_038}


def mc_replacement_d3_039(mc_replacement_d2_039):
    feature = _clean(mc_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_039'] = {'inputs': ['mc_replacement_d2_039'], 'func': mc_replacement_d3_039}


def mc_replacement_d3_040(mc_replacement_d2_040):
    feature = _clean(mc_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_040'] = {'inputs': ['mc_replacement_d2_040'], 'func': mc_replacement_d3_040}


def mc_replacement_d3_041(mc_replacement_d2_041):
    feature = _clean(mc_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_041'] = {'inputs': ['mc_replacement_d2_041'], 'func': mc_replacement_d3_041}


def mc_replacement_d3_042(mc_replacement_d2_042):
    feature = _clean(mc_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_042'] = {'inputs': ['mc_replacement_d2_042'], 'func': mc_replacement_d3_042}


def mc_replacement_d3_043(mc_replacement_d2_043):
    feature = _clean(mc_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_043'] = {'inputs': ['mc_replacement_d2_043'], 'func': mc_replacement_d3_043}


def mc_replacement_d3_044(mc_replacement_d2_044):
    feature = _clean(mc_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_044'] = {'inputs': ['mc_replacement_d2_044'], 'func': mc_replacement_d3_044}


def mc_replacement_d3_045(mc_replacement_d2_045):
    feature = _clean(mc_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_045'] = {'inputs': ['mc_replacement_d2_045'], 'func': mc_replacement_d3_045}


def mc_replacement_d3_046(mc_replacement_d2_046):
    feature = _clean(mc_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_046'] = {'inputs': ['mc_replacement_d2_046'], 'func': mc_replacement_d3_046}


def mc_replacement_d3_047(mc_replacement_d2_047):
    feature = _clean(mc_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_047'] = {'inputs': ['mc_replacement_d2_047'], 'func': mc_replacement_d3_047}


def mc_replacement_d3_048(mc_replacement_d2_048):
    feature = _clean(mc_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_048'] = {'inputs': ['mc_replacement_d2_048'], 'func': mc_replacement_d3_048}


def mc_replacement_d3_049(mc_replacement_d2_049):
    feature = _clean(mc_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_049'] = {'inputs': ['mc_replacement_d2_049'], 'func': mc_replacement_d3_049}


def mc_replacement_d3_050(mc_replacement_d2_050):
    feature = _clean(mc_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_050'] = {'inputs': ['mc_replacement_d2_050'], 'func': mc_replacement_d3_050}


def mc_replacement_d3_051(mc_replacement_d2_051):
    feature = _clean(mc_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_051'] = {'inputs': ['mc_replacement_d2_051'], 'func': mc_replacement_d3_051}


def mc_replacement_d3_052(mc_replacement_d2_052):
    feature = _clean(mc_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_052'] = {'inputs': ['mc_replacement_d2_052'], 'func': mc_replacement_d3_052}


def mc_replacement_d3_053(mc_replacement_d2_053):
    feature = _clean(mc_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_053'] = {'inputs': ['mc_replacement_d2_053'], 'func': mc_replacement_d3_053}


def mc_replacement_d3_054(mc_replacement_d2_054):
    feature = _clean(mc_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_054'] = {'inputs': ['mc_replacement_d2_054'], 'func': mc_replacement_d3_054}


def mc_replacement_d3_055(mc_replacement_d2_055):
    feature = _clean(mc_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_055'] = {'inputs': ['mc_replacement_d2_055'], 'func': mc_replacement_d3_055}


def mc_replacement_d3_056(mc_replacement_d2_056):
    feature = _clean(mc_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_056'] = {'inputs': ['mc_replacement_d2_056'], 'func': mc_replacement_d3_056}


def mc_replacement_d3_057(mc_replacement_d2_057):
    feature = _clean(mc_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_057'] = {'inputs': ['mc_replacement_d2_057'], 'func': mc_replacement_d3_057}


def mc_replacement_d3_058(mc_replacement_d2_058):
    feature = _clean(mc_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_058'] = {'inputs': ['mc_replacement_d2_058'], 'func': mc_replacement_d3_058}


def mc_replacement_d3_059(mc_replacement_d2_059):
    feature = _clean(mc_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_059'] = {'inputs': ['mc_replacement_d2_059'], 'func': mc_replacement_d3_059}


def mc_replacement_d3_060(mc_replacement_d2_060):
    feature = _clean(mc_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_060'] = {'inputs': ['mc_replacement_d2_060'], 'func': mc_replacement_d3_060}


def mc_replacement_d3_061(mc_replacement_d2_061):
    feature = _clean(mc_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_061'] = {'inputs': ['mc_replacement_d2_061'], 'func': mc_replacement_d3_061}


def mc_replacement_d3_062(mc_replacement_d2_062):
    feature = _clean(mc_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_062'] = {'inputs': ['mc_replacement_d2_062'], 'func': mc_replacement_d3_062}


def mc_replacement_d3_063(mc_replacement_d2_063):
    feature = _clean(mc_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_063'] = {'inputs': ['mc_replacement_d2_063'], 'func': mc_replacement_d3_063}


def mc_replacement_d3_064(mc_replacement_d2_064):
    feature = _clean(mc_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_064'] = {'inputs': ['mc_replacement_d2_064'], 'func': mc_replacement_d3_064}


def mc_replacement_d3_065(mc_replacement_d2_065):
    feature = _clean(mc_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_065'] = {'inputs': ['mc_replacement_d2_065'], 'func': mc_replacement_d3_065}


def mc_replacement_d3_066(mc_replacement_d2_066):
    feature = _clean(mc_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_066'] = {'inputs': ['mc_replacement_d2_066'], 'func': mc_replacement_d3_066}


def mc_replacement_d3_067(mc_replacement_d2_067):
    feature = _clean(mc_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_067'] = {'inputs': ['mc_replacement_d2_067'], 'func': mc_replacement_d3_067}


def mc_replacement_d3_068(mc_replacement_d2_068):
    feature = _clean(mc_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_068'] = {'inputs': ['mc_replacement_d2_068'], 'func': mc_replacement_d3_068}


def mc_replacement_d3_069(mc_replacement_d2_069):
    feature = _clean(mc_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_069'] = {'inputs': ['mc_replacement_d2_069'], 'func': mc_replacement_d3_069}


def mc_replacement_d3_070(mc_replacement_d2_070):
    feature = _clean(mc_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_070'] = {'inputs': ['mc_replacement_d2_070'], 'func': mc_replacement_d3_070}


def mc_replacement_d3_071(mc_replacement_d2_071):
    feature = _clean(mc_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_071'] = {'inputs': ['mc_replacement_d2_071'], 'func': mc_replacement_d3_071}


def mc_replacement_d3_072(mc_replacement_d2_072):
    feature = _clean(mc_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_072'] = {'inputs': ['mc_replacement_d2_072'], 'func': mc_replacement_d3_072}


def mc_replacement_d3_073(mc_replacement_d2_073):
    feature = _clean(mc_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_073'] = {'inputs': ['mc_replacement_d2_073'], 'func': mc_replacement_d3_073}


def mc_replacement_d3_074(mc_replacement_d2_074):
    feature = _clean(mc_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_074'] = {'inputs': ['mc_replacement_d2_074'], 'func': mc_replacement_d3_074}


def mc_replacement_d3_075(mc_replacement_d2_075):
    feature = _clean(mc_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_075'] = {'inputs': ['mc_replacement_d2_075'], 'func': mc_replacement_d3_075}


def mc_replacement_d3_076(mc_replacement_d2_076):
    feature = _clean(mc_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_076'] = {'inputs': ['mc_replacement_d2_076'], 'func': mc_replacement_d3_076}


def mc_replacement_d3_077(mc_replacement_d2_077):
    feature = _clean(mc_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_077'] = {'inputs': ['mc_replacement_d2_077'], 'func': mc_replacement_d3_077}


def mc_replacement_d3_078(mc_replacement_d2_078):
    feature = _clean(mc_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_078'] = {'inputs': ['mc_replacement_d2_078'], 'func': mc_replacement_d3_078}


def mc_replacement_d3_079(mc_replacement_d2_079):
    feature = _clean(mc_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_079'] = {'inputs': ['mc_replacement_d2_079'], 'func': mc_replacement_d3_079}


def mc_replacement_d3_080(mc_replacement_d2_080):
    feature = _clean(mc_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_080'] = {'inputs': ['mc_replacement_d2_080'], 'func': mc_replacement_d3_080}


def mc_replacement_d3_081(mc_replacement_d2_081):
    feature = _clean(mc_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_081'] = {'inputs': ['mc_replacement_d2_081'], 'func': mc_replacement_d3_081}


def mc_replacement_d3_082(mc_replacement_d2_082):
    feature = _clean(mc_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_082'] = {'inputs': ['mc_replacement_d2_082'], 'func': mc_replacement_d3_082}


def mc_replacement_d3_083(mc_replacement_d2_083):
    feature = _clean(mc_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_083'] = {'inputs': ['mc_replacement_d2_083'], 'func': mc_replacement_d3_083}


def mc_replacement_d3_084(mc_replacement_d2_084):
    feature = _clean(mc_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_084'] = {'inputs': ['mc_replacement_d2_084'], 'func': mc_replacement_d3_084}


def mc_replacement_d3_085(mc_replacement_d2_085):
    feature = _clean(mc_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_085'] = {'inputs': ['mc_replacement_d2_085'], 'func': mc_replacement_d3_085}


def mc_replacement_d3_086(mc_replacement_d2_086):
    feature = _clean(mc_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_086'] = {'inputs': ['mc_replacement_d2_086'], 'func': mc_replacement_d3_086}


def mc_replacement_d3_087(mc_replacement_d2_087):
    feature = _clean(mc_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_087'] = {'inputs': ['mc_replacement_d2_087'], 'func': mc_replacement_d3_087}


def mc_replacement_d3_088(mc_replacement_d2_088):
    feature = _clean(mc_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_088'] = {'inputs': ['mc_replacement_d2_088'], 'func': mc_replacement_d3_088}


def mc_replacement_d3_089(mc_replacement_d2_089):
    feature = _clean(mc_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_089'] = {'inputs': ['mc_replacement_d2_089'], 'func': mc_replacement_d3_089}


def mc_replacement_d3_090(mc_replacement_d2_090):
    feature = _clean(mc_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_090'] = {'inputs': ['mc_replacement_d2_090'], 'func': mc_replacement_d3_090}


def mc_replacement_d3_091(mc_replacement_d2_091):
    feature = _clean(mc_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_091'] = {'inputs': ['mc_replacement_d2_091'], 'func': mc_replacement_d3_091}


def mc_replacement_d3_092(mc_replacement_d2_092):
    feature = _clean(mc_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_092'] = {'inputs': ['mc_replacement_d2_092'], 'func': mc_replacement_d3_092}


def mc_replacement_d3_093(mc_replacement_d2_093):
    feature = _clean(mc_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_093'] = {'inputs': ['mc_replacement_d2_093'], 'func': mc_replacement_d3_093}


def mc_replacement_d3_094(mc_replacement_d2_094):
    feature = _clean(mc_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_094'] = {'inputs': ['mc_replacement_d2_094'], 'func': mc_replacement_d3_094}


def mc_replacement_d3_095(mc_replacement_d2_095):
    feature = _clean(mc_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_095'] = {'inputs': ['mc_replacement_d2_095'], 'func': mc_replacement_d3_095}


def mc_replacement_d3_096(mc_replacement_d2_096):
    feature = _clean(mc_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_096'] = {'inputs': ['mc_replacement_d2_096'], 'func': mc_replacement_d3_096}


def mc_replacement_d3_097(mc_replacement_d2_097):
    feature = _clean(mc_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_097'] = {'inputs': ['mc_replacement_d2_097'], 'func': mc_replacement_d3_097}


def mc_replacement_d3_098(mc_replacement_d2_098):
    feature = _clean(mc_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_098'] = {'inputs': ['mc_replacement_d2_098'], 'func': mc_replacement_d3_098}


def mc_replacement_d3_099(mc_replacement_d2_099):
    feature = _clean(mc_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_099'] = {'inputs': ['mc_replacement_d2_099'], 'func': mc_replacement_d3_099}


def mc_replacement_d3_100(mc_replacement_d2_100):
    feature = _clean(mc_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_100'] = {'inputs': ['mc_replacement_d2_100'], 'func': mc_replacement_d3_100}


def mc_replacement_d3_101(mc_replacement_d2_101):
    feature = _clean(mc_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_101'] = {'inputs': ['mc_replacement_d2_101'], 'func': mc_replacement_d3_101}


def mc_replacement_d3_102(mc_replacement_d2_102):
    feature = _clean(mc_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_102'] = {'inputs': ['mc_replacement_d2_102'], 'func': mc_replacement_d3_102}


def mc_replacement_d3_103(mc_replacement_d2_103):
    feature = _clean(mc_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_103'] = {'inputs': ['mc_replacement_d2_103'], 'func': mc_replacement_d3_103}


def mc_replacement_d3_104(mc_replacement_d2_104):
    feature = _clean(mc_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_104'] = {'inputs': ['mc_replacement_d2_104'], 'func': mc_replacement_d3_104}


def mc_replacement_d3_105(mc_replacement_d2_105):
    feature = _clean(mc_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_105'] = {'inputs': ['mc_replacement_d2_105'], 'func': mc_replacement_d3_105}


def mc_replacement_d3_106(mc_replacement_d2_106):
    feature = _clean(mc_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_106'] = {'inputs': ['mc_replacement_d2_106'], 'func': mc_replacement_d3_106}


def mc_replacement_d3_107(mc_replacement_d2_107):
    feature = _clean(mc_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_107'] = {'inputs': ['mc_replacement_d2_107'], 'func': mc_replacement_d3_107}


def mc_replacement_d3_108(mc_replacement_d2_108):
    feature = _clean(mc_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_108'] = {'inputs': ['mc_replacement_d2_108'], 'func': mc_replacement_d3_108}


def mc_replacement_d3_109(mc_replacement_d2_109):
    feature = _clean(mc_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_109'] = {'inputs': ['mc_replacement_d2_109'], 'func': mc_replacement_d3_109}


def mc_replacement_d3_110(mc_replacement_d2_110):
    feature = _clean(mc_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_110'] = {'inputs': ['mc_replacement_d2_110'], 'func': mc_replacement_d3_110}


def mc_replacement_d3_111(mc_replacement_d2_111):
    feature = _clean(mc_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_111'] = {'inputs': ['mc_replacement_d2_111'], 'func': mc_replacement_d3_111}


def mc_replacement_d3_112(mc_replacement_d2_112):
    feature = _clean(mc_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_112'] = {'inputs': ['mc_replacement_d2_112'], 'func': mc_replacement_d3_112}


def mc_replacement_d3_113(mc_replacement_d2_113):
    feature = _clean(mc_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_113'] = {'inputs': ['mc_replacement_d2_113'], 'func': mc_replacement_d3_113}


def mc_replacement_d3_114(mc_replacement_d2_114):
    feature = _clean(mc_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_114'] = {'inputs': ['mc_replacement_d2_114'], 'func': mc_replacement_d3_114}


def mc_replacement_d3_115(mc_replacement_d2_115):
    feature = _clean(mc_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_115'] = {'inputs': ['mc_replacement_d2_115'], 'func': mc_replacement_d3_115}


def mc_replacement_d3_116(mc_replacement_d2_116):
    feature = _clean(mc_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_116'] = {'inputs': ['mc_replacement_d2_116'], 'func': mc_replacement_d3_116}


def mc_replacement_d3_117(mc_replacement_d2_117):
    feature = _clean(mc_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_117'] = {'inputs': ['mc_replacement_d2_117'], 'func': mc_replacement_d3_117}


def mc_replacement_d3_118(mc_replacement_d2_118):
    feature = _clean(mc_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_118'] = {'inputs': ['mc_replacement_d2_118'], 'func': mc_replacement_d3_118}


def mc_replacement_d3_119(mc_replacement_d2_119):
    feature = _clean(mc_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_119'] = {'inputs': ['mc_replacement_d2_119'], 'func': mc_replacement_d3_119}


def mc_replacement_d3_120(mc_replacement_d2_120):
    feature = _clean(mc_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_120'] = {'inputs': ['mc_replacement_d2_120'], 'func': mc_replacement_d3_120}


def mc_replacement_d3_121(mc_replacement_d2_121):
    feature = _clean(mc_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_121'] = {'inputs': ['mc_replacement_d2_121'], 'func': mc_replacement_d3_121}


def mc_replacement_d3_122(mc_replacement_d2_122):
    feature = _clean(mc_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_122'] = {'inputs': ['mc_replacement_d2_122'], 'func': mc_replacement_d3_122}


def mc_replacement_d3_123(mc_replacement_d2_123):
    feature = _clean(mc_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_123'] = {'inputs': ['mc_replacement_d2_123'], 'func': mc_replacement_d3_123}


def mc_replacement_d3_124(mc_replacement_d2_124):
    feature = _clean(mc_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_124'] = {'inputs': ['mc_replacement_d2_124'], 'func': mc_replacement_d3_124}


def mc_replacement_d3_125(mc_replacement_d2_125):
    feature = _clean(mc_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_125'] = {'inputs': ['mc_replacement_d2_125'], 'func': mc_replacement_d3_125}


def mc_replacement_d3_126(mc_replacement_d2_126):
    feature = _clean(mc_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_126'] = {'inputs': ['mc_replacement_d2_126'], 'func': mc_replacement_d3_126}


def mc_replacement_d3_127(mc_replacement_d2_127):
    feature = _clean(mc_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_127'] = {'inputs': ['mc_replacement_d2_127'], 'func': mc_replacement_d3_127}


def mc_replacement_d3_128(mc_replacement_d2_128):
    feature = _clean(mc_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_128'] = {'inputs': ['mc_replacement_d2_128'], 'func': mc_replacement_d3_128}


def mc_replacement_d3_129(mc_replacement_d2_129):
    feature = _clean(mc_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_129'] = {'inputs': ['mc_replacement_d2_129'], 'func': mc_replacement_d3_129}


def mc_replacement_d3_130(mc_replacement_d2_130):
    feature = _clean(mc_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_130'] = {'inputs': ['mc_replacement_d2_130'], 'func': mc_replacement_d3_130}


def mc_replacement_d3_131(mc_replacement_d2_131):
    feature = _clean(mc_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_131'] = {'inputs': ['mc_replacement_d2_131'], 'func': mc_replacement_d3_131}


def mc_replacement_d3_132(mc_replacement_d2_132):
    feature = _clean(mc_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_132'] = {'inputs': ['mc_replacement_d2_132'], 'func': mc_replacement_d3_132}


def mc_replacement_d3_133(mc_replacement_d2_133):
    feature = _clean(mc_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_133'] = {'inputs': ['mc_replacement_d2_133'], 'func': mc_replacement_d3_133}


def mc_replacement_d3_134(mc_replacement_d2_134):
    feature = _clean(mc_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_134'] = {'inputs': ['mc_replacement_d2_134'], 'func': mc_replacement_d3_134}


def mc_replacement_d3_135(mc_replacement_d2_135):
    feature = _clean(mc_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_135'] = {'inputs': ['mc_replacement_d2_135'], 'func': mc_replacement_d3_135}


def mc_replacement_d3_136(mc_replacement_d2_136):
    feature = _clean(mc_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_136'] = {'inputs': ['mc_replacement_d2_136'], 'func': mc_replacement_d3_136}


def mc_replacement_d3_137(mc_replacement_d2_137):
    feature = _clean(mc_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_137'] = {'inputs': ['mc_replacement_d2_137'], 'func': mc_replacement_d3_137}


def mc_replacement_d3_138(mc_replacement_d2_138):
    feature = _clean(mc_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_138'] = {'inputs': ['mc_replacement_d2_138'], 'func': mc_replacement_d3_138}


def mc_replacement_d3_139(mc_replacement_d2_139):
    feature = _clean(mc_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_139'] = {'inputs': ['mc_replacement_d2_139'], 'func': mc_replacement_d3_139}


def mc_replacement_d3_140(mc_replacement_d2_140):
    feature = _clean(mc_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_140'] = {'inputs': ['mc_replacement_d2_140'], 'func': mc_replacement_d3_140}


def mc_replacement_d3_141(mc_replacement_d2_141):
    feature = _clean(mc_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_141'] = {'inputs': ['mc_replacement_d2_141'], 'func': mc_replacement_d3_141}


def mc_replacement_d3_142(mc_replacement_d2_142):
    feature = _clean(mc_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_142'] = {'inputs': ['mc_replacement_d2_142'], 'func': mc_replacement_d3_142}


def mc_replacement_d3_143(mc_replacement_d2_143):
    feature = _clean(mc_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_143'] = {'inputs': ['mc_replacement_d2_143'], 'func': mc_replacement_d3_143}


def mc_replacement_d3_144(mc_replacement_d2_144):
    feature = _clean(mc_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_144'] = {'inputs': ['mc_replacement_d2_144'], 'func': mc_replacement_d3_144}


def mc_replacement_d3_145(mc_replacement_d2_145):
    feature = _clean(mc_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_145'] = {'inputs': ['mc_replacement_d2_145'], 'func': mc_replacement_d3_145}


def mc_replacement_d3_146(mc_replacement_d2_146):
    feature = _clean(mc_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_146'] = {'inputs': ['mc_replacement_d2_146'], 'func': mc_replacement_d3_146}


def mc_replacement_d3_147(mc_replacement_d2_147):
    feature = _clean(mc_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_147'] = {'inputs': ['mc_replacement_d2_147'], 'func': mc_replacement_d3_147}


def mc_replacement_d3_148(mc_replacement_d2_148):
    feature = _clean(mc_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_148'] = {'inputs': ['mc_replacement_d2_148'], 'func': mc_replacement_d3_148}


def mc_replacement_d3_149(mc_replacement_d2_149):
    feature = _clean(mc_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_149'] = {'inputs': ['mc_replacement_d2_149'], 'func': mc_replacement_d3_149}


def mc_replacement_d3_150(mc_replacement_d2_150):
    feature = _clean(mc_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_150'] = {'inputs': ['mc_replacement_d2_150'], 'func': mc_replacement_d3_150}


def mc_replacement_d3_151(mc_replacement_d2_151):
    feature = _clean(mc_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_151'] = {'inputs': ['mc_replacement_d2_151'], 'func': mc_replacement_d3_151}


def mc_replacement_d3_152(mc_replacement_d2_152):
    feature = _clean(mc_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_152'] = {'inputs': ['mc_replacement_d2_152'], 'func': mc_replacement_d3_152}


def mc_replacement_d3_153(mc_replacement_d2_153):
    feature = _clean(mc_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_153'] = {'inputs': ['mc_replacement_d2_153'], 'func': mc_replacement_d3_153}


def mc_replacement_d3_154(mc_replacement_d2_154):
    feature = _clean(mc_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_154'] = {'inputs': ['mc_replacement_d2_154'], 'func': mc_replacement_d3_154}


def mc_replacement_d3_155(mc_replacement_d2_155):
    feature = _clean(mc_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_155'] = {'inputs': ['mc_replacement_d2_155'], 'func': mc_replacement_d3_155}


def mc_replacement_d3_156(mc_replacement_d2_156):
    feature = _clean(mc_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_156'] = {'inputs': ['mc_replacement_d2_156'], 'func': mc_replacement_d3_156}


def mc_replacement_d3_157(mc_replacement_d2_157):
    feature = _clean(mc_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_157'] = {'inputs': ['mc_replacement_d2_157'], 'func': mc_replacement_d3_157}


def mc_replacement_d3_158(mc_replacement_d2_158):
    feature = _clean(mc_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_158'] = {'inputs': ['mc_replacement_d2_158'], 'func': mc_replacement_d3_158}


def mc_replacement_d3_159(mc_replacement_d2_159):
    feature = _clean(mc_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_159'] = {'inputs': ['mc_replacement_d2_159'], 'func': mc_replacement_d3_159}


def mc_replacement_d3_160(mc_replacement_d2_160):
    feature = _clean(mc_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_160'] = {'inputs': ['mc_replacement_d2_160'], 'func': mc_replacement_d3_160}


def mc_replacement_d3_161(mc_replacement_d2_161):
    feature = _clean(mc_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_161'] = {'inputs': ['mc_replacement_d2_161'], 'func': mc_replacement_d3_161}


def mc_replacement_d3_162(mc_replacement_d2_162):
    feature = _clean(mc_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_162'] = {'inputs': ['mc_replacement_d2_162'], 'func': mc_replacement_d3_162}


def mc_replacement_d3_163(mc_replacement_d2_163):
    feature = _clean(mc_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_163'] = {'inputs': ['mc_replacement_d2_163'], 'func': mc_replacement_d3_163}


def mc_replacement_d3_164(mc_replacement_d2_164):
    feature = _clean(mc_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_164'] = {'inputs': ['mc_replacement_d2_164'], 'func': mc_replacement_d3_164}


def mc_replacement_d3_165(mc_replacement_d2_165):
    feature = _clean(mc_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_165'] = {'inputs': ['mc_replacement_d2_165'], 'func': mc_replacement_d3_165}


def mc_replacement_d3_166(mc_replacement_d2_166):
    feature = _clean(mc_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
MC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mc_replacement_d3_166'] = {'inputs': ['mc_replacement_d2_166'], 'func': mc_replacement_d3_166}


# Third-derivative extensions for repaired first-base features.
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def mgc_base_universe_d3_001_mgc_003_fcf_burn_to_cash_63(mgc_base_universe_d2_001_mgc_003_fcf_burn_to_cash_63):
    return _base_universe_d3(mgc_base_universe_d2_001_mgc_003_fcf_burn_to_cash_63, 1)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_001_mgc_003_fcf_burn_to_cash_63'] = {'inputs': ['mgc_base_universe_d2_001_mgc_003_fcf_burn_to_cash_63'], 'func': mgc_base_universe_d3_001_mgc_003_fcf_burn_to_cash_63}


def mgc_base_universe_d3_002_mgc_004_debt_to_equity_84(mgc_base_universe_d2_002_mgc_004_debt_to_equity_84):
    return _base_universe_d3(mgc_base_universe_d2_002_mgc_004_debt_to_equity_84, 2)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_002_mgc_004_debt_to_equity_84'] = {'inputs': ['mgc_base_universe_d2_002_mgc_004_debt_to_equity_84'], 'func': mgc_base_universe_d3_002_mgc_004_debt_to_equity_84}


def mgc_base_universe_d3_003_mgc_005_debt_to_assets_126(mgc_base_universe_d2_003_mgc_005_debt_to_assets_126):
    return _base_universe_d3(mgc_base_universe_d2_003_mgc_005_debt_to_assets_126, 3)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_003_mgc_005_debt_to_assets_126'] = {'inputs': ['mgc_base_universe_d2_003_mgc_005_debt_to_assets_126'], 'func': mgc_base_universe_d3_003_mgc_005_debt_to_assets_126}


def mgc_base_universe_d3_004_mgc_012_accrual_gap_1260(mgc_base_universe_d2_004_mgc_012_accrual_gap_1260):
    return _base_universe_d3(mgc_base_universe_d2_004_mgc_012_accrual_gap_1260, 4)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_004_mgc_012_accrual_gap_1260'] = {'inputs': ['mgc_base_universe_d2_004_mgc_012_accrual_gap_1260'], 'func': mgc_base_universe_d3_004_mgc_012_accrual_gap_1260}


def mgc_base_universe_d3_005_mgc_016_debt_to_equity_21(mgc_base_universe_d2_005_mgc_016_debt_to_equity_21):
    return _base_universe_d3(mgc_base_universe_d2_005_mgc_016_debt_to_equity_21, 5)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_005_mgc_016_debt_to_equity_21'] = {'inputs': ['mgc_base_universe_d2_005_mgc_016_debt_to_equity_21'], 'func': mgc_base_universe_d3_005_mgc_016_debt_to_equity_21}


def mgc_base_universe_d3_006_mgc_017_debt_to_assets_42(mgc_base_universe_d2_006_mgc_017_debt_to_assets_42):
    return _base_universe_d3(mgc_base_universe_d2_006_mgc_017_debt_to_assets_42, 6)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_006_mgc_017_debt_to_assets_42'] = {'inputs': ['mgc_base_universe_d2_006_mgc_017_debt_to_assets_42'], 'func': mgc_base_universe_d3_006_mgc_017_debt_to_assets_42}


def mgc_base_universe_d3_007_mgc_024_accrual_gap_504(mgc_base_universe_d2_007_mgc_024_accrual_gap_504):
    return _base_universe_d3(mgc_base_universe_d2_007_mgc_024_accrual_gap_504, 7)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_007_mgc_024_accrual_gap_504'] = {'inputs': ['mgc_base_universe_d2_007_mgc_024_accrual_gap_504'], 'func': mgc_base_universe_d3_007_mgc_024_accrual_gap_504}


def mgc_base_universe_d3_008_mgc_027_fcf_burn_to_cash_1260(mgc_base_universe_d2_008_mgc_027_fcf_burn_to_cash_1260):
    return _base_universe_d3(mgc_base_universe_d2_008_mgc_027_fcf_burn_to_cash_1260, 8)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_008_mgc_027_fcf_burn_to_cash_1260'] = {'inputs': ['mgc_base_universe_d2_008_mgc_027_fcf_burn_to_cash_1260'], 'func': mgc_base_universe_d3_008_mgc_027_fcf_burn_to_cash_1260}


def mgc_base_universe_d3_009_mgc_028_debt_to_equity_1512(mgc_base_universe_d2_009_mgc_028_debt_to_equity_1512):
    return _base_universe_d3(mgc_base_universe_d2_009_mgc_028_debt_to_equity_1512, 9)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_009_mgc_028_debt_to_equity_1512'] = {'inputs': ['mgc_base_universe_d2_009_mgc_028_debt_to_equity_1512'], 'func': mgc_base_universe_d3_009_mgc_028_debt_to_equity_1512}


def mgc_base_universe_d3_010_mgc_029_debt_to_assets_63(mgc_base_universe_d2_010_mgc_029_debt_to_assets_63):
    return _base_universe_d3(mgc_base_universe_d2_010_mgc_029_debt_to_assets_63, 10)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_010_mgc_029_debt_to_assets_63'] = {'inputs': ['mgc_base_universe_d2_010_mgc_029_debt_to_assets_63'], 'func': mgc_base_universe_d3_010_mgc_029_debt_to_assets_63}


def mgc_base_universe_d3_011_mgc_031_interest_coverage_stress_21(mgc_base_universe_d2_011_mgc_031_interest_coverage_stress_21):
    return _base_universe_d3(mgc_base_universe_d2_011_mgc_031_interest_coverage_stress_21, 11)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_011_mgc_031_interest_coverage_stress_21'] = {'inputs': ['mgc_base_universe_d2_011_mgc_031_interest_coverage_stress_21'], 'func': mgc_base_universe_d3_011_mgc_031_interest_coverage_stress_21}


def mgc_base_universe_d3_012_mgc_036_accrual_gap_189(mgc_base_universe_d2_012_mgc_036_accrual_gap_189):
    return _base_universe_d3(mgc_base_universe_d2_012_mgc_036_accrual_gap_189, 12)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_012_mgc_036_accrual_gap_189'] = {'inputs': ['mgc_base_universe_d2_012_mgc_036_accrual_gap_189'], 'func': mgc_base_universe_d3_012_mgc_036_accrual_gap_189}


def mgc_base_universe_d3_013_mgc_039_fcf_burn_to_cash_504(mgc_base_universe_d2_013_mgc_039_fcf_burn_to_cash_504):
    return _base_universe_d3(mgc_base_universe_d2_013_mgc_039_fcf_burn_to_cash_504, 13)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_013_mgc_039_fcf_burn_to_cash_504'] = {'inputs': ['mgc_base_universe_d2_013_mgc_039_fcf_burn_to_cash_504'], 'func': mgc_base_universe_d3_013_mgc_039_fcf_burn_to_cash_504}


def mgc_base_universe_d3_014_mgc_040_debt_to_equity_756(mgc_base_universe_d2_014_mgc_040_debt_to_equity_756):
    return _base_universe_d3(mgc_base_universe_d2_014_mgc_040_debt_to_equity_756, 14)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_014_mgc_040_debt_to_equity_756'] = {'inputs': ['mgc_base_universe_d2_014_mgc_040_debt_to_equity_756'], 'func': mgc_base_universe_d3_014_mgc_040_debt_to_equity_756}


def mgc_base_universe_d3_015_mgc_041_debt_to_assets_1008(mgc_base_universe_d2_015_mgc_041_debt_to_assets_1008):
    return _base_universe_d3(mgc_base_universe_d2_015_mgc_041_debt_to_assets_1008, 15)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_015_mgc_041_debt_to_assets_1008'] = {'inputs': ['mgc_base_universe_d2_015_mgc_041_debt_to_assets_1008'], 'func': mgc_base_universe_d3_015_mgc_041_debt_to_assets_1008}


def mgc_base_universe_d3_016_mgc_043_interest_coverage_stress_1512(mgc_base_universe_d2_016_mgc_043_interest_coverage_stress_1512):
    return _base_universe_d3(mgc_base_universe_d2_016_mgc_043_interest_coverage_stress_1512, 16)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_016_mgc_043_interest_coverage_stress_1512'] = {'inputs': ['mgc_base_universe_d2_016_mgc_043_interest_coverage_stress_1512'], 'func': mgc_base_universe_d3_016_mgc_043_interest_coverage_stress_1512}


def mgc_base_universe_d3_017_mgc_048_accrual_gap_63(mgc_base_universe_d2_017_mgc_048_accrual_gap_63):
    return _base_universe_d3(mgc_base_universe_d2_017_mgc_048_accrual_gap_63, 17)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_017_mgc_048_accrual_gap_63'] = {'inputs': ['mgc_base_universe_d2_017_mgc_048_accrual_gap_63'], 'func': mgc_base_universe_d3_017_mgc_048_accrual_gap_63}


def mgc_base_universe_d3_018_mgc_051_fcf_burn_to_cash_189(mgc_base_universe_d2_018_mgc_051_fcf_burn_to_cash_189):
    return _base_universe_d3(mgc_base_universe_d2_018_mgc_051_fcf_burn_to_cash_189, 18)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_018_mgc_051_fcf_burn_to_cash_189'] = {'inputs': ['mgc_base_universe_d2_018_mgc_051_fcf_burn_to_cash_189'], 'func': mgc_base_universe_d3_018_mgc_051_fcf_burn_to_cash_189}


def mgc_base_universe_d3_019_mgc_052_debt_to_equity_252(mgc_base_universe_d2_019_mgc_052_debt_to_equity_252):
    return _base_universe_d3(mgc_base_universe_d2_019_mgc_052_debt_to_equity_252, 19)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_019_mgc_052_debt_to_equity_252'] = {'inputs': ['mgc_base_universe_d2_019_mgc_052_debt_to_equity_252'], 'func': mgc_base_universe_d3_019_mgc_052_debt_to_equity_252}


def mgc_base_universe_d3_020_mgc_053_debt_to_assets_378(mgc_base_universe_d2_020_mgc_053_debt_to_assets_378):
    return _base_universe_d3(mgc_base_universe_d2_020_mgc_053_debt_to_assets_378, 20)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_020_mgc_053_debt_to_assets_378'] = {'inputs': ['mgc_base_universe_d2_020_mgc_053_debt_to_assets_378'], 'func': mgc_base_universe_d3_020_mgc_053_debt_to_assets_378}


def mgc_base_universe_d3_021_mgc_055_interest_coverage_stress_756(mgc_base_universe_d2_021_mgc_055_interest_coverage_stress_756):
    return _base_universe_d3(mgc_base_universe_d2_021_mgc_055_interest_coverage_stress_756, 21)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_021_mgc_055_interest_coverage_stress_756'] = {'inputs': ['mgc_base_universe_d2_021_mgc_055_interest_coverage_stress_756'], 'func': mgc_base_universe_d3_021_mgc_055_interest_coverage_stress_756}


def mgc_base_universe_d3_022_mgc_060_accrual_gap_252(mgc_base_universe_d2_022_mgc_060_accrual_gap_252):
    return _base_universe_d3(mgc_base_universe_d2_022_mgc_060_accrual_gap_252, 22)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_022_mgc_060_accrual_gap_252'] = {'inputs': ['mgc_base_universe_d2_022_mgc_060_accrual_gap_252'], 'func': mgc_base_universe_d3_022_mgc_060_accrual_gap_252}


def mgc_base_universe_d3_023_mgc_basefill_001(mgc_base_universe_d2_023_mgc_basefill_001):
    return _base_universe_d3(mgc_base_universe_d2_023_mgc_basefill_001, 23)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_023_mgc_basefill_001'] = {'inputs': ['mgc_base_universe_d2_023_mgc_basefill_001'], 'func': mgc_base_universe_d3_023_mgc_basefill_001}


def mgc_base_universe_d3_024_mgc_basefill_002(mgc_base_universe_d2_024_mgc_basefill_002):
    return _base_universe_d3(mgc_base_universe_d2_024_mgc_basefill_002, 24)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_024_mgc_basefill_002'] = {'inputs': ['mgc_base_universe_d2_024_mgc_basefill_002'], 'func': mgc_base_universe_d3_024_mgc_basefill_002}


def mgc_base_universe_d3_025_mgc_basefill_006(mgc_base_universe_d2_025_mgc_basefill_006):
    return _base_universe_d3(mgc_base_universe_d2_025_mgc_basefill_006, 25)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_025_mgc_basefill_006'] = {'inputs': ['mgc_base_universe_d2_025_mgc_basefill_006'], 'func': mgc_base_universe_d3_025_mgc_basefill_006}


def mgc_base_universe_d3_026_mgc_basefill_008(mgc_base_universe_d2_026_mgc_basefill_008):
    return _base_universe_d3(mgc_base_universe_d2_026_mgc_basefill_008, 26)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_026_mgc_basefill_008'] = {'inputs': ['mgc_base_universe_d2_026_mgc_basefill_008'], 'func': mgc_base_universe_d3_026_mgc_basefill_008}


def mgc_base_universe_d3_027_mgc_basefill_009(mgc_base_universe_d2_027_mgc_basefill_009):
    return _base_universe_d3(mgc_base_universe_d2_027_mgc_basefill_009, 27)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_027_mgc_basefill_009'] = {'inputs': ['mgc_base_universe_d2_027_mgc_basefill_009'], 'func': mgc_base_universe_d3_027_mgc_basefill_009}


def mgc_base_universe_d3_028_mgc_basefill_010(mgc_base_universe_d2_028_mgc_basefill_010):
    return _base_universe_d3(mgc_base_universe_d2_028_mgc_basefill_010, 28)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_028_mgc_basefill_010'] = {'inputs': ['mgc_base_universe_d2_028_mgc_basefill_010'], 'func': mgc_base_universe_d3_028_mgc_basefill_010}


def mgc_base_universe_d3_029_mgc_basefill_011(mgc_base_universe_d2_029_mgc_basefill_011):
    return _base_universe_d3(mgc_base_universe_d2_029_mgc_basefill_011, 29)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_029_mgc_basefill_011'] = {'inputs': ['mgc_base_universe_d2_029_mgc_basefill_011'], 'func': mgc_base_universe_d3_029_mgc_basefill_011}


def mgc_base_universe_d3_030_mgc_basefill_013(mgc_base_universe_d2_030_mgc_basefill_013):
    return _base_universe_d3(mgc_base_universe_d2_030_mgc_basefill_013, 30)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_030_mgc_basefill_013'] = {'inputs': ['mgc_base_universe_d2_030_mgc_basefill_013'], 'func': mgc_base_universe_d3_030_mgc_basefill_013}


def mgc_base_universe_d3_031_mgc_basefill_014(mgc_base_universe_d2_031_mgc_basefill_014):
    return _base_universe_d3(mgc_base_universe_d2_031_mgc_basefill_014, 31)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_031_mgc_basefill_014'] = {'inputs': ['mgc_base_universe_d2_031_mgc_basefill_014'], 'func': mgc_base_universe_d3_031_mgc_basefill_014}


def mgc_base_universe_d3_032_mgc_basefill_015(mgc_base_universe_d2_032_mgc_basefill_015):
    return _base_universe_d3(mgc_base_universe_d2_032_mgc_basefill_015, 32)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_032_mgc_basefill_015'] = {'inputs': ['mgc_base_universe_d2_032_mgc_basefill_015'], 'func': mgc_base_universe_d3_032_mgc_basefill_015}


def mgc_base_universe_d3_033_mgc_basefill_018(mgc_base_universe_d2_033_mgc_basefill_018):
    return _base_universe_d3(mgc_base_universe_d2_033_mgc_basefill_018, 33)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_033_mgc_basefill_018'] = {'inputs': ['mgc_base_universe_d2_033_mgc_basefill_018'], 'func': mgc_base_universe_d3_033_mgc_basefill_018}


def mgc_base_universe_d3_034_mgc_basefill_020(mgc_base_universe_d2_034_mgc_basefill_020):
    return _base_universe_d3(mgc_base_universe_d2_034_mgc_basefill_020, 34)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_034_mgc_basefill_020'] = {'inputs': ['mgc_base_universe_d2_034_mgc_basefill_020'], 'func': mgc_base_universe_d3_034_mgc_basefill_020}


def mgc_base_universe_d3_035_mgc_basefill_021(mgc_base_universe_d2_035_mgc_basefill_021):
    return _base_universe_d3(mgc_base_universe_d2_035_mgc_basefill_021, 35)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_035_mgc_basefill_021'] = {'inputs': ['mgc_base_universe_d2_035_mgc_basefill_021'], 'func': mgc_base_universe_d3_035_mgc_basefill_021}


def mgc_base_universe_d3_036_mgc_basefill_022(mgc_base_universe_d2_036_mgc_basefill_022):
    return _base_universe_d3(mgc_base_universe_d2_036_mgc_basefill_022, 36)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_036_mgc_basefill_022'] = {'inputs': ['mgc_base_universe_d2_036_mgc_basefill_022'], 'func': mgc_base_universe_d3_036_mgc_basefill_022}


def mgc_base_universe_d3_037_mgc_basefill_023(mgc_base_universe_d2_037_mgc_basefill_023):
    return _base_universe_d3(mgc_base_universe_d2_037_mgc_basefill_023, 37)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_037_mgc_basefill_023'] = {'inputs': ['mgc_base_universe_d2_037_mgc_basefill_023'], 'func': mgc_base_universe_d3_037_mgc_basefill_023}


def mgc_base_universe_d3_038_mgc_basefill_025(mgc_base_universe_d2_038_mgc_basefill_025):
    return _base_universe_d3(mgc_base_universe_d2_038_mgc_basefill_025, 38)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_038_mgc_basefill_025'] = {'inputs': ['mgc_base_universe_d2_038_mgc_basefill_025'], 'func': mgc_base_universe_d3_038_mgc_basefill_025}


def mgc_base_universe_d3_039_mgc_basefill_026(mgc_base_universe_d2_039_mgc_basefill_026):
    return _base_universe_d3(mgc_base_universe_d2_039_mgc_basefill_026, 39)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_039_mgc_basefill_026'] = {'inputs': ['mgc_base_universe_d2_039_mgc_basefill_026'], 'func': mgc_base_universe_d3_039_mgc_basefill_026}


def mgc_base_universe_d3_040_mgc_basefill_030(mgc_base_universe_d2_040_mgc_basefill_030):
    return _base_universe_d3(mgc_base_universe_d2_040_mgc_basefill_030, 40)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_040_mgc_basefill_030'] = {'inputs': ['mgc_base_universe_d2_040_mgc_basefill_030'], 'func': mgc_base_universe_d3_040_mgc_basefill_030}


def mgc_base_universe_d3_041_mgc_basefill_032(mgc_base_universe_d2_041_mgc_basefill_032):
    return _base_universe_d3(mgc_base_universe_d2_041_mgc_basefill_032, 41)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_041_mgc_basefill_032'] = {'inputs': ['mgc_base_universe_d2_041_mgc_basefill_032'], 'func': mgc_base_universe_d3_041_mgc_basefill_032}


def mgc_base_universe_d3_042_mgc_basefill_033(mgc_base_universe_d2_042_mgc_basefill_033):
    return _base_universe_d3(mgc_base_universe_d2_042_mgc_basefill_033, 42)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_042_mgc_basefill_033'] = {'inputs': ['mgc_base_universe_d2_042_mgc_basefill_033'], 'func': mgc_base_universe_d3_042_mgc_basefill_033}


def mgc_base_universe_d3_043_mgc_basefill_034(mgc_base_universe_d2_043_mgc_basefill_034):
    return _base_universe_d3(mgc_base_universe_d2_043_mgc_basefill_034, 43)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_043_mgc_basefill_034'] = {'inputs': ['mgc_base_universe_d2_043_mgc_basefill_034'], 'func': mgc_base_universe_d3_043_mgc_basefill_034}


def mgc_base_universe_d3_044_mgc_basefill_035(mgc_base_universe_d2_044_mgc_basefill_035):
    return _base_universe_d3(mgc_base_universe_d2_044_mgc_basefill_035, 44)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_044_mgc_basefill_035'] = {'inputs': ['mgc_base_universe_d2_044_mgc_basefill_035'], 'func': mgc_base_universe_d3_044_mgc_basefill_035}


def mgc_base_universe_d3_045_mgc_basefill_037(mgc_base_universe_d2_045_mgc_basefill_037):
    return _base_universe_d3(mgc_base_universe_d2_045_mgc_basefill_037, 45)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_045_mgc_basefill_037'] = {'inputs': ['mgc_base_universe_d2_045_mgc_basefill_037'], 'func': mgc_base_universe_d3_045_mgc_basefill_037}


def mgc_base_universe_d3_046_mgc_basefill_038(mgc_base_universe_d2_046_mgc_basefill_038):
    return _base_universe_d3(mgc_base_universe_d2_046_mgc_basefill_038, 46)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_046_mgc_basefill_038'] = {'inputs': ['mgc_base_universe_d2_046_mgc_basefill_038'], 'func': mgc_base_universe_d3_046_mgc_basefill_038}


def mgc_base_universe_d3_047_mgc_basefill_042(mgc_base_universe_d2_047_mgc_basefill_042):
    return _base_universe_d3(mgc_base_universe_d2_047_mgc_basefill_042, 47)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_047_mgc_basefill_042'] = {'inputs': ['mgc_base_universe_d2_047_mgc_basefill_042'], 'func': mgc_base_universe_d3_047_mgc_basefill_042}


def mgc_base_universe_d3_048_mgc_basefill_044(mgc_base_universe_d2_048_mgc_basefill_044):
    return _base_universe_d3(mgc_base_universe_d2_048_mgc_basefill_044, 48)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_048_mgc_basefill_044'] = {'inputs': ['mgc_base_universe_d2_048_mgc_basefill_044'], 'func': mgc_base_universe_d3_048_mgc_basefill_044}


def mgc_base_universe_d3_049_mgc_basefill_045(mgc_base_universe_d2_049_mgc_basefill_045):
    return _base_universe_d3(mgc_base_universe_d2_049_mgc_basefill_045, 49)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_049_mgc_basefill_045'] = {'inputs': ['mgc_base_universe_d2_049_mgc_basefill_045'], 'func': mgc_base_universe_d3_049_mgc_basefill_045}


def mgc_base_universe_d3_050_mgc_basefill_046(mgc_base_universe_d2_050_mgc_basefill_046):
    return _base_universe_d3(mgc_base_universe_d2_050_mgc_basefill_046, 50)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_050_mgc_basefill_046'] = {'inputs': ['mgc_base_universe_d2_050_mgc_basefill_046'], 'func': mgc_base_universe_d3_050_mgc_basefill_046}


def mgc_base_universe_d3_051_mgc_basefill_047(mgc_base_universe_d2_051_mgc_basefill_047):
    return _base_universe_d3(mgc_base_universe_d2_051_mgc_basefill_047, 51)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_051_mgc_basefill_047'] = {'inputs': ['mgc_base_universe_d2_051_mgc_basefill_047'], 'func': mgc_base_universe_d3_051_mgc_basefill_047}


def mgc_base_universe_d3_052_mgc_basefill_049(mgc_base_universe_d2_052_mgc_basefill_049):
    return _base_universe_d3(mgc_base_universe_d2_052_mgc_basefill_049, 52)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_052_mgc_basefill_049'] = {'inputs': ['mgc_base_universe_d2_052_mgc_basefill_049'], 'func': mgc_base_universe_d3_052_mgc_basefill_049}


def mgc_base_universe_d3_053_mgc_basefill_050(mgc_base_universe_d2_053_mgc_basefill_050):
    return _base_universe_d3(mgc_base_universe_d2_053_mgc_basefill_050, 53)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_053_mgc_basefill_050'] = {'inputs': ['mgc_base_universe_d2_053_mgc_basefill_050'], 'func': mgc_base_universe_d3_053_mgc_basefill_050}


def mgc_base_universe_d3_054_mgc_basefill_054(mgc_base_universe_d2_054_mgc_basefill_054):
    return _base_universe_d3(mgc_base_universe_d2_054_mgc_basefill_054, 54)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_054_mgc_basefill_054'] = {'inputs': ['mgc_base_universe_d2_054_mgc_basefill_054'], 'func': mgc_base_universe_d3_054_mgc_basefill_054}


def mgc_base_universe_d3_055_mgc_basefill_056(mgc_base_universe_d2_055_mgc_basefill_056):
    return _base_universe_d3(mgc_base_universe_d2_055_mgc_basefill_056, 55)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_055_mgc_basefill_056'] = {'inputs': ['mgc_base_universe_d2_055_mgc_basefill_056'], 'func': mgc_base_universe_d3_055_mgc_basefill_056}


def mgc_base_universe_d3_056_mgc_basefill_057(mgc_base_universe_d2_056_mgc_basefill_057):
    return _base_universe_d3(mgc_base_universe_d2_056_mgc_basefill_057, 56)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_056_mgc_basefill_057'] = {'inputs': ['mgc_base_universe_d2_056_mgc_basefill_057'], 'func': mgc_base_universe_d3_056_mgc_basefill_057}


def mgc_base_universe_d3_057_mgc_basefill_058(mgc_base_universe_d2_057_mgc_basefill_058):
    return _base_universe_d3(mgc_base_universe_d2_057_mgc_basefill_058, 57)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_057_mgc_basefill_058'] = {'inputs': ['mgc_base_universe_d2_057_mgc_basefill_058'], 'func': mgc_base_universe_d3_057_mgc_basefill_058}


def mgc_base_universe_d3_058_mgc_basefill_059(mgc_base_universe_d2_058_mgc_basefill_059):
    return _base_universe_d3(mgc_base_universe_d2_058_mgc_basefill_059, 58)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_058_mgc_basefill_059'] = {'inputs': ['mgc_base_universe_d2_058_mgc_basefill_059'], 'func': mgc_base_universe_d3_058_mgc_basefill_059}


def mgc_base_universe_d3_059_mgc_basefill_061(mgc_base_universe_d2_059_mgc_basefill_061):
    return _base_universe_d3(mgc_base_universe_d2_059_mgc_basefill_061, 59)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_059_mgc_basefill_061'] = {'inputs': ['mgc_base_universe_d2_059_mgc_basefill_061'], 'func': mgc_base_universe_d3_059_mgc_basefill_061}


def mgc_base_universe_d3_060_mgc_basefill_062(mgc_base_universe_d2_060_mgc_basefill_062):
    return _base_universe_d3(mgc_base_universe_d2_060_mgc_basefill_062, 60)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_060_mgc_basefill_062'] = {'inputs': ['mgc_base_universe_d2_060_mgc_basefill_062'], 'func': mgc_base_universe_d3_060_mgc_basefill_062}


def mgc_base_universe_d3_061_mgc_basefill_063(mgc_base_universe_d2_061_mgc_basefill_063):
    return _base_universe_d3(mgc_base_universe_d2_061_mgc_basefill_063, 61)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_061_mgc_basefill_063'] = {'inputs': ['mgc_base_universe_d2_061_mgc_basefill_063'], 'func': mgc_base_universe_d3_061_mgc_basefill_063}


def mgc_base_universe_d3_062_mgc_basefill_064(mgc_base_universe_d2_062_mgc_basefill_064):
    return _base_universe_d3(mgc_base_universe_d2_062_mgc_basefill_064, 62)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_062_mgc_basefill_064'] = {'inputs': ['mgc_base_universe_d2_062_mgc_basefill_064'], 'func': mgc_base_universe_d3_062_mgc_basefill_064}


def mgc_base_universe_d3_063_mgc_basefill_065(mgc_base_universe_d2_063_mgc_basefill_065):
    return _base_universe_d3(mgc_base_universe_d2_063_mgc_basefill_065, 63)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_063_mgc_basefill_065'] = {'inputs': ['mgc_base_universe_d2_063_mgc_basefill_065'], 'func': mgc_base_universe_d3_063_mgc_basefill_065}


def mgc_base_universe_d3_064_mgc_basefill_066(mgc_base_universe_d2_064_mgc_basefill_066):
    return _base_universe_d3(mgc_base_universe_d2_064_mgc_basefill_066, 64)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_064_mgc_basefill_066'] = {'inputs': ['mgc_base_universe_d2_064_mgc_basefill_066'], 'func': mgc_base_universe_d3_064_mgc_basefill_066}


def mgc_base_universe_d3_065_mgc_basefill_067(mgc_base_universe_d2_065_mgc_basefill_067):
    return _base_universe_d3(mgc_base_universe_d2_065_mgc_basefill_067, 65)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_065_mgc_basefill_067'] = {'inputs': ['mgc_base_universe_d2_065_mgc_basefill_067'], 'func': mgc_base_universe_d3_065_mgc_basefill_067}


def mgc_base_universe_d3_066_mgc_basefill_068(mgc_base_universe_d2_066_mgc_basefill_068):
    return _base_universe_d3(mgc_base_universe_d2_066_mgc_basefill_068, 66)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_066_mgc_basefill_068'] = {'inputs': ['mgc_base_universe_d2_066_mgc_basefill_068'], 'func': mgc_base_universe_d3_066_mgc_basefill_068}


def mgc_base_universe_d3_067_mgc_basefill_069(mgc_base_universe_d2_067_mgc_basefill_069):
    return _base_universe_d3(mgc_base_universe_d2_067_mgc_basefill_069, 67)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_067_mgc_basefill_069'] = {'inputs': ['mgc_base_universe_d2_067_mgc_basefill_069'], 'func': mgc_base_universe_d3_067_mgc_basefill_069}


def mgc_base_universe_d3_068_mgc_basefill_070(mgc_base_universe_d2_068_mgc_basefill_070):
    return _base_universe_d3(mgc_base_universe_d2_068_mgc_basefill_070, 68)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_068_mgc_basefill_070'] = {'inputs': ['mgc_base_universe_d2_068_mgc_basefill_070'], 'func': mgc_base_universe_d3_068_mgc_basefill_070}


def mgc_base_universe_d3_069_mgc_basefill_071(mgc_base_universe_d2_069_mgc_basefill_071):
    return _base_universe_d3(mgc_base_universe_d2_069_mgc_basefill_071, 69)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_069_mgc_basefill_071'] = {'inputs': ['mgc_base_universe_d2_069_mgc_basefill_071'], 'func': mgc_base_universe_d3_069_mgc_basefill_071}


def mgc_base_universe_d3_070_mgc_basefill_072(mgc_base_universe_d2_070_mgc_basefill_072):
    return _base_universe_d3(mgc_base_universe_d2_070_mgc_basefill_072, 70)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_070_mgc_basefill_072'] = {'inputs': ['mgc_base_universe_d2_070_mgc_basefill_072'], 'func': mgc_base_universe_d3_070_mgc_basefill_072}


def mgc_base_universe_d3_071_mgc_basefill_073(mgc_base_universe_d2_071_mgc_basefill_073):
    return _base_universe_d3(mgc_base_universe_d2_071_mgc_basefill_073, 71)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_071_mgc_basefill_073'] = {'inputs': ['mgc_base_universe_d2_071_mgc_basefill_073'], 'func': mgc_base_universe_d3_071_mgc_basefill_073}


def mgc_base_universe_d3_072_mgc_basefill_074(mgc_base_universe_d2_072_mgc_basefill_074):
    return _base_universe_d3(mgc_base_universe_d2_072_mgc_basefill_074, 72)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_072_mgc_basefill_074'] = {'inputs': ['mgc_base_universe_d2_072_mgc_basefill_074'], 'func': mgc_base_universe_d3_072_mgc_basefill_074}


def mgc_base_universe_d3_073_mgc_basefill_075(mgc_base_universe_d2_073_mgc_basefill_075):
    return _base_universe_d3(mgc_base_universe_d2_073_mgc_basefill_075, 73)
MGC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mgc_base_universe_d3_073_mgc_basefill_075'] = {'inputs': ['mgc_base_universe_d2_073_mgc_basefill_075'], 'func': mgc_base_universe_d3_073_mgc_basefill_075}
