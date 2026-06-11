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



def gap_176_gap_001_gap_down_frequency_5_001_accel_1(gap_151_gap_001_gap_down_frequency_5_001_roc_1):
    feature = _s(gap_151_gap_001_gap_down_frequency_5_001_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def gap_177_gap_007_gap_down_frequency_126_007_accel_5(gap_152_gap_007_gap_down_frequency_126_007_roc_5):
    feature = _s(gap_152_gap_007_gap_down_frequency_126_007_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def gap_178_gap_013_gap_down_frequency_1008_013_accel_42(gap_153_gap_013_gap_down_frequency_1008_013_roc_42):
    feature = _s(gap_153_gap_013_gap_down_frequency_1008_013_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def gap_179_gap_019_gap_down_frequency_42_019_accel_126(gap_154_gap_019_gap_down_frequency_42_019_roc_126):
    feature = _s(gap_154_gap_019_gap_down_frequency_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def gap_180_gap_025_gap_down_frequency_378_025_accel_378(gap_155_gap_025_gap_down_frequency_378_025_roc_378):
    feature = _s(gap_155_gap_025_gap_down_frequency_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















GAP_STRUCTURE_REGISTRY_3RD_DERIVATIVES = {
    'gap_176_gap_001_gap_down_frequency_5_001_accel_1': {'inputs': ['gap_151_gap_001_gap_down_frequency_5_001_roc_1'], 'func': gap_176_gap_001_gap_down_frequency_5_001_accel_1},
    'gap_177_gap_007_gap_down_frequency_126_007_accel_5': {'inputs': ['gap_152_gap_007_gap_down_frequency_126_007_roc_5'], 'func': gap_177_gap_007_gap_down_frequency_126_007_accel_5},
    'gap_178_gap_013_gap_down_frequency_1008_013_accel_42': {'inputs': ['gap_153_gap_013_gap_down_frequency_1008_013_roc_42'], 'func': gap_178_gap_013_gap_down_frequency_1008_013_accel_42},
    'gap_179_gap_019_gap_down_frequency_42_019_accel_126': {'inputs': ['gap_154_gap_019_gap_down_frequency_42_019_roc_126'], 'func': gap_179_gap_019_gap_down_frequency_42_019_accel_126},
    'gap_180_gap_025_gap_down_frequency_378_025_accel_378': {'inputs': ['gap_155_gap_025_gap_down_frequency_378_025_roc_378'], 'func': gap_180_gap_025_gap_down_frequency_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def gs_replacement_d3_001(gs_replacement_d2_001):
    feature = _clean(gs_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_001'] = {'inputs': ['gs_replacement_d2_001'], 'func': gs_replacement_d3_001}


def gs_replacement_d3_002(gs_replacement_d2_002):
    feature = _clean(gs_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_002'] = {'inputs': ['gs_replacement_d2_002'], 'func': gs_replacement_d3_002}


def gs_replacement_d3_003(gs_replacement_d2_003):
    feature = _clean(gs_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_003'] = {'inputs': ['gs_replacement_d2_003'], 'func': gs_replacement_d3_003}


def gs_replacement_d3_004(gs_replacement_d2_004):
    feature = _clean(gs_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_004'] = {'inputs': ['gs_replacement_d2_004'], 'func': gs_replacement_d3_004}


def gs_replacement_d3_005(gs_replacement_d2_005):
    feature = _clean(gs_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_005'] = {'inputs': ['gs_replacement_d2_005'], 'func': gs_replacement_d3_005}


def gs_replacement_d3_006(gs_replacement_d2_006):
    feature = _clean(gs_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_006'] = {'inputs': ['gs_replacement_d2_006'], 'func': gs_replacement_d3_006}


def gs_replacement_d3_007(gs_replacement_d2_007):
    feature = _clean(gs_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_007'] = {'inputs': ['gs_replacement_d2_007'], 'func': gs_replacement_d3_007}


def gs_replacement_d3_008(gs_replacement_d2_008):
    feature = _clean(gs_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_008'] = {'inputs': ['gs_replacement_d2_008'], 'func': gs_replacement_d3_008}


def gs_replacement_d3_009(gs_replacement_d2_009):
    feature = _clean(gs_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_009'] = {'inputs': ['gs_replacement_d2_009'], 'func': gs_replacement_d3_009}


def gs_replacement_d3_010(gs_replacement_d2_010):
    feature = _clean(gs_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_010'] = {'inputs': ['gs_replacement_d2_010'], 'func': gs_replacement_d3_010}


def gs_replacement_d3_011(gs_replacement_d2_011):
    feature = _clean(gs_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_011'] = {'inputs': ['gs_replacement_d2_011'], 'func': gs_replacement_d3_011}


def gs_replacement_d3_012(gs_replacement_d2_012):
    feature = _clean(gs_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_012'] = {'inputs': ['gs_replacement_d2_012'], 'func': gs_replacement_d3_012}


def gs_replacement_d3_013(gs_replacement_d2_013):
    feature = _clean(gs_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_013'] = {'inputs': ['gs_replacement_d2_013'], 'func': gs_replacement_d3_013}


def gs_replacement_d3_014(gs_replacement_d2_014):
    feature = _clean(gs_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_014'] = {'inputs': ['gs_replacement_d2_014'], 'func': gs_replacement_d3_014}


def gs_replacement_d3_015(gs_replacement_d2_015):
    feature = _clean(gs_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_015'] = {'inputs': ['gs_replacement_d2_015'], 'func': gs_replacement_d3_015}


def gs_replacement_d3_016(gs_replacement_d2_016):
    feature = _clean(gs_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_016'] = {'inputs': ['gs_replacement_d2_016'], 'func': gs_replacement_d3_016}


def gs_replacement_d3_017(gs_replacement_d2_017):
    feature = _clean(gs_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_017'] = {'inputs': ['gs_replacement_d2_017'], 'func': gs_replacement_d3_017}


def gs_replacement_d3_018(gs_replacement_d2_018):
    feature = _clean(gs_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_018'] = {'inputs': ['gs_replacement_d2_018'], 'func': gs_replacement_d3_018}


def gs_replacement_d3_019(gs_replacement_d2_019):
    feature = _clean(gs_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_019'] = {'inputs': ['gs_replacement_d2_019'], 'func': gs_replacement_d3_019}


def gs_replacement_d3_020(gs_replacement_d2_020):
    feature = _clean(gs_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_020'] = {'inputs': ['gs_replacement_d2_020'], 'func': gs_replacement_d3_020}


def gs_replacement_d3_021(gs_replacement_d2_021):
    feature = _clean(gs_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_021'] = {'inputs': ['gs_replacement_d2_021'], 'func': gs_replacement_d3_021}


def gs_replacement_d3_022(gs_replacement_d2_022):
    feature = _clean(gs_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_022'] = {'inputs': ['gs_replacement_d2_022'], 'func': gs_replacement_d3_022}


def gs_replacement_d3_023(gs_replacement_d2_023):
    feature = _clean(gs_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_023'] = {'inputs': ['gs_replacement_d2_023'], 'func': gs_replacement_d3_023}


def gs_replacement_d3_024(gs_replacement_d2_024):
    feature = _clean(gs_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_024'] = {'inputs': ['gs_replacement_d2_024'], 'func': gs_replacement_d3_024}


def gs_replacement_d3_025(gs_replacement_d2_025):
    feature = _clean(gs_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_025'] = {'inputs': ['gs_replacement_d2_025'], 'func': gs_replacement_d3_025}


def gs_replacement_d3_026(gs_replacement_d2_026):
    feature = _clean(gs_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_026'] = {'inputs': ['gs_replacement_d2_026'], 'func': gs_replacement_d3_026}


def gs_replacement_d3_027(gs_replacement_d2_027):
    feature = _clean(gs_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_027'] = {'inputs': ['gs_replacement_d2_027'], 'func': gs_replacement_d3_027}


def gs_replacement_d3_028(gs_replacement_d2_028):
    feature = _clean(gs_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_028'] = {'inputs': ['gs_replacement_d2_028'], 'func': gs_replacement_d3_028}


def gs_replacement_d3_029(gs_replacement_d2_029):
    feature = _clean(gs_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_029'] = {'inputs': ['gs_replacement_d2_029'], 'func': gs_replacement_d3_029}


def gs_replacement_d3_030(gs_replacement_d2_030):
    feature = _clean(gs_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_030'] = {'inputs': ['gs_replacement_d2_030'], 'func': gs_replacement_d3_030}


def gs_replacement_d3_031(gs_replacement_d2_031):
    feature = _clean(gs_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_031'] = {'inputs': ['gs_replacement_d2_031'], 'func': gs_replacement_d3_031}


def gs_replacement_d3_032(gs_replacement_d2_032):
    feature = _clean(gs_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_032'] = {'inputs': ['gs_replacement_d2_032'], 'func': gs_replacement_d3_032}


def gs_replacement_d3_033(gs_replacement_d2_033):
    feature = _clean(gs_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_033'] = {'inputs': ['gs_replacement_d2_033'], 'func': gs_replacement_d3_033}


def gs_replacement_d3_034(gs_replacement_d2_034):
    feature = _clean(gs_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_034'] = {'inputs': ['gs_replacement_d2_034'], 'func': gs_replacement_d3_034}


def gs_replacement_d3_035(gs_replacement_d2_035):
    feature = _clean(gs_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_035'] = {'inputs': ['gs_replacement_d2_035'], 'func': gs_replacement_d3_035}


def gs_replacement_d3_036(gs_replacement_d2_036):
    feature = _clean(gs_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_036'] = {'inputs': ['gs_replacement_d2_036'], 'func': gs_replacement_d3_036}


def gs_replacement_d3_037(gs_replacement_d2_037):
    feature = _clean(gs_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_037'] = {'inputs': ['gs_replacement_d2_037'], 'func': gs_replacement_d3_037}


def gs_replacement_d3_038(gs_replacement_d2_038):
    feature = _clean(gs_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_038'] = {'inputs': ['gs_replacement_d2_038'], 'func': gs_replacement_d3_038}


def gs_replacement_d3_039(gs_replacement_d2_039):
    feature = _clean(gs_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_039'] = {'inputs': ['gs_replacement_d2_039'], 'func': gs_replacement_d3_039}


def gs_replacement_d3_040(gs_replacement_d2_040):
    feature = _clean(gs_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_040'] = {'inputs': ['gs_replacement_d2_040'], 'func': gs_replacement_d3_040}


def gs_replacement_d3_041(gs_replacement_d2_041):
    feature = _clean(gs_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_041'] = {'inputs': ['gs_replacement_d2_041'], 'func': gs_replacement_d3_041}


def gs_replacement_d3_042(gs_replacement_d2_042):
    feature = _clean(gs_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_042'] = {'inputs': ['gs_replacement_d2_042'], 'func': gs_replacement_d3_042}


def gs_replacement_d3_043(gs_replacement_d2_043):
    feature = _clean(gs_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_043'] = {'inputs': ['gs_replacement_d2_043'], 'func': gs_replacement_d3_043}


def gs_replacement_d3_044(gs_replacement_d2_044):
    feature = _clean(gs_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_044'] = {'inputs': ['gs_replacement_d2_044'], 'func': gs_replacement_d3_044}


def gs_replacement_d3_045(gs_replacement_d2_045):
    feature = _clean(gs_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_045'] = {'inputs': ['gs_replacement_d2_045'], 'func': gs_replacement_d3_045}


def gs_replacement_d3_046(gs_replacement_d2_046):
    feature = _clean(gs_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_046'] = {'inputs': ['gs_replacement_d2_046'], 'func': gs_replacement_d3_046}


def gs_replacement_d3_047(gs_replacement_d2_047):
    feature = _clean(gs_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_047'] = {'inputs': ['gs_replacement_d2_047'], 'func': gs_replacement_d3_047}


def gs_replacement_d3_048(gs_replacement_d2_048):
    feature = _clean(gs_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_048'] = {'inputs': ['gs_replacement_d2_048'], 'func': gs_replacement_d3_048}


def gs_replacement_d3_049(gs_replacement_d2_049):
    feature = _clean(gs_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_049'] = {'inputs': ['gs_replacement_d2_049'], 'func': gs_replacement_d3_049}


def gs_replacement_d3_050(gs_replacement_d2_050):
    feature = _clean(gs_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_050'] = {'inputs': ['gs_replacement_d2_050'], 'func': gs_replacement_d3_050}


def gs_replacement_d3_051(gs_replacement_d2_051):
    feature = _clean(gs_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_051'] = {'inputs': ['gs_replacement_d2_051'], 'func': gs_replacement_d3_051}


def gs_replacement_d3_052(gs_replacement_d2_052):
    feature = _clean(gs_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_052'] = {'inputs': ['gs_replacement_d2_052'], 'func': gs_replacement_d3_052}


def gs_replacement_d3_053(gs_replacement_d2_053):
    feature = _clean(gs_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_053'] = {'inputs': ['gs_replacement_d2_053'], 'func': gs_replacement_d3_053}


def gs_replacement_d3_054(gs_replacement_d2_054):
    feature = _clean(gs_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_054'] = {'inputs': ['gs_replacement_d2_054'], 'func': gs_replacement_d3_054}


def gs_replacement_d3_055(gs_replacement_d2_055):
    feature = _clean(gs_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_055'] = {'inputs': ['gs_replacement_d2_055'], 'func': gs_replacement_d3_055}


def gs_replacement_d3_056(gs_replacement_d2_056):
    feature = _clean(gs_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_056'] = {'inputs': ['gs_replacement_d2_056'], 'func': gs_replacement_d3_056}


def gs_replacement_d3_057(gs_replacement_d2_057):
    feature = _clean(gs_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_057'] = {'inputs': ['gs_replacement_d2_057'], 'func': gs_replacement_d3_057}


def gs_replacement_d3_058(gs_replacement_d2_058):
    feature = _clean(gs_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_058'] = {'inputs': ['gs_replacement_d2_058'], 'func': gs_replacement_d3_058}


def gs_replacement_d3_059(gs_replacement_d2_059):
    feature = _clean(gs_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_059'] = {'inputs': ['gs_replacement_d2_059'], 'func': gs_replacement_d3_059}


def gs_replacement_d3_060(gs_replacement_d2_060):
    feature = _clean(gs_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_060'] = {'inputs': ['gs_replacement_d2_060'], 'func': gs_replacement_d3_060}


def gs_replacement_d3_061(gs_replacement_d2_061):
    feature = _clean(gs_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_061'] = {'inputs': ['gs_replacement_d2_061'], 'func': gs_replacement_d3_061}


def gs_replacement_d3_062(gs_replacement_d2_062):
    feature = _clean(gs_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_062'] = {'inputs': ['gs_replacement_d2_062'], 'func': gs_replacement_d3_062}


def gs_replacement_d3_063(gs_replacement_d2_063):
    feature = _clean(gs_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_063'] = {'inputs': ['gs_replacement_d2_063'], 'func': gs_replacement_d3_063}


def gs_replacement_d3_064(gs_replacement_d2_064):
    feature = _clean(gs_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_064'] = {'inputs': ['gs_replacement_d2_064'], 'func': gs_replacement_d3_064}


def gs_replacement_d3_065(gs_replacement_d2_065):
    feature = _clean(gs_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_065'] = {'inputs': ['gs_replacement_d2_065'], 'func': gs_replacement_d3_065}


def gs_replacement_d3_066(gs_replacement_d2_066):
    feature = _clean(gs_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_066'] = {'inputs': ['gs_replacement_d2_066'], 'func': gs_replacement_d3_066}


def gs_replacement_d3_067(gs_replacement_d2_067):
    feature = _clean(gs_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_067'] = {'inputs': ['gs_replacement_d2_067'], 'func': gs_replacement_d3_067}


def gs_replacement_d3_068(gs_replacement_d2_068):
    feature = _clean(gs_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_068'] = {'inputs': ['gs_replacement_d2_068'], 'func': gs_replacement_d3_068}


def gs_replacement_d3_069(gs_replacement_d2_069):
    feature = _clean(gs_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_069'] = {'inputs': ['gs_replacement_d2_069'], 'func': gs_replacement_d3_069}


def gs_replacement_d3_070(gs_replacement_d2_070):
    feature = _clean(gs_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_070'] = {'inputs': ['gs_replacement_d2_070'], 'func': gs_replacement_d3_070}


def gs_replacement_d3_071(gs_replacement_d2_071):
    feature = _clean(gs_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_071'] = {'inputs': ['gs_replacement_d2_071'], 'func': gs_replacement_d3_071}


def gs_replacement_d3_072(gs_replacement_d2_072):
    feature = _clean(gs_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_072'] = {'inputs': ['gs_replacement_d2_072'], 'func': gs_replacement_d3_072}


def gs_replacement_d3_073(gs_replacement_d2_073):
    feature = _clean(gs_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_073'] = {'inputs': ['gs_replacement_d2_073'], 'func': gs_replacement_d3_073}


def gs_replacement_d3_074(gs_replacement_d2_074):
    feature = _clean(gs_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_074'] = {'inputs': ['gs_replacement_d2_074'], 'func': gs_replacement_d3_074}


def gs_replacement_d3_075(gs_replacement_d2_075):
    feature = _clean(gs_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_075'] = {'inputs': ['gs_replacement_d2_075'], 'func': gs_replacement_d3_075}


def gs_replacement_d3_076(gs_replacement_d2_076):
    feature = _clean(gs_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_076'] = {'inputs': ['gs_replacement_d2_076'], 'func': gs_replacement_d3_076}


def gs_replacement_d3_077(gs_replacement_d2_077):
    feature = _clean(gs_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_077'] = {'inputs': ['gs_replacement_d2_077'], 'func': gs_replacement_d3_077}


def gs_replacement_d3_078(gs_replacement_d2_078):
    feature = _clean(gs_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_078'] = {'inputs': ['gs_replacement_d2_078'], 'func': gs_replacement_d3_078}


def gs_replacement_d3_079(gs_replacement_d2_079):
    feature = _clean(gs_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_079'] = {'inputs': ['gs_replacement_d2_079'], 'func': gs_replacement_d3_079}


def gs_replacement_d3_080(gs_replacement_d2_080):
    feature = _clean(gs_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_080'] = {'inputs': ['gs_replacement_d2_080'], 'func': gs_replacement_d3_080}


def gs_replacement_d3_081(gs_replacement_d2_081):
    feature = _clean(gs_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_081'] = {'inputs': ['gs_replacement_d2_081'], 'func': gs_replacement_d3_081}


def gs_replacement_d3_082(gs_replacement_d2_082):
    feature = _clean(gs_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_082'] = {'inputs': ['gs_replacement_d2_082'], 'func': gs_replacement_d3_082}


def gs_replacement_d3_083(gs_replacement_d2_083):
    feature = _clean(gs_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_083'] = {'inputs': ['gs_replacement_d2_083'], 'func': gs_replacement_d3_083}


def gs_replacement_d3_084(gs_replacement_d2_084):
    feature = _clean(gs_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_084'] = {'inputs': ['gs_replacement_d2_084'], 'func': gs_replacement_d3_084}


def gs_replacement_d3_085(gs_replacement_d2_085):
    feature = _clean(gs_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_085'] = {'inputs': ['gs_replacement_d2_085'], 'func': gs_replacement_d3_085}


def gs_replacement_d3_086(gs_replacement_d2_086):
    feature = _clean(gs_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_086'] = {'inputs': ['gs_replacement_d2_086'], 'func': gs_replacement_d3_086}


def gs_replacement_d3_087(gs_replacement_d2_087):
    feature = _clean(gs_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_087'] = {'inputs': ['gs_replacement_d2_087'], 'func': gs_replacement_d3_087}


def gs_replacement_d3_088(gs_replacement_d2_088):
    feature = _clean(gs_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_088'] = {'inputs': ['gs_replacement_d2_088'], 'func': gs_replacement_d3_088}


def gs_replacement_d3_089(gs_replacement_d2_089):
    feature = _clean(gs_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_089'] = {'inputs': ['gs_replacement_d2_089'], 'func': gs_replacement_d3_089}


def gs_replacement_d3_090(gs_replacement_d2_090):
    feature = _clean(gs_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_090'] = {'inputs': ['gs_replacement_d2_090'], 'func': gs_replacement_d3_090}


def gs_replacement_d3_091(gs_replacement_d2_091):
    feature = _clean(gs_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_091'] = {'inputs': ['gs_replacement_d2_091'], 'func': gs_replacement_d3_091}


def gs_replacement_d3_092(gs_replacement_d2_092):
    feature = _clean(gs_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_092'] = {'inputs': ['gs_replacement_d2_092'], 'func': gs_replacement_d3_092}


def gs_replacement_d3_093(gs_replacement_d2_093):
    feature = _clean(gs_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_093'] = {'inputs': ['gs_replacement_d2_093'], 'func': gs_replacement_d3_093}


def gs_replacement_d3_094(gs_replacement_d2_094):
    feature = _clean(gs_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_094'] = {'inputs': ['gs_replacement_d2_094'], 'func': gs_replacement_d3_094}


def gs_replacement_d3_095(gs_replacement_d2_095):
    feature = _clean(gs_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_095'] = {'inputs': ['gs_replacement_d2_095'], 'func': gs_replacement_d3_095}


def gs_replacement_d3_096(gs_replacement_d2_096):
    feature = _clean(gs_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_096'] = {'inputs': ['gs_replacement_d2_096'], 'func': gs_replacement_d3_096}


def gs_replacement_d3_097(gs_replacement_d2_097):
    feature = _clean(gs_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_097'] = {'inputs': ['gs_replacement_d2_097'], 'func': gs_replacement_d3_097}


def gs_replacement_d3_098(gs_replacement_d2_098):
    feature = _clean(gs_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_098'] = {'inputs': ['gs_replacement_d2_098'], 'func': gs_replacement_d3_098}


def gs_replacement_d3_099(gs_replacement_d2_099):
    feature = _clean(gs_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_099'] = {'inputs': ['gs_replacement_d2_099'], 'func': gs_replacement_d3_099}


def gs_replacement_d3_100(gs_replacement_d2_100):
    feature = _clean(gs_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_100'] = {'inputs': ['gs_replacement_d2_100'], 'func': gs_replacement_d3_100}


def gs_replacement_d3_101(gs_replacement_d2_101):
    feature = _clean(gs_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_101'] = {'inputs': ['gs_replacement_d2_101'], 'func': gs_replacement_d3_101}


def gs_replacement_d3_102(gs_replacement_d2_102):
    feature = _clean(gs_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_102'] = {'inputs': ['gs_replacement_d2_102'], 'func': gs_replacement_d3_102}


def gs_replacement_d3_103(gs_replacement_d2_103):
    feature = _clean(gs_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_103'] = {'inputs': ['gs_replacement_d2_103'], 'func': gs_replacement_d3_103}


def gs_replacement_d3_104(gs_replacement_d2_104):
    feature = _clean(gs_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_104'] = {'inputs': ['gs_replacement_d2_104'], 'func': gs_replacement_d3_104}


def gs_replacement_d3_105(gs_replacement_d2_105):
    feature = _clean(gs_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_105'] = {'inputs': ['gs_replacement_d2_105'], 'func': gs_replacement_d3_105}


def gs_replacement_d3_106(gs_replacement_d2_106):
    feature = _clean(gs_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_106'] = {'inputs': ['gs_replacement_d2_106'], 'func': gs_replacement_d3_106}


def gs_replacement_d3_107(gs_replacement_d2_107):
    feature = _clean(gs_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_107'] = {'inputs': ['gs_replacement_d2_107'], 'func': gs_replacement_d3_107}


def gs_replacement_d3_108(gs_replacement_d2_108):
    feature = _clean(gs_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_108'] = {'inputs': ['gs_replacement_d2_108'], 'func': gs_replacement_d3_108}


def gs_replacement_d3_109(gs_replacement_d2_109):
    feature = _clean(gs_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_109'] = {'inputs': ['gs_replacement_d2_109'], 'func': gs_replacement_d3_109}


def gs_replacement_d3_110(gs_replacement_d2_110):
    feature = _clean(gs_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_110'] = {'inputs': ['gs_replacement_d2_110'], 'func': gs_replacement_d3_110}


def gs_replacement_d3_111(gs_replacement_d2_111):
    feature = _clean(gs_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_111'] = {'inputs': ['gs_replacement_d2_111'], 'func': gs_replacement_d3_111}


def gs_replacement_d3_112(gs_replacement_d2_112):
    feature = _clean(gs_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_112'] = {'inputs': ['gs_replacement_d2_112'], 'func': gs_replacement_d3_112}


def gs_replacement_d3_113(gs_replacement_d2_113):
    feature = _clean(gs_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_113'] = {'inputs': ['gs_replacement_d2_113'], 'func': gs_replacement_d3_113}


def gs_replacement_d3_114(gs_replacement_d2_114):
    feature = _clean(gs_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_114'] = {'inputs': ['gs_replacement_d2_114'], 'func': gs_replacement_d3_114}


def gs_replacement_d3_115(gs_replacement_d2_115):
    feature = _clean(gs_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_115'] = {'inputs': ['gs_replacement_d2_115'], 'func': gs_replacement_d3_115}


def gs_replacement_d3_116(gs_replacement_d2_116):
    feature = _clean(gs_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_116'] = {'inputs': ['gs_replacement_d2_116'], 'func': gs_replacement_d3_116}


def gs_replacement_d3_117(gs_replacement_d2_117):
    feature = _clean(gs_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_117'] = {'inputs': ['gs_replacement_d2_117'], 'func': gs_replacement_d3_117}


def gs_replacement_d3_118(gs_replacement_d2_118):
    feature = _clean(gs_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_118'] = {'inputs': ['gs_replacement_d2_118'], 'func': gs_replacement_d3_118}


def gs_replacement_d3_119(gs_replacement_d2_119):
    feature = _clean(gs_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_119'] = {'inputs': ['gs_replacement_d2_119'], 'func': gs_replacement_d3_119}


def gs_replacement_d3_120(gs_replacement_d2_120):
    feature = _clean(gs_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_120'] = {'inputs': ['gs_replacement_d2_120'], 'func': gs_replacement_d3_120}


def gs_replacement_d3_121(gs_replacement_d2_121):
    feature = _clean(gs_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_121'] = {'inputs': ['gs_replacement_d2_121'], 'func': gs_replacement_d3_121}


def gs_replacement_d3_122(gs_replacement_d2_122):
    feature = _clean(gs_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_122'] = {'inputs': ['gs_replacement_d2_122'], 'func': gs_replacement_d3_122}


def gs_replacement_d3_123(gs_replacement_d2_123):
    feature = _clean(gs_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_123'] = {'inputs': ['gs_replacement_d2_123'], 'func': gs_replacement_d3_123}


def gs_replacement_d3_124(gs_replacement_d2_124):
    feature = _clean(gs_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_124'] = {'inputs': ['gs_replacement_d2_124'], 'func': gs_replacement_d3_124}


def gs_replacement_d3_125(gs_replacement_d2_125):
    feature = _clean(gs_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_125'] = {'inputs': ['gs_replacement_d2_125'], 'func': gs_replacement_d3_125}


def gs_replacement_d3_126(gs_replacement_d2_126):
    feature = _clean(gs_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_126'] = {'inputs': ['gs_replacement_d2_126'], 'func': gs_replacement_d3_126}


def gs_replacement_d3_127(gs_replacement_d2_127):
    feature = _clean(gs_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_127'] = {'inputs': ['gs_replacement_d2_127'], 'func': gs_replacement_d3_127}


def gs_replacement_d3_128(gs_replacement_d2_128):
    feature = _clean(gs_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_128'] = {'inputs': ['gs_replacement_d2_128'], 'func': gs_replacement_d3_128}


def gs_replacement_d3_129(gs_replacement_d2_129):
    feature = _clean(gs_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_129'] = {'inputs': ['gs_replacement_d2_129'], 'func': gs_replacement_d3_129}


def gs_replacement_d3_130(gs_replacement_d2_130):
    feature = _clean(gs_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_130'] = {'inputs': ['gs_replacement_d2_130'], 'func': gs_replacement_d3_130}


def gs_replacement_d3_131(gs_replacement_d2_131):
    feature = _clean(gs_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_131'] = {'inputs': ['gs_replacement_d2_131'], 'func': gs_replacement_d3_131}


def gs_replacement_d3_132(gs_replacement_d2_132):
    feature = _clean(gs_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_132'] = {'inputs': ['gs_replacement_d2_132'], 'func': gs_replacement_d3_132}


def gs_replacement_d3_133(gs_replacement_d2_133):
    feature = _clean(gs_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_133'] = {'inputs': ['gs_replacement_d2_133'], 'func': gs_replacement_d3_133}


def gs_replacement_d3_134(gs_replacement_d2_134):
    feature = _clean(gs_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_134'] = {'inputs': ['gs_replacement_d2_134'], 'func': gs_replacement_d3_134}


def gs_replacement_d3_135(gs_replacement_d2_135):
    feature = _clean(gs_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_135'] = {'inputs': ['gs_replacement_d2_135'], 'func': gs_replacement_d3_135}


def gs_replacement_d3_136(gs_replacement_d2_136):
    feature = _clean(gs_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_136'] = {'inputs': ['gs_replacement_d2_136'], 'func': gs_replacement_d3_136}


def gs_replacement_d3_137(gs_replacement_d2_137):
    feature = _clean(gs_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_137'] = {'inputs': ['gs_replacement_d2_137'], 'func': gs_replacement_d3_137}


def gs_replacement_d3_138(gs_replacement_d2_138):
    feature = _clean(gs_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_138'] = {'inputs': ['gs_replacement_d2_138'], 'func': gs_replacement_d3_138}


def gs_replacement_d3_139(gs_replacement_d2_139):
    feature = _clean(gs_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_139'] = {'inputs': ['gs_replacement_d2_139'], 'func': gs_replacement_d3_139}


def gs_replacement_d3_140(gs_replacement_d2_140):
    feature = _clean(gs_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_140'] = {'inputs': ['gs_replacement_d2_140'], 'func': gs_replacement_d3_140}


def gs_replacement_d3_141(gs_replacement_d2_141):
    feature = _clean(gs_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_141'] = {'inputs': ['gs_replacement_d2_141'], 'func': gs_replacement_d3_141}


def gs_replacement_d3_142(gs_replacement_d2_142):
    feature = _clean(gs_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_142'] = {'inputs': ['gs_replacement_d2_142'], 'func': gs_replacement_d3_142}


def gs_replacement_d3_143(gs_replacement_d2_143):
    feature = _clean(gs_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_143'] = {'inputs': ['gs_replacement_d2_143'], 'func': gs_replacement_d3_143}


def gs_replacement_d3_144(gs_replacement_d2_144):
    feature = _clean(gs_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_144'] = {'inputs': ['gs_replacement_d2_144'], 'func': gs_replacement_d3_144}


def gs_replacement_d3_145(gs_replacement_d2_145):
    feature = _clean(gs_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_145'] = {'inputs': ['gs_replacement_d2_145'], 'func': gs_replacement_d3_145}


def gs_replacement_d3_146(gs_replacement_d2_146):
    feature = _clean(gs_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_146'] = {'inputs': ['gs_replacement_d2_146'], 'func': gs_replacement_d3_146}


def gs_replacement_d3_147(gs_replacement_d2_147):
    feature = _clean(gs_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_147'] = {'inputs': ['gs_replacement_d2_147'], 'func': gs_replacement_d3_147}


def gs_replacement_d3_148(gs_replacement_d2_148):
    feature = _clean(gs_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_148'] = {'inputs': ['gs_replacement_d2_148'], 'func': gs_replacement_d3_148}


def gs_replacement_d3_149(gs_replacement_d2_149):
    feature = _clean(gs_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_149'] = {'inputs': ['gs_replacement_d2_149'], 'func': gs_replacement_d3_149}


def gs_replacement_d3_150(gs_replacement_d2_150):
    feature = _clean(gs_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_150'] = {'inputs': ['gs_replacement_d2_150'], 'func': gs_replacement_d3_150}


def gs_replacement_d3_151(gs_replacement_d2_151):
    feature = _clean(gs_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_151'] = {'inputs': ['gs_replacement_d2_151'], 'func': gs_replacement_d3_151}


def gs_replacement_d3_152(gs_replacement_d2_152):
    feature = _clean(gs_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_152'] = {'inputs': ['gs_replacement_d2_152'], 'func': gs_replacement_d3_152}


def gs_replacement_d3_153(gs_replacement_d2_153):
    feature = _clean(gs_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_153'] = {'inputs': ['gs_replacement_d2_153'], 'func': gs_replacement_d3_153}


def gs_replacement_d3_154(gs_replacement_d2_154):
    feature = _clean(gs_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_154'] = {'inputs': ['gs_replacement_d2_154'], 'func': gs_replacement_d3_154}


def gs_replacement_d3_155(gs_replacement_d2_155):
    feature = _clean(gs_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_155'] = {'inputs': ['gs_replacement_d2_155'], 'func': gs_replacement_d3_155}


def gs_replacement_d3_156(gs_replacement_d2_156):
    feature = _clean(gs_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_156'] = {'inputs': ['gs_replacement_d2_156'], 'func': gs_replacement_d3_156}


def gs_replacement_d3_157(gs_replacement_d2_157):
    feature = _clean(gs_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_157'] = {'inputs': ['gs_replacement_d2_157'], 'func': gs_replacement_d3_157}


def gs_replacement_d3_158(gs_replacement_d2_158):
    feature = _clean(gs_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_158'] = {'inputs': ['gs_replacement_d2_158'], 'func': gs_replacement_d3_158}


def gs_replacement_d3_159(gs_replacement_d2_159):
    feature = _clean(gs_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_159'] = {'inputs': ['gs_replacement_d2_159'], 'func': gs_replacement_d3_159}


def gs_replacement_d3_160(gs_replacement_d2_160):
    feature = _clean(gs_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
GS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gs_replacement_d3_160'] = {'inputs': ['gs_replacement_d2_160'], 'func': gs_replacement_d3_160}


# Third-derivative extensions for repaired first-base features.
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def gap_base_universe_d3_001_gap_002_gap_magnitude_10_002(gap_base_universe_d2_001_gap_002_gap_magnitude_10_002):
    return _base_universe_d3(gap_base_universe_d2_001_gap_002_gap_magnitude_10_002, 1)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_001_gap_002_gap_magnitude_10_002'] = {'inputs': ['gap_base_universe_d2_001_gap_002_gap_magnitude_10_002'], 'func': gap_base_universe_d3_001_gap_002_gap_magnitude_10_002}


def gap_base_universe_d3_002_gap_003_open_close_pressure_21_003(gap_base_universe_d2_002_gap_003_open_close_pressure_21_003):
    return _base_universe_d3(gap_base_universe_d2_002_gap_003_open_close_pressure_21_003, 2)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_002_gap_003_open_close_pressure_21_003'] = {'inputs': ['gap_base_universe_d2_002_gap_003_open_close_pressure_21_003'], 'func': gap_base_universe_d3_002_gap_003_open_close_pressure_21_003}


def gap_base_universe_d3_003_gap_004_lower_wick_ratio_42_004(gap_base_universe_d2_003_gap_004_lower_wick_ratio_42_004):
    return _base_universe_d3(gap_base_universe_d2_003_gap_004_lower_wick_ratio_42_004, 3)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_003_gap_004_lower_wick_ratio_42_004'] = {'inputs': ['gap_base_universe_d2_003_gap_004_lower_wick_ratio_42_004'], 'func': gap_base_universe_d3_003_gap_004_lower_wick_ratio_42_004}


def gap_base_universe_d3_004_gap_005_upper_wick_ratio_63_005(gap_base_universe_d2_004_gap_005_upper_wick_ratio_63_005):
    return _base_universe_d3(gap_base_universe_d2_004_gap_005_upper_wick_ratio_63_005, 4)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_004_gap_005_upper_wick_ratio_63_005'] = {'inputs': ['gap_base_universe_d2_004_gap_005_upper_wick_ratio_63_005'], 'func': gap_base_universe_d3_004_gap_005_upper_wick_ratio_63_005}


def gap_base_universe_d3_005_gap_006_body_to_range_84_006(gap_base_universe_d2_005_gap_006_body_to_range_84_006):
    return _base_universe_d3(gap_base_universe_d2_005_gap_006_body_to_range_84_006, 5)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_005_gap_006_body_to_range_84_006'] = {'inputs': ['gap_base_universe_d2_005_gap_006_body_to_range_84_006'], 'func': gap_base_universe_d3_005_gap_006_body_to_range_84_006}


def gap_base_universe_d3_006_gap_008_gap_magnitude_189_008(gap_base_universe_d2_006_gap_008_gap_magnitude_189_008):
    return _base_universe_d3(gap_base_universe_d2_006_gap_008_gap_magnitude_189_008, 6)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_006_gap_008_gap_magnitude_189_008'] = {'inputs': ['gap_base_universe_d2_006_gap_008_gap_magnitude_189_008'], 'func': gap_base_universe_d3_006_gap_008_gap_magnitude_189_008}


def gap_base_universe_d3_007_gap_009_open_close_pressure_252_009(gap_base_universe_d2_007_gap_009_open_close_pressure_252_009):
    return _base_universe_d3(gap_base_universe_d2_007_gap_009_open_close_pressure_252_009, 7)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_007_gap_009_open_close_pressure_252_009'] = {'inputs': ['gap_base_universe_d2_007_gap_009_open_close_pressure_252_009'], 'func': gap_base_universe_d3_007_gap_009_open_close_pressure_252_009}


def gap_base_universe_d3_008_gap_010_lower_wick_ratio_378_010(gap_base_universe_d2_008_gap_010_lower_wick_ratio_378_010):
    return _base_universe_d3(gap_base_universe_d2_008_gap_010_lower_wick_ratio_378_010, 8)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_008_gap_010_lower_wick_ratio_378_010'] = {'inputs': ['gap_base_universe_d2_008_gap_010_lower_wick_ratio_378_010'], 'func': gap_base_universe_d3_008_gap_010_lower_wick_ratio_378_010}


def gap_base_universe_d3_009_gap_011_upper_wick_ratio_504_011(gap_base_universe_d2_009_gap_011_upper_wick_ratio_504_011):
    return _base_universe_d3(gap_base_universe_d2_009_gap_011_upper_wick_ratio_504_011, 9)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_009_gap_011_upper_wick_ratio_504_011'] = {'inputs': ['gap_base_universe_d2_009_gap_011_upper_wick_ratio_504_011'], 'func': gap_base_universe_d3_009_gap_011_upper_wick_ratio_504_011}


def gap_base_universe_d3_010_gap_012_body_to_range_756_012(gap_base_universe_d2_010_gap_012_body_to_range_756_012):
    return _base_universe_d3(gap_base_universe_d2_010_gap_012_body_to_range_756_012, 10)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_010_gap_012_body_to_range_756_012'] = {'inputs': ['gap_base_universe_d2_010_gap_012_body_to_range_756_012'], 'func': gap_base_universe_d3_010_gap_012_body_to_range_756_012}


def gap_base_universe_d3_011_gap_014_gap_magnitude_1260_014(gap_base_universe_d2_011_gap_014_gap_magnitude_1260_014):
    return _base_universe_d3(gap_base_universe_d2_011_gap_014_gap_magnitude_1260_014, 11)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_011_gap_014_gap_magnitude_1260_014'] = {'inputs': ['gap_base_universe_d2_011_gap_014_gap_magnitude_1260_014'], 'func': gap_base_universe_d3_011_gap_014_gap_magnitude_1260_014}


def gap_base_universe_d3_012_gap_015_open_close_pressure_1512_015(gap_base_universe_d2_012_gap_015_open_close_pressure_1512_015):
    return _base_universe_d3(gap_base_universe_d2_012_gap_015_open_close_pressure_1512_015, 12)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_012_gap_015_open_close_pressure_1512_015'] = {'inputs': ['gap_base_universe_d2_012_gap_015_open_close_pressure_1512_015'], 'func': gap_base_universe_d3_012_gap_015_open_close_pressure_1512_015}


def gap_base_universe_d3_013_gap_016_lower_wick_ratio_5_016(gap_base_universe_d2_013_gap_016_lower_wick_ratio_5_016):
    return _base_universe_d3(gap_base_universe_d2_013_gap_016_lower_wick_ratio_5_016, 13)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_013_gap_016_lower_wick_ratio_5_016'] = {'inputs': ['gap_base_universe_d2_013_gap_016_lower_wick_ratio_5_016'], 'func': gap_base_universe_d3_013_gap_016_lower_wick_ratio_5_016}


def gap_base_universe_d3_014_gap_017_upper_wick_ratio_10_017(gap_base_universe_d2_014_gap_017_upper_wick_ratio_10_017):
    return _base_universe_d3(gap_base_universe_d2_014_gap_017_upper_wick_ratio_10_017, 14)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_014_gap_017_upper_wick_ratio_10_017'] = {'inputs': ['gap_base_universe_d2_014_gap_017_upper_wick_ratio_10_017'], 'func': gap_base_universe_d3_014_gap_017_upper_wick_ratio_10_017}


def gap_base_universe_d3_015_gap_018_body_to_range_21_018(gap_base_universe_d2_015_gap_018_body_to_range_21_018):
    return _base_universe_d3(gap_base_universe_d2_015_gap_018_body_to_range_21_018, 15)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_015_gap_018_body_to_range_21_018'] = {'inputs': ['gap_base_universe_d2_015_gap_018_body_to_range_21_018'], 'func': gap_base_universe_d3_015_gap_018_body_to_range_21_018}


def gap_base_universe_d3_016_gap_020_gap_magnitude_63_020(gap_base_universe_d2_016_gap_020_gap_magnitude_63_020):
    return _base_universe_d3(gap_base_universe_d2_016_gap_020_gap_magnitude_63_020, 16)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_016_gap_020_gap_magnitude_63_020'] = {'inputs': ['gap_base_universe_d2_016_gap_020_gap_magnitude_63_020'], 'func': gap_base_universe_d3_016_gap_020_gap_magnitude_63_020}


def gap_base_universe_d3_017_gap_021_open_close_pressure_84_021(gap_base_universe_d2_017_gap_021_open_close_pressure_84_021):
    return _base_universe_d3(gap_base_universe_d2_017_gap_021_open_close_pressure_84_021, 17)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_017_gap_021_open_close_pressure_84_021'] = {'inputs': ['gap_base_universe_d2_017_gap_021_open_close_pressure_84_021'], 'func': gap_base_universe_d3_017_gap_021_open_close_pressure_84_021}


def gap_base_universe_d3_018_gap_022_lower_wick_ratio_126_022(gap_base_universe_d2_018_gap_022_lower_wick_ratio_126_022):
    return _base_universe_d3(gap_base_universe_d2_018_gap_022_lower_wick_ratio_126_022, 18)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_018_gap_022_lower_wick_ratio_126_022'] = {'inputs': ['gap_base_universe_d2_018_gap_022_lower_wick_ratio_126_022'], 'func': gap_base_universe_d3_018_gap_022_lower_wick_ratio_126_022}


def gap_base_universe_d3_019_gap_023_upper_wick_ratio_189_023(gap_base_universe_d2_019_gap_023_upper_wick_ratio_189_023):
    return _base_universe_d3(gap_base_universe_d2_019_gap_023_upper_wick_ratio_189_023, 19)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_019_gap_023_upper_wick_ratio_189_023'] = {'inputs': ['gap_base_universe_d2_019_gap_023_upper_wick_ratio_189_023'], 'func': gap_base_universe_d3_019_gap_023_upper_wick_ratio_189_023}


def gap_base_universe_d3_020_gap_024_body_to_range_252_024(gap_base_universe_d2_020_gap_024_body_to_range_252_024):
    return _base_universe_d3(gap_base_universe_d2_020_gap_024_body_to_range_252_024, 20)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_020_gap_024_body_to_range_252_024'] = {'inputs': ['gap_base_universe_d2_020_gap_024_body_to_range_252_024'], 'func': gap_base_universe_d3_020_gap_024_body_to_range_252_024}


def gap_base_universe_d3_021_gap_026_gap_magnitude_504_026(gap_base_universe_d2_021_gap_026_gap_magnitude_504_026):
    return _base_universe_d3(gap_base_universe_d2_021_gap_026_gap_magnitude_504_026, 21)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_021_gap_026_gap_magnitude_504_026'] = {'inputs': ['gap_base_universe_d2_021_gap_026_gap_magnitude_504_026'], 'func': gap_base_universe_d3_021_gap_026_gap_magnitude_504_026}


def gap_base_universe_d3_022_gap_027_open_close_pressure_756_027(gap_base_universe_d2_022_gap_027_open_close_pressure_756_027):
    return _base_universe_d3(gap_base_universe_d2_022_gap_027_open_close_pressure_756_027, 22)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_022_gap_027_open_close_pressure_756_027'] = {'inputs': ['gap_base_universe_d2_022_gap_027_open_close_pressure_756_027'], 'func': gap_base_universe_d3_022_gap_027_open_close_pressure_756_027}


def gap_base_universe_d3_023_gap_028_lower_wick_ratio_1008_028(gap_base_universe_d2_023_gap_028_lower_wick_ratio_1008_028):
    return _base_universe_d3(gap_base_universe_d2_023_gap_028_lower_wick_ratio_1008_028, 23)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_023_gap_028_lower_wick_ratio_1008_028'] = {'inputs': ['gap_base_universe_d2_023_gap_028_lower_wick_ratio_1008_028'], 'func': gap_base_universe_d3_023_gap_028_lower_wick_ratio_1008_028}


def gap_base_universe_d3_024_gap_029_upper_wick_ratio_1260_029(gap_base_universe_d2_024_gap_029_upper_wick_ratio_1260_029):
    return _base_universe_d3(gap_base_universe_d2_024_gap_029_upper_wick_ratio_1260_029, 24)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_024_gap_029_upper_wick_ratio_1260_029'] = {'inputs': ['gap_base_universe_d2_024_gap_029_upper_wick_ratio_1260_029'], 'func': gap_base_universe_d3_024_gap_029_upper_wick_ratio_1260_029}


def gap_base_universe_d3_025_gap_030_body_to_range_1512_030(gap_base_universe_d2_025_gap_030_body_to_range_1512_030):
    return _base_universe_d3(gap_base_universe_d2_025_gap_030_body_to_range_1512_030, 25)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_025_gap_030_body_to_range_1512_030'] = {'inputs': ['gap_base_universe_d2_025_gap_030_body_to_range_1512_030'], 'func': gap_base_universe_d3_025_gap_030_body_to_range_1512_030}


def gap_base_universe_d3_026_gap_basefill_031(gap_base_universe_d2_026_gap_basefill_031):
    return _base_universe_d3(gap_base_universe_d2_026_gap_basefill_031, 26)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_026_gap_basefill_031'] = {'inputs': ['gap_base_universe_d2_026_gap_basefill_031'], 'func': gap_base_universe_d3_026_gap_basefill_031}


def gap_base_universe_d3_027_gap_basefill_032(gap_base_universe_d2_027_gap_basefill_032):
    return _base_universe_d3(gap_base_universe_d2_027_gap_basefill_032, 27)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_027_gap_basefill_032'] = {'inputs': ['gap_base_universe_d2_027_gap_basefill_032'], 'func': gap_base_universe_d3_027_gap_basefill_032}


def gap_base_universe_d3_028_gap_basefill_033(gap_base_universe_d2_028_gap_basefill_033):
    return _base_universe_d3(gap_base_universe_d2_028_gap_basefill_033, 28)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_028_gap_basefill_033'] = {'inputs': ['gap_base_universe_d2_028_gap_basefill_033'], 'func': gap_base_universe_d3_028_gap_basefill_033}


def gap_base_universe_d3_029_gap_basefill_034(gap_base_universe_d2_029_gap_basefill_034):
    return _base_universe_d3(gap_base_universe_d2_029_gap_basefill_034, 29)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_029_gap_basefill_034'] = {'inputs': ['gap_base_universe_d2_029_gap_basefill_034'], 'func': gap_base_universe_d3_029_gap_basefill_034}


def gap_base_universe_d3_030_gap_basefill_035(gap_base_universe_d2_030_gap_basefill_035):
    return _base_universe_d3(gap_base_universe_d2_030_gap_basefill_035, 30)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_030_gap_basefill_035'] = {'inputs': ['gap_base_universe_d2_030_gap_basefill_035'], 'func': gap_base_universe_d3_030_gap_basefill_035}


def gap_base_universe_d3_031_gap_basefill_036(gap_base_universe_d2_031_gap_basefill_036):
    return _base_universe_d3(gap_base_universe_d2_031_gap_basefill_036, 31)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_031_gap_basefill_036'] = {'inputs': ['gap_base_universe_d2_031_gap_basefill_036'], 'func': gap_base_universe_d3_031_gap_basefill_036}


def gap_base_universe_d3_032_gap_basefill_037(gap_base_universe_d2_032_gap_basefill_037):
    return _base_universe_d3(gap_base_universe_d2_032_gap_basefill_037, 32)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_032_gap_basefill_037'] = {'inputs': ['gap_base_universe_d2_032_gap_basefill_037'], 'func': gap_base_universe_d3_032_gap_basefill_037}


def gap_base_universe_d3_033_gap_basefill_038(gap_base_universe_d2_033_gap_basefill_038):
    return _base_universe_d3(gap_base_universe_d2_033_gap_basefill_038, 33)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_033_gap_basefill_038'] = {'inputs': ['gap_base_universe_d2_033_gap_basefill_038'], 'func': gap_base_universe_d3_033_gap_basefill_038}


def gap_base_universe_d3_034_gap_basefill_039(gap_base_universe_d2_034_gap_basefill_039):
    return _base_universe_d3(gap_base_universe_d2_034_gap_basefill_039, 34)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_034_gap_basefill_039'] = {'inputs': ['gap_base_universe_d2_034_gap_basefill_039'], 'func': gap_base_universe_d3_034_gap_basefill_039}


def gap_base_universe_d3_035_gap_basefill_040(gap_base_universe_d2_035_gap_basefill_040):
    return _base_universe_d3(gap_base_universe_d2_035_gap_basefill_040, 35)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_035_gap_basefill_040'] = {'inputs': ['gap_base_universe_d2_035_gap_basefill_040'], 'func': gap_base_universe_d3_035_gap_basefill_040}


def gap_base_universe_d3_036_gap_basefill_041(gap_base_universe_d2_036_gap_basefill_041):
    return _base_universe_d3(gap_base_universe_d2_036_gap_basefill_041, 36)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_036_gap_basefill_041'] = {'inputs': ['gap_base_universe_d2_036_gap_basefill_041'], 'func': gap_base_universe_d3_036_gap_basefill_041}


def gap_base_universe_d3_037_gap_basefill_042(gap_base_universe_d2_037_gap_basefill_042):
    return _base_universe_d3(gap_base_universe_d2_037_gap_basefill_042, 37)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_037_gap_basefill_042'] = {'inputs': ['gap_base_universe_d2_037_gap_basefill_042'], 'func': gap_base_universe_d3_037_gap_basefill_042}


def gap_base_universe_d3_038_gap_basefill_043(gap_base_universe_d2_038_gap_basefill_043):
    return _base_universe_d3(gap_base_universe_d2_038_gap_basefill_043, 38)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_038_gap_basefill_043'] = {'inputs': ['gap_base_universe_d2_038_gap_basefill_043'], 'func': gap_base_universe_d3_038_gap_basefill_043}


def gap_base_universe_d3_039_gap_basefill_044(gap_base_universe_d2_039_gap_basefill_044):
    return _base_universe_d3(gap_base_universe_d2_039_gap_basefill_044, 39)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_039_gap_basefill_044'] = {'inputs': ['gap_base_universe_d2_039_gap_basefill_044'], 'func': gap_base_universe_d3_039_gap_basefill_044}


def gap_base_universe_d3_040_gap_basefill_045(gap_base_universe_d2_040_gap_basefill_045):
    return _base_universe_d3(gap_base_universe_d2_040_gap_basefill_045, 40)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_040_gap_basefill_045'] = {'inputs': ['gap_base_universe_d2_040_gap_basefill_045'], 'func': gap_base_universe_d3_040_gap_basefill_045}


def gap_base_universe_d3_041_gap_basefill_046(gap_base_universe_d2_041_gap_basefill_046):
    return _base_universe_d3(gap_base_universe_d2_041_gap_basefill_046, 41)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_041_gap_basefill_046'] = {'inputs': ['gap_base_universe_d2_041_gap_basefill_046'], 'func': gap_base_universe_d3_041_gap_basefill_046}


def gap_base_universe_d3_042_gap_basefill_047(gap_base_universe_d2_042_gap_basefill_047):
    return _base_universe_d3(gap_base_universe_d2_042_gap_basefill_047, 42)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_042_gap_basefill_047'] = {'inputs': ['gap_base_universe_d2_042_gap_basefill_047'], 'func': gap_base_universe_d3_042_gap_basefill_047}


def gap_base_universe_d3_043_gap_basefill_048(gap_base_universe_d2_043_gap_basefill_048):
    return _base_universe_d3(gap_base_universe_d2_043_gap_basefill_048, 43)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_043_gap_basefill_048'] = {'inputs': ['gap_base_universe_d2_043_gap_basefill_048'], 'func': gap_base_universe_d3_043_gap_basefill_048}


def gap_base_universe_d3_044_gap_basefill_049(gap_base_universe_d2_044_gap_basefill_049):
    return _base_universe_d3(gap_base_universe_d2_044_gap_basefill_049, 44)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_044_gap_basefill_049'] = {'inputs': ['gap_base_universe_d2_044_gap_basefill_049'], 'func': gap_base_universe_d3_044_gap_basefill_049}


def gap_base_universe_d3_045_gap_basefill_050(gap_base_universe_d2_045_gap_basefill_050):
    return _base_universe_d3(gap_base_universe_d2_045_gap_basefill_050, 45)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_045_gap_basefill_050'] = {'inputs': ['gap_base_universe_d2_045_gap_basefill_050'], 'func': gap_base_universe_d3_045_gap_basefill_050}


def gap_base_universe_d3_046_gap_basefill_051(gap_base_universe_d2_046_gap_basefill_051):
    return _base_universe_d3(gap_base_universe_d2_046_gap_basefill_051, 46)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_046_gap_basefill_051'] = {'inputs': ['gap_base_universe_d2_046_gap_basefill_051'], 'func': gap_base_universe_d3_046_gap_basefill_051}


def gap_base_universe_d3_047_gap_basefill_052(gap_base_universe_d2_047_gap_basefill_052):
    return _base_universe_d3(gap_base_universe_d2_047_gap_basefill_052, 47)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_047_gap_basefill_052'] = {'inputs': ['gap_base_universe_d2_047_gap_basefill_052'], 'func': gap_base_universe_d3_047_gap_basefill_052}


def gap_base_universe_d3_048_gap_basefill_053(gap_base_universe_d2_048_gap_basefill_053):
    return _base_universe_d3(gap_base_universe_d2_048_gap_basefill_053, 48)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_048_gap_basefill_053'] = {'inputs': ['gap_base_universe_d2_048_gap_basefill_053'], 'func': gap_base_universe_d3_048_gap_basefill_053}


def gap_base_universe_d3_049_gap_basefill_054(gap_base_universe_d2_049_gap_basefill_054):
    return _base_universe_d3(gap_base_universe_d2_049_gap_basefill_054, 49)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_049_gap_basefill_054'] = {'inputs': ['gap_base_universe_d2_049_gap_basefill_054'], 'func': gap_base_universe_d3_049_gap_basefill_054}


def gap_base_universe_d3_050_gap_basefill_055(gap_base_universe_d2_050_gap_basefill_055):
    return _base_universe_d3(gap_base_universe_d2_050_gap_basefill_055, 50)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_050_gap_basefill_055'] = {'inputs': ['gap_base_universe_d2_050_gap_basefill_055'], 'func': gap_base_universe_d3_050_gap_basefill_055}


def gap_base_universe_d3_051_gap_basefill_056(gap_base_universe_d2_051_gap_basefill_056):
    return _base_universe_d3(gap_base_universe_d2_051_gap_basefill_056, 51)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_051_gap_basefill_056'] = {'inputs': ['gap_base_universe_d2_051_gap_basefill_056'], 'func': gap_base_universe_d3_051_gap_basefill_056}


def gap_base_universe_d3_052_gap_basefill_057(gap_base_universe_d2_052_gap_basefill_057):
    return _base_universe_d3(gap_base_universe_d2_052_gap_basefill_057, 52)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_052_gap_basefill_057'] = {'inputs': ['gap_base_universe_d2_052_gap_basefill_057'], 'func': gap_base_universe_d3_052_gap_basefill_057}


def gap_base_universe_d3_053_gap_basefill_058(gap_base_universe_d2_053_gap_basefill_058):
    return _base_universe_d3(gap_base_universe_d2_053_gap_basefill_058, 53)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_053_gap_basefill_058'] = {'inputs': ['gap_base_universe_d2_053_gap_basefill_058'], 'func': gap_base_universe_d3_053_gap_basefill_058}


def gap_base_universe_d3_054_gap_basefill_059(gap_base_universe_d2_054_gap_basefill_059):
    return _base_universe_d3(gap_base_universe_d2_054_gap_basefill_059, 54)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_054_gap_basefill_059'] = {'inputs': ['gap_base_universe_d2_054_gap_basefill_059'], 'func': gap_base_universe_d3_054_gap_basefill_059}


def gap_base_universe_d3_055_gap_basefill_060(gap_base_universe_d2_055_gap_basefill_060):
    return _base_universe_d3(gap_base_universe_d2_055_gap_basefill_060, 55)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_055_gap_basefill_060'] = {'inputs': ['gap_base_universe_d2_055_gap_basefill_060'], 'func': gap_base_universe_d3_055_gap_basefill_060}


def gap_base_universe_d3_056_gap_basefill_061(gap_base_universe_d2_056_gap_basefill_061):
    return _base_universe_d3(gap_base_universe_d2_056_gap_basefill_061, 56)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_056_gap_basefill_061'] = {'inputs': ['gap_base_universe_d2_056_gap_basefill_061'], 'func': gap_base_universe_d3_056_gap_basefill_061}


def gap_base_universe_d3_057_gap_basefill_062(gap_base_universe_d2_057_gap_basefill_062):
    return _base_universe_d3(gap_base_universe_d2_057_gap_basefill_062, 57)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_057_gap_basefill_062'] = {'inputs': ['gap_base_universe_d2_057_gap_basefill_062'], 'func': gap_base_universe_d3_057_gap_basefill_062}


def gap_base_universe_d3_058_gap_basefill_063(gap_base_universe_d2_058_gap_basefill_063):
    return _base_universe_d3(gap_base_universe_d2_058_gap_basefill_063, 58)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_058_gap_basefill_063'] = {'inputs': ['gap_base_universe_d2_058_gap_basefill_063'], 'func': gap_base_universe_d3_058_gap_basefill_063}


def gap_base_universe_d3_059_gap_basefill_064(gap_base_universe_d2_059_gap_basefill_064):
    return _base_universe_d3(gap_base_universe_d2_059_gap_basefill_064, 59)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_059_gap_basefill_064'] = {'inputs': ['gap_base_universe_d2_059_gap_basefill_064'], 'func': gap_base_universe_d3_059_gap_basefill_064}


def gap_base_universe_d3_060_gap_basefill_065(gap_base_universe_d2_060_gap_basefill_065):
    return _base_universe_d3(gap_base_universe_d2_060_gap_basefill_065, 60)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_060_gap_basefill_065'] = {'inputs': ['gap_base_universe_d2_060_gap_basefill_065'], 'func': gap_base_universe_d3_060_gap_basefill_065}


def gap_base_universe_d3_061_gap_basefill_066(gap_base_universe_d2_061_gap_basefill_066):
    return _base_universe_d3(gap_base_universe_d2_061_gap_basefill_066, 61)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_061_gap_basefill_066'] = {'inputs': ['gap_base_universe_d2_061_gap_basefill_066'], 'func': gap_base_universe_d3_061_gap_basefill_066}


def gap_base_universe_d3_062_gap_basefill_067(gap_base_universe_d2_062_gap_basefill_067):
    return _base_universe_d3(gap_base_universe_d2_062_gap_basefill_067, 62)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_062_gap_basefill_067'] = {'inputs': ['gap_base_universe_d2_062_gap_basefill_067'], 'func': gap_base_universe_d3_062_gap_basefill_067}


def gap_base_universe_d3_063_gap_basefill_068(gap_base_universe_d2_063_gap_basefill_068):
    return _base_universe_d3(gap_base_universe_d2_063_gap_basefill_068, 63)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_063_gap_basefill_068'] = {'inputs': ['gap_base_universe_d2_063_gap_basefill_068'], 'func': gap_base_universe_d3_063_gap_basefill_068}


def gap_base_universe_d3_064_gap_basefill_069(gap_base_universe_d2_064_gap_basefill_069):
    return _base_universe_d3(gap_base_universe_d2_064_gap_basefill_069, 64)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_064_gap_basefill_069'] = {'inputs': ['gap_base_universe_d2_064_gap_basefill_069'], 'func': gap_base_universe_d3_064_gap_basefill_069}


def gap_base_universe_d3_065_gap_basefill_070(gap_base_universe_d2_065_gap_basefill_070):
    return _base_universe_d3(gap_base_universe_d2_065_gap_basefill_070, 65)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_065_gap_basefill_070'] = {'inputs': ['gap_base_universe_d2_065_gap_basefill_070'], 'func': gap_base_universe_d3_065_gap_basefill_070}


def gap_base_universe_d3_066_gap_basefill_071(gap_base_universe_d2_066_gap_basefill_071):
    return _base_universe_d3(gap_base_universe_d2_066_gap_basefill_071, 66)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_066_gap_basefill_071'] = {'inputs': ['gap_base_universe_d2_066_gap_basefill_071'], 'func': gap_base_universe_d3_066_gap_basefill_071}


def gap_base_universe_d3_067_gap_basefill_072(gap_base_universe_d2_067_gap_basefill_072):
    return _base_universe_d3(gap_base_universe_d2_067_gap_basefill_072, 67)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_067_gap_basefill_072'] = {'inputs': ['gap_base_universe_d2_067_gap_basefill_072'], 'func': gap_base_universe_d3_067_gap_basefill_072}


def gap_base_universe_d3_068_gap_basefill_073(gap_base_universe_d2_068_gap_basefill_073):
    return _base_universe_d3(gap_base_universe_d2_068_gap_basefill_073, 68)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_068_gap_basefill_073'] = {'inputs': ['gap_base_universe_d2_068_gap_basefill_073'], 'func': gap_base_universe_d3_068_gap_basefill_073}


def gap_base_universe_d3_069_gap_basefill_074(gap_base_universe_d2_069_gap_basefill_074):
    return _base_universe_d3(gap_base_universe_d2_069_gap_basefill_074, 69)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_069_gap_basefill_074'] = {'inputs': ['gap_base_universe_d2_069_gap_basefill_074'], 'func': gap_base_universe_d3_069_gap_basefill_074}


def gap_base_universe_d3_070_gap_basefill_075(gap_base_universe_d2_070_gap_basefill_075):
    return _base_universe_d3(gap_base_universe_d2_070_gap_basefill_075, 70)
GAP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gap_base_universe_d3_070_gap_basefill_075'] = {'inputs': ['gap_base_universe_d2_070_gap_basefill_075'], 'func': gap_base_universe_d3_070_gap_basefill_075}
