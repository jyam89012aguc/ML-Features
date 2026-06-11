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



def zvd_001_amihud_illiquidity_accel_1(zvd_001_amihud_illiquidity_roc_1):
    feature = _s(zvd_001_amihud_illiquidity_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def zvd_007_amihud_illiquidity_accel_5(zvd_007_amihud_illiquidity_roc_5):
    feature = _s(zvd_007_amihud_illiquidity_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def zvd_013_amihud_illiquidity_accel_42(zvd_013_amihud_illiquidity_roc_42):
    feature = _s(zvd_013_amihud_illiquidity_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def zvd_179_zvd_019_amihud_illiquidity_42_019_accel_126(zvd_154_zvd_019_amihud_illiquidity_42_019_roc_126):
    feature = _s(zvd_154_zvd_019_amihud_illiquidity_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def zvd_180_zvd_025_amihud_illiquidity_378_025_accel_378(zvd_155_zvd_025_amihud_illiquidity_378_025_roc_378):
    feature = _s(zvd_155_zvd_025_amihud_illiquidity_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















ZERO_VOLUME_DAYS_REGISTRY_3RD_DERIVATIVES = {
    'zvd_001_amihud_illiquidity_accel_1': {'inputs': ['zvd_001_amihud_illiquidity_roc_1'], 'func': zvd_001_amihud_illiquidity_accel_1},
    'zvd_007_amihud_illiquidity_accel_5': {'inputs': ['zvd_007_amihud_illiquidity_roc_5'], 'func': zvd_007_amihud_illiquidity_accel_5},
    'zvd_013_amihud_illiquidity_accel_42': {'inputs': ['zvd_013_amihud_illiquidity_roc_42'], 'func': zvd_013_amihud_illiquidity_accel_42},
    'zvd_179_zvd_019_amihud_illiquidity_42_019_accel_126': {'inputs': ['zvd_154_zvd_019_amihud_illiquidity_42_019_roc_126'], 'func': zvd_179_zvd_019_amihud_illiquidity_42_019_accel_126},
    'zvd_180_zvd_025_amihud_illiquidity_378_025_accel_378': {'inputs': ['zvd_155_zvd_025_amihud_illiquidity_378_025_roc_378'], 'func': zvd_180_zvd_025_amihud_illiquidity_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def zvd_replacement_d3_001(zvd_replacement_d2_001):
    feature = _clean(zvd_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_001'] = {'inputs': ['zvd_replacement_d2_001'], 'func': zvd_replacement_d3_001}


def zvd_replacement_d3_002(zvd_replacement_d2_002):
    feature = _clean(zvd_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_002'] = {'inputs': ['zvd_replacement_d2_002'], 'func': zvd_replacement_d3_002}


def zvd_replacement_d3_003(zvd_replacement_d2_003):
    feature = _clean(zvd_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_003'] = {'inputs': ['zvd_replacement_d2_003'], 'func': zvd_replacement_d3_003}


def zvd_replacement_d3_004(zvd_replacement_d2_004):
    feature = _clean(zvd_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_004'] = {'inputs': ['zvd_replacement_d2_004'], 'func': zvd_replacement_d3_004}


def zvd_replacement_d3_005(zvd_replacement_d2_005):
    feature = _clean(zvd_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_005'] = {'inputs': ['zvd_replacement_d2_005'], 'func': zvd_replacement_d3_005}


def zvd_replacement_d3_006(zvd_replacement_d2_006):
    feature = _clean(zvd_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_006'] = {'inputs': ['zvd_replacement_d2_006'], 'func': zvd_replacement_d3_006}


def zvd_replacement_d3_007(zvd_replacement_d2_007):
    feature = _clean(zvd_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_007'] = {'inputs': ['zvd_replacement_d2_007'], 'func': zvd_replacement_d3_007}


def zvd_replacement_d3_008(zvd_replacement_d2_008):
    feature = _clean(zvd_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_008'] = {'inputs': ['zvd_replacement_d2_008'], 'func': zvd_replacement_d3_008}


def zvd_replacement_d3_009(zvd_replacement_d2_009):
    feature = _clean(zvd_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_009'] = {'inputs': ['zvd_replacement_d2_009'], 'func': zvd_replacement_d3_009}


def zvd_replacement_d3_010(zvd_replacement_d2_010):
    feature = _clean(zvd_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_010'] = {'inputs': ['zvd_replacement_d2_010'], 'func': zvd_replacement_d3_010}


def zvd_replacement_d3_011(zvd_replacement_d2_011):
    feature = _clean(zvd_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_011'] = {'inputs': ['zvd_replacement_d2_011'], 'func': zvd_replacement_d3_011}


def zvd_replacement_d3_012(zvd_replacement_d2_012):
    feature = _clean(zvd_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_012'] = {'inputs': ['zvd_replacement_d2_012'], 'func': zvd_replacement_d3_012}


def zvd_replacement_d3_013(zvd_replacement_d2_013):
    feature = _clean(zvd_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_013'] = {'inputs': ['zvd_replacement_d2_013'], 'func': zvd_replacement_d3_013}


def zvd_replacement_d3_014(zvd_replacement_d2_014):
    feature = _clean(zvd_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_014'] = {'inputs': ['zvd_replacement_d2_014'], 'func': zvd_replacement_d3_014}


def zvd_replacement_d3_015(zvd_replacement_d2_015):
    feature = _clean(zvd_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_015'] = {'inputs': ['zvd_replacement_d2_015'], 'func': zvd_replacement_d3_015}


def zvd_replacement_d3_016(zvd_replacement_d2_016):
    feature = _clean(zvd_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_016'] = {'inputs': ['zvd_replacement_d2_016'], 'func': zvd_replacement_d3_016}


def zvd_replacement_d3_017(zvd_replacement_d2_017):
    feature = _clean(zvd_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_017'] = {'inputs': ['zvd_replacement_d2_017'], 'func': zvd_replacement_d3_017}


def zvd_replacement_d3_018(zvd_replacement_d2_018):
    feature = _clean(zvd_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_018'] = {'inputs': ['zvd_replacement_d2_018'], 'func': zvd_replacement_d3_018}


def zvd_replacement_d3_019(zvd_replacement_d2_019):
    feature = _clean(zvd_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_019'] = {'inputs': ['zvd_replacement_d2_019'], 'func': zvd_replacement_d3_019}


def zvd_replacement_d3_020(zvd_replacement_d2_020):
    feature = _clean(zvd_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_020'] = {'inputs': ['zvd_replacement_d2_020'], 'func': zvd_replacement_d3_020}


def zvd_replacement_d3_021(zvd_replacement_d2_021):
    feature = _clean(zvd_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_021'] = {'inputs': ['zvd_replacement_d2_021'], 'func': zvd_replacement_d3_021}


def zvd_replacement_d3_022(zvd_replacement_d2_022):
    feature = _clean(zvd_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_022'] = {'inputs': ['zvd_replacement_d2_022'], 'func': zvd_replacement_d3_022}


def zvd_replacement_d3_023(zvd_replacement_d2_023):
    feature = _clean(zvd_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_023'] = {'inputs': ['zvd_replacement_d2_023'], 'func': zvd_replacement_d3_023}


def zvd_replacement_d3_024(zvd_replacement_d2_024):
    feature = _clean(zvd_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_024'] = {'inputs': ['zvd_replacement_d2_024'], 'func': zvd_replacement_d3_024}


def zvd_replacement_d3_025(zvd_replacement_d2_025):
    feature = _clean(zvd_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_025'] = {'inputs': ['zvd_replacement_d2_025'], 'func': zvd_replacement_d3_025}


def zvd_replacement_d3_026(zvd_replacement_d2_026):
    feature = _clean(zvd_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_026'] = {'inputs': ['zvd_replacement_d2_026'], 'func': zvd_replacement_d3_026}


def zvd_replacement_d3_027(zvd_replacement_d2_027):
    feature = _clean(zvd_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_027'] = {'inputs': ['zvd_replacement_d2_027'], 'func': zvd_replacement_d3_027}


def zvd_replacement_d3_028(zvd_replacement_d2_028):
    feature = _clean(zvd_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_028'] = {'inputs': ['zvd_replacement_d2_028'], 'func': zvd_replacement_d3_028}


def zvd_replacement_d3_029(zvd_replacement_d2_029):
    feature = _clean(zvd_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_029'] = {'inputs': ['zvd_replacement_d2_029'], 'func': zvd_replacement_d3_029}


def zvd_replacement_d3_030(zvd_replacement_d2_030):
    feature = _clean(zvd_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_030'] = {'inputs': ['zvd_replacement_d2_030'], 'func': zvd_replacement_d3_030}


def zvd_replacement_d3_031(zvd_replacement_d2_031):
    feature = _clean(zvd_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_031'] = {'inputs': ['zvd_replacement_d2_031'], 'func': zvd_replacement_d3_031}


def zvd_replacement_d3_032(zvd_replacement_d2_032):
    feature = _clean(zvd_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_032'] = {'inputs': ['zvd_replacement_d2_032'], 'func': zvd_replacement_d3_032}


def zvd_replacement_d3_033(zvd_replacement_d2_033):
    feature = _clean(zvd_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_033'] = {'inputs': ['zvd_replacement_d2_033'], 'func': zvd_replacement_d3_033}


def zvd_replacement_d3_034(zvd_replacement_d2_034):
    feature = _clean(zvd_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_034'] = {'inputs': ['zvd_replacement_d2_034'], 'func': zvd_replacement_d3_034}


def zvd_replacement_d3_035(zvd_replacement_d2_035):
    feature = _clean(zvd_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_035'] = {'inputs': ['zvd_replacement_d2_035'], 'func': zvd_replacement_d3_035}


def zvd_replacement_d3_036(zvd_replacement_d2_036):
    feature = _clean(zvd_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_036'] = {'inputs': ['zvd_replacement_d2_036'], 'func': zvd_replacement_d3_036}


def zvd_replacement_d3_037(zvd_replacement_d2_037):
    feature = _clean(zvd_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_037'] = {'inputs': ['zvd_replacement_d2_037'], 'func': zvd_replacement_d3_037}


def zvd_replacement_d3_038(zvd_replacement_d2_038):
    feature = _clean(zvd_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_038'] = {'inputs': ['zvd_replacement_d2_038'], 'func': zvd_replacement_d3_038}


def zvd_replacement_d3_039(zvd_replacement_d2_039):
    feature = _clean(zvd_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_039'] = {'inputs': ['zvd_replacement_d2_039'], 'func': zvd_replacement_d3_039}


def zvd_replacement_d3_040(zvd_replacement_d2_040):
    feature = _clean(zvd_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_040'] = {'inputs': ['zvd_replacement_d2_040'], 'func': zvd_replacement_d3_040}


def zvd_replacement_d3_041(zvd_replacement_d2_041):
    feature = _clean(zvd_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_041'] = {'inputs': ['zvd_replacement_d2_041'], 'func': zvd_replacement_d3_041}


def zvd_replacement_d3_042(zvd_replacement_d2_042):
    feature = _clean(zvd_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_042'] = {'inputs': ['zvd_replacement_d2_042'], 'func': zvd_replacement_d3_042}


def zvd_replacement_d3_043(zvd_replacement_d2_043):
    feature = _clean(zvd_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_043'] = {'inputs': ['zvd_replacement_d2_043'], 'func': zvd_replacement_d3_043}


def zvd_replacement_d3_044(zvd_replacement_d2_044):
    feature = _clean(zvd_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_044'] = {'inputs': ['zvd_replacement_d2_044'], 'func': zvd_replacement_d3_044}


def zvd_replacement_d3_045(zvd_replacement_d2_045):
    feature = _clean(zvd_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_045'] = {'inputs': ['zvd_replacement_d2_045'], 'func': zvd_replacement_d3_045}


def zvd_replacement_d3_046(zvd_replacement_d2_046):
    feature = _clean(zvd_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_046'] = {'inputs': ['zvd_replacement_d2_046'], 'func': zvd_replacement_d3_046}


def zvd_replacement_d3_047(zvd_replacement_d2_047):
    feature = _clean(zvd_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_047'] = {'inputs': ['zvd_replacement_d2_047'], 'func': zvd_replacement_d3_047}


def zvd_replacement_d3_048(zvd_replacement_d2_048):
    feature = _clean(zvd_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_048'] = {'inputs': ['zvd_replacement_d2_048'], 'func': zvd_replacement_d3_048}


def zvd_replacement_d3_049(zvd_replacement_d2_049):
    feature = _clean(zvd_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_049'] = {'inputs': ['zvd_replacement_d2_049'], 'func': zvd_replacement_d3_049}


def zvd_replacement_d3_050(zvd_replacement_d2_050):
    feature = _clean(zvd_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_050'] = {'inputs': ['zvd_replacement_d2_050'], 'func': zvd_replacement_d3_050}


def zvd_replacement_d3_051(zvd_replacement_d2_051):
    feature = _clean(zvd_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_051'] = {'inputs': ['zvd_replacement_d2_051'], 'func': zvd_replacement_d3_051}


def zvd_replacement_d3_052(zvd_replacement_d2_052):
    feature = _clean(zvd_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_052'] = {'inputs': ['zvd_replacement_d2_052'], 'func': zvd_replacement_d3_052}


def zvd_replacement_d3_053(zvd_replacement_d2_053):
    feature = _clean(zvd_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_053'] = {'inputs': ['zvd_replacement_d2_053'], 'func': zvd_replacement_d3_053}


def zvd_replacement_d3_054(zvd_replacement_d2_054):
    feature = _clean(zvd_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_054'] = {'inputs': ['zvd_replacement_d2_054'], 'func': zvd_replacement_d3_054}


def zvd_replacement_d3_055(zvd_replacement_d2_055):
    feature = _clean(zvd_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_055'] = {'inputs': ['zvd_replacement_d2_055'], 'func': zvd_replacement_d3_055}


def zvd_replacement_d3_056(zvd_replacement_d2_056):
    feature = _clean(zvd_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_056'] = {'inputs': ['zvd_replacement_d2_056'], 'func': zvd_replacement_d3_056}


def zvd_replacement_d3_057(zvd_replacement_d2_057):
    feature = _clean(zvd_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_057'] = {'inputs': ['zvd_replacement_d2_057'], 'func': zvd_replacement_d3_057}


def zvd_replacement_d3_058(zvd_replacement_d2_058):
    feature = _clean(zvd_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_058'] = {'inputs': ['zvd_replacement_d2_058'], 'func': zvd_replacement_d3_058}


def zvd_replacement_d3_059(zvd_replacement_d2_059):
    feature = _clean(zvd_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_059'] = {'inputs': ['zvd_replacement_d2_059'], 'func': zvd_replacement_d3_059}


def zvd_replacement_d3_060(zvd_replacement_d2_060):
    feature = _clean(zvd_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_060'] = {'inputs': ['zvd_replacement_d2_060'], 'func': zvd_replacement_d3_060}


def zvd_replacement_d3_061(zvd_replacement_d2_061):
    feature = _clean(zvd_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_061'] = {'inputs': ['zvd_replacement_d2_061'], 'func': zvd_replacement_d3_061}


def zvd_replacement_d3_062(zvd_replacement_d2_062):
    feature = _clean(zvd_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_062'] = {'inputs': ['zvd_replacement_d2_062'], 'func': zvd_replacement_d3_062}


def zvd_replacement_d3_063(zvd_replacement_d2_063):
    feature = _clean(zvd_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_063'] = {'inputs': ['zvd_replacement_d2_063'], 'func': zvd_replacement_d3_063}


def zvd_replacement_d3_064(zvd_replacement_d2_064):
    feature = _clean(zvd_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_064'] = {'inputs': ['zvd_replacement_d2_064'], 'func': zvd_replacement_d3_064}


def zvd_replacement_d3_065(zvd_replacement_d2_065):
    feature = _clean(zvd_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_065'] = {'inputs': ['zvd_replacement_d2_065'], 'func': zvd_replacement_d3_065}


def zvd_replacement_d3_066(zvd_replacement_d2_066):
    feature = _clean(zvd_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_066'] = {'inputs': ['zvd_replacement_d2_066'], 'func': zvd_replacement_d3_066}


def zvd_replacement_d3_067(zvd_replacement_d2_067):
    feature = _clean(zvd_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_067'] = {'inputs': ['zvd_replacement_d2_067'], 'func': zvd_replacement_d3_067}


def zvd_replacement_d3_068(zvd_replacement_d2_068):
    feature = _clean(zvd_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_068'] = {'inputs': ['zvd_replacement_d2_068'], 'func': zvd_replacement_d3_068}


def zvd_replacement_d3_069(zvd_replacement_d2_069):
    feature = _clean(zvd_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_069'] = {'inputs': ['zvd_replacement_d2_069'], 'func': zvd_replacement_d3_069}


def zvd_replacement_d3_070(zvd_replacement_d2_070):
    feature = _clean(zvd_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_070'] = {'inputs': ['zvd_replacement_d2_070'], 'func': zvd_replacement_d3_070}


def zvd_replacement_d3_071(zvd_replacement_d2_071):
    feature = _clean(zvd_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_071'] = {'inputs': ['zvd_replacement_d2_071'], 'func': zvd_replacement_d3_071}


def zvd_replacement_d3_072(zvd_replacement_d2_072):
    feature = _clean(zvd_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_072'] = {'inputs': ['zvd_replacement_d2_072'], 'func': zvd_replacement_d3_072}


def zvd_replacement_d3_073(zvd_replacement_d2_073):
    feature = _clean(zvd_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_073'] = {'inputs': ['zvd_replacement_d2_073'], 'func': zvd_replacement_d3_073}


def zvd_replacement_d3_074(zvd_replacement_d2_074):
    feature = _clean(zvd_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_074'] = {'inputs': ['zvd_replacement_d2_074'], 'func': zvd_replacement_d3_074}


def zvd_replacement_d3_075(zvd_replacement_d2_075):
    feature = _clean(zvd_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_075'] = {'inputs': ['zvd_replacement_d2_075'], 'func': zvd_replacement_d3_075}


def zvd_replacement_d3_076(zvd_replacement_d2_076):
    feature = _clean(zvd_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_076'] = {'inputs': ['zvd_replacement_d2_076'], 'func': zvd_replacement_d3_076}


def zvd_replacement_d3_077(zvd_replacement_d2_077):
    feature = _clean(zvd_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_077'] = {'inputs': ['zvd_replacement_d2_077'], 'func': zvd_replacement_d3_077}


def zvd_replacement_d3_078(zvd_replacement_d2_078):
    feature = _clean(zvd_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_078'] = {'inputs': ['zvd_replacement_d2_078'], 'func': zvd_replacement_d3_078}


def zvd_replacement_d3_079(zvd_replacement_d2_079):
    feature = _clean(zvd_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_079'] = {'inputs': ['zvd_replacement_d2_079'], 'func': zvd_replacement_d3_079}


def zvd_replacement_d3_080(zvd_replacement_d2_080):
    feature = _clean(zvd_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_080'] = {'inputs': ['zvd_replacement_d2_080'], 'func': zvd_replacement_d3_080}


def zvd_replacement_d3_081(zvd_replacement_d2_081):
    feature = _clean(zvd_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_081'] = {'inputs': ['zvd_replacement_d2_081'], 'func': zvd_replacement_d3_081}


def zvd_replacement_d3_082(zvd_replacement_d2_082):
    feature = _clean(zvd_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_082'] = {'inputs': ['zvd_replacement_d2_082'], 'func': zvd_replacement_d3_082}


def zvd_replacement_d3_083(zvd_replacement_d2_083):
    feature = _clean(zvd_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_083'] = {'inputs': ['zvd_replacement_d2_083'], 'func': zvd_replacement_d3_083}


def zvd_replacement_d3_084(zvd_replacement_d2_084):
    feature = _clean(zvd_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_084'] = {'inputs': ['zvd_replacement_d2_084'], 'func': zvd_replacement_d3_084}


def zvd_replacement_d3_085(zvd_replacement_d2_085):
    feature = _clean(zvd_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_085'] = {'inputs': ['zvd_replacement_d2_085'], 'func': zvd_replacement_d3_085}


def zvd_replacement_d3_086(zvd_replacement_d2_086):
    feature = _clean(zvd_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_086'] = {'inputs': ['zvd_replacement_d2_086'], 'func': zvd_replacement_d3_086}


def zvd_replacement_d3_087(zvd_replacement_d2_087):
    feature = _clean(zvd_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_087'] = {'inputs': ['zvd_replacement_d2_087'], 'func': zvd_replacement_d3_087}


def zvd_replacement_d3_088(zvd_replacement_d2_088):
    feature = _clean(zvd_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_088'] = {'inputs': ['zvd_replacement_d2_088'], 'func': zvd_replacement_d3_088}


def zvd_replacement_d3_089(zvd_replacement_d2_089):
    feature = _clean(zvd_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_089'] = {'inputs': ['zvd_replacement_d2_089'], 'func': zvd_replacement_d3_089}


def zvd_replacement_d3_090(zvd_replacement_d2_090):
    feature = _clean(zvd_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_090'] = {'inputs': ['zvd_replacement_d2_090'], 'func': zvd_replacement_d3_090}


def zvd_replacement_d3_091(zvd_replacement_d2_091):
    feature = _clean(zvd_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_091'] = {'inputs': ['zvd_replacement_d2_091'], 'func': zvd_replacement_d3_091}


def zvd_replacement_d3_092(zvd_replacement_d2_092):
    feature = _clean(zvd_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_092'] = {'inputs': ['zvd_replacement_d2_092'], 'func': zvd_replacement_d3_092}


def zvd_replacement_d3_093(zvd_replacement_d2_093):
    feature = _clean(zvd_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_093'] = {'inputs': ['zvd_replacement_d2_093'], 'func': zvd_replacement_d3_093}


def zvd_replacement_d3_094(zvd_replacement_d2_094):
    feature = _clean(zvd_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_094'] = {'inputs': ['zvd_replacement_d2_094'], 'func': zvd_replacement_d3_094}


def zvd_replacement_d3_095(zvd_replacement_d2_095):
    feature = _clean(zvd_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_095'] = {'inputs': ['zvd_replacement_d2_095'], 'func': zvd_replacement_d3_095}


def zvd_replacement_d3_096(zvd_replacement_d2_096):
    feature = _clean(zvd_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_096'] = {'inputs': ['zvd_replacement_d2_096'], 'func': zvd_replacement_d3_096}


def zvd_replacement_d3_097(zvd_replacement_d2_097):
    feature = _clean(zvd_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_097'] = {'inputs': ['zvd_replacement_d2_097'], 'func': zvd_replacement_d3_097}


def zvd_replacement_d3_098(zvd_replacement_d2_098):
    feature = _clean(zvd_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_098'] = {'inputs': ['zvd_replacement_d2_098'], 'func': zvd_replacement_d3_098}


def zvd_replacement_d3_099(zvd_replacement_d2_099):
    feature = _clean(zvd_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_099'] = {'inputs': ['zvd_replacement_d2_099'], 'func': zvd_replacement_d3_099}


def zvd_replacement_d3_100(zvd_replacement_d2_100):
    feature = _clean(zvd_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_100'] = {'inputs': ['zvd_replacement_d2_100'], 'func': zvd_replacement_d3_100}


def zvd_replacement_d3_101(zvd_replacement_d2_101):
    feature = _clean(zvd_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_101'] = {'inputs': ['zvd_replacement_d2_101'], 'func': zvd_replacement_d3_101}


def zvd_replacement_d3_102(zvd_replacement_d2_102):
    feature = _clean(zvd_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_102'] = {'inputs': ['zvd_replacement_d2_102'], 'func': zvd_replacement_d3_102}


def zvd_replacement_d3_103(zvd_replacement_d2_103):
    feature = _clean(zvd_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_103'] = {'inputs': ['zvd_replacement_d2_103'], 'func': zvd_replacement_d3_103}


def zvd_replacement_d3_104(zvd_replacement_d2_104):
    feature = _clean(zvd_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_104'] = {'inputs': ['zvd_replacement_d2_104'], 'func': zvd_replacement_d3_104}


def zvd_replacement_d3_105(zvd_replacement_d2_105):
    feature = _clean(zvd_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_105'] = {'inputs': ['zvd_replacement_d2_105'], 'func': zvd_replacement_d3_105}


def zvd_replacement_d3_106(zvd_replacement_d2_106):
    feature = _clean(zvd_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_106'] = {'inputs': ['zvd_replacement_d2_106'], 'func': zvd_replacement_d3_106}


def zvd_replacement_d3_107(zvd_replacement_d2_107):
    feature = _clean(zvd_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_107'] = {'inputs': ['zvd_replacement_d2_107'], 'func': zvd_replacement_d3_107}


def zvd_replacement_d3_108(zvd_replacement_d2_108):
    feature = _clean(zvd_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_108'] = {'inputs': ['zvd_replacement_d2_108'], 'func': zvd_replacement_d3_108}


def zvd_replacement_d3_109(zvd_replacement_d2_109):
    feature = _clean(zvd_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_109'] = {'inputs': ['zvd_replacement_d2_109'], 'func': zvd_replacement_d3_109}


def zvd_replacement_d3_110(zvd_replacement_d2_110):
    feature = _clean(zvd_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_110'] = {'inputs': ['zvd_replacement_d2_110'], 'func': zvd_replacement_d3_110}


def zvd_replacement_d3_111(zvd_replacement_d2_111):
    feature = _clean(zvd_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_111'] = {'inputs': ['zvd_replacement_d2_111'], 'func': zvd_replacement_d3_111}


def zvd_replacement_d3_112(zvd_replacement_d2_112):
    feature = _clean(zvd_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_112'] = {'inputs': ['zvd_replacement_d2_112'], 'func': zvd_replacement_d3_112}


def zvd_replacement_d3_113(zvd_replacement_d2_113):
    feature = _clean(zvd_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_113'] = {'inputs': ['zvd_replacement_d2_113'], 'func': zvd_replacement_d3_113}


def zvd_replacement_d3_114(zvd_replacement_d2_114):
    feature = _clean(zvd_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_114'] = {'inputs': ['zvd_replacement_d2_114'], 'func': zvd_replacement_d3_114}


def zvd_replacement_d3_115(zvd_replacement_d2_115):
    feature = _clean(zvd_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_115'] = {'inputs': ['zvd_replacement_d2_115'], 'func': zvd_replacement_d3_115}


def zvd_replacement_d3_116(zvd_replacement_d2_116):
    feature = _clean(zvd_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_116'] = {'inputs': ['zvd_replacement_d2_116'], 'func': zvd_replacement_d3_116}


def zvd_replacement_d3_117(zvd_replacement_d2_117):
    feature = _clean(zvd_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_117'] = {'inputs': ['zvd_replacement_d2_117'], 'func': zvd_replacement_d3_117}


def zvd_replacement_d3_118(zvd_replacement_d2_118):
    feature = _clean(zvd_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_118'] = {'inputs': ['zvd_replacement_d2_118'], 'func': zvd_replacement_d3_118}


def zvd_replacement_d3_119(zvd_replacement_d2_119):
    feature = _clean(zvd_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_119'] = {'inputs': ['zvd_replacement_d2_119'], 'func': zvd_replacement_d3_119}


def zvd_replacement_d3_120(zvd_replacement_d2_120):
    feature = _clean(zvd_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_120'] = {'inputs': ['zvd_replacement_d2_120'], 'func': zvd_replacement_d3_120}


def zvd_replacement_d3_121(zvd_replacement_d2_121):
    feature = _clean(zvd_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_121'] = {'inputs': ['zvd_replacement_d2_121'], 'func': zvd_replacement_d3_121}


def zvd_replacement_d3_122(zvd_replacement_d2_122):
    feature = _clean(zvd_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_122'] = {'inputs': ['zvd_replacement_d2_122'], 'func': zvd_replacement_d3_122}


def zvd_replacement_d3_123(zvd_replacement_d2_123):
    feature = _clean(zvd_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_123'] = {'inputs': ['zvd_replacement_d2_123'], 'func': zvd_replacement_d3_123}


def zvd_replacement_d3_124(zvd_replacement_d2_124):
    feature = _clean(zvd_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_124'] = {'inputs': ['zvd_replacement_d2_124'], 'func': zvd_replacement_d3_124}


def zvd_replacement_d3_125(zvd_replacement_d2_125):
    feature = _clean(zvd_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_125'] = {'inputs': ['zvd_replacement_d2_125'], 'func': zvd_replacement_d3_125}


def zvd_replacement_d3_126(zvd_replacement_d2_126):
    feature = _clean(zvd_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_126'] = {'inputs': ['zvd_replacement_d2_126'], 'func': zvd_replacement_d3_126}


def zvd_replacement_d3_127(zvd_replacement_d2_127):
    feature = _clean(zvd_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_127'] = {'inputs': ['zvd_replacement_d2_127'], 'func': zvd_replacement_d3_127}


def zvd_replacement_d3_128(zvd_replacement_d2_128):
    feature = _clean(zvd_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_128'] = {'inputs': ['zvd_replacement_d2_128'], 'func': zvd_replacement_d3_128}


def zvd_replacement_d3_129(zvd_replacement_d2_129):
    feature = _clean(zvd_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_129'] = {'inputs': ['zvd_replacement_d2_129'], 'func': zvd_replacement_d3_129}


def zvd_replacement_d3_130(zvd_replacement_d2_130):
    feature = _clean(zvd_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_130'] = {'inputs': ['zvd_replacement_d2_130'], 'func': zvd_replacement_d3_130}


def zvd_replacement_d3_131(zvd_replacement_d2_131):
    feature = _clean(zvd_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_131'] = {'inputs': ['zvd_replacement_d2_131'], 'func': zvd_replacement_d3_131}


def zvd_replacement_d3_132(zvd_replacement_d2_132):
    feature = _clean(zvd_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_132'] = {'inputs': ['zvd_replacement_d2_132'], 'func': zvd_replacement_d3_132}


def zvd_replacement_d3_133(zvd_replacement_d2_133):
    feature = _clean(zvd_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_133'] = {'inputs': ['zvd_replacement_d2_133'], 'func': zvd_replacement_d3_133}


def zvd_replacement_d3_134(zvd_replacement_d2_134):
    feature = _clean(zvd_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_134'] = {'inputs': ['zvd_replacement_d2_134'], 'func': zvd_replacement_d3_134}


def zvd_replacement_d3_135(zvd_replacement_d2_135):
    feature = _clean(zvd_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_135'] = {'inputs': ['zvd_replacement_d2_135'], 'func': zvd_replacement_d3_135}


def zvd_replacement_d3_136(zvd_replacement_d2_136):
    feature = _clean(zvd_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_136'] = {'inputs': ['zvd_replacement_d2_136'], 'func': zvd_replacement_d3_136}


def zvd_replacement_d3_137(zvd_replacement_d2_137):
    feature = _clean(zvd_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_137'] = {'inputs': ['zvd_replacement_d2_137'], 'func': zvd_replacement_d3_137}


def zvd_replacement_d3_138(zvd_replacement_d2_138):
    feature = _clean(zvd_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_138'] = {'inputs': ['zvd_replacement_d2_138'], 'func': zvd_replacement_d3_138}


def zvd_replacement_d3_139(zvd_replacement_d2_139):
    feature = _clean(zvd_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_139'] = {'inputs': ['zvd_replacement_d2_139'], 'func': zvd_replacement_d3_139}


def zvd_replacement_d3_140(zvd_replacement_d2_140):
    feature = _clean(zvd_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_140'] = {'inputs': ['zvd_replacement_d2_140'], 'func': zvd_replacement_d3_140}


def zvd_replacement_d3_141(zvd_replacement_d2_141):
    feature = _clean(zvd_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_141'] = {'inputs': ['zvd_replacement_d2_141'], 'func': zvd_replacement_d3_141}


def zvd_replacement_d3_142(zvd_replacement_d2_142):
    feature = _clean(zvd_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_142'] = {'inputs': ['zvd_replacement_d2_142'], 'func': zvd_replacement_d3_142}


def zvd_replacement_d3_143(zvd_replacement_d2_143):
    feature = _clean(zvd_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_143'] = {'inputs': ['zvd_replacement_d2_143'], 'func': zvd_replacement_d3_143}


def zvd_replacement_d3_144(zvd_replacement_d2_144):
    feature = _clean(zvd_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_144'] = {'inputs': ['zvd_replacement_d2_144'], 'func': zvd_replacement_d3_144}


def zvd_replacement_d3_145(zvd_replacement_d2_145):
    feature = _clean(zvd_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_145'] = {'inputs': ['zvd_replacement_d2_145'], 'func': zvd_replacement_d3_145}


def zvd_replacement_d3_146(zvd_replacement_d2_146):
    feature = _clean(zvd_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_146'] = {'inputs': ['zvd_replacement_d2_146'], 'func': zvd_replacement_d3_146}


def zvd_replacement_d3_147(zvd_replacement_d2_147):
    feature = _clean(zvd_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_147'] = {'inputs': ['zvd_replacement_d2_147'], 'func': zvd_replacement_d3_147}


def zvd_replacement_d3_148(zvd_replacement_d2_148):
    feature = _clean(zvd_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_148'] = {'inputs': ['zvd_replacement_d2_148'], 'func': zvd_replacement_d3_148}


def zvd_replacement_d3_149(zvd_replacement_d2_149):
    feature = _clean(zvd_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_149'] = {'inputs': ['zvd_replacement_d2_149'], 'func': zvd_replacement_d3_149}


def zvd_replacement_d3_150(zvd_replacement_d2_150):
    feature = _clean(zvd_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_150'] = {'inputs': ['zvd_replacement_d2_150'], 'func': zvd_replacement_d3_150}


def zvd_replacement_d3_151(zvd_replacement_d2_151):
    feature = _clean(zvd_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_151'] = {'inputs': ['zvd_replacement_d2_151'], 'func': zvd_replacement_d3_151}


def zvd_replacement_d3_152(zvd_replacement_d2_152):
    feature = _clean(zvd_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_152'] = {'inputs': ['zvd_replacement_d2_152'], 'func': zvd_replacement_d3_152}


def zvd_replacement_d3_153(zvd_replacement_d2_153):
    feature = _clean(zvd_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_153'] = {'inputs': ['zvd_replacement_d2_153'], 'func': zvd_replacement_d3_153}


def zvd_replacement_d3_154(zvd_replacement_d2_154):
    feature = _clean(zvd_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_154'] = {'inputs': ['zvd_replacement_d2_154'], 'func': zvd_replacement_d3_154}


def zvd_replacement_d3_155(zvd_replacement_d2_155):
    feature = _clean(zvd_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_155'] = {'inputs': ['zvd_replacement_d2_155'], 'func': zvd_replacement_d3_155}


def zvd_replacement_d3_156(zvd_replacement_d2_156):
    feature = _clean(zvd_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_156'] = {'inputs': ['zvd_replacement_d2_156'], 'func': zvd_replacement_d3_156}


def zvd_replacement_d3_157(zvd_replacement_d2_157):
    feature = _clean(zvd_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_157'] = {'inputs': ['zvd_replacement_d2_157'], 'func': zvd_replacement_d3_157}


def zvd_replacement_d3_158(zvd_replacement_d2_158):
    feature = _clean(zvd_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_158'] = {'inputs': ['zvd_replacement_d2_158'], 'func': zvd_replacement_d3_158}


def zvd_replacement_d3_159(zvd_replacement_d2_159):
    feature = _clean(zvd_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_159'] = {'inputs': ['zvd_replacement_d2_159'], 'func': zvd_replacement_d3_159}


def zvd_replacement_d3_160(zvd_replacement_d2_160):
    feature = _clean(zvd_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_160'] = {'inputs': ['zvd_replacement_d2_160'], 'func': zvd_replacement_d3_160}


def zvd_replacement_d3_161(zvd_replacement_d2_161):
    feature = _clean(zvd_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_161'] = {'inputs': ['zvd_replacement_d2_161'], 'func': zvd_replacement_d3_161}


def zvd_replacement_d3_162(zvd_replacement_d2_162):
    feature = _clean(zvd_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_162'] = {'inputs': ['zvd_replacement_d2_162'], 'func': zvd_replacement_d3_162}


def zvd_replacement_d3_163(zvd_replacement_d2_163):
    feature = _clean(zvd_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_163'] = {'inputs': ['zvd_replacement_d2_163'], 'func': zvd_replacement_d3_163}


def zvd_replacement_d3_164(zvd_replacement_d2_164):
    feature = _clean(zvd_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_164'] = {'inputs': ['zvd_replacement_d2_164'], 'func': zvd_replacement_d3_164}


def zvd_replacement_d3_165(zvd_replacement_d2_165):
    feature = _clean(zvd_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_165'] = {'inputs': ['zvd_replacement_d2_165'], 'func': zvd_replacement_d3_165}


def zvd_replacement_d3_166(zvd_replacement_d2_166):
    feature = _clean(zvd_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_166'] = {'inputs': ['zvd_replacement_d2_166'], 'func': zvd_replacement_d3_166}


def zvd_replacement_d3_167(zvd_replacement_d2_167):
    feature = _clean(zvd_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_167'] = {'inputs': ['zvd_replacement_d2_167'], 'func': zvd_replacement_d3_167}


def zvd_replacement_d3_168(zvd_replacement_d2_168):
    feature = _clean(zvd_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_168'] = {'inputs': ['zvd_replacement_d2_168'], 'func': zvd_replacement_d3_168}


def zvd_replacement_d3_169(zvd_replacement_d2_169):
    feature = _clean(zvd_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_169'] = {'inputs': ['zvd_replacement_d2_169'], 'func': zvd_replacement_d3_169}


def zvd_replacement_d3_170(zvd_replacement_d2_170):
    feature = _clean(zvd_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
ZVD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['zvd_replacement_d3_170'] = {'inputs': ['zvd_replacement_d2_170'], 'func': zvd_replacement_d3_170}


# Third-derivative extensions for repaired first-base features.
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def zvd_base_universe_d3_001_zvd_002_zero_volume_frequency_10_002(zvd_base_universe_d2_001_zvd_002_zero_volume_frequency_10_002):
    return _base_universe_d3(zvd_base_universe_d2_001_zvd_002_zero_volume_frequency_10_002, 1)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_001_zvd_002_zero_volume_frequency_10_002'] = {'inputs': ['zvd_base_universe_d2_001_zvd_002_zero_volume_frequency_10_002'], 'func': zvd_base_universe_d3_001_zvd_002_zero_volume_frequency_10_002}


def zvd_base_universe_d3_002_zvd_003_spread_proxy_21_003(zvd_base_universe_d2_002_zvd_003_spread_proxy_21_003):
    return _base_universe_d3(zvd_base_universe_d2_002_zvd_003_spread_proxy_21_003, 2)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_002_zvd_003_spread_proxy_21_003'] = {'inputs': ['zvd_base_universe_d2_002_zvd_003_spread_proxy_21_003'], 'func': zvd_base_universe_d3_002_zvd_003_spread_proxy_21_003}


def zvd_base_universe_d3_003_zvd_004_trading_intensity_42_004(zvd_base_universe_d2_003_zvd_004_trading_intensity_42_004):
    return _base_universe_d3(zvd_base_universe_d2_003_zvd_004_trading_intensity_42_004, 3)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_003_zvd_004_trading_intensity_42_004'] = {'inputs': ['zvd_base_universe_d2_003_zvd_004_trading_intensity_42_004'], 'func': zvd_base_universe_d3_003_zvd_004_trading_intensity_42_004}


def zvd_base_universe_d3_004_zvd_006_price_level_distress_84_006(zvd_base_universe_d2_004_zvd_006_price_level_distress_84_006):
    return _base_universe_d3(zvd_base_universe_d2_004_zvd_006_price_level_distress_84_006, 4)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_004_zvd_006_price_level_distress_84_006'] = {'inputs': ['zvd_base_universe_d2_004_zvd_006_price_level_distress_84_006'], 'func': zvd_base_universe_d3_004_zvd_006_price_level_distress_84_006}


def zvd_base_universe_d3_005_zvd_008_zero_volume_frequency_189_008(zvd_base_universe_d2_005_zvd_008_zero_volume_frequency_189_008):
    return _base_universe_d3(zvd_base_universe_d2_005_zvd_008_zero_volume_frequency_189_008, 5)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_005_zvd_008_zero_volume_frequency_189_008'] = {'inputs': ['zvd_base_universe_d2_005_zvd_008_zero_volume_frequency_189_008'], 'func': zvd_base_universe_d3_005_zvd_008_zero_volume_frequency_189_008}


def zvd_base_universe_d3_006_zvd_009_spread_proxy_252_009(zvd_base_universe_d2_006_zvd_009_spread_proxy_252_009):
    return _base_universe_d3(zvd_base_universe_d2_006_zvd_009_spread_proxy_252_009, 6)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_006_zvd_009_spread_proxy_252_009'] = {'inputs': ['zvd_base_universe_d2_006_zvd_009_spread_proxy_252_009'], 'func': zvd_base_universe_d3_006_zvd_009_spread_proxy_252_009}


def zvd_base_universe_d3_007_zvd_010_trading_intensity_378_010(zvd_base_universe_d2_007_zvd_010_trading_intensity_378_010):
    return _base_universe_d3(zvd_base_universe_d2_007_zvd_010_trading_intensity_378_010, 7)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_007_zvd_010_trading_intensity_378_010'] = {'inputs': ['zvd_base_universe_d2_007_zvd_010_trading_intensity_378_010'], 'func': zvd_base_universe_d3_007_zvd_010_trading_intensity_378_010}


def zvd_base_universe_d3_008_zvd_012_price_level_distress_756_012(zvd_base_universe_d2_008_zvd_012_price_level_distress_756_012):
    return _base_universe_d3(zvd_base_universe_d2_008_zvd_012_price_level_distress_756_012, 8)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_008_zvd_012_price_level_distress_756_012'] = {'inputs': ['zvd_base_universe_d2_008_zvd_012_price_level_distress_756_012'], 'func': zvd_base_universe_d3_008_zvd_012_price_level_distress_756_012}


def zvd_base_universe_d3_009_zvd_014_zero_volume_frequency_1260_014(zvd_base_universe_d2_009_zvd_014_zero_volume_frequency_1260_014):
    return _base_universe_d3(zvd_base_universe_d2_009_zvd_014_zero_volume_frequency_1260_014, 9)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_009_zvd_014_zero_volume_frequency_1260_014'] = {'inputs': ['zvd_base_universe_d2_009_zvd_014_zero_volume_frequency_1260_014'], 'func': zvd_base_universe_d3_009_zvd_014_zero_volume_frequency_1260_014}


def zvd_base_universe_d3_010_zvd_015_spread_proxy_1512_015(zvd_base_universe_d2_010_zvd_015_spread_proxy_1512_015):
    return _base_universe_d3(zvd_base_universe_d2_010_zvd_015_spread_proxy_1512_015, 10)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_010_zvd_015_spread_proxy_1512_015'] = {'inputs': ['zvd_base_universe_d2_010_zvd_015_spread_proxy_1512_015'], 'func': zvd_base_universe_d3_010_zvd_015_spread_proxy_1512_015}


def zvd_base_universe_d3_011_zvd_016_trading_intensity_5_016(zvd_base_universe_d2_011_zvd_016_trading_intensity_5_016):
    return _base_universe_d3(zvd_base_universe_d2_011_zvd_016_trading_intensity_5_016, 11)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_011_zvd_016_trading_intensity_5_016'] = {'inputs': ['zvd_base_universe_d2_011_zvd_016_trading_intensity_5_016'], 'func': zvd_base_universe_d3_011_zvd_016_trading_intensity_5_016}


def zvd_base_universe_d3_012_zvd_018_price_level_distress_21_018(zvd_base_universe_d2_012_zvd_018_price_level_distress_21_018):
    return _base_universe_d3(zvd_base_universe_d2_012_zvd_018_price_level_distress_21_018, 12)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_012_zvd_018_price_level_distress_21_018'] = {'inputs': ['zvd_base_universe_d2_012_zvd_018_price_level_distress_21_018'], 'func': zvd_base_universe_d3_012_zvd_018_price_level_distress_21_018}


def zvd_base_universe_d3_013_zvd_020_zero_volume_frequency_63_020(zvd_base_universe_d2_013_zvd_020_zero_volume_frequency_63_020):
    return _base_universe_d3(zvd_base_universe_d2_013_zvd_020_zero_volume_frequency_63_020, 13)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_013_zvd_020_zero_volume_frequency_63_020'] = {'inputs': ['zvd_base_universe_d2_013_zvd_020_zero_volume_frequency_63_020'], 'func': zvd_base_universe_d3_013_zvd_020_zero_volume_frequency_63_020}


def zvd_base_universe_d3_014_zvd_021_spread_proxy_84_021(zvd_base_universe_d2_014_zvd_021_spread_proxy_84_021):
    return _base_universe_d3(zvd_base_universe_d2_014_zvd_021_spread_proxy_84_021, 14)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_014_zvd_021_spread_proxy_84_021'] = {'inputs': ['zvd_base_universe_d2_014_zvd_021_spread_proxy_84_021'], 'func': zvd_base_universe_d3_014_zvd_021_spread_proxy_84_021}


def zvd_base_universe_d3_015_zvd_022_trading_intensity_126_022(zvd_base_universe_d2_015_zvd_022_trading_intensity_126_022):
    return _base_universe_d3(zvd_base_universe_d2_015_zvd_022_trading_intensity_126_022, 15)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_015_zvd_022_trading_intensity_126_022'] = {'inputs': ['zvd_base_universe_d2_015_zvd_022_trading_intensity_126_022'], 'func': zvd_base_universe_d3_015_zvd_022_trading_intensity_126_022}


def zvd_base_universe_d3_016_zvd_024_price_level_distress_252_024(zvd_base_universe_d2_016_zvd_024_price_level_distress_252_024):
    return _base_universe_d3(zvd_base_universe_d2_016_zvd_024_price_level_distress_252_024, 16)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_016_zvd_024_price_level_distress_252_024'] = {'inputs': ['zvd_base_universe_d2_016_zvd_024_price_level_distress_252_024'], 'func': zvd_base_universe_d3_016_zvd_024_price_level_distress_252_024}


def zvd_base_universe_d3_017_zvd_026_zero_volume_frequency_504_026(zvd_base_universe_d2_017_zvd_026_zero_volume_frequency_504_026):
    return _base_universe_d3(zvd_base_universe_d2_017_zvd_026_zero_volume_frequency_504_026, 17)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_017_zvd_026_zero_volume_frequency_504_026'] = {'inputs': ['zvd_base_universe_d2_017_zvd_026_zero_volume_frequency_504_026'], 'func': zvd_base_universe_d3_017_zvd_026_zero_volume_frequency_504_026}


def zvd_base_universe_d3_018_zvd_027_spread_proxy_756_027(zvd_base_universe_d2_018_zvd_027_spread_proxy_756_027):
    return _base_universe_d3(zvd_base_universe_d2_018_zvd_027_spread_proxy_756_027, 18)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_018_zvd_027_spread_proxy_756_027'] = {'inputs': ['zvd_base_universe_d2_018_zvd_027_spread_proxy_756_027'], 'func': zvd_base_universe_d3_018_zvd_027_spread_proxy_756_027}


def zvd_base_universe_d3_019_zvd_028_trading_intensity_1008_028(zvd_base_universe_d2_019_zvd_028_trading_intensity_1008_028):
    return _base_universe_d3(zvd_base_universe_d2_019_zvd_028_trading_intensity_1008_028, 19)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_019_zvd_028_trading_intensity_1008_028'] = {'inputs': ['zvd_base_universe_d2_019_zvd_028_trading_intensity_1008_028'], 'func': zvd_base_universe_d3_019_zvd_028_trading_intensity_1008_028}


def zvd_base_universe_d3_020_zvd_030_price_level_distress_1512_030(zvd_base_universe_d2_020_zvd_030_price_level_distress_1512_030):
    return _base_universe_d3(zvd_base_universe_d2_020_zvd_030_price_level_distress_1512_030, 20)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_020_zvd_030_price_level_distress_1512_030'] = {'inputs': ['zvd_base_universe_d2_020_zvd_030_price_level_distress_1512_030'], 'func': zvd_base_universe_d3_020_zvd_030_price_level_distress_1512_030}


def zvd_base_universe_d3_021_zvd_basefill_001(zvd_base_universe_d2_021_zvd_basefill_001):
    return _base_universe_d3(zvd_base_universe_d2_021_zvd_basefill_001, 21)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_021_zvd_basefill_001'] = {'inputs': ['zvd_base_universe_d2_021_zvd_basefill_001'], 'func': zvd_base_universe_d3_021_zvd_basefill_001}


def zvd_base_universe_d3_022_zvd_basefill_005(zvd_base_universe_d2_022_zvd_basefill_005):
    return _base_universe_d3(zvd_base_universe_d2_022_zvd_basefill_005, 22)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_022_zvd_basefill_005'] = {'inputs': ['zvd_base_universe_d2_022_zvd_basefill_005'], 'func': zvd_base_universe_d3_022_zvd_basefill_005}


def zvd_base_universe_d3_023_zvd_basefill_007(zvd_base_universe_d2_023_zvd_basefill_007):
    return _base_universe_d3(zvd_base_universe_d2_023_zvd_basefill_007, 23)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_023_zvd_basefill_007'] = {'inputs': ['zvd_base_universe_d2_023_zvd_basefill_007'], 'func': zvd_base_universe_d3_023_zvd_basefill_007}


def zvd_base_universe_d3_024_zvd_basefill_011(zvd_base_universe_d2_024_zvd_basefill_011):
    return _base_universe_d3(zvd_base_universe_d2_024_zvd_basefill_011, 24)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_024_zvd_basefill_011'] = {'inputs': ['zvd_base_universe_d2_024_zvd_basefill_011'], 'func': zvd_base_universe_d3_024_zvd_basefill_011}


def zvd_base_universe_d3_025_zvd_basefill_013(zvd_base_universe_d2_025_zvd_basefill_013):
    return _base_universe_d3(zvd_base_universe_d2_025_zvd_basefill_013, 25)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_025_zvd_basefill_013'] = {'inputs': ['zvd_base_universe_d2_025_zvd_basefill_013'], 'func': zvd_base_universe_d3_025_zvd_basefill_013}


def zvd_base_universe_d3_026_zvd_basefill_017(zvd_base_universe_d2_026_zvd_basefill_017):
    return _base_universe_d3(zvd_base_universe_d2_026_zvd_basefill_017, 26)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_026_zvd_basefill_017'] = {'inputs': ['zvd_base_universe_d2_026_zvd_basefill_017'], 'func': zvd_base_universe_d3_026_zvd_basefill_017}


def zvd_base_universe_d3_027_zvd_basefill_019(zvd_base_universe_d2_027_zvd_basefill_019):
    return _base_universe_d3(zvd_base_universe_d2_027_zvd_basefill_019, 27)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_027_zvd_basefill_019'] = {'inputs': ['zvd_base_universe_d2_027_zvd_basefill_019'], 'func': zvd_base_universe_d3_027_zvd_basefill_019}


def zvd_base_universe_d3_028_zvd_basefill_023(zvd_base_universe_d2_028_zvd_basefill_023):
    return _base_universe_d3(zvd_base_universe_d2_028_zvd_basefill_023, 28)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_028_zvd_basefill_023'] = {'inputs': ['zvd_base_universe_d2_028_zvd_basefill_023'], 'func': zvd_base_universe_d3_028_zvd_basefill_023}


def zvd_base_universe_d3_029_zvd_basefill_025(zvd_base_universe_d2_029_zvd_basefill_025):
    return _base_universe_d3(zvd_base_universe_d2_029_zvd_basefill_025, 29)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_029_zvd_basefill_025'] = {'inputs': ['zvd_base_universe_d2_029_zvd_basefill_025'], 'func': zvd_base_universe_d3_029_zvd_basefill_025}


def zvd_base_universe_d3_030_zvd_basefill_029(zvd_base_universe_d2_030_zvd_basefill_029):
    return _base_universe_d3(zvd_base_universe_d2_030_zvd_basefill_029, 30)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_030_zvd_basefill_029'] = {'inputs': ['zvd_base_universe_d2_030_zvd_basefill_029'], 'func': zvd_base_universe_d3_030_zvd_basefill_029}


def zvd_base_universe_d3_031_zvd_basefill_031(zvd_base_universe_d2_031_zvd_basefill_031):
    return _base_universe_d3(zvd_base_universe_d2_031_zvd_basefill_031, 31)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_031_zvd_basefill_031'] = {'inputs': ['zvd_base_universe_d2_031_zvd_basefill_031'], 'func': zvd_base_universe_d3_031_zvd_basefill_031}


def zvd_base_universe_d3_032_zvd_basefill_032(zvd_base_universe_d2_032_zvd_basefill_032):
    return _base_universe_d3(zvd_base_universe_d2_032_zvd_basefill_032, 32)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_032_zvd_basefill_032'] = {'inputs': ['zvd_base_universe_d2_032_zvd_basefill_032'], 'func': zvd_base_universe_d3_032_zvd_basefill_032}


def zvd_base_universe_d3_033_zvd_basefill_033(zvd_base_universe_d2_033_zvd_basefill_033):
    return _base_universe_d3(zvd_base_universe_d2_033_zvd_basefill_033, 33)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_033_zvd_basefill_033'] = {'inputs': ['zvd_base_universe_d2_033_zvd_basefill_033'], 'func': zvd_base_universe_d3_033_zvd_basefill_033}


def zvd_base_universe_d3_034_zvd_basefill_034(zvd_base_universe_d2_034_zvd_basefill_034):
    return _base_universe_d3(zvd_base_universe_d2_034_zvd_basefill_034, 34)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_034_zvd_basefill_034'] = {'inputs': ['zvd_base_universe_d2_034_zvd_basefill_034'], 'func': zvd_base_universe_d3_034_zvd_basefill_034}


def zvd_base_universe_d3_035_zvd_basefill_035(zvd_base_universe_d2_035_zvd_basefill_035):
    return _base_universe_d3(zvd_base_universe_d2_035_zvd_basefill_035, 35)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_035_zvd_basefill_035'] = {'inputs': ['zvd_base_universe_d2_035_zvd_basefill_035'], 'func': zvd_base_universe_d3_035_zvd_basefill_035}


def zvd_base_universe_d3_036_zvd_basefill_036(zvd_base_universe_d2_036_zvd_basefill_036):
    return _base_universe_d3(zvd_base_universe_d2_036_zvd_basefill_036, 36)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_036_zvd_basefill_036'] = {'inputs': ['zvd_base_universe_d2_036_zvd_basefill_036'], 'func': zvd_base_universe_d3_036_zvd_basefill_036}


def zvd_base_universe_d3_037_zvd_basefill_037(zvd_base_universe_d2_037_zvd_basefill_037):
    return _base_universe_d3(zvd_base_universe_d2_037_zvd_basefill_037, 37)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_037_zvd_basefill_037'] = {'inputs': ['zvd_base_universe_d2_037_zvd_basefill_037'], 'func': zvd_base_universe_d3_037_zvd_basefill_037}


def zvd_base_universe_d3_038_zvd_basefill_038(zvd_base_universe_d2_038_zvd_basefill_038):
    return _base_universe_d3(zvd_base_universe_d2_038_zvd_basefill_038, 38)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_038_zvd_basefill_038'] = {'inputs': ['zvd_base_universe_d2_038_zvd_basefill_038'], 'func': zvd_base_universe_d3_038_zvd_basefill_038}


def zvd_base_universe_d3_039_zvd_basefill_039(zvd_base_universe_d2_039_zvd_basefill_039):
    return _base_universe_d3(zvd_base_universe_d2_039_zvd_basefill_039, 39)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_039_zvd_basefill_039'] = {'inputs': ['zvd_base_universe_d2_039_zvd_basefill_039'], 'func': zvd_base_universe_d3_039_zvd_basefill_039}


def zvd_base_universe_d3_040_zvd_basefill_040(zvd_base_universe_d2_040_zvd_basefill_040):
    return _base_universe_d3(zvd_base_universe_d2_040_zvd_basefill_040, 40)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_040_zvd_basefill_040'] = {'inputs': ['zvd_base_universe_d2_040_zvd_basefill_040'], 'func': zvd_base_universe_d3_040_zvd_basefill_040}


def zvd_base_universe_d3_041_zvd_basefill_041(zvd_base_universe_d2_041_zvd_basefill_041):
    return _base_universe_d3(zvd_base_universe_d2_041_zvd_basefill_041, 41)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_041_zvd_basefill_041'] = {'inputs': ['zvd_base_universe_d2_041_zvd_basefill_041'], 'func': zvd_base_universe_d3_041_zvd_basefill_041}


def zvd_base_universe_d3_042_zvd_basefill_042(zvd_base_universe_d2_042_zvd_basefill_042):
    return _base_universe_d3(zvd_base_universe_d2_042_zvd_basefill_042, 42)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_042_zvd_basefill_042'] = {'inputs': ['zvd_base_universe_d2_042_zvd_basefill_042'], 'func': zvd_base_universe_d3_042_zvd_basefill_042}


def zvd_base_universe_d3_043_zvd_basefill_043(zvd_base_universe_d2_043_zvd_basefill_043):
    return _base_universe_d3(zvd_base_universe_d2_043_zvd_basefill_043, 43)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_043_zvd_basefill_043'] = {'inputs': ['zvd_base_universe_d2_043_zvd_basefill_043'], 'func': zvd_base_universe_d3_043_zvd_basefill_043}


def zvd_base_universe_d3_044_zvd_basefill_044(zvd_base_universe_d2_044_zvd_basefill_044):
    return _base_universe_d3(zvd_base_universe_d2_044_zvd_basefill_044, 44)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_044_zvd_basefill_044'] = {'inputs': ['zvd_base_universe_d2_044_zvd_basefill_044'], 'func': zvd_base_universe_d3_044_zvd_basefill_044}


def zvd_base_universe_d3_045_zvd_basefill_045(zvd_base_universe_d2_045_zvd_basefill_045):
    return _base_universe_d3(zvd_base_universe_d2_045_zvd_basefill_045, 45)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_045_zvd_basefill_045'] = {'inputs': ['zvd_base_universe_d2_045_zvd_basefill_045'], 'func': zvd_base_universe_d3_045_zvd_basefill_045}


def zvd_base_universe_d3_046_zvd_basefill_046(zvd_base_universe_d2_046_zvd_basefill_046):
    return _base_universe_d3(zvd_base_universe_d2_046_zvd_basefill_046, 46)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_046_zvd_basefill_046'] = {'inputs': ['zvd_base_universe_d2_046_zvd_basefill_046'], 'func': zvd_base_universe_d3_046_zvd_basefill_046}


def zvd_base_universe_d3_047_zvd_basefill_047(zvd_base_universe_d2_047_zvd_basefill_047):
    return _base_universe_d3(zvd_base_universe_d2_047_zvd_basefill_047, 47)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_047_zvd_basefill_047'] = {'inputs': ['zvd_base_universe_d2_047_zvd_basefill_047'], 'func': zvd_base_universe_d3_047_zvd_basefill_047}


def zvd_base_universe_d3_048_zvd_basefill_048(zvd_base_universe_d2_048_zvd_basefill_048):
    return _base_universe_d3(zvd_base_universe_d2_048_zvd_basefill_048, 48)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_048_zvd_basefill_048'] = {'inputs': ['zvd_base_universe_d2_048_zvd_basefill_048'], 'func': zvd_base_universe_d3_048_zvd_basefill_048}


def zvd_base_universe_d3_049_zvd_basefill_049(zvd_base_universe_d2_049_zvd_basefill_049):
    return _base_universe_d3(zvd_base_universe_d2_049_zvd_basefill_049, 49)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_049_zvd_basefill_049'] = {'inputs': ['zvd_base_universe_d2_049_zvd_basefill_049'], 'func': zvd_base_universe_d3_049_zvd_basefill_049}


def zvd_base_universe_d3_050_zvd_basefill_050(zvd_base_universe_d2_050_zvd_basefill_050):
    return _base_universe_d3(zvd_base_universe_d2_050_zvd_basefill_050, 50)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_050_zvd_basefill_050'] = {'inputs': ['zvd_base_universe_d2_050_zvd_basefill_050'], 'func': zvd_base_universe_d3_050_zvd_basefill_050}


def zvd_base_universe_d3_051_zvd_basefill_051(zvd_base_universe_d2_051_zvd_basefill_051):
    return _base_universe_d3(zvd_base_universe_d2_051_zvd_basefill_051, 51)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_051_zvd_basefill_051'] = {'inputs': ['zvd_base_universe_d2_051_zvd_basefill_051'], 'func': zvd_base_universe_d3_051_zvd_basefill_051}


def zvd_base_universe_d3_052_zvd_basefill_052(zvd_base_universe_d2_052_zvd_basefill_052):
    return _base_universe_d3(zvd_base_universe_d2_052_zvd_basefill_052, 52)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_052_zvd_basefill_052'] = {'inputs': ['zvd_base_universe_d2_052_zvd_basefill_052'], 'func': zvd_base_universe_d3_052_zvd_basefill_052}


def zvd_base_universe_d3_053_zvd_basefill_053(zvd_base_universe_d2_053_zvd_basefill_053):
    return _base_universe_d3(zvd_base_universe_d2_053_zvd_basefill_053, 53)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_053_zvd_basefill_053'] = {'inputs': ['zvd_base_universe_d2_053_zvd_basefill_053'], 'func': zvd_base_universe_d3_053_zvd_basefill_053}


def zvd_base_universe_d3_054_zvd_basefill_054(zvd_base_universe_d2_054_zvd_basefill_054):
    return _base_universe_d3(zvd_base_universe_d2_054_zvd_basefill_054, 54)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_054_zvd_basefill_054'] = {'inputs': ['zvd_base_universe_d2_054_zvd_basefill_054'], 'func': zvd_base_universe_d3_054_zvd_basefill_054}


def zvd_base_universe_d3_055_zvd_basefill_055(zvd_base_universe_d2_055_zvd_basefill_055):
    return _base_universe_d3(zvd_base_universe_d2_055_zvd_basefill_055, 55)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_055_zvd_basefill_055'] = {'inputs': ['zvd_base_universe_d2_055_zvd_basefill_055'], 'func': zvd_base_universe_d3_055_zvd_basefill_055}


def zvd_base_universe_d3_056_zvd_basefill_056(zvd_base_universe_d2_056_zvd_basefill_056):
    return _base_universe_d3(zvd_base_universe_d2_056_zvd_basefill_056, 56)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_056_zvd_basefill_056'] = {'inputs': ['zvd_base_universe_d2_056_zvd_basefill_056'], 'func': zvd_base_universe_d3_056_zvd_basefill_056}


def zvd_base_universe_d3_057_zvd_basefill_057(zvd_base_universe_d2_057_zvd_basefill_057):
    return _base_universe_d3(zvd_base_universe_d2_057_zvd_basefill_057, 57)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_057_zvd_basefill_057'] = {'inputs': ['zvd_base_universe_d2_057_zvd_basefill_057'], 'func': zvd_base_universe_d3_057_zvd_basefill_057}


def zvd_base_universe_d3_058_zvd_basefill_058(zvd_base_universe_d2_058_zvd_basefill_058):
    return _base_universe_d3(zvd_base_universe_d2_058_zvd_basefill_058, 58)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_058_zvd_basefill_058'] = {'inputs': ['zvd_base_universe_d2_058_zvd_basefill_058'], 'func': zvd_base_universe_d3_058_zvd_basefill_058}


def zvd_base_universe_d3_059_zvd_basefill_059(zvd_base_universe_d2_059_zvd_basefill_059):
    return _base_universe_d3(zvd_base_universe_d2_059_zvd_basefill_059, 59)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_059_zvd_basefill_059'] = {'inputs': ['zvd_base_universe_d2_059_zvd_basefill_059'], 'func': zvd_base_universe_d3_059_zvd_basefill_059}


def zvd_base_universe_d3_060_zvd_basefill_060(zvd_base_universe_d2_060_zvd_basefill_060):
    return _base_universe_d3(zvd_base_universe_d2_060_zvd_basefill_060, 60)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_060_zvd_basefill_060'] = {'inputs': ['zvd_base_universe_d2_060_zvd_basefill_060'], 'func': zvd_base_universe_d3_060_zvd_basefill_060}


def zvd_base_universe_d3_061_zvd_basefill_061(zvd_base_universe_d2_061_zvd_basefill_061):
    return _base_universe_d3(zvd_base_universe_d2_061_zvd_basefill_061, 61)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_061_zvd_basefill_061'] = {'inputs': ['zvd_base_universe_d2_061_zvd_basefill_061'], 'func': zvd_base_universe_d3_061_zvd_basefill_061}


def zvd_base_universe_d3_062_zvd_basefill_062(zvd_base_universe_d2_062_zvd_basefill_062):
    return _base_universe_d3(zvd_base_universe_d2_062_zvd_basefill_062, 62)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_062_zvd_basefill_062'] = {'inputs': ['zvd_base_universe_d2_062_zvd_basefill_062'], 'func': zvd_base_universe_d3_062_zvd_basefill_062}


def zvd_base_universe_d3_063_zvd_basefill_063(zvd_base_universe_d2_063_zvd_basefill_063):
    return _base_universe_d3(zvd_base_universe_d2_063_zvd_basefill_063, 63)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_063_zvd_basefill_063'] = {'inputs': ['zvd_base_universe_d2_063_zvd_basefill_063'], 'func': zvd_base_universe_d3_063_zvd_basefill_063}


def zvd_base_universe_d3_064_zvd_basefill_064(zvd_base_universe_d2_064_zvd_basefill_064):
    return _base_universe_d3(zvd_base_universe_d2_064_zvd_basefill_064, 64)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_064_zvd_basefill_064'] = {'inputs': ['zvd_base_universe_d2_064_zvd_basefill_064'], 'func': zvd_base_universe_d3_064_zvd_basefill_064}


def zvd_base_universe_d3_065_zvd_basefill_065(zvd_base_universe_d2_065_zvd_basefill_065):
    return _base_universe_d3(zvd_base_universe_d2_065_zvd_basefill_065, 65)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_065_zvd_basefill_065'] = {'inputs': ['zvd_base_universe_d2_065_zvd_basefill_065'], 'func': zvd_base_universe_d3_065_zvd_basefill_065}


def zvd_base_universe_d3_066_zvd_basefill_066(zvd_base_universe_d2_066_zvd_basefill_066):
    return _base_universe_d3(zvd_base_universe_d2_066_zvd_basefill_066, 66)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_066_zvd_basefill_066'] = {'inputs': ['zvd_base_universe_d2_066_zvd_basefill_066'], 'func': zvd_base_universe_d3_066_zvd_basefill_066}


def zvd_base_universe_d3_067_zvd_basefill_067(zvd_base_universe_d2_067_zvd_basefill_067):
    return _base_universe_d3(zvd_base_universe_d2_067_zvd_basefill_067, 67)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_067_zvd_basefill_067'] = {'inputs': ['zvd_base_universe_d2_067_zvd_basefill_067'], 'func': zvd_base_universe_d3_067_zvd_basefill_067}


def zvd_base_universe_d3_068_zvd_basefill_068(zvd_base_universe_d2_068_zvd_basefill_068):
    return _base_universe_d3(zvd_base_universe_d2_068_zvd_basefill_068, 68)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_068_zvd_basefill_068'] = {'inputs': ['zvd_base_universe_d2_068_zvd_basefill_068'], 'func': zvd_base_universe_d3_068_zvd_basefill_068}


def zvd_base_universe_d3_069_zvd_basefill_069(zvd_base_universe_d2_069_zvd_basefill_069):
    return _base_universe_d3(zvd_base_universe_d2_069_zvd_basefill_069, 69)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_069_zvd_basefill_069'] = {'inputs': ['zvd_base_universe_d2_069_zvd_basefill_069'], 'func': zvd_base_universe_d3_069_zvd_basefill_069}


def zvd_base_universe_d3_070_zvd_basefill_070(zvd_base_universe_d2_070_zvd_basefill_070):
    return _base_universe_d3(zvd_base_universe_d2_070_zvd_basefill_070, 70)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_070_zvd_basefill_070'] = {'inputs': ['zvd_base_universe_d2_070_zvd_basefill_070'], 'func': zvd_base_universe_d3_070_zvd_basefill_070}


def zvd_base_universe_d3_071_zvd_basefill_071(zvd_base_universe_d2_071_zvd_basefill_071):
    return _base_universe_d3(zvd_base_universe_d2_071_zvd_basefill_071, 71)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_071_zvd_basefill_071'] = {'inputs': ['zvd_base_universe_d2_071_zvd_basefill_071'], 'func': zvd_base_universe_d3_071_zvd_basefill_071}


def zvd_base_universe_d3_072_zvd_basefill_072(zvd_base_universe_d2_072_zvd_basefill_072):
    return _base_universe_d3(zvd_base_universe_d2_072_zvd_basefill_072, 72)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_072_zvd_basefill_072'] = {'inputs': ['zvd_base_universe_d2_072_zvd_basefill_072'], 'func': zvd_base_universe_d3_072_zvd_basefill_072}


def zvd_base_universe_d3_073_zvd_basefill_073(zvd_base_universe_d2_073_zvd_basefill_073):
    return _base_universe_d3(zvd_base_universe_d2_073_zvd_basefill_073, 73)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_073_zvd_basefill_073'] = {'inputs': ['zvd_base_universe_d2_073_zvd_basefill_073'], 'func': zvd_base_universe_d3_073_zvd_basefill_073}


def zvd_base_universe_d3_074_zvd_basefill_074(zvd_base_universe_d2_074_zvd_basefill_074):
    return _base_universe_d3(zvd_base_universe_d2_074_zvd_basefill_074, 74)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_074_zvd_basefill_074'] = {'inputs': ['zvd_base_universe_d2_074_zvd_basefill_074'], 'func': zvd_base_universe_d3_074_zvd_basefill_074}


def zvd_base_universe_d3_075_zvd_basefill_075(zvd_base_universe_d2_075_zvd_basefill_075):
    return _base_universe_d3(zvd_base_universe_d2_075_zvd_basefill_075, 75)
ZVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['zvd_base_universe_d3_075_zvd_basefill_075'] = {'inputs': ['zvd_base_universe_d2_075_zvd_basefill_075'], 'func': zvd_base_universe_d3_075_zvd_basefill_075}
