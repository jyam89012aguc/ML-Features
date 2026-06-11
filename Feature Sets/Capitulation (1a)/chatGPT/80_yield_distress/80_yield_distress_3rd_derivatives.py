import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _align_quarterly_to_daily(x, close):
    """Forward-fill sparse Sharadar quarterly/event data to close.index."""
    return _s(x).reindex(_s(close).index).ffill()


def _safe_div(a, b):
    b = _s(b).replace(0, np.nan)
    if np.isscalar(a):
        return a / b
    return _s(a) / b


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



def yld_176_yld_001_pe_compression_z_21_accel_1(yld_151_yld_001_pe_compression_z_21_roc_1):
    feature = _s(yld_151_yld_001_pe_compression_z_21_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def yld_177_yld_007_earnings_yield_spike_252_accel_42(yld_152_yld_007_earnings_yield_spike_252_roc_42):
    feature = _s(yld_152_yld_007_earnings_yield_spike_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def yld_178_yld_013_ev_marketcap_gap_1512_accel_126(yld_153_yld_013_ev_marketcap_gap_1512_roc_126):
    feature = _s(yld_153_yld_013_ev_marketcap_gap_1512_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def yld_179_yld_019_ps_compression_z_84_accel_378(yld_154_yld_019_ps_compression_z_84_roc_378):
    feature = _s(yld_154_yld_019_ps_compression_z_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def yld_180_yld_025_pe_compression_z_756_accel_4(yld_155_yld_025_pe_compression_z_756_roc_4):
    feature = _s(yld_155_yld_025_pe_compression_z_756_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















YIELD_DISTRESS_REGISTRY_3RD_DERIVATIVES = {
    'yld_176_yld_001_pe_compression_z_21_accel_1': {'inputs': ['yld_151_yld_001_pe_compression_z_21_roc_1'], 'func': yld_176_yld_001_pe_compression_z_21_accel_1},
    'yld_177_yld_007_earnings_yield_spike_252_accel_42': {'inputs': ['yld_152_yld_007_earnings_yield_spike_252_roc_42'], 'func': yld_177_yld_007_earnings_yield_spike_252_accel_42},
    'yld_178_yld_013_ev_marketcap_gap_1512_accel_126': {'inputs': ['yld_153_yld_013_ev_marketcap_gap_1512_roc_126'], 'func': yld_178_yld_013_ev_marketcap_gap_1512_accel_126},
    'yld_179_yld_019_ps_compression_z_84_accel_378': {'inputs': ['yld_154_yld_019_ps_compression_z_84_roc_378'], 'func': yld_179_yld_019_ps_compression_z_84_accel_378},
    'yld_180_yld_025_pe_compression_z_756_accel_4': {'inputs': ['yld_155_yld_025_pe_compression_z_756_roc_4'], 'func': yld_180_yld_025_pe_compression_z_756_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def yd_replacement_d3_001(yd_replacement_d2_001):
    feature = _clean(yd_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_001'] = {'inputs': ['yd_replacement_d2_001'], 'func': yd_replacement_d3_001}


def yd_replacement_d3_002(yd_replacement_d2_002):
    feature = _clean(yd_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_002'] = {'inputs': ['yd_replacement_d2_002'], 'func': yd_replacement_d3_002}


def yd_replacement_d3_003(yd_replacement_d2_003):
    feature = _clean(yd_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_003'] = {'inputs': ['yd_replacement_d2_003'], 'func': yd_replacement_d3_003}


def yd_replacement_d3_004(yd_replacement_d2_004):
    feature = _clean(yd_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_004'] = {'inputs': ['yd_replacement_d2_004'], 'func': yd_replacement_d3_004}


def yd_replacement_d3_005(yd_replacement_d2_005):
    feature = _clean(yd_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_005'] = {'inputs': ['yd_replacement_d2_005'], 'func': yd_replacement_d3_005}


def yd_replacement_d3_006(yd_replacement_d2_006):
    feature = _clean(yd_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_006'] = {'inputs': ['yd_replacement_d2_006'], 'func': yd_replacement_d3_006}


def yd_replacement_d3_007(yd_replacement_d2_007):
    feature = _clean(yd_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_007'] = {'inputs': ['yd_replacement_d2_007'], 'func': yd_replacement_d3_007}


def yd_replacement_d3_008(yd_replacement_d2_008):
    feature = _clean(yd_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_008'] = {'inputs': ['yd_replacement_d2_008'], 'func': yd_replacement_d3_008}


def yd_replacement_d3_009(yd_replacement_d2_009):
    feature = _clean(yd_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_009'] = {'inputs': ['yd_replacement_d2_009'], 'func': yd_replacement_d3_009}


def yd_replacement_d3_010(yd_replacement_d2_010):
    feature = _clean(yd_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_010'] = {'inputs': ['yd_replacement_d2_010'], 'func': yd_replacement_d3_010}


def yd_replacement_d3_011(yd_replacement_d2_011):
    feature = _clean(yd_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_011'] = {'inputs': ['yd_replacement_d2_011'], 'func': yd_replacement_d3_011}


def yd_replacement_d3_012(yd_replacement_d2_012):
    feature = _clean(yd_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_012'] = {'inputs': ['yd_replacement_d2_012'], 'func': yd_replacement_d3_012}


def yd_replacement_d3_013(yd_replacement_d2_013):
    feature = _clean(yd_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_013'] = {'inputs': ['yd_replacement_d2_013'], 'func': yd_replacement_d3_013}


def yd_replacement_d3_014(yd_replacement_d2_014):
    feature = _clean(yd_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_014'] = {'inputs': ['yd_replacement_d2_014'], 'func': yd_replacement_d3_014}


def yd_replacement_d3_015(yd_replacement_d2_015):
    feature = _clean(yd_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_015'] = {'inputs': ['yd_replacement_d2_015'], 'func': yd_replacement_d3_015}


def yd_replacement_d3_016(yd_replacement_d2_016):
    feature = _clean(yd_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_016'] = {'inputs': ['yd_replacement_d2_016'], 'func': yd_replacement_d3_016}


def yd_replacement_d3_017(yd_replacement_d2_017):
    feature = _clean(yd_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_017'] = {'inputs': ['yd_replacement_d2_017'], 'func': yd_replacement_d3_017}


def yd_replacement_d3_018(yd_replacement_d2_018):
    feature = _clean(yd_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_018'] = {'inputs': ['yd_replacement_d2_018'], 'func': yd_replacement_d3_018}


def yd_replacement_d3_019(yd_replacement_d2_019):
    feature = _clean(yd_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_019'] = {'inputs': ['yd_replacement_d2_019'], 'func': yd_replacement_d3_019}


def yd_replacement_d3_020(yd_replacement_d2_020):
    feature = _clean(yd_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_020'] = {'inputs': ['yd_replacement_d2_020'], 'func': yd_replacement_d3_020}


def yd_replacement_d3_021(yd_replacement_d2_021):
    feature = _clean(yd_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_021'] = {'inputs': ['yd_replacement_d2_021'], 'func': yd_replacement_d3_021}


def yd_replacement_d3_022(yd_replacement_d2_022):
    feature = _clean(yd_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_022'] = {'inputs': ['yd_replacement_d2_022'], 'func': yd_replacement_d3_022}


def yd_replacement_d3_023(yd_replacement_d2_023):
    feature = _clean(yd_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_023'] = {'inputs': ['yd_replacement_d2_023'], 'func': yd_replacement_d3_023}


def yd_replacement_d3_024(yd_replacement_d2_024):
    feature = _clean(yd_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_024'] = {'inputs': ['yd_replacement_d2_024'], 'func': yd_replacement_d3_024}


def yd_replacement_d3_025(yd_replacement_d2_025):
    feature = _clean(yd_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_025'] = {'inputs': ['yd_replacement_d2_025'], 'func': yd_replacement_d3_025}


def yd_replacement_d3_026(yd_replacement_d2_026):
    feature = _clean(yd_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_026'] = {'inputs': ['yd_replacement_d2_026'], 'func': yd_replacement_d3_026}


def yd_replacement_d3_027(yd_replacement_d2_027):
    feature = _clean(yd_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_027'] = {'inputs': ['yd_replacement_d2_027'], 'func': yd_replacement_d3_027}


def yd_replacement_d3_028(yd_replacement_d2_028):
    feature = _clean(yd_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_028'] = {'inputs': ['yd_replacement_d2_028'], 'func': yd_replacement_d3_028}


def yd_replacement_d3_029(yd_replacement_d2_029):
    feature = _clean(yd_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_029'] = {'inputs': ['yd_replacement_d2_029'], 'func': yd_replacement_d3_029}


def yd_replacement_d3_030(yd_replacement_d2_030):
    feature = _clean(yd_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_030'] = {'inputs': ['yd_replacement_d2_030'], 'func': yd_replacement_d3_030}


def yd_replacement_d3_031(yd_replacement_d2_031):
    feature = _clean(yd_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_031'] = {'inputs': ['yd_replacement_d2_031'], 'func': yd_replacement_d3_031}


def yd_replacement_d3_032(yd_replacement_d2_032):
    feature = _clean(yd_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_032'] = {'inputs': ['yd_replacement_d2_032'], 'func': yd_replacement_d3_032}


def yd_replacement_d3_033(yd_replacement_d2_033):
    feature = _clean(yd_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_033'] = {'inputs': ['yd_replacement_d2_033'], 'func': yd_replacement_d3_033}


def yd_replacement_d3_034(yd_replacement_d2_034):
    feature = _clean(yd_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_034'] = {'inputs': ['yd_replacement_d2_034'], 'func': yd_replacement_d3_034}


def yd_replacement_d3_035(yd_replacement_d2_035):
    feature = _clean(yd_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_035'] = {'inputs': ['yd_replacement_d2_035'], 'func': yd_replacement_d3_035}


def yd_replacement_d3_036(yd_replacement_d2_036):
    feature = _clean(yd_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_036'] = {'inputs': ['yd_replacement_d2_036'], 'func': yd_replacement_d3_036}


def yd_replacement_d3_037(yd_replacement_d2_037):
    feature = _clean(yd_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_037'] = {'inputs': ['yd_replacement_d2_037'], 'func': yd_replacement_d3_037}


def yd_replacement_d3_038(yd_replacement_d2_038):
    feature = _clean(yd_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_038'] = {'inputs': ['yd_replacement_d2_038'], 'func': yd_replacement_d3_038}


def yd_replacement_d3_039(yd_replacement_d2_039):
    feature = _clean(yd_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_039'] = {'inputs': ['yd_replacement_d2_039'], 'func': yd_replacement_d3_039}


def yd_replacement_d3_040(yd_replacement_d2_040):
    feature = _clean(yd_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_040'] = {'inputs': ['yd_replacement_d2_040'], 'func': yd_replacement_d3_040}


def yd_replacement_d3_041(yd_replacement_d2_041):
    feature = _clean(yd_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_041'] = {'inputs': ['yd_replacement_d2_041'], 'func': yd_replacement_d3_041}


def yd_replacement_d3_042(yd_replacement_d2_042):
    feature = _clean(yd_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_042'] = {'inputs': ['yd_replacement_d2_042'], 'func': yd_replacement_d3_042}


def yd_replacement_d3_043(yd_replacement_d2_043):
    feature = _clean(yd_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_043'] = {'inputs': ['yd_replacement_d2_043'], 'func': yd_replacement_d3_043}


def yd_replacement_d3_044(yd_replacement_d2_044):
    feature = _clean(yd_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_044'] = {'inputs': ['yd_replacement_d2_044'], 'func': yd_replacement_d3_044}


def yd_replacement_d3_045(yd_replacement_d2_045):
    feature = _clean(yd_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_045'] = {'inputs': ['yd_replacement_d2_045'], 'func': yd_replacement_d3_045}


def yd_replacement_d3_046(yd_replacement_d2_046):
    feature = _clean(yd_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_046'] = {'inputs': ['yd_replacement_d2_046'], 'func': yd_replacement_d3_046}


def yd_replacement_d3_047(yd_replacement_d2_047):
    feature = _clean(yd_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_047'] = {'inputs': ['yd_replacement_d2_047'], 'func': yd_replacement_d3_047}


def yd_replacement_d3_048(yd_replacement_d2_048):
    feature = _clean(yd_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_048'] = {'inputs': ['yd_replacement_d2_048'], 'func': yd_replacement_d3_048}


def yd_replacement_d3_049(yd_replacement_d2_049):
    feature = _clean(yd_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_049'] = {'inputs': ['yd_replacement_d2_049'], 'func': yd_replacement_d3_049}


def yd_replacement_d3_050(yd_replacement_d2_050):
    feature = _clean(yd_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_050'] = {'inputs': ['yd_replacement_d2_050'], 'func': yd_replacement_d3_050}


def yd_replacement_d3_051(yd_replacement_d2_051):
    feature = _clean(yd_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_051'] = {'inputs': ['yd_replacement_d2_051'], 'func': yd_replacement_d3_051}


def yd_replacement_d3_052(yd_replacement_d2_052):
    feature = _clean(yd_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_052'] = {'inputs': ['yd_replacement_d2_052'], 'func': yd_replacement_d3_052}


def yd_replacement_d3_053(yd_replacement_d2_053):
    feature = _clean(yd_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_053'] = {'inputs': ['yd_replacement_d2_053'], 'func': yd_replacement_d3_053}


def yd_replacement_d3_054(yd_replacement_d2_054):
    feature = _clean(yd_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_054'] = {'inputs': ['yd_replacement_d2_054'], 'func': yd_replacement_d3_054}


def yd_replacement_d3_055(yd_replacement_d2_055):
    feature = _clean(yd_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_055'] = {'inputs': ['yd_replacement_d2_055'], 'func': yd_replacement_d3_055}


def yd_replacement_d3_056(yd_replacement_d2_056):
    feature = _clean(yd_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_056'] = {'inputs': ['yd_replacement_d2_056'], 'func': yd_replacement_d3_056}


def yd_replacement_d3_057(yd_replacement_d2_057):
    feature = _clean(yd_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_057'] = {'inputs': ['yd_replacement_d2_057'], 'func': yd_replacement_d3_057}


def yd_replacement_d3_058(yd_replacement_d2_058):
    feature = _clean(yd_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_058'] = {'inputs': ['yd_replacement_d2_058'], 'func': yd_replacement_d3_058}


def yd_replacement_d3_059(yd_replacement_d2_059):
    feature = _clean(yd_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_059'] = {'inputs': ['yd_replacement_d2_059'], 'func': yd_replacement_d3_059}


def yd_replacement_d3_060(yd_replacement_d2_060):
    feature = _clean(yd_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_060'] = {'inputs': ['yd_replacement_d2_060'], 'func': yd_replacement_d3_060}


def yd_replacement_d3_061(yd_replacement_d2_061):
    feature = _clean(yd_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_061'] = {'inputs': ['yd_replacement_d2_061'], 'func': yd_replacement_d3_061}


def yd_replacement_d3_062(yd_replacement_d2_062):
    feature = _clean(yd_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_062'] = {'inputs': ['yd_replacement_d2_062'], 'func': yd_replacement_d3_062}


def yd_replacement_d3_063(yd_replacement_d2_063):
    feature = _clean(yd_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_063'] = {'inputs': ['yd_replacement_d2_063'], 'func': yd_replacement_d3_063}


def yd_replacement_d3_064(yd_replacement_d2_064):
    feature = _clean(yd_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_064'] = {'inputs': ['yd_replacement_d2_064'], 'func': yd_replacement_d3_064}


def yd_replacement_d3_065(yd_replacement_d2_065):
    feature = _clean(yd_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_065'] = {'inputs': ['yd_replacement_d2_065'], 'func': yd_replacement_d3_065}


def yd_replacement_d3_066(yd_replacement_d2_066):
    feature = _clean(yd_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_066'] = {'inputs': ['yd_replacement_d2_066'], 'func': yd_replacement_d3_066}


def yd_replacement_d3_067(yd_replacement_d2_067):
    feature = _clean(yd_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_067'] = {'inputs': ['yd_replacement_d2_067'], 'func': yd_replacement_d3_067}


def yd_replacement_d3_068(yd_replacement_d2_068):
    feature = _clean(yd_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_068'] = {'inputs': ['yd_replacement_d2_068'], 'func': yd_replacement_d3_068}


def yd_replacement_d3_069(yd_replacement_d2_069):
    feature = _clean(yd_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_069'] = {'inputs': ['yd_replacement_d2_069'], 'func': yd_replacement_d3_069}


def yd_replacement_d3_070(yd_replacement_d2_070):
    feature = _clean(yd_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_070'] = {'inputs': ['yd_replacement_d2_070'], 'func': yd_replacement_d3_070}


def yd_replacement_d3_071(yd_replacement_d2_071):
    feature = _clean(yd_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_071'] = {'inputs': ['yd_replacement_d2_071'], 'func': yd_replacement_d3_071}


def yd_replacement_d3_072(yd_replacement_d2_072):
    feature = _clean(yd_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_072'] = {'inputs': ['yd_replacement_d2_072'], 'func': yd_replacement_d3_072}


def yd_replacement_d3_073(yd_replacement_d2_073):
    feature = _clean(yd_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_073'] = {'inputs': ['yd_replacement_d2_073'], 'func': yd_replacement_d3_073}


def yd_replacement_d3_074(yd_replacement_d2_074):
    feature = _clean(yd_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_074'] = {'inputs': ['yd_replacement_d2_074'], 'func': yd_replacement_d3_074}


def yd_replacement_d3_075(yd_replacement_d2_075):
    feature = _clean(yd_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_075'] = {'inputs': ['yd_replacement_d2_075'], 'func': yd_replacement_d3_075}


def yd_replacement_d3_076(yd_replacement_d2_076):
    feature = _clean(yd_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_076'] = {'inputs': ['yd_replacement_d2_076'], 'func': yd_replacement_d3_076}


def yd_replacement_d3_077(yd_replacement_d2_077):
    feature = _clean(yd_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_077'] = {'inputs': ['yd_replacement_d2_077'], 'func': yd_replacement_d3_077}


def yd_replacement_d3_078(yd_replacement_d2_078):
    feature = _clean(yd_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_078'] = {'inputs': ['yd_replacement_d2_078'], 'func': yd_replacement_d3_078}


def yd_replacement_d3_079(yd_replacement_d2_079):
    feature = _clean(yd_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_079'] = {'inputs': ['yd_replacement_d2_079'], 'func': yd_replacement_d3_079}


def yd_replacement_d3_080(yd_replacement_d2_080):
    feature = _clean(yd_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_080'] = {'inputs': ['yd_replacement_d2_080'], 'func': yd_replacement_d3_080}


def yd_replacement_d3_081(yd_replacement_d2_081):
    feature = _clean(yd_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_081'] = {'inputs': ['yd_replacement_d2_081'], 'func': yd_replacement_d3_081}


def yd_replacement_d3_082(yd_replacement_d2_082):
    feature = _clean(yd_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_082'] = {'inputs': ['yd_replacement_d2_082'], 'func': yd_replacement_d3_082}


def yd_replacement_d3_083(yd_replacement_d2_083):
    feature = _clean(yd_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_083'] = {'inputs': ['yd_replacement_d2_083'], 'func': yd_replacement_d3_083}


def yd_replacement_d3_084(yd_replacement_d2_084):
    feature = _clean(yd_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_084'] = {'inputs': ['yd_replacement_d2_084'], 'func': yd_replacement_d3_084}


def yd_replacement_d3_085(yd_replacement_d2_085):
    feature = _clean(yd_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_085'] = {'inputs': ['yd_replacement_d2_085'], 'func': yd_replacement_d3_085}


def yd_replacement_d3_086(yd_replacement_d2_086):
    feature = _clean(yd_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_086'] = {'inputs': ['yd_replacement_d2_086'], 'func': yd_replacement_d3_086}


def yd_replacement_d3_087(yd_replacement_d2_087):
    feature = _clean(yd_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_087'] = {'inputs': ['yd_replacement_d2_087'], 'func': yd_replacement_d3_087}


def yd_replacement_d3_088(yd_replacement_d2_088):
    feature = _clean(yd_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_088'] = {'inputs': ['yd_replacement_d2_088'], 'func': yd_replacement_d3_088}


def yd_replacement_d3_089(yd_replacement_d2_089):
    feature = _clean(yd_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_089'] = {'inputs': ['yd_replacement_d2_089'], 'func': yd_replacement_d3_089}


def yd_replacement_d3_090(yd_replacement_d2_090):
    feature = _clean(yd_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_090'] = {'inputs': ['yd_replacement_d2_090'], 'func': yd_replacement_d3_090}


def yd_replacement_d3_091(yd_replacement_d2_091):
    feature = _clean(yd_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_091'] = {'inputs': ['yd_replacement_d2_091'], 'func': yd_replacement_d3_091}


def yd_replacement_d3_092(yd_replacement_d2_092):
    feature = _clean(yd_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_092'] = {'inputs': ['yd_replacement_d2_092'], 'func': yd_replacement_d3_092}


def yd_replacement_d3_093(yd_replacement_d2_093):
    feature = _clean(yd_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_093'] = {'inputs': ['yd_replacement_d2_093'], 'func': yd_replacement_d3_093}


def yd_replacement_d3_094(yd_replacement_d2_094):
    feature = _clean(yd_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_094'] = {'inputs': ['yd_replacement_d2_094'], 'func': yd_replacement_d3_094}


def yd_replacement_d3_095(yd_replacement_d2_095):
    feature = _clean(yd_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_095'] = {'inputs': ['yd_replacement_d2_095'], 'func': yd_replacement_d3_095}


def yd_replacement_d3_096(yd_replacement_d2_096):
    feature = _clean(yd_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_096'] = {'inputs': ['yd_replacement_d2_096'], 'func': yd_replacement_d3_096}


def yd_replacement_d3_097(yd_replacement_d2_097):
    feature = _clean(yd_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_097'] = {'inputs': ['yd_replacement_d2_097'], 'func': yd_replacement_d3_097}


def yd_replacement_d3_098(yd_replacement_d2_098):
    feature = _clean(yd_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_098'] = {'inputs': ['yd_replacement_d2_098'], 'func': yd_replacement_d3_098}


def yd_replacement_d3_099(yd_replacement_d2_099):
    feature = _clean(yd_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_099'] = {'inputs': ['yd_replacement_d2_099'], 'func': yd_replacement_d3_099}


def yd_replacement_d3_100(yd_replacement_d2_100):
    feature = _clean(yd_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_100'] = {'inputs': ['yd_replacement_d2_100'], 'func': yd_replacement_d3_100}


def yd_replacement_d3_101(yd_replacement_d2_101):
    feature = _clean(yd_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_101'] = {'inputs': ['yd_replacement_d2_101'], 'func': yd_replacement_d3_101}


def yd_replacement_d3_102(yd_replacement_d2_102):
    feature = _clean(yd_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_102'] = {'inputs': ['yd_replacement_d2_102'], 'func': yd_replacement_d3_102}


def yd_replacement_d3_103(yd_replacement_d2_103):
    feature = _clean(yd_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_103'] = {'inputs': ['yd_replacement_d2_103'], 'func': yd_replacement_d3_103}


def yd_replacement_d3_104(yd_replacement_d2_104):
    feature = _clean(yd_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_104'] = {'inputs': ['yd_replacement_d2_104'], 'func': yd_replacement_d3_104}


def yd_replacement_d3_105(yd_replacement_d2_105):
    feature = _clean(yd_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_105'] = {'inputs': ['yd_replacement_d2_105'], 'func': yd_replacement_d3_105}


def yd_replacement_d3_106(yd_replacement_d2_106):
    feature = _clean(yd_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_106'] = {'inputs': ['yd_replacement_d2_106'], 'func': yd_replacement_d3_106}


def yd_replacement_d3_107(yd_replacement_d2_107):
    feature = _clean(yd_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_107'] = {'inputs': ['yd_replacement_d2_107'], 'func': yd_replacement_d3_107}


def yd_replacement_d3_108(yd_replacement_d2_108):
    feature = _clean(yd_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_108'] = {'inputs': ['yd_replacement_d2_108'], 'func': yd_replacement_d3_108}


def yd_replacement_d3_109(yd_replacement_d2_109):
    feature = _clean(yd_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_109'] = {'inputs': ['yd_replacement_d2_109'], 'func': yd_replacement_d3_109}


def yd_replacement_d3_110(yd_replacement_d2_110):
    feature = _clean(yd_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_110'] = {'inputs': ['yd_replacement_d2_110'], 'func': yd_replacement_d3_110}


def yd_replacement_d3_111(yd_replacement_d2_111):
    feature = _clean(yd_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_111'] = {'inputs': ['yd_replacement_d2_111'], 'func': yd_replacement_d3_111}


def yd_replacement_d3_112(yd_replacement_d2_112):
    feature = _clean(yd_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_112'] = {'inputs': ['yd_replacement_d2_112'], 'func': yd_replacement_d3_112}


def yd_replacement_d3_113(yd_replacement_d2_113):
    feature = _clean(yd_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_113'] = {'inputs': ['yd_replacement_d2_113'], 'func': yd_replacement_d3_113}


def yd_replacement_d3_114(yd_replacement_d2_114):
    feature = _clean(yd_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_114'] = {'inputs': ['yd_replacement_d2_114'], 'func': yd_replacement_d3_114}


def yd_replacement_d3_115(yd_replacement_d2_115):
    feature = _clean(yd_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_115'] = {'inputs': ['yd_replacement_d2_115'], 'func': yd_replacement_d3_115}


def yd_replacement_d3_116(yd_replacement_d2_116):
    feature = _clean(yd_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_116'] = {'inputs': ['yd_replacement_d2_116'], 'func': yd_replacement_d3_116}


def yd_replacement_d3_117(yd_replacement_d2_117):
    feature = _clean(yd_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_117'] = {'inputs': ['yd_replacement_d2_117'], 'func': yd_replacement_d3_117}


def yd_replacement_d3_118(yd_replacement_d2_118):
    feature = _clean(yd_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_118'] = {'inputs': ['yd_replacement_d2_118'], 'func': yd_replacement_d3_118}


def yd_replacement_d3_119(yd_replacement_d2_119):
    feature = _clean(yd_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_119'] = {'inputs': ['yd_replacement_d2_119'], 'func': yd_replacement_d3_119}


def yd_replacement_d3_120(yd_replacement_d2_120):
    feature = _clean(yd_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_120'] = {'inputs': ['yd_replacement_d2_120'], 'func': yd_replacement_d3_120}


def yd_replacement_d3_121(yd_replacement_d2_121):
    feature = _clean(yd_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_121'] = {'inputs': ['yd_replacement_d2_121'], 'func': yd_replacement_d3_121}


def yd_replacement_d3_122(yd_replacement_d2_122):
    feature = _clean(yd_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_122'] = {'inputs': ['yd_replacement_d2_122'], 'func': yd_replacement_d3_122}


def yd_replacement_d3_123(yd_replacement_d2_123):
    feature = _clean(yd_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_123'] = {'inputs': ['yd_replacement_d2_123'], 'func': yd_replacement_d3_123}


def yd_replacement_d3_124(yd_replacement_d2_124):
    feature = _clean(yd_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_124'] = {'inputs': ['yd_replacement_d2_124'], 'func': yd_replacement_d3_124}


def yd_replacement_d3_125(yd_replacement_d2_125):
    feature = _clean(yd_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_125'] = {'inputs': ['yd_replacement_d2_125'], 'func': yd_replacement_d3_125}


def yd_replacement_d3_126(yd_replacement_d2_126):
    feature = _clean(yd_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_126'] = {'inputs': ['yd_replacement_d2_126'], 'func': yd_replacement_d3_126}


def yd_replacement_d3_127(yd_replacement_d2_127):
    feature = _clean(yd_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_127'] = {'inputs': ['yd_replacement_d2_127'], 'func': yd_replacement_d3_127}


def yd_replacement_d3_128(yd_replacement_d2_128):
    feature = _clean(yd_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_128'] = {'inputs': ['yd_replacement_d2_128'], 'func': yd_replacement_d3_128}


def yd_replacement_d3_129(yd_replacement_d2_129):
    feature = _clean(yd_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_129'] = {'inputs': ['yd_replacement_d2_129'], 'func': yd_replacement_d3_129}


def yd_replacement_d3_130(yd_replacement_d2_130):
    feature = _clean(yd_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_130'] = {'inputs': ['yd_replacement_d2_130'], 'func': yd_replacement_d3_130}


def yd_replacement_d3_131(yd_replacement_d2_131):
    feature = _clean(yd_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_131'] = {'inputs': ['yd_replacement_d2_131'], 'func': yd_replacement_d3_131}


def yd_replacement_d3_132(yd_replacement_d2_132):
    feature = _clean(yd_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_132'] = {'inputs': ['yd_replacement_d2_132'], 'func': yd_replacement_d3_132}


def yd_replacement_d3_133(yd_replacement_d2_133):
    feature = _clean(yd_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_133'] = {'inputs': ['yd_replacement_d2_133'], 'func': yd_replacement_d3_133}


def yd_replacement_d3_134(yd_replacement_d2_134):
    feature = _clean(yd_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_134'] = {'inputs': ['yd_replacement_d2_134'], 'func': yd_replacement_d3_134}


def yd_replacement_d3_135(yd_replacement_d2_135):
    feature = _clean(yd_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_135'] = {'inputs': ['yd_replacement_d2_135'], 'func': yd_replacement_d3_135}


def yd_replacement_d3_136(yd_replacement_d2_136):
    feature = _clean(yd_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_136'] = {'inputs': ['yd_replacement_d2_136'], 'func': yd_replacement_d3_136}


def yd_replacement_d3_137(yd_replacement_d2_137):
    feature = _clean(yd_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_137'] = {'inputs': ['yd_replacement_d2_137'], 'func': yd_replacement_d3_137}


def yd_replacement_d3_138(yd_replacement_d2_138):
    feature = _clean(yd_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
YD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['yd_replacement_d3_138'] = {'inputs': ['yd_replacement_d2_138'], 'func': yd_replacement_d3_138}


# Third-derivative extensions for repaired first-base features.
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def yld_base_universe_d3_001_yld_002_pb_compression_z_42(yld_base_universe_d2_001_yld_002_pb_compression_z_42):
    return _base_universe_d3(yld_base_universe_d2_001_yld_002_pb_compression_z_42, 1)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_001_yld_002_pb_compression_z_42'] = {'inputs': ['yld_base_universe_d2_001_yld_002_pb_compression_z_42'], 'func': yld_base_universe_d3_001_yld_002_pb_compression_z_42}


def yld_base_universe_d3_002_yld_003_ps_compression_z_63(yld_base_universe_d2_002_yld_003_ps_compression_z_63):
    return _base_universe_d3(yld_base_universe_d2_002_yld_003_ps_compression_z_63, 2)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_002_yld_003_ps_compression_z_63'] = {'inputs': ['yld_base_universe_d2_002_yld_003_ps_compression_z_63'], 'func': yld_base_universe_d3_002_yld_003_ps_compression_z_63}


def yld_base_universe_d3_003_yld_005_ev_marketcap_gap_126(yld_base_universe_d2_003_yld_005_ev_marketcap_gap_126):
    return _base_universe_d3(yld_base_universe_d2_003_yld_005_ev_marketcap_gap_126, 3)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_003_yld_005_ev_marketcap_gap_126'] = {'inputs': ['yld_base_universe_d2_003_yld_005_ev_marketcap_gap_126'], 'func': yld_base_universe_d3_003_yld_005_ev_marketcap_gap_126}


def yld_base_universe_d3_004_yld_006_dividend_yield_spike_189(yld_base_universe_d2_004_yld_006_dividend_yield_spike_189):
    return _base_universe_d3(yld_base_universe_d2_004_yld_006_dividend_yield_spike_189, 4)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_004_yld_006_dividend_yield_spike_189'] = {'inputs': ['yld_base_universe_d2_004_yld_006_dividend_yield_spike_189'], 'func': yld_base_universe_d3_004_yld_006_dividend_yield_spike_189}


def yld_base_universe_d3_005_yld_008_valuation_history_depth_378(yld_base_universe_d2_005_yld_008_valuation_history_depth_378):
    return _base_universe_d3(yld_base_universe_d2_005_yld_008_valuation_history_depth_378, 5)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_005_yld_008_valuation_history_depth_378'] = {'inputs': ['yld_base_universe_d2_005_yld_008_valuation_history_depth_378'], 'func': yld_base_universe_d3_005_yld_008_valuation_history_depth_378}


def yld_base_universe_d3_006_yld_009_pe_compression_z_504(yld_base_universe_d2_006_yld_009_pe_compression_z_504):
    return _base_universe_d3(yld_base_universe_d2_006_yld_009_pe_compression_z_504, 6)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_006_yld_009_pe_compression_z_504'] = {'inputs': ['yld_base_universe_d2_006_yld_009_pe_compression_z_504'], 'func': yld_base_universe_d3_006_yld_009_pe_compression_z_504}


def yld_base_universe_d3_007_yld_010_pb_compression_z_756(yld_base_universe_d2_007_yld_010_pb_compression_z_756):
    return _base_universe_d3(yld_base_universe_d2_007_yld_010_pb_compression_z_756, 7)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_007_yld_010_pb_compression_z_756'] = {'inputs': ['yld_base_universe_d2_007_yld_010_pb_compression_z_756'], 'func': yld_base_universe_d3_007_yld_010_pb_compression_z_756}


def yld_base_universe_d3_008_yld_011_ps_compression_z_1008(yld_base_universe_d2_008_yld_011_ps_compression_z_1008):
    return _base_universe_d3(yld_base_universe_d2_008_yld_011_ps_compression_z_1008, 8)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_008_yld_011_ps_compression_z_1008'] = {'inputs': ['yld_base_universe_d2_008_yld_011_ps_compression_z_1008'], 'func': yld_base_universe_d3_008_yld_011_ps_compression_z_1008}


def yld_base_universe_d3_009_yld_014_dividend_yield_spike_63(yld_base_universe_d2_009_yld_014_dividend_yield_spike_63):
    return _base_universe_d3(yld_base_universe_d2_009_yld_014_dividend_yield_spike_63, 9)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_009_yld_014_dividend_yield_spike_63'] = {'inputs': ['yld_base_universe_d2_009_yld_014_dividend_yield_spike_63'], 'func': yld_base_universe_d3_009_yld_014_dividend_yield_spike_63}


def yld_base_universe_d3_010_yld_016_valuation_history_depth_21(yld_base_universe_d2_010_yld_016_valuation_history_depth_21):
    return _base_universe_d3(yld_base_universe_d2_010_yld_016_valuation_history_depth_21, 10)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_010_yld_016_valuation_history_depth_21'] = {'inputs': ['yld_base_universe_d2_010_yld_016_valuation_history_depth_21'], 'func': yld_base_universe_d3_010_yld_016_valuation_history_depth_21}


def yld_base_universe_d3_011_yld_021_ev_marketcap_gap_189(yld_base_universe_d2_011_yld_021_ev_marketcap_gap_189):
    return _base_universe_d3(yld_base_universe_d2_011_yld_021_ev_marketcap_gap_189, 11)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_011_yld_021_ev_marketcap_gap_189'] = {'inputs': ['yld_base_universe_d2_011_yld_021_ev_marketcap_gap_189'], 'func': yld_base_universe_d3_011_yld_021_ev_marketcap_gap_189}


def yld_base_universe_d3_012_yld_023_earnings_yield_spike_378(yld_base_universe_d2_012_yld_023_earnings_yield_spike_378):
    return _base_universe_d3(yld_base_universe_d2_012_yld_023_earnings_yield_spike_378, 12)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_012_yld_023_earnings_yield_spike_378'] = {'inputs': ['yld_base_universe_d2_012_yld_023_earnings_yield_spike_378'], 'func': yld_base_universe_d3_012_yld_023_earnings_yield_spike_378}


def yld_base_universe_d3_013_yld_024_valuation_history_depth_504(yld_base_universe_d2_013_yld_024_valuation_history_depth_504):
    return _base_universe_d3(yld_base_universe_d2_013_yld_024_valuation_history_depth_504, 13)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_013_yld_024_valuation_history_depth_504'] = {'inputs': ['yld_base_universe_d2_013_yld_024_valuation_history_depth_504'], 'func': yld_base_universe_d3_013_yld_024_valuation_history_depth_504}


def yld_base_universe_d3_014_yld_027_ps_compression_z_1260(yld_base_universe_d2_014_yld_027_ps_compression_z_1260):
    return _base_universe_d3(yld_base_universe_d2_014_yld_027_ps_compression_z_1260, 14)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_014_yld_027_ps_compression_z_1260'] = {'inputs': ['yld_base_universe_d2_014_yld_027_ps_compression_z_1260'], 'func': yld_base_universe_d3_014_yld_027_ps_compression_z_1260}


def yld_base_universe_d3_015_yld_029_ev_marketcap_gap_63(yld_base_universe_d2_015_yld_029_ev_marketcap_gap_63):
    return _base_universe_d3(yld_base_universe_d2_015_yld_029_ev_marketcap_gap_63, 15)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_015_yld_029_ev_marketcap_gap_63'] = {'inputs': ['yld_base_universe_d2_015_yld_029_ev_marketcap_gap_63'], 'func': yld_base_universe_d3_015_yld_029_ev_marketcap_gap_63}


def yld_base_universe_d3_016_yld_031_earnings_yield_spike_21(yld_base_universe_d2_016_yld_031_earnings_yield_spike_21):
    return _base_universe_d3(yld_base_universe_d2_016_yld_031_earnings_yield_spike_21, 16)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_016_yld_031_earnings_yield_spike_21'] = {'inputs': ['yld_base_universe_d2_016_yld_031_earnings_yield_spike_21'], 'func': yld_base_universe_d3_016_yld_031_earnings_yield_spike_21}


def yld_base_universe_d3_017_yld_032_valuation_history_depth_42(yld_base_universe_d2_017_yld_032_valuation_history_depth_42):
    return _base_universe_d3(yld_base_universe_d2_017_yld_032_valuation_history_depth_42, 17)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_017_yld_032_valuation_history_depth_42'] = {'inputs': ['yld_base_universe_d2_017_yld_032_valuation_history_depth_42'], 'func': yld_base_universe_d3_017_yld_032_valuation_history_depth_42}


def yld_base_universe_d3_018_yld_035_ps_compression_z_126(yld_base_universe_d2_018_yld_035_ps_compression_z_126):
    return _base_universe_d3(yld_base_universe_d2_018_yld_035_ps_compression_z_126, 18)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_018_yld_035_ps_compression_z_126'] = {'inputs': ['yld_base_universe_d2_018_yld_035_ps_compression_z_126'], 'func': yld_base_universe_d3_018_yld_035_ps_compression_z_126}


def yld_base_universe_d3_019_yld_037_ev_marketcap_gap_252(yld_base_universe_d2_019_yld_037_ev_marketcap_gap_252):
    return _base_universe_d3(yld_base_universe_d2_019_yld_037_ev_marketcap_gap_252, 19)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_019_yld_037_ev_marketcap_gap_252'] = {'inputs': ['yld_base_universe_d2_019_yld_037_ev_marketcap_gap_252'], 'func': yld_base_universe_d3_019_yld_037_ev_marketcap_gap_252}


def yld_base_universe_d3_020_yld_039_earnings_yield_spike_504(yld_base_universe_d2_020_yld_039_earnings_yield_spike_504):
    return _base_universe_d3(yld_base_universe_d2_020_yld_039_earnings_yield_spike_504, 20)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_020_yld_039_earnings_yield_spike_504'] = {'inputs': ['yld_base_universe_d2_020_yld_039_earnings_yield_spike_504'], 'func': yld_base_universe_d3_020_yld_039_earnings_yield_spike_504}


def yld_base_universe_d3_021_yld_040_valuation_history_depth_756(yld_base_universe_d2_021_yld_040_valuation_history_depth_756):
    return _base_universe_d3(yld_base_universe_d2_021_yld_040_valuation_history_depth_756, 21)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_021_yld_040_valuation_history_depth_756'] = {'inputs': ['yld_base_universe_d2_021_yld_040_valuation_history_depth_756'], 'func': yld_base_universe_d3_021_yld_040_valuation_history_depth_756}


def yld_base_universe_d3_022_yld_043_ps_compression_z_1512(yld_base_universe_d2_022_yld_043_ps_compression_z_1512):
    return _base_universe_d3(yld_base_universe_d2_022_yld_043_ps_compression_z_1512, 22)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_022_yld_043_ps_compression_z_1512'] = {'inputs': ['yld_base_universe_d2_022_yld_043_ps_compression_z_1512'], 'func': yld_base_universe_d3_022_yld_043_ps_compression_z_1512}


def yld_base_universe_d3_023_yld_047_earnings_yield_spike_42(yld_base_universe_d2_023_yld_047_earnings_yield_spike_42):
    return _base_universe_d3(yld_base_universe_d2_023_yld_047_earnings_yield_spike_42, 23)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_023_yld_047_earnings_yield_spike_42'] = {'inputs': ['yld_base_universe_d2_023_yld_047_earnings_yield_spike_42'], 'func': yld_base_universe_d3_023_yld_047_earnings_yield_spike_42}


def yld_base_universe_d3_024_yld_048_valuation_history_depth_63(yld_base_universe_d2_024_yld_048_valuation_history_depth_63):
    return _base_universe_d3(yld_base_universe_d2_024_yld_048_valuation_history_depth_63, 24)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_024_yld_048_valuation_history_depth_63'] = {'inputs': ['yld_base_universe_d2_024_yld_048_valuation_history_depth_63'], 'func': yld_base_universe_d3_024_yld_048_valuation_history_depth_63}


def yld_base_universe_d3_025_yld_051_ps_compression_z_189(yld_base_universe_d2_025_yld_051_ps_compression_z_189):
    return _base_universe_d3(yld_base_universe_d2_025_yld_051_ps_compression_z_189, 25)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_025_yld_051_ps_compression_z_189'] = {'inputs': ['yld_base_universe_d2_025_yld_051_ps_compression_z_189'], 'func': yld_base_universe_d3_025_yld_051_ps_compression_z_189}


def yld_base_universe_d3_026_yld_053_ev_marketcap_gap_378(yld_base_universe_d2_026_yld_053_ev_marketcap_gap_378):
    return _base_universe_d3(yld_base_universe_d2_026_yld_053_ev_marketcap_gap_378, 26)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_026_yld_053_ev_marketcap_gap_378'] = {'inputs': ['yld_base_universe_d2_026_yld_053_ev_marketcap_gap_378'], 'func': yld_base_universe_d3_026_yld_053_ev_marketcap_gap_378}


def yld_base_universe_d3_027_yld_055_earnings_yield_spike_756(yld_base_universe_d2_027_yld_055_earnings_yield_spike_756):
    return _base_universe_d3(yld_base_universe_d2_027_yld_055_earnings_yield_spike_756, 27)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_027_yld_055_earnings_yield_spike_756'] = {'inputs': ['yld_base_universe_d2_027_yld_055_earnings_yield_spike_756'], 'func': yld_base_universe_d3_027_yld_055_earnings_yield_spike_756}


def yld_base_universe_d3_028_yld_056_valuation_history_depth_1008(yld_base_universe_d2_028_yld_056_valuation_history_depth_1008):
    return _base_universe_d3(yld_base_universe_d2_028_yld_056_valuation_history_depth_1008, 28)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_028_yld_056_valuation_history_depth_1008'] = {'inputs': ['yld_base_universe_d2_028_yld_056_valuation_history_depth_1008'], 'func': yld_base_universe_d3_028_yld_056_valuation_history_depth_1008}


def yld_base_universe_d3_029_yld_061_ev_marketcap_gap_21(yld_base_universe_d2_029_yld_061_ev_marketcap_gap_21):
    return _base_universe_d3(yld_base_universe_d2_029_yld_061_ev_marketcap_gap_21, 29)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_029_yld_061_ev_marketcap_gap_21'] = {'inputs': ['yld_base_universe_d2_029_yld_061_ev_marketcap_gap_21'], 'func': yld_base_universe_d3_029_yld_061_ev_marketcap_gap_21}


def yld_base_universe_d3_030_yld_064_valuation_history_depth_84(yld_base_universe_d2_030_yld_064_valuation_history_depth_84):
    return _base_universe_d3(yld_base_universe_d2_030_yld_064_valuation_history_depth_84, 30)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_030_yld_064_valuation_history_depth_84'] = {'inputs': ['yld_base_universe_d2_030_yld_064_valuation_history_depth_84'], 'func': yld_base_universe_d3_030_yld_064_valuation_history_depth_84}


def yld_base_universe_d3_031_yld_067_ps_compression_z_252(yld_base_universe_d2_031_yld_067_ps_compression_z_252):
    return _base_universe_d3(yld_base_universe_d2_031_yld_067_ps_compression_z_252, 31)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_031_yld_067_ps_compression_z_252'] = {'inputs': ['yld_base_universe_d2_031_yld_067_ps_compression_z_252'], 'func': yld_base_universe_d3_031_yld_067_ps_compression_z_252}


def yld_base_universe_d3_032_yld_069_ev_marketcap_gap_504(yld_base_universe_d2_032_yld_069_ev_marketcap_gap_504):
    return _base_universe_d3(yld_base_universe_d2_032_yld_069_ev_marketcap_gap_504, 32)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_032_yld_069_ev_marketcap_gap_504'] = {'inputs': ['yld_base_universe_d2_032_yld_069_ev_marketcap_gap_504'], 'func': yld_base_universe_d3_032_yld_069_ev_marketcap_gap_504}


def yld_base_universe_d3_033_yld_071_earnings_yield_spike_1008(yld_base_universe_d2_033_yld_071_earnings_yield_spike_1008):
    return _base_universe_d3(yld_base_universe_d2_033_yld_071_earnings_yield_spike_1008, 33)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_033_yld_071_earnings_yield_spike_1008'] = {'inputs': ['yld_base_universe_d2_033_yld_071_earnings_yield_spike_1008'], 'func': yld_base_universe_d3_033_yld_071_earnings_yield_spike_1008}


def yld_base_universe_d3_034_yld_072_valuation_history_depth_1260(yld_base_universe_d2_034_yld_072_valuation_history_depth_1260):
    return _base_universe_d3(yld_base_universe_d2_034_yld_072_valuation_history_depth_1260, 34)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_034_yld_072_valuation_history_depth_1260'] = {'inputs': ['yld_base_universe_d2_034_yld_072_valuation_history_depth_1260'], 'func': yld_base_universe_d3_034_yld_072_valuation_history_depth_1260}


def yld_base_universe_d3_035_yld_basefill_004(yld_base_universe_d2_035_yld_basefill_004):
    return _base_universe_d3(yld_base_universe_d2_035_yld_basefill_004, 35)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_035_yld_basefill_004'] = {'inputs': ['yld_base_universe_d2_035_yld_basefill_004'], 'func': yld_base_universe_d3_035_yld_basefill_004}


def yld_base_universe_d3_036_yld_basefill_012(yld_base_universe_d2_036_yld_basefill_012):
    return _base_universe_d3(yld_base_universe_d2_036_yld_basefill_012, 36)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_036_yld_basefill_012'] = {'inputs': ['yld_base_universe_d2_036_yld_basefill_012'], 'func': yld_base_universe_d3_036_yld_basefill_012}


def yld_base_universe_d3_037_yld_basefill_015(yld_base_universe_d2_037_yld_basefill_015):
    return _base_universe_d3(yld_base_universe_d2_037_yld_basefill_015, 37)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_037_yld_basefill_015'] = {'inputs': ['yld_base_universe_d2_037_yld_basefill_015'], 'func': yld_base_universe_d3_037_yld_basefill_015}


def yld_base_universe_d3_038_yld_basefill_017(yld_base_universe_d2_038_yld_basefill_017):
    return _base_universe_d3(yld_base_universe_d2_038_yld_basefill_017, 38)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_038_yld_basefill_017'] = {'inputs': ['yld_base_universe_d2_038_yld_basefill_017'], 'func': yld_base_universe_d3_038_yld_basefill_017}


def yld_base_universe_d3_039_yld_basefill_018(yld_base_universe_d2_039_yld_basefill_018):
    return _base_universe_d3(yld_base_universe_d2_039_yld_basefill_018, 39)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_039_yld_basefill_018'] = {'inputs': ['yld_base_universe_d2_039_yld_basefill_018'], 'func': yld_base_universe_d3_039_yld_basefill_018}


def yld_base_universe_d3_040_yld_basefill_020(yld_base_universe_d2_040_yld_basefill_020):
    return _base_universe_d3(yld_base_universe_d2_040_yld_basefill_020, 40)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_040_yld_basefill_020'] = {'inputs': ['yld_base_universe_d2_040_yld_basefill_020'], 'func': yld_base_universe_d3_040_yld_basefill_020}


def yld_base_universe_d3_041_yld_basefill_022(yld_base_universe_d2_041_yld_basefill_022):
    return _base_universe_d3(yld_base_universe_d2_041_yld_basefill_022, 41)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_041_yld_basefill_022'] = {'inputs': ['yld_base_universe_d2_041_yld_basefill_022'], 'func': yld_base_universe_d3_041_yld_basefill_022}


def yld_base_universe_d3_042_yld_basefill_025(yld_base_universe_d2_042_yld_basefill_025):
    return _base_universe_d3(yld_base_universe_d2_042_yld_basefill_025, 42)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_042_yld_basefill_025'] = {'inputs': ['yld_base_universe_d2_042_yld_basefill_025'], 'func': yld_base_universe_d3_042_yld_basefill_025}


def yld_base_universe_d3_043_yld_basefill_026(yld_base_universe_d2_043_yld_basefill_026):
    return _base_universe_d3(yld_base_universe_d2_043_yld_basefill_026, 43)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_043_yld_basefill_026'] = {'inputs': ['yld_base_universe_d2_043_yld_basefill_026'], 'func': yld_base_universe_d3_043_yld_basefill_026}


def yld_base_universe_d3_044_yld_basefill_028(yld_base_universe_d2_044_yld_basefill_028):
    return _base_universe_d3(yld_base_universe_d2_044_yld_basefill_028, 44)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_044_yld_basefill_028'] = {'inputs': ['yld_base_universe_d2_044_yld_basefill_028'], 'func': yld_base_universe_d3_044_yld_basefill_028}


def yld_base_universe_d3_045_yld_basefill_030(yld_base_universe_d2_045_yld_basefill_030):
    return _base_universe_d3(yld_base_universe_d2_045_yld_basefill_030, 45)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_045_yld_basefill_030'] = {'inputs': ['yld_base_universe_d2_045_yld_basefill_030'], 'func': yld_base_universe_d3_045_yld_basefill_030}


def yld_base_universe_d3_046_yld_basefill_033(yld_base_universe_d2_046_yld_basefill_033):
    return _base_universe_d3(yld_base_universe_d2_046_yld_basefill_033, 46)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_046_yld_basefill_033'] = {'inputs': ['yld_base_universe_d2_046_yld_basefill_033'], 'func': yld_base_universe_d3_046_yld_basefill_033}


def yld_base_universe_d3_047_yld_basefill_034(yld_base_universe_d2_047_yld_basefill_034):
    return _base_universe_d3(yld_base_universe_d2_047_yld_basefill_034, 47)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_047_yld_basefill_034'] = {'inputs': ['yld_base_universe_d2_047_yld_basefill_034'], 'func': yld_base_universe_d3_047_yld_basefill_034}


def yld_base_universe_d3_048_yld_basefill_036(yld_base_universe_d2_048_yld_basefill_036):
    return _base_universe_d3(yld_base_universe_d2_048_yld_basefill_036, 48)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_048_yld_basefill_036'] = {'inputs': ['yld_base_universe_d2_048_yld_basefill_036'], 'func': yld_base_universe_d3_048_yld_basefill_036}


def yld_base_universe_d3_049_yld_basefill_038(yld_base_universe_d2_049_yld_basefill_038):
    return _base_universe_d3(yld_base_universe_d2_049_yld_basefill_038, 49)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_049_yld_basefill_038'] = {'inputs': ['yld_base_universe_d2_049_yld_basefill_038'], 'func': yld_base_universe_d3_049_yld_basefill_038}


def yld_base_universe_d3_050_yld_basefill_041(yld_base_universe_d2_050_yld_basefill_041):
    return _base_universe_d3(yld_base_universe_d2_050_yld_basefill_041, 50)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_050_yld_basefill_041'] = {'inputs': ['yld_base_universe_d2_050_yld_basefill_041'], 'func': yld_base_universe_d3_050_yld_basefill_041}


def yld_base_universe_d3_051_yld_basefill_042(yld_base_universe_d2_051_yld_basefill_042):
    return _base_universe_d3(yld_base_universe_d2_051_yld_basefill_042, 51)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_051_yld_basefill_042'] = {'inputs': ['yld_base_universe_d2_051_yld_basefill_042'], 'func': yld_base_universe_d3_051_yld_basefill_042}


def yld_base_universe_d3_052_yld_basefill_044(yld_base_universe_d2_052_yld_basefill_044):
    return _base_universe_d3(yld_base_universe_d2_052_yld_basefill_044, 52)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_052_yld_basefill_044'] = {'inputs': ['yld_base_universe_d2_052_yld_basefill_044'], 'func': yld_base_universe_d3_052_yld_basefill_044}


def yld_base_universe_d3_053_yld_basefill_045(yld_base_universe_d2_053_yld_basefill_045):
    return _base_universe_d3(yld_base_universe_d2_053_yld_basefill_045, 53)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_053_yld_basefill_045'] = {'inputs': ['yld_base_universe_d2_053_yld_basefill_045'], 'func': yld_base_universe_d3_053_yld_basefill_045}


def yld_base_universe_d3_054_yld_basefill_046(yld_base_universe_d2_054_yld_basefill_046):
    return _base_universe_d3(yld_base_universe_d2_054_yld_basefill_046, 54)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_054_yld_basefill_046'] = {'inputs': ['yld_base_universe_d2_054_yld_basefill_046'], 'func': yld_base_universe_d3_054_yld_basefill_046}


def yld_base_universe_d3_055_yld_basefill_049(yld_base_universe_d2_055_yld_basefill_049):
    return _base_universe_d3(yld_base_universe_d2_055_yld_basefill_049, 55)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_055_yld_basefill_049'] = {'inputs': ['yld_base_universe_d2_055_yld_basefill_049'], 'func': yld_base_universe_d3_055_yld_basefill_049}


def yld_base_universe_d3_056_yld_basefill_050(yld_base_universe_d2_056_yld_basefill_050):
    return _base_universe_d3(yld_base_universe_d2_056_yld_basefill_050, 56)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_056_yld_basefill_050'] = {'inputs': ['yld_base_universe_d2_056_yld_basefill_050'], 'func': yld_base_universe_d3_056_yld_basefill_050}


def yld_base_universe_d3_057_yld_basefill_052(yld_base_universe_d2_057_yld_basefill_052):
    return _base_universe_d3(yld_base_universe_d2_057_yld_basefill_052, 57)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_057_yld_basefill_052'] = {'inputs': ['yld_base_universe_d2_057_yld_basefill_052'], 'func': yld_base_universe_d3_057_yld_basefill_052}


def yld_base_universe_d3_058_yld_basefill_054(yld_base_universe_d2_058_yld_basefill_054):
    return _base_universe_d3(yld_base_universe_d2_058_yld_basefill_054, 58)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_058_yld_basefill_054'] = {'inputs': ['yld_base_universe_d2_058_yld_basefill_054'], 'func': yld_base_universe_d3_058_yld_basefill_054}


def yld_base_universe_d3_059_yld_basefill_057(yld_base_universe_d2_059_yld_basefill_057):
    return _base_universe_d3(yld_base_universe_d2_059_yld_basefill_057, 59)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_059_yld_basefill_057'] = {'inputs': ['yld_base_universe_d2_059_yld_basefill_057'], 'func': yld_base_universe_d3_059_yld_basefill_057}


def yld_base_universe_d3_060_yld_basefill_058(yld_base_universe_d2_060_yld_basefill_058):
    return _base_universe_d3(yld_base_universe_d2_060_yld_basefill_058, 60)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_060_yld_basefill_058'] = {'inputs': ['yld_base_universe_d2_060_yld_basefill_058'], 'func': yld_base_universe_d3_060_yld_basefill_058}


def yld_base_universe_d3_061_yld_basefill_059(yld_base_universe_d2_061_yld_basefill_059):
    return _base_universe_d3(yld_base_universe_d2_061_yld_basefill_059, 61)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_061_yld_basefill_059'] = {'inputs': ['yld_base_universe_d2_061_yld_basefill_059'], 'func': yld_base_universe_d3_061_yld_basefill_059}


def yld_base_universe_d3_062_yld_basefill_060(yld_base_universe_d2_062_yld_basefill_060):
    return _base_universe_d3(yld_base_universe_d2_062_yld_basefill_060, 62)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_062_yld_basefill_060'] = {'inputs': ['yld_base_universe_d2_062_yld_basefill_060'], 'func': yld_base_universe_d3_062_yld_basefill_060}


def yld_base_universe_d3_063_yld_basefill_062(yld_base_universe_d2_063_yld_basefill_062):
    return _base_universe_d3(yld_base_universe_d2_063_yld_basefill_062, 63)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_063_yld_basefill_062'] = {'inputs': ['yld_base_universe_d2_063_yld_basefill_062'], 'func': yld_base_universe_d3_063_yld_basefill_062}


def yld_base_universe_d3_064_yld_basefill_063(yld_base_universe_d2_064_yld_basefill_063):
    return _base_universe_d3(yld_base_universe_d2_064_yld_basefill_063, 64)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_064_yld_basefill_063'] = {'inputs': ['yld_base_universe_d2_064_yld_basefill_063'], 'func': yld_base_universe_d3_064_yld_basefill_063}


def yld_base_universe_d3_065_yld_basefill_065(yld_base_universe_d2_065_yld_basefill_065):
    return _base_universe_d3(yld_base_universe_d2_065_yld_basefill_065, 65)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_065_yld_basefill_065'] = {'inputs': ['yld_base_universe_d2_065_yld_basefill_065'], 'func': yld_base_universe_d3_065_yld_basefill_065}


def yld_base_universe_d3_066_yld_basefill_066(yld_base_universe_d2_066_yld_basefill_066):
    return _base_universe_d3(yld_base_universe_d2_066_yld_basefill_066, 66)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_066_yld_basefill_066'] = {'inputs': ['yld_base_universe_d2_066_yld_basefill_066'], 'func': yld_base_universe_d3_066_yld_basefill_066}


def yld_base_universe_d3_067_yld_basefill_068(yld_base_universe_d2_067_yld_basefill_068):
    return _base_universe_d3(yld_base_universe_d2_067_yld_basefill_068, 67)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_067_yld_basefill_068'] = {'inputs': ['yld_base_universe_d2_067_yld_basefill_068'], 'func': yld_base_universe_d3_067_yld_basefill_068}


def yld_base_universe_d3_068_yld_basefill_070(yld_base_universe_d2_068_yld_basefill_070):
    return _base_universe_d3(yld_base_universe_d2_068_yld_basefill_070, 68)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_068_yld_basefill_070'] = {'inputs': ['yld_base_universe_d2_068_yld_basefill_070'], 'func': yld_base_universe_d3_068_yld_basefill_070}


def yld_base_universe_d3_069_yld_basefill_073(yld_base_universe_d2_069_yld_basefill_073):
    return _base_universe_d3(yld_base_universe_d2_069_yld_basefill_073, 69)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_069_yld_basefill_073'] = {'inputs': ['yld_base_universe_d2_069_yld_basefill_073'], 'func': yld_base_universe_d3_069_yld_basefill_073}


def yld_base_universe_d3_070_yld_basefill_074(yld_base_universe_d2_070_yld_basefill_074):
    return _base_universe_d3(yld_base_universe_d2_070_yld_basefill_074, 70)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_070_yld_basefill_074'] = {'inputs': ['yld_base_universe_d2_070_yld_basefill_074'], 'func': yld_base_universe_d3_070_yld_basefill_074}


def yld_base_universe_d3_071_yld_basefill_075(yld_base_universe_d2_071_yld_basefill_075):
    return _base_universe_d3(yld_base_universe_d2_071_yld_basefill_075, 71)
YLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['yld_base_universe_d3_071_yld_basefill_075'] = {'inputs': ['yld_base_universe_d2_071_yld_basefill_075'], 'func': yld_base_universe_d3_071_yld_basefill_075}
