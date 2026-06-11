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



def gdc_176_gdc_001_gap_down_frequency_5_001_accel_1(gdc_151_gdc_001_gap_down_frequency_5_001_roc_1):
    feature = _s(gdc_151_gdc_001_gap_down_frequency_5_001_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def gdc_177_gdc_007_gap_down_frequency_126_007_accel_5(gdc_152_gdc_007_gap_down_frequency_126_007_roc_5):
    feature = _s(gdc_152_gdc_007_gap_down_frequency_126_007_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def gdc_178_gdc_013_gap_down_frequency_1008_013_accel_42(gdc_153_gdc_013_gap_down_frequency_1008_013_roc_42):
    feature = _s(gdc_153_gdc_013_gap_down_frequency_1008_013_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def gdc_179_gdc_019_gap_down_frequency_42_019_accel_126(gdc_154_gdc_019_gap_down_frequency_42_019_roc_126):
    feature = _s(gdc_154_gdc_019_gap_down_frequency_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def gdc_180_gdc_025_gap_down_frequency_378_025_accel_378(gdc_155_gdc_025_gap_down_frequency_378_025_roc_378):
    feature = _s(gdc_155_gdc_025_gap_down_frequency_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















GAP_DOWN_CLUSTERING_REGISTRY_3RD_DERIVATIVES = {
    'gdc_176_gdc_001_gap_down_frequency_5_001_accel_1': {'inputs': ['gdc_151_gdc_001_gap_down_frequency_5_001_roc_1'], 'func': gdc_176_gdc_001_gap_down_frequency_5_001_accel_1},
    'gdc_177_gdc_007_gap_down_frequency_126_007_accel_5': {'inputs': ['gdc_152_gdc_007_gap_down_frequency_126_007_roc_5'], 'func': gdc_177_gdc_007_gap_down_frequency_126_007_accel_5},
    'gdc_178_gdc_013_gap_down_frequency_1008_013_accel_42': {'inputs': ['gdc_153_gdc_013_gap_down_frequency_1008_013_roc_42'], 'func': gdc_178_gdc_013_gap_down_frequency_1008_013_accel_42},
    'gdc_179_gdc_019_gap_down_frequency_42_019_accel_126': {'inputs': ['gdc_154_gdc_019_gap_down_frequency_42_019_roc_126'], 'func': gdc_179_gdc_019_gap_down_frequency_42_019_accel_126},
    'gdc_180_gdc_025_gap_down_frequency_378_025_accel_378': {'inputs': ['gdc_155_gdc_025_gap_down_frequency_378_025_roc_378'], 'func': gdc_180_gdc_025_gap_down_frequency_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def gdc_replacement_d3_001(gdc_replacement_d2_001):
    feature = _clean(gdc_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_001'] = {'inputs': ['gdc_replacement_d2_001'], 'func': gdc_replacement_d3_001}


def gdc_replacement_d3_002(gdc_replacement_d2_002):
    feature = _clean(gdc_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_002'] = {'inputs': ['gdc_replacement_d2_002'], 'func': gdc_replacement_d3_002}


def gdc_replacement_d3_003(gdc_replacement_d2_003):
    feature = _clean(gdc_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_003'] = {'inputs': ['gdc_replacement_d2_003'], 'func': gdc_replacement_d3_003}


def gdc_replacement_d3_004(gdc_replacement_d2_004):
    feature = _clean(gdc_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_004'] = {'inputs': ['gdc_replacement_d2_004'], 'func': gdc_replacement_d3_004}


def gdc_replacement_d3_005(gdc_replacement_d2_005):
    feature = _clean(gdc_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_005'] = {'inputs': ['gdc_replacement_d2_005'], 'func': gdc_replacement_d3_005}


def gdc_replacement_d3_006(gdc_replacement_d2_006):
    feature = _clean(gdc_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_006'] = {'inputs': ['gdc_replacement_d2_006'], 'func': gdc_replacement_d3_006}


def gdc_replacement_d3_007(gdc_replacement_d2_007):
    feature = _clean(gdc_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_007'] = {'inputs': ['gdc_replacement_d2_007'], 'func': gdc_replacement_d3_007}


def gdc_replacement_d3_008(gdc_replacement_d2_008):
    feature = _clean(gdc_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_008'] = {'inputs': ['gdc_replacement_d2_008'], 'func': gdc_replacement_d3_008}


def gdc_replacement_d3_009(gdc_replacement_d2_009):
    feature = _clean(gdc_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_009'] = {'inputs': ['gdc_replacement_d2_009'], 'func': gdc_replacement_d3_009}


def gdc_replacement_d3_010(gdc_replacement_d2_010):
    feature = _clean(gdc_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_010'] = {'inputs': ['gdc_replacement_d2_010'], 'func': gdc_replacement_d3_010}


def gdc_replacement_d3_011(gdc_replacement_d2_011):
    feature = _clean(gdc_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_011'] = {'inputs': ['gdc_replacement_d2_011'], 'func': gdc_replacement_d3_011}


def gdc_replacement_d3_012(gdc_replacement_d2_012):
    feature = _clean(gdc_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_012'] = {'inputs': ['gdc_replacement_d2_012'], 'func': gdc_replacement_d3_012}


def gdc_replacement_d3_013(gdc_replacement_d2_013):
    feature = _clean(gdc_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_013'] = {'inputs': ['gdc_replacement_d2_013'], 'func': gdc_replacement_d3_013}


def gdc_replacement_d3_014(gdc_replacement_d2_014):
    feature = _clean(gdc_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_014'] = {'inputs': ['gdc_replacement_d2_014'], 'func': gdc_replacement_d3_014}


def gdc_replacement_d3_015(gdc_replacement_d2_015):
    feature = _clean(gdc_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_015'] = {'inputs': ['gdc_replacement_d2_015'], 'func': gdc_replacement_d3_015}


def gdc_replacement_d3_016(gdc_replacement_d2_016):
    feature = _clean(gdc_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_016'] = {'inputs': ['gdc_replacement_d2_016'], 'func': gdc_replacement_d3_016}


def gdc_replacement_d3_017(gdc_replacement_d2_017):
    feature = _clean(gdc_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_017'] = {'inputs': ['gdc_replacement_d2_017'], 'func': gdc_replacement_d3_017}


def gdc_replacement_d3_018(gdc_replacement_d2_018):
    feature = _clean(gdc_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_018'] = {'inputs': ['gdc_replacement_d2_018'], 'func': gdc_replacement_d3_018}


def gdc_replacement_d3_019(gdc_replacement_d2_019):
    feature = _clean(gdc_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_019'] = {'inputs': ['gdc_replacement_d2_019'], 'func': gdc_replacement_d3_019}


def gdc_replacement_d3_020(gdc_replacement_d2_020):
    feature = _clean(gdc_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_020'] = {'inputs': ['gdc_replacement_d2_020'], 'func': gdc_replacement_d3_020}


def gdc_replacement_d3_021(gdc_replacement_d2_021):
    feature = _clean(gdc_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_021'] = {'inputs': ['gdc_replacement_d2_021'], 'func': gdc_replacement_d3_021}


def gdc_replacement_d3_022(gdc_replacement_d2_022):
    feature = _clean(gdc_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_022'] = {'inputs': ['gdc_replacement_d2_022'], 'func': gdc_replacement_d3_022}


def gdc_replacement_d3_023(gdc_replacement_d2_023):
    feature = _clean(gdc_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_023'] = {'inputs': ['gdc_replacement_d2_023'], 'func': gdc_replacement_d3_023}


def gdc_replacement_d3_024(gdc_replacement_d2_024):
    feature = _clean(gdc_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_024'] = {'inputs': ['gdc_replacement_d2_024'], 'func': gdc_replacement_d3_024}


def gdc_replacement_d3_025(gdc_replacement_d2_025):
    feature = _clean(gdc_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_025'] = {'inputs': ['gdc_replacement_d2_025'], 'func': gdc_replacement_d3_025}


def gdc_replacement_d3_026(gdc_replacement_d2_026):
    feature = _clean(gdc_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_026'] = {'inputs': ['gdc_replacement_d2_026'], 'func': gdc_replacement_d3_026}


def gdc_replacement_d3_027(gdc_replacement_d2_027):
    feature = _clean(gdc_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_027'] = {'inputs': ['gdc_replacement_d2_027'], 'func': gdc_replacement_d3_027}


def gdc_replacement_d3_028(gdc_replacement_d2_028):
    feature = _clean(gdc_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_028'] = {'inputs': ['gdc_replacement_d2_028'], 'func': gdc_replacement_d3_028}


def gdc_replacement_d3_029(gdc_replacement_d2_029):
    feature = _clean(gdc_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_029'] = {'inputs': ['gdc_replacement_d2_029'], 'func': gdc_replacement_d3_029}


def gdc_replacement_d3_030(gdc_replacement_d2_030):
    feature = _clean(gdc_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_030'] = {'inputs': ['gdc_replacement_d2_030'], 'func': gdc_replacement_d3_030}


def gdc_replacement_d3_031(gdc_replacement_d2_031):
    feature = _clean(gdc_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_031'] = {'inputs': ['gdc_replacement_d2_031'], 'func': gdc_replacement_d3_031}


def gdc_replacement_d3_032(gdc_replacement_d2_032):
    feature = _clean(gdc_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_032'] = {'inputs': ['gdc_replacement_d2_032'], 'func': gdc_replacement_d3_032}


def gdc_replacement_d3_033(gdc_replacement_d2_033):
    feature = _clean(gdc_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_033'] = {'inputs': ['gdc_replacement_d2_033'], 'func': gdc_replacement_d3_033}


def gdc_replacement_d3_034(gdc_replacement_d2_034):
    feature = _clean(gdc_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_034'] = {'inputs': ['gdc_replacement_d2_034'], 'func': gdc_replacement_d3_034}


def gdc_replacement_d3_035(gdc_replacement_d2_035):
    feature = _clean(gdc_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_035'] = {'inputs': ['gdc_replacement_d2_035'], 'func': gdc_replacement_d3_035}


def gdc_replacement_d3_036(gdc_replacement_d2_036):
    feature = _clean(gdc_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_036'] = {'inputs': ['gdc_replacement_d2_036'], 'func': gdc_replacement_d3_036}


def gdc_replacement_d3_037(gdc_replacement_d2_037):
    feature = _clean(gdc_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_037'] = {'inputs': ['gdc_replacement_d2_037'], 'func': gdc_replacement_d3_037}


def gdc_replacement_d3_038(gdc_replacement_d2_038):
    feature = _clean(gdc_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_038'] = {'inputs': ['gdc_replacement_d2_038'], 'func': gdc_replacement_d3_038}


def gdc_replacement_d3_039(gdc_replacement_d2_039):
    feature = _clean(gdc_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_039'] = {'inputs': ['gdc_replacement_d2_039'], 'func': gdc_replacement_d3_039}


def gdc_replacement_d3_040(gdc_replacement_d2_040):
    feature = _clean(gdc_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_040'] = {'inputs': ['gdc_replacement_d2_040'], 'func': gdc_replacement_d3_040}


def gdc_replacement_d3_041(gdc_replacement_d2_041):
    feature = _clean(gdc_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_041'] = {'inputs': ['gdc_replacement_d2_041'], 'func': gdc_replacement_d3_041}


def gdc_replacement_d3_042(gdc_replacement_d2_042):
    feature = _clean(gdc_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_042'] = {'inputs': ['gdc_replacement_d2_042'], 'func': gdc_replacement_d3_042}


def gdc_replacement_d3_043(gdc_replacement_d2_043):
    feature = _clean(gdc_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_043'] = {'inputs': ['gdc_replacement_d2_043'], 'func': gdc_replacement_d3_043}


def gdc_replacement_d3_044(gdc_replacement_d2_044):
    feature = _clean(gdc_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_044'] = {'inputs': ['gdc_replacement_d2_044'], 'func': gdc_replacement_d3_044}


def gdc_replacement_d3_045(gdc_replacement_d2_045):
    feature = _clean(gdc_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_045'] = {'inputs': ['gdc_replacement_d2_045'], 'func': gdc_replacement_d3_045}


def gdc_replacement_d3_046(gdc_replacement_d2_046):
    feature = _clean(gdc_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_046'] = {'inputs': ['gdc_replacement_d2_046'], 'func': gdc_replacement_d3_046}


def gdc_replacement_d3_047(gdc_replacement_d2_047):
    feature = _clean(gdc_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_047'] = {'inputs': ['gdc_replacement_d2_047'], 'func': gdc_replacement_d3_047}


def gdc_replacement_d3_048(gdc_replacement_d2_048):
    feature = _clean(gdc_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_048'] = {'inputs': ['gdc_replacement_d2_048'], 'func': gdc_replacement_d3_048}


def gdc_replacement_d3_049(gdc_replacement_d2_049):
    feature = _clean(gdc_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_049'] = {'inputs': ['gdc_replacement_d2_049'], 'func': gdc_replacement_d3_049}


def gdc_replacement_d3_050(gdc_replacement_d2_050):
    feature = _clean(gdc_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_050'] = {'inputs': ['gdc_replacement_d2_050'], 'func': gdc_replacement_d3_050}


def gdc_replacement_d3_051(gdc_replacement_d2_051):
    feature = _clean(gdc_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_051'] = {'inputs': ['gdc_replacement_d2_051'], 'func': gdc_replacement_d3_051}


def gdc_replacement_d3_052(gdc_replacement_d2_052):
    feature = _clean(gdc_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_052'] = {'inputs': ['gdc_replacement_d2_052'], 'func': gdc_replacement_d3_052}


def gdc_replacement_d3_053(gdc_replacement_d2_053):
    feature = _clean(gdc_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_053'] = {'inputs': ['gdc_replacement_d2_053'], 'func': gdc_replacement_d3_053}


def gdc_replacement_d3_054(gdc_replacement_d2_054):
    feature = _clean(gdc_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_054'] = {'inputs': ['gdc_replacement_d2_054'], 'func': gdc_replacement_d3_054}


def gdc_replacement_d3_055(gdc_replacement_d2_055):
    feature = _clean(gdc_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_055'] = {'inputs': ['gdc_replacement_d2_055'], 'func': gdc_replacement_d3_055}


def gdc_replacement_d3_056(gdc_replacement_d2_056):
    feature = _clean(gdc_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_056'] = {'inputs': ['gdc_replacement_d2_056'], 'func': gdc_replacement_d3_056}


def gdc_replacement_d3_057(gdc_replacement_d2_057):
    feature = _clean(gdc_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_057'] = {'inputs': ['gdc_replacement_d2_057'], 'func': gdc_replacement_d3_057}


def gdc_replacement_d3_058(gdc_replacement_d2_058):
    feature = _clean(gdc_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_058'] = {'inputs': ['gdc_replacement_d2_058'], 'func': gdc_replacement_d3_058}


def gdc_replacement_d3_059(gdc_replacement_d2_059):
    feature = _clean(gdc_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_059'] = {'inputs': ['gdc_replacement_d2_059'], 'func': gdc_replacement_d3_059}


def gdc_replacement_d3_060(gdc_replacement_d2_060):
    feature = _clean(gdc_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_060'] = {'inputs': ['gdc_replacement_d2_060'], 'func': gdc_replacement_d3_060}


def gdc_replacement_d3_061(gdc_replacement_d2_061):
    feature = _clean(gdc_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_061'] = {'inputs': ['gdc_replacement_d2_061'], 'func': gdc_replacement_d3_061}


def gdc_replacement_d3_062(gdc_replacement_d2_062):
    feature = _clean(gdc_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_062'] = {'inputs': ['gdc_replacement_d2_062'], 'func': gdc_replacement_d3_062}


def gdc_replacement_d3_063(gdc_replacement_d2_063):
    feature = _clean(gdc_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_063'] = {'inputs': ['gdc_replacement_d2_063'], 'func': gdc_replacement_d3_063}


def gdc_replacement_d3_064(gdc_replacement_d2_064):
    feature = _clean(gdc_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_064'] = {'inputs': ['gdc_replacement_d2_064'], 'func': gdc_replacement_d3_064}


def gdc_replacement_d3_065(gdc_replacement_d2_065):
    feature = _clean(gdc_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_065'] = {'inputs': ['gdc_replacement_d2_065'], 'func': gdc_replacement_d3_065}


def gdc_replacement_d3_066(gdc_replacement_d2_066):
    feature = _clean(gdc_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_066'] = {'inputs': ['gdc_replacement_d2_066'], 'func': gdc_replacement_d3_066}


def gdc_replacement_d3_067(gdc_replacement_d2_067):
    feature = _clean(gdc_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_067'] = {'inputs': ['gdc_replacement_d2_067'], 'func': gdc_replacement_d3_067}


def gdc_replacement_d3_068(gdc_replacement_d2_068):
    feature = _clean(gdc_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_068'] = {'inputs': ['gdc_replacement_d2_068'], 'func': gdc_replacement_d3_068}


def gdc_replacement_d3_069(gdc_replacement_d2_069):
    feature = _clean(gdc_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_069'] = {'inputs': ['gdc_replacement_d2_069'], 'func': gdc_replacement_d3_069}


def gdc_replacement_d3_070(gdc_replacement_d2_070):
    feature = _clean(gdc_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_070'] = {'inputs': ['gdc_replacement_d2_070'], 'func': gdc_replacement_d3_070}


def gdc_replacement_d3_071(gdc_replacement_d2_071):
    feature = _clean(gdc_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_071'] = {'inputs': ['gdc_replacement_d2_071'], 'func': gdc_replacement_d3_071}


def gdc_replacement_d3_072(gdc_replacement_d2_072):
    feature = _clean(gdc_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_072'] = {'inputs': ['gdc_replacement_d2_072'], 'func': gdc_replacement_d3_072}


def gdc_replacement_d3_073(gdc_replacement_d2_073):
    feature = _clean(gdc_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_073'] = {'inputs': ['gdc_replacement_d2_073'], 'func': gdc_replacement_d3_073}


def gdc_replacement_d3_074(gdc_replacement_d2_074):
    feature = _clean(gdc_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_074'] = {'inputs': ['gdc_replacement_d2_074'], 'func': gdc_replacement_d3_074}


def gdc_replacement_d3_075(gdc_replacement_d2_075):
    feature = _clean(gdc_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_075'] = {'inputs': ['gdc_replacement_d2_075'], 'func': gdc_replacement_d3_075}


def gdc_replacement_d3_076(gdc_replacement_d2_076):
    feature = _clean(gdc_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_076'] = {'inputs': ['gdc_replacement_d2_076'], 'func': gdc_replacement_d3_076}


def gdc_replacement_d3_077(gdc_replacement_d2_077):
    feature = _clean(gdc_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_077'] = {'inputs': ['gdc_replacement_d2_077'], 'func': gdc_replacement_d3_077}


def gdc_replacement_d3_078(gdc_replacement_d2_078):
    feature = _clean(gdc_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_078'] = {'inputs': ['gdc_replacement_d2_078'], 'func': gdc_replacement_d3_078}


def gdc_replacement_d3_079(gdc_replacement_d2_079):
    feature = _clean(gdc_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_079'] = {'inputs': ['gdc_replacement_d2_079'], 'func': gdc_replacement_d3_079}


def gdc_replacement_d3_080(gdc_replacement_d2_080):
    feature = _clean(gdc_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_080'] = {'inputs': ['gdc_replacement_d2_080'], 'func': gdc_replacement_d3_080}


def gdc_replacement_d3_081(gdc_replacement_d2_081):
    feature = _clean(gdc_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_081'] = {'inputs': ['gdc_replacement_d2_081'], 'func': gdc_replacement_d3_081}


def gdc_replacement_d3_082(gdc_replacement_d2_082):
    feature = _clean(gdc_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_082'] = {'inputs': ['gdc_replacement_d2_082'], 'func': gdc_replacement_d3_082}


def gdc_replacement_d3_083(gdc_replacement_d2_083):
    feature = _clean(gdc_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_083'] = {'inputs': ['gdc_replacement_d2_083'], 'func': gdc_replacement_d3_083}


def gdc_replacement_d3_084(gdc_replacement_d2_084):
    feature = _clean(gdc_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_084'] = {'inputs': ['gdc_replacement_d2_084'], 'func': gdc_replacement_d3_084}


def gdc_replacement_d3_085(gdc_replacement_d2_085):
    feature = _clean(gdc_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_085'] = {'inputs': ['gdc_replacement_d2_085'], 'func': gdc_replacement_d3_085}


def gdc_replacement_d3_086(gdc_replacement_d2_086):
    feature = _clean(gdc_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_086'] = {'inputs': ['gdc_replacement_d2_086'], 'func': gdc_replacement_d3_086}


def gdc_replacement_d3_087(gdc_replacement_d2_087):
    feature = _clean(gdc_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_087'] = {'inputs': ['gdc_replacement_d2_087'], 'func': gdc_replacement_d3_087}


def gdc_replacement_d3_088(gdc_replacement_d2_088):
    feature = _clean(gdc_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_088'] = {'inputs': ['gdc_replacement_d2_088'], 'func': gdc_replacement_d3_088}


def gdc_replacement_d3_089(gdc_replacement_d2_089):
    feature = _clean(gdc_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_089'] = {'inputs': ['gdc_replacement_d2_089'], 'func': gdc_replacement_d3_089}


def gdc_replacement_d3_090(gdc_replacement_d2_090):
    feature = _clean(gdc_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_090'] = {'inputs': ['gdc_replacement_d2_090'], 'func': gdc_replacement_d3_090}


def gdc_replacement_d3_091(gdc_replacement_d2_091):
    feature = _clean(gdc_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_091'] = {'inputs': ['gdc_replacement_d2_091'], 'func': gdc_replacement_d3_091}


def gdc_replacement_d3_092(gdc_replacement_d2_092):
    feature = _clean(gdc_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_092'] = {'inputs': ['gdc_replacement_d2_092'], 'func': gdc_replacement_d3_092}


def gdc_replacement_d3_093(gdc_replacement_d2_093):
    feature = _clean(gdc_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_093'] = {'inputs': ['gdc_replacement_d2_093'], 'func': gdc_replacement_d3_093}


def gdc_replacement_d3_094(gdc_replacement_d2_094):
    feature = _clean(gdc_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_094'] = {'inputs': ['gdc_replacement_d2_094'], 'func': gdc_replacement_d3_094}


def gdc_replacement_d3_095(gdc_replacement_d2_095):
    feature = _clean(gdc_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_095'] = {'inputs': ['gdc_replacement_d2_095'], 'func': gdc_replacement_d3_095}


def gdc_replacement_d3_096(gdc_replacement_d2_096):
    feature = _clean(gdc_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_096'] = {'inputs': ['gdc_replacement_d2_096'], 'func': gdc_replacement_d3_096}


def gdc_replacement_d3_097(gdc_replacement_d2_097):
    feature = _clean(gdc_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_097'] = {'inputs': ['gdc_replacement_d2_097'], 'func': gdc_replacement_d3_097}


def gdc_replacement_d3_098(gdc_replacement_d2_098):
    feature = _clean(gdc_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_098'] = {'inputs': ['gdc_replacement_d2_098'], 'func': gdc_replacement_d3_098}


def gdc_replacement_d3_099(gdc_replacement_d2_099):
    feature = _clean(gdc_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_099'] = {'inputs': ['gdc_replacement_d2_099'], 'func': gdc_replacement_d3_099}


def gdc_replacement_d3_100(gdc_replacement_d2_100):
    feature = _clean(gdc_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_100'] = {'inputs': ['gdc_replacement_d2_100'], 'func': gdc_replacement_d3_100}


def gdc_replacement_d3_101(gdc_replacement_d2_101):
    feature = _clean(gdc_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_101'] = {'inputs': ['gdc_replacement_d2_101'], 'func': gdc_replacement_d3_101}


def gdc_replacement_d3_102(gdc_replacement_d2_102):
    feature = _clean(gdc_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_102'] = {'inputs': ['gdc_replacement_d2_102'], 'func': gdc_replacement_d3_102}


def gdc_replacement_d3_103(gdc_replacement_d2_103):
    feature = _clean(gdc_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_103'] = {'inputs': ['gdc_replacement_d2_103'], 'func': gdc_replacement_d3_103}


def gdc_replacement_d3_104(gdc_replacement_d2_104):
    feature = _clean(gdc_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_104'] = {'inputs': ['gdc_replacement_d2_104'], 'func': gdc_replacement_d3_104}


def gdc_replacement_d3_105(gdc_replacement_d2_105):
    feature = _clean(gdc_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_105'] = {'inputs': ['gdc_replacement_d2_105'], 'func': gdc_replacement_d3_105}


def gdc_replacement_d3_106(gdc_replacement_d2_106):
    feature = _clean(gdc_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_106'] = {'inputs': ['gdc_replacement_d2_106'], 'func': gdc_replacement_d3_106}


def gdc_replacement_d3_107(gdc_replacement_d2_107):
    feature = _clean(gdc_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_107'] = {'inputs': ['gdc_replacement_d2_107'], 'func': gdc_replacement_d3_107}


def gdc_replacement_d3_108(gdc_replacement_d2_108):
    feature = _clean(gdc_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_108'] = {'inputs': ['gdc_replacement_d2_108'], 'func': gdc_replacement_d3_108}


def gdc_replacement_d3_109(gdc_replacement_d2_109):
    feature = _clean(gdc_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_109'] = {'inputs': ['gdc_replacement_d2_109'], 'func': gdc_replacement_d3_109}


def gdc_replacement_d3_110(gdc_replacement_d2_110):
    feature = _clean(gdc_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_110'] = {'inputs': ['gdc_replacement_d2_110'], 'func': gdc_replacement_d3_110}


def gdc_replacement_d3_111(gdc_replacement_d2_111):
    feature = _clean(gdc_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_111'] = {'inputs': ['gdc_replacement_d2_111'], 'func': gdc_replacement_d3_111}


def gdc_replacement_d3_112(gdc_replacement_d2_112):
    feature = _clean(gdc_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_112'] = {'inputs': ['gdc_replacement_d2_112'], 'func': gdc_replacement_d3_112}


def gdc_replacement_d3_113(gdc_replacement_d2_113):
    feature = _clean(gdc_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_113'] = {'inputs': ['gdc_replacement_d2_113'], 'func': gdc_replacement_d3_113}


def gdc_replacement_d3_114(gdc_replacement_d2_114):
    feature = _clean(gdc_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_114'] = {'inputs': ['gdc_replacement_d2_114'], 'func': gdc_replacement_d3_114}


def gdc_replacement_d3_115(gdc_replacement_d2_115):
    feature = _clean(gdc_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_115'] = {'inputs': ['gdc_replacement_d2_115'], 'func': gdc_replacement_d3_115}


def gdc_replacement_d3_116(gdc_replacement_d2_116):
    feature = _clean(gdc_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_116'] = {'inputs': ['gdc_replacement_d2_116'], 'func': gdc_replacement_d3_116}


def gdc_replacement_d3_117(gdc_replacement_d2_117):
    feature = _clean(gdc_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_117'] = {'inputs': ['gdc_replacement_d2_117'], 'func': gdc_replacement_d3_117}


def gdc_replacement_d3_118(gdc_replacement_d2_118):
    feature = _clean(gdc_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_118'] = {'inputs': ['gdc_replacement_d2_118'], 'func': gdc_replacement_d3_118}


def gdc_replacement_d3_119(gdc_replacement_d2_119):
    feature = _clean(gdc_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_119'] = {'inputs': ['gdc_replacement_d2_119'], 'func': gdc_replacement_d3_119}


def gdc_replacement_d3_120(gdc_replacement_d2_120):
    feature = _clean(gdc_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_120'] = {'inputs': ['gdc_replacement_d2_120'], 'func': gdc_replacement_d3_120}


def gdc_replacement_d3_121(gdc_replacement_d2_121):
    feature = _clean(gdc_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_121'] = {'inputs': ['gdc_replacement_d2_121'], 'func': gdc_replacement_d3_121}


def gdc_replacement_d3_122(gdc_replacement_d2_122):
    feature = _clean(gdc_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_122'] = {'inputs': ['gdc_replacement_d2_122'], 'func': gdc_replacement_d3_122}


def gdc_replacement_d3_123(gdc_replacement_d2_123):
    feature = _clean(gdc_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_123'] = {'inputs': ['gdc_replacement_d2_123'], 'func': gdc_replacement_d3_123}


def gdc_replacement_d3_124(gdc_replacement_d2_124):
    feature = _clean(gdc_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_124'] = {'inputs': ['gdc_replacement_d2_124'], 'func': gdc_replacement_d3_124}


def gdc_replacement_d3_125(gdc_replacement_d2_125):
    feature = _clean(gdc_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_125'] = {'inputs': ['gdc_replacement_d2_125'], 'func': gdc_replacement_d3_125}


def gdc_replacement_d3_126(gdc_replacement_d2_126):
    feature = _clean(gdc_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_126'] = {'inputs': ['gdc_replacement_d2_126'], 'func': gdc_replacement_d3_126}


def gdc_replacement_d3_127(gdc_replacement_d2_127):
    feature = _clean(gdc_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_127'] = {'inputs': ['gdc_replacement_d2_127'], 'func': gdc_replacement_d3_127}


def gdc_replacement_d3_128(gdc_replacement_d2_128):
    feature = _clean(gdc_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_128'] = {'inputs': ['gdc_replacement_d2_128'], 'func': gdc_replacement_d3_128}


def gdc_replacement_d3_129(gdc_replacement_d2_129):
    feature = _clean(gdc_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_129'] = {'inputs': ['gdc_replacement_d2_129'], 'func': gdc_replacement_d3_129}


def gdc_replacement_d3_130(gdc_replacement_d2_130):
    feature = _clean(gdc_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_130'] = {'inputs': ['gdc_replacement_d2_130'], 'func': gdc_replacement_d3_130}


def gdc_replacement_d3_131(gdc_replacement_d2_131):
    feature = _clean(gdc_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_131'] = {'inputs': ['gdc_replacement_d2_131'], 'func': gdc_replacement_d3_131}


def gdc_replacement_d3_132(gdc_replacement_d2_132):
    feature = _clean(gdc_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_132'] = {'inputs': ['gdc_replacement_d2_132'], 'func': gdc_replacement_d3_132}


def gdc_replacement_d3_133(gdc_replacement_d2_133):
    feature = _clean(gdc_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_133'] = {'inputs': ['gdc_replacement_d2_133'], 'func': gdc_replacement_d3_133}


def gdc_replacement_d3_134(gdc_replacement_d2_134):
    feature = _clean(gdc_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_134'] = {'inputs': ['gdc_replacement_d2_134'], 'func': gdc_replacement_d3_134}


def gdc_replacement_d3_135(gdc_replacement_d2_135):
    feature = _clean(gdc_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_135'] = {'inputs': ['gdc_replacement_d2_135'], 'func': gdc_replacement_d3_135}


def gdc_replacement_d3_136(gdc_replacement_d2_136):
    feature = _clean(gdc_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_136'] = {'inputs': ['gdc_replacement_d2_136'], 'func': gdc_replacement_d3_136}


def gdc_replacement_d3_137(gdc_replacement_d2_137):
    feature = _clean(gdc_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_137'] = {'inputs': ['gdc_replacement_d2_137'], 'func': gdc_replacement_d3_137}


def gdc_replacement_d3_138(gdc_replacement_d2_138):
    feature = _clean(gdc_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_138'] = {'inputs': ['gdc_replacement_d2_138'], 'func': gdc_replacement_d3_138}


def gdc_replacement_d3_139(gdc_replacement_d2_139):
    feature = _clean(gdc_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_139'] = {'inputs': ['gdc_replacement_d2_139'], 'func': gdc_replacement_d3_139}


def gdc_replacement_d3_140(gdc_replacement_d2_140):
    feature = _clean(gdc_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_140'] = {'inputs': ['gdc_replacement_d2_140'], 'func': gdc_replacement_d3_140}


def gdc_replacement_d3_141(gdc_replacement_d2_141):
    feature = _clean(gdc_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_141'] = {'inputs': ['gdc_replacement_d2_141'], 'func': gdc_replacement_d3_141}


def gdc_replacement_d3_142(gdc_replacement_d2_142):
    feature = _clean(gdc_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_142'] = {'inputs': ['gdc_replacement_d2_142'], 'func': gdc_replacement_d3_142}


def gdc_replacement_d3_143(gdc_replacement_d2_143):
    feature = _clean(gdc_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_143'] = {'inputs': ['gdc_replacement_d2_143'], 'func': gdc_replacement_d3_143}


def gdc_replacement_d3_144(gdc_replacement_d2_144):
    feature = _clean(gdc_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_144'] = {'inputs': ['gdc_replacement_d2_144'], 'func': gdc_replacement_d3_144}


def gdc_replacement_d3_145(gdc_replacement_d2_145):
    feature = _clean(gdc_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_145'] = {'inputs': ['gdc_replacement_d2_145'], 'func': gdc_replacement_d3_145}


def gdc_replacement_d3_146(gdc_replacement_d2_146):
    feature = _clean(gdc_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_146'] = {'inputs': ['gdc_replacement_d2_146'], 'func': gdc_replacement_d3_146}


def gdc_replacement_d3_147(gdc_replacement_d2_147):
    feature = _clean(gdc_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_147'] = {'inputs': ['gdc_replacement_d2_147'], 'func': gdc_replacement_d3_147}


def gdc_replacement_d3_148(gdc_replacement_d2_148):
    feature = _clean(gdc_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_148'] = {'inputs': ['gdc_replacement_d2_148'], 'func': gdc_replacement_d3_148}


def gdc_replacement_d3_149(gdc_replacement_d2_149):
    feature = _clean(gdc_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_149'] = {'inputs': ['gdc_replacement_d2_149'], 'func': gdc_replacement_d3_149}


def gdc_replacement_d3_150(gdc_replacement_d2_150):
    feature = _clean(gdc_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_150'] = {'inputs': ['gdc_replacement_d2_150'], 'func': gdc_replacement_d3_150}


def gdc_replacement_d3_151(gdc_replacement_d2_151):
    feature = _clean(gdc_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_151'] = {'inputs': ['gdc_replacement_d2_151'], 'func': gdc_replacement_d3_151}


def gdc_replacement_d3_152(gdc_replacement_d2_152):
    feature = _clean(gdc_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_152'] = {'inputs': ['gdc_replacement_d2_152'], 'func': gdc_replacement_d3_152}


def gdc_replacement_d3_153(gdc_replacement_d2_153):
    feature = _clean(gdc_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_153'] = {'inputs': ['gdc_replacement_d2_153'], 'func': gdc_replacement_d3_153}


def gdc_replacement_d3_154(gdc_replacement_d2_154):
    feature = _clean(gdc_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_154'] = {'inputs': ['gdc_replacement_d2_154'], 'func': gdc_replacement_d3_154}


def gdc_replacement_d3_155(gdc_replacement_d2_155):
    feature = _clean(gdc_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_155'] = {'inputs': ['gdc_replacement_d2_155'], 'func': gdc_replacement_d3_155}


def gdc_replacement_d3_156(gdc_replacement_d2_156):
    feature = _clean(gdc_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_156'] = {'inputs': ['gdc_replacement_d2_156'], 'func': gdc_replacement_d3_156}


def gdc_replacement_d3_157(gdc_replacement_d2_157):
    feature = _clean(gdc_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_157'] = {'inputs': ['gdc_replacement_d2_157'], 'func': gdc_replacement_d3_157}


def gdc_replacement_d3_158(gdc_replacement_d2_158):
    feature = _clean(gdc_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_158'] = {'inputs': ['gdc_replacement_d2_158'], 'func': gdc_replacement_d3_158}


def gdc_replacement_d3_159(gdc_replacement_d2_159):
    feature = _clean(gdc_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_159'] = {'inputs': ['gdc_replacement_d2_159'], 'func': gdc_replacement_d3_159}


def gdc_replacement_d3_160(gdc_replacement_d2_160):
    feature = _clean(gdc_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
GDC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gdc_replacement_d3_160'] = {'inputs': ['gdc_replacement_d2_160'], 'func': gdc_replacement_d3_160}


# Third-derivative extensions for repaired first-base features.
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def gdc_base_universe_d3_001_gdc_002_gap_magnitude_10_002(gdc_base_universe_d2_001_gdc_002_gap_magnitude_10_002):
    return _base_universe_d3(gdc_base_universe_d2_001_gdc_002_gap_magnitude_10_002, 1)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_001_gdc_002_gap_magnitude_10_002'] = {'inputs': ['gdc_base_universe_d2_001_gdc_002_gap_magnitude_10_002'], 'func': gdc_base_universe_d3_001_gdc_002_gap_magnitude_10_002}


def gdc_base_universe_d3_002_gdc_003_open_close_pressure_21_003(gdc_base_universe_d2_002_gdc_003_open_close_pressure_21_003):
    return _base_universe_d3(gdc_base_universe_d2_002_gdc_003_open_close_pressure_21_003, 2)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_002_gdc_003_open_close_pressure_21_003'] = {'inputs': ['gdc_base_universe_d2_002_gdc_003_open_close_pressure_21_003'], 'func': gdc_base_universe_d3_002_gdc_003_open_close_pressure_21_003}


def gdc_base_universe_d3_003_gdc_004_lower_wick_ratio_42_004(gdc_base_universe_d2_003_gdc_004_lower_wick_ratio_42_004):
    return _base_universe_d3(gdc_base_universe_d2_003_gdc_004_lower_wick_ratio_42_004, 3)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_003_gdc_004_lower_wick_ratio_42_004'] = {'inputs': ['gdc_base_universe_d2_003_gdc_004_lower_wick_ratio_42_004'], 'func': gdc_base_universe_d3_003_gdc_004_lower_wick_ratio_42_004}


def gdc_base_universe_d3_004_gdc_005_upper_wick_ratio_63_005(gdc_base_universe_d2_004_gdc_005_upper_wick_ratio_63_005):
    return _base_universe_d3(gdc_base_universe_d2_004_gdc_005_upper_wick_ratio_63_005, 4)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_004_gdc_005_upper_wick_ratio_63_005'] = {'inputs': ['gdc_base_universe_d2_004_gdc_005_upper_wick_ratio_63_005'], 'func': gdc_base_universe_d3_004_gdc_005_upper_wick_ratio_63_005}


def gdc_base_universe_d3_005_gdc_006_body_to_range_84_006(gdc_base_universe_d2_005_gdc_006_body_to_range_84_006):
    return _base_universe_d3(gdc_base_universe_d2_005_gdc_006_body_to_range_84_006, 5)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_005_gdc_006_body_to_range_84_006'] = {'inputs': ['gdc_base_universe_d2_005_gdc_006_body_to_range_84_006'], 'func': gdc_base_universe_d3_005_gdc_006_body_to_range_84_006}


def gdc_base_universe_d3_006_gdc_008_gap_magnitude_189_008(gdc_base_universe_d2_006_gdc_008_gap_magnitude_189_008):
    return _base_universe_d3(gdc_base_universe_d2_006_gdc_008_gap_magnitude_189_008, 6)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_006_gdc_008_gap_magnitude_189_008'] = {'inputs': ['gdc_base_universe_d2_006_gdc_008_gap_magnitude_189_008'], 'func': gdc_base_universe_d3_006_gdc_008_gap_magnitude_189_008}


def gdc_base_universe_d3_007_gdc_009_open_close_pressure_252_009(gdc_base_universe_d2_007_gdc_009_open_close_pressure_252_009):
    return _base_universe_d3(gdc_base_universe_d2_007_gdc_009_open_close_pressure_252_009, 7)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_007_gdc_009_open_close_pressure_252_009'] = {'inputs': ['gdc_base_universe_d2_007_gdc_009_open_close_pressure_252_009'], 'func': gdc_base_universe_d3_007_gdc_009_open_close_pressure_252_009}


def gdc_base_universe_d3_008_gdc_010_lower_wick_ratio_378_010(gdc_base_universe_d2_008_gdc_010_lower_wick_ratio_378_010):
    return _base_universe_d3(gdc_base_universe_d2_008_gdc_010_lower_wick_ratio_378_010, 8)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_008_gdc_010_lower_wick_ratio_378_010'] = {'inputs': ['gdc_base_universe_d2_008_gdc_010_lower_wick_ratio_378_010'], 'func': gdc_base_universe_d3_008_gdc_010_lower_wick_ratio_378_010}


def gdc_base_universe_d3_009_gdc_011_upper_wick_ratio_504_011(gdc_base_universe_d2_009_gdc_011_upper_wick_ratio_504_011):
    return _base_universe_d3(gdc_base_universe_d2_009_gdc_011_upper_wick_ratio_504_011, 9)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_009_gdc_011_upper_wick_ratio_504_011'] = {'inputs': ['gdc_base_universe_d2_009_gdc_011_upper_wick_ratio_504_011'], 'func': gdc_base_universe_d3_009_gdc_011_upper_wick_ratio_504_011}


def gdc_base_universe_d3_010_gdc_012_body_to_range_756_012(gdc_base_universe_d2_010_gdc_012_body_to_range_756_012):
    return _base_universe_d3(gdc_base_universe_d2_010_gdc_012_body_to_range_756_012, 10)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_010_gdc_012_body_to_range_756_012'] = {'inputs': ['gdc_base_universe_d2_010_gdc_012_body_to_range_756_012'], 'func': gdc_base_universe_d3_010_gdc_012_body_to_range_756_012}


def gdc_base_universe_d3_011_gdc_014_gap_magnitude_1260_014(gdc_base_universe_d2_011_gdc_014_gap_magnitude_1260_014):
    return _base_universe_d3(gdc_base_universe_d2_011_gdc_014_gap_magnitude_1260_014, 11)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_011_gdc_014_gap_magnitude_1260_014'] = {'inputs': ['gdc_base_universe_d2_011_gdc_014_gap_magnitude_1260_014'], 'func': gdc_base_universe_d3_011_gdc_014_gap_magnitude_1260_014}


def gdc_base_universe_d3_012_gdc_015_open_close_pressure_1512_015(gdc_base_universe_d2_012_gdc_015_open_close_pressure_1512_015):
    return _base_universe_d3(gdc_base_universe_d2_012_gdc_015_open_close_pressure_1512_015, 12)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_012_gdc_015_open_close_pressure_1512_015'] = {'inputs': ['gdc_base_universe_d2_012_gdc_015_open_close_pressure_1512_015'], 'func': gdc_base_universe_d3_012_gdc_015_open_close_pressure_1512_015}


def gdc_base_universe_d3_013_gdc_016_lower_wick_ratio_5_016(gdc_base_universe_d2_013_gdc_016_lower_wick_ratio_5_016):
    return _base_universe_d3(gdc_base_universe_d2_013_gdc_016_lower_wick_ratio_5_016, 13)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_013_gdc_016_lower_wick_ratio_5_016'] = {'inputs': ['gdc_base_universe_d2_013_gdc_016_lower_wick_ratio_5_016'], 'func': gdc_base_universe_d3_013_gdc_016_lower_wick_ratio_5_016}


def gdc_base_universe_d3_014_gdc_017_upper_wick_ratio_10_017(gdc_base_universe_d2_014_gdc_017_upper_wick_ratio_10_017):
    return _base_universe_d3(gdc_base_universe_d2_014_gdc_017_upper_wick_ratio_10_017, 14)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_014_gdc_017_upper_wick_ratio_10_017'] = {'inputs': ['gdc_base_universe_d2_014_gdc_017_upper_wick_ratio_10_017'], 'func': gdc_base_universe_d3_014_gdc_017_upper_wick_ratio_10_017}


def gdc_base_universe_d3_015_gdc_018_body_to_range_21_018(gdc_base_universe_d2_015_gdc_018_body_to_range_21_018):
    return _base_universe_d3(gdc_base_universe_d2_015_gdc_018_body_to_range_21_018, 15)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_015_gdc_018_body_to_range_21_018'] = {'inputs': ['gdc_base_universe_d2_015_gdc_018_body_to_range_21_018'], 'func': gdc_base_universe_d3_015_gdc_018_body_to_range_21_018}


def gdc_base_universe_d3_016_gdc_020_gap_magnitude_63_020(gdc_base_universe_d2_016_gdc_020_gap_magnitude_63_020):
    return _base_universe_d3(gdc_base_universe_d2_016_gdc_020_gap_magnitude_63_020, 16)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_016_gdc_020_gap_magnitude_63_020'] = {'inputs': ['gdc_base_universe_d2_016_gdc_020_gap_magnitude_63_020'], 'func': gdc_base_universe_d3_016_gdc_020_gap_magnitude_63_020}


def gdc_base_universe_d3_017_gdc_021_open_close_pressure_84_021(gdc_base_universe_d2_017_gdc_021_open_close_pressure_84_021):
    return _base_universe_d3(gdc_base_universe_d2_017_gdc_021_open_close_pressure_84_021, 17)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_017_gdc_021_open_close_pressure_84_021'] = {'inputs': ['gdc_base_universe_d2_017_gdc_021_open_close_pressure_84_021'], 'func': gdc_base_universe_d3_017_gdc_021_open_close_pressure_84_021}


def gdc_base_universe_d3_018_gdc_022_lower_wick_ratio_126_022(gdc_base_universe_d2_018_gdc_022_lower_wick_ratio_126_022):
    return _base_universe_d3(gdc_base_universe_d2_018_gdc_022_lower_wick_ratio_126_022, 18)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_018_gdc_022_lower_wick_ratio_126_022'] = {'inputs': ['gdc_base_universe_d2_018_gdc_022_lower_wick_ratio_126_022'], 'func': gdc_base_universe_d3_018_gdc_022_lower_wick_ratio_126_022}


def gdc_base_universe_d3_019_gdc_023_upper_wick_ratio_189_023(gdc_base_universe_d2_019_gdc_023_upper_wick_ratio_189_023):
    return _base_universe_d3(gdc_base_universe_d2_019_gdc_023_upper_wick_ratio_189_023, 19)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_019_gdc_023_upper_wick_ratio_189_023'] = {'inputs': ['gdc_base_universe_d2_019_gdc_023_upper_wick_ratio_189_023'], 'func': gdc_base_universe_d3_019_gdc_023_upper_wick_ratio_189_023}


def gdc_base_universe_d3_020_gdc_024_body_to_range_252_024(gdc_base_universe_d2_020_gdc_024_body_to_range_252_024):
    return _base_universe_d3(gdc_base_universe_d2_020_gdc_024_body_to_range_252_024, 20)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_020_gdc_024_body_to_range_252_024'] = {'inputs': ['gdc_base_universe_d2_020_gdc_024_body_to_range_252_024'], 'func': gdc_base_universe_d3_020_gdc_024_body_to_range_252_024}


def gdc_base_universe_d3_021_gdc_026_gap_magnitude_504_026(gdc_base_universe_d2_021_gdc_026_gap_magnitude_504_026):
    return _base_universe_d3(gdc_base_universe_d2_021_gdc_026_gap_magnitude_504_026, 21)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_021_gdc_026_gap_magnitude_504_026'] = {'inputs': ['gdc_base_universe_d2_021_gdc_026_gap_magnitude_504_026'], 'func': gdc_base_universe_d3_021_gdc_026_gap_magnitude_504_026}


def gdc_base_universe_d3_022_gdc_027_open_close_pressure_756_027(gdc_base_universe_d2_022_gdc_027_open_close_pressure_756_027):
    return _base_universe_d3(gdc_base_universe_d2_022_gdc_027_open_close_pressure_756_027, 22)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_022_gdc_027_open_close_pressure_756_027'] = {'inputs': ['gdc_base_universe_d2_022_gdc_027_open_close_pressure_756_027'], 'func': gdc_base_universe_d3_022_gdc_027_open_close_pressure_756_027}


def gdc_base_universe_d3_023_gdc_028_lower_wick_ratio_1008_028(gdc_base_universe_d2_023_gdc_028_lower_wick_ratio_1008_028):
    return _base_universe_d3(gdc_base_universe_d2_023_gdc_028_lower_wick_ratio_1008_028, 23)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_023_gdc_028_lower_wick_ratio_1008_028'] = {'inputs': ['gdc_base_universe_d2_023_gdc_028_lower_wick_ratio_1008_028'], 'func': gdc_base_universe_d3_023_gdc_028_lower_wick_ratio_1008_028}


def gdc_base_universe_d3_024_gdc_029_upper_wick_ratio_1260_029(gdc_base_universe_d2_024_gdc_029_upper_wick_ratio_1260_029):
    return _base_universe_d3(gdc_base_universe_d2_024_gdc_029_upper_wick_ratio_1260_029, 24)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_024_gdc_029_upper_wick_ratio_1260_029'] = {'inputs': ['gdc_base_universe_d2_024_gdc_029_upper_wick_ratio_1260_029'], 'func': gdc_base_universe_d3_024_gdc_029_upper_wick_ratio_1260_029}


def gdc_base_universe_d3_025_gdc_030_body_to_range_1512_030(gdc_base_universe_d2_025_gdc_030_body_to_range_1512_030):
    return _base_universe_d3(gdc_base_universe_d2_025_gdc_030_body_to_range_1512_030, 25)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_025_gdc_030_body_to_range_1512_030'] = {'inputs': ['gdc_base_universe_d2_025_gdc_030_body_to_range_1512_030'], 'func': gdc_base_universe_d3_025_gdc_030_body_to_range_1512_030}


def gdc_base_universe_d3_026_gdc_basefill_031(gdc_base_universe_d2_026_gdc_basefill_031):
    return _base_universe_d3(gdc_base_universe_d2_026_gdc_basefill_031, 26)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_026_gdc_basefill_031'] = {'inputs': ['gdc_base_universe_d2_026_gdc_basefill_031'], 'func': gdc_base_universe_d3_026_gdc_basefill_031}


def gdc_base_universe_d3_027_gdc_basefill_032(gdc_base_universe_d2_027_gdc_basefill_032):
    return _base_universe_d3(gdc_base_universe_d2_027_gdc_basefill_032, 27)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_027_gdc_basefill_032'] = {'inputs': ['gdc_base_universe_d2_027_gdc_basefill_032'], 'func': gdc_base_universe_d3_027_gdc_basefill_032}


def gdc_base_universe_d3_028_gdc_basefill_033(gdc_base_universe_d2_028_gdc_basefill_033):
    return _base_universe_d3(gdc_base_universe_d2_028_gdc_basefill_033, 28)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_028_gdc_basefill_033'] = {'inputs': ['gdc_base_universe_d2_028_gdc_basefill_033'], 'func': gdc_base_universe_d3_028_gdc_basefill_033}


def gdc_base_universe_d3_029_gdc_basefill_034(gdc_base_universe_d2_029_gdc_basefill_034):
    return _base_universe_d3(gdc_base_universe_d2_029_gdc_basefill_034, 29)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_029_gdc_basefill_034'] = {'inputs': ['gdc_base_universe_d2_029_gdc_basefill_034'], 'func': gdc_base_universe_d3_029_gdc_basefill_034}


def gdc_base_universe_d3_030_gdc_basefill_035(gdc_base_universe_d2_030_gdc_basefill_035):
    return _base_universe_d3(gdc_base_universe_d2_030_gdc_basefill_035, 30)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_030_gdc_basefill_035'] = {'inputs': ['gdc_base_universe_d2_030_gdc_basefill_035'], 'func': gdc_base_universe_d3_030_gdc_basefill_035}


def gdc_base_universe_d3_031_gdc_basefill_036(gdc_base_universe_d2_031_gdc_basefill_036):
    return _base_universe_d3(gdc_base_universe_d2_031_gdc_basefill_036, 31)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_031_gdc_basefill_036'] = {'inputs': ['gdc_base_universe_d2_031_gdc_basefill_036'], 'func': gdc_base_universe_d3_031_gdc_basefill_036}


def gdc_base_universe_d3_032_gdc_basefill_037(gdc_base_universe_d2_032_gdc_basefill_037):
    return _base_universe_d3(gdc_base_universe_d2_032_gdc_basefill_037, 32)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_032_gdc_basefill_037'] = {'inputs': ['gdc_base_universe_d2_032_gdc_basefill_037'], 'func': gdc_base_universe_d3_032_gdc_basefill_037}


def gdc_base_universe_d3_033_gdc_basefill_038(gdc_base_universe_d2_033_gdc_basefill_038):
    return _base_universe_d3(gdc_base_universe_d2_033_gdc_basefill_038, 33)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_033_gdc_basefill_038'] = {'inputs': ['gdc_base_universe_d2_033_gdc_basefill_038'], 'func': gdc_base_universe_d3_033_gdc_basefill_038}


def gdc_base_universe_d3_034_gdc_basefill_039(gdc_base_universe_d2_034_gdc_basefill_039):
    return _base_universe_d3(gdc_base_universe_d2_034_gdc_basefill_039, 34)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_034_gdc_basefill_039'] = {'inputs': ['gdc_base_universe_d2_034_gdc_basefill_039'], 'func': gdc_base_universe_d3_034_gdc_basefill_039}


def gdc_base_universe_d3_035_gdc_basefill_040(gdc_base_universe_d2_035_gdc_basefill_040):
    return _base_universe_d3(gdc_base_universe_d2_035_gdc_basefill_040, 35)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_035_gdc_basefill_040'] = {'inputs': ['gdc_base_universe_d2_035_gdc_basefill_040'], 'func': gdc_base_universe_d3_035_gdc_basefill_040}


def gdc_base_universe_d3_036_gdc_basefill_041(gdc_base_universe_d2_036_gdc_basefill_041):
    return _base_universe_d3(gdc_base_universe_d2_036_gdc_basefill_041, 36)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_036_gdc_basefill_041'] = {'inputs': ['gdc_base_universe_d2_036_gdc_basefill_041'], 'func': gdc_base_universe_d3_036_gdc_basefill_041}


def gdc_base_universe_d3_037_gdc_basefill_042(gdc_base_universe_d2_037_gdc_basefill_042):
    return _base_universe_d3(gdc_base_universe_d2_037_gdc_basefill_042, 37)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_037_gdc_basefill_042'] = {'inputs': ['gdc_base_universe_d2_037_gdc_basefill_042'], 'func': gdc_base_universe_d3_037_gdc_basefill_042}


def gdc_base_universe_d3_038_gdc_basefill_043(gdc_base_universe_d2_038_gdc_basefill_043):
    return _base_universe_d3(gdc_base_universe_d2_038_gdc_basefill_043, 38)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_038_gdc_basefill_043'] = {'inputs': ['gdc_base_universe_d2_038_gdc_basefill_043'], 'func': gdc_base_universe_d3_038_gdc_basefill_043}


def gdc_base_universe_d3_039_gdc_basefill_044(gdc_base_universe_d2_039_gdc_basefill_044):
    return _base_universe_d3(gdc_base_universe_d2_039_gdc_basefill_044, 39)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_039_gdc_basefill_044'] = {'inputs': ['gdc_base_universe_d2_039_gdc_basefill_044'], 'func': gdc_base_universe_d3_039_gdc_basefill_044}


def gdc_base_universe_d3_040_gdc_basefill_045(gdc_base_universe_d2_040_gdc_basefill_045):
    return _base_universe_d3(gdc_base_universe_d2_040_gdc_basefill_045, 40)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_040_gdc_basefill_045'] = {'inputs': ['gdc_base_universe_d2_040_gdc_basefill_045'], 'func': gdc_base_universe_d3_040_gdc_basefill_045}


def gdc_base_universe_d3_041_gdc_basefill_046(gdc_base_universe_d2_041_gdc_basefill_046):
    return _base_universe_d3(gdc_base_universe_d2_041_gdc_basefill_046, 41)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_041_gdc_basefill_046'] = {'inputs': ['gdc_base_universe_d2_041_gdc_basefill_046'], 'func': gdc_base_universe_d3_041_gdc_basefill_046}


def gdc_base_universe_d3_042_gdc_basefill_047(gdc_base_universe_d2_042_gdc_basefill_047):
    return _base_universe_d3(gdc_base_universe_d2_042_gdc_basefill_047, 42)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_042_gdc_basefill_047'] = {'inputs': ['gdc_base_universe_d2_042_gdc_basefill_047'], 'func': gdc_base_universe_d3_042_gdc_basefill_047}


def gdc_base_universe_d3_043_gdc_basefill_048(gdc_base_universe_d2_043_gdc_basefill_048):
    return _base_universe_d3(gdc_base_universe_d2_043_gdc_basefill_048, 43)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_043_gdc_basefill_048'] = {'inputs': ['gdc_base_universe_d2_043_gdc_basefill_048'], 'func': gdc_base_universe_d3_043_gdc_basefill_048}


def gdc_base_universe_d3_044_gdc_basefill_049(gdc_base_universe_d2_044_gdc_basefill_049):
    return _base_universe_d3(gdc_base_universe_d2_044_gdc_basefill_049, 44)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_044_gdc_basefill_049'] = {'inputs': ['gdc_base_universe_d2_044_gdc_basefill_049'], 'func': gdc_base_universe_d3_044_gdc_basefill_049}


def gdc_base_universe_d3_045_gdc_basefill_050(gdc_base_universe_d2_045_gdc_basefill_050):
    return _base_universe_d3(gdc_base_universe_d2_045_gdc_basefill_050, 45)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_045_gdc_basefill_050'] = {'inputs': ['gdc_base_universe_d2_045_gdc_basefill_050'], 'func': gdc_base_universe_d3_045_gdc_basefill_050}


def gdc_base_universe_d3_046_gdc_basefill_051(gdc_base_universe_d2_046_gdc_basefill_051):
    return _base_universe_d3(gdc_base_universe_d2_046_gdc_basefill_051, 46)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_046_gdc_basefill_051'] = {'inputs': ['gdc_base_universe_d2_046_gdc_basefill_051'], 'func': gdc_base_universe_d3_046_gdc_basefill_051}


def gdc_base_universe_d3_047_gdc_basefill_052(gdc_base_universe_d2_047_gdc_basefill_052):
    return _base_universe_d3(gdc_base_universe_d2_047_gdc_basefill_052, 47)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_047_gdc_basefill_052'] = {'inputs': ['gdc_base_universe_d2_047_gdc_basefill_052'], 'func': gdc_base_universe_d3_047_gdc_basefill_052}


def gdc_base_universe_d3_048_gdc_basefill_053(gdc_base_universe_d2_048_gdc_basefill_053):
    return _base_universe_d3(gdc_base_universe_d2_048_gdc_basefill_053, 48)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_048_gdc_basefill_053'] = {'inputs': ['gdc_base_universe_d2_048_gdc_basefill_053'], 'func': gdc_base_universe_d3_048_gdc_basefill_053}


def gdc_base_universe_d3_049_gdc_basefill_054(gdc_base_universe_d2_049_gdc_basefill_054):
    return _base_universe_d3(gdc_base_universe_d2_049_gdc_basefill_054, 49)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_049_gdc_basefill_054'] = {'inputs': ['gdc_base_universe_d2_049_gdc_basefill_054'], 'func': gdc_base_universe_d3_049_gdc_basefill_054}


def gdc_base_universe_d3_050_gdc_basefill_055(gdc_base_universe_d2_050_gdc_basefill_055):
    return _base_universe_d3(gdc_base_universe_d2_050_gdc_basefill_055, 50)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_050_gdc_basefill_055'] = {'inputs': ['gdc_base_universe_d2_050_gdc_basefill_055'], 'func': gdc_base_universe_d3_050_gdc_basefill_055}


def gdc_base_universe_d3_051_gdc_basefill_056(gdc_base_universe_d2_051_gdc_basefill_056):
    return _base_universe_d3(gdc_base_universe_d2_051_gdc_basefill_056, 51)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_051_gdc_basefill_056'] = {'inputs': ['gdc_base_universe_d2_051_gdc_basefill_056'], 'func': gdc_base_universe_d3_051_gdc_basefill_056}


def gdc_base_universe_d3_052_gdc_basefill_057(gdc_base_universe_d2_052_gdc_basefill_057):
    return _base_universe_d3(gdc_base_universe_d2_052_gdc_basefill_057, 52)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_052_gdc_basefill_057'] = {'inputs': ['gdc_base_universe_d2_052_gdc_basefill_057'], 'func': gdc_base_universe_d3_052_gdc_basefill_057}


def gdc_base_universe_d3_053_gdc_basefill_058(gdc_base_universe_d2_053_gdc_basefill_058):
    return _base_universe_d3(gdc_base_universe_d2_053_gdc_basefill_058, 53)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_053_gdc_basefill_058'] = {'inputs': ['gdc_base_universe_d2_053_gdc_basefill_058'], 'func': gdc_base_universe_d3_053_gdc_basefill_058}


def gdc_base_universe_d3_054_gdc_basefill_059(gdc_base_universe_d2_054_gdc_basefill_059):
    return _base_universe_d3(gdc_base_universe_d2_054_gdc_basefill_059, 54)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_054_gdc_basefill_059'] = {'inputs': ['gdc_base_universe_d2_054_gdc_basefill_059'], 'func': gdc_base_universe_d3_054_gdc_basefill_059}


def gdc_base_universe_d3_055_gdc_basefill_060(gdc_base_universe_d2_055_gdc_basefill_060):
    return _base_universe_d3(gdc_base_universe_d2_055_gdc_basefill_060, 55)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_055_gdc_basefill_060'] = {'inputs': ['gdc_base_universe_d2_055_gdc_basefill_060'], 'func': gdc_base_universe_d3_055_gdc_basefill_060}


def gdc_base_universe_d3_056_gdc_basefill_061(gdc_base_universe_d2_056_gdc_basefill_061):
    return _base_universe_d3(gdc_base_universe_d2_056_gdc_basefill_061, 56)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_056_gdc_basefill_061'] = {'inputs': ['gdc_base_universe_d2_056_gdc_basefill_061'], 'func': gdc_base_universe_d3_056_gdc_basefill_061}


def gdc_base_universe_d3_057_gdc_basefill_062(gdc_base_universe_d2_057_gdc_basefill_062):
    return _base_universe_d3(gdc_base_universe_d2_057_gdc_basefill_062, 57)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_057_gdc_basefill_062'] = {'inputs': ['gdc_base_universe_d2_057_gdc_basefill_062'], 'func': gdc_base_universe_d3_057_gdc_basefill_062}


def gdc_base_universe_d3_058_gdc_basefill_063(gdc_base_universe_d2_058_gdc_basefill_063):
    return _base_universe_d3(gdc_base_universe_d2_058_gdc_basefill_063, 58)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_058_gdc_basefill_063'] = {'inputs': ['gdc_base_universe_d2_058_gdc_basefill_063'], 'func': gdc_base_universe_d3_058_gdc_basefill_063}


def gdc_base_universe_d3_059_gdc_basefill_064(gdc_base_universe_d2_059_gdc_basefill_064):
    return _base_universe_d3(gdc_base_universe_d2_059_gdc_basefill_064, 59)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_059_gdc_basefill_064'] = {'inputs': ['gdc_base_universe_d2_059_gdc_basefill_064'], 'func': gdc_base_universe_d3_059_gdc_basefill_064}


def gdc_base_universe_d3_060_gdc_basefill_065(gdc_base_universe_d2_060_gdc_basefill_065):
    return _base_universe_d3(gdc_base_universe_d2_060_gdc_basefill_065, 60)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_060_gdc_basefill_065'] = {'inputs': ['gdc_base_universe_d2_060_gdc_basefill_065'], 'func': gdc_base_universe_d3_060_gdc_basefill_065}


def gdc_base_universe_d3_061_gdc_basefill_066(gdc_base_universe_d2_061_gdc_basefill_066):
    return _base_universe_d3(gdc_base_universe_d2_061_gdc_basefill_066, 61)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_061_gdc_basefill_066'] = {'inputs': ['gdc_base_universe_d2_061_gdc_basefill_066'], 'func': gdc_base_universe_d3_061_gdc_basefill_066}


def gdc_base_universe_d3_062_gdc_basefill_067(gdc_base_universe_d2_062_gdc_basefill_067):
    return _base_universe_d3(gdc_base_universe_d2_062_gdc_basefill_067, 62)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_062_gdc_basefill_067'] = {'inputs': ['gdc_base_universe_d2_062_gdc_basefill_067'], 'func': gdc_base_universe_d3_062_gdc_basefill_067}


def gdc_base_universe_d3_063_gdc_basefill_068(gdc_base_universe_d2_063_gdc_basefill_068):
    return _base_universe_d3(gdc_base_universe_d2_063_gdc_basefill_068, 63)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_063_gdc_basefill_068'] = {'inputs': ['gdc_base_universe_d2_063_gdc_basefill_068'], 'func': gdc_base_universe_d3_063_gdc_basefill_068}


def gdc_base_universe_d3_064_gdc_basefill_069(gdc_base_universe_d2_064_gdc_basefill_069):
    return _base_universe_d3(gdc_base_universe_d2_064_gdc_basefill_069, 64)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_064_gdc_basefill_069'] = {'inputs': ['gdc_base_universe_d2_064_gdc_basefill_069'], 'func': gdc_base_universe_d3_064_gdc_basefill_069}


def gdc_base_universe_d3_065_gdc_basefill_070(gdc_base_universe_d2_065_gdc_basefill_070):
    return _base_universe_d3(gdc_base_universe_d2_065_gdc_basefill_070, 65)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_065_gdc_basefill_070'] = {'inputs': ['gdc_base_universe_d2_065_gdc_basefill_070'], 'func': gdc_base_universe_d3_065_gdc_basefill_070}


def gdc_base_universe_d3_066_gdc_basefill_071(gdc_base_universe_d2_066_gdc_basefill_071):
    return _base_universe_d3(gdc_base_universe_d2_066_gdc_basefill_071, 66)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_066_gdc_basefill_071'] = {'inputs': ['gdc_base_universe_d2_066_gdc_basefill_071'], 'func': gdc_base_universe_d3_066_gdc_basefill_071}


def gdc_base_universe_d3_067_gdc_basefill_072(gdc_base_universe_d2_067_gdc_basefill_072):
    return _base_universe_d3(gdc_base_universe_d2_067_gdc_basefill_072, 67)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_067_gdc_basefill_072'] = {'inputs': ['gdc_base_universe_d2_067_gdc_basefill_072'], 'func': gdc_base_universe_d3_067_gdc_basefill_072}


def gdc_base_universe_d3_068_gdc_basefill_073(gdc_base_universe_d2_068_gdc_basefill_073):
    return _base_universe_d3(gdc_base_universe_d2_068_gdc_basefill_073, 68)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_068_gdc_basefill_073'] = {'inputs': ['gdc_base_universe_d2_068_gdc_basefill_073'], 'func': gdc_base_universe_d3_068_gdc_basefill_073}


def gdc_base_universe_d3_069_gdc_basefill_074(gdc_base_universe_d2_069_gdc_basefill_074):
    return _base_universe_d3(gdc_base_universe_d2_069_gdc_basefill_074, 69)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_069_gdc_basefill_074'] = {'inputs': ['gdc_base_universe_d2_069_gdc_basefill_074'], 'func': gdc_base_universe_d3_069_gdc_basefill_074}


def gdc_base_universe_d3_070_gdc_basefill_075(gdc_base_universe_d2_070_gdc_basefill_075):
    return _base_universe_d3(gdc_base_universe_d2_070_gdc_basefill_075, 70)
GDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gdc_base_universe_d3_070_gdc_basefill_075'] = {'inputs': ['gdc_base_universe_d2_070_gdc_basefill_075'], 'func': gdc_base_universe_d3_070_gdc_basefill_075}
