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



def tnv_001_amihud_illiquidity_accel_1(tnv_001_amihud_illiquidity_roc_1):
    feature = _s(tnv_001_amihud_illiquidity_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def tnv_007_amihud_illiquidity_accel_5(tnv_007_amihud_illiquidity_roc_5):
    feature = _s(tnv_007_amihud_illiquidity_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def tnv_013_amihud_illiquidity_accel_42(tnv_013_amihud_illiquidity_roc_42):
    feature = _s(tnv_013_amihud_illiquidity_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def tnv_179_tnv_019_amihud_illiquidity_42_019_accel_126(tnv_154_tnv_019_amihud_illiquidity_42_019_roc_126):
    feature = _s(tnv_154_tnv_019_amihud_illiquidity_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def tnv_180_tnv_025_amihud_illiquidity_378_025_accel_378(tnv_155_tnv_025_amihud_illiquidity_378_025_roc_378):
    feature = _s(tnv_155_tnv_025_amihud_illiquidity_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















TURNOVER_RATIO_REGISTRY_3RD_DERIVATIVES = {
    'tnv_001_amihud_illiquidity_accel_1': {'inputs': ['tnv_001_amihud_illiquidity_roc_1'], 'func': tnv_001_amihud_illiquidity_accel_1},
    'tnv_007_amihud_illiquidity_accel_5': {'inputs': ['tnv_007_amihud_illiquidity_roc_5'], 'func': tnv_007_amihud_illiquidity_accel_5},
    'tnv_013_amihud_illiquidity_accel_42': {'inputs': ['tnv_013_amihud_illiquidity_roc_42'], 'func': tnv_013_amihud_illiquidity_accel_42},
    'tnv_179_tnv_019_amihud_illiquidity_42_019_accel_126': {'inputs': ['tnv_154_tnv_019_amihud_illiquidity_42_019_roc_126'], 'func': tnv_179_tnv_019_amihud_illiquidity_42_019_accel_126},
    'tnv_180_tnv_025_amihud_illiquidity_378_025_accel_378': {'inputs': ['tnv_155_tnv_025_amihud_illiquidity_378_025_roc_378'], 'func': tnv_180_tnv_025_amihud_illiquidity_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def tr_replacement_d3_001(tr_replacement_d2_001):
    feature = _clean(tr_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_001'] = {'inputs': ['tr_replacement_d2_001'], 'func': tr_replacement_d3_001}


def tr_replacement_d3_002(tr_replacement_d2_002):
    feature = _clean(tr_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_002'] = {'inputs': ['tr_replacement_d2_002'], 'func': tr_replacement_d3_002}


def tr_replacement_d3_003(tr_replacement_d2_003):
    feature = _clean(tr_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_003'] = {'inputs': ['tr_replacement_d2_003'], 'func': tr_replacement_d3_003}


def tr_replacement_d3_004(tr_replacement_d2_004):
    feature = _clean(tr_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_004'] = {'inputs': ['tr_replacement_d2_004'], 'func': tr_replacement_d3_004}


def tr_replacement_d3_005(tr_replacement_d2_005):
    feature = _clean(tr_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_005'] = {'inputs': ['tr_replacement_d2_005'], 'func': tr_replacement_d3_005}


def tr_replacement_d3_006(tr_replacement_d2_006):
    feature = _clean(tr_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_006'] = {'inputs': ['tr_replacement_d2_006'], 'func': tr_replacement_d3_006}


def tr_replacement_d3_007(tr_replacement_d2_007):
    feature = _clean(tr_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_007'] = {'inputs': ['tr_replacement_d2_007'], 'func': tr_replacement_d3_007}


def tr_replacement_d3_008(tr_replacement_d2_008):
    feature = _clean(tr_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_008'] = {'inputs': ['tr_replacement_d2_008'], 'func': tr_replacement_d3_008}


def tr_replacement_d3_009(tr_replacement_d2_009):
    feature = _clean(tr_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_009'] = {'inputs': ['tr_replacement_d2_009'], 'func': tr_replacement_d3_009}


def tr_replacement_d3_010(tr_replacement_d2_010):
    feature = _clean(tr_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_010'] = {'inputs': ['tr_replacement_d2_010'], 'func': tr_replacement_d3_010}


def tr_replacement_d3_011(tr_replacement_d2_011):
    feature = _clean(tr_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_011'] = {'inputs': ['tr_replacement_d2_011'], 'func': tr_replacement_d3_011}


def tr_replacement_d3_012(tr_replacement_d2_012):
    feature = _clean(tr_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_012'] = {'inputs': ['tr_replacement_d2_012'], 'func': tr_replacement_d3_012}


def tr_replacement_d3_013(tr_replacement_d2_013):
    feature = _clean(tr_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_013'] = {'inputs': ['tr_replacement_d2_013'], 'func': tr_replacement_d3_013}


def tr_replacement_d3_014(tr_replacement_d2_014):
    feature = _clean(tr_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_014'] = {'inputs': ['tr_replacement_d2_014'], 'func': tr_replacement_d3_014}


def tr_replacement_d3_015(tr_replacement_d2_015):
    feature = _clean(tr_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_015'] = {'inputs': ['tr_replacement_d2_015'], 'func': tr_replacement_d3_015}


def tr_replacement_d3_016(tr_replacement_d2_016):
    feature = _clean(tr_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_016'] = {'inputs': ['tr_replacement_d2_016'], 'func': tr_replacement_d3_016}


def tr_replacement_d3_017(tr_replacement_d2_017):
    feature = _clean(tr_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_017'] = {'inputs': ['tr_replacement_d2_017'], 'func': tr_replacement_d3_017}


def tr_replacement_d3_018(tr_replacement_d2_018):
    feature = _clean(tr_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_018'] = {'inputs': ['tr_replacement_d2_018'], 'func': tr_replacement_d3_018}


def tr_replacement_d3_019(tr_replacement_d2_019):
    feature = _clean(tr_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_019'] = {'inputs': ['tr_replacement_d2_019'], 'func': tr_replacement_d3_019}


def tr_replacement_d3_020(tr_replacement_d2_020):
    feature = _clean(tr_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_020'] = {'inputs': ['tr_replacement_d2_020'], 'func': tr_replacement_d3_020}


def tr_replacement_d3_021(tr_replacement_d2_021):
    feature = _clean(tr_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_021'] = {'inputs': ['tr_replacement_d2_021'], 'func': tr_replacement_d3_021}


def tr_replacement_d3_022(tr_replacement_d2_022):
    feature = _clean(tr_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_022'] = {'inputs': ['tr_replacement_d2_022'], 'func': tr_replacement_d3_022}


def tr_replacement_d3_023(tr_replacement_d2_023):
    feature = _clean(tr_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_023'] = {'inputs': ['tr_replacement_d2_023'], 'func': tr_replacement_d3_023}


def tr_replacement_d3_024(tr_replacement_d2_024):
    feature = _clean(tr_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_024'] = {'inputs': ['tr_replacement_d2_024'], 'func': tr_replacement_d3_024}


def tr_replacement_d3_025(tr_replacement_d2_025):
    feature = _clean(tr_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_025'] = {'inputs': ['tr_replacement_d2_025'], 'func': tr_replacement_d3_025}


def tr_replacement_d3_026(tr_replacement_d2_026):
    feature = _clean(tr_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_026'] = {'inputs': ['tr_replacement_d2_026'], 'func': tr_replacement_d3_026}


def tr_replacement_d3_027(tr_replacement_d2_027):
    feature = _clean(tr_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_027'] = {'inputs': ['tr_replacement_d2_027'], 'func': tr_replacement_d3_027}


def tr_replacement_d3_028(tr_replacement_d2_028):
    feature = _clean(tr_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_028'] = {'inputs': ['tr_replacement_d2_028'], 'func': tr_replacement_d3_028}


def tr_replacement_d3_029(tr_replacement_d2_029):
    feature = _clean(tr_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_029'] = {'inputs': ['tr_replacement_d2_029'], 'func': tr_replacement_d3_029}


def tr_replacement_d3_030(tr_replacement_d2_030):
    feature = _clean(tr_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_030'] = {'inputs': ['tr_replacement_d2_030'], 'func': tr_replacement_d3_030}


def tr_replacement_d3_031(tr_replacement_d2_031):
    feature = _clean(tr_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_031'] = {'inputs': ['tr_replacement_d2_031'], 'func': tr_replacement_d3_031}


def tr_replacement_d3_032(tr_replacement_d2_032):
    feature = _clean(tr_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_032'] = {'inputs': ['tr_replacement_d2_032'], 'func': tr_replacement_d3_032}


def tr_replacement_d3_033(tr_replacement_d2_033):
    feature = _clean(tr_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_033'] = {'inputs': ['tr_replacement_d2_033'], 'func': tr_replacement_d3_033}


def tr_replacement_d3_034(tr_replacement_d2_034):
    feature = _clean(tr_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_034'] = {'inputs': ['tr_replacement_d2_034'], 'func': tr_replacement_d3_034}


def tr_replacement_d3_035(tr_replacement_d2_035):
    feature = _clean(tr_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_035'] = {'inputs': ['tr_replacement_d2_035'], 'func': tr_replacement_d3_035}


def tr_replacement_d3_036(tr_replacement_d2_036):
    feature = _clean(tr_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_036'] = {'inputs': ['tr_replacement_d2_036'], 'func': tr_replacement_d3_036}


def tr_replacement_d3_037(tr_replacement_d2_037):
    feature = _clean(tr_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_037'] = {'inputs': ['tr_replacement_d2_037'], 'func': tr_replacement_d3_037}


def tr_replacement_d3_038(tr_replacement_d2_038):
    feature = _clean(tr_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_038'] = {'inputs': ['tr_replacement_d2_038'], 'func': tr_replacement_d3_038}


def tr_replacement_d3_039(tr_replacement_d2_039):
    feature = _clean(tr_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_039'] = {'inputs': ['tr_replacement_d2_039'], 'func': tr_replacement_d3_039}


def tr_replacement_d3_040(tr_replacement_d2_040):
    feature = _clean(tr_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_040'] = {'inputs': ['tr_replacement_d2_040'], 'func': tr_replacement_d3_040}


def tr_replacement_d3_041(tr_replacement_d2_041):
    feature = _clean(tr_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_041'] = {'inputs': ['tr_replacement_d2_041'], 'func': tr_replacement_d3_041}


def tr_replacement_d3_042(tr_replacement_d2_042):
    feature = _clean(tr_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_042'] = {'inputs': ['tr_replacement_d2_042'], 'func': tr_replacement_d3_042}


def tr_replacement_d3_043(tr_replacement_d2_043):
    feature = _clean(tr_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_043'] = {'inputs': ['tr_replacement_d2_043'], 'func': tr_replacement_d3_043}


def tr_replacement_d3_044(tr_replacement_d2_044):
    feature = _clean(tr_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_044'] = {'inputs': ['tr_replacement_d2_044'], 'func': tr_replacement_d3_044}


def tr_replacement_d3_045(tr_replacement_d2_045):
    feature = _clean(tr_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_045'] = {'inputs': ['tr_replacement_d2_045'], 'func': tr_replacement_d3_045}


def tr_replacement_d3_046(tr_replacement_d2_046):
    feature = _clean(tr_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_046'] = {'inputs': ['tr_replacement_d2_046'], 'func': tr_replacement_d3_046}


def tr_replacement_d3_047(tr_replacement_d2_047):
    feature = _clean(tr_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_047'] = {'inputs': ['tr_replacement_d2_047'], 'func': tr_replacement_d3_047}


def tr_replacement_d3_048(tr_replacement_d2_048):
    feature = _clean(tr_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_048'] = {'inputs': ['tr_replacement_d2_048'], 'func': tr_replacement_d3_048}


def tr_replacement_d3_049(tr_replacement_d2_049):
    feature = _clean(tr_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_049'] = {'inputs': ['tr_replacement_d2_049'], 'func': tr_replacement_d3_049}


def tr_replacement_d3_050(tr_replacement_d2_050):
    feature = _clean(tr_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_050'] = {'inputs': ['tr_replacement_d2_050'], 'func': tr_replacement_d3_050}


def tr_replacement_d3_051(tr_replacement_d2_051):
    feature = _clean(tr_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_051'] = {'inputs': ['tr_replacement_d2_051'], 'func': tr_replacement_d3_051}


def tr_replacement_d3_052(tr_replacement_d2_052):
    feature = _clean(tr_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_052'] = {'inputs': ['tr_replacement_d2_052'], 'func': tr_replacement_d3_052}


def tr_replacement_d3_053(tr_replacement_d2_053):
    feature = _clean(tr_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_053'] = {'inputs': ['tr_replacement_d2_053'], 'func': tr_replacement_d3_053}


def tr_replacement_d3_054(tr_replacement_d2_054):
    feature = _clean(tr_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_054'] = {'inputs': ['tr_replacement_d2_054'], 'func': tr_replacement_d3_054}


def tr_replacement_d3_055(tr_replacement_d2_055):
    feature = _clean(tr_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_055'] = {'inputs': ['tr_replacement_d2_055'], 'func': tr_replacement_d3_055}


def tr_replacement_d3_056(tr_replacement_d2_056):
    feature = _clean(tr_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_056'] = {'inputs': ['tr_replacement_d2_056'], 'func': tr_replacement_d3_056}


def tr_replacement_d3_057(tr_replacement_d2_057):
    feature = _clean(tr_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_057'] = {'inputs': ['tr_replacement_d2_057'], 'func': tr_replacement_d3_057}


def tr_replacement_d3_058(tr_replacement_d2_058):
    feature = _clean(tr_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_058'] = {'inputs': ['tr_replacement_d2_058'], 'func': tr_replacement_d3_058}


def tr_replacement_d3_059(tr_replacement_d2_059):
    feature = _clean(tr_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_059'] = {'inputs': ['tr_replacement_d2_059'], 'func': tr_replacement_d3_059}


def tr_replacement_d3_060(tr_replacement_d2_060):
    feature = _clean(tr_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_060'] = {'inputs': ['tr_replacement_d2_060'], 'func': tr_replacement_d3_060}


def tr_replacement_d3_061(tr_replacement_d2_061):
    feature = _clean(tr_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_061'] = {'inputs': ['tr_replacement_d2_061'], 'func': tr_replacement_d3_061}


def tr_replacement_d3_062(tr_replacement_d2_062):
    feature = _clean(tr_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_062'] = {'inputs': ['tr_replacement_d2_062'], 'func': tr_replacement_d3_062}


def tr_replacement_d3_063(tr_replacement_d2_063):
    feature = _clean(tr_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_063'] = {'inputs': ['tr_replacement_d2_063'], 'func': tr_replacement_d3_063}


def tr_replacement_d3_064(tr_replacement_d2_064):
    feature = _clean(tr_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_064'] = {'inputs': ['tr_replacement_d2_064'], 'func': tr_replacement_d3_064}


def tr_replacement_d3_065(tr_replacement_d2_065):
    feature = _clean(tr_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_065'] = {'inputs': ['tr_replacement_d2_065'], 'func': tr_replacement_d3_065}


def tr_replacement_d3_066(tr_replacement_d2_066):
    feature = _clean(tr_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_066'] = {'inputs': ['tr_replacement_d2_066'], 'func': tr_replacement_d3_066}


def tr_replacement_d3_067(tr_replacement_d2_067):
    feature = _clean(tr_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_067'] = {'inputs': ['tr_replacement_d2_067'], 'func': tr_replacement_d3_067}


def tr_replacement_d3_068(tr_replacement_d2_068):
    feature = _clean(tr_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_068'] = {'inputs': ['tr_replacement_d2_068'], 'func': tr_replacement_d3_068}


def tr_replacement_d3_069(tr_replacement_d2_069):
    feature = _clean(tr_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_069'] = {'inputs': ['tr_replacement_d2_069'], 'func': tr_replacement_d3_069}


def tr_replacement_d3_070(tr_replacement_d2_070):
    feature = _clean(tr_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_070'] = {'inputs': ['tr_replacement_d2_070'], 'func': tr_replacement_d3_070}


def tr_replacement_d3_071(tr_replacement_d2_071):
    feature = _clean(tr_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_071'] = {'inputs': ['tr_replacement_d2_071'], 'func': tr_replacement_d3_071}


def tr_replacement_d3_072(tr_replacement_d2_072):
    feature = _clean(tr_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_072'] = {'inputs': ['tr_replacement_d2_072'], 'func': tr_replacement_d3_072}


def tr_replacement_d3_073(tr_replacement_d2_073):
    feature = _clean(tr_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_073'] = {'inputs': ['tr_replacement_d2_073'], 'func': tr_replacement_d3_073}


def tr_replacement_d3_074(tr_replacement_d2_074):
    feature = _clean(tr_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_074'] = {'inputs': ['tr_replacement_d2_074'], 'func': tr_replacement_d3_074}


def tr_replacement_d3_075(tr_replacement_d2_075):
    feature = _clean(tr_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_075'] = {'inputs': ['tr_replacement_d2_075'], 'func': tr_replacement_d3_075}


def tr_replacement_d3_076(tr_replacement_d2_076):
    feature = _clean(tr_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_076'] = {'inputs': ['tr_replacement_d2_076'], 'func': tr_replacement_d3_076}


def tr_replacement_d3_077(tr_replacement_d2_077):
    feature = _clean(tr_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_077'] = {'inputs': ['tr_replacement_d2_077'], 'func': tr_replacement_d3_077}


def tr_replacement_d3_078(tr_replacement_d2_078):
    feature = _clean(tr_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_078'] = {'inputs': ['tr_replacement_d2_078'], 'func': tr_replacement_d3_078}


def tr_replacement_d3_079(tr_replacement_d2_079):
    feature = _clean(tr_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_079'] = {'inputs': ['tr_replacement_d2_079'], 'func': tr_replacement_d3_079}


def tr_replacement_d3_080(tr_replacement_d2_080):
    feature = _clean(tr_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_080'] = {'inputs': ['tr_replacement_d2_080'], 'func': tr_replacement_d3_080}


def tr_replacement_d3_081(tr_replacement_d2_081):
    feature = _clean(tr_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_081'] = {'inputs': ['tr_replacement_d2_081'], 'func': tr_replacement_d3_081}


def tr_replacement_d3_082(tr_replacement_d2_082):
    feature = _clean(tr_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_082'] = {'inputs': ['tr_replacement_d2_082'], 'func': tr_replacement_d3_082}


def tr_replacement_d3_083(tr_replacement_d2_083):
    feature = _clean(tr_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_083'] = {'inputs': ['tr_replacement_d2_083'], 'func': tr_replacement_d3_083}


def tr_replacement_d3_084(tr_replacement_d2_084):
    feature = _clean(tr_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_084'] = {'inputs': ['tr_replacement_d2_084'], 'func': tr_replacement_d3_084}


def tr_replacement_d3_085(tr_replacement_d2_085):
    feature = _clean(tr_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_085'] = {'inputs': ['tr_replacement_d2_085'], 'func': tr_replacement_d3_085}


def tr_replacement_d3_086(tr_replacement_d2_086):
    feature = _clean(tr_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_086'] = {'inputs': ['tr_replacement_d2_086'], 'func': tr_replacement_d3_086}


def tr_replacement_d3_087(tr_replacement_d2_087):
    feature = _clean(tr_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_087'] = {'inputs': ['tr_replacement_d2_087'], 'func': tr_replacement_d3_087}


def tr_replacement_d3_088(tr_replacement_d2_088):
    feature = _clean(tr_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_088'] = {'inputs': ['tr_replacement_d2_088'], 'func': tr_replacement_d3_088}


def tr_replacement_d3_089(tr_replacement_d2_089):
    feature = _clean(tr_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_089'] = {'inputs': ['tr_replacement_d2_089'], 'func': tr_replacement_d3_089}


def tr_replacement_d3_090(tr_replacement_d2_090):
    feature = _clean(tr_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_090'] = {'inputs': ['tr_replacement_d2_090'], 'func': tr_replacement_d3_090}


def tr_replacement_d3_091(tr_replacement_d2_091):
    feature = _clean(tr_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_091'] = {'inputs': ['tr_replacement_d2_091'], 'func': tr_replacement_d3_091}


def tr_replacement_d3_092(tr_replacement_d2_092):
    feature = _clean(tr_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_092'] = {'inputs': ['tr_replacement_d2_092'], 'func': tr_replacement_d3_092}


def tr_replacement_d3_093(tr_replacement_d2_093):
    feature = _clean(tr_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_093'] = {'inputs': ['tr_replacement_d2_093'], 'func': tr_replacement_d3_093}


def tr_replacement_d3_094(tr_replacement_d2_094):
    feature = _clean(tr_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_094'] = {'inputs': ['tr_replacement_d2_094'], 'func': tr_replacement_d3_094}


def tr_replacement_d3_095(tr_replacement_d2_095):
    feature = _clean(tr_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_095'] = {'inputs': ['tr_replacement_d2_095'], 'func': tr_replacement_d3_095}


def tr_replacement_d3_096(tr_replacement_d2_096):
    feature = _clean(tr_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_096'] = {'inputs': ['tr_replacement_d2_096'], 'func': tr_replacement_d3_096}


def tr_replacement_d3_097(tr_replacement_d2_097):
    feature = _clean(tr_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_097'] = {'inputs': ['tr_replacement_d2_097'], 'func': tr_replacement_d3_097}


def tr_replacement_d3_098(tr_replacement_d2_098):
    feature = _clean(tr_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_098'] = {'inputs': ['tr_replacement_d2_098'], 'func': tr_replacement_d3_098}


def tr_replacement_d3_099(tr_replacement_d2_099):
    feature = _clean(tr_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_099'] = {'inputs': ['tr_replacement_d2_099'], 'func': tr_replacement_d3_099}


def tr_replacement_d3_100(tr_replacement_d2_100):
    feature = _clean(tr_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_100'] = {'inputs': ['tr_replacement_d2_100'], 'func': tr_replacement_d3_100}


def tr_replacement_d3_101(tr_replacement_d2_101):
    feature = _clean(tr_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_101'] = {'inputs': ['tr_replacement_d2_101'], 'func': tr_replacement_d3_101}


def tr_replacement_d3_102(tr_replacement_d2_102):
    feature = _clean(tr_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_102'] = {'inputs': ['tr_replacement_d2_102'], 'func': tr_replacement_d3_102}


def tr_replacement_d3_103(tr_replacement_d2_103):
    feature = _clean(tr_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_103'] = {'inputs': ['tr_replacement_d2_103'], 'func': tr_replacement_d3_103}


def tr_replacement_d3_104(tr_replacement_d2_104):
    feature = _clean(tr_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_104'] = {'inputs': ['tr_replacement_d2_104'], 'func': tr_replacement_d3_104}


def tr_replacement_d3_105(tr_replacement_d2_105):
    feature = _clean(tr_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_105'] = {'inputs': ['tr_replacement_d2_105'], 'func': tr_replacement_d3_105}


def tr_replacement_d3_106(tr_replacement_d2_106):
    feature = _clean(tr_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_106'] = {'inputs': ['tr_replacement_d2_106'], 'func': tr_replacement_d3_106}


def tr_replacement_d3_107(tr_replacement_d2_107):
    feature = _clean(tr_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_107'] = {'inputs': ['tr_replacement_d2_107'], 'func': tr_replacement_d3_107}


def tr_replacement_d3_108(tr_replacement_d2_108):
    feature = _clean(tr_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_108'] = {'inputs': ['tr_replacement_d2_108'], 'func': tr_replacement_d3_108}


def tr_replacement_d3_109(tr_replacement_d2_109):
    feature = _clean(tr_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_109'] = {'inputs': ['tr_replacement_d2_109'], 'func': tr_replacement_d3_109}


def tr_replacement_d3_110(tr_replacement_d2_110):
    feature = _clean(tr_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_110'] = {'inputs': ['tr_replacement_d2_110'], 'func': tr_replacement_d3_110}


def tr_replacement_d3_111(tr_replacement_d2_111):
    feature = _clean(tr_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_111'] = {'inputs': ['tr_replacement_d2_111'], 'func': tr_replacement_d3_111}


def tr_replacement_d3_112(tr_replacement_d2_112):
    feature = _clean(tr_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_112'] = {'inputs': ['tr_replacement_d2_112'], 'func': tr_replacement_d3_112}


def tr_replacement_d3_113(tr_replacement_d2_113):
    feature = _clean(tr_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_113'] = {'inputs': ['tr_replacement_d2_113'], 'func': tr_replacement_d3_113}


def tr_replacement_d3_114(tr_replacement_d2_114):
    feature = _clean(tr_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_114'] = {'inputs': ['tr_replacement_d2_114'], 'func': tr_replacement_d3_114}


def tr_replacement_d3_115(tr_replacement_d2_115):
    feature = _clean(tr_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_115'] = {'inputs': ['tr_replacement_d2_115'], 'func': tr_replacement_d3_115}


def tr_replacement_d3_116(tr_replacement_d2_116):
    feature = _clean(tr_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_116'] = {'inputs': ['tr_replacement_d2_116'], 'func': tr_replacement_d3_116}


def tr_replacement_d3_117(tr_replacement_d2_117):
    feature = _clean(tr_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_117'] = {'inputs': ['tr_replacement_d2_117'], 'func': tr_replacement_d3_117}


def tr_replacement_d3_118(tr_replacement_d2_118):
    feature = _clean(tr_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_118'] = {'inputs': ['tr_replacement_d2_118'], 'func': tr_replacement_d3_118}


def tr_replacement_d3_119(tr_replacement_d2_119):
    feature = _clean(tr_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_119'] = {'inputs': ['tr_replacement_d2_119'], 'func': tr_replacement_d3_119}


def tr_replacement_d3_120(tr_replacement_d2_120):
    feature = _clean(tr_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_120'] = {'inputs': ['tr_replacement_d2_120'], 'func': tr_replacement_d3_120}


def tr_replacement_d3_121(tr_replacement_d2_121):
    feature = _clean(tr_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_121'] = {'inputs': ['tr_replacement_d2_121'], 'func': tr_replacement_d3_121}


def tr_replacement_d3_122(tr_replacement_d2_122):
    feature = _clean(tr_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_122'] = {'inputs': ['tr_replacement_d2_122'], 'func': tr_replacement_d3_122}


def tr_replacement_d3_123(tr_replacement_d2_123):
    feature = _clean(tr_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_123'] = {'inputs': ['tr_replacement_d2_123'], 'func': tr_replacement_d3_123}


def tr_replacement_d3_124(tr_replacement_d2_124):
    feature = _clean(tr_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_124'] = {'inputs': ['tr_replacement_d2_124'], 'func': tr_replacement_d3_124}


def tr_replacement_d3_125(tr_replacement_d2_125):
    feature = _clean(tr_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_125'] = {'inputs': ['tr_replacement_d2_125'], 'func': tr_replacement_d3_125}


def tr_replacement_d3_126(tr_replacement_d2_126):
    feature = _clean(tr_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_126'] = {'inputs': ['tr_replacement_d2_126'], 'func': tr_replacement_d3_126}


def tr_replacement_d3_127(tr_replacement_d2_127):
    feature = _clean(tr_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_127'] = {'inputs': ['tr_replacement_d2_127'], 'func': tr_replacement_d3_127}


def tr_replacement_d3_128(tr_replacement_d2_128):
    feature = _clean(tr_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_128'] = {'inputs': ['tr_replacement_d2_128'], 'func': tr_replacement_d3_128}


def tr_replacement_d3_129(tr_replacement_d2_129):
    feature = _clean(tr_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_129'] = {'inputs': ['tr_replacement_d2_129'], 'func': tr_replacement_d3_129}


def tr_replacement_d3_130(tr_replacement_d2_130):
    feature = _clean(tr_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_130'] = {'inputs': ['tr_replacement_d2_130'], 'func': tr_replacement_d3_130}


def tr_replacement_d3_131(tr_replacement_d2_131):
    feature = _clean(tr_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_131'] = {'inputs': ['tr_replacement_d2_131'], 'func': tr_replacement_d3_131}


def tr_replacement_d3_132(tr_replacement_d2_132):
    feature = _clean(tr_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_132'] = {'inputs': ['tr_replacement_d2_132'], 'func': tr_replacement_d3_132}


def tr_replacement_d3_133(tr_replacement_d2_133):
    feature = _clean(tr_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_133'] = {'inputs': ['tr_replacement_d2_133'], 'func': tr_replacement_d3_133}


def tr_replacement_d3_134(tr_replacement_d2_134):
    feature = _clean(tr_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_134'] = {'inputs': ['tr_replacement_d2_134'], 'func': tr_replacement_d3_134}


def tr_replacement_d3_135(tr_replacement_d2_135):
    feature = _clean(tr_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_135'] = {'inputs': ['tr_replacement_d2_135'], 'func': tr_replacement_d3_135}


def tr_replacement_d3_136(tr_replacement_d2_136):
    feature = _clean(tr_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_136'] = {'inputs': ['tr_replacement_d2_136'], 'func': tr_replacement_d3_136}


def tr_replacement_d3_137(tr_replacement_d2_137):
    feature = _clean(tr_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_137'] = {'inputs': ['tr_replacement_d2_137'], 'func': tr_replacement_d3_137}


def tr_replacement_d3_138(tr_replacement_d2_138):
    feature = _clean(tr_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_138'] = {'inputs': ['tr_replacement_d2_138'], 'func': tr_replacement_d3_138}


def tr_replacement_d3_139(tr_replacement_d2_139):
    feature = _clean(tr_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_139'] = {'inputs': ['tr_replacement_d2_139'], 'func': tr_replacement_d3_139}


def tr_replacement_d3_140(tr_replacement_d2_140):
    feature = _clean(tr_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_140'] = {'inputs': ['tr_replacement_d2_140'], 'func': tr_replacement_d3_140}


def tr_replacement_d3_141(tr_replacement_d2_141):
    feature = _clean(tr_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_141'] = {'inputs': ['tr_replacement_d2_141'], 'func': tr_replacement_d3_141}


def tr_replacement_d3_142(tr_replacement_d2_142):
    feature = _clean(tr_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_142'] = {'inputs': ['tr_replacement_d2_142'], 'func': tr_replacement_d3_142}


def tr_replacement_d3_143(tr_replacement_d2_143):
    feature = _clean(tr_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_143'] = {'inputs': ['tr_replacement_d2_143'], 'func': tr_replacement_d3_143}


def tr_replacement_d3_144(tr_replacement_d2_144):
    feature = _clean(tr_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_144'] = {'inputs': ['tr_replacement_d2_144'], 'func': tr_replacement_d3_144}


def tr_replacement_d3_145(tr_replacement_d2_145):
    feature = _clean(tr_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_145'] = {'inputs': ['tr_replacement_d2_145'], 'func': tr_replacement_d3_145}


def tr_replacement_d3_146(tr_replacement_d2_146):
    feature = _clean(tr_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_146'] = {'inputs': ['tr_replacement_d2_146'], 'func': tr_replacement_d3_146}


def tr_replacement_d3_147(tr_replacement_d2_147):
    feature = _clean(tr_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_147'] = {'inputs': ['tr_replacement_d2_147'], 'func': tr_replacement_d3_147}


def tr_replacement_d3_148(tr_replacement_d2_148):
    feature = _clean(tr_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_148'] = {'inputs': ['tr_replacement_d2_148'], 'func': tr_replacement_d3_148}


def tr_replacement_d3_149(tr_replacement_d2_149):
    feature = _clean(tr_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_149'] = {'inputs': ['tr_replacement_d2_149'], 'func': tr_replacement_d3_149}


def tr_replacement_d3_150(tr_replacement_d2_150):
    feature = _clean(tr_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_150'] = {'inputs': ['tr_replacement_d2_150'], 'func': tr_replacement_d3_150}


def tr_replacement_d3_151(tr_replacement_d2_151):
    feature = _clean(tr_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_151'] = {'inputs': ['tr_replacement_d2_151'], 'func': tr_replacement_d3_151}


def tr_replacement_d3_152(tr_replacement_d2_152):
    feature = _clean(tr_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_152'] = {'inputs': ['tr_replacement_d2_152'], 'func': tr_replacement_d3_152}


def tr_replacement_d3_153(tr_replacement_d2_153):
    feature = _clean(tr_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_153'] = {'inputs': ['tr_replacement_d2_153'], 'func': tr_replacement_d3_153}


def tr_replacement_d3_154(tr_replacement_d2_154):
    feature = _clean(tr_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_154'] = {'inputs': ['tr_replacement_d2_154'], 'func': tr_replacement_d3_154}


def tr_replacement_d3_155(tr_replacement_d2_155):
    feature = _clean(tr_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_155'] = {'inputs': ['tr_replacement_d2_155'], 'func': tr_replacement_d3_155}


def tr_replacement_d3_156(tr_replacement_d2_156):
    feature = _clean(tr_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_156'] = {'inputs': ['tr_replacement_d2_156'], 'func': tr_replacement_d3_156}


def tr_replacement_d3_157(tr_replacement_d2_157):
    feature = _clean(tr_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_157'] = {'inputs': ['tr_replacement_d2_157'], 'func': tr_replacement_d3_157}


def tr_replacement_d3_158(tr_replacement_d2_158):
    feature = _clean(tr_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_158'] = {'inputs': ['tr_replacement_d2_158'], 'func': tr_replacement_d3_158}


def tr_replacement_d3_159(tr_replacement_d2_159):
    feature = _clean(tr_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_159'] = {'inputs': ['tr_replacement_d2_159'], 'func': tr_replacement_d3_159}


def tr_replacement_d3_160(tr_replacement_d2_160):
    feature = _clean(tr_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_160'] = {'inputs': ['tr_replacement_d2_160'], 'func': tr_replacement_d3_160}


def tr_replacement_d3_161(tr_replacement_d2_161):
    feature = _clean(tr_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_161'] = {'inputs': ['tr_replacement_d2_161'], 'func': tr_replacement_d3_161}


def tr_replacement_d3_162(tr_replacement_d2_162):
    feature = _clean(tr_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_162'] = {'inputs': ['tr_replacement_d2_162'], 'func': tr_replacement_d3_162}


def tr_replacement_d3_163(tr_replacement_d2_163):
    feature = _clean(tr_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_163'] = {'inputs': ['tr_replacement_d2_163'], 'func': tr_replacement_d3_163}


def tr_replacement_d3_164(tr_replacement_d2_164):
    feature = _clean(tr_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_164'] = {'inputs': ['tr_replacement_d2_164'], 'func': tr_replacement_d3_164}


def tr_replacement_d3_165(tr_replacement_d2_165):
    feature = _clean(tr_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_165'] = {'inputs': ['tr_replacement_d2_165'], 'func': tr_replacement_d3_165}


def tr_replacement_d3_166(tr_replacement_d2_166):
    feature = _clean(tr_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_166'] = {'inputs': ['tr_replacement_d2_166'], 'func': tr_replacement_d3_166}


def tr_replacement_d3_167(tr_replacement_d2_167):
    feature = _clean(tr_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_167'] = {'inputs': ['tr_replacement_d2_167'], 'func': tr_replacement_d3_167}


def tr_replacement_d3_168(tr_replacement_d2_168):
    feature = _clean(tr_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_168'] = {'inputs': ['tr_replacement_d2_168'], 'func': tr_replacement_d3_168}


def tr_replacement_d3_169(tr_replacement_d2_169):
    feature = _clean(tr_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_169'] = {'inputs': ['tr_replacement_d2_169'], 'func': tr_replacement_d3_169}


def tr_replacement_d3_170(tr_replacement_d2_170):
    feature = _clean(tr_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
TR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tr_replacement_d3_170'] = {'inputs': ['tr_replacement_d2_170'], 'func': tr_replacement_d3_170}


# Third-derivative extensions for repaired first-base features.
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def tnv_base_universe_d3_001_tnv_002_zero_volume_frequency_10_002(tnv_base_universe_d2_001_tnv_002_zero_volume_frequency_10_002):
    return _base_universe_d3(tnv_base_universe_d2_001_tnv_002_zero_volume_frequency_10_002, 1)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_001_tnv_002_zero_volume_frequency_10_002'] = {'inputs': ['tnv_base_universe_d2_001_tnv_002_zero_volume_frequency_10_002'], 'func': tnv_base_universe_d3_001_tnv_002_zero_volume_frequency_10_002}


def tnv_base_universe_d3_002_tnv_003_spread_proxy_21_003(tnv_base_universe_d2_002_tnv_003_spread_proxy_21_003):
    return _base_universe_d3(tnv_base_universe_d2_002_tnv_003_spread_proxy_21_003, 2)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_002_tnv_003_spread_proxy_21_003'] = {'inputs': ['tnv_base_universe_d2_002_tnv_003_spread_proxy_21_003'], 'func': tnv_base_universe_d3_002_tnv_003_spread_proxy_21_003}


def tnv_base_universe_d3_003_tnv_004_trading_intensity_42_004(tnv_base_universe_d2_003_tnv_004_trading_intensity_42_004):
    return _base_universe_d3(tnv_base_universe_d2_003_tnv_004_trading_intensity_42_004, 3)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_003_tnv_004_trading_intensity_42_004'] = {'inputs': ['tnv_base_universe_d2_003_tnv_004_trading_intensity_42_004'], 'func': tnv_base_universe_d3_003_tnv_004_trading_intensity_42_004}


def tnv_base_universe_d3_004_tnv_006_price_level_distress_84_006(tnv_base_universe_d2_004_tnv_006_price_level_distress_84_006):
    return _base_universe_d3(tnv_base_universe_d2_004_tnv_006_price_level_distress_84_006, 4)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_004_tnv_006_price_level_distress_84_006'] = {'inputs': ['tnv_base_universe_d2_004_tnv_006_price_level_distress_84_006'], 'func': tnv_base_universe_d3_004_tnv_006_price_level_distress_84_006}


def tnv_base_universe_d3_005_tnv_008_zero_volume_frequency_189_008(tnv_base_universe_d2_005_tnv_008_zero_volume_frequency_189_008):
    return _base_universe_d3(tnv_base_universe_d2_005_tnv_008_zero_volume_frequency_189_008, 5)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_005_tnv_008_zero_volume_frequency_189_008'] = {'inputs': ['tnv_base_universe_d2_005_tnv_008_zero_volume_frequency_189_008'], 'func': tnv_base_universe_d3_005_tnv_008_zero_volume_frequency_189_008}


def tnv_base_universe_d3_006_tnv_009_spread_proxy_252_009(tnv_base_universe_d2_006_tnv_009_spread_proxy_252_009):
    return _base_universe_d3(tnv_base_universe_d2_006_tnv_009_spread_proxy_252_009, 6)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_006_tnv_009_spread_proxy_252_009'] = {'inputs': ['tnv_base_universe_d2_006_tnv_009_spread_proxy_252_009'], 'func': tnv_base_universe_d3_006_tnv_009_spread_proxy_252_009}


def tnv_base_universe_d3_007_tnv_010_trading_intensity_378_010(tnv_base_universe_d2_007_tnv_010_trading_intensity_378_010):
    return _base_universe_d3(tnv_base_universe_d2_007_tnv_010_trading_intensity_378_010, 7)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_007_tnv_010_trading_intensity_378_010'] = {'inputs': ['tnv_base_universe_d2_007_tnv_010_trading_intensity_378_010'], 'func': tnv_base_universe_d3_007_tnv_010_trading_intensity_378_010}


def tnv_base_universe_d3_008_tnv_012_price_level_distress_756_012(tnv_base_universe_d2_008_tnv_012_price_level_distress_756_012):
    return _base_universe_d3(tnv_base_universe_d2_008_tnv_012_price_level_distress_756_012, 8)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_008_tnv_012_price_level_distress_756_012'] = {'inputs': ['tnv_base_universe_d2_008_tnv_012_price_level_distress_756_012'], 'func': tnv_base_universe_d3_008_tnv_012_price_level_distress_756_012}


def tnv_base_universe_d3_009_tnv_014_zero_volume_frequency_1260_014(tnv_base_universe_d2_009_tnv_014_zero_volume_frequency_1260_014):
    return _base_universe_d3(tnv_base_universe_d2_009_tnv_014_zero_volume_frequency_1260_014, 9)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_009_tnv_014_zero_volume_frequency_1260_014'] = {'inputs': ['tnv_base_universe_d2_009_tnv_014_zero_volume_frequency_1260_014'], 'func': tnv_base_universe_d3_009_tnv_014_zero_volume_frequency_1260_014}


def tnv_base_universe_d3_010_tnv_015_spread_proxy_1512_015(tnv_base_universe_d2_010_tnv_015_spread_proxy_1512_015):
    return _base_universe_d3(tnv_base_universe_d2_010_tnv_015_spread_proxy_1512_015, 10)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_010_tnv_015_spread_proxy_1512_015'] = {'inputs': ['tnv_base_universe_d2_010_tnv_015_spread_proxy_1512_015'], 'func': tnv_base_universe_d3_010_tnv_015_spread_proxy_1512_015}


def tnv_base_universe_d3_011_tnv_016_trading_intensity_5_016(tnv_base_universe_d2_011_tnv_016_trading_intensity_5_016):
    return _base_universe_d3(tnv_base_universe_d2_011_tnv_016_trading_intensity_5_016, 11)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_011_tnv_016_trading_intensity_5_016'] = {'inputs': ['tnv_base_universe_d2_011_tnv_016_trading_intensity_5_016'], 'func': tnv_base_universe_d3_011_tnv_016_trading_intensity_5_016}


def tnv_base_universe_d3_012_tnv_018_price_level_distress_21_018(tnv_base_universe_d2_012_tnv_018_price_level_distress_21_018):
    return _base_universe_d3(tnv_base_universe_d2_012_tnv_018_price_level_distress_21_018, 12)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_012_tnv_018_price_level_distress_21_018'] = {'inputs': ['tnv_base_universe_d2_012_tnv_018_price_level_distress_21_018'], 'func': tnv_base_universe_d3_012_tnv_018_price_level_distress_21_018}


def tnv_base_universe_d3_013_tnv_020_zero_volume_frequency_63_020(tnv_base_universe_d2_013_tnv_020_zero_volume_frequency_63_020):
    return _base_universe_d3(tnv_base_universe_d2_013_tnv_020_zero_volume_frequency_63_020, 13)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_013_tnv_020_zero_volume_frequency_63_020'] = {'inputs': ['tnv_base_universe_d2_013_tnv_020_zero_volume_frequency_63_020'], 'func': tnv_base_universe_d3_013_tnv_020_zero_volume_frequency_63_020}


def tnv_base_universe_d3_014_tnv_021_spread_proxy_84_021(tnv_base_universe_d2_014_tnv_021_spread_proxy_84_021):
    return _base_universe_d3(tnv_base_universe_d2_014_tnv_021_spread_proxy_84_021, 14)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_014_tnv_021_spread_proxy_84_021'] = {'inputs': ['tnv_base_universe_d2_014_tnv_021_spread_proxy_84_021'], 'func': tnv_base_universe_d3_014_tnv_021_spread_proxy_84_021}


def tnv_base_universe_d3_015_tnv_022_trading_intensity_126_022(tnv_base_universe_d2_015_tnv_022_trading_intensity_126_022):
    return _base_universe_d3(tnv_base_universe_d2_015_tnv_022_trading_intensity_126_022, 15)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_015_tnv_022_trading_intensity_126_022'] = {'inputs': ['tnv_base_universe_d2_015_tnv_022_trading_intensity_126_022'], 'func': tnv_base_universe_d3_015_tnv_022_trading_intensity_126_022}


def tnv_base_universe_d3_016_tnv_024_price_level_distress_252_024(tnv_base_universe_d2_016_tnv_024_price_level_distress_252_024):
    return _base_universe_d3(tnv_base_universe_d2_016_tnv_024_price_level_distress_252_024, 16)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_016_tnv_024_price_level_distress_252_024'] = {'inputs': ['tnv_base_universe_d2_016_tnv_024_price_level_distress_252_024'], 'func': tnv_base_universe_d3_016_tnv_024_price_level_distress_252_024}


def tnv_base_universe_d3_017_tnv_026_zero_volume_frequency_504_026(tnv_base_universe_d2_017_tnv_026_zero_volume_frequency_504_026):
    return _base_universe_d3(tnv_base_universe_d2_017_tnv_026_zero_volume_frequency_504_026, 17)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_017_tnv_026_zero_volume_frequency_504_026'] = {'inputs': ['tnv_base_universe_d2_017_tnv_026_zero_volume_frequency_504_026'], 'func': tnv_base_universe_d3_017_tnv_026_zero_volume_frequency_504_026}


def tnv_base_universe_d3_018_tnv_027_spread_proxy_756_027(tnv_base_universe_d2_018_tnv_027_spread_proxy_756_027):
    return _base_universe_d3(tnv_base_universe_d2_018_tnv_027_spread_proxy_756_027, 18)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_018_tnv_027_spread_proxy_756_027'] = {'inputs': ['tnv_base_universe_d2_018_tnv_027_spread_proxy_756_027'], 'func': tnv_base_universe_d3_018_tnv_027_spread_proxy_756_027}


def tnv_base_universe_d3_019_tnv_028_trading_intensity_1008_028(tnv_base_universe_d2_019_tnv_028_trading_intensity_1008_028):
    return _base_universe_d3(tnv_base_universe_d2_019_tnv_028_trading_intensity_1008_028, 19)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_019_tnv_028_trading_intensity_1008_028'] = {'inputs': ['tnv_base_universe_d2_019_tnv_028_trading_intensity_1008_028'], 'func': tnv_base_universe_d3_019_tnv_028_trading_intensity_1008_028}


def tnv_base_universe_d3_020_tnv_030_price_level_distress_1512_030(tnv_base_universe_d2_020_tnv_030_price_level_distress_1512_030):
    return _base_universe_d3(tnv_base_universe_d2_020_tnv_030_price_level_distress_1512_030, 20)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_020_tnv_030_price_level_distress_1512_030'] = {'inputs': ['tnv_base_universe_d2_020_tnv_030_price_level_distress_1512_030'], 'func': tnv_base_universe_d3_020_tnv_030_price_level_distress_1512_030}


def tnv_base_universe_d3_021_tnv_basefill_001(tnv_base_universe_d2_021_tnv_basefill_001):
    return _base_universe_d3(tnv_base_universe_d2_021_tnv_basefill_001, 21)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_021_tnv_basefill_001'] = {'inputs': ['tnv_base_universe_d2_021_tnv_basefill_001'], 'func': tnv_base_universe_d3_021_tnv_basefill_001}


def tnv_base_universe_d3_022_tnv_basefill_005(tnv_base_universe_d2_022_tnv_basefill_005):
    return _base_universe_d3(tnv_base_universe_d2_022_tnv_basefill_005, 22)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_022_tnv_basefill_005'] = {'inputs': ['tnv_base_universe_d2_022_tnv_basefill_005'], 'func': tnv_base_universe_d3_022_tnv_basefill_005}


def tnv_base_universe_d3_023_tnv_basefill_007(tnv_base_universe_d2_023_tnv_basefill_007):
    return _base_universe_d3(tnv_base_universe_d2_023_tnv_basefill_007, 23)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_023_tnv_basefill_007'] = {'inputs': ['tnv_base_universe_d2_023_tnv_basefill_007'], 'func': tnv_base_universe_d3_023_tnv_basefill_007}


def tnv_base_universe_d3_024_tnv_basefill_011(tnv_base_universe_d2_024_tnv_basefill_011):
    return _base_universe_d3(tnv_base_universe_d2_024_tnv_basefill_011, 24)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_024_tnv_basefill_011'] = {'inputs': ['tnv_base_universe_d2_024_tnv_basefill_011'], 'func': tnv_base_universe_d3_024_tnv_basefill_011}


def tnv_base_universe_d3_025_tnv_basefill_013(tnv_base_universe_d2_025_tnv_basefill_013):
    return _base_universe_d3(tnv_base_universe_d2_025_tnv_basefill_013, 25)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_025_tnv_basefill_013'] = {'inputs': ['tnv_base_universe_d2_025_tnv_basefill_013'], 'func': tnv_base_universe_d3_025_tnv_basefill_013}


def tnv_base_universe_d3_026_tnv_basefill_017(tnv_base_universe_d2_026_tnv_basefill_017):
    return _base_universe_d3(tnv_base_universe_d2_026_tnv_basefill_017, 26)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_026_tnv_basefill_017'] = {'inputs': ['tnv_base_universe_d2_026_tnv_basefill_017'], 'func': tnv_base_universe_d3_026_tnv_basefill_017}


def tnv_base_universe_d3_027_tnv_basefill_019(tnv_base_universe_d2_027_tnv_basefill_019):
    return _base_universe_d3(tnv_base_universe_d2_027_tnv_basefill_019, 27)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_027_tnv_basefill_019'] = {'inputs': ['tnv_base_universe_d2_027_tnv_basefill_019'], 'func': tnv_base_universe_d3_027_tnv_basefill_019}


def tnv_base_universe_d3_028_tnv_basefill_023(tnv_base_universe_d2_028_tnv_basefill_023):
    return _base_universe_d3(tnv_base_universe_d2_028_tnv_basefill_023, 28)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_028_tnv_basefill_023'] = {'inputs': ['tnv_base_universe_d2_028_tnv_basefill_023'], 'func': tnv_base_universe_d3_028_tnv_basefill_023}


def tnv_base_universe_d3_029_tnv_basefill_025(tnv_base_universe_d2_029_tnv_basefill_025):
    return _base_universe_d3(tnv_base_universe_d2_029_tnv_basefill_025, 29)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_029_tnv_basefill_025'] = {'inputs': ['tnv_base_universe_d2_029_tnv_basefill_025'], 'func': tnv_base_universe_d3_029_tnv_basefill_025}


def tnv_base_universe_d3_030_tnv_basefill_029(tnv_base_universe_d2_030_tnv_basefill_029):
    return _base_universe_d3(tnv_base_universe_d2_030_tnv_basefill_029, 30)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_030_tnv_basefill_029'] = {'inputs': ['tnv_base_universe_d2_030_tnv_basefill_029'], 'func': tnv_base_universe_d3_030_tnv_basefill_029}


def tnv_base_universe_d3_031_tnv_basefill_031(tnv_base_universe_d2_031_tnv_basefill_031):
    return _base_universe_d3(tnv_base_universe_d2_031_tnv_basefill_031, 31)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_031_tnv_basefill_031'] = {'inputs': ['tnv_base_universe_d2_031_tnv_basefill_031'], 'func': tnv_base_universe_d3_031_tnv_basefill_031}


def tnv_base_universe_d3_032_tnv_basefill_032(tnv_base_universe_d2_032_tnv_basefill_032):
    return _base_universe_d3(tnv_base_universe_d2_032_tnv_basefill_032, 32)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_032_tnv_basefill_032'] = {'inputs': ['tnv_base_universe_d2_032_tnv_basefill_032'], 'func': tnv_base_universe_d3_032_tnv_basefill_032}


def tnv_base_universe_d3_033_tnv_basefill_033(tnv_base_universe_d2_033_tnv_basefill_033):
    return _base_universe_d3(tnv_base_universe_d2_033_tnv_basefill_033, 33)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_033_tnv_basefill_033'] = {'inputs': ['tnv_base_universe_d2_033_tnv_basefill_033'], 'func': tnv_base_universe_d3_033_tnv_basefill_033}


def tnv_base_universe_d3_034_tnv_basefill_034(tnv_base_universe_d2_034_tnv_basefill_034):
    return _base_universe_d3(tnv_base_universe_d2_034_tnv_basefill_034, 34)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_034_tnv_basefill_034'] = {'inputs': ['tnv_base_universe_d2_034_tnv_basefill_034'], 'func': tnv_base_universe_d3_034_tnv_basefill_034}


def tnv_base_universe_d3_035_tnv_basefill_035(tnv_base_universe_d2_035_tnv_basefill_035):
    return _base_universe_d3(tnv_base_universe_d2_035_tnv_basefill_035, 35)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_035_tnv_basefill_035'] = {'inputs': ['tnv_base_universe_d2_035_tnv_basefill_035'], 'func': tnv_base_universe_d3_035_tnv_basefill_035}


def tnv_base_universe_d3_036_tnv_basefill_036(tnv_base_universe_d2_036_tnv_basefill_036):
    return _base_universe_d3(tnv_base_universe_d2_036_tnv_basefill_036, 36)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_036_tnv_basefill_036'] = {'inputs': ['tnv_base_universe_d2_036_tnv_basefill_036'], 'func': tnv_base_universe_d3_036_tnv_basefill_036}


def tnv_base_universe_d3_037_tnv_basefill_037(tnv_base_universe_d2_037_tnv_basefill_037):
    return _base_universe_d3(tnv_base_universe_d2_037_tnv_basefill_037, 37)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_037_tnv_basefill_037'] = {'inputs': ['tnv_base_universe_d2_037_tnv_basefill_037'], 'func': tnv_base_universe_d3_037_tnv_basefill_037}


def tnv_base_universe_d3_038_tnv_basefill_038(tnv_base_universe_d2_038_tnv_basefill_038):
    return _base_universe_d3(tnv_base_universe_d2_038_tnv_basefill_038, 38)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_038_tnv_basefill_038'] = {'inputs': ['tnv_base_universe_d2_038_tnv_basefill_038'], 'func': tnv_base_universe_d3_038_tnv_basefill_038}


def tnv_base_universe_d3_039_tnv_basefill_039(tnv_base_universe_d2_039_tnv_basefill_039):
    return _base_universe_d3(tnv_base_universe_d2_039_tnv_basefill_039, 39)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_039_tnv_basefill_039'] = {'inputs': ['tnv_base_universe_d2_039_tnv_basefill_039'], 'func': tnv_base_universe_d3_039_tnv_basefill_039}


def tnv_base_universe_d3_040_tnv_basefill_040(tnv_base_universe_d2_040_tnv_basefill_040):
    return _base_universe_d3(tnv_base_universe_d2_040_tnv_basefill_040, 40)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_040_tnv_basefill_040'] = {'inputs': ['tnv_base_universe_d2_040_tnv_basefill_040'], 'func': tnv_base_universe_d3_040_tnv_basefill_040}


def tnv_base_universe_d3_041_tnv_basefill_041(tnv_base_universe_d2_041_tnv_basefill_041):
    return _base_universe_d3(tnv_base_universe_d2_041_tnv_basefill_041, 41)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_041_tnv_basefill_041'] = {'inputs': ['tnv_base_universe_d2_041_tnv_basefill_041'], 'func': tnv_base_universe_d3_041_tnv_basefill_041}


def tnv_base_universe_d3_042_tnv_basefill_042(tnv_base_universe_d2_042_tnv_basefill_042):
    return _base_universe_d3(tnv_base_universe_d2_042_tnv_basefill_042, 42)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_042_tnv_basefill_042'] = {'inputs': ['tnv_base_universe_d2_042_tnv_basefill_042'], 'func': tnv_base_universe_d3_042_tnv_basefill_042}


def tnv_base_universe_d3_043_tnv_basefill_043(tnv_base_universe_d2_043_tnv_basefill_043):
    return _base_universe_d3(tnv_base_universe_d2_043_tnv_basefill_043, 43)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_043_tnv_basefill_043'] = {'inputs': ['tnv_base_universe_d2_043_tnv_basefill_043'], 'func': tnv_base_universe_d3_043_tnv_basefill_043}


def tnv_base_universe_d3_044_tnv_basefill_044(tnv_base_universe_d2_044_tnv_basefill_044):
    return _base_universe_d3(tnv_base_universe_d2_044_tnv_basefill_044, 44)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_044_tnv_basefill_044'] = {'inputs': ['tnv_base_universe_d2_044_tnv_basefill_044'], 'func': tnv_base_universe_d3_044_tnv_basefill_044}


def tnv_base_universe_d3_045_tnv_basefill_045(tnv_base_universe_d2_045_tnv_basefill_045):
    return _base_universe_d3(tnv_base_universe_d2_045_tnv_basefill_045, 45)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_045_tnv_basefill_045'] = {'inputs': ['tnv_base_universe_d2_045_tnv_basefill_045'], 'func': tnv_base_universe_d3_045_tnv_basefill_045}


def tnv_base_universe_d3_046_tnv_basefill_046(tnv_base_universe_d2_046_tnv_basefill_046):
    return _base_universe_d3(tnv_base_universe_d2_046_tnv_basefill_046, 46)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_046_tnv_basefill_046'] = {'inputs': ['tnv_base_universe_d2_046_tnv_basefill_046'], 'func': tnv_base_universe_d3_046_tnv_basefill_046}


def tnv_base_universe_d3_047_tnv_basefill_047(tnv_base_universe_d2_047_tnv_basefill_047):
    return _base_universe_d3(tnv_base_universe_d2_047_tnv_basefill_047, 47)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_047_tnv_basefill_047'] = {'inputs': ['tnv_base_universe_d2_047_tnv_basefill_047'], 'func': tnv_base_universe_d3_047_tnv_basefill_047}


def tnv_base_universe_d3_048_tnv_basefill_048(tnv_base_universe_d2_048_tnv_basefill_048):
    return _base_universe_d3(tnv_base_universe_d2_048_tnv_basefill_048, 48)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_048_tnv_basefill_048'] = {'inputs': ['tnv_base_universe_d2_048_tnv_basefill_048'], 'func': tnv_base_universe_d3_048_tnv_basefill_048}


def tnv_base_universe_d3_049_tnv_basefill_049(tnv_base_universe_d2_049_tnv_basefill_049):
    return _base_universe_d3(tnv_base_universe_d2_049_tnv_basefill_049, 49)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_049_tnv_basefill_049'] = {'inputs': ['tnv_base_universe_d2_049_tnv_basefill_049'], 'func': tnv_base_universe_d3_049_tnv_basefill_049}


def tnv_base_universe_d3_050_tnv_basefill_050(tnv_base_universe_d2_050_tnv_basefill_050):
    return _base_universe_d3(tnv_base_universe_d2_050_tnv_basefill_050, 50)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_050_tnv_basefill_050'] = {'inputs': ['tnv_base_universe_d2_050_tnv_basefill_050'], 'func': tnv_base_universe_d3_050_tnv_basefill_050}


def tnv_base_universe_d3_051_tnv_basefill_051(tnv_base_universe_d2_051_tnv_basefill_051):
    return _base_universe_d3(tnv_base_universe_d2_051_tnv_basefill_051, 51)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_051_tnv_basefill_051'] = {'inputs': ['tnv_base_universe_d2_051_tnv_basefill_051'], 'func': tnv_base_universe_d3_051_tnv_basefill_051}


def tnv_base_universe_d3_052_tnv_basefill_052(tnv_base_universe_d2_052_tnv_basefill_052):
    return _base_universe_d3(tnv_base_universe_d2_052_tnv_basefill_052, 52)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_052_tnv_basefill_052'] = {'inputs': ['tnv_base_universe_d2_052_tnv_basefill_052'], 'func': tnv_base_universe_d3_052_tnv_basefill_052}


def tnv_base_universe_d3_053_tnv_basefill_053(tnv_base_universe_d2_053_tnv_basefill_053):
    return _base_universe_d3(tnv_base_universe_d2_053_tnv_basefill_053, 53)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_053_tnv_basefill_053'] = {'inputs': ['tnv_base_universe_d2_053_tnv_basefill_053'], 'func': tnv_base_universe_d3_053_tnv_basefill_053}


def tnv_base_universe_d3_054_tnv_basefill_054(tnv_base_universe_d2_054_tnv_basefill_054):
    return _base_universe_d3(tnv_base_universe_d2_054_tnv_basefill_054, 54)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_054_tnv_basefill_054'] = {'inputs': ['tnv_base_universe_d2_054_tnv_basefill_054'], 'func': tnv_base_universe_d3_054_tnv_basefill_054}


def tnv_base_universe_d3_055_tnv_basefill_055(tnv_base_universe_d2_055_tnv_basefill_055):
    return _base_universe_d3(tnv_base_universe_d2_055_tnv_basefill_055, 55)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_055_tnv_basefill_055'] = {'inputs': ['tnv_base_universe_d2_055_tnv_basefill_055'], 'func': tnv_base_universe_d3_055_tnv_basefill_055}


def tnv_base_universe_d3_056_tnv_basefill_056(tnv_base_universe_d2_056_tnv_basefill_056):
    return _base_universe_d3(tnv_base_universe_d2_056_tnv_basefill_056, 56)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_056_tnv_basefill_056'] = {'inputs': ['tnv_base_universe_d2_056_tnv_basefill_056'], 'func': tnv_base_universe_d3_056_tnv_basefill_056}


def tnv_base_universe_d3_057_tnv_basefill_057(tnv_base_universe_d2_057_tnv_basefill_057):
    return _base_universe_d3(tnv_base_universe_d2_057_tnv_basefill_057, 57)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_057_tnv_basefill_057'] = {'inputs': ['tnv_base_universe_d2_057_tnv_basefill_057'], 'func': tnv_base_universe_d3_057_tnv_basefill_057}


def tnv_base_universe_d3_058_tnv_basefill_058(tnv_base_universe_d2_058_tnv_basefill_058):
    return _base_universe_d3(tnv_base_universe_d2_058_tnv_basefill_058, 58)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_058_tnv_basefill_058'] = {'inputs': ['tnv_base_universe_d2_058_tnv_basefill_058'], 'func': tnv_base_universe_d3_058_tnv_basefill_058}


def tnv_base_universe_d3_059_tnv_basefill_059(tnv_base_universe_d2_059_tnv_basefill_059):
    return _base_universe_d3(tnv_base_universe_d2_059_tnv_basefill_059, 59)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_059_tnv_basefill_059'] = {'inputs': ['tnv_base_universe_d2_059_tnv_basefill_059'], 'func': tnv_base_universe_d3_059_tnv_basefill_059}


def tnv_base_universe_d3_060_tnv_basefill_060(tnv_base_universe_d2_060_tnv_basefill_060):
    return _base_universe_d3(tnv_base_universe_d2_060_tnv_basefill_060, 60)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_060_tnv_basefill_060'] = {'inputs': ['tnv_base_universe_d2_060_tnv_basefill_060'], 'func': tnv_base_universe_d3_060_tnv_basefill_060}


def tnv_base_universe_d3_061_tnv_basefill_061(tnv_base_universe_d2_061_tnv_basefill_061):
    return _base_universe_d3(tnv_base_universe_d2_061_tnv_basefill_061, 61)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_061_tnv_basefill_061'] = {'inputs': ['tnv_base_universe_d2_061_tnv_basefill_061'], 'func': tnv_base_universe_d3_061_tnv_basefill_061}


def tnv_base_universe_d3_062_tnv_basefill_062(tnv_base_universe_d2_062_tnv_basefill_062):
    return _base_universe_d3(tnv_base_universe_d2_062_tnv_basefill_062, 62)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_062_tnv_basefill_062'] = {'inputs': ['tnv_base_universe_d2_062_tnv_basefill_062'], 'func': tnv_base_universe_d3_062_tnv_basefill_062}


def tnv_base_universe_d3_063_tnv_basefill_063(tnv_base_universe_d2_063_tnv_basefill_063):
    return _base_universe_d3(tnv_base_universe_d2_063_tnv_basefill_063, 63)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_063_tnv_basefill_063'] = {'inputs': ['tnv_base_universe_d2_063_tnv_basefill_063'], 'func': tnv_base_universe_d3_063_tnv_basefill_063}


def tnv_base_universe_d3_064_tnv_basefill_064(tnv_base_universe_d2_064_tnv_basefill_064):
    return _base_universe_d3(tnv_base_universe_d2_064_tnv_basefill_064, 64)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_064_tnv_basefill_064'] = {'inputs': ['tnv_base_universe_d2_064_tnv_basefill_064'], 'func': tnv_base_universe_d3_064_tnv_basefill_064}


def tnv_base_universe_d3_065_tnv_basefill_065(tnv_base_universe_d2_065_tnv_basefill_065):
    return _base_universe_d3(tnv_base_universe_d2_065_tnv_basefill_065, 65)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_065_tnv_basefill_065'] = {'inputs': ['tnv_base_universe_d2_065_tnv_basefill_065'], 'func': tnv_base_universe_d3_065_tnv_basefill_065}


def tnv_base_universe_d3_066_tnv_basefill_066(tnv_base_universe_d2_066_tnv_basefill_066):
    return _base_universe_d3(tnv_base_universe_d2_066_tnv_basefill_066, 66)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_066_tnv_basefill_066'] = {'inputs': ['tnv_base_universe_d2_066_tnv_basefill_066'], 'func': tnv_base_universe_d3_066_tnv_basefill_066}


def tnv_base_universe_d3_067_tnv_basefill_067(tnv_base_universe_d2_067_tnv_basefill_067):
    return _base_universe_d3(tnv_base_universe_d2_067_tnv_basefill_067, 67)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_067_tnv_basefill_067'] = {'inputs': ['tnv_base_universe_d2_067_tnv_basefill_067'], 'func': tnv_base_universe_d3_067_tnv_basefill_067}


def tnv_base_universe_d3_068_tnv_basefill_068(tnv_base_universe_d2_068_tnv_basefill_068):
    return _base_universe_d3(tnv_base_universe_d2_068_tnv_basefill_068, 68)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_068_tnv_basefill_068'] = {'inputs': ['tnv_base_universe_d2_068_tnv_basefill_068'], 'func': tnv_base_universe_d3_068_tnv_basefill_068}


def tnv_base_universe_d3_069_tnv_basefill_069(tnv_base_universe_d2_069_tnv_basefill_069):
    return _base_universe_d3(tnv_base_universe_d2_069_tnv_basefill_069, 69)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_069_tnv_basefill_069'] = {'inputs': ['tnv_base_universe_d2_069_tnv_basefill_069'], 'func': tnv_base_universe_d3_069_tnv_basefill_069}


def tnv_base_universe_d3_070_tnv_basefill_070(tnv_base_universe_d2_070_tnv_basefill_070):
    return _base_universe_d3(tnv_base_universe_d2_070_tnv_basefill_070, 70)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_070_tnv_basefill_070'] = {'inputs': ['tnv_base_universe_d2_070_tnv_basefill_070'], 'func': tnv_base_universe_d3_070_tnv_basefill_070}


def tnv_base_universe_d3_071_tnv_basefill_071(tnv_base_universe_d2_071_tnv_basefill_071):
    return _base_universe_d3(tnv_base_universe_d2_071_tnv_basefill_071, 71)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_071_tnv_basefill_071'] = {'inputs': ['tnv_base_universe_d2_071_tnv_basefill_071'], 'func': tnv_base_universe_d3_071_tnv_basefill_071}


def tnv_base_universe_d3_072_tnv_basefill_072(tnv_base_universe_d2_072_tnv_basefill_072):
    return _base_universe_d3(tnv_base_universe_d2_072_tnv_basefill_072, 72)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_072_tnv_basefill_072'] = {'inputs': ['tnv_base_universe_d2_072_tnv_basefill_072'], 'func': tnv_base_universe_d3_072_tnv_basefill_072}


def tnv_base_universe_d3_073_tnv_basefill_073(tnv_base_universe_d2_073_tnv_basefill_073):
    return _base_universe_d3(tnv_base_universe_d2_073_tnv_basefill_073, 73)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_073_tnv_basefill_073'] = {'inputs': ['tnv_base_universe_d2_073_tnv_basefill_073'], 'func': tnv_base_universe_d3_073_tnv_basefill_073}


def tnv_base_universe_d3_074_tnv_basefill_074(tnv_base_universe_d2_074_tnv_basefill_074):
    return _base_universe_d3(tnv_base_universe_d2_074_tnv_basefill_074, 74)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_074_tnv_basefill_074'] = {'inputs': ['tnv_base_universe_d2_074_tnv_basefill_074'], 'func': tnv_base_universe_d3_074_tnv_basefill_074}


def tnv_base_universe_d3_075_tnv_basefill_075(tnv_base_universe_d2_075_tnv_basefill_075):
    return _base_universe_d3(tnv_base_universe_d2_075_tnv_basefill_075, 75)
TNV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tnv_base_universe_d3_075_tnv_basefill_075'] = {'inputs': ['tnv_base_universe_d2_075_tnv_basefill_075'], 'func': tnv_base_universe_d3_075_tnv_basefill_075}
