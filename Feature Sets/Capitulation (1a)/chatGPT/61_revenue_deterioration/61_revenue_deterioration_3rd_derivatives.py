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



def rvd_176_rvd_001_netinc_decline_1_accel_1(rvd_151_rvd_001_netinc_decline_1_roc_1):
    feature = _s(rvd_151_rvd_001_netinc_decline_1_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def rvd_177_rvd_007_interest_coverage_stress_252_accel_42(rvd_152_rvd_007_interest_coverage_stress_252_roc_42):
    feature = _s(rvd_152_rvd_007_interest_coverage_stress_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def rvd_178_rvd_013_netinc_decline_1_accel_126(rvd_153_rvd_013_netinc_decline_1_roc_126):
    feature = _s(rvd_153_rvd_013_netinc_decline_1_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def rvd_179_rvd_019_interest_coverage_stress_84_accel_378(rvd_154_rvd_019_interest_coverage_stress_84_roc_378):
    feature = _s(rvd_154_rvd_019_interest_coverage_stress_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def rvd_180_rvd_025_netinc_decline_1_accel_4(rvd_155_rvd_025_netinc_decline_1_roc_4):
    feature = _s(rvd_155_rvd_025_netinc_decline_1_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















REVENUE_DETERIORATION_REGISTRY_3RD_DERIVATIVES = {
    'rvd_176_rvd_001_netinc_decline_1_accel_1': {'inputs': ['rvd_151_rvd_001_netinc_decline_1_roc_1'], 'func': rvd_176_rvd_001_netinc_decline_1_accel_1},
    'rvd_177_rvd_007_interest_coverage_stress_252_accel_42': {'inputs': ['rvd_152_rvd_007_interest_coverage_stress_252_roc_42'], 'func': rvd_177_rvd_007_interest_coverage_stress_252_accel_42},
    'rvd_178_rvd_013_netinc_decline_1_accel_126': {'inputs': ['rvd_153_rvd_013_netinc_decline_1_roc_126'], 'func': rvd_178_rvd_013_netinc_decline_1_accel_126},
    'rvd_179_rvd_019_interest_coverage_stress_84_accel_378': {'inputs': ['rvd_154_rvd_019_interest_coverage_stress_84_roc_378'], 'func': rvd_179_rvd_019_interest_coverage_stress_84_accel_378},
    'rvd_180_rvd_025_netinc_decline_1_accel_4': {'inputs': ['rvd_155_rvd_025_netinc_decline_1_roc_4'], 'func': rvd_180_rvd_025_netinc_decline_1_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def rd_replacement_d3_001(rd_replacement_d2_001):
    feature = _clean(rd_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_001'] = {'inputs': ['rd_replacement_d2_001'], 'func': rd_replacement_d3_001}


def rd_replacement_d3_002(rd_replacement_d2_002):
    feature = _clean(rd_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_002'] = {'inputs': ['rd_replacement_d2_002'], 'func': rd_replacement_d3_002}


def rd_replacement_d3_003(rd_replacement_d2_003):
    feature = _clean(rd_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_003'] = {'inputs': ['rd_replacement_d2_003'], 'func': rd_replacement_d3_003}


def rd_replacement_d3_004(rd_replacement_d2_004):
    feature = _clean(rd_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_004'] = {'inputs': ['rd_replacement_d2_004'], 'func': rd_replacement_d3_004}


def rd_replacement_d3_005(rd_replacement_d2_005):
    feature = _clean(rd_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_005'] = {'inputs': ['rd_replacement_d2_005'], 'func': rd_replacement_d3_005}


def rd_replacement_d3_006(rd_replacement_d2_006):
    feature = _clean(rd_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_006'] = {'inputs': ['rd_replacement_d2_006'], 'func': rd_replacement_d3_006}


def rd_replacement_d3_007(rd_replacement_d2_007):
    feature = _clean(rd_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_007'] = {'inputs': ['rd_replacement_d2_007'], 'func': rd_replacement_d3_007}


def rd_replacement_d3_008(rd_replacement_d2_008):
    feature = _clean(rd_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_008'] = {'inputs': ['rd_replacement_d2_008'], 'func': rd_replacement_d3_008}


def rd_replacement_d3_009(rd_replacement_d2_009):
    feature = _clean(rd_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_009'] = {'inputs': ['rd_replacement_d2_009'], 'func': rd_replacement_d3_009}


def rd_replacement_d3_010(rd_replacement_d2_010):
    feature = _clean(rd_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_010'] = {'inputs': ['rd_replacement_d2_010'], 'func': rd_replacement_d3_010}


def rd_replacement_d3_011(rd_replacement_d2_011):
    feature = _clean(rd_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_011'] = {'inputs': ['rd_replacement_d2_011'], 'func': rd_replacement_d3_011}


def rd_replacement_d3_012(rd_replacement_d2_012):
    feature = _clean(rd_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_012'] = {'inputs': ['rd_replacement_d2_012'], 'func': rd_replacement_d3_012}


def rd_replacement_d3_013(rd_replacement_d2_013):
    feature = _clean(rd_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_013'] = {'inputs': ['rd_replacement_d2_013'], 'func': rd_replacement_d3_013}


def rd_replacement_d3_014(rd_replacement_d2_014):
    feature = _clean(rd_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_014'] = {'inputs': ['rd_replacement_d2_014'], 'func': rd_replacement_d3_014}


def rd_replacement_d3_015(rd_replacement_d2_015):
    feature = _clean(rd_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_015'] = {'inputs': ['rd_replacement_d2_015'], 'func': rd_replacement_d3_015}


def rd_replacement_d3_016(rd_replacement_d2_016):
    feature = _clean(rd_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_016'] = {'inputs': ['rd_replacement_d2_016'], 'func': rd_replacement_d3_016}


def rd_replacement_d3_017(rd_replacement_d2_017):
    feature = _clean(rd_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_017'] = {'inputs': ['rd_replacement_d2_017'], 'func': rd_replacement_d3_017}


def rd_replacement_d3_018(rd_replacement_d2_018):
    feature = _clean(rd_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_018'] = {'inputs': ['rd_replacement_d2_018'], 'func': rd_replacement_d3_018}


def rd_replacement_d3_019(rd_replacement_d2_019):
    feature = _clean(rd_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_019'] = {'inputs': ['rd_replacement_d2_019'], 'func': rd_replacement_d3_019}


def rd_replacement_d3_020(rd_replacement_d2_020):
    feature = _clean(rd_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_020'] = {'inputs': ['rd_replacement_d2_020'], 'func': rd_replacement_d3_020}


def rd_replacement_d3_021(rd_replacement_d2_021):
    feature = _clean(rd_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_021'] = {'inputs': ['rd_replacement_d2_021'], 'func': rd_replacement_d3_021}


def rd_replacement_d3_022(rd_replacement_d2_022):
    feature = _clean(rd_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_022'] = {'inputs': ['rd_replacement_d2_022'], 'func': rd_replacement_d3_022}


def rd_replacement_d3_023(rd_replacement_d2_023):
    feature = _clean(rd_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_023'] = {'inputs': ['rd_replacement_d2_023'], 'func': rd_replacement_d3_023}


def rd_replacement_d3_024(rd_replacement_d2_024):
    feature = _clean(rd_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_024'] = {'inputs': ['rd_replacement_d2_024'], 'func': rd_replacement_d3_024}


def rd_replacement_d3_025(rd_replacement_d2_025):
    feature = _clean(rd_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_025'] = {'inputs': ['rd_replacement_d2_025'], 'func': rd_replacement_d3_025}


def rd_replacement_d3_026(rd_replacement_d2_026):
    feature = _clean(rd_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_026'] = {'inputs': ['rd_replacement_d2_026'], 'func': rd_replacement_d3_026}


def rd_replacement_d3_027(rd_replacement_d2_027):
    feature = _clean(rd_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_027'] = {'inputs': ['rd_replacement_d2_027'], 'func': rd_replacement_d3_027}


def rd_replacement_d3_028(rd_replacement_d2_028):
    feature = _clean(rd_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_028'] = {'inputs': ['rd_replacement_d2_028'], 'func': rd_replacement_d3_028}


def rd_replacement_d3_029(rd_replacement_d2_029):
    feature = _clean(rd_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_029'] = {'inputs': ['rd_replacement_d2_029'], 'func': rd_replacement_d3_029}


def rd_replacement_d3_030(rd_replacement_d2_030):
    feature = _clean(rd_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_030'] = {'inputs': ['rd_replacement_d2_030'], 'func': rd_replacement_d3_030}


def rd_replacement_d3_031(rd_replacement_d2_031):
    feature = _clean(rd_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_031'] = {'inputs': ['rd_replacement_d2_031'], 'func': rd_replacement_d3_031}


def rd_replacement_d3_032(rd_replacement_d2_032):
    feature = _clean(rd_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_032'] = {'inputs': ['rd_replacement_d2_032'], 'func': rd_replacement_d3_032}


def rd_replacement_d3_033(rd_replacement_d2_033):
    feature = _clean(rd_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_033'] = {'inputs': ['rd_replacement_d2_033'], 'func': rd_replacement_d3_033}


def rd_replacement_d3_034(rd_replacement_d2_034):
    feature = _clean(rd_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_034'] = {'inputs': ['rd_replacement_d2_034'], 'func': rd_replacement_d3_034}


def rd_replacement_d3_035(rd_replacement_d2_035):
    feature = _clean(rd_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_035'] = {'inputs': ['rd_replacement_d2_035'], 'func': rd_replacement_d3_035}


def rd_replacement_d3_036(rd_replacement_d2_036):
    feature = _clean(rd_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_036'] = {'inputs': ['rd_replacement_d2_036'], 'func': rd_replacement_d3_036}


def rd_replacement_d3_037(rd_replacement_d2_037):
    feature = _clean(rd_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_037'] = {'inputs': ['rd_replacement_d2_037'], 'func': rd_replacement_d3_037}


def rd_replacement_d3_038(rd_replacement_d2_038):
    feature = _clean(rd_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_038'] = {'inputs': ['rd_replacement_d2_038'], 'func': rd_replacement_d3_038}


def rd_replacement_d3_039(rd_replacement_d2_039):
    feature = _clean(rd_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_039'] = {'inputs': ['rd_replacement_d2_039'], 'func': rd_replacement_d3_039}


def rd_replacement_d3_040(rd_replacement_d2_040):
    feature = _clean(rd_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_040'] = {'inputs': ['rd_replacement_d2_040'], 'func': rd_replacement_d3_040}


def rd_replacement_d3_041(rd_replacement_d2_041):
    feature = _clean(rd_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_041'] = {'inputs': ['rd_replacement_d2_041'], 'func': rd_replacement_d3_041}


def rd_replacement_d3_042(rd_replacement_d2_042):
    feature = _clean(rd_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_042'] = {'inputs': ['rd_replacement_d2_042'], 'func': rd_replacement_d3_042}


def rd_replacement_d3_043(rd_replacement_d2_043):
    feature = _clean(rd_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_043'] = {'inputs': ['rd_replacement_d2_043'], 'func': rd_replacement_d3_043}


def rd_replacement_d3_044(rd_replacement_d2_044):
    feature = _clean(rd_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_044'] = {'inputs': ['rd_replacement_d2_044'], 'func': rd_replacement_d3_044}


def rd_replacement_d3_045(rd_replacement_d2_045):
    feature = _clean(rd_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_045'] = {'inputs': ['rd_replacement_d2_045'], 'func': rd_replacement_d3_045}


def rd_replacement_d3_046(rd_replacement_d2_046):
    feature = _clean(rd_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_046'] = {'inputs': ['rd_replacement_d2_046'], 'func': rd_replacement_d3_046}


def rd_replacement_d3_047(rd_replacement_d2_047):
    feature = _clean(rd_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_047'] = {'inputs': ['rd_replacement_d2_047'], 'func': rd_replacement_d3_047}


def rd_replacement_d3_048(rd_replacement_d2_048):
    feature = _clean(rd_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_048'] = {'inputs': ['rd_replacement_d2_048'], 'func': rd_replacement_d3_048}


def rd_replacement_d3_049(rd_replacement_d2_049):
    feature = _clean(rd_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_049'] = {'inputs': ['rd_replacement_d2_049'], 'func': rd_replacement_d3_049}


def rd_replacement_d3_050(rd_replacement_d2_050):
    feature = _clean(rd_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_050'] = {'inputs': ['rd_replacement_d2_050'], 'func': rd_replacement_d3_050}


def rd_replacement_d3_051(rd_replacement_d2_051):
    feature = _clean(rd_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_051'] = {'inputs': ['rd_replacement_d2_051'], 'func': rd_replacement_d3_051}


def rd_replacement_d3_052(rd_replacement_d2_052):
    feature = _clean(rd_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_052'] = {'inputs': ['rd_replacement_d2_052'], 'func': rd_replacement_d3_052}


def rd_replacement_d3_053(rd_replacement_d2_053):
    feature = _clean(rd_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_053'] = {'inputs': ['rd_replacement_d2_053'], 'func': rd_replacement_d3_053}


def rd_replacement_d3_054(rd_replacement_d2_054):
    feature = _clean(rd_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_054'] = {'inputs': ['rd_replacement_d2_054'], 'func': rd_replacement_d3_054}


def rd_replacement_d3_055(rd_replacement_d2_055):
    feature = _clean(rd_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_055'] = {'inputs': ['rd_replacement_d2_055'], 'func': rd_replacement_d3_055}


def rd_replacement_d3_056(rd_replacement_d2_056):
    feature = _clean(rd_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_056'] = {'inputs': ['rd_replacement_d2_056'], 'func': rd_replacement_d3_056}


def rd_replacement_d3_057(rd_replacement_d2_057):
    feature = _clean(rd_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_057'] = {'inputs': ['rd_replacement_d2_057'], 'func': rd_replacement_d3_057}


def rd_replacement_d3_058(rd_replacement_d2_058):
    feature = _clean(rd_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_058'] = {'inputs': ['rd_replacement_d2_058'], 'func': rd_replacement_d3_058}


def rd_replacement_d3_059(rd_replacement_d2_059):
    feature = _clean(rd_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_059'] = {'inputs': ['rd_replacement_d2_059'], 'func': rd_replacement_d3_059}


def rd_replacement_d3_060(rd_replacement_d2_060):
    feature = _clean(rd_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_060'] = {'inputs': ['rd_replacement_d2_060'], 'func': rd_replacement_d3_060}


def rd_replacement_d3_061(rd_replacement_d2_061):
    feature = _clean(rd_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_061'] = {'inputs': ['rd_replacement_d2_061'], 'func': rd_replacement_d3_061}


def rd_replacement_d3_062(rd_replacement_d2_062):
    feature = _clean(rd_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_062'] = {'inputs': ['rd_replacement_d2_062'], 'func': rd_replacement_d3_062}


def rd_replacement_d3_063(rd_replacement_d2_063):
    feature = _clean(rd_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_063'] = {'inputs': ['rd_replacement_d2_063'], 'func': rd_replacement_d3_063}


def rd_replacement_d3_064(rd_replacement_d2_064):
    feature = _clean(rd_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_064'] = {'inputs': ['rd_replacement_d2_064'], 'func': rd_replacement_d3_064}


def rd_replacement_d3_065(rd_replacement_d2_065):
    feature = _clean(rd_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_065'] = {'inputs': ['rd_replacement_d2_065'], 'func': rd_replacement_d3_065}


def rd_replacement_d3_066(rd_replacement_d2_066):
    feature = _clean(rd_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_066'] = {'inputs': ['rd_replacement_d2_066'], 'func': rd_replacement_d3_066}


def rd_replacement_d3_067(rd_replacement_d2_067):
    feature = _clean(rd_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_067'] = {'inputs': ['rd_replacement_d2_067'], 'func': rd_replacement_d3_067}


def rd_replacement_d3_068(rd_replacement_d2_068):
    feature = _clean(rd_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_068'] = {'inputs': ['rd_replacement_d2_068'], 'func': rd_replacement_d3_068}


def rd_replacement_d3_069(rd_replacement_d2_069):
    feature = _clean(rd_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_069'] = {'inputs': ['rd_replacement_d2_069'], 'func': rd_replacement_d3_069}


def rd_replacement_d3_070(rd_replacement_d2_070):
    feature = _clean(rd_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_070'] = {'inputs': ['rd_replacement_d2_070'], 'func': rd_replacement_d3_070}


def rd_replacement_d3_071(rd_replacement_d2_071):
    feature = _clean(rd_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_071'] = {'inputs': ['rd_replacement_d2_071'], 'func': rd_replacement_d3_071}


def rd_replacement_d3_072(rd_replacement_d2_072):
    feature = _clean(rd_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_072'] = {'inputs': ['rd_replacement_d2_072'], 'func': rd_replacement_d3_072}


def rd_replacement_d3_073(rd_replacement_d2_073):
    feature = _clean(rd_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_073'] = {'inputs': ['rd_replacement_d2_073'], 'func': rd_replacement_d3_073}


def rd_replacement_d3_074(rd_replacement_d2_074):
    feature = _clean(rd_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_074'] = {'inputs': ['rd_replacement_d2_074'], 'func': rd_replacement_d3_074}


def rd_replacement_d3_075(rd_replacement_d2_075):
    feature = _clean(rd_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_075'] = {'inputs': ['rd_replacement_d2_075'], 'func': rd_replacement_d3_075}


def rd_replacement_d3_076(rd_replacement_d2_076):
    feature = _clean(rd_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_076'] = {'inputs': ['rd_replacement_d2_076'], 'func': rd_replacement_d3_076}


def rd_replacement_d3_077(rd_replacement_d2_077):
    feature = _clean(rd_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_077'] = {'inputs': ['rd_replacement_d2_077'], 'func': rd_replacement_d3_077}


def rd_replacement_d3_078(rd_replacement_d2_078):
    feature = _clean(rd_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_078'] = {'inputs': ['rd_replacement_d2_078'], 'func': rd_replacement_d3_078}


def rd_replacement_d3_079(rd_replacement_d2_079):
    feature = _clean(rd_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_079'] = {'inputs': ['rd_replacement_d2_079'], 'func': rd_replacement_d3_079}


def rd_replacement_d3_080(rd_replacement_d2_080):
    feature = _clean(rd_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_080'] = {'inputs': ['rd_replacement_d2_080'], 'func': rd_replacement_d3_080}


def rd_replacement_d3_081(rd_replacement_d2_081):
    feature = _clean(rd_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_081'] = {'inputs': ['rd_replacement_d2_081'], 'func': rd_replacement_d3_081}


def rd_replacement_d3_082(rd_replacement_d2_082):
    feature = _clean(rd_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_082'] = {'inputs': ['rd_replacement_d2_082'], 'func': rd_replacement_d3_082}


def rd_replacement_d3_083(rd_replacement_d2_083):
    feature = _clean(rd_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_083'] = {'inputs': ['rd_replacement_d2_083'], 'func': rd_replacement_d3_083}


def rd_replacement_d3_084(rd_replacement_d2_084):
    feature = _clean(rd_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_084'] = {'inputs': ['rd_replacement_d2_084'], 'func': rd_replacement_d3_084}


def rd_replacement_d3_085(rd_replacement_d2_085):
    feature = _clean(rd_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_085'] = {'inputs': ['rd_replacement_d2_085'], 'func': rd_replacement_d3_085}


def rd_replacement_d3_086(rd_replacement_d2_086):
    feature = _clean(rd_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_086'] = {'inputs': ['rd_replacement_d2_086'], 'func': rd_replacement_d3_086}


def rd_replacement_d3_087(rd_replacement_d2_087):
    feature = _clean(rd_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_087'] = {'inputs': ['rd_replacement_d2_087'], 'func': rd_replacement_d3_087}


def rd_replacement_d3_088(rd_replacement_d2_088):
    feature = _clean(rd_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_088'] = {'inputs': ['rd_replacement_d2_088'], 'func': rd_replacement_d3_088}


def rd_replacement_d3_089(rd_replacement_d2_089):
    feature = _clean(rd_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_089'] = {'inputs': ['rd_replacement_d2_089'], 'func': rd_replacement_d3_089}


def rd_replacement_d3_090(rd_replacement_d2_090):
    feature = _clean(rd_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_090'] = {'inputs': ['rd_replacement_d2_090'], 'func': rd_replacement_d3_090}


def rd_replacement_d3_091(rd_replacement_d2_091):
    feature = _clean(rd_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_091'] = {'inputs': ['rd_replacement_d2_091'], 'func': rd_replacement_d3_091}


def rd_replacement_d3_092(rd_replacement_d2_092):
    feature = _clean(rd_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_092'] = {'inputs': ['rd_replacement_d2_092'], 'func': rd_replacement_d3_092}


def rd_replacement_d3_093(rd_replacement_d2_093):
    feature = _clean(rd_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_093'] = {'inputs': ['rd_replacement_d2_093'], 'func': rd_replacement_d3_093}


def rd_replacement_d3_094(rd_replacement_d2_094):
    feature = _clean(rd_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_094'] = {'inputs': ['rd_replacement_d2_094'], 'func': rd_replacement_d3_094}


def rd_replacement_d3_095(rd_replacement_d2_095):
    feature = _clean(rd_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_095'] = {'inputs': ['rd_replacement_d2_095'], 'func': rd_replacement_d3_095}


def rd_replacement_d3_096(rd_replacement_d2_096):
    feature = _clean(rd_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_096'] = {'inputs': ['rd_replacement_d2_096'], 'func': rd_replacement_d3_096}


def rd_replacement_d3_097(rd_replacement_d2_097):
    feature = _clean(rd_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_097'] = {'inputs': ['rd_replacement_d2_097'], 'func': rd_replacement_d3_097}


def rd_replacement_d3_098(rd_replacement_d2_098):
    feature = _clean(rd_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_098'] = {'inputs': ['rd_replacement_d2_098'], 'func': rd_replacement_d3_098}


def rd_replacement_d3_099(rd_replacement_d2_099):
    feature = _clean(rd_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_099'] = {'inputs': ['rd_replacement_d2_099'], 'func': rd_replacement_d3_099}


def rd_replacement_d3_100(rd_replacement_d2_100):
    feature = _clean(rd_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_100'] = {'inputs': ['rd_replacement_d2_100'], 'func': rd_replacement_d3_100}


def rd_replacement_d3_101(rd_replacement_d2_101):
    feature = _clean(rd_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_101'] = {'inputs': ['rd_replacement_d2_101'], 'func': rd_replacement_d3_101}


def rd_replacement_d3_102(rd_replacement_d2_102):
    feature = _clean(rd_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_102'] = {'inputs': ['rd_replacement_d2_102'], 'func': rd_replacement_d3_102}


def rd_replacement_d3_103(rd_replacement_d2_103):
    feature = _clean(rd_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_103'] = {'inputs': ['rd_replacement_d2_103'], 'func': rd_replacement_d3_103}


def rd_replacement_d3_104(rd_replacement_d2_104):
    feature = _clean(rd_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_104'] = {'inputs': ['rd_replacement_d2_104'], 'func': rd_replacement_d3_104}


def rd_replacement_d3_105(rd_replacement_d2_105):
    feature = _clean(rd_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_105'] = {'inputs': ['rd_replacement_d2_105'], 'func': rd_replacement_d3_105}


def rd_replacement_d3_106(rd_replacement_d2_106):
    feature = _clean(rd_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_106'] = {'inputs': ['rd_replacement_d2_106'], 'func': rd_replacement_d3_106}


def rd_replacement_d3_107(rd_replacement_d2_107):
    feature = _clean(rd_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_107'] = {'inputs': ['rd_replacement_d2_107'], 'func': rd_replacement_d3_107}


def rd_replacement_d3_108(rd_replacement_d2_108):
    feature = _clean(rd_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_108'] = {'inputs': ['rd_replacement_d2_108'], 'func': rd_replacement_d3_108}


def rd_replacement_d3_109(rd_replacement_d2_109):
    feature = _clean(rd_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_109'] = {'inputs': ['rd_replacement_d2_109'], 'func': rd_replacement_d3_109}


def rd_replacement_d3_110(rd_replacement_d2_110):
    feature = _clean(rd_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_110'] = {'inputs': ['rd_replacement_d2_110'], 'func': rd_replacement_d3_110}


def rd_replacement_d3_111(rd_replacement_d2_111):
    feature = _clean(rd_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_111'] = {'inputs': ['rd_replacement_d2_111'], 'func': rd_replacement_d3_111}


def rd_replacement_d3_112(rd_replacement_d2_112):
    feature = _clean(rd_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_112'] = {'inputs': ['rd_replacement_d2_112'], 'func': rd_replacement_d3_112}


def rd_replacement_d3_113(rd_replacement_d2_113):
    feature = _clean(rd_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_113'] = {'inputs': ['rd_replacement_d2_113'], 'func': rd_replacement_d3_113}


def rd_replacement_d3_114(rd_replacement_d2_114):
    feature = _clean(rd_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_114'] = {'inputs': ['rd_replacement_d2_114'], 'func': rd_replacement_d3_114}


def rd_replacement_d3_115(rd_replacement_d2_115):
    feature = _clean(rd_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_115'] = {'inputs': ['rd_replacement_d2_115'], 'func': rd_replacement_d3_115}


def rd_replacement_d3_116(rd_replacement_d2_116):
    feature = _clean(rd_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_116'] = {'inputs': ['rd_replacement_d2_116'], 'func': rd_replacement_d3_116}


def rd_replacement_d3_117(rd_replacement_d2_117):
    feature = _clean(rd_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_117'] = {'inputs': ['rd_replacement_d2_117'], 'func': rd_replacement_d3_117}


def rd_replacement_d3_118(rd_replacement_d2_118):
    feature = _clean(rd_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_118'] = {'inputs': ['rd_replacement_d2_118'], 'func': rd_replacement_d3_118}


def rd_replacement_d3_119(rd_replacement_d2_119):
    feature = _clean(rd_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_119'] = {'inputs': ['rd_replacement_d2_119'], 'func': rd_replacement_d3_119}


def rd_replacement_d3_120(rd_replacement_d2_120):
    feature = _clean(rd_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_120'] = {'inputs': ['rd_replacement_d2_120'], 'func': rd_replacement_d3_120}


def rd_replacement_d3_121(rd_replacement_d2_121):
    feature = _clean(rd_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_121'] = {'inputs': ['rd_replacement_d2_121'], 'func': rd_replacement_d3_121}


def rd_replacement_d3_122(rd_replacement_d2_122):
    feature = _clean(rd_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_122'] = {'inputs': ['rd_replacement_d2_122'], 'func': rd_replacement_d3_122}


def rd_replacement_d3_123(rd_replacement_d2_123):
    feature = _clean(rd_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_123'] = {'inputs': ['rd_replacement_d2_123'], 'func': rd_replacement_d3_123}


def rd_replacement_d3_124(rd_replacement_d2_124):
    feature = _clean(rd_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_124'] = {'inputs': ['rd_replacement_d2_124'], 'func': rd_replacement_d3_124}


def rd_replacement_d3_125(rd_replacement_d2_125):
    feature = _clean(rd_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_125'] = {'inputs': ['rd_replacement_d2_125'], 'func': rd_replacement_d3_125}


def rd_replacement_d3_126(rd_replacement_d2_126):
    feature = _clean(rd_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_126'] = {'inputs': ['rd_replacement_d2_126'], 'func': rd_replacement_d3_126}


def rd_replacement_d3_127(rd_replacement_d2_127):
    feature = _clean(rd_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_127'] = {'inputs': ['rd_replacement_d2_127'], 'func': rd_replacement_d3_127}


def rd_replacement_d3_128(rd_replacement_d2_128):
    feature = _clean(rd_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_128'] = {'inputs': ['rd_replacement_d2_128'], 'func': rd_replacement_d3_128}


def rd_replacement_d3_129(rd_replacement_d2_129):
    feature = _clean(rd_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_129'] = {'inputs': ['rd_replacement_d2_129'], 'func': rd_replacement_d3_129}


def rd_replacement_d3_130(rd_replacement_d2_130):
    feature = _clean(rd_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_130'] = {'inputs': ['rd_replacement_d2_130'], 'func': rd_replacement_d3_130}


def rd_replacement_d3_131(rd_replacement_d2_131):
    feature = _clean(rd_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_131'] = {'inputs': ['rd_replacement_d2_131'], 'func': rd_replacement_d3_131}


def rd_replacement_d3_132(rd_replacement_d2_132):
    feature = _clean(rd_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_132'] = {'inputs': ['rd_replacement_d2_132'], 'func': rd_replacement_d3_132}


def rd_replacement_d3_133(rd_replacement_d2_133):
    feature = _clean(rd_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_133'] = {'inputs': ['rd_replacement_d2_133'], 'func': rd_replacement_d3_133}


def rd_replacement_d3_134(rd_replacement_d2_134):
    feature = _clean(rd_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_134'] = {'inputs': ['rd_replacement_d2_134'], 'func': rd_replacement_d3_134}


def rd_replacement_d3_135(rd_replacement_d2_135):
    feature = _clean(rd_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_135'] = {'inputs': ['rd_replacement_d2_135'], 'func': rd_replacement_d3_135}


def rd_replacement_d3_136(rd_replacement_d2_136):
    feature = _clean(rd_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_136'] = {'inputs': ['rd_replacement_d2_136'], 'func': rd_replacement_d3_136}


def rd_replacement_d3_137(rd_replacement_d2_137):
    feature = _clean(rd_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_137'] = {'inputs': ['rd_replacement_d2_137'], 'func': rd_replacement_d3_137}


def rd_replacement_d3_138(rd_replacement_d2_138):
    feature = _clean(rd_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_138'] = {'inputs': ['rd_replacement_d2_138'], 'func': rd_replacement_d3_138}


def rd_replacement_d3_139(rd_replacement_d2_139):
    feature = _clean(rd_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_139'] = {'inputs': ['rd_replacement_d2_139'], 'func': rd_replacement_d3_139}


def rd_replacement_d3_140(rd_replacement_d2_140):
    feature = _clean(rd_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_140'] = {'inputs': ['rd_replacement_d2_140'], 'func': rd_replacement_d3_140}


def rd_replacement_d3_141(rd_replacement_d2_141):
    feature = _clean(rd_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_141'] = {'inputs': ['rd_replacement_d2_141'], 'func': rd_replacement_d3_141}


def rd_replacement_d3_142(rd_replacement_d2_142):
    feature = _clean(rd_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_142'] = {'inputs': ['rd_replacement_d2_142'], 'func': rd_replacement_d3_142}


def rd_replacement_d3_143(rd_replacement_d2_143):
    feature = _clean(rd_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_143'] = {'inputs': ['rd_replacement_d2_143'], 'func': rd_replacement_d3_143}


def rd_replacement_d3_144(rd_replacement_d2_144):
    feature = _clean(rd_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_144'] = {'inputs': ['rd_replacement_d2_144'], 'func': rd_replacement_d3_144}


def rd_replacement_d3_145(rd_replacement_d2_145):
    feature = _clean(rd_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_145'] = {'inputs': ['rd_replacement_d2_145'], 'func': rd_replacement_d3_145}


def rd_replacement_d3_146(rd_replacement_d2_146):
    feature = _clean(rd_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_146'] = {'inputs': ['rd_replacement_d2_146'], 'func': rd_replacement_d3_146}


def rd_replacement_d3_147(rd_replacement_d2_147):
    feature = _clean(rd_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_147'] = {'inputs': ['rd_replacement_d2_147'], 'func': rd_replacement_d3_147}


def rd_replacement_d3_148(rd_replacement_d2_148):
    feature = _clean(rd_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_148'] = {'inputs': ['rd_replacement_d2_148'], 'func': rd_replacement_d3_148}


def rd_replacement_d3_149(rd_replacement_d2_149):
    feature = _clean(rd_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_149'] = {'inputs': ['rd_replacement_d2_149'], 'func': rd_replacement_d3_149}


def rd_replacement_d3_150(rd_replacement_d2_150):
    feature = _clean(rd_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_150'] = {'inputs': ['rd_replacement_d2_150'], 'func': rd_replacement_d3_150}


def rd_replacement_d3_151(rd_replacement_d2_151):
    feature = _clean(rd_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_151'] = {'inputs': ['rd_replacement_d2_151'], 'func': rd_replacement_d3_151}


def rd_replacement_d3_152(rd_replacement_d2_152):
    feature = _clean(rd_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_152'] = {'inputs': ['rd_replacement_d2_152'], 'func': rd_replacement_d3_152}


def rd_replacement_d3_153(rd_replacement_d2_153):
    feature = _clean(rd_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_153'] = {'inputs': ['rd_replacement_d2_153'], 'func': rd_replacement_d3_153}


def rd_replacement_d3_154(rd_replacement_d2_154):
    feature = _clean(rd_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_154'] = {'inputs': ['rd_replacement_d2_154'], 'func': rd_replacement_d3_154}


def rd_replacement_d3_155(rd_replacement_d2_155):
    feature = _clean(rd_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_155'] = {'inputs': ['rd_replacement_d2_155'], 'func': rd_replacement_d3_155}


def rd_replacement_d3_156(rd_replacement_d2_156):
    feature = _clean(rd_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_156'] = {'inputs': ['rd_replacement_d2_156'], 'func': rd_replacement_d3_156}


def rd_replacement_d3_157(rd_replacement_d2_157):
    feature = _clean(rd_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_157'] = {'inputs': ['rd_replacement_d2_157'], 'func': rd_replacement_d3_157}


def rd_replacement_d3_158(rd_replacement_d2_158):
    feature = _clean(rd_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_158'] = {'inputs': ['rd_replacement_d2_158'], 'func': rd_replacement_d3_158}


def rd_replacement_d3_159(rd_replacement_d2_159):
    feature = _clean(rd_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_159'] = {'inputs': ['rd_replacement_d2_159'], 'func': rd_replacement_d3_159}


def rd_replacement_d3_160(rd_replacement_d2_160):
    feature = _clean(rd_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_160'] = {'inputs': ['rd_replacement_d2_160'], 'func': rd_replacement_d3_160}


def rd_replacement_d3_161(rd_replacement_d2_161):
    feature = _clean(rd_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_161'] = {'inputs': ['rd_replacement_d2_161'], 'func': rd_replacement_d3_161}


def rd_replacement_d3_162(rd_replacement_d2_162):
    feature = _clean(rd_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_162'] = {'inputs': ['rd_replacement_d2_162'], 'func': rd_replacement_d3_162}


def rd_replacement_d3_163(rd_replacement_d2_163):
    feature = _clean(rd_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_163'] = {'inputs': ['rd_replacement_d2_163'], 'func': rd_replacement_d3_163}


def rd_replacement_d3_164(rd_replacement_d2_164):
    feature = _clean(rd_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_164'] = {'inputs': ['rd_replacement_d2_164'], 'func': rd_replacement_d3_164}


def rd_replacement_d3_165(rd_replacement_d2_165):
    feature = _clean(rd_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_165'] = {'inputs': ['rd_replacement_d2_165'], 'func': rd_replacement_d3_165}


def rd_replacement_d3_166(rd_replacement_d2_166):
    feature = _clean(rd_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_166'] = {'inputs': ['rd_replacement_d2_166'], 'func': rd_replacement_d3_166}


# Third-derivative extensions for repaired first-base features.
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def rvd_base_universe_d3_001_rvd_003_fcf_burn_to_cash_63(rvd_base_universe_d2_001_rvd_003_fcf_burn_to_cash_63):
    return _base_universe_d3(rvd_base_universe_d2_001_rvd_003_fcf_burn_to_cash_63, 1)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_001_rvd_003_fcf_burn_to_cash_63'] = {'inputs': ['rvd_base_universe_d2_001_rvd_003_fcf_burn_to_cash_63'], 'func': rvd_base_universe_d3_001_rvd_003_fcf_burn_to_cash_63}


def rvd_base_universe_d3_002_rvd_004_debt_to_equity_84(rvd_base_universe_d2_002_rvd_004_debt_to_equity_84):
    return _base_universe_d3(rvd_base_universe_d2_002_rvd_004_debt_to_equity_84, 2)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_002_rvd_004_debt_to_equity_84'] = {'inputs': ['rvd_base_universe_d2_002_rvd_004_debt_to_equity_84'], 'func': rvd_base_universe_d3_002_rvd_004_debt_to_equity_84}


def rvd_base_universe_d3_003_rvd_005_debt_to_assets_126(rvd_base_universe_d2_003_rvd_005_debt_to_assets_126):
    return _base_universe_d3(rvd_base_universe_d2_003_rvd_005_debt_to_assets_126, 3)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_003_rvd_005_debt_to_assets_126'] = {'inputs': ['rvd_base_universe_d2_003_rvd_005_debt_to_assets_126'], 'func': rvd_base_universe_d3_003_rvd_005_debt_to_assets_126}


def rvd_base_universe_d3_004_rvd_012_accrual_gap_1260(rvd_base_universe_d2_004_rvd_012_accrual_gap_1260):
    return _base_universe_d3(rvd_base_universe_d2_004_rvd_012_accrual_gap_1260, 4)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_004_rvd_012_accrual_gap_1260'] = {'inputs': ['rvd_base_universe_d2_004_rvd_012_accrual_gap_1260'], 'func': rvd_base_universe_d3_004_rvd_012_accrual_gap_1260}


def rvd_base_universe_d3_005_rvd_016_debt_to_equity_21(rvd_base_universe_d2_005_rvd_016_debt_to_equity_21):
    return _base_universe_d3(rvd_base_universe_d2_005_rvd_016_debt_to_equity_21, 5)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_005_rvd_016_debt_to_equity_21'] = {'inputs': ['rvd_base_universe_d2_005_rvd_016_debt_to_equity_21'], 'func': rvd_base_universe_d3_005_rvd_016_debt_to_equity_21}


def rvd_base_universe_d3_006_rvd_017_debt_to_assets_42(rvd_base_universe_d2_006_rvd_017_debt_to_assets_42):
    return _base_universe_d3(rvd_base_universe_d2_006_rvd_017_debt_to_assets_42, 6)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_006_rvd_017_debt_to_assets_42'] = {'inputs': ['rvd_base_universe_d2_006_rvd_017_debt_to_assets_42'], 'func': rvd_base_universe_d3_006_rvd_017_debt_to_assets_42}


def rvd_base_universe_d3_007_rvd_024_accrual_gap_504(rvd_base_universe_d2_007_rvd_024_accrual_gap_504):
    return _base_universe_d3(rvd_base_universe_d2_007_rvd_024_accrual_gap_504, 7)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_007_rvd_024_accrual_gap_504'] = {'inputs': ['rvd_base_universe_d2_007_rvd_024_accrual_gap_504'], 'func': rvd_base_universe_d3_007_rvd_024_accrual_gap_504}


def rvd_base_universe_d3_008_rvd_027_fcf_burn_to_cash_1260(rvd_base_universe_d2_008_rvd_027_fcf_burn_to_cash_1260):
    return _base_universe_d3(rvd_base_universe_d2_008_rvd_027_fcf_burn_to_cash_1260, 8)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_008_rvd_027_fcf_burn_to_cash_1260'] = {'inputs': ['rvd_base_universe_d2_008_rvd_027_fcf_burn_to_cash_1260'], 'func': rvd_base_universe_d3_008_rvd_027_fcf_burn_to_cash_1260}


def rvd_base_universe_d3_009_rvd_028_debt_to_equity_1512(rvd_base_universe_d2_009_rvd_028_debt_to_equity_1512):
    return _base_universe_d3(rvd_base_universe_d2_009_rvd_028_debt_to_equity_1512, 9)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_009_rvd_028_debt_to_equity_1512'] = {'inputs': ['rvd_base_universe_d2_009_rvd_028_debt_to_equity_1512'], 'func': rvd_base_universe_d3_009_rvd_028_debt_to_equity_1512}


def rvd_base_universe_d3_010_rvd_029_debt_to_assets_63(rvd_base_universe_d2_010_rvd_029_debt_to_assets_63):
    return _base_universe_d3(rvd_base_universe_d2_010_rvd_029_debt_to_assets_63, 10)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_010_rvd_029_debt_to_assets_63'] = {'inputs': ['rvd_base_universe_d2_010_rvd_029_debt_to_assets_63'], 'func': rvd_base_universe_d3_010_rvd_029_debt_to_assets_63}


def rvd_base_universe_d3_011_rvd_031_interest_coverage_stress_21(rvd_base_universe_d2_011_rvd_031_interest_coverage_stress_21):
    return _base_universe_d3(rvd_base_universe_d2_011_rvd_031_interest_coverage_stress_21, 11)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_011_rvd_031_interest_coverage_stress_21'] = {'inputs': ['rvd_base_universe_d2_011_rvd_031_interest_coverage_stress_21'], 'func': rvd_base_universe_d3_011_rvd_031_interest_coverage_stress_21}


def rvd_base_universe_d3_012_rvd_036_accrual_gap_189(rvd_base_universe_d2_012_rvd_036_accrual_gap_189):
    return _base_universe_d3(rvd_base_universe_d2_012_rvd_036_accrual_gap_189, 12)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_012_rvd_036_accrual_gap_189'] = {'inputs': ['rvd_base_universe_d2_012_rvd_036_accrual_gap_189'], 'func': rvd_base_universe_d3_012_rvd_036_accrual_gap_189}


def rvd_base_universe_d3_013_rvd_039_fcf_burn_to_cash_504(rvd_base_universe_d2_013_rvd_039_fcf_burn_to_cash_504):
    return _base_universe_d3(rvd_base_universe_d2_013_rvd_039_fcf_burn_to_cash_504, 13)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_013_rvd_039_fcf_burn_to_cash_504'] = {'inputs': ['rvd_base_universe_d2_013_rvd_039_fcf_burn_to_cash_504'], 'func': rvd_base_universe_d3_013_rvd_039_fcf_burn_to_cash_504}


def rvd_base_universe_d3_014_rvd_040_debt_to_equity_756(rvd_base_universe_d2_014_rvd_040_debt_to_equity_756):
    return _base_universe_d3(rvd_base_universe_d2_014_rvd_040_debt_to_equity_756, 14)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_014_rvd_040_debt_to_equity_756'] = {'inputs': ['rvd_base_universe_d2_014_rvd_040_debt_to_equity_756'], 'func': rvd_base_universe_d3_014_rvd_040_debt_to_equity_756}


def rvd_base_universe_d3_015_rvd_041_debt_to_assets_1008(rvd_base_universe_d2_015_rvd_041_debt_to_assets_1008):
    return _base_universe_d3(rvd_base_universe_d2_015_rvd_041_debt_to_assets_1008, 15)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_015_rvd_041_debt_to_assets_1008'] = {'inputs': ['rvd_base_universe_d2_015_rvd_041_debt_to_assets_1008'], 'func': rvd_base_universe_d3_015_rvd_041_debt_to_assets_1008}


def rvd_base_universe_d3_016_rvd_043_interest_coverage_stress_1512(rvd_base_universe_d2_016_rvd_043_interest_coverage_stress_1512):
    return _base_universe_d3(rvd_base_universe_d2_016_rvd_043_interest_coverage_stress_1512, 16)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_016_rvd_043_interest_coverage_stress_1512'] = {'inputs': ['rvd_base_universe_d2_016_rvd_043_interest_coverage_stress_1512'], 'func': rvd_base_universe_d3_016_rvd_043_interest_coverage_stress_1512}


def rvd_base_universe_d3_017_rvd_048_accrual_gap_63(rvd_base_universe_d2_017_rvd_048_accrual_gap_63):
    return _base_universe_d3(rvd_base_universe_d2_017_rvd_048_accrual_gap_63, 17)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_017_rvd_048_accrual_gap_63'] = {'inputs': ['rvd_base_universe_d2_017_rvd_048_accrual_gap_63'], 'func': rvd_base_universe_d3_017_rvd_048_accrual_gap_63}


def rvd_base_universe_d3_018_rvd_051_fcf_burn_to_cash_189(rvd_base_universe_d2_018_rvd_051_fcf_burn_to_cash_189):
    return _base_universe_d3(rvd_base_universe_d2_018_rvd_051_fcf_burn_to_cash_189, 18)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_018_rvd_051_fcf_burn_to_cash_189'] = {'inputs': ['rvd_base_universe_d2_018_rvd_051_fcf_burn_to_cash_189'], 'func': rvd_base_universe_d3_018_rvd_051_fcf_burn_to_cash_189}


def rvd_base_universe_d3_019_rvd_052_debt_to_equity_252(rvd_base_universe_d2_019_rvd_052_debt_to_equity_252):
    return _base_universe_d3(rvd_base_universe_d2_019_rvd_052_debt_to_equity_252, 19)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_019_rvd_052_debt_to_equity_252'] = {'inputs': ['rvd_base_universe_d2_019_rvd_052_debt_to_equity_252'], 'func': rvd_base_universe_d3_019_rvd_052_debt_to_equity_252}


def rvd_base_universe_d3_020_rvd_053_debt_to_assets_378(rvd_base_universe_d2_020_rvd_053_debt_to_assets_378):
    return _base_universe_d3(rvd_base_universe_d2_020_rvd_053_debt_to_assets_378, 20)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_020_rvd_053_debt_to_assets_378'] = {'inputs': ['rvd_base_universe_d2_020_rvd_053_debt_to_assets_378'], 'func': rvd_base_universe_d3_020_rvd_053_debt_to_assets_378}


def rvd_base_universe_d3_021_rvd_055_interest_coverage_stress_756(rvd_base_universe_d2_021_rvd_055_interest_coverage_stress_756):
    return _base_universe_d3(rvd_base_universe_d2_021_rvd_055_interest_coverage_stress_756, 21)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_021_rvd_055_interest_coverage_stress_756'] = {'inputs': ['rvd_base_universe_d2_021_rvd_055_interest_coverage_stress_756'], 'func': rvd_base_universe_d3_021_rvd_055_interest_coverage_stress_756}


def rvd_base_universe_d3_022_rvd_060_accrual_gap_252(rvd_base_universe_d2_022_rvd_060_accrual_gap_252):
    return _base_universe_d3(rvd_base_universe_d2_022_rvd_060_accrual_gap_252, 22)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_022_rvd_060_accrual_gap_252'] = {'inputs': ['rvd_base_universe_d2_022_rvd_060_accrual_gap_252'], 'func': rvd_base_universe_d3_022_rvd_060_accrual_gap_252}


def rvd_base_universe_d3_023_rvd_basefill_001(rvd_base_universe_d2_023_rvd_basefill_001):
    return _base_universe_d3(rvd_base_universe_d2_023_rvd_basefill_001, 23)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_023_rvd_basefill_001'] = {'inputs': ['rvd_base_universe_d2_023_rvd_basefill_001'], 'func': rvd_base_universe_d3_023_rvd_basefill_001}


def rvd_base_universe_d3_024_rvd_basefill_002(rvd_base_universe_d2_024_rvd_basefill_002):
    return _base_universe_d3(rvd_base_universe_d2_024_rvd_basefill_002, 24)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_024_rvd_basefill_002'] = {'inputs': ['rvd_base_universe_d2_024_rvd_basefill_002'], 'func': rvd_base_universe_d3_024_rvd_basefill_002}


def rvd_base_universe_d3_025_rvd_basefill_006(rvd_base_universe_d2_025_rvd_basefill_006):
    return _base_universe_d3(rvd_base_universe_d2_025_rvd_basefill_006, 25)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_025_rvd_basefill_006'] = {'inputs': ['rvd_base_universe_d2_025_rvd_basefill_006'], 'func': rvd_base_universe_d3_025_rvd_basefill_006}


def rvd_base_universe_d3_026_rvd_basefill_008(rvd_base_universe_d2_026_rvd_basefill_008):
    return _base_universe_d3(rvd_base_universe_d2_026_rvd_basefill_008, 26)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_026_rvd_basefill_008'] = {'inputs': ['rvd_base_universe_d2_026_rvd_basefill_008'], 'func': rvd_base_universe_d3_026_rvd_basefill_008}


def rvd_base_universe_d3_027_rvd_basefill_009(rvd_base_universe_d2_027_rvd_basefill_009):
    return _base_universe_d3(rvd_base_universe_d2_027_rvd_basefill_009, 27)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_027_rvd_basefill_009'] = {'inputs': ['rvd_base_universe_d2_027_rvd_basefill_009'], 'func': rvd_base_universe_d3_027_rvd_basefill_009}


def rvd_base_universe_d3_028_rvd_basefill_010(rvd_base_universe_d2_028_rvd_basefill_010):
    return _base_universe_d3(rvd_base_universe_d2_028_rvd_basefill_010, 28)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_028_rvd_basefill_010'] = {'inputs': ['rvd_base_universe_d2_028_rvd_basefill_010'], 'func': rvd_base_universe_d3_028_rvd_basefill_010}


def rvd_base_universe_d3_029_rvd_basefill_011(rvd_base_universe_d2_029_rvd_basefill_011):
    return _base_universe_d3(rvd_base_universe_d2_029_rvd_basefill_011, 29)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_029_rvd_basefill_011'] = {'inputs': ['rvd_base_universe_d2_029_rvd_basefill_011'], 'func': rvd_base_universe_d3_029_rvd_basefill_011}


def rvd_base_universe_d3_030_rvd_basefill_013(rvd_base_universe_d2_030_rvd_basefill_013):
    return _base_universe_d3(rvd_base_universe_d2_030_rvd_basefill_013, 30)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_030_rvd_basefill_013'] = {'inputs': ['rvd_base_universe_d2_030_rvd_basefill_013'], 'func': rvd_base_universe_d3_030_rvd_basefill_013}


def rvd_base_universe_d3_031_rvd_basefill_014(rvd_base_universe_d2_031_rvd_basefill_014):
    return _base_universe_d3(rvd_base_universe_d2_031_rvd_basefill_014, 31)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_031_rvd_basefill_014'] = {'inputs': ['rvd_base_universe_d2_031_rvd_basefill_014'], 'func': rvd_base_universe_d3_031_rvd_basefill_014}


def rvd_base_universe_d3_032_rvd_basefill_015(rvd_base_universe_d2_032_rvd_basefill_015):
    return _base_universe_d3(rvd_base_universe_d2_032_rvd_basefill_015, 32)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_032_rvd_basefill_015'] = {'inputs': ['rvd_base_universe_d2_032_rvd_basefill_015'], 'func': rvd_base_universe_d3_032_rvd_basefill_015}


def rvd_base_universe_d3_033_rvd_basefill_018(rvd_base_universe_d2_033_rvd_basefill_018):
    return _base_universe_d3(rvd_base_universe_d2_033_rvd_basefill_018, 33)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_033_rvd_basefill_018'] = {'inputs': ['rvd_base_universe_d2_033_rvd_basefill_018'], 'func': rvd_base_universe_d3_033_rvd_basefill_018}


def rvd_base_universe_d3_034_rvd_basefill_020(rvd_base_universe_d2_034_rvd_basefill_020):
    return _base_universe_d3(rvd_base_universe_d2_034_rvd_basefill_020, 34)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_034_rvd_basefill_020'] = {'inputs': ['rvd_base_universe_d2_034_rvd_basefill_020'], 'func': rvd_base_universe_d3_034_rvd_basefill_020}


def rvd_base_universe_d3_035_rvd_basefill_021(rvd_base_universe_d2_035_rvd_basefill_021):
    return _base_universe_d3(rvd_base_universe_d2_035_rvd_basefill_021, 35)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_035_rvd_basefill_021'] = {'inputs': ['rvd_base_universe_d2_035_rvd_basefill_021'], 'func': rvd_base_universe_d3_035_rvd_basefill_021}


def rvd_base_universe_d3_036_rvd_basefill_022(rvd_base_universe_d2_036_rvd_basefill_022):
    return _base_universe_d3(rvd_base_universe_d2_036_rvd_basefill_022, 36)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_036_rvd_basefill_022'] = {'inputs': ['rvd_base_universe_d2_036_rvd_basefill_022'], 'func': rvd_base_universe_d3_036_rvd_basefill_022}


def rvd_base_universe_d3_037_rvd_basefill_023(rvd_base_universe_d2_037_rvd_basefill_023):
    return _base_universe_d3(rvd_base_universe_d2_037_rvd_basefill_023, 37)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_037_rvd_basefill_023'] = {'inputs': ['rvd_base_universe_d2_037_rvd_basefill_023'], 'func': rvd_base_universe_d3_037_rvd_basefill_023}


def rvd_base_universe_d3_038_rvd_basefill_025(rvd_base_universe_d2_038_rvd_basefill_025):
    return _base_universe_d3(rvd_base_universe_d2_038_rvd_basefill_025, 38)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_038_rvd_basefill_025'] = {'inputs': ['rvd_base_universe_d2_038_rvd_basefill_025'], 'func': rvd_base_universe_d3_038_rvd_basefill_025}


def rvd_base_universe_d3_039_rvd_basefill_026(rvd_base_universe_d2_039_rvd_basefill_026):
    return _base_universe_d3(rvd_base_universe_d2_039_rvd_basefill_026, 39)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_039_rvd_basefill_026'] = {'inputs': ['rvd_base_universe_d2_039_rvd_basefill_026'], 'func': rvd_base_universe_d3_039_rvd_basefill_026}


def rvd_base_universe_d3_040_rvd_basefill_030(rvd_base_universe_d2_040_rvd_basefill_030):
    return _base_universe_d3(rvd_base_universe_d2_040_rvd_basefill_030, 40)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_040_rvd_basefill_030'] = {'inputs': ['rvd_base_universe_d2_040_rvd_basefill_030'], 'func': rvd_base_universe_d3_040_rvd_basefill_030}


def rvd_base_universe_d3_041_rvd_basefill_032(rvd_base_universe_d2_041_rvd_basefill_032):
    return _base_universe_d3(rvd_base_universe_d2_041_rvd_basefill_032, 41)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_041_rvd_basefill_032'] = {'inputs': ['rvd_base_universe_d2_041_rvd_basefill_032'], 'func': rvd_base_universe_d3_041_rvd_basefill_032}


def rvd_base_universe_d3_042_rvd_basefill_033(rvd_base_universe_d2_042_rvd_basefill_033):
    return _base_universe_d3(rvd_base_universe_d2_042_rvd_basefill_033, 42)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_042_rvd_basefill_033'] = {'inputs': ['rvd_base_universe_d2_042_rvd_basefill_033'], 'func': rvd_base_universe_d3_042_rvd_basefill_033}


def rvd_base_universe_d3_043_rvd_basefill_034(rvd_base_universe_d2_043_rvd_basefill_034):
    return _base_universe_d3(rvd_base_universe_d2_043_rvd_basefill_034, 43)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_043_rvd_basefill_034'] = {'inputs': ['rvd_base_universe_d2_043_rvd_basefill_034'], 'func': rvd_base_universe_d3_043_rvd_basefill_034}


def rvd_base_universe_d3_044_rvd_basefill_035(rvd_base_universe_d2_044_rvd_basefill_035):
    return _base_universe_d3(rvd_base_universe_d2_044_rvd_basefill_035, 44)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_044_rvd_basefill_035'] = {'inputs': ['rvd_base_universe_d2_044_rvd_basefill_035'], 'func': rvd_base_universe_d3_044_rvd_basefill_035}


def rvd_base_universe_d3_045_rvd_basefill_037(rvd_base_universe_d2_045_rvd_basefill_037):
    return _base_universe_d3(rvd_base_universe_d2_045_rvd_basefill_037, 45)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_045_rvd_basefill_037'] = {'inputs': ['rvd_base_universe_d2_045_rvd_basefill_037'], 'func': rvd_base_universe_d3_045_rvd_basefill_037}


def rvd_base_universe_d3_046_rvd_basefill_038(rvd_base_universe_d2_046_rvd_basefill_038):
    return _base_universe_d3(rvd_base_universe_d2_046_rvd_basefill_038, 46)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_046_rvd_basefill_038'] = {'inputs': ['rvd_base_universe_d2_046_rvd_basefill_038'], 'func': rvd_base_universe_d3_046_rvd_basefill_038}


def rvd_base_universe_d3_047_rvd_basefill_042(rvd_base_universe_d2_047_rvd_basefill_042):
    return _base_universe_d3(rvd_base_universe_d2_047_rvd_basefill_042, 47)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_047_rvd_basefill_042'] = {'inputs': ['rvd_base_universe_d2_047_rvd_basefill_042'], 'func': rvd_base_universe_d3_047_rvd_basefill_042}


def rvd_base_universe_d3_048_rvd_basefill_044(rvd_base_universe_d2_048_rvd_basefill_044):
    return _base_universe_d3(rvd_base_universe_d2_048_rvd_basefill_044, 48)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_048_rvd_basefill_044'] = {'inputs': ['rvd_base_universe_d2_048_rvd_basefill_044'], 'func': rvd_base_universe_d3_048_rvd_basefill_044}


def rvd_base_universe_d3_049_rvd_basefill_045(rvd_base_universe_d2_049_rvd_basefill_045):
    return _base_universe_d3(rvd_base_universe_d2_049_rvd_basefill_045, 49)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_049_rvd_basefill_045'] = {'inputs': ['rvd_base_universe_d2_049_rvd_basefill_045'], 'func': rvd_base_universe_d3_049_rvd_basefill_045}


def rvd_base_universe_d3_050_rvd_basefill_046(rvd_base_universe_d2_050_rvd_basefill_046):
    return _base_universe_d3(rvd_base_universe_d2_050_rvd_basefill_046, 50)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_050_rvd_basefill_046'] = {'inputs': ['rvd_base_universe_d2_050_rvd_basefill_046'], 'func': rvd_base_universe_d3_050_rvd_basefill_046}


def rvd_base_universe_d3_051_rvd_basefill_047(rvd_base_universe_d2_051_rvd_basefill_047):
    return _base_universe_d3(rvd_base_universe_d2_051_rvd_basefill_047, 51)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_051_rvd_basefill_047'] = {'inputs': ['rvd_base_universe_d2_051_rvd_basefill_047'], 'func': rvd_base_universe_d3_051_rvd_basefill_047}


def rvd_base_universe_d3_052_rvd_basefill_049(rvd_base_universe_d2_052_rvd_basefill_049):
    return _base_universe_d3(rvd_base_universe_d2_052_rvd_basefill_049, 52)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_052_rvd_basefill_049'] = {'inputs': ['rvd_base_universe_d2_052_rvd_basefill_049'], 'func': rvd_base_universe_d3_052_rvd_basefill_049}


def rvd_base_universe_d3_053_rvd_basefill_050(rvd_base_universe_d2_053_rvd_basefill_050):
    return _base_universe_d3(rvd_base_universe_d2_053_rvd_basefill_050, 53)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_053_rvd_basefill_050'] = {'inputs': ['rvd_base_universe_d2_053_rvd_basefill_050'], 'func': rvd_base_universe_d3_053_rvd_basefill_050}


def rvd_base_universe_d3_054_rvd_basefill_054(rvd_base_universe_d2_054_rvd_basefill_054):
    return _base_universe_d3(rvd_base_universe_d2_054_rvd_basefill_054, 54)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_054_rvd_basefill_054'] = {'inputs': ['rvd_base_universe_d2_054_rvd_basefill_054'], 'func': rvd_base_universe_d3_054_rvd_basefill_054}


def rvd_base_universe_d3_055_rvd_basefill_056(rvd_base_universe_d2_055_rvd_basefill_056):
    return _base_universe_d3(rvd_base_universe_d2_055_rvd_basefill_056, 55)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_055_rvd_basefill_056'] = {'inputs': ['rvd_base_universe_d2_055_rvd_basefill_056'], 'func': rvd_base_universe_d3_055_rvd_basefill_056}


def rvd_base_universe_d3_056_rvd_basefill_057(rvd_base_universe_d2_056_rvd_basefill_057):
    return _base_universe_d3(rvd_base_universe_d2_056_rvd_basefill_057, 56)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_056_rvd_basefill_057'] = {'inputs': ['rvd_base_universe_d2_056_rvd_basefill_057'], 'func': rvd_base_universe_d3_056_rvd_basefill_057}


def rvd_base_universe_d3_057_rvd_basefill_058(rvd_base_universe_d2_057_rvd_basefill_058):
    return _base_universe_d3(rvd_base_universe_d2_057_rvd_basefill_058, 57)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_057_rvd_basefill_058'] = {'inputs': ['rvd_base_universe_d2_057_rvd_basefill_058'], 'func': rvd_base_universe_d3_057_rvd_basefill_058}


def rvd_base_universe_d3_058_rvd_basefill_059(rvd_base_universe_d2_058_rvd_basefill_059):
    return _base_universe_d3(rvd_base_universe_d2_058_rvd_basefill_059, 58)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_058_rvd_basefill_059'] = {'inputs': ['rvd_base_universe_d2_058_rvd_basefill_059'], 'func': rvd_base_universe_d3_058_rvd_basefill_059}


def rvd_base_universe_d3_059_rvd_basefill_061(rvd_base_universe_d2_059_rvd_basefill_061):
    return _base_universe_d3(rvd_base_universe_d2_059_rvd_basefill_061, 59)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_059_rvd_basefill_061'] = {'inputs': ['rvd_base_universe_d2_059_rvd_basefill_061'], 'func': rvd_base_universe_d3_059_rvd_basefill_061}


def rvd_base_universe_d3_060_rvd_basefill_062(rvd_base_universe_d2_060_rvd_basefill_062):
    return _base_universe_d3(rvd_base_universe_d2_060_rvd_basefill_062, 60)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_060_rvd_basefill_062'] = {'inputs': ['rvd_base_universe_d2_060_rvd_basefill_062'], 'func': rvd_base_universe_d3_060_rvd_basefill_062}


def rvd_base_universe_d3_061_rvd_basefill_063(rvd_base_universe_d2_061_rvd_basefill_063):
    return _base_universe_d3(rvd_base_universe_d2_061_rvd_basefill_063, 61)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_061_rvd_basefill_063'] = {'inputs': ['rvd_base_universe_d2_061_rvd_basefill_063'], 'func': rvd_base_universe_d3_061_rvd_basefill_063}


def rvd_base_universe_d3_062_rvd_basefill_064(rvd_base_universe_d2_062_rvd_basefill_064):
    return _base_universe_d3(rvd_base_universe_d2_062_rvd_basefill_064, 62)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_062_rvd_basefill_064'] = {'inputs': ['rvd_base_universe_d2_062_rvd_basefill_064'], 'func': rvd_base_universe_d3_062_rvd_basefill_064}


def rvd_base_universe_d3_063_rvd_basefill_065(rvd_base_universe_d2_063_rvd_basefill_065):
    return _base_universe_d3(rvd_base_universe_d2_063_rvd_basefill_065, 63)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_063_rvd_basefill_065'] = {'inputs': ['rvd_base_universe_d2_063_rvd_basefill_065'], 'func': rvd_base_universe_d3_063_rvd_basefill_065}


def rvd_base_universe_d3_064_rvd_basefill_066(rvd_base_universe_d2_064_rvd_basefill_066):
    return _base_universe_d3(rvd_base_universe_d2_064_rvd_basefill_066, 64)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_064_rvd_basefill_066'] = {'inputs': ['rvd_base_universe_d2_064_rvd_basefill_066'], 'func': rvd_base_universe_d3_064_rvd_basefill_066}


def rvd_base_universe_d3_065_rvd_basefill_067(rvd_base_universe_d2_065_rvd_basefill_067):
    return _base_universe_d3(rvd_base_universe_d2_065_rvd_basefill_067, 65)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_065_rvd_basefill_067'] = {'inputs': ['rvd_base_universe_d2_065_rvd_basefill_067'], 'func': rvd_base_universe_d3_065_rvd_basefill_067}


def rvd_base_universe_d3_066_rvd_basefill_068(rvd_base_universe_d2_066_rvd_basefill_068):
    return _base_universe_d3(rvd_base_universe_d2_066_rvd_basefill_068, 66)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_066_rvd_basefill_068'] = {'inputs': ['rvd_base_universe_d2_066_rvd_basefill_068'], 'func': rvd_base_universe_d3_066_rvd_basefill_068}


def rvd_base_universe_d3_067_rvd_basefill_069(rvd_base_universe_d2_067_rvd_basefill_069):
    return _base_universe_d3(rvd_base_universe_d2_067_rvd_basefill_069, 67)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_067_rvd_basefill_069'] = {'inputs': ['rvd_base_universe_d2_067_rvd_basefill_069'], 'func': rvd_base_universe_d3_067_rvd_basefill_069}


def rvd_base_universe_d3_068_rvd_basefill_070(rvd_base_universe_d2_068_rvd_basefill_070):
    return _base_universe_d3(rvd_base_universe_d2_068_rvd_basefill_070, 68)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_068_rvd_basefill_070'] = {'inputs': ['rvd_base_universe_d2_068_rvd_basefill_070'], 'func': rvd_base_universe_d3_068_rvd_basefill_070}


def rvd_base_universe_d3_069_rvd_basefill_071(rvd_base_universe_d2_069_rvd_basefill_071):
    return _base_universe_d3(rvd_base_universe_d2_069_rvd_basefill_071, 69)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_069_rvd_basefill_071'] = {'inputs': ['rvd_base_universe_d2_069_rvd_basefill_071'], 'func': rvd_base_universe_d3_069_rvd_basefill_071}


def rvd_base_universe_d3_070_rvd_basefill_072(rvd_base_universe_d2_070_rvd_basefill_072):
    return _base_universe_d3(rvd_base_universe_d2_070_rvd_basefill_072, 70)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_070_rvd_basefill_072'] = {'inputs': ['rvd_base_universe_d2_070_rvd_basefill_072'], 'func': rvd_base_universe_d3_070_rvd_basefill_072}


def rvd_base_universe_d3_071_rvd_basefill_073(rvd_base_universe_d2_071_rvd_basefill_073):
    return _base_universe_d3(rvd_base_universe_d2_071_rvd_basefill_073, 71)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_071_rvd_basefill_073'] = {'inputs': ['rvd_base_universe_d2_071_rvd_basefill_073'], 'func': rvd_base_universe_d3_071_rvd_basefill_073}


def rvd_base_universe_d3_072_rvd_basefill_074(rvd_base_universe_d2_072_rvd_basefill_074):
    return _base_universe_d3(rvd_base_universe_d2_072_rvd_basefill_074, 72)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_072_rvd_basefill_074'] = {'inputs': ['rvd_base_universe_d2_072_rvd_basefill_074'], 'func': rvd_base_universe_d3_072_rvd_basefill_074}


def rvd_base_universe_d3_073_rvd_basefill_075(rvd_base_universe_d2_073_rvd_basefill_075):
    return _base_universe_d3(rvd_base_universe_d2_073_rvd_basefill_075, 73)
RVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rvd_base_universe_d3_073_rvd_basefill_075'] = {'inputs': ['rvd_base_universe_d2_073_rvd_basefill_075'], 'func': rvd_base_universe_d3_073_rvd_basefill_075}
