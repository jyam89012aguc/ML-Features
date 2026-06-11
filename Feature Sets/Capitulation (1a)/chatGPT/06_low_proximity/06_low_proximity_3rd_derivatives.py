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



def lp_176_lp_001_drawdown_from_high_5_001_accel_1(lp_151_lp_001_drawdown_from_high_5_001_roc_1):
    feature = _s(lp_151_lp_001_drawdown_from_high_5_001_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def lp_177_lp_007_drawdown_from_high_126_007_accel_5(lp_152_lp_007_drawdown_from_high_126_007_roc_5):
    feature = _s(lp_152_lp_007_drawdown_from_high_126_007_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def lp_178_lp_013_drawdown_from_high_1008_013_accel_42(lp_153_lp_013_drawdown_from_high_1008_013_roc_42):
    feature = _s(lp_153_lp_013_drawdown_from_high_1008_013_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def lp_179_lp_019_drawdown_from_high_42_019_accel_126(lp_154_lp_019_drawdown_from_high_42_019_roc_126):
    feature = _s(lp_154_lp_019_drawdown_from_high_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def lp_180_lp_025_drawdown_from_high_378_025_accel_378(lp_155_lp_025_drawdown_from_high_378_025_roc_378):
    feature = _s(lp_155_lp_025_drawdown_from_high_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















LOW_PROXIMITY_REGISTRY_3RD_DERIVATIVES = {
    'lp_176_lp_001_drawdown_from_high_5_001_accel_1': {'inputs': ['lp_151_lp_001_drawdown_from_high_5_001_roc_1'], 'func': lp_176_lp_001_drawdown_from_high_5_001_accel_1},
    'lp_177_lp_007_drawdown_from_high_126_007_accel_5': {'inputs': ['lp_152_lp_007_drawdown_from_high_126_007_roc_5'], 'func': lp_177_lp_007_drawdown_from_high_126_007_accel_5},
    'lp_178_lp_013_drawdown_from_high_1008_013_accel_42': {'inputs': ['lp_153_lp_013_drawdown_from_high_1008_013_roc_42'], 'func': lp_178_lp_013_drawdown_from_high_1008_013_accel_42},
    'lp_179_lp_019_drawdown_from_high_42_019_accel_126': {'inputs': ['lp_154_lp_019_drawdown_from_high_42_019_roc_126'], 'func': lp_179_lp_019_drawdown_from_high_42_019_accel_126},
    'lp_180_lp_025_drawdown_from_high_378_025_accel_378': {'inputs': ['lp_155_lp_025_drawdown_from_high_378_025_roc_378'], 'func': lp_180_lp_025_drawdown_from_high_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def lp_replacement_d3_001(lp_replacement_d2_001):
    feature = _clean(lp_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_001'] = {'inputs': ['lp_replacement_d2_001'], 'func': lp_replacement_d3_001}


def lp_replacement_d3_002(lp_replacement_d2_002):
    feature = _clean(lp_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_002'] = {'inputs': ['lp_replacement_d2_002'], 'func': lp_replacement_d3_002}


def lp_replacement_d3_003(lp_replacement_d2_003):
    feature = _clean(lp_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_003'] = {'inputs': ['lp_replacement_d2_003'], 'func': lp_replacement_d3_003}


def lp_replacement_d3_004(lp_replacement_d2_004):
    feature = _clean(lp_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_004'] = {'inputs': ['lp_replacement_d2_004'], 'func': lp_replacement_d3_004}


def lp_replacement_d3_005(lp_replacement_d2_005):
    feature = _clean(lp_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_005'] = {'inputs': ['lp_replacement_d2_005'], 'func': lp_replacement_d3_005}


def lp_replacement_d3_006(lp_replacement_d2_006):
    feature = _clean(lp_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_006'] = {'inputs': ['lp_replacement_d2_006'], 'func': lp_replacement_d3_006}


def lp_replacement_d3_007(lp_replacement_d2_007):
    feature = _clean(lp_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_007'] = {'inputs': ['lp_replacement_d2_007'], 'func': lp_replacement_d3_007}


def lp_replacement_d3_008(lp_replacement_d2_008):
    feature = _clean(lp_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_008'] = {'inputs': ['lp_replacement_d2_008'], 'func': lp_replacement_d3_008}


def lp_replacement_d3_009(lp_replacement_d2_009):
    feature = _clean(lp_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_009'] = {'inputs': ['lp_replacement_d2_009'], 'func': lp_replacement_d3_009}


def lp_replacement_d3_010(lp_replacement_d2_010):
    feature = _clean(lp_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_010'] = {'inputs': ['lp_replacement_d2_010'], 'func': lp_replacement_d3_010}


def lp_replacement_d3_011(lp_replacement_d2_011):
    feature = _clean(lp_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_011'] = {'inputs': ['lp_replacement_d2_011'], 'func': lp_replacement_d3_011}


def lp_replacement_d3_012(lp_replacement_d2_012):
    feature = _clean(lp_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_012'] = {'inputs': ['lp_replacement_d2_012'], 'func': lp_replacement_d3_012}


def lp_replacement_d3_013(lp_replacement_d2_013):
    feature = _clean(lp_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_013'] = {'inputs': ['lp_replacement_d2_013'], 'func': lp_replacement_d3_013}


def lp_replacement_d3_014(lp_replacement_d2_014):
    feature = _clean(lp_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_014'] = {'inputs': ['lp_replacement_d2_014'], 'func': lp_replacement_d3_014}


def lp_replacement_d3_015(lp_replacement_d2_015):
    feature = _clean(lp_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_015'] = {'inputs': ['lp_replacement_d2_015'], 'func': lp_replacement_d3_015}


def lp_replacement_d3_016(lp_replacement_d2_016):
    feature = _clean(lp_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_016'] = {'inputs': ['lp_replacement_d2_016'], 'func': lp_replacement_d3_016}


def lp_replacement_d3_017(lp_replacement_d2_017):
    feature = _clean(lp_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_017'] = {'inputs': ['lp_replacement_d2_017'], 'func': lp_replacement_d3_017}


def lp_replacement_d3_018(lp_replacement_d2_018):
    feature = _clean(lp_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_018'] = {'inputs': ['lp_replacement_d2_018'], 'func': lp_replacement_d3_018}


def lp_replacement_d3_019(lp_replacement_d2_019):
    feature = _clean(lp_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_019'] = {'inputs': ['lp_replacement_d2_019'], 'func': lp_replacement_d3_019}


def lp_replacement_d3_020(lp_replacement_d2_020):
    feature = _clean(lp_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_020'] = {'inputs': ['lp_replacement_d2_020'], 'func': lp_replacement_d3_020}


def lp_replacement_d3_021(lp_replacement_d2_021):
    feature = _clean(lp_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_021'] = {'inputs': ['lp_replacement_d2_021'], 'func': lp_replacement_d3_021}


def lp_replacement_d3_022(lp_replacement_d2_022):
    feature = _clean(lp_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_022'] = {'inputs': ['lp_replacement_d2_022'], 'func': lp_replacement_d3_022}


def lp_replacement_d3_023(lp_replacement_d2_023):
    feature = _clean(lp_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_023'] = {'inputs': ['lp_replacement_d2_023'], 'func': lp_replacement_d3_023}


def lp_replacement_d3_024(lp_replacement_d2_024):
    feature = _clean(lp_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_024'] = {'inputs': ['lp_replacement_d2_024'], 'func': lp_replacement_d3_024}


def lp_replacement_d3_025(lp_replacement_d2_025):
    feature = _clean(lp_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_025'] = {'inputs': ['lp_replacement_d2_025'], 'func': lp_replacement_d3_025}


def lp_replacement_d3_026(lp_replacement_d2_026):
    feature = _clean(lp_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_026'] = {'inputs': ['lp_replacement_d2_026'], 'func': lp_replacement_d3_026}


def lp_replacement_d3_027(lp_replacement_d2_027):
    feature = _clean(lp_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_027'] = {'inputs': ['lp_replacement_d2_027'], 'func': lp_replacement_d3_027}


def lp_replacement_d3_028(lp_replacement_d2_028):
    feature = _clean(lp_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_028'] = {'inputs': ['lp_replacement_d2_028'], 'func': lp_replacement_d3_028}


def lp_replacement_d3_029(lp_replacement_d2_029):
    feature = _clean(lp_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_029'] = {'inputs': ['lp_replacement_d2_029'], 'func': lp_replacement_d3_029}


def lp_replacement_d3_030(lp_replacement_d2_030):
    feature = _clean(lp_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_030'] = {'inputs': ['lp_replacement_d2_030'], 'func': lp_replacement_d3_030}


def lp_replacement_d3_031(lp_replacement_d2_031):
    feature = _clean(lp_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_031'] = {'inputs': ['lp_replacement_d2_031'], 'func': lp_replacement_d3_031}


def lp_replacement_d3_032(lp_replacement_d2_032):
    feature = _clean(lp_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_032'] = {'inputs': ['lp_replacement_d2_032'], 'func': lp_replacement_d3_032}


def lp_replacement_d3_033(lp_replacement_d2_033):
    feature = _clean(lp_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_033'] = {'inputs': ['lp_replacement_d2_033'], 'func': lp_replacement_d3_033}


def lp_replacement_d3_034(lp_replacement_d2_034):
    feature = _clean(lp_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_034'] = {'inputs': ['lp_replacement_d2_034'], 'func': lp_replacement_d3_034}


def lp_replacement_d3_035(lp_replacement_d2_035):
    feature = _clean(lp_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_035'] = {'inputs': ['lp_replacement_d2_035'], 'func': lp_replacement_d3_035}


def lp_replacement_d3_036(lp_replacement_d2_036):
    feature = _clean(lp_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_036'] = {'inputs': ['lp_replacement_d2_036'], 'func': lp_replacement_d3_036}


def lp_replacement_d3_037(lp_replacement_d2_037):
    feature = _clean(lp_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_037'] = {'inputs': ['lp_replacement_d2_037'], 'func': lp_replacement_d3_037}


def lp_replacement_d3_038(lp_replacement_d2_038):
    feature = _clean(lp_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_038'] = {'inputs': ['lp_replacement_d2_038'], 'func': lp_replacement_d3_038}


def lp_replacement_d3_039(lp_replacement_d2_039):
    feature = _clean(lp_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_039'] = {'inputs': ['lp_replacement_d2_039'], 'func': lp_replacement_d3_039}


def lp_replacement_d3_040(lp_replacement_d2_040):
    feature = _clean(lp_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_040'] = {'inputs': ['lp_replacement_d2_040'], 'func': lp_replacement_d3_040}


def lp_replacement_d3_041(lp_replacement_d2_041):
    feature = _clean(lp_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_041'] = {'inputs': ['lp_replacement_d2_041'], 'func': lp_replacement_d3_041}


def lp_replacement_d3_042(lp_replacement_d2_042):
    feature = _clean(lp_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_042'] = {'inputs': ['lp_replacement_d2_042'], 'func': lp_replacement_d3_042}


def lp_replacement_d3_043(lp_replacement_d2_043):
    feature = _clean(lp_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_043'] = {'inputs': ['lp_replacement_d2_043'], 'func': lp_replacement_d3_043}


def lp_replacement_d3_044(lp_replacement_d2_044):
    feature = _clean(lp_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_044'] = {'inputs': ['lp_replacement_d2_044'], 'func': lp_replacement_d3_044}


def lp_replacement_d3_045(lp_replacement_d2_045):
    feature = _clean(lp_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_045'] = {'inputs': ['lp_replacement_d2_045'], 'func': lp_replacement_d3_045}


def lp_replacement_d3_046(lp_replacement_d2_046):
    feature = _clean(lp_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_046'] = {'inputs': ['lp_replacement_d2_046'], 'func': lp_replacement_d3_046}


def lp_replacement_d3_047(lp_replacement_d2_047):
    feature = _clean(lp_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_047'] = {'inputs': ['lp_replacement_d2_047'], 'func': lp_replacement_d3_047}


def lp_replacement_d3_048(lp_replacement_d2_048):
    feature = _clean(lp_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_048'] = {'inputs': ['lp_replacement_d2_048'], 'func': lp_replacement_d3_048}


def lp_replacement_d3_049(lp_replacement_d2_049):
    feature = _clean(lp_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_049'] = {'inputs': ['lp_replacement_d2_049'], 'func': lp_replacement_d3_049}


def lp_replacement_d3_050(lp_replacement_d2_050):
    feature = _clean(lp_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_050'] = {'inputs': ['lp_replacement_d2_050'], 'func': lp_replacement_d3_050}


def lp_replacement_d3_051(lp_replacement_d2_051):
    feature = _clean(lp_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_051'] = {'inputs': ['lp_replacement_d2_051'], 'func': lp_replacement_d3_051}


def lp_replacement_d3_052(lp_replacement_d2_052):
    feature = _clean(lp_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_052'] = {'inputs': ['lp_replacement_d2_052'], 'func': lp_replacement_d3_052}


def lp_replacement_d3_053(lp_replacement_d2_053):
    feature = _clean(lp_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_053'] = {'inputs': ['lp_replacement_d2_053'], 'func': lp_replacement_d3_053}


def lp_replacement_d3_054(lp_replacement_d2_054):
    feature = _clean(lp_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_054'] = {'inputs': ['lp_replacement_d2_054'], 'func': lp_replacement_d3_054}


def lp_replacement_d3_055(lp_replacement_d2_055):
    feature = _clean(lp_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_055'] = {'inputs': ['lp_replacement_d2_055'], 'func': lp_replacement_d3_055}


def lp_replacement_d3_056(lp_replacement_d2_056):
    feature = _clean(lp_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_056'] = {'inputs': ['lp_replacement_d2_056'], 'func': lp_replacement_d3_056}


def lp_replacement_d3_057(lp_replacement_d2_057):
    feature = _clean(lp_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_057'] = {'inputs': ['lp_replacement_d2_057'], 'func': lp_replacement_d3_057}


def lp_replacement_d3_058(lp_replacement_d2_058):
    feature = _clean(lp_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_058'] = {'inputs': ['lp_replacement_d2_058'], 'func': lp_replacement_d3_058}


def lp_replacement_d3_059(lp_replacement_d2_059):
    feature = _clean(lp_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_059'] = {'inputs': ['lp_replacement_d2_059'], 'func': lp_replacement_d3_059}


def lp_replacement_d3_060(lp_replacement_d2_060):
    feature = _clean(lp_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_060'] = {'inputs': ['lp_replacement_d2_060'], 'func': lp_replacement_d3_060}


def lp_replacement_d3_061(lp_replacement_d2_061):
    feature = _clean(lp_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_061'] = {'inputs': ['lp_replacement_d2_061'], 'func': lp_replacement_d3_061}


def lp_replacement_d3_062(lp_replacement_d2_062):
    feature = _clean(lp_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_062'] = {'inputs': ['lp_replacement_d2_062'], 'func': lp_replacement_d3_062}


def lp_replacement_d3_063(lp_replacement_d2_063):
    feature = _clean(lp_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_063'] = {'inputs': ['lp_replacement_d2_063'], 'func': lp_replacement_d3_063}


def lp_replacement_d3_064(lp_replacement_d2_064):
    feature = _clean(lp_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_064'] = {'inputs': ['lp_replacement_d2_064'], 'func': lp_replacement_d3_064}


def lp_replacement_d3_065(lp_replacement_d2_065):
    feature = _clean(lp_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_065'] = {'inputs': ['lp_replacement_d2_065'], 'func': lp_replacement_d3_065}


def lp_replacement_d3_066(lp_replacement_d2_066):
    feature = _clean(lp_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_066'] = {'inputs': ['lp_replacement_d2_066'], 'func': lp_replacement_d3_066}


def lp_replacement_d3_067(lp_replacement_d2_067):
    feature = _clean(lp_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_067'] = {'inputs': ['lp_replacement_d2_067'], 'func': lp_replacement_d3_067}


def lp_replacement_d3_068(lp_replacement_d2_068):
    feature = _clean(lp_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_068'] = {'inputs': ['lp_replacement_d2_068'], 'func': lp_replacement_d3_068}


def lp_replacement_d3_069(lp_replacement_d2_069):
    feature = _clean(lp_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_069'] = {'inputs': ['lp_replacement_d2_069'], 'func': lp_replacement_d3_069}


def lp_replacement_d3_070(lp_replacement_d2_070):
    feature = _clean(lp_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_070'] = {'inputs': ['lp_replacement_d2_070'], 'func': lp_replacement_d3_070}


def lp_replacement_d3_071(lp_replacement_d2_071):
    feature = _clean(lp_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_071'] = {'inputs': ['lp_replacement_d2_071'], 'func': lp_replacement_d3_071}


def lp_replacement_d3_072(lp_replacement_d2_072):
    feature = _clean(lp_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_072'] = {'inputs': ['lp_replacement_d2_072'], 'func': lp_replacement_d3_072}


def lp_replacement_d3_073(lp_replacement_d2_073):
    feature = _clean(lp_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_073'] = {'inputs': ['lp_replacement_d2_073'], 'func': lp_replacement_d3_073}


def lp_replacement_d3_074(lp_replacement_d2_074):
    feature = _clean(lp_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_074'] = {'inputs': ['lp_replacement_d2_074'], 'func': lp_replacement_d3_074}


def lp_replacement_d3_075(lp_replacement_d2_075):
    feature = _clean(lp_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_075'] = {'inputs': ['lp_replacement_d2_075'], 'func': lp_replacement_d3_075}


def lp_replacement_d3_076(lp_replacement_d2_076):
    feature = _clean(lp_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_076'] = {'inputs': ['lp_replacement_d2_076'], 'func': lp_replacement_d3_076}


def lp_replacement_d3_077(lp_replacement_d2_077):
    feature = _clean(lp_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_077'] = {'inputs': ['lp_replacement_d2_077'], 'func': lp_replacement_d3_077}


def lp_replacement_d3_078(lp_replacement_d2_078):
    feature = _clean(lp_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_078'] = {'inputs': ['lp_replacement_d2_078'], 'func': lp_replacement_d3_078}


def lp_replacement_d3_079(lp_replacement_d2_079):
    feature = _clean(lp_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_079'] = {'inputs': ['lp_replacement_d2_079'], 'func': lp_replacement_d3_079}


def lp_replacement_d3_080(lp_replacement_d2_080):
    feature = _clean(lp_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_080'] = {'inputs': ['lp_replacement_d2_080'], 'func': lp_replacement_d3_080}


def lp_replacement_d3_081(lp_replacement_d2_081):
    feature = _clean(lp_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_081'] = {'inputs': ['lp_replacement_d2_081'], 'func': lp_replacement_d3_081}


def lp_replacement_d3_082(lp_replacement_d2_082):
    feature = _clean(lp_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_082'] = {'inputs': ['lp_replacement_d2_082'], 'func': lp_replacement_d3_082}


def lp_replacement_d3_083(lp_replacement_d2_083):
    feature = _clean(lp_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_083'] = {'inputs': ['lp_replacement_d2_083'], 'func': lp_replacement_d3_083}


def lp_replacement_d3_084(lp_replacement_d2_084):
    feature = _clean(lp_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_084'] = {'inputs': ['lp_replacement_d2_084'], 'func': lp_replacement_d3_084}


def lp_replacement_d3_085(lp_replacement_d2_085):
    feature = _clean(lp_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_085'] = {'inputs': ['lp_replacement_d2_085'], 'func': lp_replacement_d3_085}


def lp_replacement_d3_086(lp_replacement_d2_086):
    feature = _clean(lp_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_086'] = {'inputs': ['lp_replacement_d2_086'], 'func': lp_replacement_d3_086}


def lp_replacement_d3_087(lp_replacement_d2_087):
    feature = _clean(lp_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_087'] = {'inputs': ['lp_replacement_d2_087'], 'func': lp_replacement_d3_087}


def lp_replacement_d3_088(lp_replacement_d2_088):
    feature = _clean(lp_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_088'] = {'inputs': ['lp_replacement_d2_088'], 'func': lp_replacement_d3_088}


def lp_replacement_d3_089(lp_replacement_d2_089):
    feature = _clean(lp_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_089'] = {'inputs': ['lp_replacement_d2_089'], 'func': lp_replacement_d3_089}


def lp_replacement_d3_090(lp_replacement_d2_090):
    feature = _clean(lp_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_090'] = {'inputs': ['lp_replacement_d2_090'], 'func': lp_replacement_d3_090}


def lp_replacement_d3_091(lp_replacement_d2_091):
    feature = _clean(lp_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_091'] = {'inputs': ['lp_replacement_d2_091'], 'func': lp_replacement_d3_091}


def lp_replacement_d3_092(lp_replacement_d2_092):
    feature = _clean(lp_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_092'] = {'inputs': ['lp_replacement_d2_092'], 'func': lp_replacement_d3_092}


def lp_replacement_d3_093(lp_replacement_d2_093):
    feature = _clean(lp_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_093'] = {'inputs': ['lp_replacement_d2_093'], 'func': lp_replacement_d3_093}


def lp_replacement_d3_094(lp_replacement_d2_094):
    feature = _clean(lp_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_094'] = {'inputs': ['lp_replacement_d2_094'], 'func': lp_replacement_d3_094}


def lp_replacement_d3_095(lp_replacement_d2_095):
    feature = _clean(lp_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_095'] = {'inputs': ['lp_replacement_d2_095'], 'func': lp_replacement_d3_095}


def lp_replacement_d3_096(lp_replacement_d2_096):
    feature = _clean(lp_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_096'] = {'inputs': ['lp_replacement_d2_096'], 'func': lp_replacement_d3_096}


def lp_replacement_d3_097(lp_replacement_d2_097):
    feature = _clean(lp_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_097'] = {'inputs': ['lp_replacement_d2_097'], 'func': lp_replacement_d3_097}


def lp_replacement_d3_098(lp_replacement_d2_098):
    feature = _clean(lp_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_098'] = {'inputs': ['lp_replacement_d2_098'], 'func': lp_replacement_d3_098}


def lp_replacement_d3_099(lp_replacement_d2_099):
    feature = _clean(lp_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_099'] = {'inputs': ['lp_replacement_d2_099'], 'func': lp_replacement_d3_099}


def lp_replacement_d3_100(lp_replacement_d2_100):
    feature = _clean(lp_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_100'] = {'inputs': ['lp_replacement_d2_100'], 'func': lp_replacement_d3_100}


def lp_replacement_d3_101(lp_replacement_d2_101):
    feature = _clean(lp_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_101'] = {'inputs': ['lp_replacement_d2_101'], 'func': lp_replacement_d3_101}


def lp_replacement_d3_102(lp_replacement_d2_102):
    feature = _clean(lp_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_102'] = {'inputs': ['lp_replacement_d2_102'], 'func': lp_replacement_d3_102}


def lp_replacement_d3_103(lp_replacement_d2_103):
    feature = _clean(lp_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_103'] = {'inputs': ['lp_replacement_d2_103'], 'func': lp_replacement_d3_103}


def lp_replacement_d3_104(lp_replacement_d2_104):
    feature = _clean(lp_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_104'] = {'inputs': ['lp_replacement_d2_104'], 'func': lp_replacement_d3_104}


def lp_replacement_d3_105(lp_replacement_d2_105):
    feature = _clean(lp_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_105'] = {'inputs': ['lp_replacement_d2_105'], 'func': lp_replacement_d3_105}


def lp_replacement_d3_106(lp_replacement_d2_106):
    feature = _clean(lp_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_106'] = {'inputs': ['lp_replacement_d2_106'], 'func': lp_replacement_d3_106}


def lp_replacement_d3_107(lp_replacement_d2_107):
    feature = _clean(lp_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_107'] = {'inputs': ['lp_replacement_d2_107'], 'func': lp_replacement_d3_107}


def lp_replacement_d3_108(lp_replacement_d2_108):
    feature = _clean(lp_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_108'] = {'inputs': ['lp_replacement_d2_108'], 'func': lp_replacement_d3_108}


def lp_replacement_d3_109(lp_replacement_d2_109):
    feature = _clean(lp_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_109'] = {'inputs': ['lp_replacement_d2_109'], 'func': lp_replacement_d3_109}


def lp_replacement_d3_110(lp_replacement_d2_110):
    feature = _clean(lp_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_110'] = {'inputs': ['lp_replacement_d2_110'], 'func': lp_replacement_d3_110}


def lp_replacement_d3_111(lp_replacement_d2_111):
    feature = _clean(lp_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_111'] = {'inputs': ['lp_replacement_d2_111'], 'func': lp_replacement_d3_111}


def lp_replacement_d3_112(lp_replacement_d2_112):
    feature = _clean(lp_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_112'] = {'inputs': ['lp_replacement_d2_112'], 'func': lp_replacement_d3_112}


def lp_replacement_d3_113(lp_replacement_d2_113):
    feature = _clean(lp_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_113'] = {'inputs': ['lp_replacement_d2_113'], 'func': lp_replacement_d3_113}


def lp_replacement_d3_114(lp_replacement_d2_114):
    feature = _clean(lp_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_114'] = {'inputs': ['lp_replacement_d2_114'], 'func': lp_replacement_d3_114}


def lp_replacement_d3_115(lp_replacement_d2_115):
    feature = _clean(lp_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_115'] = {'inputs': ['lp_replacement_d2_115'], 'func': lp_replacement_d3_115}


def lp_replacement_d3_116(lp_replacement_d2_116):
    feature = _clean(lp_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_116'] = {'inputs': ['lp_replacement_d2_116'], 'func': lp_replacement_d3_116}


def lp_replacement_d3_117(lp_replacement_d2_117):
    feature = _clean(lp_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_117'] = {'inputs': ['lp_replacement_d2_117'], 'func': lp_replacement_d3_117}


def lp_replacement_d3_118(lp_replacement_d2_118):
    feature = _clean(lp_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_118'] = {'inputs': ['lp_replacement_d2_118'], 'func': lp_replacement_d3_118}


def lp_replacement_d3_119(lp_replacement_d2_119):
    feature = _clean(lp_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_119'] = {'inputs': ['lp_replacement_d2_119'], 'func': lp_replacement_d3_119}


def lp_replacement_d3_120(lp_replacement_d2_120):
    feature = _clean(lp_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_120'] = {'inputs': ['lp_replacement_d2_120'], 'func': lp_replacement_d3_120}


def lp_replacement_d3_121(lp_replacement_d2_121):
    feature = _clean(lp_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_121'] = {'inputs': ['lp_replacement_d2_121'], 'func': lp_replacement_d3_121}


def lp_replacement_d3_122(lp_replacement_d2_122):
    feature = _clean(lp_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_122'] = {'inputs': ['lp_replacement_d2_122'], 'func': lp_replacement_d3_122}


def lp_replacement_d3_123(lp_replacement_d2_123):
    feature = _clean(lp_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_123'] = {'inputs': ['lp_replacement_d2_123'], 'func': lp_replacement_d3_123}


def lp_replacement_d3_124(lp_replacement_d2_124):
    feature = _clean(lp_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_124'] = {'inputs': ['lp_replacement_d2_124'], 'func': lp_replacement_d3_124}


def lp_replacement_d3_125(lp_replacement_d2_125):
    feature = _clean(lp_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_125'] = {'inputs': ['lp_replacement_d2_125'], 'func': lp_replacement_d3_125}


def lp_replacement_d3_126(lp_replacement_d2_126):
    feature = _clean(lp_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_126'] = {'inputs': ['lp_replacement_d2_126'], 'func': lp_replacement_d3_126}


def lp_replacement_d3_127(lp_replacement_d2_127):
    feature = _clean(lp_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_127'] = {'inputs': ['lp_replacement_d2_127'], 'func': lp_replacement_d3_127}


def lp_replacement_d3_128(lp_replacement_d2_128):
    feature = _clean(lp_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_128'] = {'inputs': ['lp_replacement_d2_128'], 'func': lp_replacement_d3_128}


def lp_replacement_d3_129(lp_replacement_d2_129):
    feature = _clean(lp_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_129'] = {'inputs': ['lp_replacement_d2_129'], 'func': lp_replacement_d3_129}


def lp_replacement_d3_130(lp_replacement_d2_130):
    feature = _clean(lp_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_130'] = {'inputs': ['lp_replacement_d2_130'], 'func': lp_replacement_d3_130}


def lp_replacement_d3_131(lp_replacement_d2_131):
    feature = _clean(lp_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_131'] = {'inputs': ['lp_replacement_d2_131'], 'func': lp_replacement_d3_131}


def lp_replacement_d3_132(lp_replacement_d2_132):
    feature = _clean(lp_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_132'] = {'inputs': ['lp_replacement_d2_132'], 'func': lp_replacement_d3_132}


def lp_replacement_d3_133(lp_replacement_d2_133):
    feature = _clean(lp_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_133'] = {'inputs': ['lp_replacement_d2_133'], 'func': lp_replacement_d3_133}


def lp_replacement_d3_134(lp_replacement_d2_134):
    feature = _clean(lp_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_134'] = {'inputs': ['lp_replacement_d2_134'], 'func': lp_replacement_d3_134}


def lp_replacement_d3_135(lp_replacement_d2_135):
    feature = _clean(lp_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_135'] = {'inputs': ['lp_replacement_d2_135'], 'func': lp_replacement_d3_135}


def lp_replacement_d3_136(lp_replacement_d2_136):
    feature = _clean(lp_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_136'] = {'inputs': ['lp_replacement_d2_136'], 'func': lp_replacement_d3_136}


def lp_replacement_d3_137(lp_replacement_d2_137):
    feature = _clean(lp_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_137'] = {'inputs': ['lp_replacement_d2_137'], 'func': lp_replacement_d3_137}


def lp_replacement_d3_138(lp_replacement_d2_138):
    feature = _clean(lp_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_138'] = {'inputs': ['lp_replacement_d2_138'], 'func': lp_replacement_d3_138}


def lp_replacement_d3_139(lp_replacement_d2_139):
    feature = _clean(lp_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_139'] = {'inputs': ['lp_replacement_d2_139'], 'func': lp_replacement_d3_139}


def lp_replacement_d3_140(lp_replacement_d2_140):
    feature = _clean(lp_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_140'] = {'inputs': ['lp_replacement_d2_140'], 'func': lp_replacement_d3_140}


def lp_replacement_d3_141(lp_replacement_d2_141):
    feature = _clean(lp_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_141'] = {'inputs': ['lp_replacement_d2_141'], 'func': lp_replacement_d3_141}


def lp_replacement_d3_142(lp_replacement_d2_142):
    feature = _clean(lp_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_142'] = {'inputs': ['lp_replacement_d2_142'], 'func': lp_replacement_d3_142}


def lp_replacement_d3_143(lp_replacement_d2_143):
    feature = _clean(lp_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_143'] = {'inputs': ['lp_replacement_d2_143'], 'func': lp_replacement_d3_143}


def lp_replacement_d3_144(lp_replacement_d2_144):
    feature = _clean(lp_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_144'] = {'inputs': ['lp_replacement_d2_144'], 'func': lp_replacement_d3_144}


def lp_replacement_d3_145(lp_replacement_d2_145):
    feature = _clean(lp_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_145'] = {'inputs': ['lp_replacement_d2_145'], 'func': lp_replacement_d3_145}


def lp_replacement_d3_146(lp_replacement_d2_146):
    feature = _clean(lp_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_146'] = {'inputs': ['lp_replacement_d2_146'], 'func': lp_replacement_d3_146}


def lp_replacement_d3_147(lp_replacement_d2_147):
    feature = _clean(lp_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_147'] = {'inputs': ['lp_replacement_d2_147'], 'func': lp_replacement_d3_147}


def lp_replacement_d3_148(lp_replacement_d2_148):
    feature = _clean(lp_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_148'] = {'inputs': ['lp_replacement_d2_148'], 'func': lp_replacement_d3_148}


def lp_replacement_d3_149(lp_replacement_d2_149):
    feature = _clean(lp_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_149'] = {'inputs': ['lp_replacement_d2_149'], 'func': lp_replacement_d3_149}


def lp_replacement_d3_150(lp_replacement_d2_150):
    feature = _clean(lp_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_150'] = {'inputs': ['lp_replacement_d2_150'], 'func': lp_replacement_d3_150}


def lp_replacement_d3_151(lp_replacement_d2_151):
    feature = _clean(lp_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_151'] = {'inputs': ['lp_replacement_d2_151'], 'func': lp_replacement_d3_151}


def lp_replacement_d3_152(lp_replacement_d2_152):
    feature = _clean(lp_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_152'] = {'inputs': ['lp_replacement_d2_152'], 'func': lp_replacement_d3_152}


def lp_replacement_d3_153(lp_replacement_d2_153):
    feature = _clean(lp_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_153'] = {'inputs': ['lp_replacement_d2_153'], 'func': lp_replacement_d3_153}


def lp_replacement_d3_154(lp_replacement_d2_154):
    feature = _clean(lp_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_154'] = {'inputs': ['lp_replacement_d2_154'], 'func': lp_replacement_d3_154}


def lp_replacement_d3_155(lp_replacement_d2_155):
    feature = _clean(lp_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_155'] = {'inputs': ['lp_replacement_d2_155'], 'func': lp_replacement_d3_155}


def lp_replacement_d3_156(lp_replacement_d2_156):
    feature = _clean(lp_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_156'] = {'inputs': ['lp_replacement_d2_156'], 'func': lp_replacement_d3_156}


def lp_replacement_d3_157(lp_replacement_d2_157):
    feature = _clean(lp_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_157'] = {'inputs': ['lp_replacement_d2_157'], 'func': lp_replacement_d3_157}


def lp_replacement_d3_158(lp_replacement_d2_158):
    feature = _clean(lp_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_158'] = {'inputs': ['lp_replacement_d2_158'], 'func': lp_replacement_d3_158}


def lp_replacement_d3_159(lp_replacement_d2_159):
    feature = _clean(lp_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_159'] = {'inputs': ['lp_replacement_d2_159'], 'func': lp_replacement_d3_159}


def lp_replacement_d3_160(lp_replacement_d2_160):
    feature = _clean(lp_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_160'] = {'inputs': ['lp_replacement_d2_160'], 'func': lp_replacement_d3_160}


def lp_replacement_d3_161(lp_replacement_d2_161):
    feature = _clean(lp_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_161'] = {'inputs': ['lp_replacement_d2_161'], 'func': lp_replacement_d3_161}


def lp_replacement_d3_162(lp_replacement_d2_162):
    feature = _clean(lp_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_162'] = {'inputs': ['lp_replacement_d2_162'], 'func': lp_replacement_d3_162}


def lp_replacement_d3_163(lp_replacement_d2_163):
    feature = _clean(lp_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_163'] = {'inputs': ['lp_replacement_d2_163'], 'func': lp_replacement_d3_163}


def lp_replacement_d3_164(lp_replacement_d2_164):
    feature = _clean(lp_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_164'] = {'inputs': ['lp_replacement_d2_164'], 'func': lp_replacement_d3_164}


def lp_replacement_d3_165(lp_replacement_d2_165):
    feature = _clean(lp_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_165'] = {'inputs': ['lp_replacement_d2_165'], 'func': lp_replacement_d3_165}


def lp_replacement_d3_166(lp_replacement_d2_166):
    feature = _clean(lp_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_166'] = {'inputs': ['lp_replacement_d2_166'], 'func': lp_replacement_d3_166}


def lp_replacement_d3_167(lp_replacement_d2_167):
    feature = _clean(lp_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_167'] = {'inputs': ['lp_replacement_d2_167'], 'func': lp_replacement_d3_167}


def lp_replacement_d3_168(lp_replacement_d2_168):
    feature = _clean(lp_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_168'] = {'inputs': ['lp_replacement_d2_168'], 'func': lp_replacement_d3_168}


def lp_replacement_d3_169(lp_replacement_d2_169):
    feature = _clean(lp_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_169'] = {'inputs': ['lp_replacement_d2_169'], 'func': lp_replacement_d3_169}


def lp_replacement_d3_170(lp_replacement_d2_170):
    feature = _clean(lp_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
LP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lp_replacement_d3_170'] = {'inputs': ['lp_replacement_d2_170'], 'func': lp_replacement_d3_170}


# Third-derivative extensions for repaired first-base features.
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def lp_base_universe_d3_001_lp_002_low_distance_10_002(lp_base_universe_d2_001_lp_002_low_distance_10_002):
    return _base_universe_d3(lp_base_universe_d2_001_lp_002_low_distance_10_002, 1)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_001_lp_002_low_distance_10_002'] = {'inputs': ['lp_base_universe_d2_001_lp_002_low_distance_10_002'], 'func': lp_base_universe_d3_001_lp_002_low_distance_10_002}


def lp_base_universe_d3_002_lp_003_underwater_area_21_003(lp_base_universe_d2_002_lp_003_underwater_area_21_003):
    return _base_universe_d3(lp_base_universe_d2_002_lp_003_underwater_area_21_003, 2)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_002_lp_003_underwater_area_21_003'] = {'inputs': ['lp_base_universe_d2_002_lp_003_underwater_area_21_003'], 'func': lp_base_universe_d3_002_lp_003_underwater_area_21_003}


def lp_base_universe_d3_003_lp_006_lower_high_ratio_84_006(lp_base_universe_d2_003_lp_006_lower_high_ratio_84_006):
    return _base_universe_d3(lp_base_universe_d2_003_lp_006_lower_high_ratio_84_006, 3)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_003_lp_006_lower_high_ratio_84_006'] = {'inputs': ['lp_base_universe_d2_003_lp_006_lower_high_ratio_84_006'], 'func': lp_base_universe_d3_003_lp_006_lower_high_ratio_84_006}


def lp_base_universe_d3_004_lp_008_low_distance_189_008(lp_base_universe_d2_004_lp_008_low_distance_189_008):
    return _base_universe_d3(lp_base_universe_d2_004_lp_008_low_distance_189_008, 4)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_004_lp_008_low_distance_189_008'] = {'inputs': ['lp_base_universe_d2_004_lp_008_low_distance_189_008'], 'func': lp_base_universe_d3_004_lp_008_low_distance_189_008}


def lp_base_universe_d3_005_lp_009_underwater_area_252_009(lp_base_universe_d2_005_lp_009_underwater_area_252_009):
    return _base_universe_d3(lp_base_universe_d2_005_lp_009_underwater_area_252_009, 5)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_005_lp_009_underwater_area_252_009'] = {'inputs': ['lp_base_universe_d2_005_lp_009_underwater_area_252_009'], 'func': lp_base_universe_d3_005_lp_009_underwater_area_252_009}


def lp_base_universe_d3_006_lp_012_lower_high_ratio_756_012(lp_base_universe_d2_006_lp_012_lower_high_ratio_756_012):
    return _base_universe_d3(lp_base_universe_d2_006_lp_012_lower_high_ratio_756_012, 6)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_006_lp_012_lower_high_ratio_756_012'] = {'inputs': ['lp_base_universe_d2_006_lp_012_lower_high_ratio_756_012'], 'func': lp_base_universe_d3_006_lp_012_lower_high_ratio_756_012}


def lp_base_universe_d3_007_lp_014_low_distance_1260_014(lp_base_universe_d2_007_lp_014_low_distance_1260_014):
    return _base_universe_d3(lp_base_universe_d2_007_lp_014_low_distance_1260_014, 7)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_007_lp_014_low_distance_1260_014'] = {'inputs': ['lp_base_universe_d2_007_lp_014_low_distance_1260_014'], 'func': lp_base_universe_d3_007_lp_014_low_distance_1260_014}


def lp_base_universe_d3_008_lp_015_underwater_area_1512_015(lp_base_universe_d2_008_lp_015_underwater_area_1512_015):
    return _base_universe_d3(lp_base_universe_d2_008_lp_015_underwater_area_1512_015, 8)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_008_lp_015_underwater_area_1512_015'] = {'inputs': ['lp_base_universe_d2_008_lp_015_underwater_area_1512_015'], 'func': lp_base_universe_d3_008_lp_015_underwater_area_1512_015}


def lp_base_universe_d3_009_lp_018_lower_high_ratio_21_018(lp_base_universe_d2_009_lp_018_lower_high_ratio_21_018):
    return _base_universe_d3(lp_base_universe_d2_009_lp_018_lower_high_ratio_21_018, 9)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_009_lp_018_lower_high_ratio_21_018'] = {'inputs': ['lp_base_universe_d2_009_lp_018_lower_high_ratio_21_018'], 'func': lp_base_universe_d3_009_lp_018_lower_high_ratio_21_018}


def lp_base_universe_d3_010_lp_020_low_distance_63_020(lp_base_universe_d2_010_lp_020_low_distance_63_020):
    return _base_universe_d3(lp_base_universe_d2_010_lp_020_low_distance_63_020, 10)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_010_lp_020_low_distance_63_020'] = {'inputs': ['lp_base_universe_d2_010_lp_020_low_distance_63_020'], 'func': lp_base_universe_d3_010_lp_020_low_distance_63_020}


def lp_base_universe_d3_011_lp_021_underwater_area_84_021(lp_base_universe_d2_011_lp_021_underwater_area_84_021):
    return _base_universe_d3(lp_base_universe_d2_011_lp_021_underwater_area_84_021, 11)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_011_lp_021_underwater_area_84_021'] = {'inputs': ['lp_base_universe_d2_011_lp_021_underwater_area_84_021'], 'func': lp_base_universe_d3_011_lp_021_underwater_area_84_021}


def lp_base_universe_d3_012_lp_024_lower_high_ratio_252_024(lp_base_universe_d2_012_lp_024_lower_high_ratio_252_024):
    return _base_universe_d3(lp_base_universe_d2_012_lp_024_lower_high_ratio_252_024, 12)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_012_lp_024_lower_high_ratio_252_024'] = {'inputs': ['lp_base_universe_d2_012_lp_024_lower_high_ratio_252_024'], 'func': lp_base_universe_d3_012_lp_024_lower_high_ratio_252_024}


def lp_base_universe_d3_013_lp_026_low_distance_504_026(lp_base_universe_d2_013_lp_026_low_distance_504_026):
    return _base_universe_d3(lp_base_universe_d2_013_lp_026_low_distance_504_026, 13)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_013_lp_026_low_distance_504_026'] = {'inputs': ['lp_base_universe_d2_013_lp_026_low_distance_504_026'], 'func': lp_base_universe_d3_013_lp_026_low_distance_504_026}


def lp_base_universe_d3_014_lp_027_underwater_area_756_027(lp_base_universe_d2_014_lp_027_underwater_area_756_027):
    return _base_universe_d3(lp_base_universe_d2_014_lp_027_underwater_area_756_027, 14)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_014_lp_027_underwater_area_756_027'] = {'inputs': ['lp_base_universe_d2_014_lp_027_underwater_area_756_027'], 'func': lp_base_universe_d3_014_lp_027_underwater_area_756_027}


def lp_base_universe_d3_015_lp_030_lower_high_ratio_1512_030(lp_base_universe_d2_015_lp_030_lower_high_ratio_1512_030):
    return _base_universe_d3(lp_base_universe_d2_015_lp_030_lower_high_ratio_1512_030, 15)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_015_lp_030_lower_high_ratio_1512_030'] = {'inputs': ['lp_base_universe_d2_015_lp_030_lower_high_ratio_1512_030'], 'func': lp_base_universe_d3_015_lp_030_lower_high_ratio_1512_030}


def lp_base_universe_d3_016_lp_basefill_004(lp_base_universe_d2_016_lp_basefill_004):
    return _base_universe_d3(lp_base_universe_d2_016_lp_basefill_004, 16)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_016_lp_basefill_004'] = {'inputs': ['lp_base_universe_d2_016_lp_basefill_004'], 'func': lp_base_universe_d3_016_lp_basefill_004}


def lp_base_universe_d3_017_lp_basefill_005(lp_base_universe_d2_017_lp_basefill_005):
    return _base_universe_d3(lp_base_universe_d2_017_lp_basefill_005, 17)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_017_lp_basefill_005'] = {'inputs': ['lp_base_universe_d2_017_lp_basefill_005'], 'func': lp_base_universe_d3_017_lp_basefill_005}


def lp_base_universe_d3_018_lp_basefill_010(lp_base_universe_d2_018_lp_basefill_010):
    return _base_universe_d3(lp_base_universe_d2_018_lp_basefill_010, 18)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_018_lp_basefill_010'] = {'inputs': ['lp_base_universe_d2_018_lp_basefill_010'], 'func': lp_base_universe_d3_018_lp_basefill_010}


def lp_base_universe_d3_019_lp_basefill_011(lp_base_universe_d2_019_lp_basefill_011):
    return _base_universe_d3(lp_base_universe_d2_019_lp_basefill_011, 19)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_019_lp_basefill_011'] = {'inputs': ['lp_base_universe_d2_019_lp_basefill_011'], 'func': lp_base_universe_d3_019_lp_basefill_011}


def lp_base_universe_d3_020_lp_basefill_016(lp_base_universe_d2_020_lp_basefill_016):
    return _base_universe_d3(lp_base_universe_d2_020_lp_basefill_016, 20)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_020_lp_basefill_016'] = {'inputs': ['lp_base_universe_d2_020_lp_basefill_016'], 'func': lp_base_universe_d3_020_lp_basefill_016}


def lp_base_universe_d3_021_lp_basefill_017(lp_base_universe_d2_021_lp_basefill_017):
    return _base_universe_d3(lp_base_universe_d2_021_lp_basefill_017, 21)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_021_lp_basefill_017'] = {'inputs': ['lp_base_universe_d2_021_lp_basefill_017'], 'func': lp_base_universe_d3_021_lp_basefill_017}


def lp_base_universe_d3_022_lp_basefill_022(lp_base_universe_d2_022_lp_basefill_022):
    return _base_universe_d3(lp_base_universe_d2_022_lp_basefill_022, 22)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_022_lp_basefill_022'] = {'inputs': ['lp_base_universe_d2_022_lp_basefill_022'], 'func': lp_base_universe_d3_022_lp_basefill_022}


def lp_base_universe_d3_023_lp_basefill_023(lp_base_universe_d2_023_lp_basefill_023):
    return _base_universe_d3(lp_base_universe_d2_023_lp_basefill_023, 23)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_023_lp_basefill_023'] = {'inputs': ['lp_base_universe_d2_023_lp_basefill_023'], 'func': lp_base_universe_d3_023_lp_basefill_023}


def lp_base_universe_d3_024_lp_basefill_028(lp_base_universe_d2_024_lp_basefill_028):
    return _base_universe_d3(lp_base_universe_d2_024_lp_basefill_028, 24)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_024_lp_basefill_028'] = {'inputs': ['lp_base_universe_d2_024_lp_basefill_028'], 'func': lp_base_universe_d3_024_lp_basefill_028}


def lp_base_universe_d3_025_lp_basefill_029(lp_base_universe_d2_025_lp_basefill_029):
    return _base_universe_d3(lp_base_universe_d2_025_lp_basefill_029, 25)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_025_lp_basefill_029'] = {'inputs': ['lp_base_universe_d2_025_lp_basefill_029'], 'func': lp_base_universe_d3_025_lp_basefill_029}


def lp_base_universe_d3_026_lp_basefill_031(lp_base_universe_d2_026_lp_basefill_031):
    return _base_universe_d3(lp_base_universe_d2_026_lp_basefill_031, 26)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_026_lp_basefill_031'] = {'inputs': ['lp_base_universe_d2_026_lp_basefill_031'], 'func': lp_base_universe_d3_026_lp_basefill_031}


def lp_base_universe_d3_027_lp_basefill_032(lp_base_universe_d2_027_lp_basefill_032):
    return _base_universe_d3(lp_base_universe_d2_027_lp_basefill_032, 27)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_027_lp_basefill_032'] = {'inputs': ['lp_base_universe_d2_027_lp_basefill_032'], 'func': lp_base_universe_d3_027_lp_basefill_032}


def lp_base_universe_d3_028_lp_basefill_033(lp_base_universe_d2_028_lp_basefill_033):
    return _base_universe_d3(lp_base_universe_d2_028_lp_basefill_033, 28)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_028_lp_basefill_033'] = {'inputs': ['lp_base_universe_d2_028_lp_basefill_033'], 'func': lp_base_universe_d3_028_lp_basefill_033}


def lp_base_universe_d3_029_lp_basefill_034(lp_base_universe_d2_029_lp_basefill_034):
    return _base_universe_d3(lp_base_universe_d2_029_lp_basefill_034, 29)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_029_lp_basefill_034'] = {'inputs': ['lp_base_universe_d2_029_lp_basefill_034'], 'func': lp_base_universe_d3_029_lp_basefill_034}


def lp_base_universe_d3_030_lp_basefill_035(lp_base_universe_d2_030_lp_basefill_035):
    return _base_universe_d3(lp_base_universe_d2_030_lp_basefill_035, 30)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_030_lp_basefill_035'] = {'inputs': ['lp_base_universe_d2_030_lp_basefill_035'], 'func': lp_base_universe_d3_030_lp_basefill_035}


def lp_base_universe_d3_031_lp_basefill_036(lp_base_universe_d2_031_lp_basefill_036):
    return _base_universe_d3(lp_base_universe_d2_031_lp_basefill_036, 31)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_031_lp_basefill_036'] = {'inputs': ['lp_base_universe_d2_031_lp_basefill_036'], 'func': lp_base_universe_d3_031_lp_basefill_036}


def lp_base_universe_d3_032_lp_basefill_037(lp_base_universe_d2_032_lp_basefill_037):
    return _base_universe_d3(lp_base_universe_d2_032_lp_basefill_037, 32)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_032_lp_basefill_037'] = {'inputs': ['lp_base_universe_d2_032_lp_basefill_037'], 'func': lp_base_universe_d3_032_lp_basefill_037}


def lp_base_universe_d3_033_lp_basefill_038(lp_base_universe_d2_033_lp_basefill_038):
    return _base_universe_d3(lp_base_universe_d2_033_lp_basefill_038, 33)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_033_lp_basefill_038'] = {'inputs': ['lp_base_universe_d2_033_lp_basefill_038'], 'func': lp_base_universe_d3_033_lp_basefill_038}


def lp_base_universe_d3_034_lp_basefill_039(lp_base_universe_d2_034_lp_basefill_039):
    return _base_universe_d3(lp_base_universe_d2_034_lp_basefill_039, 34)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_034_lp_basefill_039'] = {'inputs': ['lp_base_universe_d2_034_lp_basefill_039'], 'func': lp_base_universe_d3_034_lp_basefill_039}


def lp_base_universe_d3_035_lp_basefill_040(lp_base_universe_d2_035_lp_basefill_040):
    return _base_universe_d3(lp_base_universe_d2_035_lp_basefill_040, 35)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_035_lp_basefill_040'] = {'inputs': ['lp_base_universe_d2_035_lp_basefill_040'], 'func': lp_base_universe_d3_035_lp_basefill_040}


def lp_base_universe_d3_036_lp_basefill_041(lp_base_universe_d2_036_lp_basefill_041):
    return _base_universe_d3(lp_base_universe_d2_036_lp_basefill_041, 36)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_036_lp_basefill_041'] = {'inputs': ['lp_base_universe_d2_036_lp_basefill_041'], 'func': lp_base_universe_d3_036_lp_basefill_041}


def lp_base_universe_d3_037_lp_basefill_042(lp_base_universe_d2_037_lp_basefill_042):
    return _base_universe_d3(lp_base_universe_d2_037_lp_basefill_042, 37)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_037_lp_basefill_042'] = {'inputs': ['lp_base_universe_d2_037_lp_basefill_042'], 'func': lp_base_universe_d3_037_lp_basefill_042}


def lp_base_universe_d3_038_lp_basefill_043(lp_base_universe_d2_038_lp_basefill_043):
    return _base_universe_d3(lp_base_universe_d2_038_lp_basefill_043, 38)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_038_lp_basefill_043'] = {'inputs': ['lp_base_universe_d2_038_lp_basefill_043'], 'func': lp_base_universe_d3_038_lp_basefill_043}


def lp_base_universe_d3_039_lp_basefill_044(lp_base_universe_d2_039_lp_basefill_044):
    return _base_universe_d3(lp_base_universe_d2_039_lp_basefill_044, 39)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_039_lp_basefill_044'] = {'inputs': ['lp_base_universe_d2_039_lp_basefill_044'], 'func': lp_base_universe_d3_039_lp_basefill_044}


def lp_base_universe_d3_040_lp_basefill_045(lp_base_universe_d2_040_lp_basefill_045):
    return _base_universe_d3(lp_base_universe_d2_040_lp_basefill_045, 40)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_040_lp_basefill_045'] = {'inputs': ['lp_base_universe_d2_040_lp_basefill_045'], 'func': lp_base_universe_d3_040_lp_basefill_045}


def lp_base_universe_d3_041_lp_basefill_046(lp_base_universe_d2_041_lp_basefill_046):
    return _base_universe_d3(lp_base_universe_d2_041_lp_basefill_046, 41)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_041_lp_basefill_046'] = {'inputs': ['lp_base_universe_d2_041_lp_basefill_046'], 'func': lp_base_universe_d3_041_lp_basefill_046}


def lp_base_universe_d3_042_lp_basefill_047(lp_base_universe_d2_042_lp_basefill_047):
    return _base_universe_d3(lp_base_universe_d2_042_lp_basefill_047, 42)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_042_lp_basefill_047'] = {'inputs': ['lp_base_universe_d2_042_lp_basefill_047'], 'func': lp_base_universe_d3_042_lp_basefill_047}


def lp_base_universe_d3_043_lp_basefill_048(lp_base_universe_d2_043_lp_basefill_048):
    return _base_universe_d3(lp_base_universe_d2_043_lp_basefill_048, 43)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_043_lp_basefill_048'] = {'inputs': ['lp_base_universe_d2_043_lp_basefill_048'], 'func': lp_base_universe_d3_043_lp_basefill_048}


def lp_base_universe_d3_044_lp_basefill_049(lp_base_universe_d2_044_lp_basefill_049):
    return _base_universe_d3(lp_base_universe_d2_044_lp_basefill_049, 44)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_044_lp_basefill_049'] = {'inputs': ['lp_base_universe_d2_044_lp_basefill_049'], 'func': lp_base_universe_d3_044_lp_basefill_049}


def lp_base_universe_d3_045_lp_basefill_050(lp_base_universe_d2_045_lp_basefill_050):
    return _base_universe_d3(lp_base_universe_d2_045_lp_basefill_050, 45)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_045_lp_basefill_050'] = {'inputs': ['lp_base_universe_d2_045_lp_basefill_050'], 'func': lp_base_universe_d3_045_lp_basefill_050}


def lp_base_universe_d3_046_lp_basefill_051(lp_base_universe_d2_046_lp_basefill_051):
    return _base_universe_d3(lp_base_universe_d2_046_lp_basefill_051, 46)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_046_lp_basefill_051'] = {'inputs': ['lp_base_universe_d2_046_lp_basefill_051'], 'func': lp_base_universe_d3_046_lp_basefill_051}


def lp_base_universe_d3_047_lp_basefill_052(lp_base_universe_d2_047_lp_basefill_052):
    return _base_universe_d3(lp_base_universe_d2_047_lp_basefill_052, 47)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_047_lp_basefill_052'] = {'inputs': ['lp_base_universe_d2_047_lp_basefill_052'], 'func': lp_base_universe_d3_047_lp_basefill_052}


def lp_base_universe_d3_048_lp_basefill_053(lp_base_universe_d2_048_lp_basefill_053):
    return _base_universe_d3(lp_base_universe_d2_048_lp_basefill_053, 48)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_048_lp_basefill_053'] = {'inputs': ['lp_base_universe_d2_048_lp_basefill_053'], 'func': lp_base_universe_d3_048_lp_basefill_053}


def lp_base_universe_d3_049_lp_basefill_054(lp_base_universe_d2_049_lp_basefill_054):
    return _base_universe_d3(lp_base_universe_d2_049_lp_basefill_054, 49)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_049_lp_basefill_054'] = {'inputs': ['lp_base_universe_d2_049_lp_basefill_054'], 'func': lp_base_universe_d3_049_lp_basefill_054}


def lp_base_universe_d3_050_lp_basefill_055(lp_base_universe_d2_050_lp_basefill_055):
    return _base_universe_d3(lp_base_universe_d2_050_lp_basefill_055, 50)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_050_lp_basefill_055'] = {'inputs': ['lp_base_universe_d2_050_lp_basefill_055'], 'func': lp_base_universe_d3_050_lp_basefill_055}


def lp_base_universe_d3_051_lp_basefill_056(lp_base_universe_d2_051_lp_basefill_056):
    return _base_universe_d3(lp_base_universe_d2_051_lp_basefill_056, 51)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_051_lp_basefill_056'] = {'inputs': ['lp_base_universe_d2_051_lp_basefill_056'], 'func': lp_base_universe_d3_051_lp_basefill_056}


def lp_base_universe_d3_052_lp_basefill_057(lp_base_universe_d2_052_lp_basefill_057):
    return _base_universe_d3(lp_base_universe_d2_052_lp_basefill_057, 52)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_052_lp_basefill_057'] = {'inputs': ['lp_base_universe_d2_052_lp_basefill_057'], 'func': lp_base_universe_d3_052_lp_basefill_057}


def lp_base_universe_d3_053_lp_basefill_058(lp_base_universe_d2_053_lp_basefill_058):
    return _base_universe_d3(lp_base_universe_d2_053_lp_basefill_058, 53)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_053_lp_basefill_058'] = {'inputs': ['lp_base_universe_d2_053_lp_basefill_058'], 'func': lp_base_universe_d3_053_lp_basefill_058}


def lp_base_universe_d3_054_lp_basefill_059(lp_base_universe_d2_054_lp_basefill_059):
    return _base_universe_d3(lp_base_universe_d2_054_lp_basefill_059, 54)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_054_lp_basefill_059'] = {'inputs': ['lp_base_universe_d2_054_lp_basefill_059'], 'func': lp_base_universe_d3_054_lp_basefill_059}


def lp_base_universe_d3_055_lp_basefill_060(lp_base_universe_d2_055_lp_basefill_060):
    return _base_universe_d3(lp_base_universe_d2_055_lp_basefill_060, 55)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_055_lp_basefill_060'] = {'inputs': ['lp_base_universe_d2_055_lp_basefill_060'], 'func': lp_base_universe_d3_055_lp_basefill_060}


def lp_base_universe_d3_056_lp_basefill_061(lp_base_universe_d2_056_lp_basefill_061):
    return _base_universe_d3(lp_base_universe_d2_056_lp_basefill_061, 56)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_056_lp_basefill_061'] = {'inputs': ['lp_base_universe_d2_056_lp_basefill_061'], 'func': lp_base_universe_d3_056_lp_basefill_061}


def lp_base_universe_d3_057_lp_basefill_062(lp_base_universe_d2_057_lp_basefill_062):
    return _base_universe_d3(lp_base_universe_d2_057_lp_basefill_062, 57)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_057_lp_basefill_062'] = {'inputs': ['lp_base_universe_d2_057_lp_basefill_062'], 'func': lp_base_universe_d3_057_lp_basefill_062}


def lp_base_universe_d3_058_lp_basefill_063(lp_base_universe_d2_058_lp_basefill_063):
    return _base_universe_d3(lp_base_universe_d2_058_lp_basefill_063, 58)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_058_lp_basefill_063'] = {'inputs': ['lp_base_universe_d2_058_lp_basefill_063'], 'func': lp_base_universe_d3_058_lp_basefill_063}


def lp_base_universe_d3_059_lp_basefill_064(lp_base_universe_d2_059_lp_basefill_064):
    return _base_universe_d3(lp_base_universe_d2_059_lp_basefill_064, 59)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_059_lp_basefill_064'] = {'inputs': ['lp_base_universe_d2_059_lp_basefill_064'], 'func': lp_base_universe_d3_059_lp_basefill_064}


def lp_base_universe_d3_060_lp_basefill_065(lp_base_universe_d2_060_lp_basefill_065):
    return _base_universe_d3(lp_base_universe_d2_060_lp_basefill_065, 60)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_060_lp_basefill_065'] = {'inputs': ['lp_base_universe_d2_060_lp_basefill_065'], 'func': lp_base_universe_d3_060_lp_basefill_065}


def lp_base_universe_d3_061_lp_basefill_066(lp_base_universe_d2_061_lp_basefill_066):
    return _base_universe_d3(lp_base_universe_d2_061_lp_basefill_066, 61)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_061_lp_basefill_066'] = {'inputs': ['lp_base_universe_d2_061_lp_basefill_066'], 'func': lp_base_universe_d3_061_lp_basefill_066}


def lp_base_universe_d3_062_lp_basefill_067(lp_base_universe_d2_062_lp_basefill_067):
    return _base_universe_d3(lp_base_universe_d2_062_lp_basefill_067, 62)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_062_lp_basefill_067'] = {'inputs': ['lp_base_universe_d2_062_lp_basefill_067'], 'func': lp_base_universe_d3_062_lp_basefill_067}


def lp_base_universe_d3_063_lp_basefill_068(lp_base_universe_d2_063_lp_basefill_068):
    return _base_universe_d3(lp_base_universe_d2_063_lp_basefill_068, 63)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_063_lp_basefill_068'] = {'inputs': ['lp_base_universe_d2_063_lp_basefill_068'], 'func': lp_base_universe_d3_063_lp_basefill_068}


def lp_base_universe_d3_064_lp_basefill_069(lp_base_universe_d2_064_lp_basefill_069):
    return _base_universe_d3(lp_base_universe_d2_064_lp_basefill_069, 64)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_064_lp_basefill_069'] = {'inputs': ['lp_base_universe_d2_064_lp_basefill_069'], 'func': lp_base_universe_d3_064_lp_basefill_069}


def lp_base_universe_d3_065_lp_basefill_070(lp_base_universe_d2_065_lp_basefill_070):
    return _base_universe_d3(lp_base_universe_d2_065_lp_basefill_070, 65)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_065_lp_basefill_070'] = {'inputs': ['lp_base_universe_d2_065_lp_basefill_070'], 'func': lp_base_universe_d3_065_lp_basefill_070}


def lp_base_universe_d3_066_lp_basefill_071(lp_base_universe_d2_066_lp_basefill_071):
    return _base_universe_d3(lp_base_universe_d2_066_lp_basefill_071, 66)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_066_lp_basefill_071'] = {'inputs': ['lp_base_universe_d2_066_lp_basefill_071'], 'func': lp_base_universe_d3_066_lp_basefill_071}


def lp_base_universe_d3_067_lp_basefill_072(lp_base_universe_d2_067_lp_basefill_072):
    return _base_universe_d3(lp_base_universe_d2_067_lp_basefill_072, 67)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_067_lp_basefill_072'] = {'inputs': ['lp_base_universe_d2_067_lp_basefill_072'], 'func': lp_base_universe_d3_067_lp_basefill_072}


def lp_base_universe_d3_068_lp_basefill_073(lp_base_universe_d2_068_lp_basefill_073):
    return _base_universe_d3(lp_base_universe_d2_068_lp_basefill_073, 68)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_068_lp_basefill_073'] = {'inputs': ['lp_base_universe_d2_068_lp_basefill_073'], 'func': lp_base_universe_d3_068_lp_basefill_073}


def lp_base_universe_d3_069_lp_basefill_074(lp_base_universe_d2_069_lp_basefill_074):
    return _base_universe_d3(lp_base_universe_d2_069_lp_basefill_074, 69)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_069_lp_basefill_074'] = {'inputs': ['lp_base_universe_d2_069_lp_basefill_074'], 'func': lp_base_universe_d3_069_lp_basefill_074}


def lp_base_universe_d3_070_lp_basefill_075(lp_base_universe_d2_070_lp_basefill_075):
    return _base_universe_d3(lp_base_universe_d2_070_lp_basefill_075, 70)
LP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lp_base_universe_d3_070_lp_basefill_075'] = {'inputs': ['lp_base_universe_d2_070_lp_basefill_075'], 'func': lp_base_universe_d3_070_lp_basefill_075}
