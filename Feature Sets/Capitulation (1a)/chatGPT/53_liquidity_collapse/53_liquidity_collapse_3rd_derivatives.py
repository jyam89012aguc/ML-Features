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



def lqc_001_amihud_illiquidity_accel_1(lqc_001_amihud_illiquidity_roc_1):
    feature = _s(lqc_001_amihud_illiquidity_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def lqc_007_amihud_illiquidity_accel_5(lqc_007_amihud_illiquidity_roc_5):
    feature = _s(lqc_007_amihud_illiquidity_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def lqc_013_amihud_illiquidity_accel_42(lqc_013_amihud_illiquidity_roc_42):
    feature = _s(lqc_013_amihud_illiquidity_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def lqc_179_lqc_019_amihud_illiquidity_42_019_accel_126(lqc_154_lqc_019_amihud_illiquidity_42_019_roc_126):
    feature = _s(lqc_154_lqc_019_amihud_illiquidity_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def lqc_180_lqc_025_amihud_illiquidity_378_025_accel_378(lqc_155_lqc_025_amihud_illiquidity_378_025_roc_378):
    feature = _s(lqc_155_lqc_025_amihud_illiquidity_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















LIQUIDITY_COLLAPSE_REGISTRY_3RD_DERIVATIVES = {
    'lqc_001_amihud_illiquidity_accel_1': {'inputs': ['lqc_001_amihud_illiquidity_roc_1'], 'func': lqc_001_amihud_illiquidity_accel_1},
    'lqc_007_amihud_illiquidity_accel_5': {'inputs': ['lqc_007_amihud_illiquidity_roc_5'], 'func': lqc_007_amihud_illiquidity_accel_5},
    'lqc_013_amihud_illiquidity_accel_42': {'inputs': ['lqc_013_amihud_illiquidity_roc_42'], 'func': lqc_013_amihud_illiquidity_accel_42},
    'lqc_179_lqc_019_amihud_illiquidity_42_019_accel_126': {'inputs': ['lqc_154_lqc_019_amihud_illiquidity_42_019_roc_126'], 'func': lqc_179_lqc_019_amihud_illiquidity_42_019_accel_126},
    'lqc_180_lqc_025_amihud_illiquidity_378_025_accel_378': {'inputs': ['lqc_155_lqc_025_amihud_illiquidity_378_025_roc_378'], 'func': lqc_180_lqc_025_amihud_illiquidity_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def lc_replacement_d3_001(lc_replacement_d2_001):
    feature = _clean(lc_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_001'] = {'inputs': ['lc_replacement_d2_001'], 'func': lc_replacement_d3_001}


def lc_replacement_d3_002(lc_replacement_d2_002):
    feature = _clean(lc_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_002'] = {'inputs': ['lc_replacement_d2_002'], 'func': lc_replacement_d3_002}


def lc_replacement_d3_003(lc_replacement_d2_003):
    feature = _clean(lc_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_003'] = {'inputs': ['lc_replacement_d2_003'], 'func': lc_replacement_d3_003}


def lc_replacement_d3_004(lc_replacement_d2_004):
    feature = _clean(lc_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_004'] = {'inputs': ['lc_replacement_d2_004'], 'func': lc_replacement_d3_004}


def lc_replacement_d3_005(lc_replacement_d2_005):
    feature = _clean(lc_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_005'] = {'inputs': ['lc_replacement_d2_005'], 'func': lc_replacement_d3_005}


def lc_replacement_d3_006(lc_replacement_d2_006):
    feature = _clean(lc_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_006'] = {'inputs': ['lc_replacement_d2_006'], 'func': lc_replacement_d3_006}


def lc_replacement_d3_007(lc_replacement_d2_007):
    feature = _clean(lc_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_007'] = {'inputs': ['lc_replacement_d2_007'], 'func': lc_replacement_d3_007}


def lc_replacement_d3_008(lc_replacement_d2_008):
    feature = _clean(lc_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_008'] = {'inputs': ['lc_replacement_d2_008'], 'func': lc_replacement_d3_008}


def lc_replacement_d3_009(lc_replacement_d2_009):
    feature = _clean(lc_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_009'] = {'inputs': ['lc_replacement_d2_009'], 'func': lc_replacement_d3_009}


def lc_replacement_d3_010(lc_replacement_d2_010):
    feature = _clean(lc_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_010'] = {'inputs': ['lc_replacement_d2_010'], 'func': lc_replacement_d3_010}


def lc_replacement_d3_011(lc_replacement_d2_011):
    feature = _clean(lc_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_011'] = {'inputs': ['lc_replacement_d2_011'], 'func': lc_replacement_d3_011}


def lc_replacement_d3_012(lc_replacement_d2_012):
    feature = _clean(lc_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_012'] = {'inputs': ['lc_replacement_d2_012'], 'func': lc_replacement_d3_012}


def lc_replacement_d3_013(lc_replacement_d2_013):
    feature = _clean(lc_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_013'] = {'inputs': ['lc_replacement_d2_013'], 'func': lc_replacement_d3_013}


def lc_replacement_d3_014(lc_replacement_d2_014):
    feature = _clean(lc_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_014'] = {'inputs': ['lc_replacement_d2_014'], 'func': lc_replacement_d3_014}


def lc_replacement_d3_015(lc_replacement_d2_015):
    feature = _clean(lc_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_015'] = {'inputs': ['lc_replacement_d2_015'], 'func': lc_replacement_d3_015}


def lc_replacement_d3_016(lc_replacement_d2_016):
    feature = _clean(lc_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_016'] = {'inputs': ['lc_replacement_d2_016'], 'func': lc_replacement_d3_016}


def lc_replacement_d3_017(lc_replacement_d2_017):
    feature = _clean(lc_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_017'] = {'inputs': ['lc_replacement_d2_017'], 'func': lc_replacement_d3_017}


def lc_replacement_d3_018(lc_replacement_d2_018):
    feature = _clean(lc_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_018'] = {'inputs': ['lc_replacement_d2_018'], 'func': lc_replacement_d3_018}


def lc_replacement_d3_019(lc_replacement_d2_019):
    feature = _clean(lc_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_019'] = {'inputs': ['lc_replacement_d2_019'], 'func': lc_replacement_d3_019}


def lc_replacement_d3_020(lc_replacement_d2_020):
    feature = _clean(lc_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_020'] = {'inputs': ['lc_replacement_d2_020'], 'func': lc_replacement_d3_020}


def lc_replacement_d3_021(lc_replacement_d2_021):
    feature = _clean(lc_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_021'] = {'inputs': ['lc_replacement_d2_021'], 'func': lc_replacement_d3_021}


def lc_replacement_d3_022(lc_replacement_d2_022):
    feature = _clean(lc_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_022'] = {'inputs': ['lc_replacement_d2_022'], 'func': lc_replacement_d3_022}


def lc_replacement_d3_023(lc_replacement_d2_023):
    feature = _clean(lc_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_023'] = {'inputs': ['lc_replacement_d2_023'], 'func': lc_replacement_d3_023}


def lc_replacement_d3_024(lc_replacement_d2_024):
    feature = _clean(lc_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_024'] = {'inputs': ['lc_replacement_d2_024'], 'func': lc_replacement_d3_024}


def lc_replacement_d3_025(lc_replacement_d2_025):
    feature = _clean(lc_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_025'] = {'inputs': ['lc_replacement_d2_025'], 'func': lc_replacement_d3_025}


def lc_replacement_d3_026(lc_replacement_d2_026):
    feature = _clean(lc_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_026'] = {'inputs': ['lc_replacement_d2_026'], 'func': lc_replacement_d3_026}


def lc_replacement_d3_027(lc_replacement_d2_027):
    feature = _clean(lc_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_027'] = {'inputs': ['lc_replacement_d2_027'], 'func': lc_replacement_d3_027}


def lc_replacement_d3_028(lc_replacement_d2_028):
    feature = _clean(lc_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_028'] = {'inputs': ['lc_replacement_d2_028'], 'func': lc_replacement_d3_028}


def lc_replacement_d3_029(lc_replacement_d2_029):
    feature = _clean(lc_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_029'] = {'inputs': ['lc_replacement_d2_029'], 'func': lc_replacement_d3_029}


def lc_replacement_d3_030(lc_replacement_d2_030):
    feature = _clean(lc_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_030'] = {'inputs': ['lc_replacement_d2_030'], 'func': lc_replacement_d3_030}


def lc_replacement_d3_031(lc_replacement_d2_031):
    feature = _clean(lc_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_031'] = {'inputs': ['lc_replacement_d2_031'], 'func': lc_replacement_d3_031}


def lc_replacement_d3_032(lc_replacement_d2_032):
    feature = _clean(lc_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_032'] = {'inputs': ['lc_replacement_d2_032'], 'func': lc_replacement_d3_032}


def lc_replacement_d3_033(lc_replacement_d2_033):
    feature = _clean(lc_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_033'] = {'inputs': ['lc_replacement_d2_033'], 'func': lc_replacement_d3_033}


def lc_replacement_d3_034(lc_replacement_d2_034):
    feature = _clean(lc_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_034'] = {'inputs': ['lc_replacement_d2_034'], 'func': lc_replacement_d3_034}


def lc_replacement_d3_035(lc_replacement_d2_035):
    feature = _clean(lc_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_035'] = {'inputs': ['lc_replacement_d2_035'], 'func': lc_replacement_d3_035}


def lc_replacement_d3_036(lc_replacement_d2_036):
    feature = _clean(lc_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_036'] = {'inputs': ['lc_replacement_d2_036'], 'func': lc_replacement_d3_036}


def lc_replacement_d3_037(lc_replacement_d2_037):
    feature = _clean(lc_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_037'] = {'inputs': ['lc_replacement_d2_037'], 'func': lc_replacement_d3_037}


def lc_replacement_d3_038(lc_replacement_d2_038):
    feature = _clean(lc_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_038'] = {'inputs': ['lc_replacement_d2_038'], 'func': lc_replacement_d3_038}


def lc_replacement_d3_039(lc_replacement_d2_039):
    feature = _clean(lc_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_039'] = {'inputs': ['lc_replacement_d2_039'], 'func': lc_replacement_d3_039}


def lc_replacement_d3_040(lc_replacement_d2_040):
    feature = _clean(lc_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_040'] = {'inputs': ['lc_replacement_d2_040'], 'func': lc_replacement_d3_040}


def lc_replacement_d3_041(lc_replacement_d2_041):
    feature = _clean(lc_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_041'] = {'inputs': ['lc_replacement_d2_041'], 'func': lc_replacement_d3_041}


def lc_replacement_d3_042(lc_replacement_d2_042):
    feature = _clean(lc_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_042'] = {'inputs': ['lc_replacement_d2_042'], 'func': lc_replacement_d3_042}


def lc_replacement_d3_043(lc_replacement_d2_043):
    feature = _clean(lc_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_043'] = {'inputs': ['lc_replacement_d2_043'], 'func': lc_replacement_d3_043}


def lc_replacement_d3_044(lc_replacement_d2_044):
    feature = _clean(lc_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_044'] = {'inputs': ['lc_replacement_d2_044'], 'func': lc_replacement_d3_044}


def lc_replacement_d3_045(lc_replacement_d2_045):
    feature = _clean(lc_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_045'] = {'inputs': ['lc_replacement_d2_045'], 'func': lc_replacement_d3_045}


def lc_replacement_d3_046(lc_replacement_d2_046):
    feature = _clean(lc_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_046'] = {'inputs': ['lc_replacement_d2_046'], 'func': lc_replacement_d3_046}


def lc_replacement_d3_047(lc_replacement_d2_047):
    feature = _clean(lc_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_047'] = {'inputs': ['lc_replacement_d2_047'], 'func': lc_replacement_d3_047}


def lc_replacement_d3_048(lc_replacement_d2_048):
    feature = _clean(lc_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_048'] = {'inputs': ['lc_replacement_d2_048'], 'func': lc_replacement_d3_048}


def lc_replacement_d3_049(lc_replacement_d2_049):
    feature = _clean(lc_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_049'] = {'inputs': ['lc_replacement_d2_049'], 'func': lc_replacement_d3_049}


def lc_replacement_d3_050(lc_replacement_d2_050):
    feature = _clean(lc_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_050'] = {'inputs': ['lc_replacement_d2_050'], 'func': lc_replacement_d3_050}


def lc_replacement_d3_051(lc_replacement_d2_051):
    feature = _clean(lc_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_051'] = {'inputs': ['lc_replacement_d2_051'], 'func': lc_replacement_d3_051}


def lc_replacement_d3_052(lc_replacement_d2_052):
    feature = _clean(lc_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_052'] = {'inputs': ['lc_replacement_d2_052'], 'func': lc_replacement_d3_052}


def lc_replacement_d3_053(lc_replacement_d2_053):
    feature = _clean(lc_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_053'] = {'inputs': ['lc_replacement_d2_053'], 'func': lc_replacement_d3_053}


def lc_replacement_d3_054(lc_replacement_d2_054):
    feature = _clean(lc_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_054'] = {'inputs': ['lc_replacement_d2_054'], 'func': lc_replacement_d3_054}


def lc_replacement_d3_055(lc_replacement_d2_055):
    feature = _clean(lc_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_055'] = {'inputs': ['lc_replacement_d2_055'], 'func': lc_replacement_d3_055}


def lc_replacement_d3_056(lc_replacement_d2_056):
    feature = _clean(lc_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_056'] = {'inputs': ['lc_replacement_d2_056'], 'func': lc_replacement_d3_056}


def lc_replacement_d3_057(lc_replacement_d2_057):
    feature = _clean(lc_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_057'] = {'inputs': ['lc_replacement_d2_057'], 'func': lc_replacement_d3_057}


def lc_replacement_d3_058(lc_replacement_d2_058):
    feature = _clean(lc_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_058'] = {'inputs': ['lc_replacement_d2_058'], 'func': lc_replacement_d3_058}


def lc_replacement_d3_059(lc_replacement_d2_059):
    feature = _clean(lc_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_059'] = {'inputs': ['lc_replacement_d2_059'], 'func': lc_replacement_d3_059}


def lc_replacement_d3_060(lc_replacement_d2_060):
    feature = _clean(lc_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_060'] = {'inputs': ['lc_replacement_d2_060'], 'func': lc_replacement_d3_060}


def lc_replacement_d3_061(lc_replacement_d2_061):
    feature = _clean(lc_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_061'] = {'inputs': ['lc_replacement_d2_061'], 'func': lc_replacement_d3_061}


def lc_replacement_d3_062(lc_replacement_d2_062):
    feature = _clean(lc_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_062'] = {'inputs': ['lc_replacement_d2_062'], 'func': lc_replacement_d3_062}


def lc_replacement_d3_063(lc_replacement_d2_063):
    feature = _clean(lc_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_063'] = {'inputs': ['lc_replacement_d2_063'], 'func': lc_replacement_d3_063}


def lc_replacement_d3_064(lc_replacement_d2_064):
    feature = _clean(lc_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_064'] = {'inputs': ['lc_replacement_d2_064'], 'func': lc_replacement_d3_064}


def lc_replacement_d3_065(lc_replacement_d2_065):
    feature = _clean(lc_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_065'] = {'inputs': ['lc_replacement_d2_065'], 'func': lc_replacement_d3_065}


def lc_replacement_d3_066(lc_replacement_d2_066):
    feature = _clean(lc_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_066'] = {'inputs': ['lc_replacement_d2_066'], 'func': lc_replacement_d3_066}


def lc_replacement_d3_067(lc_replacement_d2_067):
    feature = _clean(lc_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_067'] = {'inputs': ['lc_replacement_d2_067'], 'func': lc_replacement_d3_067}


def lc_replacement_d3_068(lc_replacement_d2_068):
    feature = _clean(lc_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_068'] = {'inputs': ['lc_replacement_d2_068'], 'func': lc_replacement_d3_068}


def lc_replacement_d3_069(lc_replacement_d2_069):
    feature = _clean(lc_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_069'] = {'inputs': ['lc_replacement_d2_069'], 'func': lc_replacement_d3_069}


def lc_replacement_d3_070(lc_replacement_d2_070):
    feature = _clean(lc_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_070'] = {'inputs': ['lc_replacement_d2_070'], 'func': lc_replacement_d3_070}


def lc_replacement_d3_071(lc_replacement_d2_071):
    feature = _clean(lc_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_071'] = {'inputs': ['lc_replacement_d2_071'], 'func': lc_replacement_d3_071}


def lc_replacement_d3_072(lc_replacement_d2_072):
    feature = _clean(lc_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_072'] = {'inputs': ['lc_replacement_d2_072'], 'func': lc_replacement_d3_072}


def lc_replacement_d3_073(lc_replacement_d2_073):
    feature = _clean(lc_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_073'] = {'inputs': ['lc_replacement_d2_073'], 'func': lc_replacement_d3_073}


def lc_replacement_d3_074(lc_replacement_d2_074):
    feature = _clean(lc_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_074'] = {'inputs': ['lc_replacement_d2_074'], 'func': lc_replacement_d3_074}


def lc_replacement_d3_075(lc_replacement_d2_075):
    feature = _clean(lc_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_075'] = {'inputs': ['lc_replacement_d2_075'], 'func': lc_replacement_d3_075}


def lc_replacement_d3_076(lc_replacement_d2_076):
    feature = _clean(lc_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_076'] = {'inputs': ['lc_replacement_d2_076'], 'func': lc_replacement_d3_076}


def lc_replacement_d3_077(lc_replacement_d2_077):
    feature = _clean(lc_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_077'] = {'inputs': ['lc_replacement_d2_077'], 'func': lc_replacement_d3_077}


def lc_replacement_d3_078(lc_replacement_d2_078):
    feature = _clean(lc_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_078'] = {'inputs': ['lc_replacement_d2_078'], 'func': lc_replacement_d3_078}


def lc_replacement_d3_079(lc_replacement_d2_079):
    feature = _clean(lc_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_079'] = {'inputs': ['lc_replacement_d2_079'], 'func': lc_replacement_d3_079}


def lc_replacement_d3_080(lc_replacement_d2_080):
    feature = _clean(lc_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_080'] = {'inputs': ['lc_replacement_d2_080'], 'func': lc_replacement_d3_080}


def lc_replacement_d3_081(lc_replacement_d2_081):
    feature = _clean(lc_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_081'] = {'inputs': ['lc_replacement_d2_081'], 'func': lc_replacement_d3_081}


def lc_replacement_d3_082(lc_replacement_d2_082):
    feature = _clean(lc_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_082'] = {'inputs': ['lc_replacement_d2_082'], 'func': lc_replacement_d3_082}


def lc_replacement_d3_083(lc_replacement_d2_083):
    feature = _clean(lc_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_083'] = {'inputs': ['lc_replacement_d2_083'], 'func': lc_replacement_d3_083}


def lc_replacement_d3_084(lc_replacement_d2_084):
    feature = _clean(lc_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_084'] = {'inputs': ['lc_replacement_d2_084'], 'func': lc_replacement_d3_084}


def lc_replacement_d3_085(lc_replacement_d2_085):
    feature = _clean(lc_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_085'] = {'inputs': ['lc_replacement_d2_085'], 'func': lc_replacement_d3_085}


def lc_replacement_d3_086(lc_replacement_d2_086):
    feature = _clean(lc_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_086'] = {'inputs': ['lc_replacement_d2_086'], 'func': lc_replacement_d3_086}


def lc_replacement_d3_087(lc_replacement_d2_087):
    feature = _clean(lc_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_087'] = {'inputs': ['lc_replacement_d2_087'], 'func': lc_replacement_d3_087}


def lc_replacement_d3_088(lc_replacement_d2_088):
    feature = _clean(lc_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_088'] = {'inputs': ['lc_replacement_d2_088'], 'func': lc_replacement_d3_088}


def lc_replacement_d3_089(lc_replacement_d2_089):
    feature = _clean(lc_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_089'] = {'inputs': ['lc_replacement_d2_089'], 'func': lc_replacement_d3_089}


def lc_replacement_d3_090(lc_replacement_d2_090):
    feature = _clean(lc_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_090'] = {'inputs': ['lc_replacement_d2_090'], 'func': lc_replacement_d3_090}


def lc_replacement_d3_091(lc_replacement_d2_091):
    feature = _clean(lc_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_091'] = {'inputs': ['lc_replacement_d2_091'], 'func': lc_replacement_d3_091}


def lc_replacement_d3_092(lc_replacement_d2_092):
    feature = _clean(lc_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_092'] = {'inputs': ['lc_replacement_d2_092'], 'func': lc_replacement_d3_092}


def lc_replacement_d3_093(lc_replacement_d2_093):
    feature = _clean(lc_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_093'] = {'inputs': ['lc_replacement_d2_093'], 'func': lc_replacement_d3_093}


def lc_replacement_d3_094(lc_replacement_d2_094):
    feature = _clean(lc_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_094'] = {'inputs': ['lc_replacement_d2_094'], 'func': lc_replacement_d3_094}


def lc_replacement_d3_095(lc_replacement_d2_095):
    feature = _clean(lc_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_095'] = {'inputs': ['lc_replacement_d2_095'], 'func': lc_replacement_d3_095}


def lc_replacement_d3_096(lc_replacement_d2_096):
    feature = _clean(lc_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_096'] = {'inputs': ['lc_replacement_d2_096'], 'func': lc_replacement_d3_096}


def lc_replacement_d3_097(lc_replacement_d2_097):
    feature = _clean(lc_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_097'] = {'inputs': ['lc_replacement_d2_097'], 'func': lc_replacement_d3_097}


def lc_replacement_d3_098(lc_replacement_d2_098):
    feature = _clean(lc_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_098'] = {'inputs': ['lc_replacement_d2_098'], 'func': lc_replacement_d3_098}


def lc_replacement_d3_099(lc_replacement_d2_099):
    feature = _clean(lc_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_099'] = {'inputs': ['lc_replacement_d2_099'], 'func': lc_replacement_d3_099}


def lc_replacement_d3_100(lc_replacement_d2_100):
    feature = _clean(lc_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_100'] = {'inputs': ['lc_replacement_d2_100'], 'func': lc_replacement_d3_100}


def lc_replacement_d3_101(lc_replacement_d2_101):
    feature = _clean(lc_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_101'] = {'inputs': ['lc_replacement_d2_101'], 'func': lc_replacement_d3_101}


def lc_replacement_d3_102(lc_replacement_d2_102):
    feature = _clean(lc_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_102'] = {'inputs': ['lc_replacement_d2_102'], 'func': lc_replacement_d3_102}


def lc_replacement_d3_103(lc_replacement_d2_103):
    feature = _clean(lc_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_103'] = {'inputs': ['lc_replacement_d2_103'], 'func': lc_replacement_d3_103}


def lc_replacement_d3_104(lc_replacement_d2_104):
    feature = _clean(lc_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_104'] = {'inputs': ['lc_replacement_d2_104'], 'func': lc_replacement_d3_104}


def lc_replacement_d3_105(lc_replacement_d2_105):
    feature = _clean(lc_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_105'] = {'inputs': ['lc_replacement_d2_105'], 'func': lc_replacement_d3_105}


def lc_replacement_d3_106(lc_replacement_d2_106):
    feature = _clean(lc_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_106'] = {'inputs': ['lc_replacement_d2_106'], 'func': lc_replacement_d3_106}


def lc_replacement_d3_107(lc_replacement_d2_107):
    feature = _clean(lc_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_107'] = {'inputs': ['lc_replacement_d2_107'], 'func': lc_replacement_d3_107}


def lc_replacement_d3_108(lc_replacement_d2_108):
    feature = _clean(lc_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_108'] = {'inputs': ['lc_replacement_d2_108'], 'func': lc_replacement_d3_108}


def lc_replacement_d3_109(lc_replacement_d2_109):
    feature = _clean(lc_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_109'] = {'inputs': ['lc_replacement_d2_109'], 'func': lc_replacement_d3_109}


def lc_replacement_d3_110(lc_replacement_d2_110):
    feature = _clean(lc_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_110'] = {'inputs': ['lc_replacement_d2_110'], 'func': lc_replacement_d3_110}


def lc_replacement_d3_111(lc_replacement_d2_111):
    feature = _clean(lc_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_111'] = {'inputs': ['lc_replacement_d2_111'], 'func': lc_replacement_d3_111}


def lc_replacement_d3_112(lc_replacement_d2_112):
    feature = _clean(lc_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_112'] = {'inputs': ['lc_replacement_d2_112'], 'func': lc_replacement_d3_112}


def lc_replacement_d3_113(lc_replacement_d2_113):
    feature = _clean(lc_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_113'] = {'inputs': ['lc_replacement_d2_113'], 'func': lc_replacement_d3_113}


def lc_replacement_d3_114(lc_replacement_d2_114):
    feature = _clean(lc_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_114'] = {'inputs': ['lc_replacement_d2_114'], 'func': lc_replacement_d3_114}


def lc_replacement_d3_115(lc_replacement_d2_115):
    feature = _clean(lc_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_115'] = {'inputs': ['lc_replacement_d2_115'], 'func': lc_replacement_d3_115}


def lc_replacement_d3_116(lc_replacement_d2_116):
    feature = _clean(lc_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_116'] = {'inputs': ['lc_replacement_d2_116'], 'func': lc_replacement_d3_116}


def lc_replacement_d3_117(lc_replacement_d2_117):
    feature = _clean(lc_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_117'] = {'inputs': ['lc_replacement_d2_117'], 'func': lc_replacement_d3_117}


def lc_replacement_d3_118(lc_replacement_d2_118):
    feature = _clean(lc_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_118'] = {'inputs': ['lc_replacement_d2_118'], 'func': lc_replacement_d3_118}


def lc_replacement_d3_119(lc_replacement_d2_119):
    feature = _clean(lc_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_119'] = {'inputs': ['lc_replacement_d2_119'], 'func': lc_replacement_d3_119}


def lc_replacement_d3_120(lc_replacement_d2_120):
    feature = _clean(lc_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_120'] = {'inputs': ['lc_replacement_d2_120'], 'func': lc_replacement_d3_120}


def lc_replacement_d3_121(lc_replacement_d2_121):
    feature = _clean(lc_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_121'] = {'inputs': ['lc_replacement_d2_121'], 'func': lc_replacement_d3_121}


def lc_replacement_d3_122(lc_replacement_d2_122):
    feature = _clean(lc_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_122'] = {'inputs': ['lc_replacement_d2_122'], 'func': lc_replacement_d3_122}


def lc_replacement_d3_123(lc_replacement_d2_123):
    feature = _clean(lc_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_123'] = {'inputs': ['lc_replacement_d2_123'], 'func': lc_replacement_d3_123}


def lc_replacement_d3_124(lc_replacement_d2_124):
    feature = _clean(lc_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_124'] = {'inputs': ['lc_replacement_d2_124'], 'func': lc_replacement_d3_124}


def lc_replacement_d3_125(lc_replacement_d2_125):
    feature = _clean(lc_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_125'] = {'inputs': ['lc_replacement_d2_125'], 'func': lc_replacement_d3_125}


def lc_replacement_d3_126(lc_replacement_d2_126):
    feature = _clean(lc_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_126'] = {'inputs': ['lc_replacement_d2_126'], 'func': lc_replacement_d3_126}


def lc_replacement_d3_127(lc_replacement_d2_127):
    feature = _clean(lc_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_127'] = {'inputs': ['lc_replacement_d2_127'], 'func': lc_replacement_d3_127}


def lc_replacement_d3_128(lc_replacement_d2_128):
    feature = _clean(lc_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_128'] = {'inputs': ['lc_replacement_d2_128'], 'func': lc_replacement_d3_128}


def lc_replacement_d3_129(lc_replacement_d2_129):
    feature = _clean(lc_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_129'] = {'inputs': ['lc_replacement_d2_129'], 'func': lc_replacement_d3_129}


def lc_replacement_d3_130(lc_replacement_d2_130):
    feature = _clean(lc_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_130'] = {'inputs': ['lc_replacement_d2_130'], 'func': lc_replacement_d3_130}


def lc_replacement_d3_131(lc_replacement_d2_131):
    feature = _clean(lc_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_131'] = {'inputs': ['lc_replacement_d2_131'], 'func': lc_replacement_d3_131}


def lc_replacement_d3_132(lc_replacement_d2_132):
    feature = _clean(lc_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_132'] = {'inputs': ['lc_replacement_d2_132'], 'func': lc_replacement_d3_132}


def lc_replacement_d3_133(lc_replacement_d2_133):
    feature = _clean(lc_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_133'] = {'inputs': ['lc_replacement_d2_133'], 'func': lc_replacement_d3_133}


def lc_replacement_d3_134(lc_replacement_d2_134):
    feature = _clean(lc_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_134'] = {'inputs': ['lc_replacement_d2_134'], 'func': lc_replacement_d3_134}


def lc_replacement_d3_135(lc_replacement_d2_135):
    feature = _clean(lc_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_135'] = {'inputs': ['lc_replacement_d2_135'], 'func': lc_replacement_d3_135}


def lc_replacement_d3_136(lc_replacement_d2_136):
    feature = _clean(lc_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_136'] = {'inputs': ['lc_replacement_d2_136'], 'func': lc_replacement_d3_136}


def lc_replacement_d3_137(lc_replacement_d2_137):
    feature = _clean(lc_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_137'] = {'inputs': ['lc_replacement_d2_137'], 'func': lc_replacement_d3_137}


def lc_replacement_d3_138(lc_replacement_d2_138):
    feature = _clean(lc_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_138'] = {'inputs': ['lc_replacement_d2_138'], 'func': lc_replacement_d3_138}


def lc_replacement_d3_139(lc_replacement_d2_139):
    feature = _clean(lc_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_139'] = {'inputs': ['lc_replacement_d2_139'], 'func': lc_replacement_d3_139}


def lc_replacement_d3_140(lc_replacement_d2_140):
    feature = _clean(lc_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_140'] = {'inputs': ['lc_replacement_d2_140'], 'func': lc_replacement_d3_140}


def lc_replacement_d3_141(lc_replacement_d2_141):
    feature = _clean(lc_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_141'] = {'inputs': ['lc_replacement_d2_141'], 'func': lc_replacement_d3_141}


def lc_replacement_d3_142(lc_replacement_d2_142):
    feature = _clean(lc_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_142'] = {'inputs': ['lc_replacement_d2_142'], 'func': lc_replacement_d3_142}


def lc_replacement_d3_143(lc_replacement_d2_143):
    feature = _clean(lc_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_143'] = {'inputs': ['lc_replacement_d2_143'], 'func': lc_replacement_d3_143}


def lc_replacement_d3_144(lc_replacement_d2_144):
    feature = _clean(lc_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_144'] = {'inputs': ['lc_replacement_d2_144'], 'func': lc_replacement_d3_144}


def lc_replacement_d3_145(lc_replacement_d2_145):
    feature = _clean(lc_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_145'] = {'inputs': ['lc_replacement_d2_145'], 'func': lc_replacement_d3_145}


def lc_replacement_d3_146(lc_replacement_d2_146):
    feature = _clean(lc_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_146'] = {'inputs': ['lc_replacement_d2_146'], 'func': lc_replacement_d3_146}


def lc_replacement_d3_147(lc_replacement_d2_147):
    feature = _clean(lc_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_147'] = {'inputs': ['lc_replacement_d2_147'], 'func': lc_replacement_d3_147}


def lc_replacement_d3_148(lc_replacement_d2_148):
    feature = _clean(lc_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_148'] = {'inputs': ['lc_replacement_d2_148'], 'func': lc_replacement_d3_148}


def lc_replacement_d3_149(lc_replacement_d2_149):
    feature = _clean(lc_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_149'] = {'inputs': ['lc_replacement_d2_149'], 'func': lc_replacement_d3_149}


def lc_replacement_d3_150(lc_replacement_d2_150):
    feature = _clean(lc_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_150'] = {'inputs': ['lc_replacement_d2_150'], 'func': lc_replacement_d3_150}


def lc_replacement_d3_151(lc_replacement_d2_151):
    feature = _clean(lc_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_151'] = {'inputs': ['lc_replacement_d2_151'], 'func': lc_replacement_d3_151}


def lc_replacement_d3_152(lc_replacement_d2_152):
    feature = _clean(lc_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_152'] = {'inputs': ['lc_replacement_d2_152'], 'func': lc_replacement_d3_152}


def lc_replacement_d3_153(lc_replacement_d2_153):
    feature = _clean(lc_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_153'] = {'inputs': ['lc_replacement_d2_153'], 'func': lc_replacement_d3_153}


def lc_replacement_d3_154(lc_replacement_d2_154):
    feature = _clean(lc_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_154'] = {'inputs': ['lc_replacement_d2_154'], 'func': lc_replacement_d3_154}


def lc_replacement_d3_155(lc_replacement_d2_155):
    feature = _clean(lc_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_155'] = {'inputs': ['lc_replacement_d2_155'], 'func': lc_replacement_d3_155}


def lc_replacement_d3_156(lc_replacement_d2_156):
    feature = _clean(lc_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_156'] = {'inputs': ['lc_replacement_d2_156'], 'func': lc_replacement_d3_156}


def lc_replacement_d3_157(lc_replacement_d2_157):
    feature = _clean(lc_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_157'] = {'inputs': ['lc_replacement_d2_157'], 'func': lc_replacement_d3_157}


def lc_replacement_d3_158(lc_replacement_d2_158):
    feature = _clean(lc_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_158'] = {'inputs': ['lc_replacement_d2_158'], 'func': lc_replacement_d3_158}


def lc_replacement_d3_159(lc_replacement_d2_159):
    feature = _clean(lc_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_159'] = {'inputs': ['lc_replacement_d2_159'], 'func': lc_replacement_d3_159}


def lc_replacement_d3_160(lc_replacement_d2_160):
    feature = _clean(lc_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_160'] = {'inputs': ['lc_replacement_d2_160'], 'func': lc_replacement_d3_160}


def lc_replacement_d3_161(lc_replacement_d2_161):
    feature = _clean(lc_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_161'] = {'inputs': ['lc_replacement_d2_161'], 'func': lc_replacement_d3_161}


def lc_replacement_d3_162(lc_replacement_d2_162):
    feature = _clean(lc_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_162'] = {'inputs': ['lc_replacement_d2_162'], 'func': lc_replacement_d3_162}


def lc_replacement_d3_163(lc_replacement_d2_163):
    feature = _clean(lc_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_163'] = {'inputs': ['lc_replacement_d2_163'], 'func': lc_replacement_d3_163}


def lc_replacement_d3_164(lc_replacement_d2_164):
    feature = _clean(lc_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_164'] = {'inputs': ['lc_replacement_d2_164'], 'func': lc_replacement_d3_164}


def lc_replacement_d3_165(lc_replacement_d2_165):
    feature = _clean(lc_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_165'] = {'inputs': ['lc_replacement_d2_165'], 'func': lc_replacement_d3_165}


def lc_replacement_d3_166(lc_replacement_d2_166):
    feature = _clean(lc_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_166'] = {'inputs': ['lc_replacement_d2_166'], 'func': lc_replacement_d3_166}


def lc_replacement_d3_167(lc_replacement_d2_167):
    feature = _clean(lc_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_167'] = {'inputs': ['lc_replacement_d2_167'], 'func': lc_replacement_d3_167}


def lc_replacement_d3_168(lc_replacement_d2_168):
    feature = _clean(lc_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_168'] = {'inputs': ['lc_replacement_d2_168'], 'func': lc_replacement_d3_168}


def lc_replacement_d3_169(lc_replacement_d2_169):
    feature = _clean(lc_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_169'] = {'inputs': ['lc_replacement_d2_169'], 'func': lc_replacement_d3_169}


def lc_replacement_d3_170(lc_replacement_d2_170):
    feature = _clean(lc_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
LC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lc_replacement_d3_170'] = {'inputs': ['lc_replacement_d2_170'], 'func': lc_replacement_d3_170}


# Third-derivative extensions for repaired first-base features.
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def lqc_base_universe_d3_001_lqc_002_zero_volume_frequency_10_002(lqc_base_universe_d2_001_lqc_002_zero_volume_frequency_10_002):
    return _base_universe_d3(lqc_base_universe_d2_001_lqc_002_zero_volume_frequency_10_002, 1)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_001_lqc_002_zero_volume_frequency_10_002'] = {'inputs': ['lqc_base_universe_d2_001_lqc_002_zero_volume_frequency_10_002'], 'func': lqc_base_universe_d3_001_lqc_002_zero_volume_frequency_10_002}


def lqc_base_universe_d3_002_lqc_003_spread_proxy_21_003(lqc_base_universe_d2_002_lqc_003_spread_proxy_21_003):
    return _base_universe_d3(lqc_base_universe_d2_002_lqc_003_spread_proxy_21_003, 2)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_002_lqc_003_spread_proxy_21_003'] = {'inputs': ['lqc_base_universe_d2_002_lqc_003_spread_proxy_21_003'], 'func': lqc_base_universe_d3_002_lqc_003_spread_proxy_21_003}


def lqc_base_universe_d3_003_lqc_004_trading_intensity_42_004(lqc_base_universe_d2_003_lqc_004_trading_intensity_42_004):
    return _base_universe_d3(lqc_base_universe_d2_003_lqc_004_trading_intensity_42_004, 3)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_003_lqc_004_trading_intensity_42_004'] = {'inputs': ['lqc_base_universe_d2_003_lqc_004_trading_intensity_42_004'], 'func': lqc_base_universe_d3_003_lqc_004_trading_intensity_42_004}


def lqc_base_universe_d3_004_lqc_006_price_level_distress_84_006(lqc_base_universe_d2_004_lqc_006_price_level_distress_84_006):
    return _base_universe_d3(lqc_base_universe_d2_004_lqc_006_price_level_distress_84_006, 4)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_004_lqc_006_price_level_distress_84_006'] = {'inputs': ['lqc_base_universe_d2_004_lqc_006_price_level_distress_84_006'], 'func': lqc_base_universe_d3_004_lqc_006_price_level_distress_84_006}


def lqc_base_universe_d3_005_lqc_008_zero_volume_frequency_189_008(lqc_base_universe_d2_005_lqc_008_zero_volume_frequency_189_008):
    return _base_universe_d3(lqc_base_universe_d2_005_lqc_008_zero_volume_frequency_189_008, 5)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_005_lqc_008_zero_volume_frequency_189_008'] = {'inputs': ['lqc_base_universe_d2_005_lqc_008_zero_volume_frequency_189_008'], 'func': lqc_base_universe_d3_005_lqc_008_zero_volume_frequency_189_008}


def lqc_base_universe_d3_006_lqc_009_spread_proxy_252_009(lqc_base_universe_d2_006_lqc_009_spread_proxy_252_009):
    return _base_universe_d3(lqc_base_universe_d2_006_lqc_009_spread_proxy_252_009, 6)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_006_lqc_009_spread_proxy_252_009'] = {'inputs': ['lqc_base_universe_d2_006_lqc_009_spread_proxy_252_009'], 'func': lqc_base_universe_d3_006_lqc_009_spread_proxy_252_009}


def lqc_base_universe_d3_007_lqc_010_trading_intensity_378_010(lqc_base_universe_d2_007_lqc_010_trading_intensity_378_010):
    return _base_universe_d3(lqc_base_universe_d2_007_lqc_010_trading_intensity_378_010, 7)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_007_lqc_010_trading_intensity_378_010'] = {'inputs': ['lqc_base_universe_d2_007_lqc_010_trading_intensity_378_010'], 'func': lqc_base_universe_d3_007_lqc_010_trading_intensity_378_010}


def lqc_base_universe_d3_008_lqc_012_price_level_distress_756_012(lqc_base_universe_d2_008_lqc_012_price_level_distress_756_012):
    return _base_universe_d3(lqc_base_universe_d2_008_lqc_012_price_level_distress_756_012, 8)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_008_lqc_012_price_level_distress_756_012'] = {'inputs': ['lqc_base_universe_d2_008_lqc_012_price_level_distress_756_012'], 'func': lqc_base_universe_d3_008_lqc_012_price_level_distress_756_012}


def lqc_base_universe_d3_009_lqc_014_zero_volume_frequency_1260_014(lqc_base_universe_d2_009_lqc_014_zero_volume_frequency_1260_014):
    return _base_universe_d3(lqc_base_universe_d2_009_lqc_014_zero_volume_frequency_1260_014, 9)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_009_lqc_014_zero_volume_frequency_1260_014'] = {'inputs': ['lqc_base_universe_d2_009_lqc_014_zero_volume_frequency_1260_014'], 'func': lqc_base_universe_d3_009_lqc_014_zero_volume_frequency_1260_014}


def lqc_base_universe_d3_010_lqc_015_spread_proxy_1512_015(lqc_base_universe_d2_010_lqc_015_spread_proxy_1512_015):
    return _base_universe_d3(lqc_base_universe_d2_010_lqc_015_spread_proxy_1512_015, 10)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_010_lqc_015_spread_proxy_1512_015'] = {'inputs': ['lqc_base_universe_d2_010_lqc_015_spread_proxy_1512_015'], 'func': lqc_base_universe_d3_010_lqc_015_spread_proxy_1512_015}


def lqc_base_universe_d3_011_lqc_016_trading_intensity_5_016(lqc_base_universe_d2_011_lqc_016_trading_intensity_5_016):
    return _base_universe_d3(lqc_base_universe_d2_011_lqc_016_trading_intensity_5_016, 11)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_011_lqc_016_trading_intensity_5_016'] = {'inputs': ['lqc_base_universe_d2_011_lqc_016_trading_intensity_5_016'], 'func': lqc_base_universe_d3_011_lqc_016_trading_intensity_5_016}


def lqc_base_universe_d3_012_lqc_018_price_level_distress_21_018(lqc_base_universe_d2_012_lqc_018_price_level_distress_21_018):
    return _base_universe_d3(lqc_base_universe_d2_012_lqc_018_price_level_distress_21_018, 12)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_012_lqc_018_price_level_distress_21_018'] = {'inputs': ['lqc_base_universe_d2_012_lqc_018_price_level_distress_21_018'], 'func': lqc_base_universe_d3_012_lqc_018_price_level_distress_21_018}


def lqc_base_universe_d3_013_lqc_020_zero_volume_frequency_63_020(lqc_base_universe_d2_013_lqc_020_zero_volume_frequency_63_020):
    return _base_universe_d3(lqc_base_universe_d2_013_lqc_020_zero_volume_frequency_63_020, 13)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_013_lqc_020_zero_volume_frequency_63_020'] = {'inputs': ['lqc_base_universe_d2_013_lqc_020_zero_volume_frequency_63_020'], 'func': lqc_base_universe_d3_013_lqc_020_zero_volume_frequency_63_020}


def lqc_base_universe_d3_014_lqc_021_spread_proxy_84_021(lqc_base_universe_d2_014_lqc_021_spread_proxy_84_021):
    return _base_universe_d3(lqc_base_universe_d2_014_lqc_021_spread_proxy_84_021, 14)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_014_lqc_021_spread_proxy_84_021'] = {'inputs': ['lqc_base_universe_d2_014_lqc_021_spread_proxy_84_021'], 'func': lqc_base_universe_d3_014_lqc_021_spread_proxy_84_021}


def lqc_base_universe_d3_015_lqc_022_trading_intensity_126_022(lqc_base_universe_d2_015_lqc_022_trading_intensity_126_022):
    return _base_universe_d3(lqc_base_universe_d2_015_lqc_022_trading_intensity_126_022, 15)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_015_lqc_022_trading_intensity_126_022'] = {'inputs': ['lqc_base_universe_d2_015_lqc_022_trading_intensity_126_022'], 'func': lqc_base_universe_d3_015_lqc_022_trading_intensity_126_022}


def lqc_base_universe_d3_016_lqc_024_price_level_distress_252_024(lqc_base_universe_d2_016_lqc_024_price_level_distress_252_024):
    return _base_universe_d3(lqc_base_universe_d2_016_lqc_024_price_level_distress_252_024, 16)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_016_lqc_024_price_level_distress_252_024'] = {'inputs': ['lqc_base_universe_d2_016_lqc_024_price_level_distress_252_024'], 'func': lqc_base_universe_d3_016_lqc_024_price_level_distress_252_024}


def lqc_base_universe_d3_017_lqc_026_zero_volume_frequency_504_026(lqc_base_universe_d2_017_lqc_026_zero_volume_frequency_504_026):
    return _base_universe_d3(lqc_base_universe_d2_017_lqc_026_zero_volume_frequency_504_026, 17)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_017_lqc_026_zero_volume_frequency_504_026'] = {'inputs': ['lqc_base_universe_d2_017_lqc_026_zero_volume_frequency_504_026'], 'func': lqc_base_universe_d3_017_lqc_026_zero_volume_frequency_504_026}


def lqc_base_universe_d3_018_lqc_027_spread_proxy_756_027(lqc_base_universe_d2_018_lqc_027_spread_proxy_756_027):
    return _base_universe_d3(lqc_base_universe_d2_018_lqc_027_spread_proxy_756_027, 18)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_018_lqc_027_spread_proxy_756_027'] = {'inputs': ['lqc_base_universe_d2_018_lqc_027_spread_proxy_756_027'], 'func': lqc_base_universe_d3_018_lqc_027_spread_proxy_756_027}


def lqc_base_universe_d3_019_lqc_028_trading_intensity_1008_028(lqc_base_universe_d2_019_lqc_028_trading_intensity_1008_028):
    return _base_universe_d3(lqc_base_universe_d2_019_lqc_028_trading_intensity_1008_028, 19)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_019_lqc_028_trading_intensity_1008_028'] = {'inputs': ['lqc_base_universe_d2_019_lqc_028_trading_intensity_1008_028'], 'func': lqc_base_universe_d3_019_lqc_028_trading_intensity_1008_028}


def lqc_base_universe_d3_020_lqc_030_price_level_distress_1512_030(lqc_base_universe_d2_020_lqc_030_price_level_distress_1512_030):
    return _base_universe_d3(lqc_base_universe_d2_020_lqc_030_price_level_distress_1512_030, 20)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_020_lqc_030_price_level_distress_1512_030'] = {'inputs': ['lqc_base_universe_d2_020_lqc_030_price_level_distress_1512_030'], 'func': lqc_base_universe_d3_020_lqc_030_price_level_distress_1512_030}


def lqc_base_universe_d3_021_lqc_basefill_001(lqc_base_universe_d2_021_lqc_basefill_001):
    return _base_universe_d3(lqc_base_universe_d2_021_lqc_basefill_001, 21)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_021_lqc_basefill_001'] = {'inputs': ['lqc_base_universe_d2_021_lqc_basefill_001'], 'func': lqc_base_universe_d3_021_lqc_basefill_001}


def lqc_base_universe_d3_022_lqc_basefill_005(lqc_base_universe_d2_022_lqc_basefill_005):
    return _base_universe_d3(lqc_base_universe_d2_022_lqc_basefill_005, 22)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_022_lqc_basefill_005'] = {'inputs': ['lqc_base_universe_d2_022_lqc_basefill_005'], 'func': lqc_base_universe_d3_022_lqc_basefill_005}


def lqc_base_universe_d3_023_lqc_basefill_007(lqc_base_universe_d2_023_lqc_basefill_007):
    return _base_universe_d3(lqc_base_universe_d2_023_lqc_basefill_007, 23)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_023_lqc_basefill_007'] = {'inputs': ['lqc_base_universe_d2_023_lqc_basefill_007'], 'func': lqc_base_universe_d3_023_lqc_basefill_007}


def lqc_base_universe_d3_024_lqc_basefill_011(lqc_base_universe_d2_024_lqc_basefill_011):
    return _base_universe_d3(lqc_base_universe_d2_024_lqc_basefill_011, 24)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_024_lqc_basefill_011'] = {'inputs': ['lqc_base_universe_d2_024_lqc_basefill_011'], 'func': lqc_base_universe_d3_024_lqc_basefill_011}


def lqc_base_universe_d3_025_lqc_basefill_013(lqc_base_universe_d2_025_lqc_basefill_013):
    return _base_universe_d3(lqc_base_universe_d2_025_lqc_basefill_013, 25)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_025_lqc_basefill_013'] = {'inputs': ['lqc_base_universe_d2_025_lqc_basefill_013'], 'func': lqc_base_universe_d3_025_lqc_basefill_013}


def lqc_base_universe_d3_026_lqc_basefill_017(lqc_base_universe_d2_026_lqc_basefill_017):
    return _base_universe_d3(lqc_base_universe_d2_026_lqc_basefill_017, 26)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_026_lqc_basefill_017'] = {'inputs': ['lqc_base_universe_d2_026_lqc_basefill_017'], 'func': lqc_base_universe_d3_026_lqc_basefill_017}


def lqc_base_universe_d3_027_lqc_basefill_019(lqc_base_universe_d2_027_lqc_basefill_019):
    return _base_universe_d3(lqc_base_universe_d2_027_lqc_basefill_019, 27)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_027_lqc_basefill_019'] = {'inputs': ['lqc_base_universe_d2_027_lqc_basefill_019'], 'func': lqc_base_universe_d3_027_lqc_basefill_019}


def lqc_base_universe_d3_028_lqc_basefill_023(lqc_base_universe_d2_028_lqc_basefill_023):
    return _base_universe_d3(lqc_base_universe_d2_028_lqc_basefill_023, 28)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_028_lqc_basefill_023'] = {'inputs': ['lqc_base_universe_d2_028_lqc_basefill_023'], 'func': lqc_base_universe_d3_028_lqc_basefill_023}


def lqc_base_universe_d3_029_lqc_basefill_025(lqc_base_universe_d2_029_lqc_basefill_025):
    return _base_universe_d3(lqc_base_universe_d2_029_lqc_basefill_025, 29)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_029_lqc_basefill_025'] = {'inputs': ['lqc_base_universe_d2_029_lqc_basefill_025'], 'func': lqc_base_universe_d3_029_lqc_basefill_025}


def lqc_base_universe_d3_030_lqc_basefill_029(lqc_base_universe_d2_030_lqc_basefill_029):
    return _base_universe_d3(lqc_base_universe_d2_030_lqc_basefill_029, 30)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_030_lqc_basefill_029'] = {'inputs': ['lqc_base_universe_d2_030_lqc_basefill_029'], 'func': lqc_base_universe_d3_030_lqc_basefill_029}


def lqc_base_universe_d3_031_lqc_basefill_031(lqc_base_universe_d2_031_lqc_basefill_031):
    return _base_universe_d3(lqc_base_universe_d2_031_lqc_basefill_031, 31)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_031_lqc_basefill_031'] = {'inputs': ['lqc_base_universe_d2_031_lqc_basefill_031'], 'func': lqc_base_universe_d3_031_lqc_basefill_031}


def lqc_base_universe_d3_032_lqc_basefill_032(lqc_base_universe_d2_032_lqc_basefill_032):
    return _base_universe_d3(lqc_base_universe_d2_032_lqc_basefill_032, 32)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_032_lqc_basefill_032'] = {'inputs': ['lqc_base_universe_d2_032_lqc_basefill_032'], 'func': lqc_base_universe_d3_032_lqc_basefill_032}


def lqc_base_universe_d3_033_lqc_basefill_033(lqc_base_universe_d2_033_lqc_basefill_033):
    return _base_universe_d3(lqc_base_universe_d2_033_lqc_basefill_033, 33)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_033_lqc_basefill_033'] = {'inputs': ['lqc_base_universe_d2_033_lqc_basefill_033'], 'func': lqc_base_universe_d3_033_lqc_basefill_033}


def lqc_base_universe_d3_034_lqc_basefill_034(lqc_base_universe_d2_034_lqc_basefill_034):
    return _base_universe_d3(lqc_base_universe_d2_034_lqc_basefill_034, 34)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_034_lqc_basefill_034'] = {'inputs': ['lqc_base_universe_d2_034_lqc_basefill_034'], 'func': lqc_base_universe_d3_034_lqc_basefill_034}


def lqc_base_universe_d3_035_lqc_basefill_035(lqc_base_universe_d2_035_lqc_basefill_035):
    return _base_universe_d3(lqc_base_universe_d2_035_lqc_basefill_035, 35)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_035_lqc_basefill_035'] = {'inputs': ['lqc_base_universe_d2_035_lqc_basefill_035'], 'func': lqc_base_universe_d3_035_lqc_basefill_035}


def lqc_base_universe_d3_036_lqc_basefill_036(lqc_base_universe_d2_036_lqc_basefill_036):
    return _base_universe_d3(lqc_base_universe_d2_036_lqc_basefill_036, 36)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_036_lqc_basefill_036'] = {'inputs': ['lqc_base_universe_d2_036_lqc_basefill_036'], 'func': lqc_base_universe_d3_036_lqc_basefill_036}


def lqc_base_universe_d3_037_lqc_basefill_037(lqc_base_universe_d2_037_lqc_basefill_037):
    return _base_universe_d3(lqc_base_universe_d2_037_lqc_basefill_037, 37)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_037_lqc_basefill_037'] = {'inputs': ['lqc_base_universe_d2_037_lqc_basefill_037'], 'func': lqc_base_universe_d3_037_lqc_basefill_037}


def lqc_base_universe_d3_038_lqc_basefill_038(lqc_base_universe_d2_038_lqc_basefill_038):
    return _base_universe_d3(lqc_base_universe_d2_038_lqc_basefill_038, 38)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_038_lqc_basefill_038'] = {'inputs': ['lqc_base_universe_d2_038_lqc_basefill_038'], 'func': lqc_base_universe_d3_038_lqc_basefill_038}


def lqc_base_universe_d3_039_lqc_basefill_039(lqc_base_universe_d2_039_lqc_basefill_039):
    return _base_universe_d3(lqc_base_universe_d2_039_lqc_basefill_039, 39)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_039_lqc_basefill_039'] = {'inputs': ['lqc_base_universe_d2_039_lqc_basefill_039'], 'func': lqc_base_universe_d3_039_lqc_basefill_039}


def lqc_base_universe_d3_040_lqc_basefill_040(lqc_base_universe_d2_040_lqc_basefill_040):
    return _base_universe_d3(lqc_base_universe_d2_040_lqc_basefill_040, 40)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_040_lqc_basefill_040'] = {'inputs': ['lqc_base_universe_d2_040_lqc_basefill_040'], 'func': lqc_base_universe_d3_040_lqc_basefill_040}


def lqc_base_universe_d3_041_lqc_basefill_041(lqc_base_universe_d2_041_lqc_basefill_041):
    return _base_universe_d3(lqc_base_universe_d2_041_lqc_basefill_041, 41)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_041_lqc_basefill_041'] = {'inputs': ['lqc_base_universe_d2_041_lqc_basefill_041'], 'func': lqc_base_universe_d3_041_lqc_basefill_041}


def lqc_base_universe_d3_042_lqc_basefill_042(lqc_base_universe_d2_042_lqc_basefill_042):
    return _base_universe_d3(lqc_base_universe_d2_042_lqc_basefill_042, 42)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_042_lqc_basefill_042'] = {'inputs': ['lqc_base_universe_d2_042_lqc_basefill_042'], 'func': lqc_base_universe_d3_042_lqc_basefill_042}


def lqc_base_universe_d3_043_lqc_basefill_043(lqc_base_universe_d2_043_lqc_basefill_043):
    return _base_universe_d3(lqc_base_universe_d2_043_lqc_basefill_043, 43)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_043_lqc_basefill_043'] = {'inputs': ['lqc_base_universe_d2_043_lqc_basefill_043'], 'func': lqc_base_universe_d3_043_lqc_basefill_043}


def lqc_base_universe_d3_044_lqc_basefill_044(lqc_base_universe_d2_044_lqc_basefill_044):
    return _base_universe_d3(lqc_base_universe_d2_044_lqc_basefill_044, 44)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_044_lqc_basefill_044'] = {'inputs': ['lqc_base_universe_d2_044_lqc_basefill_044'], 'func': lqc_base_universe_d3_044_lqc_basefill_044}


def lqc_base_universe_d3_045_lqc_basefill_045(lqc_base_universe_d2_045_lqc_basefill_045):
    return _base_universe_d3(lqc_base_universe_d2_045_lqc_basefill_045, 45)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_045_lqc_basefill_045'] = {'inputs': ['lqc_base_universe_d2_045_lqc_basefill_045'], 'func': lqc_base_universe_d3_045_lqc_basefill_045}


def lqc_base_universe_d3_046_lqc_basefill_046(lqc_base_universe_d2_046_lqc_basefill_046):
    return _base_universe_d3(lqc_base_universe_d2_046_lqc_basefill_046, 46)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_046_lqc_basefill_046'] = {'inputs': ['lqc_base_universe_d2_046_lqc_basefill_046'], 'func': lqc_base_universe_d3_046_lqc_basefill_046}


def lqc_base_universe_d3_047_lqc_basefill_047(lqc_base_universe_d2_047_lqc_basefill_047):
    return _base_universe_d3(lqc_base_universe_d2_047_lqc_basefill_047, 47)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_047_lqc_basefill_047'] = {'inputs': ['lqc_base_universe_d2_047_lqc_basefill_047'], 'func': lqc_base_universe_d3_047_lqc_basefill_047}


def lqc_base_universe_d3_048_lqc_basefill_048(lqc_base_universe_d2_048_lqc_basefill_048):
    return _base_universe_d3(lqc_base_universe_d2_048_lqc_basefill_048, 48)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_048_lqc_basefill_048'] = {'inputs': ['lqc_base_universe_d2_048_lqc_basefill_048'], 'func': lqc_base_universe_d3_048_lqc_basefill_048}


def lqc_base_universe_d3_049_lqc_basefill_049(lqc_base_universe_d2_049_lqc_basefill_049):
    return _base_universe_d3(lqc_base_universe_d2_049_lqc_basefill_049, 49)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_049_lqc_basefill_049'] = {'inputs': ['lqc_base_universe_d2_049_lqc_basefill_049'], 'func': lqc_base_universe_d3_049_lqc_basefill_049}


def lqc_base_universe_d3_050_lqc_basefill_050(lqc_base_universe_d2_050_lqc_basefill_050):
    return _base_universe_d3(lqc_base_universe_d2_050_lqc_basefill_050, 50)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_050_lqc_basefill_050'] = {'inputs': ['lqc_base_universe_d2_050_lqc_basefill_050'], 'func': lqc_base_universe_d3_050_lqc_basefill_050}


def lqc_base_universe_d3_051_lqc_basefill_051(lqc_base_universe_d2_051_lqc_basefill_051):
    return _base_universe_d3(lqc_base_universe_d2_051_lqc_basefill_051, 51)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_051_lqc_basefill_051'] = {'inputs': ['lqc_base_universe_d2_051_lqc_basefill_051'], 'func': lqc_base_universe_d3_051_lqc_basefill_051}


def lqc_base_universe_d3_052_lqc_basefill_052(lqc_base_universe_d2_052_lqc_basefill_052):
    return _base_universe_d3(lqc_base_universe_d2_052_lqc_basefill_052, 52)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_052_lqc_basefill_052'] = {'inputs': ['lqc_base_universe_d2_052_lqc_basefill_052'], 'func': lqc_base_universe_d3_052_lqc_basefill_052}


def lqc_base_universe_d3_053_lqc_basefill_053(lqc_base_universe_d2_053_lqc_basefill_053):
    return _base_universe_d3(lqc_base_universe_d2_053_lqc_basefill_053, 53)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_053_lqc_basefill_053'] = {'inputs': ['lqc_base_universe_d2_053_lqc_basefill_053'], 'func': lqc_base_universe_d3_053_lqc_basefill_053}


def lqc_base_universe_d3_054_lqc_basefill_054(lqc_base_universe_d2_054_lqc_basefill_054):
    return _base_universe_d3(lqc_base_universe_d2_054_lqc_basefill_054, 54)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_054_lqc_basefill_054'] = {'inputs': ['lqc_base_universe_d2_054_lqc_basefill_054'], 'func': lqc_base_universe_d3_054_lqc_basefill_054}


def lqc_base_universe_d3_055_lqc_basefill_055(lqc_base_universe_d2_055_lqc_basefill_055):
    return _base_universe_d3(lqc_base_universe_d2_055_lqc_basefill_055, 55)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_055_lqc_basefill_055'] = {'inputs': ['lqc_base_universe_d2_055_lqc_basefill_055'], 'func': lqc_base_universe_d3_055_lqc_basefill_055}


def lqc_base_universe_d3_056_lqc_basefill_056(lqc_base_universe_d2_056_lqc_basefill_056):
    return _base_universe_d3(lqc_base_universe_d2_056_lqc_basefill_056, 56)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_056_lqc_basefill_056'] = {'inputs': ['lqc_base_universe_d2_056_lqc_basefill_056'], 'func': lqc_base_universe_d3_056_lqc_basefill_056}


def lqc_base_universe_d3_057_lqc_basefill_057(lqc_base_universe_d2_057_lqc_basefill_057):
    return _base_universe_d3(lqc_base_universe_d2_057_lqc_basefill_057, 57)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_057_lqc_basefill_057'] = {'inputs': ['lqc_base_universe_d2_057_lqc_basefill_057'], 'func': lqc_base_universe_d3_057_lqc_basefill_057}


def lqc_base_universe_d3_058_lqc_basefill_058(lqc_base_universe_d2_058_lqc_basefill_058):
    return _base_universe_d3(lqc_base_universe_d2_058_lqc_basefill_058, 58)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_058_lqc_basefill_058'] = {'inputs': ['lqc_base_universe_d2_058_lqc_basefill_058'], 'func': lqc_base_universe_d3_058_lqc_basefill_058}


def lqc_base_universe_d3_059_lqc_basefill_059(lqc_base_universe_d2_059_lqc_basefill_059):
    return _base_universe_d3(lqc_base_universe_d2_059_lqc_basefill_059, 59)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_059_lqc_basefill_059'] = {'inputs': ['lqc_base_universe_d2_059_lqc_basefill_059'], 'func': lqc_base_universe_d3_059_lqc_basefill_059}


def lqc_base_universe_d3_060_lqc_basefill_060(lqc_base_universe_d2_060_lqc_basefill_060):
    return _base_universe_d3(lqc_base_universe_d2_060_lqc_basefill_060, 60)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_060_lqc_basefill_060'] = {'inputs': ['lqc_base_universe_d2_060_lqc_basefill_060'], 'func': lqc_base_universe_d3_060_lqc_basefill_060}


def lqc_base_universe_d3_061_lqc_basefill_061(lqc_base_universe_d2_061_lqc_basefill_061):
    return _base_universe_d3(lqc_base_universe_d2_061_lqc_basefill_061, 61)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_061_lqc_basefill_061'] = {'inputs': ['lqc_base_universe_d2_061_lqc_basefill_061'], 'func': lqc_base_universe_d3_061_lqc_basefill_061}


def lqc_base_universe_d3_062_lqc_basefill_062(lqc_base_universe_d2_062_lqc_basefill_062):
    return _base_universe_d3(lqc_base_universe_d2_062_lqc_basefill_062, 62)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_062_lqc_basefill_062'] = {'inputs': ['lqc_base_universe_d2_062_lqc_basefill_062'], 'func': lqc_base_universe_d3_062_lqc_basefill_062}


def lqc_base_universe_d3_063_lqc_basefill_063(lqc_base_universe_d2_063_lqc_basefill_063):
    return _base_universe_d3(lqc_base_universe_d2_063_lqc_basefill_063, 63)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_063_lqc_basefill_063'] = {'inputs': ['lqc_base_universe_d2_063_lqc_basefill_063'], 'func': lqc_base_universe_d3_063_lqc_basefill_063}


def lqc_base_universe_d3_064_lqc_basefill_064(lqc_base_universe_d2_064_lqc_basefill_064):
    return _base_universe_d3(lqc_base_universe_d2_064_lqc_basefill_064, 64)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_064_lqc_basefill_064'] = {'inputs': ['lqc_base_universe_d2_064_lqc_basefill_064'], 'func': lqc_base_universe_d3_064_lqc_basefill_064}


def lqc_base_universe_d3_065_lqc_basefill_065(lqc_base_universe_d2_065_lqc_basefill_065):
    return _base_universe_d3(lqc_base_universe_d2_065_lqc_basefill_065, 65)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_065_lqc_basefill_065'] = {'inputs': ['lqc_base_universe_d2_065_lqc_basefill_065'], 'func': lqc_base_universe_d3_065_lqc_basefill_065}


def lqc_base_universe_d3_066_lqc_basefill_066(lqc_base_universe_d2_066_lqc_basefill_066):
    return _base_universe_d3(lqc_base_universe_d2_066_lqc_basefill_066, 66)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_066_lqc_basefill_066'] = {'inputs': ['lqc_base_universe_d2_066_lqc_basefill_066'], 'func': lqc_base_universe_d3_066_lqc_basefill_066}


def lqc_base_universe_d3_067_lqc_basefill_067(lqc_base_universe_d2_067_lqc_basefill_067):
    return _base_universe_d3(lqc_base_universe_d2_067_lqc_basefill_067, 67)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_067_lqc_basefill_067'] = {'inputs': ['lqc_base_universe_d2_067_lqc_basefill_067'], 'func': lqc_base_universe_d3_067_lqc_basefill_067}


def lqc_base_universe_d3_068_lqc_basefill_068(lqc_base_universe_d2_068_lqc_basefill_068):
    return _base_universe_d3(lqc_base_universe_d2_068_lqc_basefill_068, 68)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_068_lqc_basefill_068'] = {'inputs': ['lqc_base_universe_d2_068_lqc_basefill_068'], 'func': lqc_base_universe_d3_068_lqc_basefill_068}


def lqc_base_universe_d3_069_lqc_basefill_069(lqc_base_universe_d2_069_lqc_basefill_069):
    return _base_universe_d3(lqc_base_universe_d2_069_lqc_basefill_069, 69)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_069_lqc_basefill_069'] = {'inputs': ['lqc_base_universe_d2_069_lqc_basefill_069'], 'func': lqc_base_universe_d3_069_lqc_basefill_069}


def lqc_base_universe_d3_070_lqc_basefill_070(lqc_base_universe_d2_070_lqc_basefill_070):
    return _base_universe_d3(lqc_base_universe_d2_070_lqc_basefill_070, 70)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_070_lqc_basefill_070'] = {'inputs': ['lqc_base_universe_d2_070_lqc_basefill_070'], 'func': lqc_base_universe_d3_070_lqc_basefill_070}


def lqc_base_universe_d3_071_lqc_basefill_071(lqc_base_universe_d2_071_lqc_basefill_071):
    return _base_universe_d3(lqc_base_universe_d2_071_lqc_basefill_071, 71)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_071_lqc_basefill_071'] = {'inputs': ['lqc_base_universe_d2_071_lqc_basefill_071'], 'func': lqc_base_universe_d3_071_lqc_basefill_071}


def lqc_base_universe_d3_072_lqc_basefill_072(lqc_base_universe_d2_072_lqc_basefill_072):
    return _base_universe_d3(lqc_base_universe_d2_072_lqc_basefill_072, 72)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_072_lqc_basefill_072'] = {'inputs': ['lqc_base_universe_d2_072_lqc_basefill_072'], 'func': lqc_base_universe_d3_072_lqc_basefill_072}


def lqc_base_universe_d3_073_lqc_basefill_073(lqc_base_universe_d2_073_lqc_basefill_073):
    return _base_universe_d3(lqc_base_universe_d2_073_lqc_basefill_073, 73)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_073_lqc_basefill_073'] = {'inputs': ['lqc_base_universe_d2_073_lqc_basefill_073'], 'func': lqc_base_universe_d3_073_lqc_basefill_073}


def lqc_base_universe_d3_074_lqc_basefill_074(lqc_base_universe_d2_074_lqc_basefill_074):
    return _base_universe_d3(lqc_base_universe_d2_074_lqc_basefill_074, 74)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_074_lqc_basefill_074'] = {'inputs': ['lqc_base_universe_d2_074_lqc_basefill_074'], 'func': lqc_base_universe_d3_074_lqc_basefill_074}


def lqc_base_universe_d3_075_lqc_basefill_075(lqc_base_universe_d2_075_lqc_basefill_075):
    return _base_universe_d3(lqc_base_universe_d2_075_lqc_basefill_075, 75)
LQC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lqc_base_universe_d3_075_lqc_basefill_075'] = {'inputs': ['lqc_base_universe_d2_075_lqc_basefill_075'], 'func': lqc_base_universe_d3_075_lqc_basefill_075}
