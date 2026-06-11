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



def lqd_176_lqd_001_netinc_decline_1_accel_1(lqd_151_lqd_001_netinc_decline_1_roc_1):
    feature = _s(lqd_151_lqd_001_netinc_decline_1_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def lqd_177_lqd_007_interest_coverage_stress_252_accel_42(lqd_152_lqd_007_interest_coverage_stress_252_roc_42):
    feature = _s(lqd_152_lqd_007_interest_coverage_stress_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def lqd_178_lqd_013_netinc_decline_1_accel_126(lqd_153_lqd_013_netinc_decline_1_roc_126):
    feature = _s(lqd_153_lqd_013_netinc_decline_1_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def lqd_179_lqd_019_interest_coverage_stress_84_accel_378(lqd_154_lqd_019_interest_coverage_stress_84_roc_378):
    feature = _s(lqd_154_lqd_019_interest_coverage_stress_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def lqd_180_lqd_025_netinc_decline_1_accel_4(lqd_155_lqd_025_netinc_decline_1_roc_4):
    feature = _s(lqd_155_lqd_025_netinc_decline_1_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















LIQUIDITY_DISTRESS_REGISTRY_3RD_DERIVATIVES = {
    'lqd_176_lqd_001_netinc_decline_1_accel_1': {'inputs': ['lqd_151_lqd_001_netinc_decline_1_roc_1'], 'func': lqd_176_lqd_001_netinc_decline_1_accel_1},
    'lqd_177_lqd_007_interest_coverage_stress_252_accel_42': {'inputs': ['lqd_152_lqd_007_interest_coverage_stress_252_roc_42'], 'func': lqd_177_lqd_007_interest_coverage_stress_252_accel_42},
    'lqd_178_lqd_013_netinc_decline_1_accel_126': {'inputs': ['lqd_153_lqd_013_netinc_decline_1_roc_126'], 'func': lqd_178_lqd_013_netinc_decline_1_accel_126},
    'lqd_179_lqd_019_interest_coverage_stress_84_accel_378': {'inputs': ['lqd_154_lqd_019_interest_coverage_stress_84_roc_378'], 'func': lqd_179_lqd_019_interest_coverage_stress_84_accel_378},
    'lqd_180_lqd_025_netinc_decline_1_accel_4': {'inputs': ['lqd_155_lqd_025_netinc_decline_1_roc_4'], 'func': lqd_180_lqd_025_netinc_decline_1_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def ld_replacement_d3_001(ld_replacement_d2_001):
    feature = _clean(ld_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_001'] = {'inputs': ['ld_replacement_d2_001'], 'func': ld_replacement_d3_001}


def ld_replacement_d3_002(ld_replacement_d2_002):
    feature = _clean(ld_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_002'] = {'inputs': ['ld_replacement_d2_002'], 'func': ld_replacement_d3_002}


def ld_replacement_d3_003(ld_replacement_d2_003):
    feature = _clean(ld_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_003'] = {'inputs': ['ld_replacement_d2_003'], 'func': ld_replacement_d3_003}


def ld_replacement_d3_004(ld_replacement_d2_004):
    feature = _clean(ld_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_004'] = {'inputs': ['ld_replacement_d2_004'], 'func': ld_replacement_d3_004}


def ld_replacement_d3_005(ld_replacement_d2_005):
    feature = _clean(ld_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_005'] = {'inputs': ['ld_replacement_d2_005'], 'func': ld_replacement_d3_005}


def ld_replacement_d3_006(ld_replacement_d2_006):
    feature = _clean(ld_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_006'] = {'inputs': ['ld_replacement_d2_006'], 'func': ld_replacement_d3_006}


def ld_replacement_d3_007(ld_replacement_d2_007):
    feature = _clean(ld_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_007'] = {'inputs': ['ld_replacement_d2_007'], 'func': ld_replacement_d3_007}


def ld_replacement_d3_008(ld_replacement_d2_008):
    feature = _clean(ld_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_008'] = {'inputs': ['ld_replacement_d2_008'], 'func': ld_replacement_d3_008}


def ld_replacement_d3_009(ld_replacement_d2_009):
    feature = _clean(ld_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_009'] = {'inputs': ['ld_replacement_d2_009'], 'func': ld_replacement_d3_009}


def ld_replacement_d3_010(ld_replacement_d2_010):
    feature = _clean(ld_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_010'] = {'inputs': ['ld_replacement_d2_010'], 'func': ld_replacement_d3_010}


def ld_replacement_d3_011(ld_replacement_d2_011):
    feature = _clean(ld_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_011'] = {'inputs': ['ld_replacement_d2_011'], 'func': ld_replacement_d3_011}


def ld_replacement_d3_012(ld_replacement_d2_012):
    feature = _clean(ld_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_012'] = {'inputs': ['ld_replacement_d2_012'], 'func': ld_replacement_d3_012}


def ld_replacement_d3_013(ld_replacement_d2_013):
    feature = _clean(ld_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_013'] = {'inputs': ['ld_replacement_d2_013'], 'func': ld_replacement_d3_013}


def ld_replacement_d3_014(ld_replacement_d2_014):
    feature = _clean(ld_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_014'] = {'inputs': ['ld_replacement_d2_014'], 'func': ld_replacement_d3_014}


def ld_replacement_d3_015(ld_replacement_d2_015):
    feature = _clean(ld_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_015'] = {'inputs': ['ld_replacement_d2_015'], 'func': ld_replacement_d3_015}


def ld_replacement_d3_016(ld_replacement_d2_016):
    feature = _clean(ld_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_016'] = {'inputs': ['ld_replacement_d2_016'], 'func': ld_replacement_d3_016}


def ld_replacement_d3_017(ld_replacement_d2_017):
    feature = _clean(ld_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_017'] = {'inputs': ['ld_replacement_d2_017'], 'func': ld_replacement_d3_017}


def ld_replacement_d3_018(ld_replacement_d2_018):
    feature = _clean(ld_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_018'] = {'inputs': ['ld_replacement_d2_018'], 'func': ld_replacement_d3_018}


def ld_replacement_d3_019(ld_replacement_d2_019):
    feature = _clean(ld_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_019'] = {'inputs': ['ld_replacement_d2_019'], 'func': ld_replacement_d3_019}


def ld_replacement_d3_020(ld_replacement_d2_020):
    feature = _clean(ld_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_020'] = {'inputs': ['ld_replacement_d2_020'], 'func': ld_replacement_d3_020}


def ld_replacement_d3_021(ld_replacement_d2_021):
    feature = _clean(ld_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_021'] = {'inputs': ['ld_replacement_d2_021'], 'func': ld_replacement_d3_021}


def ld_replacement_d3_022(ld_replacement_d2_022):
    feature = _clean(ld_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_022'] = {'inputs': ['ld_replacement_d2_022'], 'func': ld_replacement_d3_022}


def ld_replacement_d3_023(ld_replacement_d2_023):
    feature = _clean(ld_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_023'] = {'inputs': ['ld_replacement_d2_023'], 'func': ld_replacement_d3_023}


def ld_replacement_d3_024(ld_replacement_d2_024):
    feature = _clean(ld_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_024'] = {'inputs': ['ld_replacement_d2_024'], 'func': ld_replacement_d3_024}


def ld_replacement_d3_025(ld_replacement_d2_025):
    feature = _clean(ld_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_025'] = {'inputs': ['ld_replacement_d2_025'], 'func': ld_replacement_d3_025}


def ld_replacement_d3_026(ld_replacement_d2_026):
    feature = _clean(ld_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_026'] = {'inputs': ['ld_replacement_d2_026'], 'func': ld_replacement_d3_026}


def ld_replacement_d3_027(ld_replacement_d2_027):
    feature = _clean(ld_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_027'] = {'inputs': ['ld_replacement_d2_027'], 'func': ld_replacement_d3_027}


def ld_replacement_d3_028(ld_replacement_d2_028):
    feature = _clean(ld_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_028'] = {'inputs': ['ld_replacement_d2_028'], 'func': ld_replacement_d3_028}


def ld_replacement_d3_029(ld_replacement_d2_029):
    feature = _clean(ld_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_029'] = {'inputs': ['ld_replacement_d2_029'], 'func': ld_replacement_d3_029}


def ld_replacement_d3_030(ld_replacement_d2_030):
    feature = _clean(ld_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_030'] = {'inputs': ['ld_replacement_d2_030'], 'func': ld_replacement_d3_030}


def ld_replacement_d3_031(ld_replacement_d2_031):
    feature = _clean(ld_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_031'] = {'inputs': ['ld_replacement_d2_031'], 'func': ld_replacement_d3_031}


def ld_replacement_d3_032(ld_replacement_d2_032):
    feature = _clean(ld_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_032'] = {'inputs': ['ld_replacement_d2_032'], 'func': ld_replacement_d3_032}


def ld_replacement_d3_033(ld_replacement_d2_033):
    feature = _clean(ld_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_033'] = {'inputs': ['ld_replacement_d2_033'], 'func': ld_replacement_d3_033}


def ld_replacement_d3_034(ld_replacement_d2_034):
    feature = _clean(ld_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_034'] = {'inputs': ['ld_replacement_d2_034'], 'func': ld_replacement_d3_034}


def ld_replacement_d3_035(ld_replacement_d2_035):
    feature = _clean(ld_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_035'] = {'inputs': ['ld_replacement_d2_035'], 'func': ld_replacement_d3_035}


def ld_replacement_d3_036(ld_replacement_d2_036):
    feature = _clean(ld_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_036'] = {'inputs': ['ld_replacement_d2_036'], 'func': ld_replacement_d3_036}


def ld_replacement_d3_037(ld_replacement_d2_037):
    feature = _clean(ld_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_037'] = {'inputs': ['ld_replacement_d2_037'], 'func': ld_replacement_d3_037}


def ld_replacement_d3_038(ld_replacement_d2_038):
    feature = _clean(ld_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_038'] = {'inputs': ['ld_replacement_d2_038'], 'func': ld_replacement_d3_038}


def ld_replacement_d3_039(ld_replacement_d2_039):
    feature = _clean(ld_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_039'] = {'inputs': ['ld_replacement_d2_039'], 'func': ld_replacement_d3_039}


def ld_replacement_d3_040(ld_replacement_d2_040):
    feature = _clean(ld_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_040'] = {'inputs': ['ld_replacement_d2_040'], 'func': ld_replacement_d3_040}


def ld_replacement_d3_041(ld_replacement_d2_041):
    feature = _clean(ld_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_041'] = {'inputs': ['ld_replacement_d2_041'], 'func': ld_replacement_d3_041}


def ld_replacement_d3_042(ld_replacement_d2_042):
    feature = _clean(ld_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_042'] = {'inputs': ['ld_replacement_d2_042'], 'func': ld_replacement_d3_042}


def ld_replacement_d3_043(ld_replacement_d2_043):
    feature = _clean(ld_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_043'] = {'inputs': ['ld_replacement_d2_043'], 'func': ld_replacement_d3_043}


def ld_replacement_d3_044(ld_replacement_d2_044):
    feature = _clean(ld_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_044'] = {'inputs': ['ld_replacement_d2_044'], 'func': ld_replacement_d3_044}


def ld_replacement_d3_045(ld_replacement_d2_045):
    feature = _clean(ld_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_045'] = {'inputs': ['ld_replacement_d2_045'], 'func': ld_replacement_d3_045}


def ld_replacement_d3_046(ld_replacement_d2_046):
    feature = _clean(ld_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_046'] = {'inputs': ['ld_replacement_d2_046'], 'func': ld_replacement_d3_046}


def ld_replacement_d3_047(ld_replacement_d2_047):
    feature = _clean(ld_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_047'] = {'inputs': ['ld_replacement_d2_047'], 'func': ld_replacement_d3_047}


def ld_replacement_d3_048(ld_replacement_d2_048):
    feature = _clean(ld_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_048'] = {'inputs': ['ld_replacement_d2_048'], 'func': ld_replacement_d3_048}


def ld_replacement_d3_049(ld_replacement_d2_049):
    feature = _clean(ld_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_049'] = {'inputs': ['ld_replacement_d2_049'], 'func': ld_replacement_d3_049}


def ld_replacement_d3_050(ld_replacement_d2_050):
    feature = _clean(ld_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_050'] = {'inputs': ['ld_replacement_d2_050'], 'func': ld_replacement_d3_050}


def ld_replacement_d3_051(ld_replacement_d2_051):
    feature = _clean(ld_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_051'] = {'inputs': ['ld_replacement_d2_051'], 'func': ld_replacement_d3_051}


def ld_replacement_d3_052(ld_replacement_d2_052):
    feature = _clean(ld_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_052'] = {'inputs': ['ld_replacement_d2_052'], 'func': ld_replacement_d3_052}


def ld_replacement_d3_053(ld_replacement_d2_053):
    feature = _clean(ld_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_053'] = {'inputs': ['ld_replacement_d2_053'], 'func': ld_replacement_d3_053}


def ld_replacement_d3_054(ld_replacement_d2_054):
    feature = _clean(ld_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_054'] = {'inputs': ['ld_replacement_d2_054'], 'func': ld_replacement_d3_054}


def ld_replacement_d3_055(ld_replacement_d2_055):
    feature = _clean(ld_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_055'] = {'inputs': ['ld_replacement_d2_055'], 'func': ld_replacement_d3_055}


def ld_replacement_d3_056(ld_replacement_d2_056):
    feature = _clean(ld_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_056'] = {'inputs': ['ld_replacement_d2_056'], 'func': ld_replacement_d3_056}


def ld_replacement_d3_057(ld_replacement_d2_057):
    feature = _clean(ld_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_057'] = {'inputs': ['ld_replacement_d2_057'], 'func': ld_replacement_d3_057}


def ld_replacement_d3_058(ld_replacement_d2_058):
    feature = _clean(ld_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_058'] = {'inputs': ['ld_replacement_d2_058'], 'func': ld_replacement_d3_058}


def ld_replacement_d3_059(ld_replacement_d2_059):
    feature = _clean(ld_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_059'] = {'inputs': ['ld_replacement_d2_059'], 'func': ld_replacement_d3_059}


def ld_replacement_d3_060(ld_replacement_d2_060):
    feature = _clean(ld_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_060'] = {'inputs': ['ld_replacement_d2_060'], 'func': ld_replacement_d3_060}


def ld_replacement_d3_061(ld_replacement_d2_061):
    feature = _clean(ld_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_061'] = {'inputs': ['ld_replacement_d2_061'], 'func': ld_replacement_d3_061}


def ld_replacement_d3_062(ld_replacement_d2_062):
    feature = _clean(ld_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_062'] = {'inputs': ['ld_replacement_d2_062'], 'func': ld_replacement_d3_062}


def ld_replacement_d3_063(ld_replacement_d2_063):
    feature = _clean(ld_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_063'] = {'inputs': ['ld_replacement_d2_063'], 'func': ld_replacement_d3_063}


def ld_replacement_d3_064(ld_replacement_d2_064):
    feature = _clean(ld_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_064'] = {'inputs': ['ld_replacement_d2_064'], 'func': ld_replacement_d3_064}


def ld_replacement_d3_065(ld_replacement_d2_065):
    feature = _clean(ld_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_065'] = {'inputs': ['ld_replacement_d2_065'], 'func': ld_replacement_d3_065}


def ld_replacement_d3_066(ld_replacement_d2_066):
    feature = _clean(ld_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_066'] = {'inputs': ['ld_replacement_d2_066'], 'func': ld_replacement_d3_066}


def ld_replacement_d3_067(ld_replacement_d2_067):
    feature = _clean(ld_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_067'] = {'inputs': ['ld_replacement_d2_067'], 'func': ld_replacement_d3_067}


def ld_replacement_d3_068(ld_replacement_d2_068):
    feature = _clean(ld_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_068'] = {'inputs': ['ld_replacement_d2_068'], 'func': ld_replacement_d3_068}


def ld_replacement_d3_069(ld_replacement_d2_069):
    feature = _clean(ld_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_069'] = {'inputs': ['ld_replacement_d2_069'], 'func': ld_replacement_d3_069}


def ld_replacement_d3_070(ld_replacement_d2_070):
    feature = _clean(ld_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_070'] = {'inputs': ['ld_replacement_d2_070'], 'func': ld_replacement_d3_070}


def ld_replacement_d3_071(ld_replacement_d2_071):
    feature = _clean(ld_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_071'] = {'inputs': ['ld_replacement_d2_071'], 'func': ld_replacement_d3_071}


def ld_replacement_d3_072(ld_replacement_d2_072):
    feature = _clean(ld_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_072'] = {'inputs': ['ld_replacement_d2_072'], 'func': ld_replacement_d3_072}


def ld_replacement_d3_073(ld_replacement_d2_073):
    feature = _clean(ld_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_073'] = {'inputs': ['ld_replacement_d2_073'], 'func': ld_replacement_d3_073}


def ld_replacement_d3_074(ld_replacement_d2_074):
    feature = _clean(ld_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_074'] = {'inputs': ['ld_replacement_d2_074'], 'func': ld_replacement_d3_074}


def ld_replacement_d3_075(ld_replacement_d2_075):
    feature = _clean(ld_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_075'] = {'inputs': ['ld_replacement_d2_075'], 'func': ld_replacement_d3_075}


def ld_replacement_d3_076(ld_replacement_d2_076):
    feature = _clean(ld_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_076'] = {'inputs': ['ld_replacement_d2_076'], 'func': ld_replacement_d3_076}


def ld_replacement_d3_077(ld_replacement_d2_077):
    feature = _clean(ld_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_077'] = {'inputs': ['ld_replacement_d2_077'], 'func': ld_replacement_d3_077}


def ld_replacement_d3_078(ld_replacement_d2_078):
    feature = _clean(ld_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_078'] = {'inputs': ['ld_replacement_d2_078'], 'func': ld_replacement_d3_078}


def ld_replacement_d3_079(ld_replacement_d2_079):
    feature = _clean(ld_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_079'] = {'inputs': ['ld_replacement_d2_079'], 'func': ld_replacement_d3_079}


def ld_replacement_d3_080(ld_replacement_d2_080):
    feature = _clean(ld_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_080'] = {'inputs': ['ld_replacement_d2_080'], 'func': ld_replacement_d3_080}


def ld_replacement_d3_081(ld_replacement_d2_081):
    feature = _clean(ld_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_081'] = {'inputs': ['ld_replacement_d2_081'], 'func': ld_replacement_d3_081}


def ld_replacement_d3_082(ld_replacement_d2_082):
    feature = _clean(ld_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_082'] = {'inputs': ['ld_replacement_d2_082'], 'func': ld_replacement_d3_082}


def ld_replacement_d3_083(ld_replacement_d2_083):
    feature = _clean(ld_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_083'] = {'inputs': ['ld_replacement_d2_083'], 'func': ld_replacement_d3_083}


def ld_replacement_d3_084(ld_replacement_d2_084):
    feature = _clean(ld_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_084'] = {'inputs': ['ld_replacement_d2_084'], 'func': ld_replacement_d3_084}


def ld_replacement_d3_085(ld_replacement_d2_085):
    feature = _clean(ld_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_085'] = {'inputs': ['ld_replacement_d2_085'], 'func': ld_replacement_d3_085}


def ld_replacement_d3_086(ld_replacement_d2_086):
    feature = _clean(ld_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_086'] = {'inputs': ['ld_replacement_d2_086'], 'func': ld_replacement_d3_086}


def ld_replacement_d3_087(ld_replacement_d2_087):
    feature = _clean(ld_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_087'] = {'inputs': ['ld_replacement_d2_087'], 'func': ld_replacement_d3_087}


def ld_replacement_d3_088(ld_replacement_d2_088):
    feature = _clean(ld_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_088'] = {'inputs': ['ld_replacement_d2_088'], 'func': ld_replacement_d3_088}


def ld_replacement_d3_089(ld_replacement_d2_089):
    feature = _clean(ld_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_089'] = {'inputs': ['ld_replacement_d2_089'], 'func': ld_replacement_d3_089}


def ld_replacement_d3_090(ld_replacement_d2_090):
    feature = _clean(ld_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_090'] = {'inputs': ['ld_replacement_d2_090'], 'func': ld_replacement_d3_090}


def ld_replacement_d3_091(ld_replacement_d2_091):
    feature = _clean(ld_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_091'] = {'inputs': ['ld_replacement_d2_091'], 'func': ld_replacement_d3_091}


def ld_replacement_d3_092(ld_replacement_d2_092):
    feature = _clean(ld_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_092'] = {'inputs': ['ld_replacement_d2_092'], 'func': ld_replacement_d3_092}


def ld_replacement_d3_093(ld_replacement_d2_093):
    feature = _clean(ld_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_093'] = {'inputs': ['ld_replacement_d2_093'], 'func': ld_replacement_d3_093}


def ld_replacement_d3_094(ld_replacement_d2_094):
    feature = _clean(ld_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_094'] = {'inputs': ['ld_replacement_d2_094'], 'func': ld_replacement_d3_094}


def ld_replacement_d3_095(ld_replacement_d2_095):
    feature = _clean(ld_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_095'] = {'inputs': ['ld_replacement_d2_095'], 'func': ld_replacement_d3_095}


def ld_replacement_d3_096(ld_replacement_d2_096):
    feature = _clean(ld_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_096'] = {'inputs': ['ld_replacement_d2_096'], 'func': ld_replacement_d3_096}


def ld_replacement_d3_097(ld_replacement_d2_097):
    feature = _clean(ld_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_097'] = {'inputs': ['ld_replacement_d2_097'], 'func': ld_replacement_d3_097}


def ld_replacement_d3_098(ld_replacement_d2_098):
    feature = _clean(ld_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_098'] = {'inputs': ['ld_replacement_d2_098'], 'func': ld_replacement_d3_098}


def ld_replacement_d3_099(ld_replacement_d2_099):
    feature = _clean(ld_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_099'] = {'inputs': ['ld_replacement_d2_099'], 'func': ld_replacement_d3_099}


def ld_replacement_d3_100(ld_replacement_d2_100):
    feature = _clean(ld_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_100'] = {'inputs': ['ld_replacement_d2_100'], 'func': ld_replacement_d3_100}


def ld_replacement_d3_101(ld_replacement_d2_101):
    feature = _clean(ld_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_101'] = {'inputs': ['ld_replacement_d2_101'], 'func': ld_replacement_d3_101}


def ld_replacement_d3_102(ld_replacement_d2_102):
    feature = _clean(ld_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_102'] = {'inputs': ['ld_replacement_d2_102'], 'func': ld_replacement_d3_102}


def ld_replacement_d3_103(ld_replacement_d2_103):
    feature = _clean(ld_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_103'] = {'inputs': ['ld_replacement_d2_103'], 'func': ld_replacement_d3_103}


def ld_replacement_d3_104(ld_replacement_d2_104):
    feature = _clean(ld_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_104'] = {'inputs': ['ld_replacement_d2_104'], 'func': ld_replacement_d3_104}


def ld_replacement_d3_105(ld_replacement_d2_105):
    feature = _clean(ld_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_105'] = {'inputs': ['ld_replacement_d2_105'], 'func': ld_replacement_d3_105}


def ld_replacement_d3_106(ld_replacement_d2_106):
    feature = _clean(ld_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_106'] = {'inputs': ['ld_replacement_d2_106'], 'func': ld_replacement_d3_106}


def ld_replacement_d3_107(ld_replacement_d2_107):
    feature = _clean(ld_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_107'] = {'inputs': ['ld_replacement_d2_107'], 'func': ld_replacement_d3_107}


def ld_replacement_d3_108(ld_replacement_d2_108):
    feature = _clean(ld_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_108'] = {'inputs': ['ld_replacement_d2_108'], 'func': ld_replacement_d3_108}


def ld_replacement_d3_109(ld_replacement_d2_109):
    feature = _clean(ld_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_109'] = {'inputs': ['ld_replacement_d2_109'], 'func': ld_replacement_d3_109}


def ld_replacement_d3_110(ld_replacement_d2_110):
    feature = _clean(ld_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_110'] = {'inputs': ['ld_replacement_d2_110'], 'func': ld_replacement_d3_110}


def ld_replacement_d3_111(ld_replacement_d2_111):
    feature = _clean(ld_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_111'] = {'inputs': ['ld_replacement_d2_111'], 'func': ld_replacement_d3_111}


def ld_replacement_d3_112(ld_replacement_d2_112):
    feature = _clean(ld_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_112'] = {'inputs': ['ld_replacement_d2_112'], 'func': ld_replacement_d3_112}


def ld_replacement_d3_113(ld_replacement_d2_113):
    feature = _clean(ld_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_113'] = {'inputs': ['ld_replacement_d2_113'], 'func': ld_replacement_d3_113}


def ld_replacement_d3_114(ld_replacement_d2_114):
    feature = _clean(ld_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_114'] = {'inputs': ['ld_replacement_d2_114'], 'func': ld_replacement_d3_114}


def ld_replacement_d3_115(ld_replacement_d2_115):
    feature = _clean(ld_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_115'] = {'inputs': ['ld_replacement_d2_115'], 'func': ld_replacement_d3_115}


def ld_replacement_d3_116(ld_replacement_d2_116):
    feature = _clean(ld_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_116'] = {'inputs': ['ld_replacement_d2_116'], 'func': ld_replacement_d3_116}


def ld_replacement_d3_117(ld_replacement_d2_117):
    feature = _clean(ld_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_117'] = {'inputs': ['ld_replacement_d2_117'], 'func': ld_replacement_d3_117}


def ld_replacement_d3_118(ld_replacement_d2_118):
    feature = _clean(ld_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_118'] = {'inputs': ['ld_replacement_d2_118'], 'func': ld_replacement_d3_118}


def ld_replacement_d3_119(ld_replacement_d2_119):
    feature = _clean(ld_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_119'] = {'inputs': ['ld_replacement_d2_119'], 'func': ld_replacement_d3_119}


def ld_replacement_d3_120(ld_replacement_d2_120):
    feature = _clean(ld_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_120'] = {'inputs': ['ld_replacement_d2_120'], 'func': ld_replacement_d3_120}


def ld_replacement_d3_121(ld_replacement_d2_121):
    feature = _clean(ld_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_121'] = {'inputs': ['ld_replacement_d2_121'], 'func': ld_replacement_d3_121}


def ld_replacement_d3_122(ld_replacement_d2_122):
    feature = _clean(ld_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_122'] = {'inputs': ['ld_replacement_d2_122'], 'func': ld_replacement_d3_122}


def ld_replacement_d3_123(ld_replacement_d2_123):
    feature = _clean(ld_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_123'] = {'inputs': ['ld_replacement_d2_123'], 'func': ld_replacement_d3_123}


def ld_replacement_d3_124(ld_replacement_d2_124):
    feature = _clean(ld_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_124'] = {'inputs': ['ld_replacement_d2_124'], 'func': ld_replacement_d3_124}


def ld_replacement_d3_125(ld_replacement_d2_125):
    feature = _clean(ld_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_125'] = {'inputs': ['ld_replacement_d2_125'], 'func': ld_replacement_d3_125}


def ld_replacement_d3_126(ld_replacement_d2_126):
    feature = _clean(ld_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_126'] = {'inputs': ['ld_replacement_d2_126'], 'func': ld_replacement_d3_126}


def ld_replacement_d3_127(ld_replacement_d2_127):
    feature = _clean(ld_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_127'] = {'inputs': ['ld_replacement_d2_127'], 'func': ld_replacement_d3_127}


def ld_replacement_d3_128(ld_replacement_d2_128):
    feature = _clean(ld_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_128'] = {'inputs': ['ld_replacement_d2_128'], 'func': ld_replacement_d3_128}


def ld_replacement_d3_129(ld_replacement_d2_129):
    feature = _clean(ld_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_129'] = {'inputs': ['ld_replacement_d2_129'], 'func': ld_replacement_d3_129}


def ld_replacement_d3_130(ld_replacement_d2_130):
    feature = _clean(ld_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_130'] = {'inputs': ['ld_replacement_d2_130'], 'func': ld_replacement_d3_130}


def ld_replacement_d3_131(ld_replacement_d2_131):
    feature = _clean(ld_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_131'] = {'inputs': ['ld_replacement_d2_131'], 'func': ld_replacement_d3_131}


def ld_replacement_d3_132(ld_replacement_d2_132):
    feature = _clean(ld_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_132'] = {'inputs': ['ld_replacement_d2_132'], 'func': ld_replacement_d3_132}


def ld_replacement_d3_133(ld_replacement_d2_133):
    feature = _clean(ld_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_133'] = {'inputs': ['ld_replacement_d2_133'], 'func': ld_replacement_d3_133}


def ld_replacement_d3_134(ld_replacement_d2_134):
    feature = _clean(ld_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_134'] = {'inputs': ['ld_replacement_d2_134'], 'func': ld_replacement_d3_134}


def ld_replacement_d3_135(ld_replacement_d2_135):
    feature = _clean(ld_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_135'] = {'inputs': ['ld_replacement_d2_135'], 'func': ld_replacement_d3_135}


def ld_replacement_d3_136(ld_replacement_d2_136):
    feature = _clean(ld_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_136'] = {'inputs': ['ld_replacement_d2_136'], 'func': ld_replacement_d3_136}


def ld_replacement_d3_137(ld_replacement_d2_137):
    feature = _clean(ld_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_137'] = {'inputs': ['ld_replacement_d2_137'], 'func': ld_replacement_d3_137}


def ld_replacement_d3_138(ld_replacement_d2_138):
    feature = _clean(ld_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_138'] = {'inputs': ['ld_replacement_d2_138'], 'func': ld_replacement_d3_138}


def ld_replacement_d3_139(ld_replacement_d2_139):
    feature = _clean(ld_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_139'] = {'inputs': ['ld_replacement_d2_139'], 'func': ld_replacement_d3_139}


def ld_replacement_d3_140(ld_replacement_d2_140):
    feature = _clean(ld_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_140'] = {'inputs': ['ld_replacement_d2_140'], 'func': ld_replacement_d3_140}


def ld_replacement_d3_141(ld_replacement_d2_141):
    feature = _clean(ld_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_141'] = {'inputs': ['ld_replacement_d2_141'], 'func': ld_replacement_d3_141}


def ld_replacement_d3_142(ld_replacement_d2_142):
    feature = _clean(ld_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_142'] = {'inputs': ['ld_replacement_d2_142'], 'func': ld_replacement_d3_142}


def ld_replacement_d3_143(ld_replacement_d2_143):
    feature = _clean(ld_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_143'] = {'inputs': ['ld_replacement_d2_143'], 'func': ld_replacement_d3_143}


def ld_replacement_d3_144(ld_replacement_d2_144):
    feature = _clean(ld_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_144'] = {'inputs': ['ld_replacement_d2_144'], 'func': ld_replacement_d3_144}


def ld_replacement_d3_145(ld_replacement_d2_145):
    feature = _clean(ld_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_145'] = {'inputs': ['ld_replacement_d2_145'], 'func': ld_replacement_d3_145}


def ld_replacement_d3_146(ld_replacement_d2_146):
    feature = _clean(ld_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_146'] = {'inputs': ['ld_replacement_d2_146'], 'func': ld_replacement_d3_146}


def ld_replacement_d3_147(ld_replacement_d2_147):
    feature = _clean(ld_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_147'] = {'inputs': ['ld_replacement_d2_147'], 'func': ld_replacement_d3_147}


def ld_replacement_d3_148(ld_replacement_d2_148):
    feature = _clean(ld_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_148'] = {'inputs': ['ld_replacement_d2_148'], 'func': ld_replacement_d3_148}


def ld_replacement_d3_149(ld_replacement_d2_149):
    feature = _clean(ld_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_149'] = {'inputs': ['ld_replacement_d2_149'], 'func': ld_replacement_d3_149}


def ld_replacement_d3_150(ld_replacement_d2_150):
    feature = _clean(ld_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_150'] = {'inputs': ['ld_replacement_d2_150'], 'func': ld_replacement_d3_150}


def ld_replacement_d3_151(ld_replacement_d2_151):
    feature = _clean(ld_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_151'] = {'inputs': ['ld_replacement_d2_151'], 'func': ld_replacement_d3_151}


def ld_replacement_d3_152(ld_replacement_d2_152):
    feature = _clean(ld_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_152'] = {'inputs': ['ld_replacement_d2_152'], 'func': ld_replacement_d3_152}


def ld_replacement_d3_153(ld_replacement_d2_153):
    feature = _clean(ld_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_153'] = {'inputs': ['ld_replacement_d2_153'], 'func': ld_replacement_d3_153}


def ld_replacement_d3_154(ld_replacement_d2_154):
    feature = _clean(ld_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_154'] = {'inputs': ['ld_replacement_d2_154'], 'func': ld_replacement_d3_154}


def ld_replacement_d3_155(ld_replacement_d2_155):
    feature = _clean(ld_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_155'] = {'inputs': ['ld_replacement_d2_155'], 'func': ld_replacement_d3_155}


def ld_replacement_d3_156(ld_replacement_d2_156):
    feature = _clean(ld_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_156'] = {'inputs': ['ld_replacement_d2_156'], 'func': ld_replacement_d3_156}


def ld_replacement_d3_157(ld_replacement_d2_157):
    feature = _clean(ld_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_157'] = {'inputs': ['ld_replacement_d2_157'], 'func': ld_replacement_d3_157}


def ld_replacement_d3_158(ld_replacement_d2_158):
    feature = _clean(ld_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_158'] = {'inputs': ['ld_replacement_d2_158'], 'func': ld_replacement_d3_158}


def ld_replacement_d3_159(ld_replacement_d2_159):
    feature = _clean(ld_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_159'] = {'inputs': ['ld_replacement_d2_159'], 'func': ld_replacement_d3_159}


def ld_replacement_d3_160(ld_replacement_d2_160):
    feature = _clean(ld_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_160'] = {'inputs': ['ld_replacement_d2_160'], 'func': ld_replacement_d3_160}


def ld_replacement_d3_161(ld_replacement_d2_161):
    feature = _clean(ld_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_161'] = {'inputs': ['ld_replacement_d2_161'], 'func': ld_replacement_d3_161}


def ld_replacement_d3_162(ld_replacement_d2_162):
    feature = _clean(ld_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_162'] = {'inputs': ['ld_replacement_d2_162'], 'func': ld_replacement_d3_162}


def ld_replacement_d3_163(ld_replacement_d2_163):
    feature = _clean(ld_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_163'] = {'inputs': ['ld_replacement_d2_163'], 'func': ld_replacement_d3_163}


def ld_replacement_d3_164(ld_replacement_d2_164):
    feature = _clean(ld_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_164'] = {'inputs': ['ld_replacement_d2_164'], 'func': ld_replacement_d3_164}


def ld_replacement_d3_165(ld_replacement_d2_165):
    feature = _clean(ld_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_165'] = {'inputs': ['ld_replacement_d2_165'], 'func': ld_replacement_d3_165}


def ld_replacement_d3_166(ld_replacement_d2_166):
    feature = _clean(ld_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
LD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ld_replacement_d3_166'] = {'inputs': ['ld_replacement_d2_166'], 'func': ld_replacement_d3_166}


# Third-derivative extensions for repaired first-base features.
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def lqd_base_universe_d3_001_lqd_003_fcf_burn_to_cash_63(lqd_base_universe_d2_001_lqd_003_fcf_burn_to_cash_63):
    return _base_universe_d3(lqd_base_universe_d2_001_lqd_003_fcf_burn_to_cash_63, 1)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_001_lqd_003_fcf_burn_to_cash_63'] = {'inputs': ['lqd_base_universe_d2_001_lqd_003_fcf_burn_to_cash_63'], 'func': lqd_base_universe_d3_001_lqd_003_fcf_burn_to_cash_63}


def lqd_base_universe_d3_002_lqd_004_debt_to_equity_84(lqd_base_universe_d2_002_lqd_004_debt_to_equity_84):
    return _base_universe_d3(lqd_base_universe_d2_002_lqd_004_debt_to_equity_84, 2)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_002_lqd_004_debt_to_equity_84'] = {'inputs': ['lqd_base_universe_d2_002_lqd_004_debt_to_equity_84'], 'func': lqd_base_universe_d3_002_lqd_004_debt_to_equity_84}


def lqd_base_universe_d3_003_lqd_005_debt_to_assets_126(lqd_base_universe_d2_003_lqd_005_debt_to_assets_126):
    return _base_universe_d3(lqd_base_universe_d2_003_lqd_005_debt_to_assets_126, 3)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_003_lqd_005_debt_to_assets_126'] = {'inputs': ['lqd_base_universe_d2_003_lqd_005_debt_to_assets_126'], 'func': lqd_base_universe_d3_003_lqd_005_debt_to_assets_126}


def lqd_base_universe_d3_004_lqd_012_accrual_gap_1260(lqd_base_universe_d2_004_lqd_012_accrual_gap_1260):
    return _base_universe_d3(lqd_base_universe_d2_004_lqd_012_accrual_gap_1260, 4)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_004_lqd_012_accrual_gap_1260'] = {'inputs': ['lqd_base_universe_d2_004_lqd_012_accrual_gap_1260'], 'func': lqd_base_universe_d3_004_lqd_012_accrual_gap_1260}


def lqd_base_universe_d3_005_lqd_016_debt_to_equity_21(lqd_base_universe_d2_005_lqd_016_debt_to_equity_21):
    return _base_universe_d3(lqd_base_universe_d2_005_lqd_016_debt_to_equity_21, 5)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_005_lqd_016_debt_to_equity_21'] = {'inputs': ['lqd_base_universe_d2_005_lqd_016_debt_to_equity_21'], 'func': lqd_base_universe_d3_005_lqd_016_debt_to_equity_21}


def lqd_base_universe_d3_006_lqd_017_debt_to_assets_42(lqd_base_universe_d2_006_lqd_017_debt_to_assets_42):
    return _base_universe_d3(lqd_base_universe_d2_006_lqd_017_debt_to_assets_42, 6)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_006_lqd_017_debt_to_assets_42'] = {'inputs': ['lqd_base_universe_d2_006_lqd_017_debt_to_assets_42'], 'func': lqd_base_universe_d3_006_lqd_017_debt_to_assets_42}


def lqd_base_universe_d3_007_lqd_024_accrual_gap_504(lqd_base_universe_d2_007_lqd_024_accrual_gap_504):
    return _base_universe_d3(lqd_base_universe_d2_007_lqd_024_accrual_gap_504, 7)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_007_lqd_024_accrual_gap_504'] = {'inputs': ['lqd_base_universe_d2_007_lqd_024_accrual_gap_504'], 'func': lqd_base_universe_d3_007_lqd_024_accrual_gap_504}


def lqd_base_universe_d3_008_lqd_027_fcf_burn_to_cash_1260(lqd_base_universe_d2_008_lqd_027_fcf_burn_to_cash_1260):
    return _base_universe_d3(lqd_base_universe_d2_008_lqd_027_fcf_burn_to_cash_1260, 8)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_008_lqd_027_fcf_burn_to_cash_1260'] = {'inputs': ['lqd_base_universe_d2_008_lqd_027_fcf_burn_to_cash_1260'], 'func': lqd_base_universe_d3_008_lqd_027_fcf_burn_to_cash_1260}


def lqd_base_universe_d3_009_lqd_028_debt_to_equity_1512(lqd_base_universe_d2_009_lqd_028_debt_to_equity_1512):
    return _base_universe_d3(lqd_base_universe_d2_009_lqd_028_debt_to_equity_1512, 9)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_009_lqd_028_debt_to_equity_1512'] = {'inputs': ['lqd_base_universe_d2_009_lqd_028_debt_to_equity_1512'], 'func': lqd_base_universe_d3_009_lqd_028_debt_to_equity_1512}


def lqd_base_universe_d3_010_lqd_029_debt_to_assets_63(lqd_base_universe_d2_010_lqd_029_debt_to_assets_63):
    return _base_universe_d3(lqd_base_universe_d2_010_lqd_029_debt_to_assets_63, 10)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_010_lqd_029_debt_to_assets_63'] = {'inputs': ['lqd_base_universe_d2_010_lqd_029_debt_to_assets_63'], 'func': lqd_base_universe_d3_010_lqd_029_debt_to_assets_63}


def lqd_base_universe_d3_011_lqd_031_interest_coverage_stress_21(lqd_base_universe_d2_011_lqd_031_interest_coverage_stress_21):
    return _base_universe_d3(lqd_base_universe_d2_011_lqd_031_interest_coverage_stress_21, 11)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_011_lqd_031_interest_coverage_stress_21'] = {'inputs': ['lqd_base_universe_d2_011_lqd_031_interest_coverage_stress_21'], 'func': lqd_base_universe_d3_011_lqd_031_interest_coverage_stress_21}


def lqd_base_universe_d3_012_lqd_036_accrual_gap_189(lqd_base_universe_d2_012_lqd_036_accrual_gap_189):
    return _base_universe_d3(lqd_base_universe_d2_012_lqd_036_accrual_gap_189, 12)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_012_lqd_036_accrual_gap_189'] = {'inputs': ['lqd_base_universe_d2_012_lqd_036_accrual_gap_189'], 'func': lqd_base_universe_d3_012_lqd_036_accrual_gap_189}


def lqd_base_universe_d3_013_lqd_039_fcf_burn_to_cash_504(lqd_base_universe_d2_013_lqd_039_fcf_burn_to_cash_504):
    return _base_universe_d3(lqd_base_universe_d2_013_lqd_039_fcf_burn_to_cash_504, 13)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_013_lqd_039_fcf_burn_to_cash_504'] = {'inputs': ['lqd_base_universe_d2_013_lqd_039_fcf_burn_to_cash_504'], 'func': lqd_base_universe_d3_013_lqd_039_fcf_burn_to_cash_504}


def lqd_base_universe_d3_014_lqd_040_debt_to_equity_756(lqd_base_universe_d2_014_lqd_040_debt_to_equity_756):
    return _base_universe_d3(lqd_base_universe_d2_014_lqd_040_debt_to_equity_756, 14)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_014_lqd_040_debt_to_equity_756'] = {'inputs': ['lqd_base_universe_d2_014_lqd_040_debt_to_equity_756'], 'func': lqd_base_universe_d3_014_lqd_040_debt_to_equity_756}


def lqd_base_universe_d3_015_lqd_041_debt_to_assets_1008(lqd_base_universe_d2_015_lqd_041_debt_to_assets_1008):
    return _base_universe_d3(lqd_base_universe_d2_015_lqd_041_debt_to_assets_1008, 15)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_015_lqd_041_debt_to_assets_1008'] = {'inputs': ['lqd_base_universe_d2_015_lqd_041_debt_to_assets_1008'], 'func': lqd_base_universe_d3_015_lqd_041_debt_to_assets_1008}


def lqd_base_universe_d3_016_lqd_043_interest_coverage_stress_1512(lqd_base_universe_d2_016_lqd_043_interest_coverage_stress_1512):
    return _base_universe_d3(lqd_base_universe_d2_016_lqd_043_interest_coverage_stress_1512, 16)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_016_lqd_043_interest_coverage_stress_1512'] = {'inputs': ['lqd_base_universe_d2_016_lqd_043_interest_coverage_stress_1512'], 'func': lqd_base_universe_d3_016_lqd_043_interest_coverage_stress_1512}


def lqd_base_universe_d3_017_lqd_048_accrual_gap_63(lqd_base_universe_d2_017_lqd_048_accrual_gap_63):
    return _base_universe_d3(lqd_base_universe_d2_017_lqd_048_accrual_gap_63, 17)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_017_lqd_048_accrual_gap_63'] = {'inputs': ['lqd_base_universe_d2_017_lqd_048_accrual_gap_63'], 'func': lqd_base_universe_d3_017_lqd_048_accrual_gap_63}


def lqd_base_universe_d3_018_lqd_051_fcf_burn_to_cash_189(lqd_base_universe_d2_018_lqd_051_fcf_burn_to_cash_189):
    return _base_universe_d3(lqd_base_universe_d2_018_lqd_051_fcf_burn_to_cash_189, 18)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_018_lqd_051_fcf_burn_to_cash_189'] = {'inputs': ['lqd_base_universe_d2_018_lqd_051_fcf_burn_to_cash_189'], 'func': lqd_base_universe_d3_018_lqd_051_fcf_burn_to_cash_189}


def lqd_base_universe_d3_019_lqd_052_debt_to_equity_252(lqd_base_universe_d2_019_lqd_052_debt_to_equity_252):
    return _base_universe_d3(lqd_base_universe_d2_019_lqd_052_debt_to_equity_252, 19)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_019_lqd_052_debt_to_equity_252'] = {'inputs': ['lqd_base_universe_d2_019_lqd_052_debt_to_equity_252'], 'func': lqd_base_universe_d3_019_lqd_052_debt_to_equity_252}


def lqd_base_universe_d3_020_lqd_053_debt_to_assets_378(lqd_base_universe_d2_020_lqd_053_debt_to_assets_378):
    return _base_universe_d3(lqd_base_universe_d2_020_lqd_053_debt_to_assets_378, 20)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_020_lqd_053_debt_to_assets_378'] = {'inputs': ['lqd_base_universe_d2_020_lqd_053_debt_to_assets_378'], 'func': lqd_base_universe_d3_020_lqd_053_debt_to_assets_378}


def lqd_base_universe_d3_021_lqd_055_interest_coverage_stress_756(lqd_base_universe_d2_021_lqd_055_interest_coverage_stress_756):
    return _base_universe_d3(lqd_base_universe_d2_021_lqd_055_interest_coverage_stress_756, 21)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_021_lqd_055_interest_coverage_stress_756'] = {'inputs': ['lqd_base_universe_d2_021_lqd_055_interest_coverage_stress_756'], 'func': lqd_base_universe_d3_021_lqd_055_interest_coverage_stress_756}


def lqd_base_universe_d3_022_lqd_060_accrual_gap_252(lqd_base_universe_d2_022_lqd_060_accrual_gap_252):
    return _base_universe_d3(lqd_base_universe_d2_022_lqd_060_accrual_gap_252, 22)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_022_lqd_060_accrual_gap_252'] = {'inputs': ['lqd_base_universe_d2_022_lqd_060_accrual_gap_252'], 'func': lqd_base_universe_d3_022_lqd_060_accrual_gap_252}


def lqd_base_universe_d3_023_lqd_basefill_001(lqd_base_universe_d2_023_lqd_basefill_001):
    return _base_universe_d3(lqd_base_universe_d2_023_lqd_basefill_001, 23)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_023_lqd_basefill_001'] = {'inputs': ['lqd_base_universe_d2_023_lqd_basefill_001'], 'func': lqd_base_universe_d3_023_lqd_basefill_001}


def lqd_base_universe_d3_024_lqd_basefill_002(lqd_base_universe_d2_024_lqd_basefill_002):
    return _base_universe_d3(lqd_base_universe_d2_024_lqd_basefill_002, 24)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_024_lqd_basefill_002'] = {'inputs': ['lqd_base_universe_d2_024_lqd_basefill_002'], 'func': lqd_base_universe_d3_024_lqd_basefill_002}


def lqd_base_universe_d3_025_lqd_basefill_006(lqd_base_universe_d2_025_lqd_basefill_006):
    return _base_universe_d3(lqd_base_universe_d2_025_lqd_basefill_006, 25)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_025_lqd_basefill_006'] = {'inputs': ['lqd_base_universe_d2_025_lqd_basefill_006'], 'func': lqd_base_universe_d3_025_lqd_basefill_006}


def lqd_base_universe_d3_026_lqd_basefill_008(lqd_base_universe_d2_026_lqd_basefill_008):
    return _base_universe_d3(lqd_base_universe_d2_026_lqd_basefill_008, 26)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_026_lqd_basefill_008'] = {'inputs': ['lqd_base_universe_d2_026_lqd_basefill_008'], 'func': lqd_base_universe_d3_026_lqd_basefill_008}


def lqd_base_universe_d3_027_lqd_basefill_009(lqd_base_universe_d2_027_lqd_basefill_009):
    return _base_universe_d3(lqd_base_universe_d2_027_lqd_basefill_009, 27)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_027_lqd_basefill_009'] = {'inputs': ['lqd_base_universe_d2_027_lqd_basefill_009'], 'func': lqd_base_universe_d3_027_lqd_basefill_009}


def lqd_base_universe_d3_028_lqd_basefill_010(lqd_base_universe_d2_028_lqd_basefill_010):
    return _base_universe_d3(lqd_base_universe_d2_028_lqd_basefill_010, 28)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_028_lqd_basefill_010'] = {'inputs': ['lqd_base_universe_d2_028_lqd_basefill_010'], 'func': lqd_base_universe_d3_028_lqd_basefill_010}


def lqd_base_universe_d3_029_lqd_basefill_011(lqd_base_universe_d2_029_lqd_basefill_011):
    return _base_universe_d3(lqd_base_universe_d2_029_lqd_basefill_011, 29)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_029_lqd_basefill_011'] = {'inputs': ['lqd_base_universe_d2_029_lqd_basefill_011'], 'func': lqd_base_universe_d3_029_lqd_basefill_011}


def lqd_base_universe_d3_030_lqd_basefill_013(lqd_base_universe_d2_030_lqd_basefill_013):
    return _base_universe_d3(lqd_base_universe_d2_030_lqd_basefill_013, 30)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_030_lqd_basefill_013'] = {'inputs': ['lqd_base_universe_d2_030_lqd_basefill_013'], 'func': lqd_base_universe_d3_030_lqd_basefill_013}


def lqd_base_universe_d3_031_lqd_basefill_014(lqd_base_universe_d2_031_lqd_basefill_014):
    return _base_universe_d3(lqd_base_universe_d2_031_lqd_basefill_014, 31)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_031_lqd_basefill_014'] = {'inputs': ['lqd_base_universe_d2_031_lqd_basefill_014'], 'func': lqd_base_universe_d3_031_lqd_basefill_014}


def lqd_base_universe_d3_032_lqd_basefill_015(lqd_base_universe_d2_032_lqd_basefill_015):
    return _base_universe_d3(lqd_base_universe_d2_032_lqd_basefill_015, 32)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_032_lqd_basefill_015'] = {'inputs': ['lqd_base_universe_d2_032_lqd_basefill_015'], 'func': lqd_base_universe_d3_032_lqd_basefill_015}


def lqd_base_universe_d3_033_lqd_basefill_018(lqd_base_universe_d2_033_lqd_basefill_018):
    return _base_universe_d3(lqd_base_universe_d2_033_lqd_basefill_018, 33)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_033_lqd_basefill_018'] = {'inputs': ['lqd_base_universe_d2_033_lqd_basefill_018'], 'func': lqd_base_universe_d3_033_lqd_basefill_018}


def lqd_base_universe_d3_034_lqd_basefill_020(lqd_base_universe_d2_034_lqd_basefill_020):
    return _base_universe_d3(lqd_base_universe_d2_034_lqd_basefill_020, 34)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_034_lqd_basefill_020'] = {'inputs': ['lqd_base_universe_d2_034_lqd_basefill_020'], 'func': lqd_base_universe_d3_034_lqd_basefill_020}


def lqd_base_universe_d3_035_lqd_basefill_021(lqd_base_universe_d2_035_lqd_basefill_021):
    return _base_universe_d3(lqd_base_universe_d2_035_lqd_basefill_021, 35)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_035_lqd_basefill_021'] = {'inputs': ['lqd_base_universe_d2_035_lqd_basefill_021'], 'func': lqd_base_universe_d3_035_lqd_basefill_021}


def lqd_base_universe_d3_036_lqd_basefill_022(lqd_base_universe_d2_036_lqd_basefill_022):
    return _base_universe_d3(lqd_base_universe_d2_036_lqd_basefill_022, 36)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_036_lqd_basefill_022'] = {'inputs': ['lqd_base_universe_d2_036_lqd_basefill_022'], 'func': lqd_base_universe_d3_036_lqd_basefill_022}


def lqd_base_universe_d3_037_lqd_basefill_023(lqd_base_universe_d2_037_lqd_basefill_023):
    return _base_universe_d3(lqd_base_universe_d2_037_lqd_basefill_023, 37)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_037_lqd_basefill_023'] = {'inputs': ['lqd_base_universe_d2_037_lqd_basefill_023'], 'func': lqd_base_universe_d3_037_lqd_basefill_023}


def lqd_base_universe_d3_038_lqd_basefill_025(lqd_base_universe_d2_038_lqd_basefill_025):
    return _base_universe_d3(lqd_base_universe_d2_038_lqd_basefill_025, 38)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_038_lqd_basefill_025'] = {'inputs': ['lqd_base_universe_d2_038_lqd_basefill_025'], 'func': lqd_base_universe_d3_038_lqd_basefill_025}


def lqd_base_universe_d3_039_lqd_basefill_026(lqd_base_universe_d2_039_lqd_basefill_026):
    return _base_universe_d3(lqd_base_universe_d2_039_lqd_basefill_026, 39)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_039_lqd_basefill_026'] = {'inputs': ['lqd_base_universe_d2_039_lqd_basefill_026'], 'func': lqd_base_universe_d3_039_lqd_basefill_026}


def lqd_base_universe_d3_040_lqd_basefill_030(lqd_base_universe_d2_040_lqd_basefill_030):
    return _base_universe_d3(lqd_base_universe_d2_040_lqd_basefill_030, 40)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_040_lqd_basefill_030'] = {'inputs': ['lqd_base_universe_d2_040_lqd_basefill_030'], 'func': lqd_base_universe_d3_040_lqd_basefill_030}


def lqd_base_universe_d3_041_lqd_basefill_032(lqd_base_universe_d2_041_lqd_basefill_032):
    return _base_universe_d3(lqd_base_universe_d2_041_lqd_basefill_032, 41)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_041_lqd_basefill_032'] = {'inputs': ['lqd_base_universe_d2_041_lqd_basefill_032'], 'func': lqd_base_universe_d3_041_lqd_basefill_032}


def lqd_base_universe_d3_042_lqd_basefill_033(lqd_base_universe_d2_042_lqd_basefill_033):
    return _base_universe_d3(lqd_base_universe_d2_042_lqd_basefill_033, 42)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_042_lqd_basefill_033'] = {'inputs': ['lqd_base_universe_d2_042_lqd_basefill_033'], 'func': lqd_base_universe_d3_042_lqd_basefill_033}


def lqd_base_universe_d3_043_lqd_basefill_034(lqd_base_universe_d2_043_lqd_basefill_034):
    return _base_universe_d3(lqd_base_universe_d2_043_lqd_basefill_034, 43)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_043_lqd_basefill_034'] = {'inputs': ['lqd_base_universe_d2_043_lqd_basefill_034'], 'func': lqd_base_universe_d3_043_lqd_basefill_034}


def lqd_base_universe_d3_044_lqd_basefill_035(lqd_base_universe_d2_044_lqd_basefill_035):
    return _base_universe_d3(lqd_base_universe_d2_044_lqd_basefill_035, 44)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_044_lqd_basefill_035'] = {'inputs': ['lqd_base_universe_d2_044_lqd_basefill_035'], 'func': lqd_base_universe_d3_044_lqd_basefill_035}


def lqd_base_universe_d3_045_lqd_basefill_037(lqd_base_universe_d2_045_lqd_basefill_037):
    return _base_universe_d3(lqd_base_universe_d2_045_lqd_basefill_037, 45)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_045_lqd_basefill_037'] = {'inputs': ['lqd_base_universe_d2_045_lqd_basefill_037'], 'func': lqd_base_universe_d3_045_lqd_basefill_037}


def lqd_base_universe_d3_046_lqd_basefill_038(lqd_base_universe_d2_046_lqd_basefill_038):
    return _base_universe_d3(lqd_base_universe_d2_046_lqd_basefill_038, 46)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_046_lqd_basefill_038'] = {'inputs': ['lqd_base_universe_d2_046_lqd_basefill_038'], 'func': lqd_base_universe_d3_046_lqd_basefill_038}


def lqd_base_universe_d3_047_lqd_basefill_042(lqd_base_universe_d2_047_lqd_basefill_042):
    return _base_universe_d3(lqd_base_universe_d2_047_lqd_basefill_042, 47)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_047_lqd_basefill_042'] = {'inputs': ['lqd_base_universe_d2_047_lqd_basefill_042'], 'func': lqd_base_universe_d3_047_lqd_basefill_042}


def lqd_base_universe_d3_048_lqd_basefill_044(lqd_base_universe_d2_048_lqd_basefill_044):
    return _base_universe_d3(lqd_base_universe_d2_048_lqd_basefill_044, 48)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_048_lqd_basefill_044'] = {'inputs': ['lqd_base_universe_d2_048_lqd_basefill_044'], 'func': lqd_base_universe_d3_048_lqd_basefill_044}


def lqd_base_universe_d3_049_lqd_basefill_045(lqd_base_universe_d2_049_lqd_basefill_045):
    return _base_universe_d3(lqd_base_universe_d2_049_lqd_basefill_045, 49)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_049_lqd_basefill_045'] = {'inputs': ['lqd_base_universe_d2_049_lqd_basefill_045'], 'func': lqd_base_universe_d3_049_lqd_basefill_045}


def lqd_base_universe_d3_050_lqd_basefill_046(lqd_base_universe_d2_050_lqd_basefill_046):
    return _base_universe_d3(lqd_base_universe_d2_050_lqd_basefill_046, 50)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_050_lqd_basefill_046'] = {'inputs': ['lqd_base_universe_d2_050_lqd_basefill_046'], 'func': lqd_base_universe_d3_050_lqd_basefill_046}


def lqd_base_universe_d3_051_lqd_basefill_047(lqd_base_universe_d2_051_lqd_basefill_047):
    return _base_universe_d3(lqd_base_universe_d2_051_lqd_basefill_047, 51)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_051_lqd_basefill_047'] = {'inputs': ['lqd_base_universe_d2_051_lqd_basefill_047'], 'func': lqd_base_universe_d3_051_lqd_basefill_047}


def lqd_base_universe_d3_052_lqd_basefill_049(lqd_base_universe_d2_052_lqd_basefill_049):
    return _base_universe_d3(lqd_base_universe_d2_052_lqd_basefill_049, 52)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_052_lqd_basefill_049'] = {'inputs': ['lqd_base_universe_d2_052_lqd_basefill_049'], 'func': lqd_base_universe_d3_052_lqd_basefill_049}


def lqd_base_universe_d3_053_lqd_basefill_050(lqd_base_universe_d2_053_lqd_basefill_050):
    return _base_universe_d3(lqd_base_universe_d2_053_lqd_basefill_050, 53)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_053_lqd_basefill_050'] = {'inputs': ['lqd_base_universe_d2_053_lqd_basefill_050'], 'func': lqd_base_universe_d3_053_lqd_basefill_050}


def lqd_base_universe_d3_054_lqd_basefill_054(lqd_base_universe_d2_054_lqd_basefill_054):
    return _base_universe_d3(lqd_base_universe_d2_054_lqd_basefill_054, 54)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_054_lqd_basefill_054'] = {'inputs': ['lqd_base_universe_d2_054_lqd_basefill_054'], 'func': lqd_base_universe_d3_054_lqd_basefill_054}


def lqd_base_universe_d3_055_lqd_basefill_056(lqd_base_universe_d2_055_lqd_basefill_056):
    return _base_universe_d3(lqd_base_universe_d2_055_lqd_basefill_056, 55)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_055_lqd_basefill_056'] = {'inputs': ['lqd_base_universe_d2_055_lqd_basefill_056'], 'func': lqd_base_universe_d3_055_lqd_basefill_056}


def lqd_base_universe_d3_056_lqd_basefill_057(lqd_base_universe_d2_056_lqd_basefill_057):
    return _base_universe_d3(lqd_base_universe_d2_056_lqd_basefill_057, 56)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_056_lqd_basefill_057'] = {'inputs': ['lqd_base_universe_d2_056_lqd_basefill_057'], 'func': lqd_base_universe_d3_056_lqd_basefill_057}


def lqd_base_universe_d3_057_lqd_basefill_058(lqd_base_universe_d2_057_lqd_basefill_058):
    return _base_universe_d3(lqd_base_universe_d2_057_lqd_basefill_058, 57)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_057_lqd_basefill_058'] = {'inputs': ['lqd_base_universe_d2_057_lqd_basefill_058'], 'func': lqd_base_universe_d3_057_lqd_basefill_058}


def lqd_base_universe_d3_058_lqd_basefill_059(lqd_base_universe_d2_058_lqd_basefill_059):
    return _base_universe_d3(lqd_base_universe_d2_058_lqd_basefill_059, 58)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_058_lqd_basefill_059'] = {'inputs': ['lqd_base_universe_d2_058_lqd_basefill_059'], 'func': lqd_base_universe_d3_058_lqd_basefill_059}


def lqd_base_universe_d3_059_lqd_basefill_061(lqd_base_universe_d2_059_lqd_basefill_061):
    return _base_universe_d3(lqd_base_universe_d2_059_lqd_basefill_061, 59)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_059_lqd_basefill_061'] = {'inputs': ['lqd_base_universe_d2_059_lqd_basefill_061'], 'func': lqd_base_universe_d3_059_lqd_basefill_061}


def lqd_base_universe_d3_060_lqd_basefill_062(lqd_base_universe_d2_060_lqd_basefill_062):
    return _base_universe_d3(lqd_base_universe_d2_060_lqd_basefill_062, 60)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_060_lqd_basefill_062'] = {'inputs': ['lqd_base_universe_d2_060_lqd_basefill_062'], 'func': lqd_base_universe_d3_060_lqd_basefill_062}


def lqd_base_universe_d3_061_lqd_basefill_063(lqd_base_universe_d2_061_lqd_basefill_063):
    return _base_universe_d3(lqd_base_universe_d2_061_lqd_basefill_063, 61)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_061_lqd_basefill_063'] = {'inputs': ['lqd_base_universe_d2_061_lqd_basefill_063'], 'func': lqd_base_universe_d3_061_lqd_basefill_063}


def lqd_base_universe_d3_062_lqd_basefill_064(lqd_base_universe_d2_062_lqd_basefill_064):
    return _base_universe_d3(lqd_base_universe_d2_062_lqd_basefill_064, 62)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_062_lqd_basefill_064'] = {'inputs': ['lqd_base_universe_d2_062_lqd_basefill_064'], 'func': lqd_base_universe_d3_062_lqd_basefill_064}


def lqd_base_universe_d3_063_lqd_basefill_065(lqd_base_universe_d2_063_lqd_basefill_065):
    return _base_universe_d3(lqd_base_universe_d2_063_lqd_basefill_065, 63)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_063_lqd_basefill_065'] = {'inputs': ['lqd_base_universe_d2_063_lqd_basefill_065'], 'func': lqd_base_universe_d3_063_lqd_basefill_065}


def lqd_base_universe_d3_064_lqd_basefill_066(lqd_base_universe_d2_064_lqd_basefill_066):
    return _base_universe_d3(lqd_base_universe_d2_064_lqd_basefill_066, 64)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_064_lqd_basefill_066'] = {'inputs': ['lqd_base_universe_d2_064_lqd_basefill_066'], 'func': lqd_base_universe_d3_064_lqd_basefill_066}


def lqd_base_universe_d3_065_lqd_basefill_067(lqd_base_universe_d2_065_lqd_basefill_067):
    return _base_universe_d3(lqd_base_universe_d2_065_lqd_basefill_067, 65)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_065_lqd_basefill_067'] = {'inputs': ['lqd_base_universe_d2_065_lqd_basefill_067'], 'func': lqd_base_universe_d3_065_lqd_basefill_067}


def lqd_base_universe_d3_066_lqd_basefill_068(lqd_base_universe_d2_066_lqd_basefill_068):
    return _base_universe_d3(lqd_base_universe_d2_066_lqd_basefill_068, 66)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_066_lqd_basefill_068'] = {'inputs': ['lqd_base_universe_d2_066_lqd_basefill_068'], 'func': lqd_base_universe_d3_066_lqd_basefill_068}


def lqd_base_universe_d3_067_lqd_basefill_069(lqd_base_universe_d2_067_lqd_basefill_069):
    return _base_universe_d3(lqd_base_universe_d2_067_lqd_basefill_069, 67)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_067_lqd_basefill_069'] = {'inputs': ['lqd_base_universe_d2_067_lqd_basefill_069'], 'func': lqd_base_universe_d3_067_lqd_basefill_069}


def lqd_base_universe_d3_068_lqd_basefill_070(lqd_base_universe_d2_068_lqd_basefill_070):
    return _base_universe_d3(lqd_base_universe_d2_068_lqd_basefill_070, 68)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_068_lqd_basefill_070'] = {'inputs': ['lqd_base_universe_d2_068_lqd_basefill_070'], 'func': lqd_base_universe_d3_068_lqd_basefill_070}


def lqd_base_universe_d3_069_lqd_basefill_071(lqd_base_universe_d2_069_lqd_basefill_071):
    return _base_universe_d3(lqd_base_universe_d2_069_lqd_basefill_071, 69)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_069_lqd_basefill_071'] = {'inputs': ['lqd_base_universe_d2_069_lqd_basefill_071'], 'func': lqd_base_universe_d3_069_lqd_basefill_071}


def lqd_base_universe_d3_070_lqd_basefill_072(lqd_base_universe_d2_070_lqd_basefill_072):
    return _base_universe_d3(lqd_base_universe_d2_070_lqd_basefill_072, 70)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_070_lqd_basefill_072'] = {'inputs': ['lqd_base_universe_d2_070_lqd_basefill_072'], 'func': lqd_base_universe_d3_070_lqd_basefill_072}


def lqd_base_universe_d3_071_lqd_basefill_073(lqd_base_universe_d2_071_lqd_basefill_073):
    return _base_universe_d3(lqd_base_universe_d2_071_lqd_basefill_073, 71)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_071_lqd_basefill_073'] = {'inputs': ['lqd_base_universe_d2_071_lqd_basefill_073'], 'func': lqd_base_universe_d3_071_lqd_basefill_073}


def lqd_base_universe_d3_072_lqd_basefill_074(lqd_base_universe_d2_072_lqd_basefill_074):
    return _base_universe_d3(lqd_base_universe_d2_072_lqd_basefill_074, 72)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_072_lqd_basefill_074'] = {'inputs': ['lqd_base_universe_d2_072_lqd_basefill_074'], 'func': lqd_base_universe_d3_072_lqd_basefill_074}


def lqd_base_universe_d3_073_lqd_basefill_075(lqd_base_universe_d2_073_lqd_basefill_075):
    return _base_universe_d3(lqd_base_universe_d2_073_lqd_basefill_075, 73)
LQD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqd_base_universe_d3_073_lqd_basefill_075'] = {'inputs': ['lqd_base_universe_d2_073_lqd_basefill_075'], 'func': lqd_base_universe_d3_073_lqd_basefill_075}
