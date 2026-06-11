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



def fmo_176_fmo_001_netinc_decline_1_accel_1(fmo_151_fmo_001_netinc_decline_1_roc_1):
    feature = _s(fmo_151_fmo_001_netinc_decline_1_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def fmo_177_fmo_007_interest_coverage_stress_252_accel_42(fmo_152_fmo_007_interest_coverage_stress_252_roc_42):
    feature = _s(fmo_152_fmo_007_interest_coverage_stress_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def fmo_178_fmo_013_netinc_decline_1_accel_126(fmo_153_fmo_013_netinc_decline_1_roc_126):
    feature = _s(fmo_153_fmo_013_netinc_decline_1_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def fmo_179_fmo_019_interest_coverage_stress_84_accel_378(fmo_154_fmo_019_interest_coverage_stress_84_roc_378):
    feature = _s(fmo_154_fmo_019_interest_coverage_stress_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def fmo_180_fmo_025_netinc_decline_1_accel_4(fmo_155_fmo_025_netinc_decline_1_roc_4):
    feature = _s(fmo_155_fmo_025_netinc_decline_1_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















FUNDAMENTAL_MOMENTUM_REGISTRY_3RD_DERIVATIVES = {
    'fmo_176_fmo_001_netinc_decline_1_accel_1': {'inputs': ['fmo_151_fmo_001_netinc_decline_1_roc_1'], 'func': fmo_176_fmo_001_netinc_decline_1_accel_1},
    'fmo_177_fmo_007_interest_coverage_stress_252_accel_42': {'inputs': ['fmo_152_fmo_007_interest_coverage_stress_252_roc_42'], 'func': fmo_177_fmo_007_interest_coverage_stress_252_accel_42},
    'fmo_178_fmo_013_netinc_decline_1_accel_126': {'inputs': ['fmo_153_fmo_013_netinc_decline_1_roc_126'], 'func': fmo_178_fmo_013_netinc_decline_1_accel_126},
    'fmo_179_fmo_019_interest_coverage_stress_84_accel_378': {'inputs': ['fmo_154_fmo_019_interest_coverage_stress_84_roc_378'], 'func': fmo_179_fmo_019_interest_coverage_stress_84_accel_378},
    'fmo_180_fmo_025_netinc_decline_1_accel_4': {'inputs': ['fmo_155_fmo_025_netinc_decline_1_roc_4'], 'func': fmo_180_fmo_025_netinc_decline_1_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def fm_replacement_d3_001(fm_replacement_d2_001):
    feature = _clean(fm_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_001'] = {'inputs': ['fm_replacement_d2_001'], 'func': fm_replacement_d3_001}


def fm_replacement_d3_002(fm_replacement_d2_002):
    feature = _clean(fm_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_002'] = {'inputs': ['fm_replacement_d2_002'], 'func': fm_replacement_d3_002}


def fm_replacement_d3_003(fm_replacement_d2_003):
    feature = _clean(fm_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_003'] = {'inputs': ['fm_replacement_d2_003'], 'func': fm_replacement_d3_003}


def fm_replacement_d3_004(fm_replacement_d2_004):
    feature = _clean(fm_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_004'] = {'inputs': ['fm_replacement_d2_004'], 'func': fm_replacement_d3_004}


def fm_replacement_d3_005(fm_replacement_d2_005):
    feature = _clean(fm_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_005'] = {'inputs': ['fm_replacement_d2_005'], 'func': fm_replacement_d3_005}


def fm_replacement_d3_006(fm_replacement_d2_006):
    feature = _clean(fm_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_006'] = {'inputs': ['fm_replacement_d2_006'], 'func': fm_replacement_d3_006}


def fm_replacement_d3_007(fm_replacement_d2_007):
    feature = _clean(fm_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_007'] = {'inputs': ['fm_replacement_d2_007'], 'func': fm_replacement_d3_007}


def fm_replacement_d3_008(fm_replacement_d2_008):
    feature = _clean(fm_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_008'] = {'inputs': ['fm_replacement_d2_008'], 'func': fm_replacement_d3_008}


def fm_replacement_d3_009(fm_replacement_d2_009):
    feature = _clean(fm_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_009'] = {'inputs': ['fm_replacement_d2_009'], 'func': fm_replacement_d3_009}


def fm_replacement_d3_010(fm_replacement_d2_010):
    feature = _clean(fm_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_010'] = {'inputs': ['fm_replacement_d2_010'], 'func': fm_replacement_d3_010}


def fm_replacement_d3_011(fm_replacement_d2_011):
    feature = _clean(fm_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_011'] = {'inputs': ['fm_replacement_d2_011'], 'func': fm_replacement_d3_011}


def fm_replacement_d3_012(fm_replacement_d2_012):
    feature = _clean(fm_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_012'] = {'inputs': ['fm_replacement_d2_012'], 'func': fm_replacement_d3_012}


def fm_replacement_d3_013(fm_replacement_d2_013):
    feature = _clean(fm_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_013'] = {'inputs': ['fm_replacement_d2_013'], 'func': fm_replacement_d3_013}


def fm_replacement_d3_014(fm_replacement_d2_014):
    feature = _clean(fm_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_014'] = {'inputs': ['fm_replacement_d2_014'], 'func': fm_replacement_d3_014}


def fm_replacement_d3_015(fm_replacement_d2_015):
    feature = _clean(fm_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_015'] = {'inputs': ['fm_replacement_d2_015'], 'func': fm_replacement_d3_015}


def fm_replacement_d3_016(fm_replacement_d2_016):
    feature = _clean(fm_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_016'] = {'inputs': ['fm_replacement_d2_016'], 'func': fm_replacement_d3_016}


def fm_replacement_d3_017(fm_replacement_d2_017):
    feature = _clean(fm_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_017'] = {'inputs': ['fm_replacement_d2_017'], 'func': fm_replacement_d3_017}


def fm_replacement_d3_018(fm_replacement_d2_018):
    feature = _clean(fm_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_018'] = {'inputs': ['fm_replacement_d2_018'], 'func': fm_replacement_d3_018}


def fm_replacement_d3_019(fm_replacement_d2_019):
    feature = _clean(fm_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_019'] = {'inputs': ['fm_replacement_d2_019'], 'func': fm_replacement_d3_019}


def fm_replacement_d3_020(fm_replacement_d2_020):
    feature = _clean(fm_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_020'] = {'inputs': ['fm_replacement_d2_020'], 'func': fm_replacement_d3_020}


def fm_replacement_d3_021(fm_replacement_d2_021):
    feature = _clean(fm_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_021'] = {'inputs': ['fm_replacement_d2_021'], 'func': fm_replacement_d3_021}


def fm_replacement_d3_022(fm_replacement_d2_022):
    feature = _clean(fm_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_022'] = {'inputs': ['fm_replacement_d2_022'], 'func': fm_replacement_d3_022}


def fm_replacement_d3_023(fm_replacement_d2_023):
    feature = _clean(fm_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_023'] = {'inputs': ['fm_replacement_d2_023'], 'func': fm_replacement_d3_023}


def fm_replacement_d3_024(fm_replacement_d2_024):
    feature = _clean(fm_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_024'] = {'inputs': ['fm_replacement_d2_024'], 'func': fm_replacement_d3_024}


def fm_replacement_d3_025(fm_replacement_d2_025):
    feature = _clean(fm_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_025'] = {'inputs': ['fm_replacement_d2_025'], 'func': fm_replacement_d3_025}


def fm_replacement_d3_026(fm_replacement_d2_026):
    feature = _clean(fm_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_026'] = {'inputs': ['fm_replacement_d2_026'], 'func': fm_replacement_d3_026}


def fm_replacement_d3_027(fm_replacement_d2_027):
    feature = _clean(fm_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_027'] = {'inputs': ['fm_replacement_d2_027'], 'func': fm_replacement_d3_027}


def fm_replacement_d3_028(fm_replacement_d2_028):
    feature = _clean(fm_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_028'] = {'inputs': ['fm_replacement_d2_028'], 'func': fm_replacement_d3_028}


def fm_replacement_d3_029(fm_replacement_d2_029):
    feature = _clean(fm_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_029'] = {'inputs': ['fm_replacement_d2_029'], 'func': fm_replacement_d3_029}


def fm_replacement_d3_030(fm_replacement_d2_030):
    feature = _clean(fm_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_030'] = {'inputs': ['fm_replacement_d2_030'], 'func': fm_replacement_d3_030}


def fm_replacement_d3_031(fm_replacement_d2_031):
    feature = _clean(fm_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_031'] = {'inputs': ['fm_replacement_d2_031'], 'func': fm_replacement_d3_031}


def fm_replacement_d3_032(fm_replacement_d2_032):
    feature = _clean(fm_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_032'] = {'inputs': ['fm_replacement_d2_032'], 'func': fm_replacement_d3_032}


def fm_replacement_d3_033(fm_replacement_d2_033):
    feature = _clean(fm_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_033'] = {'inputs': ['fm_replacement_d2_033'], 'func': fm_replacement_d3_033}


def fm_replacement_d3_034(fm_replacement_d2_034):
    feature = _clean(fm_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_034'] = {'inputs': ['fm_replacement_d2_034'], 'func': fm_replacement_d3_034}


def fm_replacement_d3_035(fm_replacement_d2_035):
    feature = _clean(fm_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_035'] = {'inputs': ['fm_replacement_d2_035'], 'func': fm_replacement_d3_035}


def fm_replacement_d3_036(fm_replacement_d2_036):
    feature = _clean(fm_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_036'] = {'inputs': ['fm_replacement_d2_036'], 'func': fm_replacement_d3_036}


def fm_replacement_d3_037(fm_replacement_d2_037):
    feature = _clean(fm_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_037'] = {'inputs': ['fm_replacement_d2_037'], 'func': fm_replacement_d3_037}


def fm_replacement_d3_038(fm_replacement_d2_038):
    feature = _clean(fm_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_038'] = {'inputs': ['fm_replacement_d2_038'], 'func': fm_replacement_d3_038}


def fm_replacement_d3_039(fm_replacement_d2_039):
    feature = _clean(fm_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_039'] = {'inputs': ['fm_replacement_d2_039'], 'func': fm_replacement_d3_039}


def fm_replacement_d3_040(fm_replacement_d2_040):
    feature = _clean(fm_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_040'] = {'inputs': ['fm_replacement_d2_040'], 'func': fm_replacement_d3_040}


def fm_replacement_d3_041(fm_replacement_d2_041):
    feature = _clean(fm_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_041'] = {'inputs': ['fm_replacement_d2_041'], 'func': fm_replacement_d3_041}


def fm_replacement_d3_042(fm_replacement_d2_042):
    feature = _clean(fm_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_042'] = {'inputs': ['fm_replacement_d2_042'], 'func': fm_replacement_d3_042}


def fm_replacement_d3_043(fm_replacement_d2_043):
    feature = _clean(fm_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_043'] = {'inputs': ['fm_replacement_d2_043'], 'func': fm_replacement_d3_043}


def fm_replacement_d3_044(fm_replacement_d2_044):
    feature = _clean(fm_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_044'] = {'inputs': ['fm_replacement_d2_044'], 'func': fm_replacement_d3_044}


def fm_replacement_d3_045(fm_replacement_d2_045):
    feature = _clean(fm_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_045'] = {'inputs': ['fm_replacement_d2_045'], 'func': fm_replacement_d3_045}


def fm_replacement_d3_046(fm_replacement_d2_046):
    feature = _clean(fm_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_046'] = {'inputs': ['fm_replacement_d2_046'], 'func': fm_replacement_d3_046}


def fm_replacement_d3_047(fm_replacement_d2_047):
    feature = _clean(fm_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_047'] = {'inputs': ['fm_replacement_d2_047'], 'func': fm_replacement_d3_047}


def fm_replacement_d3_048(fm_replacement_d2_048):
    feature = _clean(fm_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_048'] = {'inputs': ['fm_replacement_d2_048'], 'func': fm_replacement_d3_048}


def fm_replacement_d3_049(fm_replacement_d2_049):
    feature = _clean(fm_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_049'] = {'inputs': ['fm_replacement_d2_049'], 'func': fm_replacement_d3_049}


def fm_replacement_d3_050(fm_replacement_d2_050):
    feature = _clean(fm_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_050'] = {'inputs': ['fm_replacement_d2_050'], 'func': fm_replacement_d3_050}


def fm_replacement_d3_051(fm_replacement_d2_051):
    feature = _clean(fm_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_051'] = {'inputs': ['fm_replacement_d2_051'], 'func': fm_replacement_d3_051}


def fm_replacement_d3_052(fm_replacement_d2_052):
    feature = _clean(fm_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_052'] = {'inputs': ['fm_replacement_d2_052'], 'func': fm_replacement_d3_052}


def fm_replacement_d3_053(fm_replacement_d2_053):
    feature = _clean(fm_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_053'] = {'inputs': ['fm_replacement_d2_053'], 'func': fm_replacement_d3_053}


def fm_replacement_d3_054(fm_replacement_d2_054):
    feature = _clean(fm_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_054'] = {'inputs': ['fm_replacement_d2_054'], 'func': fm_replacement_d3_054}


def fm_replacement_d3_055(fm_replacement_d2_055):
    feature = _clean(fm_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_055'] = {'inputs': ['fm_replacement_d2_055'], 'func': fm_replacement_d3_055}


def fm_replacement_d3_056(fm_replacement_d2_056):
    feature = _clean(fm_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_056'] = {'inputs': ['fm_replacement_d2_056'], 'func': fm_replacement_d3_056}


def fm_replacement_d3_057(fm_replacement_d2_057):
    feature = _clean(fm_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_057'] = {'inputs': ['fm_replacement_d2_057'], 'func': fm_replacement_d3_057}


def fm_replacement_d3_058(fm_replacement_d2_058):
    feature = _clean(fm_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_058'] = {'inputs': ['fm_replacement_d2_058'], 'func': fm_replacement_d3_058}


def fm_replacement_d3_059(fm_replacement_d2_059):
    feature = _clean(fm_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_059'] = {'inputs': ['fm_replacement_d2_059'], 'func': fm_replacement_d3_059}


def fm_replacement_d3_060(fm_replacement_d2_060):
    feature = _clean(fm_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_060'] = {'inputs': ['fm_replacement_d2_060'], 'func': fm_replacement_d3_060}


def fm_replacement_d3_061(fm_replacement_d2_061):
    feature = _clean(fm_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_061'] = {'inputs': ['fm_replacement_d2_061'], 'func': fm_replacement_d3_061}


def fm_replacement_d3_062(fm_replacement_d2_062):
    feature = _clean(fm_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_062'] = {'inputs': ['fm_replacement_d2_062'], 'func': fm_replacement_d3_062}


def fm_replacement_d3_063(fm_replacement_d2_063):
    feature = _clean(fm_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_063'] = {'inputs': ['fm_replacement_d2_063'], 'func': fm_replacement_d3_063}


def fm_replacement_d3_064(fm_replacement_d2_064):
    feature = _clean(fm_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_064'] = {'inputs': ['fm_replacement_d2_064'], 'func': fm_replacement_d3_064}


def fm_replacement_d3_065(fm_replacement_d2_065):
    feature = _clean(fm_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_065'] = {'inputs': ['fm_replacement_d2_065'], 'func': fm_replacement_d3_065}


def fm_replacement_d3_066(fm_replacement_d2_066):
    feature = _clean(fm_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_066'] = {'inputs': ['fm_replacement_d2_066'], 'func': fm_replacement_d3_066}


def fm_replacement_d3_067(fm_replacement_d2_067):
    feature = _clean(fm_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_067'] = {'inputs': ['fm_replacement_d2_067'], 'func': fm_replacement_d3_067}


def fm_replacement_d3_068(fm_replacement_d2_068):
    feature = _clean(fm_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_068'] = {'inputs': ['fm_replacement_d2_068'], 'func': fm_replacement_d3_068}


def fm_replacement_d3_069(fm_replacement_d2_069):
    feature = _clean(fm_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_069'] = {'inputs': ['fm_replacement_d2_069'], 'func': fm_replacement_d3_069}


def fm_replacement_d3_070(fm_replacement_d2_070):
    feature = _clean(fm_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_070'] = {'inputs': ['fm_replacement_d2_070'], 'func': fm_replacement_d3_070}


def fm_replacement_d3_071(fm_replacement_d2_071):
    feature = _clean(fm_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_071'] = {'inputs': ['fm_replacement_d2_071'], 'func': fm_replacement_d3_071}


def fm_replacement_d3_072(fm_replacement_d2_072):
    feature = _clean(fm_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_072'] = {'inputs': ['fm_replacement_d2_072'], 'func': fm_replacement_d3_072}


def fm_replacement_d3_073(fm_replacement_d2_073):
    feature = _clean(fm_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_073'] = {'inputs': ['fm_replacement_d2_073'], 'func': fm_replacement_d3_073}


def fm_replacement_d3_074(fm_replacement_d2_074):
    feature = _clean(fm_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_074'] = {'inputs': ['fm_replacement_d2_074'], 'func': fm_replacement_d3_074}


def fm_replacement_d3_075(fm_replacement_d2_075):
    feature = _clean(fm_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_075'] = {'inputs': ['fm_replacement_d2_075'], 'func': fm_replacement_d3_075}


def fm_replacement_d3_076(fm_replacement_d2_076):
    feature = _clean(fm_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_076'] = {'inputs': ['fm_replacement_d2_076'], 'func': fm_replacement_d3_076}


def fm_replacement_d3_077(fm_replacement_d2_077):
    feature = _clean(fm_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_077'] = {'inputs': ['fm_replacement_d2_077'], 'func': fm_replacement_d3_077}


def fm_replacement_d3_078(fm_replacement_d2_078):
    feature = _clean(fm_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_078'] = {'inputs': ['fm_replacement_d2_078'], 'func': fm_replacement_d3_078}


def fm_replacement_d3_079(fm_replacement_d2_079):
    feature = _clean(fm_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_079'] = {'inputs': ['fm_replacement_d2_079'], 'func': fm_replacement_d3_079}


def fm_replacement_d3_080(fm_replacement_d2_080):
    feature = _clean(fm_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_080'] = {'inputs': ['fm_replacement_d2_080'], 'func': fm_replacement_d3_080}


def fm_replacement_d3_081(fm_replacement_d2_081):
    feature = _clean(fm_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_081'] = {'inputs': ['fm_replacement_d2_081'], 'func': fm_replacement_d3_081}


def fm_replacement_d3_082(fm_replacement_d2_082):
    feature = _clean(fm_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_082'] = {'inputs': ['fm_replacement_d2_082'], 'func': fm_replacement_d3_082}


def fm_replacement_d3_083(fm_replacement_d2_083):
    feature = _clean(fm_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_083'] = {'inputs': ['fm_replacement_d2_083'], 'func': fm_replacement_d3_083}


def fm_replacement_d3_084(fm_replacement_d2_084):
    feature = _clean(fm_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_084'] = {'inputs': ['fm_replacement_d2_084'], 'func': fm_replacement_d3_084}


def fm_replacement_d3_085(fm_replacement_d2_085):
    feature = _clean(fm_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_085'] = {'inputs': ['fm_replacement_d2_085'], 'func': fm_replacement_d3_085}


def fm_replacement_d3_086(fm_replacement_d2_086):
    feature = _clean(fm_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_086'] = {'inputs': ['fm_replacement_d2_086'], 'func': fm_replacement_d3_086}


def fm_replacement_d3_087(fm_replacement_d2_087):
    feature = _clean(fm_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_087'] = {'inputs': ['fm_replacement_d2_087'], 'func': fm_replacement_d3_087}


def fm_replacement_d3_088(fm_replacement_d2_088):
    feature = _clean(fm_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_088'] = {'inputs': ['fm_replacement_d2_088'], 'func': fm_replacement_d3_088}


def fm_replacement_d3_089(fm_replacement_d2_089):
    feature = _clean(fm_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_089'] = {'inputs': ['fm_replacement_d2_089'], 'func': fm_replacement_d3_089}


def fm_replacement_d3_090(fm_replacement_d2_090):
    feature = _clean(fm_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_090'] = {'inputs': ['fm_replacement_d2_090'], 'func': fm_replacement_d3_090}


def fm_replacement_d3_091(fm_replacement_d2_091):
    feature = _clean(fm_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_091'] = {'inputs': ['fm_replacement_d2_091'], 'func': fm_replacement_d3_091}


def fm_replacement_d3_092(fm_replacement_d2_092):
    feature = _clean(fm_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_092'] = {'inputs': ['fm_replacement_d2_092'], 'func': fm_replacement_d3_092}


def fm_replacement_d3_093(fm_replacement_d2_093):
    feature = _clean(fm_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_093'] = {'inputs': ['fm_replacement_d2_093'], 'func': fm_replacement_d3_093}


def fm_replacement_d3_094(fm_replacement_d2_094):
    feature = _clean(fm_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_094'] = {'inputs': ['fm_replacement_d2_094'], 'func': fm_replacement_d3_094}


def fm_replacement_d3_095(fm_replacement_d2_095):
    feature = _clean(fm_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_095'] = {'inputs': ['fm_replacement_d2_095'], 'func': fm_replacement_d3_095}


def fm_replacement_d3_096(fm_replacement_d2_096):
    feature = _clean(fm_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_096'] = {'inputs': ['fm_replacement_d2_096'], 'func': fm_replacement_d3_096}


def fm_replacement_d3_097(fm_replacement_d2_097):
    feature = _clean(fm_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_097'] = {'inputs': ['fm_replacement_d2_097'], 'func': fm_replacement_d3_097}


def fm_replacement_d3_098(fm_replacement_d2_098):
    feature = _clean(fm_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_098'] = {'inputs': ['fm_replacement_d2_098'], 'func': fm_replacement_d3_098}


def fm_replacement_d3_099(fm_replacement_d2_099):
    feature = _clean(fm_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_099'] = {'inputs': ['fm_replacement_d2_099'], 'func': fm_replacement_d3_099}


def fm_replacement_d3_100(fm_replacement_d2_100):
    feature = _clean(fm_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_100'] = {'inputs': ['fm_replacement_d2_100'], 'func': fm_replacement_d3_100}


def fm_replacement_d3_101(fm_replacement_d2_101):
    feature = _clean(fm_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_101'] = {'inputs': ['fm_replacement_d2_101'], 'func': fm_replacement_d3_101}


def fm_replacement_d3_102(fm_replacement_d2_102):
    feature = _clean(fm_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_102'] = {'inputs': ['fm_replacement_d2_102'], 'func': fm_replacement_d3_102}


def fm_replacement_d3_103(fm_replacement_d2_103):
    feature = _clean(fm_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_103'] = {'inputs': ['fm_replacement_d2_103'], 'func': fm_replacement_d3_103}


def fm_replacement_d3_104(fm_replacement_d2_104):
    feature = _clean(fm_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_104'] = {'inputs': ['fm_replacement_d2_104'], 'func': fm_replacement_d3_104}


def fm_replacement_d3_105(fm_replacement_d2_105):
    feature = _clean(fm_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_105'] = {'inputs': ['fm_replacement_d2_105'], 'func': fm_replacement_d3_105}


def fm_replacement_d3_106(fm_replacement_d2_106):
    feature = _clean(fm_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_106'] = {'inputs': ['fm_replacement_d2_106'], 'func': fm_replacement_d3_106}


def fm_replacement_d3_107(fm_replacement_d2_107):
    feature = _clean(fm_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_107'] = {'inputs': ['fm_replacement_d2_107'], 'func': fm_replacement_d3_107}


def fm_replacement_d3_108(fm_replacement_d2_108):
    feature = _clean(fm_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_108'] = {'inputs': ['fm_replacement_d2_108'], 'func': fm_replacement_d3_108}


def fm_replacement_d3_109(fm_replacement_d2_109):
    feature = _clean(fm_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_109'] = {'inputs': ['fm_replacement_d2_109'], 'func': fm_replacement_d3_109}


def fm_replacement_d3_110(fm_replacement_d2_110):
    feature = _clean(fm_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_110'] = {'inputs': ['fm_replacement_d2_110'], 'func': fm_replacement_d3_110}


def fm_replacement_d3_111(fm_replacement_d2_111):
    feature = _clean(fm_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_111'] = {'inputs': ['fm_replacement_d2_111'], 'func': fm_replacement_d3_111}


def fm_replacement_d3_112(fm_replacement_d2_112):
    feature = _clean(fm_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_112'] = {'inputs': ['fm_replacement_d2_112'], 'func': fm_replacement_d3_112}


def fm_replacement_d3_113(fm_replacement_d2_113):
    feature = _clean(fm_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_113'] = {'inputs': ['fm_replacement_d2_113'], 'func': fm_replacement_d3_113}


def fm_replacement_d3_114(fm_replacement_d2_114):
    feature = _clean(fm_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_114'] = {'inputs': ['fm_replacement_d2_114'], 'func': fm_replacement_d3_114}


def fm_replacement_d3_115(fm_replacement_d2_115):
    feature = _clean(fm_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_115'] = {'inputs': ['fm_replacement_d2_115'], 'func': fm_replacement_d3_115}


def fm_replacement_d3_116(fm_replacement_d2_116):
    feature = _clean(fm_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_116'] = {'inputs': ['fm_replacement_d2_116'], 'func': fm_replacement_d3_116}


def fm_replacement_d3_117(fm_replacement_d2_117):
    feature = _clean(fm_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_117'] = {'inputs': ['fm_replacement_d2_117'], 'func': fm_replacement_d3_117}


def fm_replacement_d3_118(fm_replacement_d2_118):
    feature = _clean(fm_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_118'] = {'inputs': ['fm_replacement_d2_118'], 'func': fm_replacement_d3_118}


def fm_replacement_d3_119(fm_replacement_d2_119):
    feature = _clean(fm_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_119'] = {'inputs': ['fm_replacement_d2_119'], 'func': fm_replacement_d3_119}


def fm_replacement_d3_120(fm_replacement_d2_120):
    feature = _clean(fm_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_120'] = {'inputs': ['fm_replacement_d2_120'], 'func': fm_replacement_d3_120}


def fm_replacement_d3_121(fm_replacement_d2_121):
    feature = _clean(fm_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_121'] = {'inputs': ['fm_replacement_d2_121'], 'func': fm_replacement_d3_121}


def fm_replacement_d3_122(fm_replacement_d2_122):
    feature = _clean(fm_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_122'] = {'inputs': ['fm_replacement_d2_122'], 'func': fm_replacement_d3_122}


def fm_replacement_d3_123(fm_replacement_d2_123):
    feature = _clean(fm_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_123'] = {'inputs': ['fm_replacement_d2_123'], 'func': fm_replacement_d3_123}


def fm_replacement_d3_124(fm_replacement_d2_124):
    feature = _clean(fm_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_124'] = {'inputs': ['fm_replacement_d2_124'], 'func': fm_replacement_d3_124}


def fm_replacement_d3_125(fm_replacement_d2_125):
    feature = _clean(fm_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_125'] = {'inputs': ['fm_replacement_d2_125'], 'func': fm_replacement_d3_125}


def fm_replacement_d3_126(fm_replacement_d2_126):
    feature = _clean(fm_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_126'] = {'inputs': ['fm_replacement_d2_126'], 'func': fm_replacement_d3_126}


def fm_replacement_d3_127(fm_replacement_d2_127):
    feature = _clean(fm_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_127'] = {'inputs': ['fm_replacement_d2_127'], 'func': fm_replacement_d3_127}


def fm_replacement_d3_128(fm_replacement_d2_128):
    feature = _clean(fm_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_128'] = {'inputs': ['fm_replacement_d2_128'], 'func': fm_replacement_d3_128}


def fm_replacement_d3_129(fm_replacement_d2_129):
    feature = _clean(fm_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_129'] = {'inputs': ['fm_replacement_d2_129'], 'func': fm_replacement_d3_129}


def fm_replacement_d3_130(fm_replacement_d2_130):
    feature = _clean(fm_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_130'] = {'inputs': ['fm_replacement_d2_130'], 'func': fm_replacement_d3_130}


def fm_replacement_d3_131(fm_replacement_d2_131):
    feature = _clean(fm_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_131'] = {'inputs': ['fm_replacement_d2_131'], 'func': fm_replacement_d3_131}


def fm_replacement_d3_132(fm_replacement_d2_132):
    feature = _clean(fm_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_132'] = {'inputs': ['fm_replacement_d2_132'], 'func': fm_replacement_d3_132}


def fm_replacement_d3_133(fm_replacement_d2_133):
    feature = _clean(fm_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_133'] = {'inputs': ['fm_replacement_d2_133'], 'func': fm_replacement_d3_133}


def fm_replacement_d3_134(fm_replacement_d2_134):
    feature = _clean(fm_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_134'] = {'inputs': ['fm_replacement_d2_134'], 'func': fm_replacement_d3_134}


def fm_replacement_d3_135(fm_replacement_d2_135):
    feature = _clean(fm_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_135'] = {'inputs': ['fm_replacement_d2_135'], 'func': fm_replacement_d3_135}


def fm_replacement_d3_136(fm_replacement_d2_136):
    feature = _clean(fm_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_136'] = {'inputs': ['fm_replacement_d2_136'], 'func': fm_replacement_d3_136}


def fm_replacement_d3_137(fm_replacement_d2_137):
    feature = _clean(fm_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_137'] = {'inputs': ['fm_replacement_d2_137'], 'func': fm_replacement_d3_137}


def fm_replacement_d3_138(fm_replacement_d2_138):
    feature = _clean(fm_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_138'] = {'inputs': ['fm_replacement_d2_138'], 'func': fm_replacement_d3_138}


def fm_replacement_d3_139(fm_replacement_d2_139):
    feature = _clean(fm_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_139'] = {'inputs': ['fm_replacement_d2_139'], 'func': fm_replacement_d3_139}


def fm_replacement_d3_140(fm_replacement_d2_140):
    feature = _clean(fm_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_140'] = {'inputs': ['fm_replacement_d2_140'], 'func': fm_replacement_d3_140}


def fm_replacement_d3_141(fm_replacement_d2_141):
    feature = _clean(fm_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_141'] = {'inputs': ['fm_replacement_d2_141'], 'func': fm_replacement_d3_141}


def fm_replacement_d3_142(fm_replacement_d2_142):
    feature = _clean(fm_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_142'] = {'inputs': ['fm_replacement_d2_142'], 'func': fm_replacement_d3_142}


def fm_replacement_d3_143(fm_replacement_d2_143):
    feature = _clean(fm_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_143'] = {'inputs': ['fm_replacement_d2_143'], 'func': fm_replacement_d3_143}


def fm_replacement_d3_144(fm_replacement_d2_144):
    feature = _clean(fm_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_144'] = {'inputs': ['fm_replacement_d2_144'], 'func': fm_replacement_d3_144}


def fm_replacement_d3_145(fm_replacement_d2_145):
    feature = _clean(fm_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_145'] = {'inputs': ['fm_replacement_d2_145'], 'func': fm_replacement_d3_145}


def fm_replacement_d3_146(fm_replacement_d2_146):
    feature = _clean(fm_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_146'] = {'inputs': ['fm_replacement_d2_146'], 'func': fm_replacement_d3_146}


def fm_replacement_d3_147(fm_replacement_d2_147):
    feature = _clean(fm_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_147'] = {'inputs': ['fm_replacement_d2_147'], 'func': fm_replacement_d3_147}


def fm_replacement_d3_148(fm_replacement_d2_148):
    feature = _clean(fm_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_148'] = {'inputs': ['fm_replacement_d2_148'], 'func': fm_replacement_d3_148}


def fm_replacement_d3_149(fm_replacement_d2_149):
    feature = _clean(fm_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_149'] = {'inputs': ['fm_replacement_d2_149'], 'func': fm_replacement_d3_149}


def fm_replacement_d3_150(fm_replacement_d2_150):
    feature = _clean(fm_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_150'] = {'inputs': ['fm_replacement_d2_150'], 'func': fm_replacement_d3_150}


def fm_replacement_d3_151(fm_replacement_d2_151):
    feature = _clean(fm_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_151'] = {'inputs': ['fm_replacement_d2_151'], 'func': fm_replacement_d3_151}


def fm_replacement_d3_152(fm_replacement_d2_152):
    feature = _clean(fm_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_152'] = {'inputs': ['fm_replacement_d2_152'], 'func': fm_replacement_d3_152}


def fm_replacement_d3_153(fm_replacement_d2_153):
    feature = _clean(fm_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_153'] = {'inputs': ['fm_replacement_d2_153'], 'func': fm_replacement_d3_153}


def fm_replacement_d3_154(fm_replacement_d2_154):
    feature = _clean(fm_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_154'] = {'inputs': ['fm_replacement_d2_154'], 'func': fm_replacement_d3_154}


def fm_replacement_d3_155(fm_replacement_d2_155):
    feature = _clean(fm_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_155'] = {'inputs': ['fm_replacement_d2_155'], 'func': fm_replacement_d3_155}


def fm_replacement_d3_156(fm_replacement_d2_156):
    feature = _clean(fm_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_156'] = {'inputs': ['fm_replacement_d2_156'], 'func': fm_replacement_d3_156}


def fm_replacement_d3_157(fm_replacement_d2_157):
    feature = _clean(fm_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_157'] = {'inputs': ['fm_replacement_d2_157'], 'func': fm_replacement_d3_157}


def fm_replacement_d3_158(fm_replacement_d2_158):
    feature = _clean(fm_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_158'] = {'inputs': ['fm_replacement_d2_158'], 'func': fm_replacement_d3_158}


def fm_replacement_d3_159(fm_replacement_d2_159):
    feature = _clean(fm_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_159'] = {'inputs': ['fm_replacement_d2_159'], 'func': fm_replacement_d3_159}


def fm_replacement_d3_160(fm_replacement_d2_160):
    feature = _clean(fm_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_160'] = {'inputs': ['fm_replacement_d2_160'], 'func': fm_replacement_d3_160}


def fm_replacement_d3_161(fm_replacement_d2_161):
    feature = _clean(fm_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_161'] = {'inputs': ['fm_replacement_d2_161'], 'func': fm_replacement_d3_161}


def fm_replacement_d3_162(fm_replacement_d2_162):
    feature = _clean(fm_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_162'] = {'inputs': ['fm_replacement_d2_162'], 'func': fm_replacement_d3_162}


def fm_replacement_d3_163(fm_replacement_d2_163):
    feature = _clean(fm_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_163'] = {'inputs': ['fm_replacement_d2_163'], 'func': fm_replacement_d3_163}


def fm_replacement_d3_164(fm_replacement_d2_164):
    feature = _clean(fm_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_164'] = {'inputs': ['fm_replacement_d2_164'], 'func': fm_replacement_d3_164}


def fm_replacement_d3_165(fm_replacement_d2_165):
    feature = _clean(fm_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_165'] = {'inputs': ['fm_replacement_d2_165'], 'func': fm_replacement_d3_165}


def fm_replacement_d3_166(fm_replacement_d2_166):
    feature = _clean(fm_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
FM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fm_replacement_d3_166'] = {'inputs': ['fm_replacement_d2_166'], 'func': fm_replacement_d3_166}


# Third-derivative extensions for repaired first-base features.
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def fmo_base_universe_d3_001_fmo_003_fcf_burn_to_cash_63(fmo_base_universe_d2_001_fmo_003_fcf_burn_to_cash_63):
    return _base_universe_d3(fmo_base_universe_d2_001_fmo_003_fcf_burn_to_cash_63, 1)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_001_fmo_003_fcf_burn_to_cash_63'] = {'inputs': ['fmo_base_universe_d2_001_fmo_003_fcf_burn_to_cash_63'], 'func': fmo_base_universe_d3_001_fmo_003_fcf_burn_to_cash_63}


def fmo_base_universe_d3_002_fmo_004_debt_to_equity_84(fmo_base_universe_d2_002_fmo_004_debt_to_equity_84):
    return _base_universe_d3(fmo_base_universe_d2_002_fmo_004_debt_to_equity_84, 2)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_002_fmo_004_debt_to_equity_84'] = {'inputs': ['fmo_base_universe_d2_002_fmo_004_debt_to_equity_84'], 'func': fmo_base_universe_d3_002_fmo_004_debt_to_equity_84}


def fmo_base_universe_d3_003_fmo_005_debt_to_assets_126(fmo_base_universe_d2_003_fmo_005_debt_to_assets_126):
    return _base_universe_d3(fmo_base_universe_d2_003_fmo_005_debt_to_assets_126, 3)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_003_fmo_005_debt_to_assets_126'] = {'inputs': ['fmo_base_universe_d2_003_fmo_005_debt_to_assets_126'], 'func': fmo_base_universe_d3_003_fmo_005_debt_to_assets_126}


def fmo_base_universe_d3_004_fmo_012_accrual_gap_1260(fmo_base_universe_d2_004_fmo_012_accrual_gap_1260):
    return _base_universe_d3(fmo_base_universe_d2_004_fmo_012_accrual_gap_1260, 4)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_004_fmo_012_accrual_gap_1260'] = {'inputs': ['fmo_base_universe_d2_004_fmo_012_accrual_gap_1260'], 'func': fmo_base_universe_d3_004_fmo_012_accrual_gap_1260}


def fmo_base_universe_d3_005_fmo_016_debt_to_equity_21(fmo_base_universe_d2_005_fmo_016_debt_to_equity_21):
    return _base_universe_d3(fmo_base_universe_d2_005_fmo_016_debt_to_equity_21, 5)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_005_fmo_016_debt_to_equity_21'] = {'inputs': ['fmo_base_universe_d2_005_fmo_016_debt_to_equity_21'], 'func': fmo_base_universe_d3_005_fmo_016_debt_to_equity_21}


def fmo_base_universe_d3_006_fmo_017_debt_to_assets_42(fmo_base_universe_d2_006_fmo_017_debt_to_assets_42):
    return _base_universe_d3(fmo_base_universe_d2_006_fmo_017_debt_to_assets_42, 6)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_006_fmo_017_debt_to_assets_42'] = {'inputs': ['fmo_base_universe_d2_006_fmo_017_debt_to_assets_42'], 'func': fmo_base_universe_d3_006_fmo_017_debt_to_assets_42}


def fmo_base_universe_d3_007_fmo_024_accrual_gap_504(fmo_base_universe_d2_007_fmo_024_accrual_gap_504):
    return _base_universe_d3(fmo_base_universe_d2_007_fmo_024_accrual_gap_504, 7)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_007_fmo_024_accrual_gap_504'] = {'inputs': ['fmo_base_universe_d2_007_fmo_024_accrual_gap_504'], 'func': fmo_base_universe_d3_007_fmo_024_accrual_gap_504}


def fmo_base_universe_d3_008_fmo_027_fcf_burn_to_cash_1260(fmo_base_universe_d2_008_fmo_027_fcf_burn_to_cash_1260):
    return _base_universe_d3(fmo_base_universe_d2_008_fmo_027_fcf_burn_to_cash_1260, 8)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_008_fmo_027_fcf_burn_to_cash_1260'] = {'inputs': ['fmo_base_universe_d2_008_fmo_027_fcf_burn_to_cash_1260'], 'func': fmo_base_universe_d3_008_fmo_027_fcf_burn_to_cash_1260}


def fmo_base_universe_d3_009_fmo_028_debt_to_equity_1512(fmo_base_universe_d2_009_fmo_028_debt_to_equity_1512):
    return _base_universe_d3(fmo_base_universe_d2_009_fmo_028_debt_to_equity_1512, 9)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_009_fmo_028_debt_to_equity_1512'] = {'inputs': ['fmo_base_universe_d2_009_fmo_028_debt_to_equity_1512'], 'func': fmo_base_universe_d3_009_fmo_028_debt_to_equity_1512}


def fmo_base_universe_d3_010_fmo_029_debt_to_assets_63(fmo_base_universe_d2_010_fmo_029_debt_to_assets_63):
    return _base_universe_d3(fmo_base_universe_d2_010_fmo_029_debt_to_assets_63, 10)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_010_fmo_029_debt_to_assets_63'] = {'inputs': ['fmo_base_universe_d2_010_fmo_029_debt_to_assets_63'], 'func': fmo_base_universe_d3_010_fmo_029_debt_to_assets_63}


def fmo_base_universe_d3_011_fmo_031_interest_coverage_stress_21(fmo_base_universe_d2_011_fmo_031_interest_coverage_stress_21):
    return _base_universe_d3(fmo_base_universe_d2_011_fmo_031_interest_coverage_stress_21, 11)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_011_fmo_031_interest_coverage_stress_21'] = {'inputs': ['fmo_base_universe_d2_011_fmo_031_interest_coverage_stress_21'], 'func': fmo_base_universe_d3_011_fmo_031_interest_coverage_stress_21}


def fmo_base_universe_d3_012_fmo_036_accrual_gap_189(fmo_base_universe_d2_012_fmo_036_accrual_gap_189):
    return _base_universe_d3(fmo_base_universe_d2_012_fmo_036_accrual_gap_189, 12)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_012_fmo_036_accrual_gap_189'] = {'inputs': ['fmo_base_universe_d2_012_fmo_036_accrual_gap_189'], 'func': fmo_base_universe_d3_012_fmo_036_accrual_gap_189}


def fmo_base_universe_d3_013_fmo_039_fcf_burn_to_cash_504(fmo_base_universe_d2_013_fmo_039_fcf_burn_to_cash_504):
    return _base_universe_d3(fmo_base_universe_d2_013_fmo_039_fcf_burn_to_cash_504, 13)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_013_fmo_039_fcf_burn_to_cash_504'] = {'inputs': ['fmo_base_universe_d2_013_fmo_039_fcf_burn_to_cash_504'], 'func': fmo_base_universe_d3_013_fmo_039_fcf_burn_to_cash_504}


def fmo_base_universe_d3_014_fmo_040_debt_to_equity_756(fmo_base_universe_d2_014_fmo_040_debt_to_equity_756):
    return _base_universe_d3(fmo_base_universe_d2_014_fmo_040_debt_to_equity_756, 14)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_014_fmo_040_debt_to_equity_756'] = {'inputs': ['fmo_base_universe_d2_014_fmo_040_debt_to_equity_756'], 'func': fmo_base_universe_d3_014_fmo_040_debt_to_equity_756}


def fmo_base_universe_d3_015_fmo_041_debt_to_assets_1008(fmo_base_universe_d2_015_fmo_041_debt_to_assets_1008):
    return _base_universe_d3(fmo_base_universe_d2_015_fmo_041_debt_to_assets_1008, 15)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_015_fmo_041_debt_to_assets_1008'] = {'inputs': ['fmo_base_universe_d2_015_fmo_041_debt_to_assets_1008'], 'func': fmo_base_universe_d3_015_fmo_041_debt_to_assets_1008}


def fmo_base_universe_d3_016_fmo_043_interest_coverage_stress_1512(fmo_base_universe_d2_016_fmo_043_interest_coverage_stress_1512):
    return _base_universe_d3(fmo_base_universe_d2_016_fmo_043_interest_coverage_stress_1512, 16)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_016_fmo_043_interest_coverage_stress_1512'] = {'inputs': ['fmo_base_universe_d2_016_fmo_043_interest_coverage_stress_1512'], 'func': fmo_base_universe_d3_016_fmo_043_interest_coverage_stress_1512}


def fmo_base_universe_d3_017_fmo_048_accrual_gap_63(fmo_base_universe_d2_017_fmo_048_accrual_gap_63):
    return _base_universe_d3(fmo_base_universe_d2_017_fmo_048_accrual_gap_63, 17)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_017_fmo_048_accrual_gap_63'] = {'inputs': ['fmo_base_universe_d2_017_fmo_048_accrual_gap_63'], 'func': fmo_base_universe_d3_017_fmo_048_accrual_gap_63}


def fmo_base_universe_d3_018_fmo_051_fcf_burn_to_cash_189(fmo_base_universe_d2_018_fmo_051_fcf_burn_to_cash_189):
    return _base_universe_d3(fmo_base_universe_d2_018_fmo_051_fcf_burn_to_cash_189, 18)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_018_fmo_051_fcf_burn_to_cash_189'] = {'inputs': ['fmo_base_universe_d2_018_fmo_051_fcf_burn_to_cash_189'], 'func': fmo_base_universe_d3_018_fmo_051_fcf_burn_to_cash_189}


def fmo_base_universe_d3_019_fmo_052_debt_to_equity_252(fmo_base_universe_d2_019_fmo_052_debt_to_equity_252):
    return _base_universe_d3(fmo_base_universe_d2_019_fmo_052_debt_to_equity_252, 19)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_019_fmo_052_debt_to_equity_252'] = {'inputs': ['fmo_base_universe_d2_019_fmo_052_debt_to_equity_252'], 'func': fmo_base_universe_d3_019_fmo_052_debt_to_equity_252}


def fmo_base_universe_d3_020_fmo_053_debt_to_assets_378(fmo_base_universe_d2_020_fmo_053_debt_to_assets_378):
    return _base_universe_d3(fmo_base_universe_d2_020_fmo_053_debt_to_assets_378, 20)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_020_fmo_053_debt_to_assets_378'] = {'inputs': ['fmo_base_universe_d2_020_fmo_053_debt_to_assets_378'], 'func': fmo_base_universe_d3_020_fmo_053_debt_to_assets_378}


def fmo_base_universe_d3_021_fmo_055_interest_coverage_stress_756(fmo_base_universe_d2_021_fmo_055_interest_coverage_stress_756):
    return _base_universe_d3(fmo_base_universe_d2_021_fmo_055_interest_coverage_stress_756, 21)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_021_fmo_055_interest_coverage_stress_756'] = {'inputs': ['fmo_base_universe_d2_021_fmo_055_interest_coverage_stress_756'], 'func': fmo_base_universe_d3_021_fmo_055_interest_coverage_stress_756}


def fmo_base_universe_d3_022_fmo_060_accrual_gap_252(fmo_base_universe_d2_022_fmo_060_accrual_gap_252):
    return _base_universe_d3(fmo_base_universe_d2_022_fmo_060_accrual_gap_252, 22)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_022_fmo_060_accrual_gap_252'] = {'inputs': ['fmo_base_universe_d2_022_fmo_060_accrual_gap_252'], 'func': fmo_base_universe_d3_022_fmo_060_accrual_gap_252}


def fmo_base_universe_d3_023_fmo_basefill_001(fmo_base_universe_d2_023_fmo_basefill_001):
    return _base_universe_d3(fmo_base_universe_d2_023_fmo_basefill_001, 23)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_023_fmo_basefill_001'] = {'inputs': ['fmo_base_universe_d2_023_fmo_basefill_001'], 'func': fmo_base_universe_d3_023_fmo_basefill_001}


def fmo_base_universe_d3_024_fmo_basefill_002(fmo_base_universe_d2_024_fmo_basefill_002):
    return _base_universe_d3(fmo_base_universe_d2_024_fmo_basefill_002, 24)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_024_fmo_basefill_002'] = {'inputs': ['fmo_base_universe_d2_024_fmo_basefill_002'], 'func': fmo_base_universe_d3_024_fmo_basefill_002}


def fmo_base_universe_d3_025_fmo_basefill_006(fmo_base_universe_d2_025_fmo_basefill_006):
    return _base_universe_d3(fmo_base_universe_d2_025_fmo_basefill_006, 25)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_025_fmo_basefill_006'] = {'inputs': ['fmo_base_universe_d2_025_fmo_basefill_006'], 'func': fmo_base_universe_d3_025_fmo_basefill_006}


def fmo_base_universe_d3_026_fmo_basefill_008(fmo_base_universe_d2_026_fmo_basefill_008):
    return _base_universe_d3(fmo_base_universe_d2_026_fmo_basefill_008, 26)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_026_fmo_basefill_008'] = {'inputs': ['fmo_base_universe_d2_026_fmo_basefill_008'], 'func': fmo_base_universe_d3_026_fmo_basefill_008}


def fmo_base_universe_d3_027_fmo_basefill_009(fmo_base_universe_d2_027_fmo_basefill_009):
    return _base_universe_d3(fmo_base_universe_d2_027_fmo_basefill_009, 27)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_027_fmo_basefill_009'] = {'inputs': ['fmo_base_universe_d2_027_fmo_basefill_009'], 'func': fmo_base_universe_d3_027_fmo_basefill_009}


def fmo_base_universe_d3_028_fmo_basefill_010(fmo_base_universe_d2_028_fmo_basefill_010):
    return _base_universe_d3(fmo_base_universe_d2_028_fmo_basefill_010, 28)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_028_fmo_basefill_010'] = {'inputs': ['fmo_base_universe_d2_028_fmo_basefill_010'], 'func': fmo_base_universe_d3_028_fmo_basefill_010}


def fmo_base_universe_d3_029_fmo_basefill_011(fmo_base_universe_d2_029_fmo_basefill_011):
    return _base_universe_d3(fmo_base_universe_d2_029_fmo_basefill_011, 29)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_029_fmo_basefill_011'] = {'inputs': ['fmo_base_universe_d2_029_fmo_basefill_011'], 'func': fmo_base_universe_d3_029_fmo_basefill_011}


def fmo_base_universe_d3_030_fmo_basefill_013(fmo_base_universe_d2_030_fmo_basefill_013):
    return _base_universe_d3(fmo_base_universe_d2_030_fmo_basefill_013, 30)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_030_fmo_basefill_013'] = {'inputs': ['fmo_base_universe_d2_030_fmo_basefill_013'], 'func': fmo_base_universe_d3_030_fmo_basefill_013}


def fmo_base_universe_d3_031_fmo_basefill_014(fmo_base_universe_d2_031_fmo_basefill_014):
    return _base_universe_d3(fmo_base_universe_d2_031_fmo_basefill_014, 31)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_031_fmo_basefill_014'] = {'inputs': ['fmo_base_universe_d2_031_fmo_basefill_014'], 'func': fmo_base_universe_d3_031_fmo_basefill_014}


def fmo_base_universe_d3_032_fmo_basefill_015(fmo_base_universe_d2_032_fmo_basefill_015):
    return _base_universe_d3(fmo_base_universe_d2_032_fmo_basefill_015, 32)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_032_fmo_basefill_015'] = {'inputs': ['fmo_base_universe_d2_032_fmo_basefill_015'], 'func': fmo_base_universe_d3_032_fmo_basefill_015}


def fmo_base_universe_d3_033_fmo_basefill_018(fmo_base_universe_d2_033_fmo_basefill_018):
    return _base_universe_d3(fmo_base_universe_d2_033_fmo_basefill_018, 33)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_033_fmo_basefill_018'] = {'inputs': ['fmo_base_universe_d2_033_fmo_basefill_018'], 'func': fmo_base_universe_d3_033_fmo_basefill_018}


def fmo_base_universe_d3_034_fmo_basefill_020(fmo_base_universe_d2_034_fmo_basefill_020):
    return _base_universe_d3(fmo_base_universe_d2_034_fmo_basefill_020, 34)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_034_fmo_basefill_020'] = {'inputs': ['fmo_base_universe_d2_034_fmo_basefill_020'], 'func': fmo_base_universe_d3_034_fmo_basefill_020}


def fmo_base_universe_d3_035_fmo_basefill_021(fmo_base_universe_d2_035_fmo_basefill_021):
    return _base_universe_d3(fmo_base_universe_d2_035_fmo_basefill_021, 35)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_035_fmo_basefill_021'] = {'inputs': ['fmo_base_universe_d2_035_fmo_basefill_021'], 'func': fmo_base_universe_d3_035_fmo_basefill_021}


def fmo_base_universe_d3_036_fmo_basefill_022(fmo_base_universe_d2_036_fmo_basefill_022):
    return _base_universe_d3(fmo_base_universe_d2_036_fmo_basefill_022, 36)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_036_fmo_basefill_022'] = {'inputs': ['fmo_base_universe_d2_036_fmo_basefill_022'], 'func': fmo_base_universe_d3_036_fmo_basefill_022}


def fmo_base_universe_d3_037_fmo_basefill_023(fmo_base_universe_d2_037_fmo_basefill_023):
    return _base_universe_d3(fmo_base_universe_d2_037_fmo_basefill_023, 37)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_037_fmo_basefill_023'] = {'inputs': ['fmo_base_universe_d2_037_fmo_basefill_023'], 'func': fmo_base_universe_d3_037_fmo_basefill_023}


def fmo_base_universe_d3_038_fmo_basefill_025(fmo_base_universe_d2_038_fmo_basefill_025):
    return _base_universe_d3(fmo_base_universe_d2_038_fmo_basefill_025, 38)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_038_fmo_basefill_025'] = {'inputs': ['fmo_base_universe_d2_038_fmo_basefill_025'], 'func': fmo_base_universe_d3_038_fmo_basefill_025}


def fmo_base_universe_d3_039_fmo_basefill_026(fmo_base_universe_d2_039_fmo_basefill_026):
    return _base_universe_d3(fmo_base_universe_d2_039_fmo_basefill_026, 39)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_039_fmo_basefill_026'] = {'inputs': ['fmo_base_universe_d2_039_fmo_basefill_026'], 'func': fmo_base_universe_d3_039_fmo_basefill_026}


def fmo_base_universe_d3_040_fmo_basefill_030(fmo_base_universe_d2_040_fmo_basefill_030):
    return _base_universe_d3(fmo_base_universe_d2_040_fmo_basefill_030, 40)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_040_fmo_basefill_030'] = {'inputs': ['fmo_base_universe_d2_040_fmo_basefill_030'], 'func': fmo_base_universe_d3_040_fmo_basefill_030}


def fmo_base_universe_d3_041_fmo_basefill_032(fmo_base_universe_d2_041_fmo_basefill_032):
    return _base_universe_d3(fmo_base_universe_d2_041_fmo_basefill_032, 41)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_041_fmo_basefill_032'] = {'inputs': ['fmo_base_universe_d2_041_fmo_basefill_032'], 'func': fmo_base_universe_d3_041_fmo_basefill_032}


def fmo_base_universe_d3_042_fmo_basefill_033(fmo_base_universe_d2_042_fmo_basefill_033):
    return _base_universe_d3(fmo_base_universe_d2_042_fmo_basefill_033, 42)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_042_fmo_basefill_033'] = {'inputs': ['fmo_base_universe_d2_042_fmo_basefill_033'], 'func': fmo_base_universe_d3_042_fmo_basefill_033}


def fmo_base_universe_d3_043_fmo_basefill_034(fmo_base_universe_d2_043_fmo_basefill_034):
    return _base_universe_d3(fmo_base_universe_d2_043_fmo_basefill_034, 43)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_043_fmo_basefill_034'] = {'inputs': ['fmo_base_universe_d2_043_fmo_basefill_034'], 'func': fmo_base_universe_d3_043_fmo_basefill_034}


def fmo_base_universe_d3_044_fmo_basefill_035(fmo_base_universe_d2_044_fmo_basefill_035):
    return _base_universe_d3(fmo_base_universe_d2_044_fmo_basefill_035, 44)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_044_fmo_basefill_035'] = {'inputs': ['fmo_base_universe_d2_044_fmo_basefill_035'], 'func': fmo_base_universe_d3_044_fmo_basefill_035}


def fmo_base_universe_d3_045_fmo_basefill_037(fmo_base_universe_d2_045_fmo_basefill_037):
    return _base_universe_d3(fmo_base_universe_d2_045_fmo_basefill_037, 45)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_045_fmo_basefill_037'] = {'inputs': ['fmo_base_universe_d2_045_fmo_basefill_037'], 'func': fmo_base_universe_d3_045_fmo_basefill_037}


def fmo_base_universe_d3_046_fmo_basefill_038(fmo_base_universe_d2_046_fmo_basefill_038):
    return _base_universe_d3(fmo_base_universe_d2_046_fmo_basefill_038, 46)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_046_fmo_basefill_038'] = {'inputs': ['fmo_base_universe_d2_046_fmo_basefill_038'], 'func': fmo_base_universe_d3_046_fmo_basefill_038}


def fmo_base_universe_d3_047_fmo_basefill_042(fmo_base_universe_d2_047_fmo_basefill_042):
    return _base_universe_d3(fmo_base_universe_d2_047_fmo_basefill_042, 47)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_047_fmo_basefill_042'] = {'inputs': ['fmo_base_universe_d2_047_fmo_basefill_042'], 'func': fmo_base_universe_d3_047_fmo_basefill_042}


def fmo_base_universe_d3_048_fmo_basefill_044(fmo_base_universe_d2_048_fmo_basefill_044):
    return _base_universe_d3(fmo_base_universe_d2_048_fmo_basefill_044, 48)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_048_fmo_basefill_044'] = {'inputs': ['fmo_base_universe_d2_048_fmo_basefill_044'], 'func': fmo_base_universe_d3_048_fmo_basefill_044}


def fmo_base_universe_d3_049_fmo_basefill_045(fmo_base_universe_d2_049_fmo_basefill_045):
    return _base_universe_d3(fmo_base_universe_d2_049_fmo_basefill_045, 49)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_049_fmo_basefill_045'] = {'inputs': ['fmo_base_universe_d2_049_fmo_basefill_045'], 'func': fmo_base_universe_d3_049_fmo_basefill_045}


def fmo_base_universe_d3_050_fmo_basefill_046(fmo_base_universe_d2_050_fmo_basefill_046):
    return _base_universe_d3(fmo_base_universe_d2_050_fmo_basefill_046, 50)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_050_fmo_basefill_046'] = {'inputs': ['fmo_base_universe_d2_050_fmo_basefill_046'], 'func': fmo_base_universe_d3_050_fmo_basefill_046}


def fmo_base_universe_d3_051_fmo_basefill_047(fmo_base_universe_d2_051_fmo_basefill_047):
    return _base_universe_d3(fmo_base_universe_d2_051_fmo_basefill_047, 51)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_051_fmo_basefill_047'] = {'inputs': ['fmo_base_universe_d2_051_fmo_basefill_047'], 'func': fmo_base_universe_d3_051_fmo_basefill_047}


def fmo_base_universe_d3_052_fmo_basefill_049(fmo_base_universe_d2_052_fmo_basefill_049):
    return _base_universe_d3(fmo_base_universe_d2_052_fmo_basefill_049, 52)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_052_fmo_basefill_049'] = {'inputs': ['fmo_base_universe_d2_052_fmo_basefill_049'], 'func': fmo_base_universe_d3_052_fmo_basefill_049}


def fmo_base_universe_d3_053_fmo_basefill_050(fmo_base_universe_d2_053_fmo_basefill_050):
    return _base_universe_d3(fmo_base_universe_d2_053_fmo_basefill_050, 53)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_053_fmo_basefill_050'] = {'inputs': ['fmo_base_universe_d2_053_fmo_basefill_050'], 'func': fmo_base_universe_d3_053_fmo_basefill_050}


def fmo_base_universe_d3_054_fmo_basefill_054(fmo_base_universe_d2_054_fmo_basefill_054):
    return _base_universe_d3(fmo_base_universe_d2_054_fmo_basefill_054, 54)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_054_fmo_basefill_054'] = {'inputs': ['fmo_base_universe_d2_054_fmo_basefill_054'], 'func': fmo_base_universe_d3_054_fmo_basefill_054}


def fmo_base_universe_d3_055_fmo_basefill_056(fmo_base_universe_d2_055_fmo_basefill_056):
    return _base_universe_d3(fmo_base_universe_d2_055_fmo_basefill_056, 55)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_055_fmo_basefill_056'] = {'inputs': ['fmo_base_universe_d2_055_fmo_basefill_056'], 'func': fmo_base_universe_d3_055_fmo_basefill_056}


def fmo_base_universe_d3_056_fmo_basefill_057(fmo_base_universe_d2_056_fmo_basefill_057):
    return _base_universe_d3(fmo_base_universe_d2_056_fmo_basefill_057, 56)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_056_fmo_basefill_057'] = {'inputs': ['fmo_base_universe_d2_056_fmo_basefill_057'], 'func': fmo_base_universe_d3_056_fmo_basefill_057}


def fmo_base_universe_d3_057_fmo_basefill_058(fmo_base_universe_d2_057_fmo_basefill_058):
    return _base_universe_d3(fmo_base_universe_d2_057_fmo_basefill_058, 57)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_057_fmo_basefill_058'] = {'inputs': ['fmo_base_universe_d2_057_fmo_basefill_058'], 'func': fmo_base_universe_d3_057_fmo_basefill_058}


def fmo_base_universe_d3_058_fmo_basefill_059(fmo_base_universe_d2_058_fmo_basefill_059):
    return _base_universe_d3(fmo_base_universe_d2_058_fmo_basefill_059, 58)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_058_fmo_basefill_059'] = {'inputs': ['fmo_base_universe_d2_058_fmo_basefill_059'], 'func': fmo_base_universe_d3_058_fmo_basefill_059}


def fmo_base_universe_d3_059_fmo_basefill_061(fmo_base_universe_d2_059_fmo_basefill_061):
    return _base_universe_d3(fmo_base_universe_d2_059_fmo_basefill_061, 59)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_059_fmo_basefill_061'] = {'inputs': ['fmo_base_universe_d2_059_fmo_basefill_061'], 'func': fmo_base_universe_d3_059_fmo_basefill_061}


def fmo_base_universe_d3_060_fmo_basefill_062(fmo_base_universe_d2_060_fmo_basefill_062):
    return _base_universe_d3(fmo_base_universe_d2_060_fmo_basefill_062, 60)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_060_fmo_basefill_062'] = {'inputs': ['fmo_base_universe_d2_060_fmo_basefill_062'], 'func': fmo_base_universe_d3_060_fmo_basefill_062}


def fmo_base_universe_d3_061_fmo_basefill_063(fmo_base_universe_d2_061_fmo_basefill_063):
    return _base_universe_d3(fmo_base_universe_d2_061_fmo_basefill_063, 61)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_061_fmo_basefill_063'] = {'inputs': ['fmo_base_universe_d2_061_fmo_basefill_063'], 'func': fmo_base_universe_d3_061_fmo_basefill_063}


def fmo_base_universe_d3_062_fmo_basefill_064(fmo_base_universe_d2_062_fmo_basefill_064):
    return _base_universe_d3(fmo_base_universe_d2_062_fmo_basefill_064, 62)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_062_fmo_basefill_064'] = {'inputs': ['fmo_base_universe_d2_062_fmo_basefill_064'], 'func': fmo_base_universe_d3_062_fmo_basefill_064}


def fmo_base_universe_d3_063_fmo_basefill_065(fmo_base_universe_d2_063_fmo_basefill_065):
    return _base_universe_d3(fmo_base_universe_d2_063_fmo_basefill_065, 63)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_063_fmo_basefill_065'] = {'inputs': ['fmo_base_universe_d2_063_fmo_basefill_065'], 'func': fmo_base_universe_d3_063_fmo_basefill_065}


def fmo_base_universe_d3_064_fmo_basefill_066(fmo_base_universe_d2_064_fmo_basefill_066):
    return _base_universe_d3(fmo_base_universe_d2_064_fmo_basefill_066, 64)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_064_fmo_basefill_066'] = {'inputs': ['fmo_base_universe_d2_064_fmo_basefill_066'], 'func': fmo_base_universe_d3_064_fmo_basefill_066}


def fmo_base_universe_d3_065_fmo_basefill_067(fmo_base_universe_d2_065_fmo_basefill_067):
    return _base_universe_d3(fmo_base_universe_d2_065_fmo_basefill_067, 65)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_065_fmo_basefill_067'] = {'inputs': ['fmo_base_universe_d2_065_fmo_basefill_067'], 'func': fmo_base_universe_d3_065_fmo_basefill_067}


def fmo_base_universe_d3_066_fmo_basefill_068(fmo_base_universe_d2_066_fmo_basefill_068):
    return _base_universe_d3(fmo_base_universe_d2_066_fmo_basefill_068, 66)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_066_fmo_basefill_068'] = {'inputs': ['fmo_base_universe_d2_066_fmo_basefill_068'], 'func': fmo_base_universe_d3_066_fmo_basefill_068}


def fmo_base_universe_d3_067_fmo_basefill_069(fmo_base_universe_d2_067_fmo_basefill_069):
    return _base_universe_d3(fmo_base_universe_d2_067_fmo_basefill_069, 67)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_067_fmo_basefill_069'] = {'inputs': ['fmo_base_universe_d2_067_fmo_basefill_069'], 'func': fmo_base_universe_d3_067_fmo_basefill_069}


def fmo_base_universe_d3_068_fmo_basefill_070(fmo_base_universe_d2_068_fmo_basefill_070):
    return _base_universe_d3(fmo_base_universe_d2_068_fmo_basefill_070, 68)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_068_fmo_basefill_070'] = {'inputs': ['fmo_base_universe_d2_068_fmo_basefill_070'], 'func': fmo_base_universe_d3_068_fmo_basefill_070}


def fmo_base_universe_d3_069_fmo_basefill_071(fmo_base_universe_d2_069_fmo_basefill_071):
    return _base_universe_d3(fmo_base_universe_d2_069_fmo_basefill_071, 69)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_069_fmo_basefill_071'] = {'inputs': ['fmo_base_universe_d2_069_fmo_basefill_071'], 'func': fmo_base_universe_d3_069_fmo_basefill_071}


def fmo_base_universe_d3_070_fmo_basefill_072(fmo_base_universe_d2_070_fmo_basefill_072):
    return _base_universe_d3(fmo_base_universe_d2_070_fmo_basefill_072, 70)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_070_fmo_basefill_072'] = {'inputs': ['fmo_base_universe_d2_070_fmo_basefill_072'], 'func': fmo_base_universe_d3_070_fmo_basefill_072}


def fmo_base_universe_d3_071_fmo_basefill_073(fmo_base_universe_d2_071_fmo_basefill_073):
    return _base_universe_d3(fmo_base_universe_d2_071_fmo_basefill_073, 71)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_071_fmo_basefill_073'] = {'inputs': ['fmo_base_universe_d2_071_fmo_basefill_073'], 'func': fmo_base_universe_d3_071_fmo_basefill_073}


def fmo_base_universe_d3_072_fmo_basefill_074(fmo_base_universe_d2_072_fmo_basefill_074):
    return _base_universe_d3(fmo_base_universe_d2_072_fmo_basefill_074, 72)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_072_fmo_basefill_074'] = {'inputs': ['fmo_base_universe_d2_072_fmo_basefill_074'], 'func': fmo_base_universe_d3_072_fmo_basefill_074}


def fmo_base_universe_d3_073_fmo_basefill_075(fmo_base_universe_d2_073_fmo_basefill_075):
    return _base_universe_d3(fmo_base_universe_d2_073_fmo_basefill_075, 73)
FMO_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fmo_base_universe_d3_073_fmo_basefill_075'] = {'inputs': ['fmo_base_universe_d2_073_fmo_basefill_075'], 'func': fmo_base_universe_d3_073_fmo_basefill_075}
