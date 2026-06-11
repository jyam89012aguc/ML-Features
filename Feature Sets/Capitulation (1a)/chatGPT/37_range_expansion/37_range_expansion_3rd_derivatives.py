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



def rex_001_realized_vol_z_accel_1(rex_001_realized_vol_z_roc_1):
    feature = _s(rex_001_realized_vol_z_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def rex_007_realized_vol_z_accel_5(rex_007_realized_vol_z_roc_5):
    feature = _s(rex_007_realized_vol_z_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def rex_013_realized_vol_z_accel_42(rex_013_realized_vol_z_roc_42):
    feature = _s(rex_013_realized_vol_z_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def rex_179_rex_019_realized_vol_z_42_019_accel_126(rex_154_rex_019_realized_vol_z_42_019_roc_126):
    feature = _s(rex_154_rex_019_realized_vol_z_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def rex_180_rex_025_realized_vol_z_378_025_accel_378(rex_155_rex_025_realized_vol_z_378_025_roc_378):
    feature = _s(rex_155_rex_025_realized_vol_z_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















RANGE_EXPANSION_REGISTRY_3RD_DERIVATIVES = {
    'rex_001_realized_vol_z_accel_1': {'inputs': ['rex_001_realized_vol_z_roc_1'], 'func': rex_001_realized_vol_z_accel_1},
    'rex_007_realized_vol_z_accel_5': {'inputs': ['rex_007_realized_vol_z_roc_5'], 'func': rex_007_realized_vol_z_accel_5},
    'rex_013_realized_vol_z_accel_42': {'inputs': ['rex_013_realized_vol_z_roc_42'], 'func': rex_013_realized_vol_z_accel_42},
    'rex_179_rex_019_realized_vol_z_42_019_accel_126': {'inputs': ['rex_154_rex_019_realized_vol_z_42_019_roc_126'], 'func': rex_179_rex_019_realized_vol_z_42_019_accel_126},
    'rex_180_rex_025_realized_vol_z_378_025_accel_378': {'inputs': ['rex_155_rex_025_realized_vol_z_378_025_roc_378'], 'func': rex_180_rex_025_realized_vol_z_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def re_replacement_d3_001(re_replacement_d2_001):
    feature = _clean(re_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_001'] = {'inputs': ['re_replacement_d2_001'], 'func': re_replacement_d3_001}


def re_replacement_d3_002(re_replacement_d2_002):
    feature = _clean(re_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_002'] = {'inputs': ['re_replacement_d2_002'], 'func': re_replacement_d3_002}


def re_replacement_d3_003(re_replacement_d2_003):
    feature = _clean(re_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_003'] = {'inputs': ['re_replacement_d2_003'], 'func': re_replacement_d3_003}


def re_replacement_d3_004(re_replacement_d2_004):
    feature = _clean(re_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_004'] = {'inputs': ['re_replacement_d2_004'], 'func': re_replacement_d3_004}


def re_replacement_d3_005(re_replacement_d2_005):
    feature = _clean(re_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_005'] = {'inputs': ['re_replacement_d2_005'], 'func': re_replacement_d3_005}


def re_replacement_d3_006(re_replacement_d2_006):
    feature = _clean(re_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_006'] = {'inputs': ['re_replacement_d2_006'], 'func': re_replacement_d3_006}


def re_replacement_d3_007(re_replacement_d2_007):
    feature = _clean(re_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_007'] = {'inputs': ['re_replacement_d2_007'], 'func': re_replacement_d3_007}


def re_replacement_d3_008(re_replacement_d2_008):
    feature = _clean(re_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_008'] = {'inputs': ['re_replacement_d2_008'], 'func': re_replacement_d3_008}


def re_replacement_d3_009(re_replacement_d2_009):
    feature = _clean(re_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_009'] = {'inputs': ['re_replacement_d2_009'], 'func': re_replacement_d3_009}


def re_replacement_d3_010(re_replacement_d2_010):
    feature = _clean(re_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_010'] = {'inputs': ['re_replacement_d2_010'], 'func': re_replacement_d3_010}


def re_replacement_d3_011(re_replacement_d2_011):
    feature = _clean(re_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_011'] = {'inputs': ['re_replacement_d2_011'], 'func': re_replacement_d3_011}


def re_replacement_d3_012(re_replacement_d2_012):
    feature = _clean(re_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_012'] = {'inputs': ['re_replacement_d2_012'], 'func': re_replacement_d3_012}


def re_replacement_d3_013(re_replacement_d2_013):
    feature = _clean(re_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_013'] = {'inputs': ['re_replacement_d2_013'], 'func': re_replacement_d3_013}


def re_replacement_d3_014(re_replacement_d2_014):
    feature = _clean(re_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_014'] = {'inputs': ['re_replacement_d2_014'], 'func': re_replacement_d3_014}


def re_replacement_d3_015(re_replacement_d2_015):
    feature = _clean(re_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_015'] = {'inputs': ['re_replacement_d2_015'], 'func': re_replacement_d3_015}


def re_replacement_d3_016(re_replacement_d2_016):
    feature = _clean(re_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_016'] = {'inputs': ['re_replacement_d2_016'], 'func': re_replacement_d3_016}


def re_replacement_d3_017(re_replacement_d2_017):
    feature = _clean(re_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_017'] = {'inputs': ['re_replacement_d2_017'], 'func': re_replacement_d3_017}


def re_replacement_d3_018(re_replacement_d2_018):
    feature = _clean(re_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_018'] = {'inputs': ['re_replacement_d2_018'], 'func': re_replacement_d3_018}


def re_replacement_d3_019(re_replacement_d2_019):
    feature = _clean(re_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_019'] = {'inputs': ['re_replacement_d2_019'], 'func': re_replacement_d3_019}


def re_replacement_d3_020(re_replacement_d2_020):
    feature = _clean(re_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_020'] = {'inputs': ['re_replacement_d2_020'], 'func': re_replacement_d3_020}


def re_replacement_d3_021(re_replacement_d2_021):
    feature = _clean(re_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_021'] = {'inputs': ['re_replacement_d2_021'], 'func': re_replacement_d3_021}


def re_replacement_d3_022(re_replacement_d2_022):
    feature = _clean(re_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_022'] = {'inputs': ['re_replacement_d2_022'], 'func': re_replacement_d3_022}


def re_replacement_d3_023(re_replacement_d2_023):
    feature = _clean(re_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_023'] = {'inputs': ['re_replacement_d2_023'], 'func': re_replacement_d3_023}


def re_replacement_d3_024(re_replacement_d2_024):
    feature = _clean(re_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_024'] = {'inputs': ['re_replacement_d2_024'], 'func': re_replacement_d3_024}


def re_replacement_d3_025(re_replacement_d2_025):
    feature = _clean(re_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_025'] = {'inputs': ['re_replacement_d2_025'], 'func': re_replacement_d3_025}


def re_replacement_d3_026(re_replacement_d2_026):
    feature = _clean(re_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_026'] = {'inputs': ['re_replacement_d2_026'], 'func': re_replacement_d3_026}


def re_replacement_d3_027(re_replacement_d2_027):
    feature = _clean(re_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_027'] = {'inputs': ['re_replacement_d2_027'], 'func': re_replacement_d3_027}


def re_replacement_d3_028(re_replacement_d2_028):
    feature = _clean(re_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_028'] = {'inputs': ['re_replacement_d2_028'], 'func': re_replacement_d3_028}


def re_replacement_d3_029(re_replacement_d2_029):
    feature = _clean(re_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_029'] = {'inputs': ['re_replacement_d2_029'], 'func': re_replacement_d3_029}


def re_replacement_d3_030(re_replacement_d2_030):
    feature = _clean(re_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_030'] = {'inputs': ['re_replacement_d2_030'], 'func': re_replacement_d3_030}


def re_replacement_d3_031(re_replacement_d2_031):
    feature = _clean(re_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_031'] = {'inputs': ['re_replacement_d2_031'], 'func': re_replacement_d3_031}


def re_replacement_d3_032(re_replacement_d2_032):
    feature = _clean(re_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_032'] = {'inputs': ['re_replacement_d2_032'], 'func': re_replacement_d3_032}


def re_replacement_d3_033(re_replacement_d2_033):
    feature = _clean(re_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_033'] = {'inputs': ['re_replacement_d2_033'], 'func': re_replacement_d3_033}


def re_replacement_d3_034(re_replacement_d2_034):
    feature = _clean(re_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_034'] = {'inputs': ['re_replacement_d2_034'], 'func': re_replacement_d3_034}


def re_replacement_d3_035(re_replacement_d2_035):
    feature = _clean(re_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_035'] = {'inputs': ['re_replacement_d2_035'], 'func': re_replacement_d3_035}


def re_replacement_d3_036(re_replacement_d2_036):
    feature = _clean(re_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_036'] = {'inputs': ['re_replacement_d2_036'], 'func': re_replacement_d3_036}


def re_replacement_d3_037(re_replacement_d2_037):
    feature = _clean(re_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_037'] = {'inputs': ['re_replacement_d2_037'], 'func': re_replacement_d3_037}


def re_replacement_d3_038(re_replacement_d2_038):
    feature = _clean(re_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_038'] = {'inputs': ['re_replacement_d2_038'], 'func': re_replacement_d3_038}


def re_replacement_d3_039(re_replacement_d2_039):
    feature = _clean(re_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_039'] = {'inputs': ['re_replacement_d2_039'], 'func': re_replacement_d3_039}


def re_replacement_d3_040(re_replacement_d2_040):
    feature = _clean(re_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_040'] = {'inputs': ['re_replacement_d2_040'], 'func': re_replacement_d3_040}


def re_replacement_d3_041(re_replacement_d2_041):
    feature = _clean(re_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_041'] = {'inputs': ['re_replacement_d2_041'], 'func': re_replacement_d3_041}


def re_replacement_d3_042(re_replacement_d2_042):
    feature = _clean(re_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_042'] = {'inputs': ['re_replacement_d2_042'], 'func': re_replacement_d3_042}


def re_replacement_d3_043(re_replacement_d2_043):
    feature = _clean(re_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_043'] = {'inputs': ['re_replacement_d2_043'], 'func': re_replacement_d3_043}


def re_replacement_d3_044(re_replacement_d2_044):
    feature = _clean(re_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_044'] = {'inputs': ['re_replacement_d2_044'], 'func': re_replacement_d3_044}


def re_replacement_d3_045(re_replacement_d2_045):
    feature = _clean(re_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_045'] = {'inputs': ['re_replacement_d2_045'], 'func': re_replacement_d3_045}


def re_replacement_d3_046(re_replacement_d2_046):
    feature = _clean(re_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_046'] = {'inputs': ['re_replacement_d2_046'], 'func': re_replacement_d3_046}


def re_replacement_d3_047(re_replacement_d2_047):
    feature = _clean(re_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_047'] = {'inputs': ['re_replacement_d2_047'], 'func': re_replacement_d3_047}


def re_replacement_d3_048(re_replacement_d2_048):
    feature = _clean(re_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_048'] = {'inputs': ['re_replacement_d2_048'], 'func': re_replacement_d3_048}


def re_replacement_d3_049(re_replacement_d2_049):
    feature = _clean(re_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_049'] = {'inputs': ['re_replacement_d2_049'], 'func': re_replacement_d3_049}


def re_replacement_d3_050(re_replacement_d2_050):
    feature = _clean(re_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_050'] = {'inputs': ['re_replacement_d2_050'], 'func': re_replacement_d3_050}


def re_replacement_d3_051(re_replacement_d2_051):
    feature = _clean(re_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_051'] = {'inputs': ['re_replacement_d2_051'], 'func': re_replacement_d3_051}


def re_replacement_d3_052(re_replacement_d2_052):
    feature = _clean(re_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_052'] = {'inputs': ['re_replacement_d2_052'], 'func': re_replacement_d3_052}


def re_replacement_d3_053(re_replacement_d2_053):
    feature = _clean(re_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_053'] = {'inputs': ['re_replacement_d2_053'], 'func': re_replacement_d3_053}


def re_replacement_d3_054(re_replacement_d2_054):
    feature = _clean(re_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_054'] = {'inputs': ['re_replacement_d2_054'], 'func': re_replacement_d3_054}


def re_replacement_d3_055(re_replacement_d2_055):
    feature = _clean(re_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_055'] = {'inputs': ['re_replacement_d2_055'], 'func': re_replacement_d3_055}


def re_replacement_d3_056(re_replacement_d2_056):
    feature = _clean(re_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_056'] = {'inputs': ['re_replacement_d2_056'], 'func': re_replacement_d3_056}


def re_replacement_d3_057(re_replacement_d2_057):
    feature = _clean(re_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_057'] = {'inputs': ['re_replacement_d2_057'], 'func': re_replacement_d3_057}


def re_replacement_d3_058(re_replacement_d2_058):
    feature = _clean(re_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_058'] = {'inputs': ['re_replacement_d2_058'], 'func': re_replacement_d3_058}


def re_replacement_d3_059(re_replacement_d2_059):
    feature = _clean(re_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_059'] = {'inputs': ['re_replacement_d2_059'], 'func': re_replacement_d3_059}


def re_replacement_d3_060(re_replacement_d2_060):
    feature = _clean(re_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_060'] = {'inputs': ['re_replacement_d2_060'], 'func': re_replacement_d3_060}


def re_replacement_d3_061(re_replacement_d2_061):
    feature = _clean(re_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_061'] = {'inputs': ['re_replacement_d2_061'], 'func': re_replacement_d3_061}


def re_replacement_d3_062(re_replacement_d2_062):
    feature = _clean(re_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_062'] = {'inputs': ['re_replacement_d2_062'], 'func': re_replacement_d3_062}


def re_replacement_d3_063(re_replacement_d2_063):
    feature = _clean(re_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_063'] = {'inputs': ['re_replacement_d2_063'], 'func': re_replacement_d3_063}


def re_replacement_d3_064(re_replacement_d2_064):
    feature = _clean(re_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_064'] = {'inputs': ['re_replacement_d2_064'], 'func': re_replacement_d3_064}


def re_replacement_d3_065(re_replacement_d2_065):
    feature = _clean(re_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_065'] = {'inputs': ['re_replacement_d2_065'], 'func': re_replacement_d3_065}


def re_replacement_d3_066(re_replacement_d2_066):
    feature = _clean(re_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_066'] = {'inputs': ['re_replacement_d2_066'], 'func': re_replacement_d3_066}


def re_replacement_d3_067(re_replacement_d2_067):
    feature = _clean(re_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_067'] = {'inputs': ['re_replacement_d2_067'], 'func': re_replacement_d3_067}


def re_replacement_d3_068(re_replacement_d2_068):
    feature = _clean(re_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_068'] = {'inputs': ['re_replacement_d2_068'], 'func': re_replacement_d3_068}


def re_replacement_d3_069(re_replacement_d2_069):
    feature = _clean(re_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_069'] = {'inputs': ['re_replacement_d2_069'], 'func': re_replacement_d3_069}


def re_replacement_d3_070(re_replacement_d2_070):
    feature = _clean(re_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_070'] = {'inputs': ['re_replacement_d2_070'], 'func': re_replacement_d3_070}


def re_replacement_d3_071(re_replacement_d2_071):
    feature = _clean(re_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_071'] = {'inputs': ['re_replacement_d2_071'], 'func': re_replacement_d3_071}


def re_replacement_d3_072(re_replacement_d2_072):
    feature = _clean(re_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_072'] = {'inputs': ['re_replacement_d2_072'], 'func': re_replacement_d3_072}


def re_replacement_d3_073(re_replacement_d2_073):
    feature = _clean(re_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_073'] = {'inputs': ['re_replacement_d2_073'], 'func': re_replacement_d3_073}


def re_replacement_d3_074(re_replacement_d2_074):
    feature = _clean(re_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_074'] = {'inputs': ['re_replacement_d2_074'], 'func': re_replacement_d3_074}


def re_replacement_d3_075(re_replacement_d2_075):
    feature = _clean(re_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_075'] = {'inputs': ['re_replacement_d2_075'], 'func': re_replacement_d3_075}


def re_replacement_d3_076(re_replacement_d2_076):
    feature = _clean(re_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_076'] = {'inputs': ['re_replacement_d2_076'], 'func': re_replacement_d3_076}


def re_replacement_d3_077(re_replacement_d2_077):
    feature = _clean(re_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_077'] = {'inputs': ['re_replacement_d2_077'], 'func': re_replacement_d3_077}


def re_replacement_d3_078(re_replacement_d2_078):
    feature = _clean(re_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_078'] = {'inputs': ['re_replacement_d2_078'], 'func': re_replacement_d3_078}


def re_replacement_d3_079(re_replacement_d2_079):
    feature = _clean(re_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_079'] = {'inputs': ['re_replacement_d2_079'], 'func': re_replacement_d3_079}


def re_replacement_d3_080(re_replacement_d2_080):
    feature = _clean(re_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_080'] = {'inputs': ['re_replacement_d2_080'], 'func': re_replacement_d3_080}


def re_replacement_d3_081(re_replacement_d2_081):
    feature = _clean(re_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_081'] = {'inputs': ['re_replacement_d2_081'], 'func': re_replacement_d3_081}


def re_replacement_d3_082(re_replacement_d2_082):
    feature = _clean(re_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_082'] = {'inputs': ['re_replacement_d2_082'], 'func': re_replacement_d3_082}


def re_replacement_d3_083(re_replacement_d2_083):
    feature = _clean(re_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_083'] = {'inputs': ['re_replacement_d2_083'], 'func': re_replacement_d3_083}


def re_replacement_d3_084(re_replacement_d2_084):
    feature = _clean(re_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_084'] = {'inputs': ['re_replacement_d2_084'], 'func': re_replacement_d3_084}


def re_replacement_d3_085(re_replacement_d2_085):
    feature = _clean(re_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_085'] = {'inputs': ['re_replacement_d2_085'], 'func': re_replacement_d3_085}


def re_replacement_d3_086(re_replacement_d2_086):
    feature = _clean(re_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_086'] = {'inputs': ['re_replacement_d2_086'], 'func': re_replacement_d3_086}


def re_replacement_d3_087(re_replacement_d2_087):
    feature = _clean(re_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_087'] = {'inputs': ['re_replacement_d2_087'], 'func': re_replacement_d3_087}


def re_replacement_d3_088(re_replacement_d2_088):
    feature = _clean(re_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_088'] = {'inputs': ['re_replacement_d2_088'], 'func': re_replacement_d3_088}


def re_replacement_d3_089(re_replacement_d2_089):
    feature = _clean(re_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_089'] = {'inputs': ['re_replacement_d2_089'], 'func': re_replacement_d3_089}


def re_replacement_d3_090(re_replacement_d2_090):
    feature = _clean(re_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_090'] = {'inputs': ['re_replacement_d2_090'], 'func': re_replacement_d3_090}


def re_replacement_d3_091(re_replacement_d2_091):
    feature = _clean(re_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_091'] = {'inputs': ['re_replacement_d2_091'], 'func': re_replacement_d3_091}


def re_replacement_d3_092(re_replacement_d2_092):
    feature = _clean(re_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_092'] = {'inputs': ['re_replacement_d2_092'], 'func': re_replacement_d3_092}


def re_replacement_d3_093(re_replacement_d2_093):
    feature = _clean(re_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_093'] = {'inputs': ['re_replacement_d2_093'], 'func': re_replacement_d3_093}


def re_replacement_d3_094(re_replacement_d2_094):
    feature = _clean(re_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_094'] = {'inputs': ['re_replacement_d2_094'], 'func': re_replacement_d3_094}


def re_replacement_d3_095(re_replacement_d2_095):
    feature = _clean(re_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_095'] = {'inputs': ['re_replacement_d2_095'], 'func': re_replacement_d3_095}


def re_replacement_d3_096(re_replacement_d2_096):
    feature = _clean(re_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_096'] = {'inputs': ['re_replacement_d2_096'], 'func': re_replacement_d3_096}


def re_replacement_d3_097(re_replacement_d2_097):
    feature = _clean(re_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_097'] = {'inputs': ['re_replacement_d2_097'], 'func': re_replacement_d3_097}


def re_replacement_d3_098(re_replacement_d2_098):
    feature = _clean(re_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_098'] = {'inputs': ['re_replacement_d2_098'], 'func': re_replacement_d3_098}


def re_replacement_d3_099(re_replacement_d2_099):
    feature = _clean(re_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_099'] = {'inputs': ['re_replacement_d2_099'], 'func': re_replacement_d3_099}


def re_replacement_d3_100(re_replacement_d2_100):
    feature = _clean(re_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_100'] = {'inputs': ['re_replacement_d2_100'], 'func': re_replacement_d3_100}


def re_replacement_d3_101(re_replacement_d2_101):
    feature = _clean(re_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_101'] = {'inputs': ['re_replacement_d2_101'], 'func': re_replacement_d3_101}


def re_replacement_d3_102(re_replacement_d2_102):
    feature = _clean(re_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_102'] = {'inputs': ['re_replacement_d2_102'], 'func': re_replacement_d3_102}


def re_replacement_d3_103(re_replacement_d2_103):
    feature = _clean(re_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_103'] = {'inputs': ['re_replacement_d2_103'], 'func': re_replacement_d3_103}


def re_replacement_d3_104(re_replacement_d2_104):
    feature = _clean(re_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_104'] = {'inputs': ['re_replacement_d2_104'], 'func': re_replacement_d3_104}


def re_replacement_d3_105(re_replacement_d2_105):
    feature = _clean(re_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_105'] = {'inputs': ['re_replacement_d2_105'], 'func': re_replacement_d3_105}


def re_replacement_d3_106(re_replacement_d2_106):
    feature = _clean(re_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_106'] = {'inputs': ['re_replacement_d2_106'], 'func': re_replacement_d3_106}


def re_replacement_d3_107(re_replacement_d2_107):
    feature = _clean(re_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_107'] = {'inputs': ['re_replacement_d2_107'], 'func': re_replacement_d3_107}


def re_replacement_d3_108(re_replacement_d2_108):
    feature = _clean(re_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_108'] = {'inputs': ['re_replacement_d2_108'], 'func': re_replacement_d3_108}


def re_replacement_d3_109(re_replacement_d2_109):
    feature = _clean(re_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_109'] = {'inputs': ['re_replacement_d2_109'], 'func': re_replacement_d3_109}


def re_replacement_d3_110(re_replacement_d2_110):
    feature = _clean(re_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_110'] = {'inputs': ['re_replacement_d2_110'], 'func': re_replacement_d3_110}


def re_replacement_d3_111(re_replacement_d2_111):
    feature = _clean(re_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_111'] = {'inputs': ['re_replacement_d2_111'], 'func': re_replacement_d3_111}


def re_replacement_d3_112(re_replacement_d2_112):
    feature = _clean(re_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_112'] = {'inputs': ['re_replacement_d2_112'], 'func': re_replacement_d3_112}


def re_replacement_d3_113(re_replacement_d2_113):
    feature = _clean(re_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_113'] = {'inputs': ['re_replacement_d2_113'], 'func': re_replacement_d3_113}


def re_replacement_d3_114(re_replacement_d2_114):
    feature = _clean(re_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_114'] = {'inputs': ['re_replacement_d2_114'], 'func': re_replacement_d3_114}


def re_replacement_d3_115(re_replacement_d2_115):
    feature = _clean(re_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_115'] = {'inputs': ['re_replacement_d2_115'], 'func': re_replacement_d3_115}


def re_replacement_d3_116(re_replacement_d2_116):
    feature = _clean(re_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_116'] = {'inputs': ['re_replacement_d2_116'], 'func': re_replacement_d3_116}


def re_replacement_d3_117(re_replacement_d2_117):
    feature = _clean(re_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_117'] = {'inputs': ['re_replacement_d2_117'], 'func': re_replacement_d3_117}


def re_replacement_d3_118(re_replacement_d2_118):
    feature = _clean(re_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_118'] = {'inputs': ['re_replacement_d2_118'], 'func': re_replacement_d3_118}


def re_replacement_d3_119(re_replacement_d2_119):
    feature = _clean(re_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_119'] = {'inputs': ['re_replacement_d2_119'], 'func': re_replacement_d3_119}


def re_replacement_d3_120(re_replacement_d2_120):
    feature = _clean(re_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_120'] = {'inputs': ['re_replacement_d2_120'], 'func': re_replacement_d3_120}


def re_replacement_d3_121(re_replacement_d2_121):
    feature = _clean(re_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_121'] = {'inputs': ['re_replacement_d2_121'], 'func': re_replacement_d3_121}


def re_replacement_d3_122(re_replacement_d2_122):
    feature = _clean(re_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_122'] = {'inputs': ['re_replacement_d2_122'], 'func': re_replacement_d3_122}


def re_replacement_d3_123(re_replacement_d2_123):
    feature = _clean(re_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_123'] = {'inputs': ['re_replacement_d2_123'], 'func': re_replacement_d3_123}


def re_replacement_d3_124(re_replacement_d2_124):
    feature = _clean(re_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_124'] = {'inputs': ['re_replacement_d2_124'], 'func': re_replacement_d3_124}


def re_replacement_d3_125(re_replacement_d2_125):
    feature = _clean(re_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_125'] = {'inputs': ['re_replacement_d2_125'], 'func': re_replacement_d3_125}


def re_replacement_d3_126(re_replacement_d2_126):
    feature = _clean(re_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_126'] = {'inputs': ['re_replacement_d2_126'], 'func': re_replacement_d3_126}


def re_replacement_d3_127(re_replacement_d2_127):
    feature = _clean(re_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_127'] = {'inputs': ['re_replacement_d2_127'], 'func': re_replacement_d3_127}


def re_replacement_d3_128(re_replacement_d2_128):
    feature = _clean(re_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_128'] = {'inputs': ['re_replacement_d2_128'], 'func': re_replacement_d3_128}


def re_replacement_d3_129(re_replacement_d2_129):
    feature = _clean(re_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_129'] = {'inputs': ['re_replacement_d2_129'], 'func': re_replacement_d3_129}


def re_replacement_d3_130(re_replacement_d2_130):
    feature = _clean(re_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_130'] = {'inputs': ['re_replacement_d2_130'], 'func': re_replacement_d3_130}


def re_replacement_d3_131(re_replacement_d2_131):
    feature = _clean(re_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_131'] = {'inputs': ['re_replacement_d2_131'], 'func': re_replacement_d3_131}


def re_replacement_d3_132(re_replacement_d2_132):
    feature = _clean(re_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_132'] = {'inputs': ['re_replacement_d2_132'], 'func': re_replacement_d3_132}


def re_replacement_d3_133(re_replacement_d2_133):
    feature = _clean(re_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_133'] = {'inputs': ['re_replacement_d2_133'], 'func': re_replacement_d3_133}


def re_replacement_d3_134(re_replacement_d2_134):
    feature = _clean(re_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_134'] = {'inputs': ['re_replacement_d2_134'], 'func': re_replacement_d3_134}


def re_replacement_d3_135(re_replacement_d2_135):
    feature = _clean(re_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_135'] = {'inputs': ['re_replacement_d2_135'], 'func': re_replacement_d3_135}


def re_replacement_d3_136(re_replacement_d2_136):
    feature = _clean(re_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_136'] = {'inputs': ['re_replacement_d2_136'], 'func': re_replacement_d3_136}


def re_replacement_d3_137(re_replacement_d2_137):
    feature = _clean(re_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_137'] = {'inputs': ['re_replacement_d2_137'], 'func': re_replacement_d3_137}


def re_replacement_d3_138(re_replacement_d2_138):
    feature = _clean(re_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_138'] = {'inputs': ['re_replacement_d2_138'], 'func': re_replacement_d3_138}


def re_replacement_d3_139(re_replacement_d2_139):
    feature = _clean(re_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_139'] = {'inputs': ['re_replacement_d2_139'], 'func': re_replacement_d3_139}


def re_replacement_d3_140(re_replacement_d2_140):
    feature = _clean(re_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_140'] = {'inputs': ['re_replacement_d2_140'], 'func': re_replacement_d3_140}


def re_replacement_d3_141(re_replacement_d2_141):
    feature = _clean(re_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_141'] = {'inputs': ['re_replacement_d2_141'], 'func': re_replacement_d3_141}


def re_replacement_d3_142(re_replacement_d2_142):
    feature = _clean(re_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_142'] = {'inputs': ['re_replacement_d2_142'], 'func': re_replacement_d3_142}


def re_replacement_d3_143(re_replacement_d2_143):
    feature = _clean(re_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_143'] = {'inputs': ['re_replacement_d2_143'], 'func': re_replacement_d3_143}


def re_replacement_d3_144(re_replacement_d2_144):
    feature = _clean(re_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_144'] = {'inputs': ['re_replacement_d2_144'], 'func': re_replacement_d3_144}


def re_replacement_d3_145(re_replacement_d2_145):
    feature = _clean(re_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_145'] = {'inputs': ['re_replacement_d2_145'], 'func': re_replacement_d3_145}


def re_replacement_d3_146(re_replacement_d2_146):
    feature = _clean(re_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_146'] = {'inputs': ['re_replacement_d2_146'], 'func': re_replacement_d3_146}


def re_replacement_d3_147(re_replacement_d2_147):
    feature = _clean(re_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_147'] = {'inputs': ['re_replacement_d2_147'], 'func': re_replacement_d3_147}


def re_replacement_d3_148(re_replacement_d2_148):
    feature = _clean(re_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_148'] = {'inputs': ['re_replacement_d2_148'], 'func': re_replacement_d3_148}


def re_replacement_d3_149(re_replacement_d2_149):
    feature = _clean(re_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_149'] = {'inputs': ['re_replacement_d2_149'], 'func': re_replacement_d3_149}


def re_replacement_d3_150(re_replacement_d2_150):
    feature = _clean(re_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_150'] = {'inputs': ['re_replacement_d2_150'], 'func': re_replacement_d3_150}


def re_replacement_d3_151(re_replacement_d2_151):
    feature = _clean(re_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_151'] = {'inputs': ['re_replacement_d2_151'], 'func': re_replacement_d3_151}


def re_replacement_d3_152(re_replacement_d2_152):
    feature = _clean(re_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_152'] = {'inputs': ['re_replacement_d2_152'], 'func': re_replacement_d3_152}


def re_replacement_d3_153(re_replacement_d2_153):
    feature = _clean(re_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_153'] = {'inputs': ['re_replacement_d2_153'], 'func': re_replacement_d3_153}


def re_replacement_d3_154(re_replacement_d2_154):
    feature = _clean(re_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_154'] = {'inputs': ['re_replacement_d2_154'], 'func': re_replacement_d3_154}


def re_replacement_d3_155(re_replacement_d2_155):
    feature = _clean(re_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_155'] = {'inputs': ['re_replacement_d2_155'], 'func': re_replacement_d3_155}


def re_replacement_d3_156(re_replacement_d2_156):
    feature = _clean(re_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_156'] = {'inputs': ['re_replacement_d2_156'], 'func': re_replacement_d3_156}


def re_replacement_d3_157(re_replacement_d2_157):
    feature = _clean(re_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_157'] = {'inputs': ['re_replacement_d2_157'], 'func': re_replacement_d3_157}


def re_replacement_d3_158(re_replacement_d2_158):
    feature = _clean(re_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_158'] = {'inputs': ['re_replacement_d2_158'], 'func': re_replacement_d3_158}


def re_replacement_d3_159(re_replacement_d2_159):
    feature = _clean(re_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_159'] = {'inputs': ['re_replacement_d2_159'], 'func': re_replacement_d3_159}


def re_replacement_d3_160(re_replacement_d2_160):
    feature = _clean(re_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_160'] = {'inputs': ['re_replacement_d2_160'], 'func': re_replacement_d3_160}


def re_replacement_d3_161(re_replacement_d2_161):
    feature = _clean(re_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_161'] = {'inputs': ['re_replacement_d2_161'], 'func': re_replacement_d3_161}


def re_replacement_d3_162(re_replacement_d2_162):
    feature = _clean(re_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_162'] = {'inputs': ['re_replacement_d2_162'], 'func': re_replacement_d3_162}


def re_replacement_d3_163(re_replacement_d2_163):
    feature = _clean(re_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_163'] = {'inputs': ['re_replacement_d2_163'], 'func': re_replacement_d3_163}


def re_replacement_d3_164(re_replacement_d2_164):
    feature = _clean(re_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_164'] = {'inputs': ['re_replacement_d2_164'], 'func': re_replacement_d3_164}


def re_replacement_d3_165(re_replacement_d2_165):
    feature = _clean(re_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_165'] = {'inputs': ['re_replacement_d2_165'], 'func': re_replacement_d3_165}


def re_replacement_d3_166(re_replacement_d2_166):
    feature = _clean(re_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_166'] = {'inputs': ['re_replacement_d2_166'], 'func': re_replacement_d3_166}


def re_replacement_d3_167(re_replacement_d2_167):
    feature = _clean(re_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_167'] = {'inputs': ['re_replacement_d2_167'], 'func': re_replacement_d3_167}


def re_replacement_d3_168(re_replacement_d2_168):
    feature = _clean(re_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_168'] = {'inputs': ['re_replacement_d2_168'], 'func': re_replacement_d3_168}


def re_replacement_d3_169(re_replacement_d2_169):
    feature = _clean(re_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_169'] = {'inputs': ['re_replacement_d2_169'], 'func': re_replacement_d3_169}


def re_replacement_d3_170(re_replacement_d2_170):
    feature = _clean(re_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_170'] = {'inputs': ['re_replacement_d2_170'], 'func': re_replacement_d3_170}


def re_replacement_d3_171(re_replacement_d2_171):
    feature = _clean(re_replacement_d2_171)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_171'] = {'inputs': ['re_replacement_d2_171'], 'func': re_replacement_d3_171}


def re_replacement_d3_172(re_replacement_d2_172):
    feature = _clean(re_replacement_d2_172)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_172'] = {'inputs': ['re_replacement_d2_172'], 'func': re_replacement_d3_172}


def re_replacement_d3_173(re_replacement_d2_173):
    feature = _clean(re_replacement_d2_173)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_173'] = {'inputs': ['re_replacement_d2_173'], 'func': re_replacement_d3_173}


def re_replacement_d3_174(re_replacement_d2_174):
    feature = _clean(re_replacement_d2_174)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087000).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_174'] = {'inputs': ['re_replacement_d2_174'], 'func': re_replacement_d3_174}


def re_replacement_d3_175(re_replacement_d2_175):
    feature = _clean(re_replacement_d2_175)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087500).reindex(feature.index)
RE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['re_replacement_d3_175'] = {'inputs': ['re_replacement_d2_175'], 'func': re_replacement_d3_175}


# Third-derivative extensions for repaired first-base features.
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def rex_base_universe_d3_001_rex_002_range_expansion_10_002(rex_base_universe_d2_001_rex_002_range_expansion_10_002):
    return _base_universe_d3(rex_base_universe_d2_001_rex_002_range_expansion_10_002, 1)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_001_rex_002_range_expansion_10_002'] = {'inputs': ['rex_base_universe_d2_001_rex_002_range_expansion_10_002'], 'func': rex_base_universe_d3_001_rex_002_range_expansion_10_002}


def rex_base_universe_d3_002_rex_004_close_location_42_004(rex_base_universe_d2_002_rex_004_close_location_42_004):
    return _base_universe_d3(rex_base_universe_d2_002_rex_004_close_location_42_004, 2)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_002_rex_004_close_location_42_004'] = {'inputs': ['rex_base_universe_d2_002_rex_004_close_location_42_004'], 'func': rex_base_universe_d3_002_rex_004_close_location_42_004}


def rex_base_universe_d3_003_rex_005_atr_move_63_005(rex_base_universe_d2_003_rex_005_atr_move_63_005):
    return _base_universe_d3(rex_base_universe_d2_003_rex_005_atr_move_63_005, 3)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_003_rex_005_atr_move_63_005'] = {'inputs': ['rex_base_universe_d2_003_rex_005_atr_move_63_005'], 'func': rex_base_universe_d3_003_rex_005_atr_move_63_005}


def rex_base_universe_d3_004_rex_008_range_expansion_189_008(rex_base_universe_d2_004_rex_008_range_expansion_189_008):
    return _base_universe_d3(rex_base_universe_d2_004_rex_008_range_expansion_189_008, 4)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_004_rex_008_range_expansion_189_008'] = {'inputs': ['rex_base_universe_d2_004_rex_008_range_expansion_189_008'], 'func': rex_base_universe_d3_004_rex_008_range_expansion_189_008}


def rex_base_universe_d3_005_rex_010_close_location_378_010(rex_base_universe_d2_005_rex_010_close_location_378_010):
    return _base_universe_d3(rex_base_universe_d2_005_rex_010_close_location_378_010, 5)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_005_rex_010_close_location_378_010'] = {'inputs': ['rex_base_universe_d2_005_rex_010_close_location_378_010'], 'func': rex_base_universe_d3_005_rex_010_close_location_378_010}


def rex_base_universe_d3_006_rex_011_atr_move_504_011(rex_base_universe_d2_006_rex_011_atr_move_504_011):
    return _base_universe_d3(rex_base_universe_d2_006_rex_011_atr_move_504_011, 6)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_006_rex_011_atr_move_504_011'] = {'inputs': ['rex_base_universe_d2_006_rex_011_atr_move_504_011'], 'func': rex_base_universe_d3_006_rex_011_atr_move_504_011}


def rex_base_universe_d3_007_rex_014_range_expansion_1260_014(rex_base_universe_d2_007_rex_014_range_expansion_1260_014):
    return _base_universe_d3(rex_base_universe_d2_007_rex_014_range_expansion_1260_014, 7)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_007_rex_014_range_expansion_1260_014'] = {'inputs': ['rex_base_universe_d2_007_rex_014_range_expansion_1260_014'], 'func': rex_base_universe_d3_007_rex_014_range_expansion_1260_014}


def rex_base_universe_d3_008_rex_016_close_location_5_016(rex_base_universe_d2_008_rex_016_close_location_5_016):
    return _base_universe_d3(rex_base_universe_d2_008_rex_016_close_location_5_016, 8)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_008_rex_016_close_location_5_016'] = {'inputs': ['rex_base_universe_d2_008_rex_016_close_location_5_016'], 'func': rex_base_universe_d3_008_rex_016_close_location_5_016}


def rex_base_universe_d3_009_rex_017_atr_move_10_017(rex_base_universe_d2_009_rex_017_atr_move_10_017):
    return _base_universe_d3(rex_base_universe_d2_009_rex_017_atr_move_10_017, 9)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_009_rex_017_atr_move_10_017'] = {'inputs': ['rex_base_universe_d2_009_rex_017_atr_move_10_017'], 'func': rex_base_universe_d3_009_rex_017_atr_move_10_017}


def rex_base_universe_d3_010_rex_020_range_expansion_63_020(rex_base_universe_d2_010_rex_020_range_expansion_63_020):
    return _base_universe_d3(rex_base_universe_d2_010_rex_020_range_expansion_63_020, 10)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_010_rex_020_range_expansion_63_020'] = {'inputs': ['rex_base_universe_d2_010_rex_020_range_expansion_63_020'], 'func': rex_base_universe_d3_010_rex_020_range_expansion_63_020}


def rex_base_universe_d3_011_rex_022_close_location_126_022(rex_base_universe_d2_011_rex_022_close_location_126_022):
    return _base_universe_d3(rex_base_universe_d2_011_rex_022_close_location_126_022, 11)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_011_rex_022_close_location_126_022'] = {'inputs': ['rex_base_universe_d2_011_rex_022_close_location_126_022'], 'func': rex_base_universe_d3_011_rex_022_close_location_126_022}


def rex_base_universe_d3_012_rex_023_atr_move_189_023(rex_base_universe_d2_012_rex_023_atr_move_189_023):
    return _base_universe_d3(rex_base_universe_d2_012_rex_023_atr_move_189_023, 12)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_012_rex_023_atr_move_189_023'] = {'inputs': ['rex_base_universe_d2_012_rex_023_atr_move_189_023'], 'func': rex_base_universe_d3_012_rex_023_atr_move_189_023}


def rex_base_universe_d3_013_rex_026_range_expansion_504_026(rex_base_universe_d2_013_rex_026_range_expansion_504_026):
    return _base_universe_d3(rex_base_universe_d2_013_rex_026_range_expansion_504_026, 13)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_013_rex_026_range_expansion_504_026'] = {'inputs': ['rex_base_universe_d2_013_rex_026_range_expansion_504_026'], 'func': rex_base_universe_d3_013_rex_026_range_expansion_504_026}


def rex_base_universe_d3_014_rex_028_close_location_1008_028(rex_base_universe_d2_014_rex_028_close_location_1008_028):
    return _base_universe_d3(rex_base_universe_d2_014_rex_028_close_location_1008_028, 14)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_014_rex_028_close_location_1008_028'] = {'inputs': ['rex_base_universe_d2_014_rex_028_close_location_1008_028'], 'func': rex_base_universe_d3_014_rex_028_close_location_1008_028}


def rex_base_universe_d3_015_rex_029_atr_move_1260_029(rex_base_universe_d2_015_rex_029_atr_move_1260_029):
    return _base_universe_d3(rex_base_universe_d2_015_rex_029_atr_move_1260_029, 15)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_015_rex_029_atr_move_1260_029'] = {'inputs': ['rex_base_universe_d2_015_rex_029_atr_move_1260_029'], 'func': rex_base_universe_d3_015_rex_029_atr_move_1260_029}


def rex_base_universe_d3_016_rex_basefill_001(rex_base_universe_d2_016_rex_basefill_001):
    return _base_universe_d3(rex_base_universe_d2_016_rex_basefill_001, 16)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_016_rex_basefill_001'] = {'inputs': ['rex_base_universe_d2_016_rex_basefill_001'], 'func': rex_base_universe_d3_016_rex_basefill_001}


def rex_base_universe_d3_017_rex_basefill_003(rex_base_universe_d2_017_rex_basefill_003):
    return _base_universe_d3(rex_base_universe_d2_017_rex_basefill_003, 17)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_017_rex_basefill_003'] = {'inputs': ['rex_base_universe_d2_017_rex_basefill_003'], 'func': rex_base_universe_d3_017_rex_basefill_003}


def rex_base_universe_d3_018_rex_basefill_006(rex_base_universe_d2_018_rex_basefill_006):
    return _base_universe_d3(rex_base_universe_d2_018_rex_basefill_006, 18)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_018_rex_basefill_006'] = {'inputs': ['rex_base_universe_d2_018_rex_basefill_006'], 'func': rex_base_universe_d3_018_rex_basefill_006}


def rex_base_universe_d3_019_rex_basefill_007(rex_base_universe_d2_019_rex_basefill_007):
    return _base_universe_d3(rex_base_universe_d2_019_rex_basefill_007, 19)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_019_rex_basefill_007'] = {'inputs': ['rex_base_universe_d2_019_rex_basefill_007'], 'func': rex_base_universe_d3_019_rex_basefill_007}


def rex_base_universe_d3_020_rex_basefill_009(rex_base_universe_d2_020_rex_basefill_009):
    return _base_universe_d3(rex_base_universe_d2_020_rex_basefill_009, 20)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_020_rex_basefill_009'] = {'inputs': ['rex_base_universe_d2_020_rex_basefill_009'], 'func': rex_base_universe_d3_020_rex_basefill_009}


def rex_base_universe_d3_021_rex_basefill_012(rex_base_universe_d2_021_rex_basefill_012):
    return _base_universe_d3(rex_base_universe_d2_021_rex_basefill_012, 21)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_021_rex_basefill_012'] = {'inputs': ['rex_base_universe_d2_021_rex_basefill_012'], 'func': rex_base_universe_d3_021_rex_basefill_012}


def rex_base_universe_d3_022_rex_basefill_013(rex_base_universe_d2_022_rex_basefill_013):
    return _base_universe_d3(rex_base_universe_d2_022_rex_basefill_013, 22)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_022_rex_basefill_013'] = {'inputs': ['rex_base_universe_d2_022_rex_basefill_013'], 'func': rex_base_universe_d3_022_rex_basefill_013}


def rex_base_universe_d3_023_rex_basefill_015(rex_base_universe_d2_023_rex_basefill_015):
    return _base_universe_d3(rex_base_universe_d2_023_rex_basefill_015, 23)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_023_rex_basefill_015'] = {'inputs': ['rex_base_universe_d2_023_rex_basefill_015'], 'func': rex_base_universe_d3_023_rex_basefill_015}


def rex_base_universe_d3_024_rex_basefill_018(rex_base_universe_d2_024_rex_basefill_018):
    return _base_universe_d3(rex_base_universe_d2_024_rex_basefill_018, 24)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_024_rex_basefill_018'] = {'inputs': ['rex_base_universe_d2_024_rex_basefill_018'], 'func': rex_base_universe_d3_024_rex_basefill_018}


def rex_base_universe_d3_025_rex_basefill_019(rex_base_universe_d2_025_rex_basefill_019):
    return _base_universe_d3(rex_base_universe_d2_025_rex_basefill_019, 25)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_025_rex_basefill_019'] = {'inputs': ['rex_base_universe_d2_025_rex_basefill_019'], 'func': rex_base_universe_d3_025_rex_basefill_019}


def rex_base_universe_d3_026_rex_basefill_021(rex_base_universe_d2_026_rex_basefill_021):
    return _base_universe_d3(rex_base_universe_d2_026_rex_basefill_021, 26)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_026_rex_basefill_021'] = {'inputs': ['rex_base_universe_d2_026_rex_basefill_021'], 'func': rex_base_universe_d3_026_rex_basefill_021}


def rex_base_universe_d3_027_rex_basefill_024(rex_base_universe_d2_027_rex_basefill_024):
    return _base_universe_d3(rex_base_universe_d2_027_rex_basefill_024, 27)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_027_rex_basefill_024'] = {'inputs': ['rex_base_universe_d2_027_rex_basefill_024'], 'func': rex_base_universe_d3_027_rex_basefill_024}


def rex_base_universe_d3_028_rex_basefill_025(rex_base_universe_d2_028_rex_basefill_025):
    return _base_universe_d3(rex_base_universe_d2_028_rex_basefill_025, 28)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_028_rex_basefill_025'] = {'inputs': ['rex_base_universe_d2_028_rex_basefill_025'], 'func': rex_base_universe_d3_028_rex_basefill_025}


def rex_base_universe_d3_029_rex_basefill_027(rex_base_universe_d2_029_rex_basefill_027):
    return _base_universe_d3(rex_base_universe_d2_029_rex_basefill_027, 29)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_029_rex_basefill_027'] = {'inputs': ['rex_base_universe_d2_029_rex_basefill_027'], 'func': rex_base_universe_d3_029_rex_basefill_027}


def rex_base_universe_d3_030_rex_basefill_030(rex_base_universe_d2_030_rex_basefill_030):
    return _base_universe_d3(rex_base_universe_d2_030_rex_basefill_030, 30)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_030_rex_basefill_030'] = {'inputs': ['rex_base_universe_d2_030_rex_basefill_030'], 'func': rex_base_universe_d3_030_rex_basefill_030}


def rex_base_universe_d3_031_rex_basefill_031(rex_base_universe_d2_031_rex_basefill_031):
    return _base_universe_d3(rex_base_universe_d2_031_rex_basefill_031, 31)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_031_rex_basefill_031'] = {'inputs': ['rex_base_universe_d2_031_rex_basefill_031'], 'func': rex_base_universe_d3_031_rex_basefill_031}


def rex_base_universe_d3_032_rex_basefill_032(rex_base_universe_d2_032_rex_basefill_032):
    return _base_universe_d3(rex_base_universe_d2_032_rex_basefill_032, 32)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_032_rex_basefill_032'] = {'inputs': ['rex_base_universe_d2_032_rex_basefill_032'], 'func': rex_base_universe_d3_032_rex_basefill_032}


def rex_base_universe_d3_033_rex_basefill_033(rex_base_universe_d2_033_rex_basefill_033):
    return _base_universe_d3(rex_base_universe_d2_033_rex_basefill_033, 33)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_033_rex_basefill_033'] = {'inputs': ['rex_base_universe_d2_033_rex_basefill_033'], 'func': rex_base_universe_d3_033_rex_basefill_033}


def rex_base_universe_d3_034_rex_basefill_034(rex_base_universe_d2_034_rex_basefill_034):
    return _base_universe_d3(rex_base_universe_d2_034_rex_basefill_034, 34)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_034_rex_basefill_034'] = {'inputs': ['rex_base_universe_d2_034_rex_basefill_034'], 'func': rex_base_universe_d3_034_rex_basefill_034}


def rex_base_universe_d3_035_rex_basefill_035(rex_base_universe_d2_035_rex_basefill_035):
    return _base_universe_d3(rex_base_universe_d2_035_rex_basefill_035, 35)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_035_rex_basefill_035'] = {'inputs': ['rex_base_universe_d2_035_rex_basefill_035'], 'func': rex_base_universe_d3_035_rex_basefill_035}


def rex_base_universe_d3_036_rex_basefill_036(rex_base_universe_d2_036_rex_basefill_036):
    return _base_universe_d3(rex_base_universe_d2_036_rex_basefill_036, 36)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_036_rex_basefill_036'] = {'inputs': ['rex_base_universe_d2_036_rex_basefill_036'], 'func': rex_base_universe_d3_036_rex_basefill_036}


def rex_base_universe_d3_037_rex_basefill_037(rex_base_universe_d2_037_rex_basefill_037):
    return _base_universe_d3(rex_base_universe_d2_037_rex_basefill_037, 37)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_037_rex_basefill_037'] = {'inputs': ['rex_base_universe_d2_037_rex_basefill_037'], 'func': rex_base_universe_d3_037_rex_basefill_037}


def rex_base_universe_d3_038_rex_basefill_038(rex_base_universe_d2_038_rex_basefill_038):
    return _base_universe_d3(rex_base_universe_d2_038_rex_basefill_038, 38)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_038_rex_basefill_038'] = {'inputs': ['rex_base_universe_d2_038_rex_basefill_038'], 'func': rex_base_universe_d3_038_rex_basefill_038}


def rex_base_universe_d3_039_rex_basefill_039(rex_base_universe_d2_039_rex_basefill_039):
    return _base_universe_d3(rex_base_universe_d2_039_rex_basefill_039, 39)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_039_rex_basefill_039'] = {'inputs': ['rex_base_universe_d2_039_rex_basefill_039'], 'func': rex_base_universe_d3_039_rex_basefill_039}


def rex_base_universe_d3_040_rex_basefill_040(rex_base_universe_d2_040_rex_basefill_040):
    return _base_universe_d3(rex_base_universe_d2_040_rex_basefill_040, 40)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_040_rex_basefill_040'] = {'inputs': ['rex_base_universe_d2_040_rex_basefill_040'], 'func': rex_base_universe_d3_040_rex_basefill_040}


def rex_base_universe_d3_041_rex_basefill_041(rex_base_universe_d2_041_rex_basefill_041):
    return _base_universe_d3(rex_base_universe_d2_041_rex_basefill_041, 41)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_041_rex_basefill_041'] = {'inputs': ['rex_base_universe_d2_041_rex_basefill_041'], 'func': rex_base_universe_d3_041_rex_basefill_041}


def rex_base_universe_d3_042_rex_basefill_042(rex_base_universe_d2_042_rex_basefill_042):
    return _base_universe_d3(rex_base_universe_d2_042_rex_basefill_042, 42)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_042_rex_basefill_042'] = {'inputs': ['rex_base_universe_d2_042_rex_basefill_042'], 'func': rex_base_universe_d3_042_rex_basefill_042}


def rex_base_universe_d3_043_rex_basefill_043(rex_base_universe_d2_043_rex_basefill_043):
    return _base_universe_d3(rex_base_universe_d2_043_rex_basefill_043, 43)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_043_rex_basefill_043'] = {'inputs': ['rex_base_universe_d2_043_rex_basefill_043'], 'func': rex_base_universe_d3_043_rex_basefill_043}


def rex_base_universe_d3_044_rex_basefill_044(rex_base_universe_d2_044_rex_basefill_044):
    return _base_universe_d3(rex_base_universe_d2_044_rex_basefill_044, 44)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_044_rex_basefill_044'] = {'inputs': ['rex_base_universe_d2_044_rex_basefill_044'], 'func': rex_base_universe_d3_044_rex_basefill_044}


def rex_base_universe_d3_045_rex_basefill_045(rex_base_universe_d2_045_rex_basefill_045):
    return _base_universe_d3(rex_base_universe_d2_045_rex_basefill_045, 45)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_045_rex_basefill_045'] = {'inputs': ['rex_base_universe_d2_045_rex_basefill_045'], 'func': rex_base_universe_d3_045_rex_basefill_045}


def rex_base_universe_d3_046_rex_basefill_046(rex_base_universe_d2_046_rex_basefill_046):
    return _base_universe_d3(rex_base_universe_d2_046_rex_basefill_046, 46)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_046_rex_basefill_046'] = {'inputs': ['rex_base_universe_d2_046_rex_basefill_046'], 'func': rex_base_universe_d3_046_rex_basefill_046}


def rex_base_universe_d3_047_rex_basefill_047(rex_base_universe_d2_047_rex_basefill_047):
    return _base_universe_d3(rex_base_universe_d2_047_rex_basefill_047, 47)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_047_rex_basefill_047'] = {'inputs': ['rex_base_universe_d2_047_rex_basefill_047'], 'func': rex_base_universe_d3_047_rex_basefill_047}


def rex_base_universe_d3_048_rex_basefill_048(rex_base_universe_d2_048_rex_basefill_048):
    return _base_universe_d3(rex_base_universe_d2_048_rex_basefill_048, 48)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_048_rex_basefill_048'] = {'inputs': ['rex_base_universe_d2_048_rex_basefill_048'], 'func': rex_base_universe_d3_048_rex_basefill_048}


def rex_base_universe_d3_049_rex_basefill_049(rex_base_universe_d2_049_rex_basefill_049):
    return _base_universe_d3(rex_base_universe_d2_049_rex_basefill_049, 49)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_049_rex_basefill_049'] = {'inputs': ['rex_base_universe_d2_049_rex_basefill_049'], 'func': rex_base_universe_d3_049_rex_basefill_049}


def rex_base_universe_d3_050_rex_basefill_050(rex_base_universe_d2_050_rex_basefill_050):
    return _base_universe_d3(rex_base_universe_d2_050_rex_basefill_050, 50)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_050_rex_basefill_050'] = {'inputs': ['rex_base_universe_d2_050_rex_basefill_050'], 'func': rex_base_universe_d3_050_rex_basefill_050}


def rex_base_universe_d3_051_rex_basefill_051(rex_base_universe_d2_051_rex_basefill_051):
    return _base_universe_d3(rex_base_universe_d2_051_rex_basefill_051, 51)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_051_rex_basefill_051'] = {'inputs': ['rex_base_universe_d2_051_rex_basefill_051'], 'func': rex_base_universe_d3_051_rex_basefill_051}


def rex_base_universe_d3_052_rex_basefill_052(rex_base_universe_d2_052_rex_basefill_052):
    return _base_universe_d3(rex_base_universe_d2_052_rex_basefill_052, 52)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_052_rex_basefill_052'] = {'inputs': ['rex_base_universe_d2_052_rex_basefill_052'], 'func': rex_base_universe_d3_052_rex_basefill_052}


def rex_base_universe_d3_053_rex_basefill_053(rex_base_universe_d2_053_rex_basefill_053):
    return _base_universe_d3(rex_base_universe_d2_053_rex_basefill_053, 53)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_053_rex_basefill_053'] = {'inputs': ['rex_base_universe_d2_053_rex_basefill_053'], 'func': rex_base_universe_d3_053_rex_basefill_053}


def rex_base_universe_d3_054_rex_basefill_054(rex_base_universe_d2_054_rex_basefill_054):
    return _base_universe_d3(rex_base_universe_d2_054_rex_basefill_054, 54)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_054_rex_basefill_054'] = {'inputs': ['rex_base_universe_d2_054_rex_basefill_054'], 'func': rex_base_universe_d3_054_rex_basefill_054}


def rex_base_universe_d3_055_rex_basefill_055(rex_base_universe_d2_055_rex_basefill_055):
    return _base_universe_d3(rex_base_universe_d2_055_rex_basefill_055, 55)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_055_rex_basefill_055'] = {'inputs': ['rex_base_universe_d2_055_rex_basefill_055'], 'func': rex_base_universe_d3_055_rex_basefill_055}


def rex_base_universe_d3_056_rex_basefill_056(rex_base_universe_d2_056_rex_basefill_056):
    return _base_universe_d3(rex_base_universe_d2_056_rex_basefill_056, 56)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_056_rex_basefill_056'] = {'inputs': ['rex_base_universe_d2_056_rex_basefill_056'], 'func': rex_base_universe_d3_056_rex_basefill_056}


def rex_base_universe_d3_057_rex_basefill_057(rex_base_universe_d2_057_rex_basefill_057):
    return _base_universe_d3(rex_base_universe_d2_057_rex_basefill_057, 57)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_057_rex_basefill_057'] = {'inputs': ['rex_base_universe_d2_057_rex_basefill_057'], 'func': rex_base_universe_d3_057_rex_basefill_057}


def rex_base_universe_d3_058_rex_basefill_058(rex_base_universe_d2_058_rex_basefill_058):
    return _base_universe_d3(rex_base_universe_d2_058_rex_basefill_058, 58)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_058_rex_basefill_058'] = {'inputs': ['rex_base_universe_d2_058_rex_basefill_058'], 'func': rex_base_universe_d3_058_rex_basefill_058}


def rex_base_universe_d3_059_rex_basefill_059(rex_base_universe_d2_059_rex_basefill_059):
    return _base_universe_d3(rex_base_universe_d2_059_rex_basefill_059, 59)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_059_rex_basefill_059'] = {'inputs': ['rex_base_universe_d2_059_rex_basefill_059'], 'func': rex_base_universe_d3_059_rex_basefill_059}


def rex_base_universe_d3_060_rex_basefill_060(rex_base_universe_d2_060_rex_basefill_060):
    return _base_universe_d3(rex_base_universe_d2_060_rex_basefill_060, 60)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_060_rex_basefill_060'] = {'inputs': ['rex_base_universe_d2_060_rex_basefill_060'], 'func': rex_base_universe_d3_060_rex_basefill_060}


def rex_base_universe_d3_061_rex_basefill_061(rex_base_universe_d2_061_rex_basefill_061):
    return _base_universe_d3(rex_base_universe_d2_061_rex_basefill_061, 61)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_061_rex_basefill_061'] = {'inputs': ['rex_base_universe_d2_061_rex_basefill_061'], 'func': rex_base_universe_d3_061_rex_basefill_061}


def rex_base_universe_d3_062_rex_basefill_062(rex_base_universe_d2_062_rex_basefill_062):
    return _base_universe_d3(rex_base_universe_d2_062_rex_basefill_062, 62)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_062_rex_basefill_062'] = {'inputs': ['rex_base_universe_d2_062_rex_basefill_062'], 'func': rex_base_universe_d3_062_rex_basefill_062}


def rex_base_universe_d3_063_rex_basefill_063(rex_base_universe_d2_063_rex_basefill_063):
    return _base_universe_d3(rex_base_universe_d2_063_rex_basefill_063, 63)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_063_rex_basefill_063'] = {'inputs': ['rex_base_universe_d2_063_rex_basefill_063'], 'func': rex_base_universe_d3_063_rex_basefill_063}


def rex_base_universe_d3_064_rex_basefill_064(rex_base_universe_d2_064_rex_basefill_064):
    return _base_universe_d3(rex_base_universe_d2_064_rex_basefill_064, 64)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_064_rex_basefill_064'] = {'inputs': ['rex_base_universe_d2_064_rex_basefill_064'], 'func': rex_base_universe_d3_064_rex_basefill_064}


def rex_base_universe_d3_065_rex_basefill_065(rex_base_universe_d2_065_rex_basefill_065):
    return _base_universe_d3(rex_base_universe_d2_065_rex_basefill_065, 65)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_065_rex_basefill_065'] = {'inputs': ['rex_base_universe_d2_065_rex_basefill_065'], 'func': rex_base_universe_d3_065_rex_basefill_065}


def rex_base_universe_d3_066_rex_basefill_066(rex_base_universe_d2_066_rex_basefill_066):
    return _base_universe_d3(rex_base_universe_d2_066_rex_basefill_066, 66)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_066_rex_basefill_066'] = {'inputs': ['rex_base_universe_d2_066_rex_basefill_066'], 'func': rex_base_universe_d3_066_rex_basefill_066}


def rex_base_universe_d3_067_rex_basefill_067(rex_base_universe_d2_067_rex_basefill_067):
    return _base_universe_d3(rex_base_universe_d2_067_rex_basefill_067, 67)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_067_rex_basefill_067'] = {'inputs': ['rex_base_universe_d2_067_rex_basefill_067'], 'func': rex_base_universe_d3_067_rex_basefill_067}


def rex_base_universe_d3_068_rex_basefill_068(rex_base_universe_d2_068_rex_basefill_068):
    return _base_universe_d3(rex_base_universe_d2_068_rex_basefill_068, 68)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_068_rex_basefill_068'] = {'inputs': ['rex_base_universe_d2_068_rex_basefill_068'], 'func': rex_base_universe_d3_068_rex_basefill_068}


def rex_base_universe_d3_069_rex_basefill_069(rex_base_universe_d2_069_rex_basefill_069):
    return _base_universe_d3(rex_base_universe_d2_069_rex_basefill_069, 69)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_069_rex_basefill_069'] = {'inputs': ['rex_base_universe_d2_069_rex_basefill_069'], 'func': rex_base_universe_d3_069_rex_basefill_069}


def rex_base_universe_d3_070_rex_basefill_070(rex_base_universe_d2_070_rex_basefill_070):
    return _base_universe_d3(rex_base_universe_d2_070_rex_basefill_070, 70)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_070_rex_basefill_070'] = {'inputs': ['rex_base_universe_d2_070_rex_basefill_070'], 'func': rex_base_universe_d3_070_rex_basefill_070}


def rex_base_universe_d3_071_rex_basefill_071(rex_base_universe_d2_071_rex_basefill_071):
    return _base_universe_d3(rex_base_universe_d2_071_rex_basefill_071, 71)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_071_rex_basefill_071'] = {'inputs': ['rex_base_universe_d2_071_rex_basefill_071'], 'func': rex_base_universe_d3_071_rex_basefill_071}


def rex_base_universe_d3_072_rex_basefill_072(rex_base_universe_d2_072_rex_basefill_072):
    return _base_universe_d3(rex_base_universe_d2_072_rex_basefill_072, 72)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_072_rex_basefill_072'] = {'inputs': ['rex_base_universe_d2_072_rex_basefill_072'], 'func': rex_base_universe_d3_072_rex_basefill_072}


def rex_base_universe_d3_073_rex_basefill_073(rex_base_universe_d2_073_rex_basefill_073):
    return _base_universe_d3(rex_base_universe_d2_073_rex_basefill_073, 73)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_073_rex_basefill_073'] = {'inputs': ['rex_base_universe_d2_073_rex_basefill_073'], 'func': rex_base_universe_d3_073_rex_basefill_073}


def rex_base_universe_d3_074_rex_basefill_074(rex_base_universe_d2_074_rex_basefill_074):
    return _base_universe_d3(rex_base_universe_d2_074_rex_basefill_074, 74)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_074_rex_basefill_074'] = {'inputs': ['rex_base_universe_d2_074_rex_basefill_074'], 'func': rex_base_universe_d3_074_rex_basefill_074}


def rex_base_universe_d3_075_rex_basefill_075(rex_base_universe_d2_075_rex_basefill_075):
    return _base_universe_d3(rex_base_universe_d2_075_rex_basefill_075, 75)
REX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rex_base_universe_d3_075_rex_basefill_075'] = {'inputs': ['rex_base_universe_d2_075_rex_basefill_075'], 'func': rex_base_universe_d3_075_rex_basefill_075}
