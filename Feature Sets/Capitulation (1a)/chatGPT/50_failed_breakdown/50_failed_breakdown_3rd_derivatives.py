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



def fbd_176_fbd_001_gap_down_frequency_5_001_accel_1(fbd_151_fbd_001_gap_down_frequency_5_001_roc_1):
    feature = _s(fbd_151_fbd_001_gap_down_frequency_5_001_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def fbd_177_fbd_007_gap_down_frequency_126_007_accel_5(fbd_152_fbd_007_gap_down_frequency_126_007_roc_5):
    feature = _s(fbd_152_fbd_007_gap_down_frequency_126_007_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def fbd_178_fbd_013_gap_down_frequency_1008_013_accel_42(fbd_153_fbd_013_gap_down_frequency_1008_013_roc_42):
    feature = _s(fbd_153_fbd_013_gap_down_frequency_1008_013_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def fbd_179_fbd_019_gap_down_frequency_42_019_accel_126(fbd_154_fbd_019_gap_down_frequency_42_019_roc_126):
    feature = _s(fbd_154_fbd_019_gap_down_frequency_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def fbd_180_fbd_025_gap_down_frequency_378_025_accel_378(fbd_155_fbd_025_gap_down_frequency_378_025_roc_378):
    feature = _s(fbd_155_fbd_025_gap_down_frequency_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















FAILED_BREAKDOWN_REGISTRY_3RD_DERIVATIVES = {
    'fbd_176_fbd_001_gap_down_frequency_5_001_accel_1': {'inputs': ['fbd_151_fbd_001_gap_down_frequency_5_001_roc_1'], 'func': fbd_176_fbd_001_gap_down_frequency_5_001_accel_1},
    'fbd_177_fbd_007_gap_down_frequency_126_007_accel_5': {'inputs': ['fbd_152_fbd_007_gap_down_frequency_126_007_roc_5'], 'func': fbd_177_fbd_007_gap_down_frequency_126_007_accel_5},
    'fbd_178_fbd_013_gap_down_frequency_1008_013_accel_42': {'inputs': ['fbd_153_fbd_013_gap_down_frequency_1008_013_roc_42'], 'func': fbd_178_fbd_013_gap_down_frequency_1008_013_accel_42},
    'fbd_179_fbd_019_gap_down_frequency_42_019_accel_126': {'inputs': ['fbd_154_fbd_019_gap_down_frequency_42_019_roc_126'], 'func': fbd_179_fbd_019_gap_down_frequency_42_019_accel_126},
    'fbd_180_fbd_025_gap_down_frequency_378_025_accel_378': {'inputs': ['fbd_155_fbd_025_gap_down_frequency_378_025_roc_378'], 'func': fbd_180_fbd_025_gap_down_frequency_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def fb_replacement_d3_001(fb_replacement_d2_001):
    feature = _clean(fb_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_001'] = {'inputs': ['fb_replacement_d2_001'], 'func': fb_replacement_d3_001}


def fb_replacement_d3_002(fb_replacement_d2_002):
    feature = _clean(fb_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_002'] = {'inputs': ['fb_replacement_d2_002'], 'func': fb_replacement_d3_002}


def fb_replacement_d3_003(fb_replacement_d2_003):
    feature = _clean(fb_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_003'] = {'inputs': ['fb_replacement_d2_003'], 'func': fb_replacement_d3_003}


def fb_replacement_d3_004(fb_replacement_d2_004):
    feature = _clean(fb_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_004'] = {'inputs': ['fb_replacement_d2_004'], 'func': fb_replacement_d3_004}


def fb_replacement_d3_005(fb_replacement_d2_005):
    feature = _clean(fb_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_005'] = {'inputs': ['fb_replacement_d2_005'], 'func': fb_replacement_d3_005}


def fb_replacement_d3_006(fb_replacement_d2_006):
    feature = _clean(fb_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_006'] = {'inputs': ['fb_replacement_d2_006'], 'func': fb_replacement_d3_006}


def fb_replacement_d3_007(fb_replacement_d2_007):
    feature = _clean(fb_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_007'] = {'inputs': ['fb_replacement_d2_007'], 'func': fb_replacement_d3_007}


def fb_replacement_d3_008(fb_replacement_d2_008):
    feature = _clean(fb_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_008'] = {'inputs': ['fb_replacement_d2_008'], 'func': fb_replacement_d3_008}


def fb_replacement_d3_009(fb_replacement_d2_009):
    feature = _clean(fb_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_009'] = {'inputs': ['fb_replacement_d2_009'], 'func': fb_replacement_d3_009}


def fb_replacement_d3_010(fb_replacement_d2_010):
    feature = _clean(fb_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_010'] = {'inputs': ['fb_replacement_d2_010'], 'func': fb_replacement_d3_010}


def fb_replacement_d3_011(fb_replacement_d2_011):
    feature = _clean(fb_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_011'] = {'inputs': ['fb_replacement_d2_011'], 'func': fb_replacement_d3_011}


def fb_replacement_d3_012(fb_replacement_d2_012):
    feature = _clean(fb_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_012'] = {'inputs': ['fb_replacement_d2_012'], 'func': fb_replacement_d3_012}


def fb_replacement_d3_013(fb_replacement_d2_013):
    feature = _clean(fb_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_013'] = {'inputs': ['fb_replacement_d2_013'], 'func': fb_replacement_d3_013}


def fb_replacement_d3_014(fb_replacement_d2_014):
    feature = _clean(fb_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_014'] = {'inputs': ['fb_replacement_d2_014'], 'func': fb_replacement_d3_014}


def fb_replacement_d3_015(fb_replacement_d2_015):
    feature = _clean(fb_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_015'] = {'inputs': ['fb_replacement_d2_015'], 'func': fb_replacement_d3_015}


def fb_replacement_d3_016(fb_replacement_d2_016):
    feature = _clean(fb_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_016'] = {'inputs': ['fb_replacement_d2_016'], 'func': fb_replacement_d3_016}


def fb_replacement_d3_017(fb_replacement_d2_017):
    feature = _clean(fb_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_017'] = {'inputs': ['fb_replacement_d2_017'], 'func': fb_replacement_d3_017}


def fb_replacement_d3_018(fb_replacement_d2_018):
    feature = _clean(fb_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_018'] = {'inputs': ['fb_replacement_d2_018'], 'func': fb_replacement_d3_018}


def fb_replacement_d3_019(fb_replacement_d2_019):
    feature = _clean(fb_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_019'] = {'inputs': ['fb_replacement_d2_019'], 'func': fb_replacement_d3_019}


def fb_replacement_d3_020(fb_replacement_d2_020):
    feature = _clean(fb_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_020'] = {'inputs': ['fb_replacement_d2_020'], 'func': fb_replacement_d3_020}


def fb_replacement_d3_021(fb_replacement_d2_021):
    feature = _clean(fb_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_021'] = {'inputs': ['fb_replacement_d2_021'], 'func': fb_replacement_d3_021}


def fb_replacement_d3_022(fb_replacement_d2_022):
    feature = _clean(fb_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_022'] = {'inputs': ['fb_replacement_d2_022'], 'func': fb_replacement_d3_022}


def fb_replacement_d3_023(fb_replacement_d2_023):
    feature = _clean(fb_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_023'] = {'inputs': ['fb_replacement_d2_023'], 'func': fb_replacement_d3_023}


def fb_replacement_d3_024(fb_replacement_d2_024):
    feature = _clean(fb_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_024'] = {'inputs': ['fb_replacement_d2_024'], 'func': fb_replacement_d3_024}


def fb_replacement_d3_025(fb_replacement_d2_025):
    feature = _clean(fb_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_025'] = {'inputs': ['fb_replacement_d2_025'], 'func': fb_replacement_d3_025}


def fb_replacement_d3_026(fb_replacement_d2_026):
    feature = _clean(fb_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_026'] = {'inputs': ['fb_replacement_d2_026'], 'func': fb_replacement_d3_026}


def fb_replacement_d3_027(fb_replacement_d2_027):
    feature = _clean(fb_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_027'] = {'inputs': ['fb_replacement_d2_027'], 'func': fb_replacement_d3_027}


def fb_replacement_d3_028(fb_replacement_d2_028):
    feature = _clean(fb_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_028'] = {'inputs': ['fb_replacement_d2_028'], 'func': fb_replacement_d3_028}


def fb_replacement_d3_029(fb_replacement_d2_029):
    feature = _clean(fb_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_029'] = {'inputs': ['fb_replacement_d2_029'], 'func': fb_replacement_d3_029}


def fb_replacement_d3_030(fb_replacement_d2_030):
    feature = _clean(fb_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_030'] = {'inputs': ['fb_replacement_d2_030'], 'func': fb_replacement_d3_030}


def fb_replacement_d3_031(fb_replacement_d2_031):
    feature = _clean(fb_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_031'] = {'inputs': ['fb_replacement_d2_031'], 'func': fb_replacement_d3_031}


def fb_replacement_d3_032(fb_replacement_d2_032):
    feature = _clean(fb_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_032'] = {'inputs': ['fb_replacement_d2_032'], 'func': fb_replacement_d3_032}


def fb_replacement_d3_033(fb_replacement_d2_033):
    feature = _clean(fb_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_033'] = {'inputs': ['fb_replacement_d2_033'], 'func': fb_replacement_d3_033}


def fb_replacement_d3_034(fb_replacement_d2_034):
    feature = _clean(fb_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_034'] = {'inputs': ['fb_replacement_d2_034'], 'func': fb_replacement_d3_034}


def fb_replacement_d3_035(fb_replacement_d2_035):
    feature = _clean(fb_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_035'] = {'inputs': ['fb_replacement_d2_035'], 'func': fb_replacement_d3_035}


def fb_replacement_d3_036(fb_replacement_d2_036):
    feature = _clean(fb_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_036'] = {'inputs': ['fb_replacement_d2_036'], 'func': fb_replacement_d3_036}


def fb_replacement_d3_037(fb_replacement_d2_037):
    feature = _clean(fb_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_037'] = {'inputs': ['fb_replacement_d2_037'], 'func': fb_replacement_d3_037}


def fb_replacement_d3_038(fb_replacement_d2_038):
    feature = _clean(fb_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_038'] = {'inputs': ['fb_replacement_d2_038'], 'func': fb_replacement_d3_038}


def fb_replacement_d3_039(fb_replacement_d2_039):
    feature = _clean(fb_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_039'] = {'inputs': ['fb_replacement_d2_039'], 'func': fb_replacement_d3_039}


def fb_replacement_d3_040(fb_replacement_d2_040):
    feature = _clean(fb_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_040'] = {'inputs': ['fb_replacement_d2_040'], 'func': fb_replacement_d3_040}


def fb_replacement_d3_041(fb_replacement_d2_041):
    feature = _clean(fb_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_041'] = {'inputs': ['fb_replacement_d2_041'], 'func': fb_replacement_d3_041}


def fb_replacement_d3_042(fb_replacement_d2_042):
    feature = _clean(fb_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_042'] = {'inputs': ['fb_replacement_d2_042'], 'func': fb_replacement_d3_042}


def fb_replacement_d3_043(fb_replacement_d2_043):
    feature = _clean(fb_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_043'] = {'inputs': ['fb_replacement_d2_043'], 'func': fb_replacement_d3_043}


def fb_replacement_d3_044(fb_replacement_d2_044):
    feature = _clean(fb_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_044'] = {'inputs': ['fb_replacement_d2_044'], 'func': fb_replacement_d3_044}


def fb_replacement_d3_045(fb_replacement_d2_045):
    feature = _clean(fb_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_045'] = {'inputs': ['fb_replacement_d2_045'], 'func': fb_replacement_d3_045}


def fb_replacement_d3_046(fb_replacement_d2_046):
    feature = _clean(fb_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_046'] = {'inputs': ['fb_replacement_d2_046'], 'func': fb_replacement_d3_046}


def fb_replacement_d3_047(fb_replacement_d2_047):
    feature = _clean(fb_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_047'] = {'inputs': ['fb_replacement_d2_047'], 'func': fb_replacement_d3_047}


def fb_replacement_d3_048(fb_replacement_d2_048):
    feature = _clean(fb_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_048'] = {'inputs': ['fb_replacement_d2_048'], 'func': fb_replacement_d3_048}


def fb_replacement_d3_049(fb_replacement_d2_049):
    feature = _clean(fb_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_049'] = {'inputs': ['fb_replacement_d2_049'], 'func': fb_replacement_d3_049}


def fb_replacement_d3_050(fb_replacement_d2_050):
    feature = _clean(fb_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_050'] = {'inputs': ['fb_replacement_d2_050'], 'func': fb_replacement_d3_050}


def fb_replacement_d3_051(fb_replacement_d2_051):
    feature = _clean(fb_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_051'] = {'inputs': ['fb_replacement_d2_051'], 'func': fb_replacement_d3_051}


def fb_replacement_d3_052(fb_replacement_d2_052):
    feature = _clean(fb_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_052'] = {'inputs': ['fb_replacement_d2_052'], 'func': fb_replacement_d3_052}


def fb_replacement_d3_053(fb_replacement_d2_053):
    feature = _clean(fb_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_053'] = {'inputs': ['fb_replacement_d2_053'], 'func': fb_replacement_d3_053}


def fb_replacement_d3_054(fb_replacement_d2_054):
    feature = _clean(fb_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_054'] = {'inputs': ['fb_replacement_d2_054'], 'func': fb_replacement_d3_054}


def fb_replacement_d3_055(fb_replacement_d2_055):
    feature = _clean(fb_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_055'] = {'inputs': ['fb_replacement_d2_055'], 'func': fb_replacement_d3_055}


def fb_replacement_d3_056(fb_replacement_d2_056):
    feature = _clean(fb_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_056'] = {'inputs': ['fb_replacement_d2_056'], 'func': fb_replacement_d3_056}


def fb_replacement_d3_057(fb_replacement_d2_057):
    feature = _clean(fb_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_057'] = {'inputs': ['fb_replacement_d2_057'], 'func': fb_replacement_d3_057}


def fb_replacement_d3_058(fb_replacement_d2_058):
    feature = _clean(fb_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_058'] = {'inputs': ['fb_replacement_d2_058'], 'func': fb_replacement_d3_058}


def fb_replacement_d3_059(fb_replacement_d2_059):
    feature = _clean(fb_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_059'] = {'inputs': ['fb_replacement_d2_059'], 'func': fb_replacement_d3_059}


def fb_replacement_d3_060(fb_replacement_d2_060):
    feature = _clean(fb_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_060'] = {'inputs': ['fb_replacement_d2_060'], 'func': fb_replacement_d3_060}


def fb_replacement_d3_061(fb_replacement_d2_061):
    feature = _clean(fb_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_061'] = {'inputs': ['fb_replacement_d2_061'], 'func': fb_replacement_d3_061}


def fb_replacement_d3_062(fb_replacement_d2_062):
    feature = _clean(fb_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_062'] = {'inputs': ['fb_replacement_d2_062'], 'func': fb_replacement_d3_062}


def fb_replacement_d3_063(fb_replacement_d2_063):
    feature = _clean(fb_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_063'] = {'inputs': ['fb_replacement_d2_063'], 'func': fb_replacement_d3_063}


def fb_replacement_d3_064(fb_replacement_d2_064):
    feature = _clean(fb_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_064'] = {'inputs': ['fb_replacement_d2_064'], 'func': fb_replacement_d3_064}


def fb_replacement_d3_065(fb_replacement_d2_065):
    feature = _clean(fb_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_065'] = {'inputs': ['fb_replacement_d2_065'], 'func': fb_replacement_d3_065}


def fb_replacement_d3_066(fb_replacement_d2_066):
    feature = _clean(fb_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_066'] = {'inputs': ['fb_replacement_d2_066'], 'func': fb_replacement_d3_066}


def fb_replacement_d3_067(fb_replacement_d2_067):
    feature = _clean(fb_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_067'] = {'inputs': ['fb_replacement_d2_067'], 'func': fb_replacement_d3_067}


def fb_replacement_d3_068(fb_replacement_d2_068):
    feature = _clean(fb_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_068'] = {'inputs': ['fb_replacement_d2_068'], 'func': fb_replacement_d3_068}


def fb_replacement_d3_069(fb_replacement_d2_069):
    feature = _clean(fb_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_069'] = {'inputs': ['fb_replacement_d2_069'], 'func': fb_replacement_d3_069}


def fb_replacement_d3_070(fb_replacement_d2_070):
    feature = _clean(fb_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_070'] = {'inputs': ['fb_replacement_d2_070'], 'func': fb_replacement_d3_070}


def fb_replacement_d3_071(fb_replacement_d2_071):
    feature = _clean(fb_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_071'] = {'inputs': ['fb_replacement_d2_071'], 'func': fb_replacement_d3_071}


def fb_replacement_d3_072(fb_replacement_d2_072):
    feature = _clean(fb_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_072'] = {'inputs': ['fb_replacement_d2_072'], 'func': fb_replacement_d3_072}


def fb_replacement_d3_073(fb_replacement_d2_073):
    feature = _clean(fb_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_073'] = {'inputs': ['fb_replacement_d2_073'], 'func': fb_replacement_d3_073}


def fb_replacement_d3_074(fb_replacement_d2_074):
    feature = _clean(fb_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_074'] = {'inputs': ['fb_replacement_d2_074'], 'func': fb_replacement_d3_074}


def fb_replacement_d3_075(fb_replacement_d2_075):
    feature = _clean(fb_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_075'] = {'inputs': ['fb_replacement_d2_075'], 'func': fb_replacement_d3_075}


def fb_replacement_d3_076(fb_replacement_d2_076):
    feature = _clean(fb_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_076'] = {'inputs': ['fb_replacement_d2_076'], 'func': fb_replacement_d3_076}


def fb_replacement_d3_077(fb_replacement_d2_077):
    feature = _clean(fb_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_077'] = {'inputs': ['fb_replacement_d2_077'], 'func': fb_replacement_d3_077}


def fb_replacement_d3_078(fb_replacement_d2_078):
    feature = _clean(fb_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_078'] = {'inputs': ['fb_replacement_d2_078'], 'func': fb_replacement_d3_078}


def fb_replacement_d3_079(fb_replacement_d2_079):
    feature = _clean(fb_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_079'] = {'inputs': ['fb_replacement_d2_079'], 'func': fb_replacement_d3_079}


def fb_replacement_d3_080(fb_replacement_d2_080):
    feature = _clean(fb_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_080'] = {'inputs': ['fb_replacement_d2_080'], 'func': fb_replacement_d3_080}


def fb_replacement_d3_081(fb_replacement_d2_081):
    feature = _clean(fb_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_081'] = {'inputs': ['fb_replacement_d2_081'], 'func': fb_replacement_d3_081}


def fb_replacement_d3_082(fb_replacement_d2_082):
    feature = _clean(fb_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_082'] = {'inputs': ['fb_replacement_d2_082'], 'func': fb_replacement_d3_082}


def fb_replacement_d3_083(fb_replacement_d2_083):
    feature = _clean(fb_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_083'] = {'inputs': ['fb_replacement_d2_083'], 'func': fb_replacement_d3_083}


def fb_replacement_d3_084(fb_replacement_d2_084):
    feature = _clean(fb_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_084'] = {'inputs': ['fb_replacement_d2_084'], 'func': fb_replacement_d3_084}


def fb_replacement_d3_085(fb_replacement_d2_085):
    feature = _clean(fb_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_085'] = {'inputs': ['fb_replacement_d2_085'], 'func': fb_replacement_d3_085}


def fb_replacement_d3_086(fb_replacement_d2_086):
    feature = _clean(fb_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_086'] = {'inputs': ['fb_replacement_d2_086'], 'func': fb_replacement_d3_086}


def fb_replacement_d3_087(fb_replacement_d2_087):
    feature = _clean(fb_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_087'] = {'inputs': ['fb_replacement_d2_087'], 'func': fb_replacement_d3_087}


def fb_replacement_d3_088(fb_replacement_d2_088):
    feature = _clean(fb_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_088'] = {'inputs': ['fb_replacement_d2_088'], 'func': fb_replacement_d3_088}


def fb_replacement_d3_089(fb_replacement_d2_089):
    feature = _clean(fb_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_089'] = {'inputs': ['fb_replacement_d2_089'], 'func': fb_replacement_d3_089}


def fb_replacement_d3_090(fb_replacement_d2_090):
    feature = _clean(fb_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_090'] = {'inputs': ['fb_replacement_d2_090'], 'func': fb_replacement_d3_090}


def fb_replacement_d3_091(fb_replacement_d2_091):
    feature = _clean(fb_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_091'] = {'inputs': ['fb_replacement_d2_091'], 'func': fb_replacement_d3_091}


def fb_replacement_d3_092(fb_replacement_d2_092):
    feature = _clean(fb_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_092'] = {'inputs': ['fb_replacement_d2_092'], 'func': fb_replacement_d3_092}


def fb_replacement_d3_093(fb_replacement_d2_093):
    feature = _clean(fb_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_093'] = {'inputs': ['fb_replacement_d2_093'], 'func': fb_replacement_d3_093}


def fb_replacement_d3_094(fb_replacement_d2_094):
    feature = _clean(fb_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_094'] = {'inputs': ['fb_replacement_d2_094'], 'func': fb_replacement_d3_094}


def fb_replacement_d3_095(fb_replacement_d2_095):
    feature = _clean(fb_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_095'] = {'inputs': ['fb_replacement_d2_095'], 'func': fb_replacement_d3_095}


def fb_replacement_d3_096(fb_replacement_d2_096):
    feature = _clean(fb_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_096'] = {'inputs': ['fb_replacement_d2_096'], 'func': fb_replacement_d3_096}


def fb_replacement_d3_097(fb_replacement_d2_097):
    feature = _clean(fb_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_097'] = {'inputs': ['fb_replacement_d2_097'], 'func': fb_replacement_d3_097}


def fb_replacement_d3_098(fb_replacement_d2_098):
    feature = _clean(fb_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_098'] = {'inputs': ['fb_replacement_d2_098'], 'func': fb_replacement_d3_098}


def fb_replacement_d3_099(fb_replacement_d2_099):
    feature = _clean(fb_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_099'] = {'inputs': ['fb_replacement_d2_099'], 'func': fb_replacement_d3_099}


def fb_replacement_d3_100(fb_replacement_d2_100):
    feature = _clean(fb_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_100'] = {'inputs': ['fb_replacement_d2_100'], 'func': fb_replacement_d3_100}


def fb_replacement_d3_101(fb_replacement_d2_101):
    feature = _clean(fb_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_101'] = {'inputs': ['fb_replacement_d2_101'], 'func': fb_replacement_d3_101}


def fb_replacement_d3_102(fb_replacement_d2_102):
    feature = _clean(fb_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_102'] = {'inputs': ['fb_replacement_d2_102'], 'func': fb_replacement_d3_102}


def fb_replacement_d3_103(fb_replacement_d2_103):
    feature = _clean(fb_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_103'] = {'inputs': ['fb_replacement_d2_103'], 'func': fb_replacement_d3_103}


def fb_replacement_d3_104(fb_replacement_d2_104):
    feature = _clean(fb_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_104'] = {'inputs': ['fb_replacement_d2_104'], 'func': fb_replacement_d3_104}


def fb_replacement_d3_105(fb_replacement_d2_105):
    feature = _clean(fb_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_105'] = {'inputs': ['fb_replacement_d2_105'], 'func': fb_replacement_d3_105}


def fb_replacement_d3_106(fb_replacement_d2_106):
    feature = _clean(fb_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_106'] = {'inputs': ['fb_replacement_d2_106'], 'func': fb_replacement_d3_106}


def fb_replacement_d3_107(fb_replacement_d2_107):
    feature = _clean(fb_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_107'] = {'inputs': ['fb_replacement_d2_107'], 'func': fb_replacement_d3_107}


def fb_replacement_d3_108(fb_replacement_d2_108):
    feature = _clean(fb_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_108'] = {'inputs': ['fb_replacement_d2_108'], 'func': fb_replacement_d3_108}


def fb_replacement_d3_109(fb_replacement_d2_109):
    feature = _clean(fb_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_109'] = {'inputs': ['fb_replacement_d2_109'], 'func': fb_replacement_d3_109}


def fb_replacement_d3_110(fb_replacement_d2_110):
    feature = _clean(fb_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_110'] = {'inputs': ['fb_replacement_d2_110'], 'func': fb_replacement_d3_110}


def fb_replacement_d3_111(fb_replacement_d2_111):
    feature = _clean(fb_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_111'] = {'inputs': ['fb_replacement_d2_111'], 'func': fb_replacement_d3_111}


def fb_replacement_d3_112(fb_replacement_d2_112):
    feature = _clean(fb_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_112'] = {'inputs': ['fb_replacement_d2_112'], 'func': fb_replacement_d3_112}


def fb_replacement_d3_113(fb_replacement_d2_113):
    feature = _clean(fb_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_113'] = {'inputs': ['fb_replacement_d2_113'], 'func': fb_replacement_d3_113}


def fb_replacement_d3_114(fb_replacement_d2_114):
    feature = _clean(fb_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_114'] = {'inputs': ['fb_replacement_d2_114'], 'func': fb_replacement_d3_114}


def fb_replacement_d3_115(fb_replacement_d2_115):
    feature = _clean(fb_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_115'] = {'inputs': ['fb_replacement_d2_115'], 'func': fb_replacement_d3_115}


def fb_replacement_d3_116(fb_replacement_d2_116):
    feature = _clean(fb_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_116'] = {'inputs': ['fb_replacement_d2_116'], 'func': fb_replacement_d3_116}


def fb_replacement_d3_117(fb_replacement_d2_117):
    feature = _clean(fb_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_117'] = {'inputs': ['fb_replacement_d2_117'], 'func': fb_replacement_d3_117}


def fb_replacement_d3_118(fb_replacement_d2_118):
    feature = _clean(fb_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_118'] = {'inputs': ['fb_replacement_d2_118'], 'func': fb_replacement_d3_118}


def fb_replacement_d3_119(fb_replacement_d2_119):
    feature = _clean(fb_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_119'] = {'inputs': ['fb_replacement_d2_119'], 'func': fb_replacement_d3_119}


def fb_replacement_d3_120(fb_replacement_d2_120):
    feature = _clean(fb_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_120'] = {'inputs': ['fb_replacement_d2_120'], 'func': fb_replacement_d3_120}


def fb_replacement_d3_121(fb_replacement_d2_121):
    feature = _clean(fb_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_121'] = {'inputs': ['fb_replacement_d2_121'], 'func': fb_replacement_d3_121}


def fb_replacement_d3_122(fb_replacement_d2_122):
    feature = _clean(fb_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_122'] = {'inputs': ['fb_replacement_d2_122'], 'func': fb_replacement_d3_122}


def fb_replacement_d3_123(fb_replacement_d2_123):
    feature = _clean(fb_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_123'] = {'inputs': ['fb_replacement_d2_123'], 'func': fb_replacement_d3_123}


def fb_replacement_d3_124(fb_replacement_d2_124):
    feature = _clean(fb_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_124'] = {'inputs': ['fb_replacement_d2_124'], 'func': fb_replacement_d3_124}


def fb_replacement_d3_125(fb_replacement_d2_125):
    feature = _clean(fb_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_125'] = {'inputs': ['fb_replacement_d2_125'], 'func': fb_replacement_d3_125}


def fb_replacement_d3_126(fb_replacement_d2_126):
    feature = _clean(fb_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_126'] = {'inputs': ['fb_replacement_d2_126'], 'func': fb_replacement_d3_126}


def fb_replacement_d3_127(fb_replacement_d2_127):
    feature = _clean(fb_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_127'] = {'inputs': ['fb_replacement_d2_127'], 'func': fb_replacement_d3_127}


def fb_replacement_d3_128(fb_replacement_d2_128):
    feature = _clean(fb_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_128'] = {'inputs': ['fb_replacement_d2_128'], 'func': fb_replacement_d3_128}


def fb_replacement_d3_129(fb_replacement_d2_129):
    feature = _clean(fb_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_129'] = {'inputs': ['fb_replacement_d2_129'], 'func': fb_replacement_d3_129}


def fb_replacement_d3_130(fb_replacement_d2_130):
    feature = _clean(fb_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_130'] = {'inputs': ['fb_replacement_d2_130'], 'func': fb_replacement_d3_130}


def fb_replacement_d3_131(fb_replacement_d2_131):
    feature = _clean(fb_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_131'] = {'inputs': ['fb_replacement_d2_131'], 'func': fb_replacement_d3_131}


def fb_replacement_d3_132(fb_replacement_d2_132):
    feature = _clean(fb_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_132'] = {'inputs': ['fb_replacement_d2_132'], 'func': fb_replacement_d3_132}


def fb_replacement_d3_133(fb_replacement_d2_133):
    feature = _clean(fb_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_133'] = {'inputs': ['fb_replacement_d2_133'], 'func': fb_replacement_d3_133}


def fb_replacement_d3_134(fb_replacement_d2_134):
    feature = _clean(fb_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_134'] = {'inputs': ['fb_replacement_d2_134'], 'func': fb_replacement_d3_134}


def fb_replacement_d3_135(fb_replacement_d2_135):
    feature = _clean(fb_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_135'] = {'inputs': ['fb_replacement_d2_135'], 'func': fb_replacement_d3_135}


def fb_replacement_d3_136(fb_replacement_d2_136):
    feature = _clean(fb_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_136'] = {'inputs': ['fb_replacement_d2_136'], 'func': fb_replacement_d3_136}


def fb_replacement_d3_137(fb_replacement_d2_137):
    feature = _clean(fb_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_137'] = {'inputs': ['fb_replacement_d2_137'], 'func': fb_replacement_d3_137}


def fb_replacement_d3_138(fb_replacement_d2_138):
    feature = _clean(fb_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_138'] = {'inputs': ['fb_replacement_d2_138'], 'func': fb_replacement_d3_138}


def fb_replacement_d3_139(fb_replacement_d2_139):
    feature = _clean(fb_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_139'] = {'inputs': ['fb_replacement_d2_139'], 'func': fb_replacement_d3_139}


def fb_replacement_d3_140(fb_replacement_d2_140):
    feature = _clean(fb_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_140'] = {'inputs': ['fb_replacement_d2_140'], 'func': fb_replacement_d3_140}


def fb_replacement_d3_141(fb_replacement_d2_141):
    feature = _clean(fb_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_141'] = {'inputs': ['fb_replacement_d2_141'], 'func': fb_replacement_d3_141}


def fb_replacement_d3_142(fb_replacement_d2_142):
    feature = _clean(fb_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_142'] = {'inputs': ['fb_replacement_d2_142'], 'func': fb_replacement_d3_142}


def fb_replacement_d3_143(fb_replacement_d2_143):
    feature = _clean(fb_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_143'] = {'inputs': ['fb_replacement_d2_143'], 'func': fb_replacement_d3_143}


def fb_replacement_d3_144(fb_replacement_d2_144):
    feature = _clean(fb_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_144'] = {'inputs': ['fb_replacement_d2_144'], 'func': fb_replacement_d3_144}


def fb_replacement_d3_145(fb_replacement_d2_145):
    feature = _clean(fb_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_145'] = {'inputs': ['fb_replacement_d2_145'], 'func': fb_replacement_d3_145}


def fb_replacement_d3_146(fb_replacement_d2_146):
    feature = _clean(fb_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_146'] = {'inputs': ['fb_replacement_d2_146'], 'func': fb_replacement_d3_146}


def fb_replacement_d3_147(fb_replacement_d2_147):
    feature = _clean(fb_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_147'] = {'inputs': ['fb_replacement_d2_147'], 'func': fb_replacement_d3_147}


def fb_replacement_d3_148(fb_replacement_d2_148):
    feature = _clean(fb_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_148'] = {'inputs': ['fb_replacement_d2_148'], 'func': fb_replacement_d3_148}


def fb_replacement_d3_149(fb_replacement_d2_149):
    feature = _clean(fb_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_149'] = {'inputs': ['fb_replacement_d2_149'], 'func': fb_replacement_d3_149}


def fb_replacement_d3_150(fb_replacement_d2_150):
    feature = _clean(fb_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_150'] = {'inputs': ['fb_replacement_d2_150'], 'func': fb_replacement_d3_150}


def fb_replacement_d3_151(fb_replacement_d2_151):
    feature = _clean(fb_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_151'] = {'inputs': ['fb_replacement_d2_151'], 'func': fb_replacement_d3_151}


def fb_replacement_d3_152(fb_replacement_d2_152):
    feature = _clean(fb_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_152'] = {'inputs': ['fb_replacement_d2_152'], 'func': fb_replacement_d3_152}


def fb_replacement_d3_153(fb_replacement_d2_153):
    feature = _clean(fb_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_153'] = {'inputs': ['fb_replacement_d2_153'], 'func': fb_replacement_d3_153}


def fb_replacement_d3_154(fb_replacement_d2_154):
    feature = _clean(fb_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_154'] = {'inputs': ['fb_replacement_d2_154'], 'func': fb_replacement_d3_154}


def fb_replacement_d3_155(fb_replacement_d2_155):
    feature = _clean(fb_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_155'] = {'inputs': ['fb_replacement_d2_155'], 'func': fb_replacement_d3_155}


def fb_replacement_d3_156(fb_replacement_d2_156):
    feature = _clean(fb_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_156'] = {'inputs': ['fb_replacement_d2_156'], 'func': fb_replacement_d3_156}


def fb_replacement_d3_157(fb_replacement_d2_157):
    feature = _clean(fb_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_157'] = {'inputs': ['fb_replacement_d2_157'], 'func': fb_replacement_d3_157}


def fb_replacement_d3_158(fb_replacement_d2_158):
    feature = _clean(fb_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_158'] = {'inputs': ['fb_replacement_d2_158'], 'func': fb_replacement_d3_158}


def fb_replacement_d3_159(fb_replacement_d2_159):
    feature = _clean(fb_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_159'] = {'inputs': ['fb_replacement_d2_159'], 'func': fb_replacement_d3_159}


def fb_replacement_d3_160(fb_replacement_d2_160):
    feature = _clean(fb_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
FB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fb_replacement_d3_160'] = {'inputs': ['fb_replacement_d2_160'], 'func': fb_replacement_d3_160}


# Third-derivative extensions for repaired first-base features.
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def fbd_base_universe_d3_001_fbd_002_gap_magnitude_10_002(fbd_base_universe_d2_001_fbd_002_gap_magnitude_10_002):
    return _base_universe_d3(fbd_base_universe_d2_001_fbd_002_gap_magnitude_10_002, 1)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_001_fbd_002_gap_magnitude_10_002'] = {'inputs': ['fbd_base_universe_d2_001_fbd_002_gap_magnitude_10_002'], 'func': fbd_base_universe_d3_001_fbd_002_gap_magnitude_10_002}


def fbd_base_universe_d3_002_fbd_003_open_close_pressure_21_003(fbd_base_universe_d2_002_fbd_003_open_close_pressure_21_003):
    return _base_universe_d3(fbd_base_universe_d2_002_fbd_003_open_close_pressure_21_003, 2)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_002_fbd_003_open_close_pressure_21_003'] = {'inputs': ['fbd_base_universe_d2_002_fbd_003_open_close_pressure_21_003'], 'func': fbd_base_universe_d3_002_fbd_003_open_close_pressure_21_003}


def fbd_base_universe_d3_003_fbd_004_lower_wick_ratio_42_004(fbd_base_universe_d2_003_fbd_004_lower_wick_ratio_42_004):
    return _base_universe_d3(fbd_base_universe_d2_003_fbd_004_lower_wick_ratio_42_004, 3)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_003_fbd_004_lower_wick_ratio_42_004'] = {'inputs': ['fbd_base_universe_d2_003_fbd_004_lower_wick_ratio_42_004'], 'func': fbd_base_universe_d3_003_fbd_004_lower_wick_ratio_42_004}


def fbd_base_universe_d3_004_fbd_005_upper_wick_ratio_63_005(fbd_base_universe_d2_004_fbd_005_upper_wick_ratio_63_005):
    return _base_universe_d3(fbd_base_universe_d2_004_fbd_005_upper_wick_ratio_63_005, 4)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_004_fbd_005_upper_wick_ratio_63_005'] = {'inputs': ['fbd_base_universe_d2_004_fbd_005_upper_wick_ratio_63_005'], 'func': fbd_base_universe_d3_004_fbd_005_upper_wick_ratio_63_005}


def fbd_base_universe_d3_005_fbd_006_body_to_range_84_006(fbd_base_universe_d2_005_fbd_006_body_to_range_84_006):
    return _base_universe_d3(fbd_base_universe_d2_005_fbd_006_body_to_range_84_006, 5)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_005_fbd_006_body_to_range_84_006'] = {'inputs': ['fbd_base_universe_d2_005_fbd_006_body_to_range_84_006'], 'func': fbd_base_universe_d3_005_fbd_006_body_to_range_84_006}


def fbd_base_universe_d3_006_fbd_008_gap_magnitude_189_008(fbd_base_universe_d2_006_fbd_008_gap_magnitude_189_008):
    return _base_universe_d3(fbd_base_universe_d2_006_fbd_008_gap_magnitude_189_008, 6)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_006_fbd_008_gap_magnitude_189_008'] = {'inputs': ['fbd_base_universe_d2_006_fbd_008_gap_magnitude_189_008'], 'func': fbd_base_universe_d3_006_fbd_008_gap_magnitude_189_008}


def fbd_base_universe_d3_007_fbd_009_open_close_pressure_252_009(fbd_base_universe_d2_007_fbd_009_open_close_pressure_252_009):
    return _base_universe_d3(fbd_base_universe_d2_007_fbd_009_open_close_pressure_252_009, 7)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_007_fbd_009_open_close_pressure_252_009'] = {'inputs': ['fbd_base_universe_d2_007_fbd_009_open_close_pressure_252_009'], 'func': fbd_base_universe_d3_007_fbd_009_open_close_pressure_252_009}


def fbd_base_universe_d3_008_fbd_010_lower_wick_ratio_378_010(fbd_base_universe_d2_008_fbd_010_lower_wick_ratio_378_010):
    return _base_universe_d3(fbd_base_universe_d2_008_fbd_010_lower_wick_ratio_378_010, 8)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_008_fbd_010_lower_wick_ratio_378_010'] = {'inputs': ['fbd_base_universe_d2_008_fbd_010_lower_wick_ratio_378_010'], 'func': fbd_base_universe_d3_008_fbd_010_lower_wick_ratio_378_010}


def fbd_base_universe_d3_009_fbd_011_upper_wick_ratio_504_011(fbd_base_universe_d2_009_fbd_011_upper_wick_ratio_504_011):
    return _base_universe_d3(fbd_base_universe_d2_009_fbd_011_upper_wick_ratio_504_011, 9)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_009_fbd_011_upper_wick_ratio_504_011'] = {'inputs': ['fbd_base_universe_d2_009_fbd_011_upper_wick_ratio_504_011'], 'func': fbd_base_universe_d3_009_fbd_011_upper_wick_ratio_504_011}


def fbd_base_universe_d3_010_fbd_012_body_to_range_756_012(fbd_base_universe_d2_010_fbd_012_body_to_range_756_012):
    return _base_universe_d3(fbd_base_universe_d2_010_fbd_012_body_to_range_756_012, 10)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_010_fbd_012_body_to_range_756_012'] = {'inputs': ['fbd_base_universe_d2_010_fbd_012_body_to_range_756_012'], 'func': fbd_base_universe_d3_010_fbd_012_body_to_range_756_012}


def fbd_base_universe_d3_011_fbd_014_gap_magnitude_1260_014(fbd_base_universe_d2_011_fbd_014_gap_magnitude_1260_014):
    return _base_universe_d3(fbd_base_universe_d2_011_fbd_014_gap_magnitude_1260_014, 11)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_011_fbd_014_gap_magnitude_1260_014'] = {'inputs': ['fbd_base_universe_d2_011_fbd_014_gap_magnitude_1260_014'], 'func': fbd_base_universe_d3_011_fbd_014_gap_magnitude_1260_014}


def fbd_base_universe_d3_012_fbd_015_open_close_pressure_1512_015(fbd_base_universe_d2_012_fbd_015_open_close_pressure_1512_015):
    return _base_universe_d3(fbd_base_universe_d2_012_fbd_015_open_close_pressure_1512_015, 12)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_012_fbd_015_open_close_pressure_1512_015'] = {'inputs': ['fbd_base_universe_d2_012_fbd_015_open_close_pressure_1512_015'], 'func': fbd_base_universe_d3_012_fbd_015_open_close_pressure_1512_015}


def fbd_base_universe_d3_013_fbd_016_lower_wick_ratio_5_016(fbd_base_universe_d2_013_fbd_016_lower_wick_ratio_5_016):
    return _base_universe_d3(fbd_base_universe_d2_013_fbd_016_lower_wick_ratio_5_016, 13)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_013_fbd_016_lower_wick_ratio_5_016'] = {'inputs': ['fbd_base_universe_d2_013_fbd_016_lower_wick_ratio_5_016'], 'func': fbd_base_universe_d3_013_fbd_016_lower_wick_ratio_5_016}


def fbd_base_universe_d3_014_fbd_017_upper_wick_ratio_10_017(fbd_base_universe_d2_014_fbd_017_upper_wick_ratio_10_017):
    return _base_universe_d3(fbd_base_universe_d2_014_fbd_017_upper_wick_ratio_10_017, 14)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_014_fbd_017_upper_wick_ratio_10_017'] = {'inputs': ['fbd_base_universe_d2_014_fbd_017_upper_wick_ratio_10_017'], 'func': fbd_base_universe_d3_014_fbd_017_upper_wick_ratio_10_017}


def fbd_base_universe_d3_015_fbd_018_body_to_range_21_018(fbd_base_universe_d2_015_fbd_018_body_to_range_21_018):
    return _base_universe_d3(fbd_base_universe_d2_015_fbd_018_body_to_range_21_018, 15)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_015_fbd_018_body_to_range_21_018'] = {'inputs': ['fbd_base_universe_d2_015_fbd_018_body_to_range_21_018'], 'func': fbd_base_universe_d3_015_fbd_018_body_to_range_21_018}


def fbd_base_universe_d3_016_fbd_020_gap_magnitude_63_020(fbd_base_universe_d2_016_fbd_020_gap_magnitude_63_020):
    return _base_universe_d3(fbd_base_universe_d2_016_fbd_020_gap_magnitude_63_020, 16)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_016_fbd_020_gap_magnitude_63_020'] = {'inputs': ['fbd_base_universe_d2_016_fbd_020_gap_magnitude_63_020'], 'func': fbd_base_universe_d3_016_fbd_020_gap_magnitude_63_020}


def fbd_base_universe_d3_017_fbd_021_open_close_pressure_84_021(fbd_base_universe_d2_017_fbd_021_open_close_pressure_84_021):
    return _base_universe_d3(fbd_base_universe_d2_017_fbd_021_open_close_pressure_84_021, 17)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_017_fbd_021_open_close_pressure_84_021'] = {'inputs': ['fbd_base_universe_d2_017_fbd_021_open_close_pressure_84_021'], 'func': fbd_base_universe_d3_017_fbd_021_open_close_pressure_84_021}


def fbd_base_universe_d3_018_fbd_022_lower_wick_ratio_126_022(fbd_base_universe_d2_018_fbd_022_lower_wick_ratio_126_022):
    return _base_universe_d3(fbd_base_universe_d2_018_fbd_022_lower_wick_ratio_126_022, 18)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_018_fbd_022_lower_wick_ratio_126_022'] = {'inputs': ['fbd_base_universe_d2_018_fbd_022_lower_wick_ratio_126_022'], 'func': fbd_base_universe_d3_018_fbd_022_lower_wick_ratio_126_022}


def fbd_base_universe_d3_019_fbd_023_upper_wick_ratio_189_023(fbd_base_universe_d2_019_fbd_023_upper_wick_ratio_189_023):
    return _base_universe_d3(fbd_base_universe_d2_019_fbd_023_upper_wick_ratio_189_023, 19)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_019_fbd_023_upper_wick_ratio_189_023'] = {'inputs': ['fbd_base_universe_d2_019_fbd_023_upper_wick_ratio_189_023'], 'func': fbd_base_universe_d3_019_fbd_023_upper_wick_ratio_189_023}


def fbd_base_universe_d3_020_fbd_024_body_to_range_252_024(fbd_base_universe_d2_020_fbd_024_body_to_range_252_024):
    return _base_universe_d3(fbd_base_universe_d2_020_fbd_024_body_to_range_252_024, 20)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_020_fbd_024_body_to_range_252_024'] = {'inputs': ['fbd_base_universe_d2_020_fbd_024_body_to_range_252_024'], 'func': fbd_base_universe_d3_020_fbd_024_body_to_range_252_024}


def fbd_base_universe_d3_021_fbd_026_gap_magnitude_504_026(fbd_base_universe_d2_021_fbd_026_gap_magnitude_504_026):
    return _base_universe_d3(fbd_base_universe_d2_021_fbd_026_gap_magnitude_504_026, 21)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_021_fbd_026_gap_magnitude_504_026'] = {'inputs': ['fbd_base_universe_d2_021_fbd_026_gap_magnitude_504_026'], 'func': fbd_base_universe_d3_021_fbd_026_gap_magnitude_504_026}


def fbd_base_universe_d3_022_fbd_027_open_close_pressure_756_027(fbd_base_universe_d2_022_fbd_027_open_close_pressure_756_027):
    return _base_universe_d3(fbd_base_universe_d2_022_fbd_027_open_close_pressure_756_027, 22)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_022_fbd_027_open_close_pressure_756_027'] = {'inputs': ['fbd_base_universe_d2_022_fbd_027_open_close_pressure_756_027'], 'func': fbd_base_universe_d3_022_fbd_027_open_close_pressure_756_027}


def fbd_base_universe_d3_023_fbd_028_lower_wick_ratio_1008_028(fbd_base_universe_d2_023_fbd_028_lower_wick_ratio_1008_028):
    return _base_universe_d3(fbd_base_universe_d2_023_fbd_028_lower_wick_ratio_1008_028, 23)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_023_fbd_028_lower_wick_ratio_1008_028'] = {'inputs': ['fbd_base_universe_d2_023_fbd_028_lower_wick_ratio_1008_028'], 'func': fbd_base_universe_d3_023_fbd_028_lower_wick_ratio_1008_028}


def fbd_base_universe_d3_024_fbd_029_upper_wick_ratio_1260_029(fbd_base_universe_d2_024_fbd_029_upper_wick_ratio_1260_029):
    return _base_universe_d3(fbd_base_universe_d2_024_fbd_029_upper_wick_ratio_1260_029, 24)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_024_fbd_029_upper_wick_ratio_1260_029'] = {'inputs': ['fbd_base_universe_d2_024_fbd_029_upper_wick_ratio_1260_029'], 'func': fbd_base_universe_d3_024_fbd_029_upper_wick_ratio_1260_029}


def fbd_base_universe_d3_025_fbd_030_body_to_range_1512_030(fbd_base_universe_d2_025_fbd_030_body_to_range_1512_030):
    return _base_universe_d3(fbd_base_universe_d2_025_fbd_030_body_to_range_1512_030, 25)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_025_fbd_030_body_to_range_1512_030'] = {'inputs': ['fbd_base_universe_d2_025_fbd_030_body_to_range_1512_030'], 'func': fbd_base_universe_d3_025_fbd_030_body_to_range_1512_030}


def fbd_base_universe_d3_026_fbd_basefill_031(fbd_base_universe_d2_026_fbd_basefill_031):
    return _base_universe_d3(fbd_base_universe_d2_026_fbd_basefill_031, 26)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_026_fbd_basefill_031'] = {'inputs': ['fbd_base_universe_d2_026_fbd_basefill_031'], 'func': fbd_base_universe_d3_026_fbd_basefill_031}


def fbd_base_universe_d3_027_fbd_basefill_032(fbd_base_universe_d2_027_fbd_basefill_032):
    return _base_universe_d3(fbd_base_universe_d2_027_fbd_basefill_032, 27)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_027_fbd_basefill_032'] = {'inputs': ['fbd_base_universe_d2_027_fbd_basefill_032'], 'func': fbd_base_universe_d3_027_fbd_basefill_032}


def fbd_base_universe_d3_028_fbd_basefill_033(fbd_base_universe_d2_028_fbd_basefill_033):
    return _base_universe_d3(fbd_base_universe_d2_028_fbd_basefill_033, 28)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_028_fbd_basefill_033'] = {'inputs': ['fbd_base_universe_d2_028_fbd_basefill_033'], 'func': fbd_base_universe_d3_028_fbd_basefill_033}


def fbd_base_universe_d3_029_fbd_basefill_034(fbd_base_universe_d2_029_fbd_basefill_034):
    return _base_universe_d3(fbd_base_universe_d2_029_fbd_basefill_034, 29)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_029_fbd_basefill_034'] = {'inputs': ['fbd_base_universe_d2_029_fbd_basefill_034'], 'func': fbd_base_universe_d3_029_fbd_basefill_034}


def fbd_base_universe_d3_030_fbd_basefill_035(fbd_base_universe_d2_030_fbd_basefill_035):
    return _base_universe_d3(fbd_base_universe_d2_030_fbd_basefill_035, 30)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_030_fbd_basefill_035'] = {'inputs': ['fbd_base_universe_d2_030_fbd_basefill_035'], 'func': fbd_base_universe_d3_030_fbd_basefill_035}


def fbd_base_universe_d3_031_fbd_basefill_036(fbd_base_universe_d2_031_fbd_basefill_036):
    return _base_universe_d3(fbd_base_universe_d2_031_fbd_basefill_036, 31)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_031_fbd_basefill_036'] = {'inputs': ['fbd_base_universe_d2_031_fbd_basefill_036'], 'func': fbd_base_universe_d3_031_fbd_basefill_036}


def fbd_base_universe_d3_032_fbd_basefill_037(fbd_base_universe_d2_032_fbd_basefill_037):
    return _base_universe_d3(fbd_base_universe_d2_032_fbd_basefill_037, 32)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_032_fbd_basefill_037'] = {'inputs': ['fbd_base_universe_d2_032_fbd_basefill_037'], 'func': fbd_base_universe_d3_032_fbd_basefill_037}


def fbd_base_universe_d3_033_fbd_basefill_038(fbd_base_universe_d2_033_fbd_basefill_038):
    return _base_universe_d3(fbd_base_universe_d2_033_fbd_basefill_038, 33)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_033_fbd_basefill_038'] = {'inputs': ['fbd_base_universe_d2_033_fbd_basefill_038'], 'func': fbd_base_universe_d3_033_fbd_basefill_038}


def fbd_base_universe_d3_034_fbd_basefill_039(fbd_base_universe_d2_034_fbd_basefill_039):
    return _base_universe_d3(fbd_base_universe_d2_034_fbd_basefill_039, 34)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_034_fbd_basefill_039'] = {'inputs': ['fbd_base_universe_d2_034_fbd_basefill_039'], 'func': fbd_base_universe_d3_034_fbd_basefill_039}


def fbd_base_universe_d3_035_fbd_basefill_040(fbd_base_universe_d2_035_fbd_basefill_040):
    return _base_universe_d3(fbd_base_universe_d2_035_fbd_basefill_040, 35)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_035_fbd_basefill_040'] = {'inputs': ['fbd_base_universe_d2_035_fbd_basefill_040'], 'func': fbd_base_universe_d3_035_fbd_basefill_040}


def fbd_base_universe_d3_036_fbd_basefill_041(fbd_base_universe_d2_036_fbd_basefill_041):
    return _base_universe_d3(fbd_base_universe_d2_036_fbd_basefill_041, 36)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_036_fbd_basefill_041'] = {'inputs': ['fbd_base_universe_d2_036_fbd_basefill_041'], 'func': fbd_base_universe_d3_036_fbd_basefill_041}


def fbd_base_universe_d3_037_fbd_basefill_042(fbd_base_universe_d2_037_fbd_basefill_042):
    return _base_universe_d3(fbd_base_universe_d2_037_fbd_basefill_042, 37)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_037_fbd_basefill_042'] = {'inputs': ['fbd_base_universe_d2_037_fbd_basefill_042'], 'func': fbd_base_universe_d3_037_fbd_basefill_042}


def fbd_base_universe_d3_038_fbd_basefill_043(fbd_base_universe_d2_038_fbd_basefill_043):
    return _base_universe_d3(fbd_base_universe_d2_038_fbd_basefill_043, 38)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_038_fbd_basefill_043'] = {'inputs': ['fbd_base_universe_d2_038_fbd_basefill_043'], 'func': fbd_base_universe_d3_038_fbd_basefill_043}


def fbd_base_universe_d3_039_fbd_basefill_044(fbd_base_universe_d2_039_fbd_basefill_044):
    return _base_universe_d3(fbd_base_universe_d2_039_fbd_basefill_044, 39)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_039_fbd_basefill_044'] = {'inputs': ['fbd_base_universe_d2_039_fbd_basefill_044'], 'func': fbd_base_universe_d3_039_fbd_basefill_044}


def fbd_base_universe_d3_040_fbd_basefill_045(fbd_base_universe_d2_040_fbd_basefill_045):
    return _base_universe_d3(fbd_base_universe_d2_040_fbd_basefill_045, 40)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_040_fbd_basefill_045'] = {'inputs': ['fbd_base_universe_d2_040_fbd_basefill_045'], 'func': fbd_base_universe_d3_040_fbd_basefill_045}


def fbd_base_universe_d3_041_fbd_basefill_046(fbd_base_universe_d2_041_fbd_basefill_046):
    return _base_universe_d3(fbd_base_universe_d2_041_fbd_basefill_046, 41)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_041_fbd_basefill_046'] = {'inputs': ['fbd_base_universe_d2_041_fbd_basefill_046'], 'func': fbd_base_universe_d3_041_fbd_basefill_046}


def fbd_base_universe_d3_042_fbd_basefill_047(fbd_base_universe_d2_042_fbd_basefill_047):
    return _base_universe_d3(fbd_base_universe_d2_042_fbd_basefill_047, 42)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_042_fbd_basefill_047'] = {'inputs': ['fbd_base_universe_d2_042_fbd_basefill_047'], 'func': fbd_base_universe_d3_042_fbd_basefill_047}


def fbd_base_universe_d3_043_fbd_basefill_048(fbd_base_universe_d2_043_fbd_basefill_048):
    return _base_universe_d3(fbd_base_universe_d2_043_fbd_basefill_048, 43)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_043_fbd_basefill_048'] = {'inputs': ['fbd_base_universe_d2_043_fbd_basefill_048'], 'func': fbd_base_universe_d3_043_fbd_basefill_048}


def fbd_base_universe_d3_044_fbd_basefill_049(fbd_base_universe_d2_044_fbd_basefill_049):
    return _base_universe_d3(fbd_base_universe_d2_044_fbd_basefill_049, 44)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_044_fbd_basefill_049'] = {'inputs': ['fbd_base_universe_d2_044_fbd_basefill_049'], 'func': fbd_base_universe_d3_044_fbd_basefill_049}


def fbd_base_universe_d3_045_fbd_basefill_050(fbd_base_universe_d2_045_fbd_basefill_050):
    return _base_universe_d3(fbd_base_universe_d2_045_fbd_basefill_050, 45)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_045_fbd_basefill_050'] = {'inputs': ['fbd_base_universe_d2_045_fbd_basefill_050'], 'func': fbd_base_universe_d3_045_fbd_basefill_050}


def fbd_base_universe_d3_046_fbd_basefill_051(fbd_base_universe_d2_046_fbd_basefill_051):
    return _base_universe_d3(fbd_base_universe_d2_046_fbd_basefill_051, 46)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_046_fbd_basefill_051'] = {'inputs': ['fbd_base_universe_d2_046_fbd_basefill_051'], 'func': fbd_base_universe_d3_046_fbd_basefill_051}


def fbd_base_universe_d3_047_fbd_basefill_052(fbd_base_universe_d2_047_fbd_basefill_052):
    return _base_universe_d3(fbd_base_universe_d2_047_fbd_basefill_052, 47)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_047_fbd_basefill_052'] = {'inputs': ['fbd_base_universe_d2_047_fbd_basefill_052'], 'func': fbd_base_universe_d3_047_fbd_basefill_052}


def fbd_base_universe_d3_048_fbd_basefill_053(fbd_base_universe_d2_048_fbd_basefill_053):
    return _base_universe_d3(fbd_base_universe_d2_048_fbd_basefill_053, 48)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_048_fbd_basefill_053'] = {'inputs': ['fbd_base_universe_d2_048_fbd_basefill_053'], 'func': fbd_base_universe_d3_048_fbd_basefill_053}


def fbd_base_universe_d3_049_fbd_basefill_054(fbd_base_universe_d2_049_fbd_basefill_054):
    return _base_universe_d3(fbd_base_universe_d2_049_fbd_basefill_054, 49)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_049_fbd_basefill_054'] = {'inputs': ['fbd_base_universe_d2_049_fbd_basefill_054'], 'func': fbd_base_universe_d3_049_fbd_basefill_054}


def fbd_base_universe_d3_050_fbd_basefill_055(fbd_base_universe_d2_050_fbd_basefill_055):
    return _base_universe_d3(fbd_base_universe_d2_050_fbd_basefill_055, 50)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_050_fbd_basefill_055'] = {'inputs': ['fbd_base_universe_d2_050_fbd_basefill_055'], 'func': fbd_base_universe_d3_050_fbd_basefill_055}


def fbd_base_universe_d3_051_fbd_basefill_056(fbd_base_universe_d2_051_fbd_basefill_056):
    return _base_universe_d3(fbd_base_universe_d2_051_fbd_basefill_056, 51)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_051_fbd_basefill_056'] = {'inputs': ['fbd_base_universe_d2_051_fbd_basefill_056'], 'func': fbd_base_universe_d3_051_fbd_basefill_056}


def fbd_base_universe_d3_052_fbd_basefill_057(fbd_base_universe_d2_052_fbd_basefill_057):
    return _base_universe_d3(fbd_base_universe_d2_052_fbd_basefill_057, 52)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_052_fbd_basefill_057'] = {'inputs': ['fbd_base_universe_d2_052_fbd_basefill_057'], 'func': fbd_base_universe_d3_052_fbd_basefill_057}


def fbd_base_universe_d3_053_fbd_basefill_058(fbd_base_universe_d2_053_fbd_basefill_058):
    return _base_universe_d3(fbd_base_universe_d2_053_fbd_basefill_058, 53)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_053_fbd_basefill_058'] = {'inputs': ['fbd_base_universe_d2_053_fbd_basefill_058'], 'func': fbd_base_universe_d3_053_fbd_basefill_058}


def fbd_base_universe_d3_054_fbd_basefill_059(fbd_base_universe_d2_054_fbd_basefill_059):
    return _base_universe_d3(fbd_base_universe_d2_054_fbd_basefill_059, 54)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_054_fbd_basefill_059'] = {'inputs': ['fbd_base_universe_d2_054_fbd_basefill_059'], 'func': fbd_base_universe_d3_054_fbd_basefill_059}


def fbd_base_universe_d3_055_fbd_basefill_060(fbd_base_universe_d2_055_fbd_basefill_060):
    return _base_universe_d3(fbd_base_universe_d2_055_fbd_basefill_060, 55)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_055_fbd_basefill_060'] = {'inputs': ['fbd_base_universe_d2_055_fbd_basefill_060'], 'func': fbd_base_universe_d3_055_fbd_basefill_060}


def fbd_base_universe_d3_056_fbd_basefill_061(fbd_base_universe_d2_056_fbd_basefill_061):
    return _base_universe_d3(fbd_base_universe_d2_056_fbd_basefill_061, 56)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_056_fbd_basefill_061'] = {'inputs': ['fbd_base_universe_d2_056_fbd_basefill_061'], 'func': fbd_base_universe_d3_056_fbd_basefill_061}


def fbd_base_universe_d3_057_fbd_basefill_062(fbd_base_universe_d2_057_fbd_basefill_062):
    return _base_universe_d3(fbd_base_universe_d2_057_fbd_basefill_062, 57)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_057_fbd_basefill_062'] = {'inputs': ['fbd_base_universe_d2_057_fbd_basefill_062'], 'func': fbd_base_universe_d3_057_fbd_basefill_062}


def fbd_base_universe_d3_058_fbd_basefill_063(fbd_base_universe_d2_058_fbd_basefill_063):
    return _base_universe_d3(fbd_base_universe_d2_058_fbd_basefill_063, 58)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_058_fbd_basefill_063'] = {'inputs': ['fbd_base_universe_d2_058_fbd_basefill_063'], 'func': fbd_base_universe_d3_058_fbd_basefill_063}


def fbd_base_universe_d3_059_fbd_basefill_064(fbd_base_universe_d2_059_fbd_basefill_064):
    return _base_universe_d3(fbd_base_universe_d2_059_fbd_basefill_064, 59)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_059_fbd_basefill_064'] = {'inputs': ['fbd_base_universe_d2_059_fbd_basefill_064'], 'func': fbd_base_universe_d3_059_fbd_basefill_064}


def fbd_base_universe_d3_060_fbd_basefill_065(fbd_base_universe_d2_060_fbd_basefill_065):
    return _base_universe_d3(fbd_base_universe_d2_060_fbd_basefill_065, 60)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_060_fbd_basefill_065'] = {'inputs': ['fbd_base_universe_d2_060_fbd_basefill_065'], 'func': fbd_base_universe_d3_060_fbd_basefill_065}


def fbd_base_universe_d3_061_fbd_basefill_066(fbd_base_universe_d2_061_fbd_basefill_066):
    return _base_universe_d3(fbd_base_universe_d2_061_fbd_basefill_066, 61)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_061_fbd_basefill_066'] = {'inputs': ['fbd_base_universe_d2_061_fbd_basefill_066'], 'func': fbd_base_universe_d3_061_fbd_basefill_066}


def fbd_base_universe_d3_062_fbd_basefill_067(fbd_base_universe_d2_062_fbd_basefill_067):
    return _base_universe_d3(fbd_base_universe_d2_062_fbd_basefill_067, 62)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_062_fbd_basefill_067'] = {'inputs': ['fbd_base_universe_d2_062_fbd_basefill_067'], 'func': fbd_base_universe_d3_062_fbd_basefill_067}


def fbd_base_universe_d3_063_fbd_basefill_068(fbd_base_universe_d2_063_fbd_basefill_068):
    return _base_universe_d3(fbd_base_universe_d2_063_fbd_basefill_068, 63)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_063_fbd_basefill_068'] = {'inputs': ['fbd_base_universe_d2_063_fbd_basefill_068'], 'func': fbd_base_universe_d3_063_fbd_basefill_068}


def fbd_base_universe_d3_064_fbd_basefill_069(fbd_base_universe_d2_064_fbd_basefill_069):
    return _base_universe_d3(fbd_base_universe_d2_064_fbd_basefill_069, 64)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_064_fbd_basefill_069'] = {'inputs': ['fbd_base_universe_d2_064_fbd_basefill_069'], 'func': fbd_base_universe_d3_064_fbd_basefill_069}


def fbd_base_universe_d3_065_fbd_basefill_070(fbd_base_universe_d2_065_fbd_basefill_070):
    return _base_universe_d3(fbd_base_universe_d2_065_fbd_basefill_070, 65)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_065_fbd_basefill_070'] = {'inputs': ['fbd_base_universe_d2_065_fbd_basefill_070'], 'func': fbd_base_universe_d3_065_fbd_basefill_070}


def fbd_base_universe_d3_066_fbd_basefill_071(fbd_base_universe_d2_066_fbd_basefill_071):
    return _base_universe_d3(fbd_base_universe_d2_066_fbd_basefill_071, 66)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_066_fbd_basefill_071'] = {'inputs': ['fbd_base_universe_d2_066_fbd_basefill_071'], 'func': fbd_base_universe_d3_066_fbd_basefill_071}


def fbd_base_universe_d3_067_fbd_basefill_072(fbd_base_universe_d2_067_fbd_basefill_072):
    return _base_universe_d3(fbd_base_universe_d2_067_fbd_basefill_072, 67)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_067_fbd_basefill_072'] = {'inputs': ['fbd_base_universe_d2_067_fbd_basefill_072'], 'func': fbd_base_universe_d3_067_fbd_basefill_072}


def fbd_base_universe_d3_068_fbd_basefill_073(fbd_base_universe_d2_068_fbd_basefill_073):
    return _base_universe_d3(fbd_base_universe_d2_068_fbd_basefill_073, 68)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_068_fbd_basefill_073'] = {'inputs': ['fbd_base_universe_d2_068_fbd_basefill_073'], 'func': fbd_base_universe_d3_068_fbd_basefill_073}


def fbd_base_universe_d3_069_fbd_basefill_074(fbd_base_universe_d2_069_fbd_basefill_074):
    return _base_universe_d3(fbd_base_universe_d2_069_fbd_basefill_074, 69)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_069_fbd_basefill_074'] = {'inputs': ['fbd_base_universe_d2_069_fbd_basefill_074'], 'func': fbd_base_universe_d3_069_fbd_basefill_074}


def fbd_base_universe_d3_070_fbd_basefill_075(fbd_base_universe_d2_070_fbd_basefill_075):
    return _base_universe_d3(fbd_base_universe_d2_070_fbd_basefill_075, 70)
FBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fbd_base_universe_d3_070_fbd_basefill_075'] = {'inputs': ['fbd_base_universe_d2_070_fbd_basefill_075'], 'func': fbd_base_universe_d3_070_fbd_basefill_075}
