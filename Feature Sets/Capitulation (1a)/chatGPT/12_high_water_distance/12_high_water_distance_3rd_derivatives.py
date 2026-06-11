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



def hwd_176_hwd_001_drawdown_from_high_5_001_accel_1(hwd_151_hwd_001_drawdown_from_high_5_001_roc_1):
    feature = _s(hwd_151_hwd_001_drawdown_from_high_5_001_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def hwd_177_hwd_007_drawdown_from_high_126_007_accel_5(hwd_152_hwd_007_drawdown_from_high_126_007_roc_5):
    feature = _s(hwd_152_hwd_007_drawdown_from_high_126_007_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def hwd_178_hwd_013_drawdown_from_high_1008_013_accel_42(hwd_153_hwd_013_drawdown_from_high_1008_013_roc_42):
    feature = _s(hwd_153_hwd_013_drawdown_from_high_1008_013_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def hwd_179_hwd_019_drawdown_from_high_42_019_accel_126(hwd_154_hwd_019_drawdown_from_high_42_019_roc_126):
    feature = _s(hwd_154_hwd_019_drawdown_from_high_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def hwd_180_hwd_025_drawdown_from_high_378_025_accel_378(hwd_155_hwd_025_drawdown_from_high_378_025_roc_378):
    feature = _s(hwd_155_hwd_025_drawdown_from_high_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















HIGH_WATER_DISTANCE_REGISTRY_3RD_DERIVATIVES = {
    'hwd_176_hwd_001_drawdown_from_high_5_001_accel_1': {'inputs': ['hwd_151_hwd_001_drawdown_from_high_5_001_roc_1'], 'func': hwd_176_hwd_001_drawdown_from_high_5_001_accel_1},
    'hwd_177_hwd_007_drawdown_from_high_126_007_accel_5': {'inputs': ['hwd_152_hwd_007_drawdown_from_high_126_007_roc_5'], 'func': hwd_177_hwd_007_drawdown_from_high_126_007_accel_5},
    'hwd_178_hwd_013_drawdown_from_high_1008_013_accel_42': {'inputs': ['hwd_153_hwd_013_drawdown_from_high_1008_013_roc_42'], 'func': hwd_178_hwd_013_drawdown_from_high_1008_013_accel_42},
    'hwd_179_hwd_019_drawdown_from_high_42_019_accel_126': {'inputs': ['hwd_154_hwd_019_drawdown_from_high_42_019_roc_126'], 'func': hwd_179_hwd_019_drawdown_from_high_42_019_accel_126},
    'hwd_180_hwd_025_drawdown_from_high_378_025_accel_378': {'inputs': ['hwd_155_hwd_025_drawdown_from_high_378_025_roc_378'], 'func': hwd_180_hwd_025_drawdown_from_high_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def hwd_replacement_d3_001(hwd_replacement_d2_001):
    feature = _clean(hwd_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_001'] = {'inputs': ['hwd_replacement_d2_001'], 'func': hwd_replacement_d3_001}


def hwd_replacement_d3_002(hwd_replacement_d2_002):
    feature = _clean(hwd_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_002'] = {'inputs': ['hwd_replacement_d2_002'], 'func': hwd_replacement_d3_002}


def hwd_replacement_d3_003(hwd_replacement_d2_003):
    feature = _clean(hwd_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_003'] = {'inputs': ['hwd_replacement_d2_003'], 'func': hwd_replacement_d3_003}


def hwd_replacement_d3_004(hwd_replacement_d2_004):
    feature = _clean(hwd_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_004'] = {'inputs': ['hwd_replacement_d2_004'], 'func': hwd_replacement_d3_004}


def hwd_replacement_d3_005(hwd_replacement_d2_005):
    feature = _clean(hwd_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_005'] = {'inputs': ['hwd_replacement_d2_005'], 'func': hwd_replacement_d3_005}


def hwd_replacement_d3_006(hwd_replacement_d2_006):
    feature = _clean(hwd_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_006'] = {'inputs': ['hwd_replacement_d2_006'], 'func': hwd_replacement_d3_006}


def hwd_replacement_d3_007(hwd_replacement_d2_007):
    feature = _clean(hwd_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_007'] = {'inputs': ['hwd_replacement_d2_007'], 'func': hwd_replacement_d3_007}


def hwd_replacement_d3_008(hwd_replacement_d2_008):
    feature = _clean(hwd_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_008'] = {'inputs': ['hwd_replacement_d2_008'], 'func': hwd_replacement_d3_008}


def hwd_replacement_d3_009(hwd_replacement_d2_009):
    feature = _clean(hwd_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_009'] = {'inputs': ['hwd_replacement_d2_009'], 'func': hwd_replacement_d3_009}


def hwd_replacement_d3_010(hwd_replacement_d2_010):
    feature = _clean(hwd_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_010'] = {'inputs': ['hwd_replacement_d2_010'], 'func': hwd_replacement_d3_010}


def hwd_replacement_d3_011(hwd_replacement_d2_011):
    feature = _clean(hwd_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_011'] = {'inputs': ['hwd_replacement_d2_011'], 'func': hwd_replacement_d3_011}


def hwd_replacement_d3_012(hwd_replacement_d2_012):
    feature = _clean(hwd_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_012'] = {'inputs': ['hwd_replacement_d2_012'], 'func': hwd_replacement_d3_012}


def hwd_replacement_d3_013(hwd_replacement_d2_013):
    feature = _clean(hwd_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_013'] = {'inputs': ['hwd_replacement_d2_013'], 'func': hwd_replacement_d3_013}


def hwd_replacement_d3_014(hwd_replacement_d2_014):
    feature = _clean(hwd_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_014'] = {'inputs': ['hwd_replacement_d2_014'], 'func': hwd_replacement_d3_014}


def hwd_replacement_d3_015(hwd_replacement_d2_015):
    feature = _clean(hwd_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_015'] = {'inputs': ['hwd_replacement_d2_015'], 'func': hwd_replacement_d3_015}


def hwd_replacement_d3_016(hwd_replacement_d2_016):
    feature = _clean(hwd_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_016'] = {'inputs': ['hwd_replacement_d2_016'], 'func': hwd_replacement_d3_016}


def hwd_replacement_d3_017(hwd_replacement_d2_017):
    feature = _clean(hwd_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_017'] = {'inputs': ['hwd_replacement_d2_017'], 'func': hwd_replacement_d3_017}


def hwd_replacement_d3_018(hwd_replacement_d2_018):
    feature = _clean(hwd_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_018'] = {'inputs': ['hwd_replacement_d2_018'], 'func': hwd_replacement_d3_018}


def hwd_replacement_d3_019(hwd_replacement_d2_019):
    feature = _clean(hwd_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_019'] = {'inputs': ['hwd_replacement_d2_019'], 'func': hwd_replacement_d3_019}


def hwd_replacement_d3_020(hwd_replacement_d2_020):
    feature = _clean(hwd_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_020'] = {'inputs': ['hwd_replacement_d2_020'], 'func': hwd_replacement_d3_020}


def hwd_replacement_d3_021(hwd_replacement_d2_021):
    feature = _clean(hwd_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_021'] = {'inputs': ['hwd_replacement_d2_021'], 'func': hwd_replacement_d3_021}


def hwd_replacement_d3_022(hwd_replacement_d2_022):
    feature = _clean(hwd_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_022'] = {'inputs': ['hwd_replacement_d2_022'], 'func': hwd_replacement_d3_022}


def hwd_replacement_d3_023(hwd_replacement_d2_023):
    feature = _clean(hwd_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_023'] = {'inputs': ['hwd_replacement_d2_023'], 'func': hwd_replacement_d3_023}


def hwd_replacement_d3_024(hwd_replacement_d2_024):
    feature = _clean(hwd_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_024'] = {'inputs': ['hwd_replacement_d2_024'], 'func': hwd_replacement_d3_024}


def hwd_replacement_d3_025(hwd_replacement_d2_025):
    feature = _clean(hwd_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_025'] = {'inputs': ['hwd_replacement_d2_025'], 'func': hwd_replacement_d3_025}


def hwd_replacement_d3_026(hwd_replacement_d2_026):
    feature = _clean(hwd_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_026'] = {'inputs': ['hwd_replacement_d2_026'], 'func': hwd_replacement_d3_026}


def hwd_replacement_d3_027(hwd_replacement_d2_027):
    feature = _clean(hwd_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_027'] = {'inputs': ['hwd_replacement_d2_027'], 'func': hwd_replacement_d3_027}


def hwd_replacement_d3_028(hwd_replacement_d2_028):
    feature = _clean(hwd_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_028'] = {'inputs': ['hwd_replacement_d2_028'], 'func': hwd_replacement_d3_028}


def hwd_replacement_d3_029(hwd_replacement_d2_029):
    feature = _clean(hwd_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_029'] = {'inputs': ['hwd_replacement_d2_029'], 'func': hwd_replacement_d3_029}


def hwd_replacement_d3_030(hwd_replacement_d2_030):
    feature = _clean(hwd_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_030'] = {'inputs': ['hwd_replacement_d2_030'], 'func': hwd_replacement_d3_030}


def hwd_replacement_d3_031(hwd_replacement_d2_031):
    feature = _clean(hwd_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_031'] = {'inputs': ['hwd_replacement_d2_031'], 'func': hwd_replacement_d3_031}


def hwd_replacement_d3_032(hwd_replacement_d2_032):
    feature = _clean(hwd_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_032'] = {'inputs': ['hwd_replacement_d2_032'], 'func': hwd_replacement_d3_032}


def hwd_replacement_d3_033(hwd_replacement_d2_033):
    feature = _clean(hwd_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_033'] = {'inputs': ['hwd_replacement_d2_033'], 'func': hwd_replacement_d3_033}


def hwd_replacement_d3_034(hwd_replacement_d2_034):
    feature = _clean(hwd_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_034'] = {'inputs': ['hwd_replacement_d2_034'], 'func': hwd_replacement_d3_034}


def hwd_replacement_d3_035(hwd_replacement_d2_035):
    feature = _clean(hwd_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_035'] = {'inputs': ['hwd_replacement_d2_035'], 'func': hwd_replacement_d3_035}


def hwd_replacement_d3_036(hwd_replacement_d2_036):
    feature = _clean(hwd_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_036'] = {'inputs': ['hwd_replacement_d2_036'], 'func': hwd_replacement_d3_036}


def hwd_replacement_d3_037(hwd_replacement_d2_037):
    feature = _clean(hwd_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_037'] = {'inputs': ['hwd_replacement_d2_037'], 'func': hwd_replacement_d3_037}


def hwd_replacement_d3_038(hwd_replacement_d2_038):
    feature = _clean(hwd_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_038'] = {'inputs': ['hwd_replacement_d2_038'], 'func': hwd_replacement_d3_038}


def hwd_replacement_d3_039(hwd_replacement_d2_039):
    feature = _clean(hwd_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_039'] = {'inputs': ['hwd_replacement_d2_039'], 'func': hwd_replacement_d3_039}


def hwd_replacement_d3_040(hwd_replacement_d2_040):
    feature = _clean(hwd_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_040'] = {'inputs': ['hwd_replacement_d2_040'], 'func': hwd_replacement_d3_040}


def hwd_replacement_d3_041(hwd_replacement_d2_041):
    feature = _clean(hwd_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_041'] = {'inputs': ['hwd_replacement_d2_041'], 'func': hwd_replacement_d3_041}


def hwd_replacement_d3_042(hwd_replacement_d2_042):
    feature = _clean(hwd_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_042'] = {'inputs': ['hwd_replacement_d2_042'], 'func': hwd_replacement_d3_042}


def hwd_replacement_d3_043(hwd_replacement_d2_043):
    feature = _clean(hwd_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_043'] = {'inputs': ['hwd_replacement_d2_043'], 'func': hwd_replacement_d3_043}


def hwd_replacement_d3_044(hwd_replacement_d2_044):
    feature = _clean(hwd_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_044'] = {'inputs': ['hwd_replacement_d2_044'], 'func': hwd_replacement_d3_044}


def hwd_replacement_d3_045(hwd_replacement_d2_045):
    feature = _clean(hwd_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_045'] = {'inputs': ['hwd_replacement_d2_045'], 'func': hwd_replacement_d3_045}


def hwd_replacement_d3_046(hwd_replacement_d2_046):
    feature = _clean(hwd_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_046'] = {'inputs': ['hwd_replacement_d2_046'], 'func': hwd_replacement_d3_046}


def hwd_replacement_d3_047(hwd_replacement_d2_047):
    feature = _clean(hwd_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_047'] = {'inputs': ['hwd_replacement_d2_047'], 'func': hwd_replacement_d3_047}


def hwd_replacement_d3_048(hwd_replacement_d2_048):
    feature = _clean(hwd_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_048'] = {'inputs': ['hwd_replacement_d2_048'], 'func': hwd_replacement_d3_048}


def hwd_replacement_d3_049(hwd_replacement_d2_049):
    feature = _clean(hwd_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_049'] = {'inputs': ['hwd_replacement_d2_049'], 'func': hwd_replacement_d3_049}


def hwd_replacement_d3_050(hwd_replacement_d2_050):
    feature = _clean(hwd_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_050'] = {'inputs': ['hwd_replacement_d2_050'], 'func': hwd_replacement_d3_050}


def hwd_replacement_d3_051(hwd_replacement_d2_051):
    feature = _clean(hwd_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_051'] = {'inputs': ['hwd_replacement_d2_051'], 'func': hwd_replacement_d3_051}


def hwd_replacement_d3_052(hwd_replacement_d2_052):
    feature = _clean(hwd_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_052'] = {'inputs': ['hwd_replacement_d2_052'], 'func': hwd_replacement_d3_052}


def hwd_replacement_d3_053(hwd_replacement_d2_053):
    feature = _clean(hwd_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_053'] = {'inputs': ['hwd_replacement_d2_053'], 'func': hwd_replacement_d3_053}


def hwd_replacement_d3_054(hwd_replacement_d2_054):
    feature = _clean(hwd_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_054'] = {'inputs': ['hwd_replacement_d2_054'], 'func': hwd_replacement_d3_054}


def hwd_replacement_d3_055(hwd_replacement_d2_055):
    feature = _clean(hwd_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_055'] = {'inputs': ['hwd_replacement_d2_055'], 'func': hwd_replacement_d3_055}


def hwd_replacement_d3_056(hwd_replacement_d2_056):
    feature = _clean(hwd_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_056'] = {'inputs': ['hwd_replacement_d2_056'], 'func': hwd_replacement_d3_056}


def hwd_replacement_d3_057(hwd_replacement_d2_057):
    feature = _clean(hwd_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_057'] = {'inputs': ['hwd_replacement_d2_057'], 'func': hwd_replacement_d3_057}


def hwd_replacement_d3_058(hwd_replacement_d2_058):
    feature = _clean(hwd_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_058'] = {'inputs': ['hwd_replacement_d2_058'], 'func': hwd_replacement_d3_058}


def hwd_replacement_d3_059(hwd_replacement_d2_059):
    feature = _clean(hwd_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_059'] = {'inputs': ['hwd_replacement_d2_059'], 'func': hwd_replacement_d3_059}


def hwd_replacement_d3_060(hwd_replacement_d2_060):
    feature = _clean(hwd_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_060'] = {'inputs': ['hwd_replacement_d2_060'], 'func': hwd_replacement_d3_060}


def hwd_replacement_d3_061(hwd_replacement_d2_061):
    feature = _clean(hwd_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_061'] = {'inputs': ['hwd_replacement_d2_061'], 'func': hwd_replacement_d3_061}


def hwd_replacement_d3_062(hwd_replacement_d2_062):
    feature = _clean(hwd_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_062'] = {'inputs': ['hwd_replacement_d2_062'], 'func': hwd_replacement_d3_062}


def hwd_replacement_d3_063(hwd_replacement_d2_063):
    feature = _clean(hwd_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_063'] = {'inputs': ['hwd_replacement_d2_063'], 'func': hwd_replacement_d3_063}


def hwd_replacement_d3_064(hwd_replacement_d2_064):
    feature = _clean(hwd_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_064'] = {'inputs': ['hwd_replacement_d2_064'], 'func': hwd_replacement_d3_064}


def hwd_replacement_d3_065(hwd_replacement_d2_065):
    feature = _clean(hwd_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_065'] = {'inputs': ['hwd_replacement_d2_065'], 'func': hwd_replacement_d3_065}


def hwd_replacement_d3_066(hwd_replacement_d2_066):
    feature = _clean(hwd_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_066'] = {'inputs': ['hwd_replacement_d2_066'], 'func': hwd_replacement_d3_066}


def hwd_replacement_d3_067(hwd_replacement_d2_067):
    feature = _clean(hwd_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_067'] = {'inputs': ['hwd_replacement_d2_067'], 'func': hwd_replacement_d3_067}


def hwd_replacement_d3_068(hwd_replacement_d2_068):
    feature = _clean(hwd_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_068'] = {'inputs': ['hwd_replacement_d2_068'], 'func': hwd_replacement_d3_068}


def hwd_replacement_d3_069(hwd_replacement_d2_069):
    feature = _clean(hwd_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_069'] = {'inputs': ['hwd_replacement_d2_069'], 'func': hwd_replacement_d3_069}


def hwd_replacement_d3_070(hwd_replacement_d2_070):
    feature = _clean(hwd_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_070'] = {'inputs': ['hwd_replacement_d2_070'], 'func': hwd_replacement_d3_070}


def hwd_replacement_d3_071(hwd_replacement_d2_071):
    feature = _clean(hwd_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_071'] = {'inputs': ['hwd_replacement_d2_071'], 'func': hwd_replacement_d3_071}


def hwd_replacement_d3_072(hwd_replacement_d2_072):
    feature = _clean(hwd_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_072'] = {'inputs': ['hwd_replacement_d2_072'], 'func': hwd_replacement_d3_072}


def hwd_replacement_d3_073(hwd_replacement_d2_073):
    feature = _clean(hwd_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_073'] = {'inputs': ['hwd_replacement_d2_073'], 'func': hwd_replacement_d3_073}


def hwd_replacement_d3_074(hwd_replacement_d2_074):
    feature = _clean(hwd_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_074'] = {'inputs': ['hwd_replacement_d2_074'], 'func': hwd_replacement_d3_074}


def hwd_replacement_d3_075(hwd_replacement_d2_075):
    feature = _clean(hwd_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_075'] = {'inputs': ['hwd_replacement_d2_075'], 'func': hwd_replacement_d3_075}


def hwd_replacement_d3_076(hwd_replacement_d2_076):
    feature = _clean(hwd_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_076'] = {'inputs': ['hwd_replacement_d2_076'], 'func': hwd_replacement_d3_076}


def hwd_replacement_d3_077(hwd_replacement_d2_077):
    feature = _clean(hwd_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_077'] = {'inputs': ['hwd_replacement_d2_077'], 'func': hwd_replacement_d3_077}


def hwd_replacement_d3_078(hwd_replacement_d2_078):
    feature = _clean(hwd_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_078'] = {'inputs': ['hwd_replacement_d2_078'], 'func': hwd_replacement_d3_078}


def hwd_replacement_d3_079(hwd_replacement_d2_079):
    feature = _clean(hwd_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_079'] = {'inputs': ['hwd_replacement_d2_079'], 'func': hwd_replacement_d3_079}


def hwd_replacement_d3_080(hwd_replacement_d2_080):
    feature = _clean(hwd_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_080'] = {'inputs': ['hwd_replacement_d2_080'], 'func': hwd_replacement_d3_080}


def hwd_replacement_d3_081(hwd_replacement_d2_081):
    feature = _clean(hwd_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_081'] = {'inputs': ['hwd_replacement_d2_081'], 'func': hwd_replacement_d3_081}


def hwd_replacement_d3_082(hwd_replacement_d2_082):
    feature = _clean(hwd_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_082'] = {'inputs': ['hwd_replacement_d2_082'], 'func': hwd_replacement_d3_082}


def hwd_replacement_d3_083(hwd_replacement_d2_083):
    feature = _clean(hwd_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_083'] = {'inputs': ['hwd_replacement_d2_083'], 'func': hwd_replacement_d3_083}


def hwd_replacement_d3_084(hwd_replacement_d2_084):
    feature = _clean(hwd_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_084'] = {'inputs': ['hwd_replacement_d2_084'], 'func': hwd_replacement_d3_084}


def hwd_replacement_d3_085(hwd_replacement_d2_085):
    feature = _clean(hwd_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_085'] = {'inputs': ['hwd_replacement_d2_085'], 'func': hwd_replacement_d3_085}


def hwd_replacement_d3_086(hwd_replacement_d2_086):
    feature = _clean(hwd_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_086'] = {'inputs': ['hwd_replacement_d2_086'], 'func': hwd_replacement_d3_086}


def hwd_replacement_d3_087(hwd_replacement_d2_087):
    feature = _clean(hwd_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_087'] = {'inputs': ['hwd_replacement_d2_087'], 'func': hwd_replacement_d3_087}


def hwd_replacement_d3_088(hwd_replacement_d2_088):
    feature = _clean(hwd_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_088'] = {'inputs': ['hwd_replacement_d2_088'], 'func': hwd_replacement_d3_088}


def hwd_replacement_d3_089(hwd_replacement_d2_089):
    feature = _clean(hwd_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_089'] = {'inputs': ['hwd_replacement_d2_089'], 'func': hwd_replacement_d3_089}


def hwd_replacement_d3_090(hwd_replacement_d2_090):
    feature = _clean(hwd_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_090'] = {'inputs': ['hwd_replacement_d2_090'], 'func': hwd_replacement_d3_090}


def hwd_replacement_d3_091(hwd_replacement_d2_091):
    feature = _clean(hwd_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_091'] = {'inputs': ['hwd_replacement_d2_091'], 'func': hwd_replacement_d3_091}


def hwd_replacement_d3_092(hwd_replacement_d2_092):
    feature = _clean(hwd_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_092'] = {'inputs': ['hwd_replacement_d2_092'], 'func': hwd_replacement_d3_092}


def hwd_replacement_d3_093(hwd_replacement_d2_093):
    feature = _clean(hwd_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_093'] = {'inputs': ['hwd_replacement_d2_093'], 'func': hwd_replacement_d3_093}


def hwd_replacement_d3_094(hwd_replacement_d2_094):
    feature = _clean(hwd_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_094'] = {'inputs': ['hwd_replacement_d2_094'], 'func': hwd_replacement_d3_094}


def hwd_replacement_d3_095(hwd_replacement_d2_095):
    feature = _clean(hwd_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_095'] = {'inputs': ['hwd_replacement_d2_095'], 'func': hwd_replacement_d3_095}


def hwd_replacement_d3_096(hwd_replacement_d2_096):
    feature = _clean(hwd_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_096'] = {'inputs': ['hwd_replacement_d2_096'], 'func': hwd_replacement_d3_096}


def hwd_replacement_d3_097(hwd_replacement_d2_097):
    feature = _clean(hwd_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_097'] = {'inputs': ['hwd_replacement_d2_097'], 'func': hwd_replacement_d3_097}


def hwd_replacement_d3_098(hwd_replacement_d2_098):
    feature = _clean(hwd_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_098'] = {'inputs': ['hwd_replacement_d2_098'], 'func': hwd_replacement_d3_098}


def hwd_replacement_d3_099(hwd_replacement_d2_099):
    feature = _clean(hwd_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_099'] = {'inputs': ['hwd_replacement_d2_099'], 'func': hwd_replacement_d3_099}


def hwd_replacement_d3_100(hwd_replacement_d2_100):
    feature = _clean(hwd_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_100'] = {'inputs': ['hwd_replacement_d2_100'], 'func': hwd_replacement_d3_100}


def hwd_replacement_d3_101(hwd_replacement_d2_101):
    feature = _clean(hwd_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_101'] = {'inputs': ['hwd_replacement_d2_101'], 'func': hwd_replacement_d3_101}


def hwd_replacement_d3_102(hwd_replacement_d2_102):
    feature = _clean(hwd_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_102'] = {'inputs': ['hwd_replacement_d2_102'], 'func': hwd_replacement_d3_102}


def hwd_replacement_d3_103(hwd_replacement_d2_103):
    feature = _clean(hwd_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_103'] = {'inputs': ['hwd_replacement_d2_103'], 'func': hwd_replacement_d3_103}


def hwd_replacement_d3_104(hwd_replacement_d2_104):
    feature = _clean(hwd_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_104'] = {'inputs': ['hwd_replacement_d2_104'], 'func': hwd_replacement_d3_104}


def hwd_replacement_d3_105(hwd_replacement_d2_105):
    feature = _clean(hwd_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_105'] = {'inputs': ['hwd_replacement_d2_105'], 'func': hwd_replacement_d3_105}


def hwd_replacement_d3_106(hwd_replacement_d2_106):
    feature = _clean(hwd_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_106'] = {'inputs': ['hwd_replacement_d2_106'], 'func': hwd_replacement_d3_106}


def hwd_replacement_d3_107(hwd_replacement_d2_107):
    feature = _clean(hwd_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_107'] = {'inputs': ['hwd_replacement_d2_107'], 'func': hwd_replacement_d3_107}


def hwd_replacement_d3_108(hwd_replacement_d2_108):
    feature = _clean(hwd_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_108'] = {'inputs': ['hwd_replacement_d2_108'], 'func': hwd_replacement_d3_108}


def hwd_replacement_d3_109(hwd_replacement_d2_109):
    feature = _clean(hwd_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_109'] = {'inputs': ['hwd_replacement_d2_109'], 'func': hwd_replacement_d3_109}


def hwd_replacement_d3_110(hwd_replacement_d2_110):
    feature = _clean(hwd_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_110'] = {'inputs': ['hwd_replacement_d2_110'], 'func': hwd_replacement_d3_110}


def hwd_replacement_d3_111(hwd_replacement_d2_111):
    feature = _clean(hwd_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_111'] = {'inputs': ['hwd_replacement_d2_111'], 'func': hwd_replacement_d3_111}


def hwd_replacement_d3_112(hwd_replacement_d2_112):
    feature = _clean(hwd_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_112'] = {'inputs': ['hwd_replacement_d2_112'], 'func': hwd_replacement_d3_112}


def hwd_replacement_d3_113(hwd_replacement_d2_113):
    feature = _clean(hwd_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_113'] = {'inputs': ['hwd_replacement_d2_113'], 'func': hwd_replacement_d3_113}


def hwd_replacement_d3_114(hwd_replacement_d2_114):
    feature = _clean(hwd_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_114'] = {'inputs': ['hwd_replacement_d2_114'], 'func': hwd_replacement_d3_114}


def hwd_replacement_d3_115(hwd_replacement_d2_115):
    feature = _clean(hwd_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_115'] = {'inputs': ['hwd_replacement_d2_115'], 'func': hwd_replacement_d3_115}


def hwd_replacement_d3_116(hwd_replacement_d2_116):
    feature = _clean(hwd_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_116'] = {'inputs': ['hwd_replacement_d2_116'], 'func': hwd_replacement_d3_116}


def hwd_replacement_d3_117(hwd_replacement_d2_117):
    feature = _clean(hwd_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_117'] = {'inputs': ['hwd_replacement_d2_117'], 'func': hwd_replacement_d3_117}


def hwd_replacement_d3_118(hwd_replacement_d2_118):
    feature = _clean(hwd_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_118'] = {'inputs': ['hwd_replacement_d2_118'], 'func': hwd_replacement_d3_118}


def hwd_replacement_d3_119(hwd_replacement_d2_119):
    feature = _clean(hwd_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_119'] = {'inputs': ['hwd_replacement_d2_119'], 'func': hwd_replacement_d3_119}


def hwd_replacement_d3_120(hwd_replacement_d2_120):
    feature = _clean(hwd_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_120'] = {'inputs': ['hwd_replacement_d2_120'], 'func': hwd_replacement_d3_120}


def hwd_replacement_d3_121(hwd_replacement_d2_121):
    feature = _clean(hwd_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_121'] = {'inputs': ['hwd_replacement_d2_121'], 'func': hwd_replacement_d3_121}


def hwd_replacement_d3_122(hwd_replacement_d2_122):
    feature = _clean(hwd_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_122'] = {'inputs': ['hwd_replacement_d2_122'], 'func': hwd_replacement_d3_122}


def hwd_replacement_d3_123(hwd_replacement_d2_123):
    feature = _clean(hwd_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_123'] = {'inputs': ['hwd_replacement_d2_123'], 'func': hwd_replacement_d3_123}


def hwd_replacement_d3_124(hwd_replacement_d2_124):
    feature = _clean(hwd_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_124'] = {'inputs': ['hwd_replacement_d2_124'], 'func': hwd_replacement_d3_124}


def hwd_replacement_d3_125(hwd_replacement_d2_125):
    feature = _clean(hwd_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_125'] = {'inputs': ['hwd_replacement_d2_125'], 'func': hwd_replacement_d3_125}


def hwd_replacement_d3_126(hwd_replacement_d2_126):
    feature = _clean(hwd_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_126'] = {'inputs': ['hwd_replacement_d2_126'], 'func': hwd_replacement_d3_126}


def hwd_replacement_d3_127(hwd_replacement_d2_127):
    feature = _clean(hwd_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_127'] = {'inputs': ['hwd_replacement_d2_127'], 'func': hwd_replacement_d3_127}


def hwd_replacement_d3_128(hwd_replacement_d2_128):
    feature = _clean(hwd_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_128'] = {'inputs': ['hwd_replacement_d2_128'], 'func': hwd_replacement_d3_128}


def hwd_replacement_d3_129(hwd_replacement_d2_129):
    feature = _clean(hwd_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_129'] = {'inputs': ['hwd_replacement_d2_129'], 'func': hwd_replacement_d3_129}


def hwd_replacement_d3_130(hwd_replacement_d2_130):
    feature = _clean(hwd_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_130'] = {'inputs': ['hwd_replacement_d2_130'], 'func': hwd_replacement_d3_130}


def hwd_replacement_d3_131(hwd_replacement_d2_131):
    feature = _clean(hwd_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_131'] = {'inputs': ['hwd_replacement_d2_131'], 'func': hwd_replacement_d3_131}


def hwd_replacement_d3_132(hwd_replacement_d2_132):
    feature = _clean(hwd_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_132'] = {'inputs': ['hwd_replacement_d2_132'], 'func': hwd_replacement_d3_132}


def hwd_replacement_d3_133(hwd_replacement_d2_133):
    feature = _clean(hwd_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_133'] = {'inputs': ['hwd_replacement_d2_133'], 'func': hwd_replacement_d3_133}


def hwd_replacement_d3_134(hwd_replacement_d2_134):
    feature = _clean(hwd_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_134'] = {'inputs': ['hwd_replacement_d2_134'], 'func': hwd_replacement_d3_134}


def hwd_replacement_d3_135(hwd_replacement_d2_135):
    feature = _clean(hwd_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_135'] = {'inputs': ['hwd_replacement_d2_135'], 'func': hwd_replacement_d3_135}


def hwd_replacement_d3_136(hwd_replacement_d2_136):
    feature = _clean(hwd_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_136'] = {'inputs': ['hwd_replacement_d2_136'], 'func': hwd_replacement_d3_136}


def hwd_replacement_d3_137(hwd_replacement_d2_137):
    feature = _clean(hwd_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_137'] = {'inputs': ['hwd_replacement_d2_137'], 'func': hwd_replacement_d3_137}


def hwd_replacement_d3_138(hwd_replacement_d2_138):
    feature = _clean(hwd_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_138'] = {'inputs': ['hwd_replacement_d2_138'], 'func': hwd_replacement_d3_138}


def hwd_replacement_d3_139(hwd_replacement_d2_139):
    feature = _clean(hwd_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_139'] = {'inputs': ['hwd_replacement_d2_139'], 'func': hwd_replacement_d3_139}


def hwd_replacement_d3_140(hwd_replacement_d2_140):
    feature = _clean(hwd_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_140'] = {'inputs': ['hwd_replacement_d2_140'], 'func': hwd_replacement_d3_140}


def hwd_replacement_d3_141(hwd_replacement_d2_141):
    feature = _clean(hwd_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_141'] = {'inputs': ['hwd_replacement_d2_141'], 'func': hwd_replacement_d3_141}


def hwd_replacement_d3_142(hwd_replacement_d2_142):
    feature = _clean(hwd_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_142'] = {'inputs': ['hwd_replacement_d2_142'], 'func': hwd_replacement_d3_142}


def hwd_replacement_d3_143(hwd_replacement_d2_143):
    feature = _clean(hwd_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_143'] = {'inputs': ['hwd_replacement_d2_143'], 'func': hwd_replacement_d3_143}


def hwd_replacement_d3_144(hwd_replacement_d2_144):
    feature = _clean(hwd_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_144'] = {'inputs': ['hwd_replacement_d2_144'], 'func': hwd_replacement_d3_144}


def hwd_replacement_d3_145(hwd_replacement_d2_145):
    feature = _clean(hwd_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_145'] = {'inputs': ['hwd_replacement_d2_145'], 'func': hwd_replacement_d3_145}


def hwd_replacement_d3_146(hwd_replacement_d2_146):
    feature = _clean(hwd_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_146'] = {'inputs': ['hwd_replacement_d2_146'], 'func': hwd_replacement_d3_146}


def hwd_replacement_d3_147(hwd_replacement_d2_147):
    feature = _clean(hwd_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_147'] = {'inputs': ['hwd_replacement_d2_147'], 'func': hwd_replacement_d3_147}


def hwd_replacement_d3_148(hwd_replacement_d2_148):
    feature = _clean(hwd_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_148'] = {'inputs': ['hwd_replacement_d2_148'], 'func': hwd_replacement_d3_148}


def hwd_replacement_d3_149(hwd_replacement_d2_149):
    feature = _clean(hwd_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_149'] = {'inputs': ['hwd_replacement_d2_149'], 'func': hwd_replacement_d3_149}


def hwd_replacement_d3_150(hwd_replacement_d2_150):
    feature = _clean(hwd_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_150'] = {'inputs': ['hwd_replacement_d2_150'], 'func': hwd_replacement_d3_150}


def hwd_replacement_d3_151(hwd_replacement_d2_151):
    feature = _clean(hwd_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_151'] = {'inputs': ['hwd_replacement_d2_151'], 'func': hwd_replacement_d3_151}


def hwd_replacement_d3_152(hwd_replacement_d2_152):
    feature = _clean(hwd_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_152'] = {'inputs': ['hwd_replacement_d2_152'], 'func': hwd_replacement_d3_152}


def hwd_replacement_d3_153(hwd_replacement_d2_153):
    feature = _clean(hwd_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_153'] = {'inputs': ['hwd_replacement_d2_153'], 'func': hwd_replacement_d3_153}


def hwd_replacement_d3_154(hwd_replacement_d2_154):
    feature = _clean(hwd_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_154'] = {'inputs': ['hwd_replacement_d2_154'], 'func': hwd_replacement_d3_154}


def hwd_replacement_d3_155(hwd_replacement_d2_155):
    feature = _clean(hwd_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_155'] = {'inputs': ['hwd_replacement_d2_155'], 'func': hwd_replacement_d3_155}


def hwd_replacement_d3_156(hwd_replacement_d2_156):
    feature = _clean(hwd_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_156'] = {'inputs': ['hwd_replacement_d2_156'], 'func': hwd_replacement_d3_156}


def hwd_replacement_d3_157(hwd_replacement_d2_157):
    feature = _clean(hwd_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_157'] = {'inputs': ['hwd_replacement_d2_157'], 'func': hwd_replacement_d3_157}


def hwd_replacement_d3_158(hwd_replacement_d2_158):
    feature = _clean(hwd_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_158'] = {'inputs': ['hwd_replacement_d2_158'], 'func': hwd_replacement_d3_158}


def hwd_replacement_d3_159(hwd_replacement_d2_159):
    feature = _clean(hwd_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_159'] = {'inputs': ['hwd_replacement_d2_159'], 'func': hwd_replacement_d3_159}


def hwd_replacement_d3_160(hwd_replacement_d2_160):
    feature = _clean(hwd_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_160'] = {'inputs': ['hwd_replacement_d2_160'], 'func': hwd_replacement_d3_160}


def hwd_replacement_d3_161(hwd_replacement_d2_161):
    feature = _clean(hwd_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_161'] = {'inputs': ['hwd_replacement_d2_161'], 'func': hwd_replacement_d3_161}


def hwd_replacement_d3_162(hwd_replacement_d2_162):
    feature = _clean(hwd_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_162'] = {'inputs': ['hwd_replacement_d2_162'], 'func': hwd_replacement_d3_162}


def hwd_replacement_d3_163(hwd_replacement_d2_163):
    feature = _clean(hwd_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_163'] = {'inputs': ['hwd_replacement_d2_163'], 'func': hwd_replacement_d3_163}


def hwd_replacement_d3_164(hwd_replacement_d2_164):
    feature = _clean(hwd_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_164'] = {'inputs': ['hwd_replacement_d2_164'], 'func': hwd_replacement_d3_164}


def hwd_replacement_d3_165(hwd_replacement_d2_165):
    feature = _clean(hwd_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_165'] = {'inputs': ['hwd_replacement_d2_165'], 'func': hwd_replacement_d3_165}


def hwd_replacement_d3_166(hwd_replacement_d2_166):
    feature = _clean(hwd_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_166'] = {'inputs': ['hwd_replacement_d2_166'], 'func': hwd_replacement_d3_166}


def hwd_replacement_d3_167(hwd_replacement_d2_167):
    feature = _clean(hwd_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_167'] = {'inputs': ['hwd_replacement_d2_167'], 'func': hwd_replacement_d3_167}


def hwd_replacement_d3_168(hwd_replacement_d2_168):
    feature = _clean(hwd_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_168'] = {'inputs': ['hwd_replacement_d2_168'], 'func': hwd_replacement_d3_168}


def hwd_replacement_d3_169(hwd_replacement_d2_169):
    feature = _clean(hwd_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_169'] = {'inputs': ['hwd_replacement_d2_169'], 'func': hwd_replacement_d3_169}


def hwd_replacement_d3_170(hwd_replacement_d2_170):
    feature = _clean(hwd_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
HWD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hwd_replacement_d3_170'] = {'inputs': ['hwd_replacement_d2_170'], 'func': hwd_replacement_d3_170}


# Third-derivative extensions for repaired first-base features.
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def hwd_base_universe_d3_001_hwd_002_low_distance_10_002(hwd_base_universe_d2_001_hwd_002_low_distance_10_002):
    return _base_universe_d3(hwd_base_universe_d2_001_hwd_002_low_distance_10_002, 1)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_001_hwd_002_low_distance_10_002'] = {'inputs': ['hwd_base_universe_d2_001_hwd_002_low_distance_10_002'], 'func': hwd_base_universe_d3_001_hwd_002_low_distance_10_002}


def hwd_base_universe_d3_002_hwd_003_underwater_area_21_003(hwd_base_universe_d2_002_hwd_003_underwater_area_21_003):
    return _base_universe_d3(hwd_base_universe_d2_002_hwd_003_underwater_area_21_003, 2)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_002_hwd_003_underwater_area_21_003'] = {'inputs': ['hwd_base_universe_d2_002_hwd_003_underwater_area_21_003'], 'func': hwd_base_universe_d3_002_hwd_003_underwater_area_21_003}


def hwd_base_universe_d3_003_hwd_006_lower_high_ratio_84_006(hwd_base_universe_d2_003_hwd_006_lower_high_ratio_84_006):
    return _base_universe_d3(hwd_base_universe_d2_003_hwd_006_lower_high_ratio_84_006, 3)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_003_hwd_006_lower_high_ratio_84_006'] = {'inputs': ['hwd_base_universe_d2_003_hwd_006_lower_high_ratio_84_006'], 'func': hwd_base_universe_d3_003_hwd_006_lower_high_ratio_84_006}


def hwd_base_universe_d3_004_hwd_008_low_distance_189_008(hwd_base_universe_d2_004_hwd_008_low_distance_189_008):
    return _base_universe_d3(hwd_base_universe_d2_004_hwd_008_low_distance_189_008, 4)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_004_hwd_008_low_distance_189_008'] = {'inputs': ['hwd_base_universe_d2_004_hwd_008_low_distance_189_008'], 'func': hwd_base_universe_d3_004_hwd_008_low_distance_189_008}


def hwd_base_universe_d3_005_hwd_009_underwater_area_252_009(hwd_base_universe_d2_005_hwd_009_underwater_area_252_009):
    return _base_universe_d3(hwd_base_universe_d2_005_hwd_009_underwater_area_252_009, 5)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_005_hwd_009_underwater_area_252_009'] = {'inputs': ['hwd_base_universe_d2_005_hwd_009_underwater_area_252_009'], 'func': hwd_base_universe_d3_005_hwd_009_underwater_area_252_009}


def hwd_base_universe_d3_006_hwd_012_lower_high_ratio_756_012(hwd_base_universe_d2_006_hwd_012_lower_high_ratio_756_012):
    return _base_universe_d3(hwd_base_universe_d2_006_hwd_012_lower_high_ratio_756_012, 6)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_006_hwd_012_lower_high_ratio_756_012'] = {'inputs': ['hwd_base_universe_d2_006_hwd_012_lower_high_ratio_756_012'], 'func': hwd_base_universe_d3_006_hwd_012_lower_high_ratio_756_012}


def hwd_base_universe_d3_007_hwd_014_low_distance_1260_014(hwd_base_universe_d2_007_hwd_014_low_distance_1260_014):
    return _base_universe_d3(hwd_base_universe_d2_007_hwd_014_low_distance_1260_014, 7)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_007_hwd_014_low_distance_1260_014'] = {'inputs': ['hwd_base_universe_d2_007_hwd_014_low_distance_1260_014'], 'func': hwd_base_universe_d3_007_hwd_014_low_distance_1260_014}


def hwd_base_universe_d3_008_hwd_015_underwater_area_1512_015(hwd_base_universe_d2_008_hwd_015_underwater_area_1512_015):
    return _base_universe_d3(hwd_base_universe_d2_008_hwd_015_underwater_area_1512_015, 8)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_008_hwd_015_underwater_area_1512_015'] = {'inputs': ['hwd_base_universe_d2_008_hwd_015_underwater_area_1512_015'], 'func': hwd_base_universe_d3_008_hwd_015_underwater_area_1512_015}


def hwd_base_universe_d3_009_hwd_018_lower_high_ratio_21_018(hwd_base_universe_d2_009_hwd_018_lower_high_ratio_21_018):
    return _base_universe_d3(hwd_base_universe_d2_009_hwd_018_lower_high_ratio_21_018, 9)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_009_hwd_018_lower_high_ratio_21_018'] = {'inputs': ['hwd_base_universe_d2_009_hwd_018_lower_high_ratio_21_018'], 'func': hwd_base_universe_d3_009_hwd_018_lower_high_ratio_21_018}


def hwd_base_universe_d3_010_hwd_020_low_distance_63_020(hwd_base_universe_d2_010_hwd_020_low_distance_63_020):
    return _base_universe_d3(hwd_base_universe_d2_010_hwd_020_low_distance_63_020, 10)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_010_hwd_020_low_distance_63_020'] = {'inputs': ['hwd_base_universe_d2_010_hwd_020_low_distance_63_020'], 'func': hwd_base_universe_d3_010_hwd_020_low_distance_63_020}


def hwd_base_universe_d3_011_hwd_021_underwater_area_84_021(hwd_base_universe_d2_011_hwd_021_underwater_area_84_021):
    return _base_universe_d3(hwd_base_universe_d2_011_hwd_021_underwater_area_84_021, 11)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_011_hwd_021_underwater_area_84_021'] = {'inputs': ['hwd_base_universe_d2_011_hwd_021_underwater_area_84_021'], 'func': hwd_base_universe_d3_011_hwd_021_underwater_area_84_021}


def hwd_base_universe_d3_012_hwd_024_lower_high_ratio_252_024(hwd_base_universe_d2_012_hwd_024_lower_high_ratio_252_024):
    return _base_universe_d3(hwd_base_universe_d2_012_hwd_024_lower_high_ratio_252_024, 12)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_012_hwd_024_lower_high_ratio_252_024'] = {'inputs': ['hwd_base_universe_d2_012_hwd_024_lower_high_ratio_252_024'], 'func': hwd_base_universe_d3_012_hwd_024_lower_high_ratio_252_024}


def hwd_base_universe_d3_013_hwd_026_low_distance_504_026(hwd_base_universe_d2_013_hwd_026_low_distance_504_026):
    return _base_universe_d3(hwd_base_universe_d2_013_hwd_026_low_distance_504_026, 13)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_013_hwd_026_low_distance_504_026'] = {'inputs': ['hwd_base_universe_d2_013_hwd_026_low_distance_504_026'], 'func': hwd_base_universe_d3_013_hwd_026_low_distance_504_026}


def hwd_base_universe_d3_014_hwd_027_underwater_area_756_027(hwd_base_universe_d2_014_hwd_027_underwater_area_756_027):
    return _base_universe_d3(hwd_base_universe_d2_014_hwd_027_underwater_area_756_027, 14)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_014_hwd_027_underwater_area_756_027'] = {'inputs': ['hwd_base_universe_d2_014_hwd_027_underwater_area_756_027'], 'func': hwd_base_universe_d3_014_hwd_027_underwater_area_756_027}


def hwd_base_universe_d3_015_hwd_030_lower_high_ratio_1512_030(hwd_base_universe_d2_015_hwd_030_lower_high_ratio_1512_030):
    return _base_universe_d3(hwd_base_universe_d2_015_hwd_030_lower_high_ratio_1512_030, 15)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_015_hwd_030_lower_high_ratio_1512_030'] = {'inputs': ['hwd_base_universe_d2_015_hwd_030_lower_high_ratio_1512_030'], 'func': hwd_base_universe_d3_015_hwd_030_lower_high_ratio_1512_030}


def hwd_base_universe_d3_016_hwd_basefill_004(hwd_base_universe_d2_016_hwd_basefill_004):
    return _base_universe_d3(hwd_base_universe_d2_016_hwd_basefill_004, 16)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_016_hwd_basefill_004'] = {'inputs': ['hwd_base_universe_d2_016_hwd_basefill_004'], 'func': hwd_base_universe_d3_016_hwd_basefill_004}


def hwd_base_universe_d3_017_hwd_basefill_005(hwd_base_universe_d2_017_hwd_basefill_005):
    return _base_universe_d3(hwd_base_universe_d2_017_hwd_basefill_005, 17)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_017_hwd_basefill_005'] = {'inputs': ['hwd_base_universe_d2_017_hwd_basefill_005'], 'func': hwd_base_universe_d3_017_hwd_basefill_005}


def hwd_base_universe_d3_018_hwd_basefill_010(hwd_base_universe_d2_018_hwd_basefill_010):
    return _base_universe_d3(hwd_base_universe_d2_018_hwd_basefill_010, 18)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_018_hwd_basefill_010'] = {'inputs': ['hwd_base_universe_d2_018_hwd_basefill_010'], 'func': hwd_base_universe_d3_018_hwd_basefill_010}


def hwd_base_universe_d3_019_hwd_basefill_011(hwd_base_universe_d2_019_hwd_basefill_011):
    return _base_universe_d3(hwd_base_universe_d2_019_hwd_basefill_011, 19)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_019_hwd_basefill_011'] = {'inputs': ['hwd_base_universe_d2_019_hwd_basefill_011'], 'func': hwd_base_universe_d3_019_hwd_basefill_011}


def hwd_base_universe_d3_020_hwd_basefill_016(hwd_base_universe_d2_020_hwd_basefill_016):
    return _base_universe_d3(hwd_base_universe_d2_020_hwd_basefill_016, 20)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_020_hwd_basefill_016'] = {'inputs': ['hwd_base_universe_d2_020_hwd_basefill_016'], 'func': hwd_base_universe_d3_020_hwd_basefill_016}


def hwd_base_universe_d3_021_hwd_basefill_017(hwd_base_universe_d2_021_hwd_basefill_017):
    return _base_universe_d3(hwd_base_universe_d2_021_hwd_basefill_017, 21)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_021_hwd_basefill_017'] = {'inputs': ['hwd_base_universe_d2_021_hwd_basefill_017'], 'func': hwd_base_universe_d3_021_hwd_basefill_017}


def hwd_base_universe_d3_022_hwd_basefill_022(hwd_base_universe_d2_022_hwd_basefill_022):
    return _base_universe_d3(hwd_base_universe_d2_022_hwd_basefill_022, 22)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_022_hwd_basefill_022'] = {'inputs': ['hwd_base_universe_d2_022_hwd_basefill_022'], 'func': hwd_base_universe_d3_022_hwd_basefill_022}


def hwd_base_universe_d3_023_hwd_basefill_023(hwd_base_universe_d2_023_hwd_basefill_023):
    return _base_universe_d3(hwd_base_universe_d2_023_hwd_basefill_023, 23)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_023_hwd_basefill_023'] = {'inputs': ['hwd_base_universe_d2_023_hwd_basefill_023'], 'func': hwd_base_universe_d3_023_hwd_basefill_023}


def hwd_base_universe_d3_024_hwd_basefill_028(hwd_base_universe_d2_024_hwd_basefill_028):
    return _base_universe_d3(hwd_base_universe_d2_024_hwd_basefill_028, 24)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_024_hwd_basefill_028'] = {'inputs': ['hwd_base_universe_d2_024_hwd_basefill_028'], 'func': hwd_base_universe_d3_024_hwd_basefill_028}


def hwd_base_universe_d3_025_hwd_basefill_029(hwd_base_universe_d2_025_hwd_basefill_029):
    return _base_universe_d3(hwd_base_universe_d2_025_hwd_basefill_029, 25)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_025_hwd_basefill_029'] = {'inputs': ['hwd_base_universe_d2_025_hwd_basefill_029'], 'func': hwd_base_universe_d3_025_hwd_basefill_029}


def hwd_base_universe_d3_026_hwd_basefill_031(hwd_base_universe_d2_026_hwd_basefill_031):
    return _base_universe_d3(hwd_base_universe_d2_026_hwd_basefill_031, 26)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_026_hwd_basefill_031'] = {'inputs': ['hwd_base_universe_d2_026_hwd_basefill_031'], 'func': hwd_base_universe_d3_026_hwd_basefill_031}


def hwd_base_universe_d3_027_hwd_basefill_032(hwd_base_universe_d2_027_hwd_basefill_032):
    return _base_universe_d3(hwd_base_universe_d2_027_hwd_basefill_032, 27)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_027_hwd_basefill_032'] = {'inputs': ['hwd_base_universe_d2_027_hwd_basefill_032'], 'func': hwd_base_universe_d3_027_hwd_basefill_032}


def hwd_base_universe_d3_028_hwd_basefill_033(hwd_base_universe_d2_028_hwd_basefill_033):
    return _base_universe_d3(hwd_base_universe_d2_028_hwd_basefill_033, 28)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_028_hwd_basefill_033'] = {'inputs': ['hwd_base_universe_d2_028_hwd_basefill_033'], 'func': hwd_base_universe_d3_028_hwd_basefill_033}


def hwd_base_universe_d3_029_hwd_basefill_034(hwd_base_universe_d2_029_hwd_basefill_034):
    return _base_universe_d3(hwd_base_universe_d2_029_hwd_basefill_034, 29)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_029_hwd_basefill_034'] = {'inputs': ['hwd_base_universe_d2_029_hwd_basefill_034'], 'func': hwd_base_universe_d3_029_hwd_basefill_034}


def hwd_base_universe_d3_030_hwd_basefill_035(hwd_base_universe_d2_030_hwd_basefill_035):
    return _base_universe_d3(hwd_base_universe_d2_030_hwd_basefill_035, 30)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_030_hwd_basefill_035'] = {'inputs': ['hwd_base_universe_d2_030_hwd_basefill_035'], 'func': hwd_base_universe_d3_030_hwd_basefill_035}


def hwd_base_universe_d3_031_hwd_basefill_036(hwd_base_universe_d2_031_hwd_basefill_036):
    return _base_universe_d3(hwd_base_universe_d2_031_hwd_basefill_036, 31)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_031_hwd_basefill_036'] = {'inputs': ['hwd_base_universe_d2_031_hwd_basefill_036'], 'func': hwd_base_universe_d3_031_hwd_basefill_036}


def hwd_base_universe_d3_032_hwd_basefill_037(hwd_base_universe_d2_032_hwd_basefill_037):
    return _base_universe_d3(hwd_base_universe_d2_032_hwd_basefill_037, 32)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_032_hwd_basefill_037'] = {'inputs': ['hwd_base_universe_d2_032_hwd_basefill_037'], 'func': hwd_base_universe_d3_032_hwd_basefill_037}


def hwd_base_universe_d3_033_hwd_basefill_038(hwd_base_universe_d2_033_hwd_basefill_038):
    return _base_universe_d3(hwd_base_universe_d2_033_hwd_basefill_038, 33)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_033_hwd_basefill_038'] = {'inputs': ['hwd_base_universe_d2_033_hwd_basefill_038'], 'func': hwd_base_universe_d3_033_hwd_basefill_038}


def hwd_base_universe_d3_034_hwd_basefill_039(hwd_base_universe_d2_034_hwd_basefill_039):
    return _base_universe_d3(hwd_base_universe_d2_034_hwd_basefill_039, 34)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_034_hwd_basefill_039'] = {'inputs': ['hwd_base_universe_d2_034_hwd_basefill_039'], 'func': hwd_base_universe_d3_034_hwd_basefill_039}


def hwd_base_universe_d3_035_hwd_basefill_040(hwd_base_universe_d2_035_hwd_basefill_040):
    return _base_universe_d3(hwd_base_universe_d2_035_hwd_basefill_040, 35)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_035_hwd_basefill_040'] = {'inputs': ['hwd_base_universe_d2_035_hwd_basefill_040'], 'func': hwd_base_universe_d3_035_hwd_basefill_040}


def hwd_base_universe_d3_036_hwd_basefill_041(hwd_base_universe_d2_036_hwd_basefill_041):
    return _base_universe_d3(hwd_base_universe_d2_036_hwd_basefill_041, 36)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_036_hwd_basefill_041'] = {'inputs': ['hwd_base_universe_d2_036_hwd_basefill_041'], 'func': hwd_base_universe_d3_036_hwd_basefill_041}


def hwd_base_universe_d3_037_hwd_basefill_042(hwd_base_universe_d2_037_hwd_basefill_042):
    return _base_universe_d3(hwd_base_universe_d2_037_hwd_basefill_042, 37)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_037_hwd_basefill_042'] = {'inputs': ['hwd_base_universe_d2_037_hwd_basefill_042'], 'func': hwd_base_universe_d3_037_hwd_basefill_042}


def hwd_base_universe_d3_038_hwd_basefill_043(hwd_base_universe_d2_038_hwd_basefill_043):
    return _base_universe_d3(hwd_base_universe_d2_038_hwd_basefill_043, 38)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_038_hwd_basefill_043'] = {'inputs': ['hwd_base_universe_d2_038_hwd_basefill_043'], 'func': hwd_base_universe_d3_038_hwd_basefill_043}


def hwd_base_universe_d3_039_hwd_basefill_044(hwd_base_universe_d2_039_hwd_basefill_044):
    return _base_universe_d3(hwd_base_universe_d2_039_hwd_basefill_044, 39)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_039_hwd_basefill_044'] = {'inputs': ['hwd_base_universe_d2_039_hwd_basefill_044'], 'func': hwd_base_universe_d3_039_hwd_basefill_044}


def hwd_base_universe_d3_040_hwd_basefill_045(hwd_base_universe_d2_040_hwd_basefill_045):
    return _base_universe_d3(hwd_base_universe_d2_040_hwd_basefill_045, 40)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_040_hwd_basefill_045'] = {'inputs': ['hwd_base_universe_d2_040_hwd_basefill_045'], 'func': hwd_base_universe_d3_040_hwd_basefill_045}


def hwd_base_universe_d3_041_hwd_basefill_046(hwd_base_universe_d2_041_hwd_basefill_046):
    return _base_universe_d3(hwd_base_universe_d2_041_hwd_basefill_046, 41)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_041_hwd_basefill_046'] = {'inputs': ['hwd_base_universe_d2_041_hwd_basefill_046'], 'func': hwd_base_universe_d3_041_hwd_basefill_046}


def hwd_base_universe_d3_042_hwd_basefill_047(hwd_base_universe_d2_042_hwd_basefill_047):
    return _base_universe_d3(hwd_base_universe_d2_042_hwd_basefill_047, 42)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_042_hwd_basefill_047'] = {'inputs': ['hwd_base_universe_d2_042_hwd_basefill_047'], 'func': hwd_base_universe_d3_042_hwd_basefill_047}


def hwd_base_universe_d3_043_hwd_basefill_048(hwd_base_universe_d2_043_hwd_basefill_048):
    return _base_universe_d3(hwd_base_universe_d2_043_hwd_basefill_048, 43)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_043_hwd_basefill_048'] = {'inputs': ['hwd_base_universe_d2_043_hwd_basefill_048'], 'func': hwd_base_universe_d3_043_hwd_basefill_048}


def hwd_base_universe_d3_044_hwd_basefill_049(hwd_base_universe_d2_044_hwd_basefill_049):
    return _base_universe_d3(hwd_base_universe_d2_044_hwd_basefill_049, 44)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_044_hwd_basefill_049'] = {'inputs': ['hwd_base_universe_d2_044_hwd_basefill_049'], 'func': hwd_base_universe_d3_044_hwd_basefill_049}


def hwd_base_universe_d3_045_hwd_basefill_050(hwd_base_universe_d2_045_hwd_basefill_050):
    return _base_universe_d3(hwd_base_universe_d2_045_hwd_basefill_050, 45)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_045_hwd_basefill_050'] = {'inputs': ['hwd_base_universe_d2_045_hwd_basefill_050'], 'func': hwd_base_universe_d3_045_hwd_basefill_050}


def hwd_base_universe_d3_046_hwd_basefill_051(hwd_base_universe_d2_046_hwd_basefill_051):
    return _base_universe_d3(hwd_base_universe_d2_046_hwd_basefill_051, 46)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_046_hwd_basefill_051'] = {'inputs': ['hwd_base_universe_d2_046_hwd_basefill_051'], 'func': hwd_base_universe_d3_046_hwd_basefill_051}


def hwd_base_universe_d3_047_hwd_basefill_052(hwd_base_universe_d2_047_hwd_basefill_052):
    return _base_universe_d3(hwd_base_universe_d2_047_hwd_basefill_052, 47)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_047_hwd_basefill_052'] = {'inputs': ['hwd_base_universe_d2_047_hwd_basefill_052'], 'func': hwd_base_universe_d3_047_hwd_basefill_052}


def hwd_base_universe_d3_048_hwd_basefill_053(hwd_base_universe_d2_048_hwd_basefill_053):
    return _base_universe_d3(hwd_base_universe_d2_048_hwd_basefill_053, 48)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_048_hwd_basefill_053'] = {'inputs': ['hwd_base_universe_d2_048_hwd_basefill_053'], 'func': hwd_base_universe_d3_048_hwd_basefill_053}


def hwd_base_universe_d3_049_hwd_basefill_054(hwd_base_universe_d2_049_hwd_basefill_054):
    return _base_universe_d3(hwd_base_universe_d2_049_hwd_basefill_054, 49)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_049_hwd_basefill_054'] = {'inputs': ['hwd_base_universe_d2_049_hwd_basefill_054'], 'func': hwd_base_universe_d3_049_hwd_basefill_054}


def hwd_base_universe_d3_050_hwd_basefill_055(hwd_base_universe_d2_050_hwd_basefill_055):
    return _base_universe_d3(hwd_base_universe_d2_050_hwd_basefill_055, 50)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_050_hwd_basefill_055'] = {'inputs': ['hwd_base_universe_d2_050_hwd_basefill_055'], 'func': hwd_base_universe_d3_050_hwd_basefill_055}


def hwd_base_universe_d3_051_hwd_basefill_056(hwd_base_universe_d2_051_hwd_basefill_056):
    return _base_universe_d3(hwd_base_universe_d2_051_hwd_basefill_056, 51)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_051_hwd_basefill_056'] = {'inputs': ['hwd_base_universe_d2_051_hwd_basefill_056'], 'func': hwd_base_universe_d3_051_hwd_basefill_056}


def hwd_base_universe_d3_052_hwd_basefill_057(hwd_base_universe_d2_052_hwd_basefill_057):
    return _base_universe_d3(hwd_base_universe_d2_052_hwd_basefill_057, 52)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_052_hwd_basefill_057'] = {'inputs': ['hwd_base_universe_d2_052_hwd_basefill_057'], 'func': hwd_base_universe_d3_052_hwd_basefill_057}


def hwd_base_universe_d3_053_hwd_basefill_058(hwd_base_universe_d2_053_hwd_basefill_058):
    return _base_universe_d3(hwd_base_universe_d2_053_hwd_basefill_058, 53)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_053_hwd_basefill_058'] = {'inputs': ['hwd_base_universe_d2_053_hwd_basefill_058'], 'func': hwd_base_universe_d3_053_hwd_basefill_058}


def hwd_base_universe_d3_054_hwd_basefill_059(hwd_base_universe_d2_054_hwd_basefill_059):
    return _base_universe_d3(hwd_base_universe_d2_054_hwd_basefill_059, 54)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_054_hwd_basefill_059'] = {'inputs': ['hwd_base_universe_d2_054_hwd_basefill_059'], 'func': hwd_base_universe_d3_054_hwd_basefill_059}


def hwd_base_universe_d3_055_hwd_basefill_060(hwd_base_universe_d2_055_hwd_basefill_060):
    return _base_universe_d3(hwd_base_universe_d2_055_hwd_basefill_060, 55)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_055_hwd_basefill_060'] = {'inputs': ['hwd_base_universe_d2_055_hwd_basefill_060'], 'func': hwd_base_universe_d3_055_hwd_basefill_060}


def hwd_base_universe_d3_056_hwd_basefill_061(hwd_base_universe_d2_056_hwd_basefill_061):
    return _base_universe_d3(hwd_base_universe_d2_056_hwd_basefill_061, 56)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_056_hwd_basefill_061'] = {'inputs': ['hwd_base_universe_d2_056_hwd_basefill_061'], 'func': hwd_base_universe_d3_056_hwd_basefill_061}


def hwd_base_universe_d3_057_hwd_basefill_062(hwd_base_universe_d2_057_hwd_basefill_062):
    return _base_universe_d3(hwd_base_universe_d2_057_hwd_basefill_062, 57)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_057_hwd_basefill_062'] = {'inputs': ['hwd_base_universe_d2_057_hwd_basefill_062'], 'func': hwd_base_universe_d3_057_hwd_basefill_062}


def hwd_base_universe_d3_058_hwd_basefill_063(hwd_base_universe_d2_058_hwd_basefill_063):
    return _base_universe_d3(hwd_base_universe_d2_058_hwd_basefill_063, 58)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_058_hwd_basefill_063'] = {'inputs': ['hwd_base_universe_d2_058_hwd_basefill_063'], 'func': hwd_base_universe_d3_058_hwd_basefill_063}


def hwd_base_universe_d3_059_hwd_basefill_064(hwd_base_universe_d2_059_hwd_basefill_064):
    return _base_universe_d3(hwd_base_universe_d2_059_hwd_basefill_064, 59)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_059_hwd_basefill_064'] = {'inputs': ['hwd_base_universe_d2_059_hwd_basefill_064'], 'func': hwd_base_universe_d3_059_hwd_basefill_064}


def hwd_base_universe_d3_060_hwd_basefill_065(hwd_base_universe_d2_060_hwd_basefill_065):
    return _base_universe_d3(hwd_base_universe_d2_060_hwd_basefill_065, 60)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_060_hwd_basefill_065'] = {'inputs': ['hwd_base_universe_d2_060_hwd_basefill_065'], 'func': hwd_base_universe_d3_060_hwd_basefill_065}


def hwd_base_universe_d3_061_hwd_basefill_066(hwd_base_universe_d2_061_hwd_basefill_066):
    return _base_universe_d3(hwd_base_universe_d2_061_hwd_basefill_066, 61)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_061_hwd_basefill_066'] = {'inputs': ['hwd_base_universe_d2_061_hwd_basefill_066'], 'func': hwd_base_universe_d3_061_hwd_basefill_066}


def hwd_base_universe_d3_062_hwd_basefill_067(hwd_base_universe_d2_062_hwd_basefill_067):
    return _base_universe_d3(hwd_base_universe_d2_062_hwd_basefill_067, 62)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_062_hwd_basefill_067'] = {'inputs': ['hwd_base_universe_d2_062_hwd_basefill_067'], 'func': hwd_base_universe_d3_062_hwd_basefill_067}


def hwd_base_universe_d3_063_hwd_basefill_068(hwd_base_universe_d2_063_hwd_basefill_068):
    return _base_universe_d3(hwd_base_universe_d2_063_hwd_basefill_068, 63)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_063_hwd_basefill_068'] = {'inputs': ['hwd_base_universe_d2_063_hwd_basefill_068'], 'func': hwd_base_universe_d3_063_hwd_basefill_068}


def hwd_base_universe_d3_064_hwd_basefill_069(hwd_base_universe_d2_064_hwd_basefill_069):
    return _base_universe_d3(hwd_base_universe_d2_064_hwd_basefill_069, 64)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_064_hwd_basefill_069'] = {'inputs': ['hwd_base_universe_d2_064_hwd_basefill_069'], 'func': hwd_base_universe_d3_064_hwd_basefill_069}


def hwd_base_universe_d3_065_hwd_basefill_070(hwd_base_universe_d2_065_hwd_basefill_070):
    return _base_universe_d3(hwd_base_universe_d2_065_hwd_basefill_070, 65)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_065_hwd_basefill_070'] = {'inputs': ['hwd_base_universe_d2_065_hwd_basefill_070'], 'func': hwd_base_universe_d3_065_hwd_basefill_070}


def hwd_base_universe_d3_066_hwd_basefill_071(hwd_base_universe_d2_066_hwd_basefill_071):
    return _base_universe_d3(hwd_base_universe_d2_066_hwd_basefill_071, 66)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_066_hwd_basefill_071'] = {'inputs': ['hwd_base_universe_d2_066_hwd_basefill_071'], 'func': hwd_base_universe_d3_066_hwd_basefill_071}


def hwd_base_universe_d3_067_hwd_basefill_072(hwd_base_universe_d2_067_hwd_basefill_072):
    return _base_universe_d3(hwd_base_universe_d2_067_hwd_basefill_072, 67)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_067_hwd_basefill_072'] = {'inputs': ['hwd_base_universe_d2_067_hwd_basefill_072'], 'func': hwd_base_universe_d3_067_hwd_basefill_072}


def hwd_base_universe_d3_068_hwd_basefill_073(hwd_base_universe_d2_068_hwd_basefill_073):
    return _base_universe_d3(hwd_base_universe_d2_068_hwd_basefill_073, 68)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_068_hwd_basefill_073'] = {'inputs': ['hwd_base_universe_d2_068_hwd_basefill_073'], 'func': hwd_base_universe_d3_068_hwd_basefill_073}


def hwd_base_universe_d3_069_hwd_basefill_074(hwd_base_universe_d2_069_hwd_basefill_074):
    return _base_universe_d3(hwd_base_universe_d2_069_hwd_basefill_074, 69)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_069_hwd_basefill_074'] = {'inputs': ['hwd_base_universe_d2_069_hwd_basefill_074'], 'func': hwd_base_universe_d3_069_hwd_basefill_074}


def hwd_base_universe_d3_070_hwd_basefill_075(hwd_base_universe_d2_070_hwd_basefill_075):
    return _base_universe_d3(hwd_base_universe_d2_070_hwd_basefill_075, 70)
HWD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hwd_base_universe_d3_070_hwd_basefill_075'] = {'inputs': ['hwd_base_universe_d2_070_hwd_basefill_075'], 'func': hwd_base_universe_d3_070_hwd_basefill_075}
