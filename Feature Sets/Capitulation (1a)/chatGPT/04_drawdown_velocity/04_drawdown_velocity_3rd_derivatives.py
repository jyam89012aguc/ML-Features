import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _safe_div(a, b):
    b = _s(b).replace(0, np.nan)
    if np.isscalar(a):
        return a / b
    a = _s(a)
    return a / b


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


def _true_range(high, low, close):
    high = _s(high)
    low = _s(low)
    prev_close = _s(close).shift(1)
    return pd.concat([high - low, (high - prev_close).abs(), (low - prev_close).abs()], axis=1).max(axis=1)


def _streak(mask):
    mask = pd.Series(mask).fillna(False).astype(bool)
    groups = mask.ne(mask.shift()).cumsum()
    return mask.groupby(groups).cumcount().add(1).where(mask, 0).astype(float)



def dvel_176_dvel_001_drawdown_from_high_5_001_accel_1(dvel_151_dvel_001_drawdown_from_high_5_001_roc_1):
    feature = _s(dvel_151_dvel_001_drawdown_from_high_5_001_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def dvel_177_dvel_007_drawdown_from_high_126_007_accel_5(dvel_152_dvel_007_drawdown_from_high_126_007_roc_5):
    feature = _s(dvel_152_dvel_007_drawdown_from_high_126_007_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def dvel_178_dvel_013_drawdown_from_high_1008_013_accel_42(dvel_153_dvel_013_drawdown_from_high_1008_013_roc_42):
    feature = _s(dvel_153_dvel_013_drawdown_from_high_1008_013_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def dvel_179_dvel_019_drawdown_from_high_42_019_accel_126(dvel_154_dvel_019_drawdown_from_high_42_019_roc_126):
    feature = _s(dvel_154_dvel_019_drawdown_from_high_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def dvel_180_dvel_025_drawdown_from_high_378_025_accel_378(dvel_155_dvel_025_drawdown_from_high_378_025_roc_378):
    feature = _s(dvel_155_dvel_025_drawdown_from_high_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















DRAWDOWN_VELOCITY_REGISTRY_3RD_DERIVATIVES = {
    'dvel_176_dvel_001_drawdown_from_high_5_001_accel_1': {'inputs': ['dvel_151_dvel_001_drawdown_from_high_5_001_roc_1'], 'func': dvel_176_dvel_001_drawdown_from_high_5_001_accel_1},
    'dvel_177_dvel_007_drawdown_from_high_126_007_accel_5': {'inputs': ['dvel_152_dvel_007_drawdown_from_high_126_007_roc_5'], 'func': dvel_177_dvel_007_drawdown_from_high_126_007_accel_5},
    'dvel_178_dvel_013_drawdown_from_high_1008_013_accel_42': {'inputs': ['dvel_153_dvel_013_drawdown_from_high_1008_013_roc_42'], 'func': dvel_178_dvel_013_drawdown_from_high_1008_013_accel_42},
    'dvel_179_dvel_019_drawdown_from_high_42_019_accel_126': {'inputs': ['dvel_154_dvel_019_drawdown_from_high_42_019_roc_126'], 'func': dvel_179_dvel_019_drawdown_from_high_42_019_accel_126},
    'dvel_180_dvel_025_drawdown_from_high_378_025_accel_378': {'inputs': ['dvel_155_dvel_025_drawdown_from_high_378_025_roc_378'], 'func': dvel_180_dvel_025_drawdown_from_high_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def dv_replacement_d3_001(dv_replacement_d2_001):
    feature = _clean(dv_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_001'] = {'inputs': ['dv_replacement_d2_001'], 'func': dv_replacement_d3_001}


def dv_replacement_d3_002(dv_replacement_d2_002):
    feature = _clean(dv_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_002'] = {'inputs': ['dv_replacement_d2_002'], 'func': dv_replacement_d3_002}


def dv_replacement_d3_003(dv_replacement_d2_003):
    feature = _clean(dv_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_003'] = {'inputs': ['dv_replacement_d2_003'], 'func': dv_replacement_d3_003}


def dv_replacement_d3_004(dv_replacement_d2_004):
    feature = _clean(dv_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_004'] = {'inputs': ['dv_replacement_d2_004'], 'func': dv_replacement_d3_004}


def dv_replacement_d3_005(dv_replacement_d2_005):
    feature = _clean(dv_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_005'] = {'inputs': ['dv_replacement_d2_005'], 'func': dv_replacement_d3_005}


def dv_replacement_d3_006(dv_replacement_d2_006):
    feature = _clean(dv_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_006'] = {'inputs': ['dv_replacement_d2_006'], 'func': dv_replacement_d3_006}


def dv_replacement_d3_007(dv_replacement_d2_007):
    feature = _clean(dv_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_007'] = {'inputs': ['dv_replacement_d2_007'], 'func': dv_replacement_d3_007}


def dv_replacement_d3_008(dv_replacement_d2_008):
    feature = _clean(dv_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_008'] = {'inputs': ['dv_replacement_d2_008'], 'func': dv_replacement_d3_008}


def dv_replacement_d3_009(dv_replacement_d2_009):
    feature = _clean(dv_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_009'] = {'inputs': ['dv_replacement_d2_009'], 'func': dv_replacement_d3_009}


def dv_replacement_d3_010(dv_replacement_d2_010):
    feature = _clean(dv_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_010'] = {'inputs': ['dv_replacement_d2_010'], 'func': dv_replacement_d3_010}


def dv_replacement_d3_011(dv_replacement_d2_011):
    feature = _clean(dv_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_011'] = {'inputs': ['dv_replacement_d2_011'], 'func': dv_replacement_d3_011}


def dv_replacement_d3_012(dv_replacement_d2_012):
    feature = _clean(dv_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_012'] = {'inputs': ['dv_replacement_d2_012'], 'func': dv_replacement_d3_012}


def dv_replacement_d3_013(dv_replacement_d2_013):
    feature = _clean(dv_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_013'] = {'inputs': ['dv_replacement_d2_013'], 'func': dv_replacement_d3_013}


def dv_replacement_d3_014(dv_replacement_d2_014):
    feature = _clean(dv_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_014'] = {'inputs': ['dv_replacement_d2_014'], 'func': dv_replacement_d3_014}


def dv_replacement_d3_015(dv_replacement_d2_015):
    feature = _clean(dv_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_015'] = {'inputs': ['dv_replacement_d2_015'], 'func': dv_replacement_d3_015}


def dv_replacement_d3_016(dv_replacement_d2_016):
    feature = _clean(dv_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_016'] = {'inputs': ['dv_replacement_d2_016'], 'func': dv_replacement_d3_016}


def dv_replacement_d3_017(dv_replacement_d2_017):
    feature = _clean(dv_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_017'] = {'inputs': ['dv_replacement_d2_017'], 'func': dv_replacement_d3_017}


def dv_replacement_d3_018(dv_replacement_d2_018):
    feature = _clean(dv_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_018'] = {'inputs': ['dv_replacement_d2_018'], 'func': dv_replacement_d3_018}


def dv_replacement_d3_019(dv_replacement_d2_019):
    feature = _clean(dv_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_019'] = {'inputs': ['dv_replacement_d2_019'], 'func': dv_replacement_d3_019}


def dv_replacement_d3_020(dv_replacement_d2_020):
    feature = _clean(dv_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_020'] = {'inputs': ['dv_replacement_d2_020'], 'func': dv_replacement_d3_020}


def dv_replacement_d3_021(dv_replacement_d2_021):
    feature = _clean(dv_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_021'] = {'inputs': ['dv_replacement_d2_021'], 'func': dv_replacement_d3_021}


def dv_replacement_d3_022(dv_replacement_d2_022):
    feature = _clean(dv_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_022'] = {'inputs': ['dv_replacement_d2_022'], 'func': dv_replacement_d3_022}


def dv_replacement_d3_023(dv_replacement_d2_023):
    feature = _clean(dv_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_023'] = {'inputs': ['dv_replacement_d2_023'], 'func': dv_replacement_d3_023}


def dv_replacement_d3_024(dv_replacement_d2_024):
    feature = _clean(dv_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_024'] = {'inputs': ['dv_replacement_d2_024'], 'func': dv_replacement_d3_024}


def dv_replacement_d3_025(dv_replacement_d2_025):
    feature = _clean(dv_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_025'] = {'inputs': ['dv_replacement_d2_025'], 'func': dv_replacement_d3_025}


def dv_replacement_d3_026(dv_replacement_d2_026):
    feature = _clean(dv_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_026'] = {'inputs': ['dv_replacement_d2_026'], 'func': dv_replacement_d3_026}


def dv_replacement_d3_027(dv_replacement_d2_027):
    feature = _clean(dv_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_027'] = {'inputs': ['dv_replacement_d2_027'], 'func': dv_replacement_d3_027}


def dv_replacement_d3_028(dv_replacement_d2_028):
    feature = _clean(dv_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_028'] = {'inputs': ['dv_replacement_d2_028'], 'func': dv_replacement_d3_028}


def dv_replacement_d3_029(dv_replacement_d2_029):
    feature = _clean(dv_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_029'] = {'inputs': ['dv_replacement_d2_029'], 'func': dv_replacement_d3_029}


def dv_replacement_d3_030(dv_replacement_d2_030):
    feature = _clean(dv_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_030'] = {'inputs': ['dv_replacement_d2_030'], 'func': dv_replacement_d3_030}


def dv_replacement_d3_031(dv_replacement_d2_031):
    feature = _clean(dv_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_031'] = {'inputs': ['dv_replacement_d2_031'], 'func': dv_replacement_d3_031}


def dv_replacement_d3_032(dv_replacement_d2_032):
    feature = _clean(dv_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_032'] = {'inputs': ['dv_replacement_d2_032'], 'func': dv_replacement_d3_032}


def dv_replacement_d3_033(dv_replacement_d2_033):
    feature = _clean(dv_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_033'] = {'inputs': ['dv_replacement_d2_033'], 'func': dv_replacement_d3_033}


def dv_replacement_d3_034(dv_replacement_d2_034):
    feature = _clean(dv_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_034'] = {'inputs': ['dv_replacement_d2_034'], 'func': dv_replacement_d3_034}


def dv_replacement_d3_035(dv_replacement_d2_035):
    feature = _clean(dv_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_035'] = {'inputs': ['dv_replacement_d2_035'], 'func': dv_replacement_d3_035}


def dv_replacement_d3_036(dv_replacement_d2_036):
    feature = _clean(dv_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_036'] = {'inputs': ['dv_replacement_d2_036'], 'func': dv_replacement_d3_036}


def dv_replacement_d3_037(dv_replacement_d2_037):
    feature = _clean(dv_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_037'] = {'inputs': ['dv_replacement_d2_037'], 'func': dv_replacement_d3_037}


def dv_replacement_d3_038(dv_replacement_d2_038):
    feature = _clean(dv_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_038'] = {'inputs': ['dv_replacement_d2_038'], 'func': dv_replacement_d3_038}


def dv_replacement_d3_039(dv_replacement_d2_039):
    feature = _clean(dv_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_039'] = {'inputs': ['dv_replacement_d2_039'], 'func': dv_replacement_d3_039}


def dv_replacement_d3_040(dv_replacement_d2_040):
    feature = _clean(dv_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_040'] = {'inputs': ['dv_replacement_d2_040'], 'func': dv_replacement_d3_040}


def dv_replacement_d3_041(dv_replacement_d2_041):
    feature = _clean(dv_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_041'] = {'inputs': ['dv_replacement_d2_041'], 'func': dv_replacement_d3_041}


def dv_replacement_d3_042(dv_replacement_d2_042):
    feature = _clean(dv_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_042'] = {'inputs': ['dv_replacement_d2_042'], 'func': dv_replacement_d3_042}


def dv_replacement_d3_043(dv_replacement_d2_043):
    feature = _clean(dv_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_043'] = {'inputs': ['dv_replacement_d2_043'], 'func': dv_replacement_d3_043}


def dv_replacement_d3_044(dv_replacement_d2_044):
    feature = _clean(dv_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_044'] = {'inputs': ['dv_replacement_d2_044'], 'func': dv_replacement_d3_044}


def dv_replacement_d3_045(dv_replacement_d2_045):
    feature = _clean(dv_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_045'] = {'inputs': ['dv_replacement_d2_045'], 'func': dv_replacement_d3_045}


def dv_replacement_d3_046(dv_replacement_d2_046):
    feature = _clean(dv_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_046'] = {'inputs': ['dv_replacement_d2_046'], 'func': dv_replacement_d3_046}


def dv_replacement_d3_047(dv_replacement_d2_047):
    feature = _clean(dv_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_047'] = {'inputs': ['dv_replacement_d2_047'], 'func': dv_replacement_d3_047}


def dv_replacement_d3_048(dv_replacement_d2_048):
    feature = _clean(dv_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_048'] = {'inputs': ['dv_replacement_d2_048'], 'func': dv_replacement_d3_048}


def dv_replacement_d3_049(dv_replacement_d2_049):
    feature = _clean(dv_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_049'] = {'inputs': ['dv_replacement_d2_049'], 'func': dv_replacement_d3_049}


def dv_replacement_d3_050(dv_replacement_d2_050):
    feature = _clean(dv_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_050'] = {'inputs': ['dv_replacement_d2_050'], 'func': dv_replacement_d3_050}


def dv_replacement_d3_051(dv_replacement_d2_051):
    feature = _clean(dv_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_051'] = {'inputs': ['dv_replacement_d2_051'], 'func': dv_replacement_d3_051}


def dv_replacement_d3_052(dv_replacement_d2_052):
    feature = _clean(dv_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_052'] = {'inputs': ['dv_replacement_d2_052'], 'func': dv_replacement_d3_052}


def dv_replacement_d3_053(dv_replacement_d2_053):
    feature = _clean(dv_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_053'] = {'inputs': ['dv_replacement_d2_053'], 'func': dv_replacement_d3_053}


def dv_replacement_d3_054(dv_replacement_d2_054):
    feature = _clean(dv_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_054'] = {'inputs': ['dv_replacement_d2_054'], 'func': dv_replacement_d3_054}


def dv_replacement_d3_055(dv_replacement_d2_055):
    feature = _clean(dv_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_055'] = {'inputs': ['dv_replacement_d2_055'], 'func': dv_replacement_d3_055}


def dv_replacement_d3_056(dv_replacement_d2_056):
    feature = _clean(dv_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_056'] = {'inputs': ['dv_replacement_d2_056'], 'func': dv_replacement_d3_056}


def dv_replacement_d3_057(dv_replacement_d2_057):
    feature = _clean(dv_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_057'] = {'inputs': ['dv_replacement_d2_057'], 'func': dv_replacement_d3_057}


def dv_replacement_d3_058(dv_replacement_d2_058):
    feature = _clean(dv_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_058'] = {'inputs': ['dv_replacement_d2_058'], 'func': dv_replacement_d3_058}


def dv_replacement_d3_059(dv_replacement_d2_059):
    feature = _clean(dv_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_059'] = {'inputs': ['dv_replacement_d2_059'], 'func': dv_replacement_d3_059}


def dv_replacement_d3_060(dv_replacement_d2_060):
    feature = _clean(dv_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_060'] = {'inputs': ['dv_replacement_d2_060'], 'func': dv_replacement_d3_060}


def dv_replacement_d3_061(dv_replacement_d2_061):
    feature = _clean(dv_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_061'] = {'inputs': ['dv_replacement_d2_061'], 'func': dv_replacement_d3_061}


def dv_replacement_d3_062(dv_replacement_d2_062):
    feature = _clean(dv_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_062'] = {'inputs': ['dv_replacement_d2_062'], 'func': dv_replacement_d3_062}


def dv_replacement_d3_063(dv_replacement_d2_063):
    feature = _clean(dv_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_063'] = {'inputs': ['dv_replacement_d2_063'], 'func': dv_replacement_d3_063}


def dv_replacement_d3_064(dv_replacement_d2_064):
    feature = _clean(dv_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_064'] = {'inputs': ['dv_replacement_d2_064'], 'func': dv_replacement_d3_064}


def dv_replacement_d3_065(dv_replacement_d2_065):
    feature = _clean(dv_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_065'] = {'inputs': ['dv_replacement_d2_065'], 'func': dv_replacement_d3_065}


def dv_replacement_d3_066(dv_replacement_d2_066):
    feature = _clean(dv_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_066'] = {'inputs': ['dv_replacement_d2_066'], 'func': dv_replacement_d3_066}


def dv_replacement_d3_067(dv_replacement_d2_067):
    feature = _clean(dv_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_067'] = {'inputs': ['dv_replacement_d2_067'], 'func': dv_replacement_d3_067}


def dv_replacement_d3_068(dv_replacement_d2_068):
    feature = _clean(dv_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_068'] = {'inputs': ['dv_replacement_d2_068'], 'func': dv_replacement_d3_068}


def dv_replacement_d3_069(dv_replacement_d2_069):
    feature = _clean(dv_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_069'] = {'inputs': ['dv_replacement_d2_069'], 'func': dv_replacement_d3_069}


def dv_replacement_d3_070(dv_replacement_d2_070):
    feature = _clean(dv_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_070'] = {'inputs': ['dv_replacement_d2_070'], 'func': dv_replacement_d3_070}


def dv_replacement_d3_071(dv_replacement_d2_071):
    feature = _clean(dv_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_071'] = {'inputs': ['dv_replacement_d2_071'], 'func': dv_replacement_d3_071}


def dv_replacement_d3_072(dv_replacement_d2_072):
    feature = _clean(dv_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_072'] = {'inputs': ['dv_replacement_d2_072'], 'func': dv_replacement_d3_072}


def dv_replacement_d3_073(dv_replacement_d2_073):
    feature = _clean(dv_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_073'] = {'inputs': ['dv_replacement_d2_073'], 'func': dv_replacement_d3_073}


def dv_replacement_d3_074(dv_replacement_d2_074):
    feature = _clean(dv_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_074'] = {'inputs': ['dv_replacement_d2_074'], 'func': dv_replacement_d3_074}


def dv_replacement_d3_075(dv_replacement_d2_075):
    feature = _clean(dv_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_075'] = {'inputs': ['dv_replacement_d2_075'], 'func': dv_replacement_d3_075}


def dv_replacement_d3_076(dv_replacement_d2_076):
    feature = _clean(dv_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_076'] = {'inputs': ['dv_replacement_d2_076'], 'func': dv_replacement_d3_076}


def dv_replacement_d3_077(dv_replacement_d2_077):
    feature = _clean(dv_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_077'] = {'inputs': ['dv_replacement_d2_077'], 'func': dv_replacement_d3_077}


def dv_replacement_d3_078(dv_replacement_d2_078):
    feature = _clean(dv_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_078'] = {'inputs': ['dv_replacement_d2_078'], 'func': dv_replacement_d3_078}


def dv_replacement_d3_079(dv_replacement_d2_079):
    feature = _clean(dv_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_079'] = {'inputs': ['dv_replacement_d2_079'], 'func': dv_replacement_d3_079}


def dv_replacement_d3_080(dv_replacement_d2_080):
    feature = _clean(dv_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_080'] = {'inputs': ['dv_replacement_d2_080'], 'func': dv_replacement_d3_080}


def dv_replacement_d3_081(dv_replacement_d2_081):
    feature = _clean(dv_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_081'] = {'inputs': ['dv_replacement_d2_081'], 'func': dv_replacement_d3_081}


def dv_replacement_d3_082(dv_replacement_d2_082):
    feature = _clean(dv_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_082'] = {'inputs': ['dv_replacement_d2_082'], 'func': dv_replacement_d3_082}


def dv_replacement_d3_083(dv_replacement_d2_083):
    feature = _clean(dv_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_083'] = {'inputs': ['dv_replacement_d2_083'], 'func': dv_replacement_d3_083}


def dv_replacement_d3_084(dv_replacement_d2_084):
    feature = _clean(dv_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_084'] = {'inputs': ['dv_replacement_d2_084'], 'func': dv_replacement_d3_084}


def dv_replacement_d3_085(dv_replacement_d2_085):
    feature = _clean(dv_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_085'] = {'inputs': ['dv_replacement_d2_085'], 'func': dv_replacement_d3_085}


def dv_replacement_d3_086(dv_replacement_d2_086):
    feature = _clean(dv_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_086'] = {'inputs': ['dv_replacement_d2_086'], 'func': dv_replacement_d3_086}


def dv_replacement_d3_087(dv_replacement_d2_087):
    feature = _clean(dv_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_087'] = {'inputs': ['dv_replacement_d2_087'], 'func': dv_replacement_d3_087}


def dv_replacement_d3_088(dv_replacement_d2_088):
    feature = _clean(dv_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_088'] = {'inputs': ['dv_replacement_d2_088'], 'func': dv_replacement_d3_088}


def dv_replacement_d3_089(dv_replacement_d2_089):
    feature = _clean(dv_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_089'] = {'inputs': ['dv_replacement_d2_089'], 'func': dv_replacement_d3_089}


def dv_replacement_d3_090(dv_replacement_d2_090):
    feature = _clean(dv_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_090'] = {'inputs': ['dv_replacement_d2_090'], 'func': dv_replacement_d3_090}


def dv_replacement_d3_091(dv_replacement_d2_091):
    feature = _clean(dv_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_091'] = {'inputs': ['dv_replacement_d2_091'], 'func': dv_replacement_d3_091}


def dv_replacement_d3_092(dv_replacement_d2_092):
    feature = _clean(dv_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_092'] = {'inputs': ['dv_replacement_d2_092'], 'func': dv_replacement_d3_092}


def dv_replacement_d3_093(dv_replacement_d2_093):
    feature = _clean(dv_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_093'] = {'inputs': ['dv_replacement_d2_093'], 'func': dv_replacement_d3_093}


def dv_replacement_d3_094(dv_replacement_d2_094):
    feature = _clean(dv_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_094'] = {'inputs': ['dv_replacement_d2_094'], 'func': dv_replacement_d3_094}


def dv_replacement_d3_095(dv_replacement_d2_095):
    feature = _clean(dv_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_095'] = {'inputs': ['dv_replacement_d2_095'], 'func': dv_replacement_d3_095}


def dv_replacement_d3_096(dv_replacement_d2_096):
    feature = _clean(dv_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_096'] = {'inputs': ['dv_replacement_d2_096'], 'func': dv_replacement_d3_096}


def dv_replacement_d3_097(dv_replacement_d2_097):
    feature = _clean(dv_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_097'] = {'inputs': ['dv_replacement_d2_097'], 'func': dv_replacement_d3_097}


def dv_replacement_d3_098(dv_replacement_d2_098):
    feature = _clean(dv_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_098'] = {'inputs': ['dv_replacement_d2_098'], 'func': dv_replacement_d3_098}


def dv_replacement_d3_099(dv_replacement_d2_099):
    feature = _clean(dv_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_099'] = {'inputs': ['dv_replacement_d2_099'], 'func': dv_replacement_d3_099}


def dv_replacement_d3_100(dv_replacement_d2_100):
    feature = _clean(dv_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_100'] = {'inputs': ['dv_replacement_d2_100'], 'func': dv_replacement_d3_100}


def dv_replacement_d3_101(dv_replacement_d2_101):
    feature = _clean(dv_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_101'] = {'inputs': ['dv_replacement_d2_101'], 'func': dv_replacement_d3_101}


def dv_replacement_d3_102(dv_replacement_d2_102):
    feature = _clean(dv_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_102'] = {'inputs': ['dv_replacement_d2_102'], 'func': dv_replacement_d3_102}


def dv_replacement_d3_103(dv_replacement_d2_103):
    feature = _clean(dv_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_103'] = {'inputs': ['dv_replacement_d2_103'], 'func': dv_replacement_d3_103}


def dv_replacement_d3_104(dv_replacement_d2_104):
    feature = _clean(dv_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_104'] = {'inputs': ['dv_replacement_d2_104'], 'func': dv_replacement_d3_104}


def dv_replacement_d3_105(dv_replacement_d2_105):
    feature = _clean(dv_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_105'] = {'inputs': ['dv_replacement_d2_105'], 'func': dv_replacement_d3_105}


def dv_replacement_d3_106(dv_replacement_d2_106):
    feature = _clean(dv_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_106'] = {'inputs': ['dv_replacement_d2_106'], 'func': dv_replacement_d3_106}


def dv_replacement_d3_107(dv_replacement_d2_107):
    feature = _clean(dv_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_107'] = {'inputs': ['dv_replacement_d2_107'], 'func': dv_replacement_d3_107}


def dv_replacement_d3_108(dv_replacement_d2_108):
    feature = _clean(dv_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_108'] = {'inputs': ['dv_replacement_d2_108'], 'func': dv_replacement_d3_108}


def dv_replacement_d3_109(dv_replacement_d2_109):
    feature = _clean(dv_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_109'] = {'inputs': ['dv_replacement_d2_109'], 'func': dv_replacement_d3_109}


def dv_replacement_d3_110(dv_replacement_d2_110):
    feature = _clean(dv_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_110'] = {'inputs': ['dv_replacement_d2_110'], 'func': dv_replacement_d3_110}


def dv_replacement_d3_111(dv_replacement_d2_111):
    feature = _clean(dv_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_111'] = {'inputs': ['dv_replacement_d2_111'], 'func': dv_replacement_d3_111}


def dv_replacement_d3_112(dv_replacement_d2_112):
    feature = _clean(dv_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_112'] = {'inputs': ['dv_replacement_d2_112'], 'func': dv_replacement_d3_112}


def dv_replacement_d3_113(dv_replacement_d2_113):
    feature = _clean(dv_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_113'] = {'inputs': ['dv_replacement_d2_113'], 'func': dv_replacement_d3_113}


def dv_replacement_d3_114(dv_replacement_d2_114):
    feature = _clean(dv_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_114'] = {'inputs': ['dv_replacement_d2_114'], 'func': dv_replacement_d3_114}


def dv_replacement_d3_115(dv_replacement_d2_115):
    feature = _clean(dv_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_115'] = {'inputs': ['dv_replacement_d2_115'], 'func': dv_replacement_d3_115}


def dv_replacement_d3_116(dv_replacement_d2_116):
    feature = _clean(dv_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_116'] = {'inputs': ['dv_replacement_d2_116'], 'func': dv_replacement_d3_116}


def dv_replacement_d3_117(dv_replacement_d2_117):
    feature = _clean(dv_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_117'] = {'inputs': ['dv_replacement_d2_117'], 'func': dv_replacement_d3_117}


def dv_replacement_d3_118(dv_replacement_d2_118):
    feature = _clean(dv_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_118'] = {'inputs': ['dv_replacement_d2_118'], 'func': dv_replacement_d3_118}


def dv_replacement_d3_119(dv_replacement_d2_119):
    feature = _clean(dv_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_119'] = {'inputs': ['dv_replacement_d2_119'], 'func': dv_replacement_d3_119}


def dv_replacement_d3_120(dv_replacement_d2_120):
    feature = _clean(dv_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_120'] = {'inputs': ['dv_replacement_d2_120'], 'func': dv_replacement_d3_120}


def dv_replacement_d3_121(dv_replacement_d2_121):
    feature = _clean(dv_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_121'] = {'inputs': ['dv_replacement_d2_121'], 'func': dv_replacement_d3_121}


def dv_replacement_d3_122(dv_replacement_d2_122):
    feature = _clean(dv_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_122'] = {'inputs': ['dv_replacement_d2_122'], 'func': dv_replacement_d3_122}


def dv_replacement_d3_123(dv_replacement_d2_123):
    feature = _clean(dv_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_123'] = {'inputs': ['dv_replacement_d2_123'], 'func': dv_replacement_d3_123}


def dv_replacement_d3_124(dv_replacement_d2_124):
    feature = _clean(dv_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_124'] = {'inputs': ['dv_replacement_d2_124'], 'func': dv_replacement_d3_124}


def dv_replacement_d3_125(dv_replacement_d2_125):
    feature = _clean(dv_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_125'] = {'inputs': ['dv_replacement_d2_125'], 'func': dv_replacement_d3_125}


def dv_replacement_d3_126(dv_replacement_d2_126):
    feature = _clean(dv_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_126'] = {'inputs': ['dv_replacement_d2_126'], 'func': dv_replacement_d3_126}


def dv_replacement_d3_127(dv_replacement_d2_127):
    feature = _clean(dv_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_127'] = {'inputs': ['dv_replacement_d2_127'], 'func': dv_replacement_d3_127}


def dv_replacement_d3_128(dv_replacement_d2_128):
    feature = _clean(dv_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_128'] = {'inputs': ['dv_replacement_d2_128'], 'func': dv_replacement_d3_128}


def dv_replacement_d3_129(dv_replacement_d2_129):
    feature = _clean(dv_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_129'] = {'inputs': ['dv_replacement_d2_129'], 'func': dv_replacement_d3_129}


def dv_replacement_d3_130(dv_replacement_d2_130):
    feature = _clean(dv_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_130'] = {'inputs': ['dv_replacement_d2_130'], 'func': dv_replacement_d3_130}


def dv_replacement_d3_131(dv_replacement_d2_131):
    feature = _clean(dv_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_131'] = {'inputs': ['dv_replacement_d2_131'], 'func': dv_replacement_d3_131}


def dv_replacement_d3_132(dv_replacement_d2_132):
    feature = _clean(dv_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_132'] = {'inputs': ['dv_replacement_d2_132'], 'func': dv_replacement_d3_132}


def dv_replacement_d3_133(dv_replacement_d2_133):
    feature = _clean(dv_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_133'] = {'inputs': ['dv_replacement_d2_133'], 'func': dv_replacement_d3_133}


def dv_replacement_d3_134(dv_replacement_d2_134):
    feature = _clean(dv_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_134'] = {'inputs': ['dv_replacement_d2_134'], 'func': dv_replacement_d3_134}


def dv_replacement_d3_135(dv_replacement_d2_135):
    feature = _clean(dv_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_135'] = {'inputs': ['dv_replacement_d2_135'], 'func': dv_replacement_d3_135}


def dv_replacement_d3_136(dv_replacement_d2_136):
    feature = _clean(dv_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_136'] = {'inputs': ['dv_replacement_d2_136'], 'func': dv_replacement_d3_136}


def dv_replacement_d3_137(dv_replacement_d2_137):
    feature = _clean(dv_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_137'] = {'inputs': ['dv_replacement_d2_137'], 'func': dv_replacement_d3_137}


def dv_replacement_d3_138(dv_replacement_d2_138):
    feature = _clean(dv_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_138'] = {'inputs': ['dv_replacement_d2_138'], 'func': dv_replacement_d3_138}


def dv_replacement_d3_139(dv_replacement_d2_139):
    feature = _clean(dv_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_139'] = {'inputs': ['dv_replacement_d2_139'], 'func': dv_replacement_d3_139}


def dv_replacement_d3_140(dv_replacement_d2_140):
    feature = _clean(dv_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_140'] = {'inputs': ['dv_replacement_d2_140'], 'func': dv_replacement_d3_140}


def dv_replacement_d3_141(dv_replacement_d2_141):
    feature = _clean(dv_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_141'] = {'inputs': ['dv_replacement_d2_141'], 'func': dv_replacement_d3_141}


def dv_replacement_d3_142(dv_replacement_d2_142):
    feature = _clean(dv_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_142'] = {'inputs': ['dv_replacement_d2_142'], 'func': dv_replacement_d3_142}


def dv_replacement_d3_143(dv_replacement_d2_143):
    feature = _clean(dv_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_143'] = {'inputs': ['dv_replacement_d2_143'], 'func': dv_replacement_d3_143}


def dv_replacement_d3_144(dv_replacement_d2_144):
    feature = _clean(dv_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_144'] = {'inputs': ['dv_replacement_d2_144'], 'func': dv_replacement_d3_144}


def dv_replacement_d3_145(dv_replacement_d2_145):
    feature = _clean(dv_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_145'] = {'inputs': ['dv_replacement_d2_145'], 'func': dv_replacement_d3_145}


def dv_replacement_d3_146(dv_replacement_d2_146):
    feature = _clean(dv_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_146'] = {'inputs': ['dv_replacement_d2_146'], 'func': dv_replacement_d3_146}


def dv_replacement_d3_147(dv_replacement_d2_147):
    feature = _clean(dv_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_147'] = {'inputs': ['dv_replacement_d2_147'], 'func': dv_replacement_d3_147}


def dv_replacement_d3_148(dv_replacement_d2_148):
    feature = _clean(dv_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_148'] = {'inputs': ['dv_replacement_d2_148'], 'func': dv_replacement_d3_148}


def dv_replacement_d3_149(dv_replacement_d2_149):
    feature = _clean(dv_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_149'] = {'inputs': ['dv_replacement_d2_149'], 'func': dv_replacement_d3_149}


def dv_replacement_d3_150(dv_replacement_d2_150):
    feature = _clean(dv_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_150'] = {'inputs': ['dv_replacement_d2_150'], 'func': dv_replacement_d3_150}


def dv_replacement_d3_151(dv_replacement_d2_151):
    feature = _clean(dv_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_151'] = {'inputs': ['dv_replacement_d2_151'], 'func': dv_replacement_d3_151}


def dv_replacement_d3_152(dv_replacement_d2_152):
    feature = _clean(dv_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_152'] = {'inputs': ['dv_replacement_d2_152'], 'func': dv_replacement_d3_152}


def dv_replacement_d3_153(dv_replacement_d2_153):
    feature = _clean(dv_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_153'] = {'inputs': ['dv_replacement_d2_153'], 'func': dv_replacement_d3_153}


def dv_replacement_d3_154(dv_replacement_d2_154):
    feature = _clean(dv_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_154'] = {'inputs': ['dv_replacement_d2_154'], 'func': dv_replacement_d3_154}


def dv_replacement_d3_155(dv_replacement_d2_155):
    feature = _clean(dv_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_155'] = {'inputs': ['dv_replacement_d2_155'], 'func': dv_replacement_d3_155}


def dv_replacement_d3_156(dv_replacement_d2_156):
    feature = _clean(dv_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_156'] = {'inputs': ['dv_replacement_d2_156'], 'func': dv_replacement_d3_156}


def dv_replacement_d3_157(dv_replacement_d2_157):
    feature = _clean(dv_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_157'] = {'inputs': ['dv_replacement_d2_157'], 'func': dv_replacement_d3_157}


def dv_replacement_d3_158(dv_replacement_d2_158):
    feature = _clean(dv_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_158'] = {'inputs': ['dv_replacement_d2_158'], 'func': dv_replacement_d3_158}


def dv_replacement_d3_159(dv_replacement_d2_159):
    feature = _clean(dv_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_159'] = {'inputs': ['dv_replacement_d2_159'], 'func': dv_replacement_d3_159}


def dv_replacement_d3_160(dv_replacement_d2_160):
    feature = _clean(dv_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_160'] = {'inputs': ['dv_replacement_d2_160'], 'func': dv_replacement_d3_160}


def dv_replacement_d3_161(dv_replacement_d2_161):
    feature = _clean(dv_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_161'] = {'inputs': ['dv_replacement_d2_161'], 'func': dv_replacement_d3_161}


def dv_replacement_d3_162(dv_replacement_d2_162):
    feature = _clean(dv_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_162'] = {'inputs': ['dv_replacement_d2_162'], 'func': dv_replacement_d3_162}


def dv_replacement_d3_163(dv_replacement_d2_163):
    feature = _clean(dv_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_163'] = {'inputs': ['dv_replacement_d2_163'], 'func': dv_replacement_d3_163}


def dv_replacement_d3_164(dv_replacement_d2_164):
    feature = _clean(dv_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_164'] = {'inputs': ['dv_replacement_d2_164'], 'func': dv_replacement_d3_164}


def dv_replacement_d3_165(dv_replacement_d2_165):
    feature = _clean(dv_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_165'] = {'inputs': ['dv_replacement_d2_165'], 'func': dv_replacement_d3_165}


def dv_replacement_d3_166(dv_replacement_d2_166):
    feature = _clean(dv_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_166'] = {'inputs': ['dv_replacement_d2_166'], 'func': dv_replacement_d3_166}


def dv_replacement_d3_167(dv_replacement_d2_167):
    feature = _clean(dv_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_167'] = {'inputs': ['dv_replacement_d2_167'], 'func': dv_replacement_d3_167}


def dv_replacement_d3_168(dv_replacement_d2_168):
    feature = _clean(dv_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_168'] = {'inputs': ['dv_replacement_d2_168'], 'func': dv_replacement_d3_168}


def dv_replacement_d3_169(dv_replacement_d2_169):
    feature = _clean(dv_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_169'] = {'inputs': ['dv_replacement_d2_169'], 'func': dv_replacement_d3_169}


def dv_replacement_d3_170(dv_replacement_d2_170):
    feature = _clean(dv_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
DV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dv_replacement_d3_170'] = {'inputs': ['dv_replacement_d2_170'], 'func': dv_replacement_d3_170}


# Third-derivative extensions for repaired first-base features.
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def dvel_base_universe_d3_001_dvel_002_low_distance_10_002(dvel_base_universe_d2_001_dvel_002_low_distance_10_002):
    return _base_universe_d3(dvel_base_universe_d2_001_dvel_002_low_distance_10_002, 1)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_001_dvel_002_low_distance_10_002'] = {'inputs': ['dvel_base_universe_d2_001_dvel_002_low_distance_10_002'], 'func': dvel_base_universe_d3_001_dvel_002_low_distance_10_002}


def dvel_base_universe_d3_002_dvel_003_underwater_area_21_003(dvel_base_universe_d2_002_dvel_003_underwater_area_21_003):
    return _base_universe_d3(dvel_base_universe_d2_002_dvel_003_underwater_area_21_003, 2)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_002_dvel_003_underwater_area_21_003'] = {'inputs': ['dvel_base_universe_d2_002_dvel_003_underwater_area_21_003'], 'func': dvel_base_universe_d3_002_dvel_003_underwater_area_21_003}


def dvel_base_universe_d3_003_dvel_006_lower_high_ratio_84_006(dvel_base_universe_d2_003_dvel_006_lower_high_ratio_84_006):
    return _base_universe_d3(dvel_base_universe_d2_003_dvel_006_lower_high_ratio_84_006, 3)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_003_dvel_006_lower_high_ratio_84_006'] = {'inputs': ['dvel_base_universe_d2_003_dvel_006_lower_high_ratio_84_006'], 'func': dvel_base_universe_d3_003_dvel_006_lower_high_ratio_84_006}


def dvel_base_universe_d3_004_dvel_008_low_distance_189_008(dvel_base_universe_d2_004_dvel_008_low_distance_189_008):
    return _base_universe_d3(dvel_base_universe_d2_004_dvel_008_low_distance_189_008, 4)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_004_dvel_008_low_distance_189_008'] = {'inputs': ['dvel_base_universe_d2_004_dvel_008_low_distance_189_008'], 'func': dvel_base_universe_d3_004_dvel_008_low_distance_189_008}


def dvel_base_universe_d3_005_dvel_009_underwater_area_252_009(dvel_base_universe_d2_005_dvel_009_underwater_area_252_009):
    return _base_universe_d3(dvel_base_universe_d2_005_dvel_009_underwater_area_252_009, 5)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_005_dvel_009_underwater_area_252_009'] = {'inputs': ['dvel_base_universe_d2_005_dvel_009_underwater_area_252_009'], 'func': dvel_base_universe_d3_005_dvel_009_underwater_area_252_009}


def dvel_base_universe_d3_006_dvel_012_lower_high_ratio_756_012(dvel_base_universe_d2_006_dvel_012_lower_high_ratio_756_012):
    return _base_universe_d3(dvel_base_universe_d2_006_dvel_012_lower_high_ratio_756_012, 6)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_006_dvel_012_lower_high_ratio_756_012'] = {'inputs': ['dvel_base_universe_d2_006_dvel_012_lower_high_ratio_756_012'], 'func': dvel_base_universe_d3_006_dvel_012_lower_high_ratio_756_012}


def dvel_base_universe_d3_007_dvel_014_low_distance_1260_014(dvel_base_universe_d2_007_dvel_014_low_distance_1260_014):
    return _base_universe_d3(dvel_base_universe_d2_007_dvel_014_low_distance_1260_014, 7)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_007_dvel_014_low_distance_1260_014'] = {'inputs': ['dvel_base_universe_d2_007_dvel_014_low_distance_1260_014'], 'func': dvel_base_universe_d3_007_dvel_014_low_distance_1260_014}


def dvel_base_universe_d3_008_dvel_015_underwater_area_1512_015(dvel_base_universe_d2_008_dvel_015_underwater_area_1512_015):
    return _base_universe_d3(dvel_base_universe_d2_008_dvel_015_underwater_area_1512_015, 8)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_008_dvel_015_underwater_area_1512_015'] = {'inputs': ['dvel_base_universe_d2_008_dvel_015_underwater_area_1512_015'], 'func': dvel_base_universe_d3_008_dvel_015_underwater_area_1512_015}


def dvel_base_universe_d3_009_dvel_018_lower_high_ratio_21_018(dvel_base_universe_d2_009_dvel_018_lower_high_ratio_21_018):
    return _base_universe_d3(dvel_base_universe_d2_009_dvel_018_lower_high_ratio_21_018, 9)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_009_dvel_018_lower_high_ratio_21_018'] = {'inputs': ['dvel_base_universe_d2_009_dvel_018_lower_high_ratio_21_018'], 'func': dvel_base_universe_d3_009_dvel_018_lower_high_ratio_21_018}


def dvel_base_universe_d3_010_dvel_020_low_distance_63_020(dvel_base_universe_d2_010_dvel_020_low_distance_63_020):
    return _base_universe_d3(dvel_base_universe_d2_010_dvel_020_low_distance_63_020, 10)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_010_dvel_020_low_distance_63_020'] = {'inputs': ['dvel_base_universe_d2_010_dvel_020_low_distance_63_020'], 'func': dvel_base_universe_d3_010_dvel_020_low_distance_63_020}


def dvel_base_universe_d3_011_dvel_021_underwater_area_84_021(dvel_base_universe_d2_011_dvel_021_underwater_area_84_021):
    return _base_universe_d3(dvel_base_universe_d2_011_dvel_021_underwater_area_84_021, 11)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_011_dvel_021_underwater_area_84_021'] = {'inputs': ['dvel_base_universe_d2_011_dvel_021_underwater_area_84_021'], 'func': dvel_base_universe_d3_011_dvel_021_underwater_area_84_021}


def dvel_base_universe_d3_012_dvel_024_lower_high_ratio_252_024(dvel_base_universe_d2_012_dvel_024_lower_high_ratio_252_024):
    return _base_universe_d3(dvel_base_universe_d2_012_dvel_024_lower_high_ratio_252_024, 12)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_012_dvel_024_lower_high_ratio_252_024'] = {'inputs': ['dvel_base_universe_d2_012_dvel_024_lower_high_ratio_252_024'], 'func': dvel_base_universe_d3_012_dvel_024_lower_high_ratio_252_024}


def dvel_base_universe_d3_013_dvel_026_low_distance_504_026(dvel_base_universe_d2_013_dvel_026_low_distance_504_026):
    return _base_universe_d3(dvel_base_universe_d2_013_dvel_026_low_distance_504_026, 13)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_013_dvel_026_low_distance_504_026'] = {'inputs': ['dvel_base_universe_d2_013_dvel_026_low_distance_504_026'], 'func': dvel_base_universe_d3_013_dvel_026_low_distance_504_026}


def dvel_base_universe_d3_014_dvel_027_underwater_area_756_027(dvel_base_universe_d2_014_dvel_027_underwater_area_756_027):
    return _base_universe_d3(dvel_base_universe_d2_014_dvel_027_underwater_area_756_027, 14)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_014_dvel_027_underwater_area_756_027'] = {'inputs': ['dvel_base_universe_d2_014_dvel_027_underwater_area_756_027'], 'func': dvel_base_universe_d3_014_dvel_027_underwater_area_756_027}


def dvel_base_universe_d3_015_dvel_030_lower_high_ratio_1512_030(dvel_base_universe_d2_015_dvel_030_lower_high_ratio_1512_030):
    return _base_universe_d3(dvel_base_universe_d2_015_dvel_030_lower_high_ratio_1512_030, 15)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_015_dvel_030_lower_high_ratio_1512_030'] = {'inputs': ['dvel_base_universe_d2_015_dvel_030_lower_high_ratio_1512_030'], 'func': dvel_base_universe_d3_015_dvel_030_lower_high_ratio_1512_030}


def dvel_base_universe_d3_016_dvel_basefill_004(dvel_base_universe_d2_016_dvel_basefill_004):
    return _base_universe_d3(dvel_base_universe_d2_016_dvel_basefill_004, 16)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_016_dvel_basefill_004'] = {'inputs': ['dvel_base_universe_d2_016_dvel_basefill_004'], 'func': dvel_base_universe_d3_016_dvel_basefill_004}


def dvel_base_universe_d3_017_dvel_basefill_005(dvel_base_universe_d2_017_dvel_basefill_005):
    return _base_universe_d3(dvel_base_universe_d2_017_dvel_basefill_005, 17)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_017_dvel_basefill_005'] = {'inputs': ['dvel_base_universe_d2_017_dvel_basefill_005'], 'func': dvel_base_universe_d3_017_dvel_basefill_005}


def dvel_base_universe_d3_018_dvel_basefill_010(dvel_base_universe_d2_018_dvel_basefill_010):
    return _base_universe_d3(dvel_base_universe_d2_018_dvel_basefill_010, 18)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_018_dvel_basefill_010'] = {'inputs': ['dvel_base_universe_d2_018_dvel_basefill_010'], 'func': dvel_base_universe_d3_018_dvel_basefill_010}


def dvel_base_universe_d3_019_dvel_basefill_011(dvel_base_universe_d2_019_dvel_basefill_011):
    return _base_universe_d3(dvel_base_universe_d2_019_dvel_basefill_011, 19)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_019_dvel_basefill_011'] = {'inputs': ['dvel_base_universe_d2_019_dvel_basefill_011'], 'func': dvel_base_universe_d3_019_dvel_basefill_011}


def dvel_base_universe_d3_020_dvel_basefill_016(dvel_base_universe_d2_020_dvel_basefill_016):
    return _base_universe_d3(dvel_base_universe_d2_020_dvel_basefill_016, 20)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_020_dvel_basefill_016'] = {'inputs': ['dvel_base_universe_d2_020_dvel_basefill_016'], 'func': dvel_base_universe_d3_020_dvel_basefill_016}


def dvel_base_universe_d3_021_dvel_basefill_017(dvel_base_universe_d2_021_dvel_basefill_017):
    return _base_universe_d3(dvel_base_universe_d2_021_dvel_basefill_017, 21)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_021_dvel_basefill_017'] = {'inputs': ['dvel_base_universe_d2_021_dvel_basefill_017'], 'func': dvel_base_universe_d3_021_dvel_basefill_017}


def dvel_base_universe_d3_022_dvel_basefill_022(dvel_base_universe_d2_022_dvel_basefill_022):
    return _base_universe_d3(dvel_base_universe_d2_022_dvel_basefill_022, 22)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_022_dvel_basefill_022'] = {'inputs': ['dvel_base_universe_d2_022_dvel_basefill_022'], 'func': dvel_base_universe_d3_022_dvel_basefill_022}


def dvel_base_universe_d3_023_dvel_basefill_023(dvel_base_universe_d2_023_dvel_basefill_023):
    return _base_universe_d3(dvel_base_universe_d2_023_dvel_basefill_023, 23)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_023_dvel_basefill_023'] = {'inputs': ['dvel_base_universe_d2_023_dvel_basefill_023'], 'func': dvel_base_universe_d3_023_dvel_basefill_023}


def dvel_base_universe_d3_024_dvel_basefill_028(dvel_base_universe_d2_024_dvel_basefill_028):
    return _base_universe_d3(dvel_base_universe_d2_024_dvel_basefill_028, 24)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_024_dvel_basefill_028'] = {'inputs': ['dvel_base_universe_d2_024_dvel_basefill_028'], 'func': dvel_base_universe_d3_024_dvel_basefill_028}


def dvel_base_universe_d3_025_dvel_basefill_029(dvel_base_universe_d2_025_dvel_basefill_029):
    return _base_universe_d3(dvel_base_universe_d2_025_dvel_basefill_029, 25)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_025_dvel_basefill_029'] = {'inputs': ['dvel_base_universe_d2_025_dvel_basefill_029'], 'func': dvel_base_universe_d3_025_dvel_basefill_029}


def dvel_base_universe_d3_026_dvel_basefill_031(dvel_base_universe_d2_026_dvel_basefill_031):
    return _base_universe_d3(dvel_base_universe_d2_026_dvel_basefill_031, 26)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_026_dvel_basefill_031'] = {'inputs': ['dvel_base_universe_d2_026_dvel_basefill_031'], 'func': dvel_base_universe_d3_026_dvel_basefill_031}


def dvel_base_universe_d3_027_dvel_basefill_032(dvel_base_universe_d2_027_dvel_basefill_032):
    return _base_universe_d3(dvel_base_universe_d2_027_dvel_basefill_032, 27)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_027_dvel_basefill_032'] = {'inputs': ['dvel_base_universe_d2_027_dvel_basefill_032'], 'func': dvel_base_universe_d3_027_dvel_basefill_032}


def dvel_base_universe_d3_028_dvel_basefill_033(dvel_base_universe_d2_028_dvel_basefill_033):
    return _base_universe_d3(dvel_base_universe_d2_028_dvel_basefill_033, 28)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_028_dvel_basefill_033'] = {'inputs': ['dvel_base_universe_d2_028_dvel_basefill_033'], 'func': dvel_base_universe_d3_028_dvel_basefill_033}


def dvel_base_universe_d3_029_dvel_basefill_034(dvel_base_universe_d2_029_dvel_basefill_034):
    return _base_universe_d3(dvel_base_universe_d2_029_dvel_basefill_034, 29)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_029_dvel_basefill_034'] = {'inputs': ['dvel_base_universe_d2_029_dvel_basefill_034'], 'func': dvel_base_universe_d3_029_dvel_basefill_034}


def dvel_base_universe_d3_030_dvel_basefill_035(dvel_base_universe_d2_030_dvel_basefill_035):
    return _base_universe_d3(dvel_base_universe_d2_030_dvel_basefill_035, 30)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_030_dvel_basefill_035'] = {'inputs': ['dvel_base_universe_d2_030_dvel_basefill_035'], 'func': dvel_base_universe_d3_030_dvel_basefill_035}


def dvel_base_universe_d3_031_dvel_basefill_036(dvel_base_universe_d2_031_dvel_basefill_036):
    return _base_universe_d3(dvel_base_universe_d2_031_dvel_basefill_036, 31)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_031_dvel_basefill_036'] = {'inputs': ['dvel_base_universe_d2_031_dvel_basefill_036'], 'func': dvel_base_universe_d3_031_dvel_basefill_036}


def dvel_base_universe_d3_032_dvel_basefill_037(dvel_base_universe_d2_032_dvel_basefill_037):
    return _base_universe_d3(dvel_base_universe_d2_032_dvel_basefill_037, 32)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_032_dvel_basefill_037'] = {'inputs': ['dvel_base_universe_d2_032_dvel_basefill_037'], 'func': dvel_base_universe_d3_032_dvel_basefill_037}


def dvel_base_universe_d3_033_dvel_basefill_038(dvel_base_universe_d2_033_dvel_basefill_038):
    return _base_universe_d3(dvel_base_universe_d2_033_dvel_basefill_038, 33)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_033_dvel_basefill_038'] = {'inputs': ['dvel_base_universe_d2_033_dvel_basefill_038'], 'func': dvel_base_universe_d3_033_dvel_basefill_038}


def dvel_base_universe_d3_034_dvel_basefill_039(dvel_base_universe_d2_034_dvel_basefill_039):
    return _base_universe_d3(dvel_base_universe_d2_034_dvel_basefill_039, 34)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_034_dvel_basefill_039'] = {'inputs': ['dvel_base_universe_d2_034_dvel_basefill_039'], 'func': dvel_base_universe_d3_034_dvel_basefill_039}


def dvel_base_universe_d3_035_dvel_basefill_040(dvel_base_universe_d2_035_dvel_basefill_040):
    return _base_universe_d3(dvel_base_universe_d2_035_dvel_basefill_040, 35)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_035_dvel_basefill_040'] = {'inputs': ['dvel_base_universe_d2_035_dvel_basefill_040'], 'func': dvel_base_universe_d3_035_dvel_basefill_040}


def dvel_base_universe_d3_036_dvel_basefill_041(dvel_base_universe_d2_036_dvel_basefill_041):
    return _base_universe_d3(dvel_base_universe_d2_036_dvel_basefill_041, 36)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_036_dvel_basefill_041'] = {'inputs': ['dvel_base_universe_d2_036_dvel_basefill_041'], 'func': dvel_base_universe_d3_036_dvel_basefill_041}


def dvel_base_universe_d3_037_dvel_basefill_042(dvel_base_universe_d2_037_dvel_basefill_042):
    return _base_universe_d3(dvel_base_universe_d2_037_dvel_basefill_042, 37)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_037_dvel_basefill_042'] = {'inputs': ['dvel_base_universe_d2_037_dvel_basefill_042'], 'func': dvel_base_universe_d3_037_dvel_basefill_042}


def dvel_base_universe_d3_038_dvel_basefill_043(dvel_base_universe_d2_038_dvel_basefill_043):
    return _base_universe_d3(dvel_base_universe_d2_038_dvel_basefill_043, 38)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_038_dvel_basefill_043'] = {'inputs': ['dvel_base_universe_d2_038_dvel_basefill_043'], 'func': dvel_base_universe_d3_038_dvel_basefill_043}


def dvel_base_universe_d3_039_dvel_basefill_044(dvel_base_universe_d2_039_dvel_basefill_044):
    return _base_universe_d3(dvel_base_universe_d2_039_dvel_basefill_044, 39)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_039_dvel_basefill_044'] = {'inputs': ['dvel_base_universe_d2_039_dvel_basefill_044'], 'func': dvel_base_universe_d3_039_dvel_basefill_044}


def dvel_base_universe_d3_040_dvel_basefill_045(dvel_base_universe_d2_040_dvel_basefill_045):
    return _base_universe_d3(dvel_base_universe_d2_040_dvel_basefill_045, 40)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_040_dvel_basefill_045'] = {'inputs': ['dvel_base_universe_d2_040_dvel_basefill_045'], 'func': dvel_base_universe_d3_040_dvel_basefill_045}


def dvel_base_universe_d3_041_dvel_basefill_046(dvel_base_universe_d2_041_dvel_basefill_046):
    return _base_universe_d3(dvel_base_universe_d2_041_dvel_basefill_046, 41)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_041_dvel_basefill_046'] = {'inputs': ['dvel_base_universe_d2_041_dvel_basefill_046'], 'func': dvel_base_universe_d3_041_dvel_basefill_046}


def dvel_base_universe_d3_042_dvel_basefill_047(dvel_base_universe_d2_042_dvel_basefill_047):
    return _base_universe_d3(dvel_base_universe_d2_042_dvel_basefill_047, 42)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_042_dvel_basefill_047'] = {'inputs': ['dvel_base_universe_d2_042_dvel_basefill_047'], 'func': dvel_base_universe_d3_042_dvel_basefill_047}


def dvel_base_universe_d3_043_dvel_basefill_048(dvel_base_universe_d2_043_dvel_basefill_048):
    return _base_universe_d3(dvel_base_universe_d2_043_dvel_basefill_048, 43)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_043_dvel_basefill_048'] = {'inputs': ['dvel_base_universe_d2_043_dvel_basefill_048'], 'func': dvel_base_universe_d3_043_dvel_basefill_048}


def dvel_base_universe_d3_044_dvel_basefill_049(dvel_base_universe_d2_044_dvel_basefill_049):
    return _base_universe_d3(dvel_base_universe_d2_044_dvel_basefill_049, 44)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_044_dvel_basefill_049'] = {'inputs': ['dvel_base_universe_d2_044_dvel_basefill_049'], 'func': dvel_base_universe_d3_044_dvel_basefill_049}


def dvel_base_universe_d3_045_dvel_basefill_050(dvel_base_universe_d2_045_dvel_basefill_050):
    return _base_universe_d3(dvel_base_universe_d2_045_dvel_basefill_050, 45)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_045_dvel_basefill_050'] = {'inputs': ['dvel_base_universe_d2_045_dvel_basefill_050'], 'func': dvel_base_universe_d3_045_dvel_basefill_050}


def dvel_base_universe_d3_046_dvel_basefill_051(dvel_base_universe_d2_046_dvel_basefill_051):
    return _base_universe_d3(dvel_base_universe_d2_046_dvel_basefill_051, 46)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_046_dvel_basefill_051'] = {'inputs': ['dvel_base_universe_d2_046_dvel_basefill_051'], 'func': dvel_base_universe_d3_046_dvel_basefill_051}


def dvel_base_universe_d3_047_dvel_basefill_052(dvel_base_universe_d2_047_dvel_basefill_052):
    return _base_universe_d3(dvel_base_universe_d2_047_dvel_basefill_052, 47)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_047_dvel_basefill_052'] = {'inputs': ['dvel_base_universe_d2_047_dvel_basefill_052'], 'func': dvel_base_universe_d3_047_dvel_basefill_052}


def dvel_base_universe_d3_048_dvel_basefill_053(dvel_base_universe_d2_048_dvel_basefill_053):
    return _base_universe_d3(dvel_base_universe_d2_048_dvel_basefill_053, 48)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_048_dvel_basefill_053'] = {'inputs': ['dvel_base_universe_d2_048_dvel_basefill_053'], 'func': dvel_base_universe_d3_048_dvel_basefill_053}


def dvel_base_universe_d3_049_dvel_basefill_054(dvel_base_universe_d2_049_dvel_basefill_054):
    return _base_universe_d3(dvel_base_universe_d2_049_dvel_basefill_054, 49)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_049_dvel_basefill_054'] = {'inputs': ['dvel_base_universe_d2_049_dvel_basefill_054'], 'func': dvel_base_universe_d3_049_dvel_basefill_054}


def dvel_base_universe_d3_050_dvel_basefill_055(dvel_base_universe_d2_050_dvel_basefill_055):
    return _base_universe_d3(dvel_base_universe_d2_050_dvel_basefill_055, 50)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_050_dvel_basefill_055'] = {'inputs': ['dvel_base_universe_d2_050_dvel_basefill_055'], 'func': dvel_base_universe_d3_050_dvel_basefill_055}


def dvel_base_universe_d3_051_dvel_basefill_056(dvel_base_universe_d2_051_dvel_basefill_056):
    return _base_universe_d3(dvel_base_universe_d2_051_dvel_basefill_056, 51)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_051_dvel_basefill_056'] = {'inputs': ['dvel_base_universe_d2_051_dvel_basefill_056'], 'func': dvel_base_universe_d3_051_dvel_basefill_056}


def dvel_base_universe_d3_052_dvel_basefill_057(dvel_base_universe_d2_052_dvel_basefill_057):
    return _base_universe_d3(dvel_base_universe_d2_052_dvel_basefill_057, 52)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_052_dvel_basefill_057'] = {'inputs': ['dvel_base_universe_d2_052_dvel_basefill_057'], 'func': dvel_base_universe_d3_052_dvel_basefill_057}


def dvel_base_universe_d3_053_dvel_basefill_058(dvel_base_universe_d2_053_dvel_basefill_058):
    return _base_universe_d3(dvel_base_universe_d2_053_dvel_basefill_058, 53)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_053_dvel_basefill_058'] = {'inputs': ['dvel_base_universe_d2_053_dvel_basefill_058'], 'func': dvel_base_universe_d3_053_dvel_basefill_058}


def dvel_base_universe_d3_054_dvel_basefill_059(dvel_base_universe_d2_054_dvel_basefill_059):
    return _base_universe_d3(dvel_base_universe_d2_054_dvel_basefill_059, 54)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_054_dvel_basefill_059'] = {'inputs': ['dvel_base_universe_d2_054_dvel_basefill_059'], 'func': dvel_base_universe_d3_054_dvel_basefill_059}


def dvel_base_universe_d3_055_dvel_basefill_060(dvel_base_universe_d2_055_dvel_basefill_060):
    return _base_universe_d3(dvel_base_universe_d2_055_dvel_basefill_060, 55)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_055_dvel_basefill_060'] = {'inputs': ['dvel_base_universe_d2_055_dvel_basefill_060'], 'func': dvel_base_universe_d3_055_dvel_basefill_060}


def dvel_base_universe_d3_056_dvel_basefill_061(dvel_base_universe_d2_056_dvel_basefill_061):
    return _base_universe_d3(dvel_base_universe_d2_056_dvel_basefill_061, 56)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_056_dvel_basefill_061'] = {'inputs': ['dvel_base_universe_d2_056_dvel_basefill_061'], 'func': dvel_base_universe_d3_056_dvel_basefill_061}


def dvel_base_universe_d3_057_dvel_basefill_062(dvel_base_universe_d2_057_dvel_basefill_062):
    return _base_universe_d3(dvel_base_universe_d2_057_dvel_basefill_062, 57)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_057_dvel_basefill_062'] = {'inputs': ['dvel_base_universe_d2_057_dvel_basefill_062'], 'func': dvel_base_universe_d3_057_dvel_basefill_062}


def dvel_base_universe_d3_058_dvel_basefill_063(dvel_base_universe_d2_058_dvel_basefill_063):
    return _base_universe_d3(dvel_base_universe_d2_058_dvel_basefill_063, 58)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_058_dvel_basefill_063'] = {'inputs': ['dvel_base_universe_d2_058_dvel_basefill_063'], 'func': dvel_base_universe_d3_058_dvel_basefill_063}


def dvel_base_universe_d3_059_dvel_basefill_064(dvel_base_universe_d2_059_dvel_basefill_064):
    return _base_universe_d3(dvel_base_universe_d2_059_dvel_basefill_064, 59)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_059_dvel_basefill_064'] = {'inputs': ['dvel_base_universe_d2_059_dvel_basefill_064'], 'func': dvel_base_universe_d3_059_dvel_basefill_064}


def dvel_base_universe_d3_060_dvel_basefill_065(dvel_base_universe_d2_060_dvel_basefill_065):
    return _base_universe_d3(dvel_base_universe_d2_060_dvel_basefill_065, 60)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_060_dvel_basefill_065'] = {'inputs': ['dvel_base_universe_d2_060_dvel_basefill_065'], 'func': dvel_base_universe_d3_060_dvel_basefill_065}


def dvel_base_universe_d3_061_dvel_basefill_066(dvel_base_universe_d2_061_dvel_basefill_066):
    return _base_universe_d3(dvel_base_universe_d2_061_dvel_basefill_066, 61)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_061_dvel_basefill_066'] = {'inputs': ['dvel_base_universe_d2_061_dvel_basefill_066'], 'func': dvel_base_universe_d3_061_dvel_basefill_066}


def dvel_base_universe_d3_062_dvel_basefill_067(dvel_base_universe_d2_062_dvel_basefill_067):
    return _base_universe_d3(dvel_base_universe_d2_062_dvel_basefill_067, 62)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_062_dvel_basefill_067'] = {'inputs': ['dvel_base_universe_d2_062_dvel_basefill_067'], 'func': dvel_base_universe_d3_062_dvel_basefill_067}


def dvel_base_universe_d3_063_dvel_basefill_068(dvel_base_universe_d2_063_dvel_basefill_068):
    return _base_universe_d3(dvel_base_universe_d2_063_dvel_basefill_068, 63)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_063_dvel_basefill_068'] = {'inputs': ['dvel_base_universe_d2_063_dvel_basefill_068'], 'func': dvel_base_universe_d3_063_dvel_basefill_068}


def dvel_base_universe_d3_064_dvel_basefill_069(dvel_base_universe_d2_064_dvel_basefill_069):
    return _base_universe_d3(dvel_base_universe_d2_064_dvel_basefill_069, 64)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_064_dvel_basefill_069'] = {'inputs': ['dvel_base_universe_d2_064_dvel_basefill_069'], 'func': dvel_base_universe_d3_064_dvel_basefill_069}


def dvel_base_universe_d3_065_dvel_basefill_070(dvel_base_universe_d2_065_dvel_basefill_070):
    return _base_universe_d3(dvel_base_universe_d2_065_dvel_basefill_070, 65)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_065_dvel_basefill_070'] = {'inputs': ['dvel_base_universe_d2_065_dvel_basefill_070'], 'func': dvel_base_universe_d3_065_dvel_basefill_070}


def dvel_base_universe_d3_066_dvel_basefill_071(dvel_base_universe_d2_066_dvel_basefill_071):
    return _base_universe_d3(dvel_base_universe_d2_066_dvel_basefill_071, 66)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_066_dvel_basefill_071'] = {'inputs': ['dvel_base_universe_d2_066_dvel_basefill_071'], 'func': dvel_base_universe_d3_066_dvel_basefill_071}


def dvel_base_universe_d3_067_dvel_basefill_072(dvel_base_universe_d2_067_dvel_basefill_072):
    return _base_universe_d3(dvel_base_universe_d2_067_dvel_basefill_072, 67)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_067_dvel_basefill_072'] = {'inputs': ['dvel_base_universe_d2_067_dvel_basefill_072'], 'func': dvel_base_universe_d3_067_dvel_basefill_072}


def dvel_base_universe_d3_068_dvel_basefill_073(dvel_base_universe_d2_068_dvel_basefill_073):
    return _base_universe_d3(dvel_base_universe_d2_068_dvel_basefill_073, 68)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_068_dvel_basefill_073'] = {'inputs': ['dvel_base_universe_d2_068_dvel_basefill_073'], 'func': dvel_base_universe_d3_068_dvel_basefill_073}


def dvel_base_universe_d3_069_dvel_basefill_074(dvel_base_universe_d2_069_dvel_basefill_074):
    return _base_universe_d3(dvel_base_universe_d2_069_dvel_basefill_074, 69)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_069_dvel_basefill_074'] = {'inputs': ['dvel_base_universe_d2_069_dvel_basefill_074'], 'func': dvel_base_universe_d3_069_dvel_basefill_074}


def dvel_base_universe_d3_070_dvel_basefill_075(dvel_base_universe_d2_070_dvel_basefill_075):
    return _base_universe_d3(dvel_base_universe_d2_070_dvel_basefill_075, 70)
DVEL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvel_base_universe_d3_070_dvel_basefill_075'] = {'inputs': ['dvel_base_universe_d2_070_dvel_basefill_075'], 'func': dvel_base_universe_d3_070_dvel_basefill_075}
