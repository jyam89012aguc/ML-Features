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



def mip_001_amihud_illiquidity_accel_1(mip_001_amihud_illiquidity_roc_1):
    feature = _s(mip_001_amihud_illiquidity_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def mip_007_amihud_illiquidity_accel_5(mip_007_amihud_illiquidity_roc_5):
    feature = _s(mip_007_amihud_illiquidity_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def mip_013_amihud_illiquidity_accel_42(mip_013_amihud_illiquidity_roc_42):
    feature = _s(mip_013_amihud_illiquidity_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def mip_179_mip_019_amihud_illiquidity_42_019_accel_126(mip_154_mip_019_amihud_illiquidity_42_019_roc_126):
    feature = _s(mip_154_mip_019_amihud_illiquidity_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def mip_180_mip_025_amihud_illiquidity_378_025_accel_378(mip_155_mip_025_amihud_illiquidity_378_025_roc_378):
    feature = _s(mip_155_mip_025_amihud_illiquidity_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















MARKET_IMPACT_PROXY_REGISTRY_3RD_DERIVATIVES = {
    'mip_001_amihud_illiquidity_accel_1': {'inputs': ['mip_001_amihud_illiquidity_roc_1'], 'func': mip_001_amihud_illiquidity_accel_1},
    'mip_007_amihud_illiquidity_accel_5': {'inputs': ['mip_007_amihud_illiquidity_roc_5'], 'func': mip_007_amihud_illiquidity_accel_5},
    'mip_013_amihud_illiquidity_accel_42': {'inputs': ['mip_013_amihud_illiquidity_roc_42'], 'func': mip_013_amihud_illiquidity_accel_42},
    'mip_179_mip_019_amihud_illiquidity_42_019_accel_126': {'inputs': ['mip_154_mip_019_amihud_illiquidity_42_019_roc_126'], 'func': mip_179_mip_019_amihud_illiquidity_42_019_accel_126},
    'mip_180_mip_025_amihud_illiquidity_378_025_accel_378': {'inputs': ['mip_155_mip_025_amihud_illiquidity_378_025_roc_378'], 'func': mip_180_mip_025_amihud_illiquidity_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def mip_replacement_d3_001(mip_replacement_d2_001):
    feature = _clean(mip_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_001'] = {'inputs': ['mip_replacement_d2_001'], 'func': mip_replacement_d3_001}


def mip_replacement_d3_002(mip_replacement_d2_002):
    feature = _clean(mip_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_002'] = {'inputs': ['mip_replacement_d2_002'], 'func': mip_replacement_d3_002}


def mip_replacement_d3_003(mip_replacement_d2_003):
    feature = _clean(mip_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_003'] = {'inputs': ['mip_replacement_d2_003'], 'func': mip_replacement_d3_003}


def mip_replacement_d3_004(mip_replacement_d2_004):
    feature = _clean(mip_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_004'] = {'inputs': ['mip_replacement_d2_004'], 'func': mip_replacement_d3_004}


def mip_replacement_d3_005(mip_replacement_d2_005):
    feature = _clean(mip_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_005'] = {'inputs': ['mip_replacement_d2_005'], 'func': mip_replacement_d3_005}


def mip_replacement_d3_006(mip_replacement_d2_006):
    feature = _clean(mip_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_006'] = {'inputs': ['mip_replacement_d2_006'], 'func': mip_replacement_d3_006}


def mip_replacement_d3_007(mip_replacement_d2_007):
    feature = _clean(mip_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_007'] = {'inputs': ['mip_replacement_d2_007'], 'func': mip_replacement_d3_007}


def mip_replacement_d3_008(mip_replacement_d2_008):
    feature = _clean(mip_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_008'] = {'inputs': ['mip_replacement_d2_008'], 'func': mip_replacement_d3_008}


def mip_replacement_d3_009(mip_replacement_d2_009):
    feature = _clean(mip_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_009'] = {'inputs': ['mip_replacement_d2_009'], 'func': mip_replacement_d3_009}


def mip_replacement_d3_010(mip_replacement_d2_010):
    feature = _clean(mip_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_010'] = {'inputs': ['mip_replacement_d2_010'], 'func': mip_replacement_d3_010}


def mip_replacement_d3_011(mip_replacement_d2_011):
    feature = _clean(mip_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_011'] = {'inputs': ['mip_replacement_d2_011'], 'func': mip_replacement_d3_011}


def mip_replacement_d3_012(mip_replacement_d2_012):
    feature = _clean(mip_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_012'] = {'inputs': ['mip_replacement_d2_012'], 'func': mip_replacement_d3_012}


def mip_replacement_d3_013(mip_replacement_d2_013):
    feature = _clean(mip_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_013'] = {'inputs': ['mip_replacement_d2_013'], 'func': mip_replacement_d3_013}


def mip_replacement_d3_014(mip_replacement_d2_014):
    feature = _clean(mip_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_014'] = {'inputs': ['mip_replacement_d2_014'], 'func': mip_replacement_d3_014}


def mip_replacement_d3_015(mip_replacement_d2_015):
    feature = _clean(mip_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_015'] = {'inputs': ['mip_replacement_d2_015'], 'func': mip_replacement_d3_015}


def mip_replacement_d3_016(mip_replacement_d2_016):
    feature = _clean(mip_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_016'] = {'inputs': ['mip_replacement_d2_016'], 'func': mip_replacement_d3_016}


def mip_replacement_d3_017(mip_replacement_d2_017):
    feature = _clean(mip_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_017'] = {'inputs': ['mip_replacement_d2_017'], 'func': mip_replacement_d3_017}


def mip_replacement_d3_018(mip_replacement_d2_018):
    feature = _clean(mip_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_018'] = {'inputs': ['mip_replacement_d2_018'], 'func': mip_replacement_d3_018}


def mip_replacement_d3_019(mip_replacement_d2_019):
    feature = _clean(mip_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_019'] = {'inputs': ['mip_replacement_d2_019'], 'func': mip_replacement_d3_019}


def mip_replacement_d3_020(mip_replacement_d2_020):
    feature = _clean(mip_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_020'] = {'inputs': ['mip_replacement_d2_020'], 'func': mip_replacement_d3_020}


def mip_replacement_d3_021(mip_replacement_d2_021):
    feature = _clean(mip_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_021'] = {'inputs': ['mip_replacement_d2_021'], 'func': mip_replacement_d3_021}


def mip_replacement_d3_022(mip_replacement_d2_022):
    feature = _clean(mip_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_022'] = {'inputs': ['mip_replacement_d2_022'], 'func': mip_replacement_d3_022}


def mip_replacement_d3_023(mip_replacement_d2_023):
    feature = _clean(mip_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_023'] = {'inputs': ['mip_replacement_d2_023'], 'func': mip_replacement_d3_023}


def mip_replacement_d3_024(mip_replacement_d2_024):
    feature = _clean(mip_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_024'] = {'inputs': ['mip_replacement_d2_024'], 'func': mip_replacement_d3_024}


def mip_replacement_d3_025(mip_replacement_d2_025):
    feature = _clean(mip_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_025'] = {'inputs': ['mip_replacement_d2_025'], 'func': mip_replacement_d3_025}


def mip_replacement_d3_026(mip_replacement_d2_026):
    feature = _clean(mip_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_026'] = {'inputs': ['mip_replacement_d2_026'], 'func': mip_replacement_d3_026}


def mip_replacement_d3_027(mip_replacement_d2_027):
    feature = _clean(mip_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_027'] = {'inputs': ['mip_replacement_d2_027'], 'func': mip_replacement_d3_027}


def mip_replacement_d3_028(mip_replacement_d2_028):
    feature = _clean(mip_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_028'] = {'inputs': ['mip_replacement_d2_028'], 'func': mip_replacement_d3_028}


def mip_replacement_d3_029(mip_replacement_d2_029):
    feature = _clean(mip_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_029'] = {'inputs': ['mip_replacement_d2_029'], 'func': mip_replacement_d3_029}


def mip_replacement_d3_030(mip_replacement_d2_030):
    feature = _clean(mip_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_030'] = {'inputs': ['mip_replacement_d2_030'], 'func': mip_replacement_d3_030}


def mip_replacement_d3_031(mip_replacement_d2_031):
    feature = _clean(mip_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_031'] = {'inputs': ['mip_replacement_d2_031'], 'func': mip_replacement_d3_031}


def mip_replacement_d3_032(mip_replacement_d2_032):
    feature = _clean(mip_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_032'] = {'inputs': ['mip_replacement_d2_032'], 'func': mip_replacement_d3_032}


def mip_replacement_d3_033(mip_replacement_d2_033):
    feature = _clean(mip_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_033'] = {'inputs': ['mip_replacement_d2_033'], 'func': mip_replacement_d3_033}


def mip_replacement_d3_034(mip_replacement_d2_034):
    feature = _clean(mip_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_034'] = {'inputs': ['mip_replacement_d2_034'], 'func': mip_replacement_d3_034}


def mip_replacement_d3_035(mip_replacement_d2_035):
    feature = _clean(mip_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_035'] = {'inputs': ['mip_replacement_d2_035'], 'func': mip_replacement_d3_035}


def mip_replacement_d3_036(mip_replacement_d2_036):
    feature = _clean(mip_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_036'] = {'inputs': ['mip_replacement_d2_036'], 'func': mip_replacement_d3_036}


def mip_replacement_d3_037(mip_replacement_d2_037):
    feature = _clean(mip_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_037'] = {'inputs': ['mip_replacement_d2_037'], 'func': mip_replacement_d3_037}


def mip_replacement_d3_038(mip_replacement_d2_038):
    feature = _clean(mip_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_038'] = {'inputs': ['mip_replacement_d2_038'], 'func': mip_replacement_d3_038}


def mip_replacement_d3_039(mip_replacement_d2_039):
    feature = _clean(mip_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_039'] = {'inputs': ['mip_replacement_d2_039'], 'func': mip_replacement_d3_039}


def mip_replacement_d3_040(mip_replacement_d2_040):
    feature = _clean(mip_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_040'] = {'inputs': ['mip_replacement_d2_040'], 'func': mip_replacement_d3_040}


def mip_replacement_d3_041(mip_replacement_d2_041):
    feature = _clean(mip_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_041'] = {'inputs': ['mip_replacement_d2_041'], 'func': mip_replacement_d3_041}


def mip_replacement_d3_042(mip_replacement_d2_042):
    feature = _clean(mip_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_042'] = {'inputs': ['mip_replacement_d2_042'], 'func': mip_replacement_d3_042}


def mip_replacement_d3_043(mip_replacement_d2_043):
    feature = _clean(mip_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_043'] = {'inputs': ['mip_replacement_d2_043'], 'func': mip_replacement_d3_043}


def mip_replacement_d3_044(mip_replacement_d2_044):
    feature = _clean(mip_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_044'] = {'inputs': ['mip_replacement_d2_044'], 'func': mip_replacement_d3_044}


def mip_replacement_d3_045(mip_replacement_d2_045):
    feature = _clean(mip_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_045'] = {'inputs': ['mip_replacement_d2_045'], 'func': mip_replacement_d3_045}


def mip_replacement_d3_046(mip_replacement_d2_046):
    feature = _clean(mip_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_046'] = {'inputs': ['mip_replacement_d2_046'], 'func': mip_replacement_d3_046}


def mip_replacement_d3_047(mip_replacement_d2_047):
    feature = _clean(mip_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_047'] = {'inputs': ['mip_replacement_d2_047'], 'func': mip_replacement_d3_047}


def mip_replacement_d3_048(mip_replacement_d2_048):
    feature = _clean(mip_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_048'] = {'inputs': ['mip_replacement_d2_048'], 'func': mip_replacement_d3_048}


def mip_replacement_d3_049(mip_replacement_d2_049):
    feature = _clean(mip_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_049'] = {'inputs': ['mip_replacement_d2_049'], 'func': mip_replacement_d3_049}


def mip_replacement_d3_050(mip_replacement_d2_050):
    feature = _clean(mip_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_050'] = {'inputs': ['mip_replacement_d2_050'], 'func': mip_replacement_d3_050}


def mip_replacement_d3_051(mip_replacement_d2_051):
    feature = _clean(mip_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_051'] = {'inputs': ['mip_replacement_d2_051'], 'func': mip_replacement_d3_051}


def mip_replacement_d3_052(mip_replacement_d2_052):
    feature = _clean(mip_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_052'] = {'inputs': ['mip_replacement_d2_052'], 'func': mip_replacement_d3_052}


def mip_replacement_d3_053(mip_replacement_d2_053):
    feature = _clean(mip_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_053'] = {'inputs': ['mip_replacement_d2_053'], 'func': mip_replacement_d3_053}


def mip_replacement_d3_054(mip_replacement_d2_054):
    feature = _clean(mip_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_054'] = {'inputs': ['mip_replacement_d2_054'], 'func': mip_replacement_d3_054}


def mip_replacement_d3_055(mip_replacement_d2_055):
    feature = _clean(mip_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_055'] = {'inputs': ['mip_replacement_d2_055'], 'func': mip_replacement_d3_055}


def mip_replacement_d3_056(mip_replacement_d2_056):
    feature = _clean(mip_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_056'] = {'inputs': ['mip_replacement_d2_056'], 'func': mip_replacement_d3_056}


def mip_replacement_d3_057(mip_replacement_d2_057):
    feature = _clean(mip_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_057'] = {'inputs': ['mip_replacement_d2_057'], 'func': mip_replacement_d3_057}


def mip_replacement_d3_058(mip_replacement_d2_058):
    feature = _clean(mip_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_058'] = {'inputs': ['mip_replacement_d2_058'], 'func': mip_replacement_d3_058}


def mip_replacement_d3_059(mip_replacement_d2_059):
    feature = _clean(mip_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_059'] = {'inputs': ['mip_replacement_d2_059'], 'func': mip_replacement_d3_059}


def mip_replacement_d3_060(mip_replacement_d2_060):
    feature = _clean(mip_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_060'] = {'inputs': ['mip_replacement_d2_060'], 'func': mip_replacement_d3_060}


def mip_replacement_d3_061(mip_replacement_d2_061):
    feature = _clean(mip_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_061'] = {'inputs': ['mip_replacement_d2_061'], 'func': mip_replacement_d3_061}


def mip_replacement_d3_062(mip_replacement_d2_062):
    feature = _clean(mip_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_062'] = {'inputs': ['mip_replacement_d2_062'], 'func': mip_replacement_d3_062}


def mip_replacement_d3_063(mip_replacement_d2_063):
    feature = _clean(mip_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_063'] = {'inputs': ['mip_replacement_d2_063'], 'func': mip_replacement_d3_063}


def mip_replacement_d3_064(mip_replacement_d2_064):
    feature = _clean(mip_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_064'] = {'inputs': ['mip_replacement_d2_064'], 'func': mip_replacement_d3_064}


def mip_replacement_d3_065(mip_replacement_d2_065):
    feature = _clean(mip_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_065'] = {'inputs': ['mip_replacement_d2_065'], 'func': mip_replacement_d3_065}


def mip_replacement_d3_066(mip_replacement_d2_066):
    feature = _clean(mip_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_066'] = {'inputs': ['mip_replacement_d2_066'], 'func': mip_replacement_d3_066}


def mip_replacement_d3_067(mip_replacement_d2_067):
    feature = _clean(mip_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_067'] = {'inputs': ['mip_replacement_d2_067'], 'func': mip_replacement_d3_067}


def mip_replacement_d3_068(mip_replacement_d2_068):
    feature = _clean(mip_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_068'] = {'inputs': ['mip_replacement_d2_068'], 'func': mip_replacement_d3_068}


def mip_replacement_d3_069(mip_replacement_d2_069):
    feature = _clean(mip_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_069'] = {'inputs': ['mip_replacement_d2_069'], 'func': mip_replacement_d3_069}


def mip_replacement_d3_070(mip_replacement_d2_070):
    feature = _clean(mip_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_070'] = {'inputs': ['mip_replacement_d2_070'], 'func': mip_replacement_d3_070}


def mip_replacement_d3_071(mip_replacement_d2_071):
    feature = _clean(mip_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_071'] = {'inputs': ['mip_replacement_d2_071'], 'func': mip_replacement_d3_071}


def mip_replacement_d3_072(mip_replacement_d2_072):
    feature = _clean(mip_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_072'] = {'inputs': ['mip_replacement_d2_072'], 'func': mip_replacement_d3_072}


def mip_replacement_d3_073(mip_replacement_d2_073):
    feature = _clean(mip_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_073'] = {'inputs': ['mip_replacement_d2_073'], 'func': mip_replacement_d3_073}


def mip_replacement_d3_074(mip_replacement_d2_074):
    feature = _clean(mip_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_074'] = {'inputs': ['mip_replacement_d2_074'], 'func': mip_replacement_d3_074}


def mip_replacement_d3_075(mip_replacement_d2_075):
    feature = _clean(mip_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_075'] = {'inputs': ['mip_replacement_d2_075'], 'func': mip_replacement_d3_075}


def mip_replacement_d3_076(mip_replacement_d2_076):
    feature = _clean(mip_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_076'] = {'inputs': ['mip_replacement_d2_076'], 'func': mip_replacement_d3_076}


def mip_replacement_d3_077(mip_replacement_d2_077):
    feature = _clean(mip_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_077'] = {'inputs': ['mip_replacement_d2_077'], 'func': mip_replacement_d3_077}


def mip_replacement_d3_078(mip_replacement_d2_078):
    feature = _clean(mip_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_078'] = {'inputs': ['mip_replacement_d2_078'], 'func': mip_replacement_d3_078}


def mip_replacement_d3_079(mip_replacement_d2_079):
    feature = _clean(mip_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_079'] = {'inputs': ['mip_replacement_d2_079'], 'func': mip_replacement_d3_079}


def mip_replacement_d3_080(mip_replacement_d2_080):
    feature = _clean(mip_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_080'] = {'inputs': ['mip_replacement_d2_080'], 'func': mip_replacement_d3_080}


def mip_replacement_d3_081(mip_replacement_d2_081):
    feature = _clean(mip_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_081'] = {'inputs': ['mip_replacement_d2_081'], 'func': mip_replacement_d3_081}


def mip_replacement_d3_082(mip_replacement_d2_082):
    feature = _clean(mip_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_082'] = {'inputs': ['mip_replacement_d2_082'], 'func': mip_replacement_d3_082}


def mip_replacement_d3_083(mip_replacement_d2_083):
    feature = _clean(mip_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_083'] = {'inputs': ['mip_replacement_d2_083'], 'func': mip_replacement_d3_083}


def mip_replacement_d3_084(mip_replacement_d2_084):
    feature = _clean(mip_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_084'] = {'inputs': ['mip_replacement_d2_084'], 'func': mip_replacement_d3_084}


def mip_replacement_d3_085(mip_replacement_d2_085):
    feature = _clean(mip_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_085'] = {'inputs': ['mip_replacement_d2_085'], 'func': mip_replacement_d3_085}


def mip_replacement_d3_086(mip_replacement_d2_086):
    feature = _clean(mip_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_086'] = {'inputs': ['mip_replacement_d2_086'], 'func': mip_replacement_d3_086}


def mip_replacement_d3_087(mip_replacement_d2_087):
    feature = _clean(mip_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_087'] = {'inputs': ['mip_replacement_d2_087'], 'func': mip_replacement_d3_087}


def mip_replacement_d3_088(mip_replacement_d2_088):
    feature = _clean(mip_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_088'] = {'inputs': ['mip_replacement_d2_088'], 'func': mip_replacement_d3_088}


def mip_replacement_d3_089(mip_replacement_d2_089):
    feature = _clean(mip_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_089'] = {'inputs': ['mip_replacement_d2_089'], 'func': mip_replacement_d3_089}


def mip_replacement_d3_090(mip_replacement_d2_090):
    feature = _clean(mip_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_090'] = {'inputs': ['mip_replacement_d2_090'], 'func': mip_replacement_d3_090}


def mip_replacement_d3_091(mip_replacement_d2_091):
    feature = _clean(mip_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_091'] = {'inputs': ['mip_replacement_d2_091'], 'func': mip_replacement_d3_091}


def mip_replacement_d3_092(mip_replacement_d2_092):
    feature = _clean(mip_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_092'] = {'inputs': ['mip_replacement_d2_092'], 'func': mip_replacement_d3_092}


def mip_replacement_d3_093(mip_replacement_d2_093):
    feature = _clean(mip_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_093'] = {'inputs': ['mip_replacement_d2_093'], 'func': mip_replacement_d3_093}


def mip_replacement_d3_094(mip_replacement_d2_094):
    feature = _clean(mip_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_094'] = {'inputs': ['mip_replacement_d2_094'], 'func': mip_replacement_d3_094}


def mip_replacement_d3_095(mip_replacement_d2_095):
    feature = _clean(mip_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_095'] = {'inputs': ['mip_replacement_d2_095'], 'func': mip_replacement_d3_095}


def mip_replacement_d3_096(mip_replacement_d2_096):
    feature = _clean(mip_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_096'] = {'inputs': ['mip_replacement_d2_096'], 'func': mip_replacement_d3_096}


def mip_replacement_d3_097(mip_replacement_d2_097):
    feature = _clean(mip_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_097'] = {'inputs': ['mip_replacement_d2_097'], 'func': mip_replacement_d3_097}


def mip_replacement_d3_098(mip_replacement_d2_098):
    feature = _clean(mip_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_098'] = {'inputs': ['mip_replacement_d2_098'], 'func': mip_replacement_d3_098}


def mip_replacement_d3_099(mip_replacement_d2_099):
    feature = _clean(mip_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_099'] = {'inputs': ['mip_replacement_d2_099'], 'func': mip_replacement_d3_099}


def mip_replacement_d3_100(mip_replacement_d2_100):
    feature = _clean(mip_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_100'] = {'inputs': ['mip_replacement_d2_100'], 'func': mip_replacement_d3_100}


def mip_replacement_d3_101(mip_replacement_d2_101):
    feature = _clean(mip_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_101'] = {'inputs': ['mip_replacement_d2_101'], 'func': mip_replacement_d3_101}


def mip_replacement_d3_102(mip_replacement_d2_102):
    feature = _clean(mip_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_102'] = {'inputs': ['mip_replacement_d2_102'], 'func': mip_replacement_d3_102}


def mip_replacement_d3_103(mip_replacement_d2_103):
    feature = _clean(mip_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_103'] = {'inputs': ['mip_replacement_d2_103'], 'func': mip_replacement_d3_103}


def mip_replacement_d3_104(mip_replacement_d2_104):
    feature = _clean(mip_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_104'] = {'inputs': ['mip_replacement_d2_104'], 'func': mip_replacement_d3_104}


def mip_replacement_d3_105(mip_replacement_d2_105):
    feature = _clean(mip_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_105'] = {'inputs': ['mip_replacement_d2_105'], 'func': mip_replacement_d3_105}


def mip_replacement_d3_106(mip_replacement_d2_106):
    feature = _clean(mip_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_106'] = {'inputs': ['mip_replacement_d2_106'], 'func': mip_replacement_d3_106}


def mip_replacement_d3_107(mip_replacement_d2_107):
    feature = _clean(mip_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_107'] = {'inputs': ['mip_replacement_d2_107'], 'func': mip_replacement_d3_107}


def mip_replacement_d3_108(mip_replacement_d2_108):
    feature = _clean(mip_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_108'] = {'inputs': ['mip_replacement_d2_108'], 'func': mip_replacement_d3_108}


def mip_replacement_d3_109(mip_replacement_d2_109):
    feature = _clean(mip_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_109'] = {'inputs': ['mip_replacement_d2_109'], 'func': mip_replacement_d3_109}


def mip_replacement_d3_110(mip_replacement_d2_110):
    feature = _clean(mip_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_110'] = {'inputs': ['mip_replacement_d2_110'], 'func': mip_replacement_d3_110}


def mip_replacement_d3_111(mip_replacement_d2_111):
    feature = _clean(mip_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_111'] = {'inputs': ['mip_replacement_d2_111'], 'func': mip_replacement_d3_111}


def mip_replacement_d3_112(mip_replacement_d2_112):
    feature = _clean(mip_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_112'] = {'inputs': ['mip_replacement_d2_112'], 'func': mip_replacement_d3_112}


def mip_replacement_d3_113(mip_replacement_d2_113):
    feature = _clean(mip_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_113'] = {'inputs': ['mip_replacement_d2_113'], 'func': mip_replacement_d3_113}


def mip_replacement_d3_114(mip_replacement_d2_114):
    feature = _clean(mip_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_114'] = {'inputs': ['mip_replacement_d2_114'], 'func': mip_replacement_d3_114}


def mip_replacement_d3_115(mip_replacement_d2_115):
    feature = _clean(mip_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_115'] = {'inputs': ['mip_replacement_d2_115'], 'func': mip_replacement_d3_115}


def mip_replacement_d3_116(mip_replacement_d2_116):
    feature = _clean(mip_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_116'] = {'inputs': ['mip_replacement_d2_116'], 'func': mip_replacement_d3_116}


def mip_replacement_d3_117(mip_replacement_d2_117):
    feature = _clean(mip_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_117'] = {'inputs': ['mip_replacement_d2_117'], 'func': mip_replacement_d3_117}


def mip_replacement_d3_118(mip_replacement_d2_118):
    feature = _clean(mip_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_118'] = {'inputs': ['mip_replacement_d2_118'], 'func': mip_replacement_d3_118}


def mip_replacement_d3_119(mip_replacement_d2_119):
    feature = _clean(mip_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_119'] = {'inputs': ['mip_replacement_d2_119'], 'func': mip_replacement_d3_119}


def mip_replacement_d3_120(mip_replacement_d2_120):
    feature = _clean(mip_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_120'] = {'inputs': ['mip_replacement_d2_120'], 'func': mip_replacement_d3_120}


def mip_replacement_d3_121(mip_replacement_d2_121):
    feature = _clean(mip_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_121'] = {'inputs': ['mip_replacement_d2_121'], 'func': mip_replacement_d3_121}


def mip_replacement_d3_122(mip_replacement_d2_122):
    feature = _clean(mip_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_122'] = {'inputs': ['mip_replacement_d2_122'], 'func': mip_replacement_d3_122}


def mip_replacement_d3_123(mip_replacement_d2_123):
    feature = _clean(mip_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_123'] = {'inputs': ['mip_replacement_d2_123'], 'func': mip_replacement_d3_123}


def mip_replacement_d3_124(mip_replacement_d2_124):
    feature = _clean(mip_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_124'] = {'inputs': ['mip_replacement_d2_124'], 'func': mip_replacement_d3_124}


def mip_replacement_d3_125(mip_replacement_d2_125):
    feature = _clean(mip_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_125'] = {'inputs': ['mip_replacement_d2_125'], 'func': mip_replacement_d3_125}


def mip_replacement_d3_126(mip_replacement_d2_126):
    feature = _clean(mip_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_126'] = {'inputs': ['mip_replacement_d2_126'], 'func': mip_replacement_d3_126}


def mip_replacement_d3_127(mip_replacement_d2_127):
    feature = _clean(mip_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_127'] = {'inputs': ['mip_replacement_d2_127'], 'func': mip_replacement_d3_127}


def mip_replacement_d3_128(mip_replacement_d2_128):
    feature = _clean(mip_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_128'] = {'inputs': ['mip_replacement_d2_128'], 'func': mip_replacement_d3_128}


def mip_replacement_d3_129(mip_replacement_d2_129):
    feature = _clean(mip_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_129'] = {'inputs': ['mip_replacement_d2_129'], 'func': mip_replacement_d3_129}


def mip_replacement_d3_130(mip_replacement_d2_130):
    feature = _clean(mip_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_130'] = {'inputs': ['mip_replacement_d2_130'], 'func': mip_replacement_d3_130}


def mip_replacement_d3_131(mip_replacement_d2_131):
    feature = _clean(mip_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_131'] = {'inputs': ['mip_replacement_d2_131'], 'func': mip_replacement_d3_131}


def mip_replacement_d3_132(mip_replacement_d2_132):
    feature = _clean(mip_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_132'] = {'inputs': ['mip_replacement_d2_132'], 'func': mip_replacement_d3_132}


def mip_replacement_d3_133(mip_replacement_d2_133):
    feature = _clean(mip_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_133'] = {'inputs': ['mip_replacement_d2_133'], 'func': mip_replacement_d3_133}


def mip_replacement_d3_134(mip_replacement_d2_134):
    feature = _clean(mip_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_134'] = {'inputs': ['mip_replacement_d2_134'], 'func': mip_replacement_d3_134}


def mip_replacement_d3_135(mip_replacement_d2_135):
    feature = _clean(mip_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_135'] = {'inputs': ['mip_replacement_d2_135'], 'func': mip_replacement_d3_135}


def mip_replacement_d3_136(mip_replacement_d2_136):
    feature = _clean(mip_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_136'] = {'inputs': ['mip_replacement_d2_136'], 'func': mip_replacement_d3_136}


def mip_replacement_d3_137(mip_replacement_d2_137):
    feature = _clean(mip_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_137'] = {'inputs': ['mip_replacement_d2_137'], 'func': mip_replacement_d3_137}


def mip_replacement_d3_138(mip_replacement_d2_138):
    feature = _clean(mip_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_138'] = {'inputs': ['mip_replacement_d2_138'], 'func': mip_replacement_d3_138}


def mip_replacement_d3_139(mip_replacement_d2_139):
    feature = _clean(mip_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_139'] = {'inputs': ['mip_replacement_d2_139'], 'func': mip_replacement_d3_139}


def mip_replacement_d3_140(mip_replacement_d2_140):
    feature = _clean(mip_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_140'] = {'inputs': ['mip_replacement_d2_140'], 'func': mip_replacement_d3_140}


def mip_replacement_d3_141(mip_replacement_d2_141):
    feature = _clean(mip_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_141'] = {'inputs': ['mip_replacement_d2_141'], 'func': mip_replacement_d3_141}


def mip_replacement_d3_142(mip_replacement_d2_142):
    feature = _clean(mip_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_142'] = {'inputs': ['mip_replacement_d2_142'], 'func': mip_replacement_d3_142}


def mip_replacement_d3_143(mip_replacement_d2_143):
    feature = _clean(mip_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_143'] = {'inputs': ['mip_replacement_d2_143'], 'func': mip_replacement_d3_143}


def mip_replacement_d3_144(mip_replacement_d2_144):
    feature = _clean(mip_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_144'] = {'inputs': ['mip_replacement_d2_144'], 'func': mip_replacement_d3_144}


def mip_replacement_d3_145(mip_replacement_d2_145):
    feature = _clean(mip_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_145'] = {'inputs': ['mip_replacement_d2_145'], 'func': mip_replacement_d3_145}


def mip_replacement_d3_146(mip_replacement_d2_146):
    feature = _clean(mip_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_146'] = {'inputs': ['mip_replacement_d2_146'], 'func': mip_replacement_d3_146}


def mip_replacement_d3_147(mip_replacement_d2_147):
    feature = _clean(mip_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_147'] = {'inputs': ['mip_replacement_d2_147'], 'func': mip_replacement_d3_147}


def mip_replacement_d3_148(mip_replacement_d2_148):
    feature = _clean(mip_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_148'] = {'inputs': ['mip_replacement_d2_148'], 'func': mip_replacement_d3_148}


def mip_replacement_d3_149(mip_replacement_d2_149):
    feature = _clean(mip_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_149'] = {'inputs': ['mip_replacement_d2_149'], 'func': mip_replacement_d3_149}


def mip_replacement_d3_150(mip_replacement_d2_150):
    feature = _clean(mip_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_150'] = {'inputs': ['mip_replacement_d2_150'], 'func': mip_replacement_d3_150}


def mip_replacement_d3_151(mip_replacement_d2_151):
    feature = _clean(mip_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_151'] = {'inputs': ['mip_replacement_d2_151'], 'func': mip_replacement_d3_151}


def mip_replacement_d3_152(mip_replacement_d2_152):
    feature = _clean(mip_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_152'] = {'inputs': ['mip_replacement_d2_152'], 'func': mip_replacement_d3_152}


def mip_replacement_d3_153(mip_replacement_d2_153):
    feature = _clean(mip_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_153'] = {'inputs': ['mip_replacement_d2_153'], 'func': mip_replacement_d3_153}


def mip_replacement_d3_154(mip_replacement_d2_154):
    feature = _clean(mip_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_154'] = {'inputs': ['mip_replacement_d2_154'], 'func': mip_replacement_d3_154}


def mip_replacement_d3_155(mip_replacement_d2_155):
    feature = _clean(mip_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_155'] = {'inputs': ['mip_replacement_d2_155'], 'func': mip_replacement_d3_155}


def mip_replacement_d3_156(mip_replacement_d2_156):
    feature = _clean(mip_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_156'] = {'inputs': ['mip_replacement_d2_156'], 'func': mip_replacement_d3_156}


def mip_replacement_d3_157(mip_replacement_d2_157):
    feature = _clean(mip_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_157'] = {'inputs': ['mip_replacement_d2_157'], 'func': mip_replacement_d3_157}


def mip_replacement_d3_158(mip_replacement_d2_158):
    feature = _clean(mip_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_158'] = {'inputs': ['mip_replacement_d2_158'], 'func': mip_replacement_d3_158}


def mip_replacement_d3_159(mip_replacement_d2_159):
    feature = _clean(mip_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_159'] = {'inputs': ['mip_replacement_d2_159'], 'func': mip_replacement_d3_159}


def mip_replacement_d3_160(mip_replacement_d2_160):
    feature = _clean(mip_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_160'] = {'inputs': ['mip_replacement_d2_160'], 'func': mip_replacement_d3_160}


def mip_replacement_d3_161(mip_replacement_d2_161):
    feature = _clean(mip_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_161'] = {'inputs': ['mip_replacement_d2_161'], 'func': mip_replacement_d3_161}


def mip_replacement_d3_162(mip_replacement_d2_162):
    feature = _clean(mip_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_162'] = {'inputs': ['mip_replacement_d2_162'], 'func': mip_replacement_d3_162}


def mip_replacement_d3_163(mip_replacement_d2_163):
    feature = _clean(mip_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_163'] = {'inputs': ['mip_replacement_d2_163'], 'func': mip_replacement_d3_163}


def mip_replacement_d3_164(mip_replacement_d2_164):
    feature = _clean(mip_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_164'] = {'inputs': ['mip_replacement_d2_164'], 'func': mip_replacement_d3_164}


def mip_replacement_d3_165(mip_replacement_d2_165):
    feature = _clean(mip_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_165'] = {'inputs': ['mip_replacement_d2_165'], 'func': mip_replacement_d3_165}


def mip_replacement_d3_166(mip_replacement_d2_166):
    feature = _clean(mip_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_166'] = {'inputs': ['mip_replacement_d2_166'], 'func': mip_replacement_d3_166}


def mip_replacement_d3_167(mip_replacement_d2_167):
    feature = _clean(mip_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_167'] = {'inputs': ['mip_replacement_d2_167'], 'func': mip_replacement_d3_167}


def mip_replacement_d3_168(mip_replacement_d2_168):
    feature = _clean(mip_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_168'] = {'inputs': ['mip_replacement_d2_168'], 'func': mip_replacement_d3_168}


def mip_replacement_d3_169(mip_replacement_d2_169):
    feature = _clean(mip_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_169'] = {'inputs': ['mip_replacement_d2_169'], 'func': mip_replacement_d3_169}


def mip_replacement_d3_170(mip_replacement_d2_170):
    feature = _clean(mip_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
MIP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['mip_replacement_d3_170'] = {'inputs': ['mip_replacement_d2_170'], 'func': mip_replacement_d3_170}


# Third-derivative extensions for repaired first-base features.
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def mip_base_universe_d3_001_mip_002_zero_volume_frequency_10_002(mip_base_universe_d2_001_mip_002_zero_volume_frequency_10_002):
    return _base_universe_d3(mip_base_universe_d2_001_mip_002_zero_volume_frequency_10_002, 1)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_001_mip_002_zero_volume_frequency_10_002'] = {'inputs': ['mip_base_universe_d2_001_mip_002_zero_volume_frequency_10_002'], 'func': mip_base_universe_d3_001_mip_002_zero_volume_frequency_10_002}


def mip_base_universe_d3_002_mip_003_spread_proxy_21_003(mip_base_universe_d2_002_mip_003_spread_proxy_21_003):
    return _base_universe_d3(mip_base_universe_d2_002_mip_003_spread_proxy_21_003, 2)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_002_mip_003_spread_proxy_21_003'] = {'inputs': ['mip_base_universe_d2_002_mip_003_spread_proxy_21_003'], 'func': mip_base_universe_d3_002_mip_003_spread_proxy_21_003}


def mip_base_universe_d3_003_mip_004_trading_intensity_42_004(mip_base_universe_d2_003_mip_004_trading_intensity_42_004):
    return _base_universe_d3(mip_base_universe_d2_003_mip_004_trading_intensity_42_004, 3)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_003_mip_004_trading_intensity_42_004'] = {'inputs': ['mip_base_universe_d2_003_mip_004_trading_intensity_42_004'], 'func': mip_base_universe_d3_003_mip_004_trading_intensity_42_004}


def mip_base_universe_d3_004_mip_006_price_level_distress_84_006(mip_base_universe_d2_004_mip_006_price_level_distress_84_006):
    return _base_universe_d3(mip_base_universe_d2_004_mip_006_price_level_distress_84_006, 4)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_004_mip_006_price_level_distress_84_006'] = {'inputs': ['mip_base_universe_d2_004_mip_006_price_level_distress_84_006'], 'func': mip_base_universe_d3_004_mip_006_price_level_distress_84_006}


def mip_base_universe_d3_005_mip_008_zero_volume_frequency_189_008(mip_base_universe_d2_005_mip_008_zero_volume_frequency_189_008):
    return _base_universe_d3(mip_base_universe_d2_005_mip_008_zero_volume_frequency_189_008, 5)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_005_mip_008_zero_volume_frequency_189_008'] = {'inputs': ['mip_base_universe_d2_005_mip_008_zero_volume_frequency_189_008'], 'func': mip_base_universe_d3_005_mip_008_zero_volume_frequency_189_008}


def mip_base_universe_d3_006_mip_009_spread_proxy_252_009(mip_base_universe_d2_006_mip_009_spread_proxy_252_009):
    return _base_universe_d3(mip_base_universe_d2_006_mip_009_spread_proxy_252_009, 6)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_006_mip_009_spread_proxy_252_009'] = {'inputs': ['mip_base_universe_d2_006_mip_009_spread_proxy_252_009'], 'func': mip_base_universe_d3_006_mip_009_spread_proxy_252_009}


def mip_base_universe_d3_007_mip_010_trading_intensity_378_010(mip_base_universe_d2_007_mip_010_trading_intensity_378_010):
    return _base_universe_d3(mip_base_universe_d2_007_mip_010_trading_intensity_378_010, 7)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_007_mip_010_trading_intensity_378_010'] = {'inputs': ['mip_base_universe_d2_007_mip_010_trading_intensity_378_010'], 'func': mip_base_universe_d3_007_mip_010_trading_intensity_378_010}


def mip_base_universe_d3_008_mip_012_price_level_distress_756_012(mip_base_universe_d2_008_mip_012_price_level_distress_756_012):
    return _base_universe_d3(mip_base_universe_d2_008_mip_012_price_level_distress_756_012, 8)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_008_mip_012_price_level_distress_756_012'] = {'inputs': ['mip_base_universe_d2_008_mip_012_price_level_distress_756_012'], 'func': mip_base_universe_d3_008_mip_012_price_level_distress_756_012}


def mip_base_universe_d3_009_mip_014_zero_volume_frequency_1260_014(mip_base_universe_d2_009_mip_014_zero_volume_frequency_1260_014):
    return _base_universe_d3(mip_base_universe_d2_009_mip_014_zero_volume_frequency_1260_014, 9)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_009_mip_014_zero_volume_frequency_1260_014'] = {'inputs': ['mip_base_universe_d2_009_mip_014_zero_volume_frequency_1260_014'], 'func': mip_base_universe_d3_009_mip_014_zero_volume_frequency_1260_014}


def mip_base_universe_d3_010_mip_015_spread_proxy_1512_015(mip_base_universe_d2_010_mip_015_spread_proxy_1512_015):
    return _base_universe_d3(mip_base_universe_d2_010_mip_015_spread_proxy_1512_015, 10)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_010_mip_015_spread_proxy_1512_015'] = {'inputs': ['mip_base_universe_d2_010_mip_015_spread_proxy_1512_015'], 'func': mip_base_universe_d3_010_mip_015_spread_proxy_1512_015}


def mip_base_universe_d3_011_mip_016_trading_intensity_5_016(mip_base_universe_d2_011_mip_016_trading_intensity_5_016):
    return _base_universe_d3(mip_base_universe_d2_011_mip_016_trading_intensity_5_016, 11)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_011_mip_016_trading_intensity_5_016'] = {'inputs': ['mip_base_universe_d2_011_mip_016_trading_intensity_5_016'], 'func': mip_base_universe_d3_011_mip_016_trading_intensity_5_016}


def mip_base_universe_d3_012_mip_018_price_level_distress_21_018(mip_base_universe_d2_012_mip_018_price_level_distress_21_018):
    return _base_universe_d3(mip_base_universe_d2_012_mip_018_price_level_distress_21_018, 12)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_012_mip_018_price_level_distress_21_018'] = {'inputs': ['mip_base_universe_d2_012_mip_018_price_level_distress_21_018'], 'func': mip_base_universe_d3_012_mip_018_price_level_distress_21_018}


def mip_base_universe_d3_013_mip_020_zero_volume_frequency_63_020(mip_base_universe_d2_013_mip_020_zero_volume_frequency_63_020):
    return _base_universe_d3(mip_base_universe_d2_013_mip_020_zero_volume_frequency_63_020, 13)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_013_mip_020_zero_volume_frequency_63_020'] = {'inputs': ['mip_base_universe_d2_013_mip_020_zero_volume_frequency_63_020'], 'func': mip_base_universe_d3_013_mip_020_zero_volume_frequency_63_020}


def mip_base_universe_d3_014_mip_021_spread_proxy_84_021(mip_base_universe_d2_014_mip_021_spread_proxy_84_021):
    return _base_universe_d3(mip_base_universe_d2_014_mip_021_spread_proxy_84_021, 14)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_014_mip_021_spread_proxy_84_021'] = {'inputs': ['mip_base_universe_d2_014_mip_021_spread_proxy_84_021'], 'func': mip_base_universe_d3_014_mip_021_spread_proxy_84_021}


def mip_base_universe_d3_015_mip_022_trading_intensity_126_022(mip_base_universe_d2_015_mip_022_trading_intensity_126_022):
    return _base_universe_d3(mip_base_universe_d2_015_mip_022_trading_intensity_126_022, 15)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_015_mip_022_trading_intensity_126_022'] = {'inputs': ['mip_base_universe_d2_015_mip_022_trading_intensity_126_022'], 'func': mip_base_universe_d3_015_mip_022_trading_intensity_126_022}


def mip_base_universe_d3_016_mip_024_price_level_distress_252_024(mip_base_universe_d2_016_mip_024_price_level_distress_252_024):
    return _base_universe_d3(mip_base_universe_d2_016_mip_024_price_level_distress_252_024, 16)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_016_mip_024_price_level_distress_252_024'] = {'inputs': ['mip_base_universe_d2_016_mip_024_price_level_distress_252_024'], 'func': mip_base_universe_d3_016_mip_024_price_level_distress_252_024}


def mip_base_universe_d3_017_mip_026_zero_volume_frequency_504_026(mip_base_universe_d2_017_mip_026_zero_volume_frequency_504_026):
    return _base_universe_d3(mip_base_universe_d2_017_mip_026_zero_volume_frequency_504_026, 17)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_017_mip_026_zero_volume_frequency_504_026'] = {'inputs': ['mip_base_universe_d2_017_mip_026_zero_volume_frequency_504_026'], 'func': mip_base_universe_d3_017_mip_026_zero_volume_frequency_504_026}


def mip_base_universe_d3_018_mip_027_spread_proxy_756_027(mip_base_universe_d2_018_mip_027_spread_proxy_756_027):
    return _base_universe_d3(mip_base_universe_d2_018_mip_027_spread_proxy_756_027, 18)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_018_mip_027_spread_proxy_756_027'] = {'inputs': ['mip_base_universe_d2_018_mip_027_spread_proxy_756_027'], 'func': mip_base_universe_d3_018_mip_027_spread_proxy_756_027}


def mip_base_universe_d3_019_mip_028_trading_intensity_1008_028(mip_base_universe_d2_019_mip_028_trading_intensity_1008_028):
    return _base_universe_d3(mip_base_universe_d2_019_mip_028_trading_intensity_1008_028, 19)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_019_mip_028_trading_intensity_1008_028'] = {'inputs': ['mip_base_universe_d2_019_mip_028_trading_intensity_1008_028'], 'func': mip_base_universe_d3_019_mip_028_trading_intensity_1008_028}


def mip_base_universe_d3_020_mip_030_price_level_distress_1512_030(mip_base_universe_d2_020_mip_030_price_level_distress_1512_030):
    return _base_universe_d3(mip_base_universe_d2_020_mip_030_price_level_distress_1512_030, 20)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_020_mip_030_price_level_distress_1512_030'] = {'inputs': ['mip_base_universe_d2_020_mip_030_price_level_distress_1512_030'], 'func': mip_base_universe_d3_020_mip_030_price_level_distress_1512_030}


def mip_base_universe_d3_021_mip_basefill_001(mip_base_universe_d2_021_mip_basefill_001):
    return _base_universe_d3(mip_base_universe_d2_021_mip_basefill_001, 21)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_021_mip_basefill_001'] = {'inputs': ['mip_base_universe_d2_021_mip_basefill_001'], 'func': mip_base_universe_d3_021_mip_basefill_001}


def mip_base_universe_d3_022_mip_basefill_005(mip_base_universe_d2_022_mip_basefill_005):
    return _base_universe_d3(mip_base_universe_d2_022_mip_basefill_005, 22)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_022_mip_basefill_005'] = {'inputs': ['mip_base_universe_d2_022_mip_basefill_005'], 'func': mip_base_universe_d3_022_mip_basefill_005}


def mip_base_universe_d3_023_mip_basefill_007(mip_base_universe_d2_023_mip_basefill_007):
    return _base_universe_d3(mip_base_universe_d2_023_mip_basefill_007, 23)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_023_mip_basefill_007'] = {'inputs': ['mip_base_universe_d2_023_mip_basefill_007'], 'func': mip_base_universe_d3_023_mip_basefill_007}


def mip_base_universe_d3_024_mip_basefill_011(mip_base_universe_d2_024_mip_basefill_011):
    return _base_universe_d3(mip_base_universe_d2_024_mip_basefill_011, 24)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_024_mip_basefill_011'] = {'inputs': ['mip_base_universe_d2_024_mip_basefill_011'], 'func': mip_base_universe_d3_024_mip_basefill_011}


def mip_base_universe_d3_025_mip_basefill_013(mip_base_universe_d2_025_mip_basefill_013):
    return _base_universe_d3(mip_base_universe_d2_025_mip_basefill_013, 25)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_025_mip_basefill_013'] = {'inputs': ['mip_base_universe_d2_025_mip_basefill_013'], 'func': mip_base_universe_d3_025_mip_basefill_013}


def mip_base_universe_d3_026_mip_basefill_017(mip_base_universe_d2_026_mip_basefill_017):
    return _base_universe_d3(mip_base_universe_d2_026_mip_basefill_017, 26)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_026_mip_basefill_017'] = {'inputs': ['mip_base_universe_d2_026_mip_basefill_017'], 'func': mip_base_universe_d3_026_mip_basefill_017}


def mip_base_universe_d3_027_mip_basefill_019(mip_base_universe_d2_027_mip_basefill_019):
    return _base_universe_d3(mip_base_universe_d2_027_mip_basefill_019, 27)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_027_mip_basefill_019'] = {'inputs': ['mip_base_universe_d2_027_mip_basefill_019'], 'func': mip_base_universe_d3_027_mip_basefill_019}


def mip_base_universe_d3_028_mip_basefill_023(mip_base_universe_d2_028_mip_basefill_023):
    return _base_universe_d3(mip_base_universe_d2_028_mip_basefill_023, 28)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_028_mip_basefill_023'] = {'inputs': ['mip_base_universe_d2_028_mip_basefill_023'], 'func': mip_base_universe_d3_028_mip_basefill_023}


def mip_base_universe_d3_029_mip_basefill_025(mip_base_universe_d2_029_mip_basefill_025):
    return _base_universe_d3(mip_base_universe_d2_029_mip_basefill_025, 29)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_029_mip_basefill_025'] = {'inputs': ['mip_base_universe_d2_029_mip_basefill_025'], 'func': mip_base_universe_d3_029_mip_basefill_025}


def mip_base_universe_d3_030_mip_basefill_029(mip_base_universe_d2_030_mip_basefill_029):
    return _base_universe_d3(mip_base_universe_d2_030_mip_basefill_029, 30)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_030_mip_basefill_029'] = {'inputs': ['mip_base_universe_d2_030_mip_basefill_029'], 'func': mip_base_universe_d3_030_mip_basefill_029}


def mip_base_universe_d3_031_mip_basefill_031(mip_base_universe_d2_031_mip_basefill_031):
    return _base_universe_d3(mip_base_universe_d2_031_mip_basefill_031, 31)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_031_mip_basefill_031'] = {'inputs': ['mip_base_universe_d2_031_mip_basefill_031'], 'func': mip_base_universe_d3_031_mip_basefill_031}


def mip_base_universe_d3_032_mip_basefill_032(mip_base_universe_d2_032_mip_basefill_032):
    return _base_universe_d3(mip_base_universe_d2_032_mip_basefill_032, 32)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_032_mip_basefill_032'] = {'inputs': ['mip_base_universe_d2_032_mip_basefill_032'], 'func': mip_base_universe_d3_032_mip_basefill_032}


def mip_base_universe_d3_033_mip_basefill_033(mip_base_universe_d2_033_mip_basefill_033):
    return _base_universe_d3(mip_base_universe_d2_033_mip_basefill_033, 33)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_033_mip_basefill_033'] = {'inputs': ['mip_base_universe_d2_033_mip_basefill_033'], 'func': mip_base_universe_d3_033_mip_basefill_033}


def mip_base_universe_d3_034_mip_basefill_034(mip_base_universe_d2_034_mip_basefill_034):
    return _base_universe_d3(mip_base_universe_d2_034_mip_basefill_034, 34)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_034_mip_basefill_034'] = {'inputs': ['mip_base_universe_d2_034_mip_basefill_034'], 'func': mip_base_universe_d3_034_mip_basefill_034}


def mip_base_universe_d3_035_mip_basefill_035(mip_base_universe_d2_035_mip_basefill_035):
    return _base_universe_d3(mip_base_universe_d2_035_mip_basefill_035, 35)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_035_mip_basefill_035'] = {'inputs': ['mip_base_universe_d2_035_mip_basefill_035'], 'func': mip_base_universe_d3_035_mip_basefill_035}


def mip_base_universe_d3_036_mip_basefill_036(mip_base_universe_d2_036_mip_basefill_036):
    return _base_universe_d3(mip_base_universe_d2_036_mip_basefill_036, 36)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_036_mip_basefill_036'] = {'inputs': ['mip_base_universe_d2_036_mip_basefill_036'], 'func': mip_base_universe_d3_036_mip_basefill_036}


def mip_base_universe_d3_037_mip_basefill_037(mip_base_universe_d2_037_mip_basefill_037):
    return _base_universe_d3(mip_base_universe_d2_037_mip_basefill_037, 37)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_037_mip_basefill_037'] = {'inputs': ['mip_base_universe_d2_037_mip_basefill_037'], 'func': mip_base_universe_d3_037_mip_basefill_037}


def mip_base_universe_d3_038_mip_basefill_038(mip_base_universe_d2_038_mip_basefill_038):
    return _base_universe_d3(mip_base_universe_d2_038_mip_basefill_038, 38)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_038_mip_basefill_038'] = {'inputs': ['mip_base_universe_d2_038_mip_basefill_038'], 'func': mip_base_universe_d3_038_mip_basefill_038}


def mip_base_universe_d3_039_mip_basefill_039(mip_base_universe_d2_039_mip_basefill_039):
    return _base_universe_d3(mip_base_universe_d2_039_mip_basefill_039, 39)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_039_mip_basefill_039'] = {'inputs': ['mip_base_universe_d2_039_mip_basefill_039'], 'func': mip_base_universe_d3_039_mip_basefill_039}


def mip_base_universe_d3_040_mip_basefill_040(mip_base_universe_d2_040_mip_basefill_040):
    return _base_universe_d3(mip_base_universe_d2_040_mip_basefill_040, 40)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_040_mip_basefill_040'] = {'inputs': ['mip_base_universe_d2_040_mip_basefill_040'], 'func': mip_base_universe_d3_040_mip_basefill_040}


def mip_base_universe_d3_041_mip_basefill_041(mip_base_universe_d2_041_mip_basefill_041):
    return _base_universe_d3(mip_base_universe_d2_041_mip_basefill_041, 41)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_041_mip_basefill_041'] = {'inputs': ['mip_base_universe_d2_041_mip_basefill_041'], 'func': mip_base_universe_d3_041_mip_basefill_041}


def mip_base_universe_d3_042_mip_basefill_042(mip_base_universe_d2_042_mip_basefill_042):
    return _base_universe_d3(mip_base_universe_d2_042_mip_basefill_042, 42)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_042_mip_basefill_042'] = {'inputs': ['mip_base_universe_d2_042_mip_basefill_042'], 'func': mip_base_universe_d3_042_mip_basefill_042}


def mip_base_universe_d3_043_mip_basefill_043(mip_base_universe_d2_043_mip_basefill_043):
    return _base_universe_d3(mip_base_universe_d2_043_mip_basefill_043, 43)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_043_mip_basefill_043'] = {'inputs': ['mip_base_universe_d2_043_mip_basefill_043'], 'func': mip_base_universe_d3_043_mip_basefill_043}


def mip_base_universe_d3_044_mip_basefill_044(mip_base_universe_d2_044_mip_basefill_044):
    return _base_universe_d3(mip_base_universe_d2_044_mip_basefill_044, 44)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_044_mip_basefill_044'] = {'inputs': ['mip_base_universe_d2_044_mip_basefill_044'], 'func': mip_base_universe_d3_044_mip_basefill_044}


def mip_base_universe_d3_045_mip_basefill_045(mip_base_universe_d2_045_mip_basefill_045):
    return _base_universe_d3(mip_base_universe_d2_045_mip_basefill_045, 45)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_045_mip_basefill_045'] = {'inputs': ['mip_base_universe_d2_045_mip_basefill_045'], 'func': mip_base_universe_d3_045_mip_basefill_045}


def mip_base_universe_d3_046_mip_basefill_046(mip_base_universe_d2_046_mip_basefill_046):
    return _base_universe_d3(mip_base_universe_d2_046_mip_basefill_046, 46)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_046_mip_basefill_046'] = {'inputs': ['mip_base_universe_d2_046_mip_basefill_046'], 'func': mip_base_universe_d3_046_mip_basefill_046}


def mip_base_universe_d3_047_mip_basefill_047(mip_base_universe_d2_047_mip_basefill_047):
    return _base_universe_d3(mip_base_universe_d2_047_mip_basefill_047, 47)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_047_mip_basefill_047'] = {'inputs': ['mip_base_universe_d2_047_mip_basefill_047'], 'func': mip_base_universe_d3_047_mip_basefill_047}


def mip_base_universe_d3_048_mip_basefill_048(mip_base_universe_d2_048_mip_basefill_048):
    return _base_universe_d3(mip_base_universe_d2_048_mip_basefill_048, 48)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_048_mip_basefill_048'] = {'inputs': ['mip_base_universe_d2_048_mip_basefill_048'], 'func': mip_base_universe_d3_048_mip_basefill_048}


def mip_base_universe_d3_049_mip_basefill_049(mip_base_universe_d2_049_mip_basefill_049):
    return _base_universe_d3(mip_base_universe_d2_049_mip_basefill_049, 49)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_049_mip_basefill_049'] = {'inputs': ['mip_base_universe_d2_049_mip_basefill_049'], 'func': mip_base_universe_d3_049_mip_basefill_049}


def mip_base_universe_d3_050_mip_basefill_050(mip_base_universe_d2_050_mip_basefill_050):
    return _base_universe_d3(mip_base_universe_d2_050_mip_basefill_050, 50)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_050_mip_basefill_050'] = {'inputs': ['mip_base_universe_d2_050_mip_basefill_050'], 'func': mip_base_universe_d3_050_mip_basefill_050}


def mip_base_universe_d3_051_mip_basefill_051(mip_base_universe_d2_051_mip_basefill_051):
    return _base_universe_d3(mip_base_universe_d2_051_mip_basefill_051, 51)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_051_mip_basefill_051'] = {'inputs': ['mip_base_universe_d2_051_mip_basefill_051'], 'func': mip_base_universe_d3_051_mip_basefill_051}


def mip_base_universe_d3_052_mip_basefill_052(mip_base_universe_d2_052_mip_basefill_052):
    return _base_universe_d3(mip_base_universe_d2_052_mip_basefill_052, 52)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_052_mip_basefill_052'] = {'inputs': ['mip_base_universe_d2_052_mip_basefill_052'], 'func': mip_base_universe_d3_052_mip_basefill_052}


def mip_base_universe_d3_053_mip_basefill_053(mip_base_universe_d2_053_mip_basefill_053):
    return _base_universe_d3(mip_base_universe_d2_053_mip_basefill_053, 53)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_053_mip_basefill_053'] = {'inputs': ['mip_base_universe_d2_053_mip_basefill_053'], 'func': mip_base_universe_d3_053_mip_basefill_053}


def mip_base_universe_d3_054_mip_basefill_054(mip_base_universe_d2_054_mip_basefill_054):
    return _base_universe_d3(mip_base_universe_d2_054_mip_basefill_054, 54)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_054_mip_basefill_054'] = {'inputs': ['mip_base_universe_d2_054_mip_basefill_054'], 'func': mip_base_universe_d3_054_mip_basefill_054}


def mip_base_universe_d3_055_mip_basefill_055(mip_base_universe_d2_055_mip_basefill_055):
    return _base_universe_d3(mip_base_universe_d2_055_mip_basefill_055, 55)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_055_mip_basefill_055'] = {'inputs': ['mip_base_universe_d2_055_mip_basefill_055'], 'func': mip_base_universe_d3_055_mip_basefill_055}


def mip_base_universe_d3_056_mip_basefill_056(mip_base_universe_d2_056_mip_basefill_056):
    return _base_universe_d3(mip_base_universe_d2_056_mip_basefill_056, 56)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_056_mip_basefill_056'] = {'inputs': ['mip_base_universe_d2_056_mip_basefill_056'], 'func': mip_base_universe_d3_056_mip_basefill_056}


def mip_base_universe_d3_057_mip_basefill_057(mip_base_universe_d2_057_mip_basefill_057):
    return _base_universe_d3(mip_base_universe_d2_057_mip_basefill_057, 57)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_057_mip_basefill_057'] = {'inputs': ['mip_base_universe_d2_057_mip_basefill_057'], 'func': mip_base_universe_d3_057_mip_basefill_057}


def mip_base_universe_d3_058_mip_basefill_058(mip_base_universe_d2_058_mip_basefill_058):
    return _base_universe_d3(mip_base_universe_d2_058_mip_basefill_058, 58)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_058_mip_basefill_058'] = {'inputs': ['mip_base_universe_d2_058_mip_basefill_058'], 'func': mip_base_universe_d3_058_mip_basefill_058}


def mip_base_universe_d3_059_mip_basefill_059(mip_base_universe_d2_059_mip_basefill_059):
    return _base_universe_d3(mip_base_universe_d2_059_mip_basefill_059, 59)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_059_mip_basefill_059'] = {'inputs': ['mip_base_universe_d2_059_mip_basefill_059'], 'func': mip_base_universe_d3_059_mip_basefill_059}


def mip_base_universe_d3_060_mip_basefill_060(mip_base_universe_d2_060_mip_basefill_060):
    return _base_universe_d3(mip_base_universe_d2_060_mip_basefill_060, 60)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_060_mip_basefill_060'] = {'inputs': ['mip_base_universe_d2_060_mip_basefill_060'], 'func': mip_base_universe_d3_060_mip_basefill_060}


def mip_base_universe_d3_061_mip_basefill_061(mip_base_universe_d2_061_mip_basefill_061):
    return _base_universe_d3(mip_base_universe_d2_061_mip_basefill_061, 61)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_061_mip_basefill_061'] = {'inputs': ['mip_base_universe_d2_061_mip_basefill_061'], 'func': mip_base_universe_d3_061_mip_basefill_061}


def mip_base_universe_d3_062_mip_basefill_062(mip_base_universe_d2_062_mip_basefill_062):
    return _base_universe_d3(mip_base_universe_d2_062_mip_basefill_062, 62)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_062_mip_basefill_062'] = {'inputs': ['mip_base_universe_d2_062_mip_basefill_062'], 'func': mip_base_universe_d3_062_mip_basefill_062}


def mip_base_universe_d3_063_mip_basefill_063(mip_base_universe_d2_063_mip_basefill_063):
    return _base_universe_d3(mip_base_universe_d2_063_mip_basefill_063, 63)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_063_mip_basefill_063'] = {'inputs': ['mip_base_universe_d2_063_mip_basefill_063'], 'func': mip_base_universe_d3_063_mip_basefill_063}


def mip_base_universe_d3_064_mip_basefill_064(mip_base_universe_d2_064_mip_basefill_064):
    return _base_universe_d3(mip_base_universe_d2_064_mip_basefill_064, 64)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_064_mip_basefill_064'] = {'inputs': ['mip_base_universe_d2_064_mip_basefill_064'], 'func': mip_base_universe_d3_064_mip_basefill_064}


def mip_base_universe_d3_065_mip_basefill_065(mip_base_universe_d2_065_mip_basefill_065):
    return _base_universe_d3(mip_base_universe_d2_065_mip_basefill_065, 65)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_065_mip_basefill_065'] = {'inputs': ['mip_base_universe_d2_065_mip_basefill_065'], 'func': mip_base_universe_d3_065_mip_basefill_065}


def mip_base_universe_d3_066_mip_basefill_066(mip_base_universe_d2_066_mip_basefill_066):
    return _base_universe_d3(mip_base_universe_d2_066_mip_basefill_066, 66)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_066_mip_basefill_066'] = {'inputs': ['mip_base_universe_d2_066_mip_basefill_066'], 'func': mip_base_universe_d3_066_mip_basefill_066}


def mip_base_universe_d3_067_mip_basefill_067(mip_base_universe_d2_067_mip_basefill_067):
    return _base_universe_d3(mip_base_universe_d2_067_mip_basefill_067, 67)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_067_mip_basefill_067'] = {'inputs': ['mip_base_universe_d2_067_mip_basefill_067'], 'func': mip_base_universe_d3_067_mip_basefill_067}


def mip_base_universe_d3_068_mip_basefill_068(mip_base_universe_d2_068_mip_basefill_068):
    return _base_universe_d3(mip_base_universe_d2_068_mip_basefill_068, 68)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_068_mip_basefill_068'] = {'inputs': ['mip_base_universe_d2_068_mip_basefill_068'], 'func': mip_base_universe_d3_068_mip_basefill_068}


def mip_base_universe_d3_069_mip_basefill_069(mip_base_universe_d2_069_mip_basefill_069):
    return _base_universe_d3(mip_base_universe_d2_069_mip_basefill_069, 69)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_069_mip_basefill_069'] = {'inputs': ['mip_base_universe_d2_069_mip_basefill_069'], 'func': mip_base_universe_d3_069_mip_basefill_069}


def mip_base_universe_d3_070_mip_basefill_070(mip_base_universe_d2_070_mip_basefill_070):
    return _base_universe_d3(mip_base_universe_d2_070_mip_basefill_070, 70)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_070_mip_basefill_070'] = {'inputs': ['mip_base_universe_d2_070_mip_basefill_070'], 'func': mip_base_universe_d3_070_mip_basefill_070}


def mip_base_universe_d3_071_mip_basefill_071(mip_base_universe_d2_071_mip_basefill_071):
    return _base_universe_d3(mip_base_universe_d2_071_mip_basefill_071, 71)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_071_mip_basefill_071'] = {'inputs': ['mip_base_universe_d2_071_mip_basefill_071'], 'func': mip_base_universe_d3_071_mip_basefill_071}


def mip_base_universe_d3_072_mip_basefill_072(mip_base_universe_d2_072_mip_basefill_072):
    return _base_universe_d3(mip_base_universe_d2_072_mip_basefill_072, 72)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_072_mip_basefill_072'] = {'inputs': ['mip_base_universe_d2_072_mip_basefill_072'], 'func': mip_base_universe_d3_072_mip_basefill_072}


def mip_base_universe_d3_073_mip_basefill_073(mip_base_universe_d2_073_mip_basefill_073):
    return _base_universe_d3(mip_base_universe_d2_073_mip_basefill_073, 73)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_073_mip_basefill_073'] = {'inputs': ['mip_base_universe_d2_073_mip_basefill_073'], 'func': mip_base_universe_d3_073_mip_basefill_073}


def mip_base_universe_d3_074_mip_basefill_074(mip_base_universe_d2_074_mip_basefill_074):
    return _base_universe_d3(mip_base_universe_d2_074_mip_basefill_074, 74)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_074_mip_basefill_074'] = {'inputs': ['mip_base_universe_d2_074_mip_basefill_074'], 'func': mip_base_universe_d3_074_mip_basefill_074}


def mip_base_universe_d3_075_mip_basefill_075(mip_base_universe_d2_075_mip_basefill_075):
    return _base_universe_d3(mip_base_universe_d2_075_mip_basefill_075, 75)
MIP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mip_base_universe_d3_075_mip_basefill_075'] = {'inputs': ['mip_base_universe_d2_075_mip_basefill_075'], 'func': mip_base_universe_d3_075_mip_basefill_075}
