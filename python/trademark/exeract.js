  function _$uF(_$yx) {
        var _$eq = _$yx.length
          , _$ZR = new Array(Math.floor(_$eq * 3 / 4));
        var _$2a, _$Zq, _$Ys, _$7P;
        var _$Jk = 0
          , _$tQ = 0
          , _$dA = _$eq - 3;
        for (_$Jk = 0; _$Jk < _$dA; ) {
            _$2a = _$yx.charCodeAt(_$Jk++);
            _$Zq = _$yx.charCodeAt(_$Jk++);
            _$Ys = _$yx.charCodeAt(_$Jk++);
            _$7P = _$yx.charCodeAt(_$Jk++);
            _$ZR[_$tQ++] = _$O4[_$2a] | _$oo[_$Zq];
            _$ZR[_$tQ++] = _$Z0[_$Zq] | _$iH[_$Ys];
            _$ZR[_$tQ++] = _$2n[_$Ys] | _$3k[_$7P];
        }
        if (_$Jk < _$eq) {
            _$2a = _$yx.charCodeAt(_$Jk++);
            _$Zq = _$yx.charCodeAt(_$Jk++);
            _$ZR[_$tQ++] = _$O4[_$2a] | _$oo[_$Zq];
            if (_$Jk < _$eq) {
                _$Ys = _$yx.charCodeAt(_$Jk);
                _$ZR[_$tQ++] = _$Z0[_$Zq] | _$iH[_$Ys];
            }
        }
        return _$ZR;
    }
var ss = "qrcklmDoExthWJiHAp1sVYKU3RFMQw8IGfPO92bvLNj.7zXBaSnu0TC6gy_4Ze5d{}|~ !#$%()*+,-;=?@[]^"
var  _$O4 = [],
    _$oo = [],
    _$Z0 = [],
    _$iH = [],
    _$2n = [],
    _$3k = [],
    _$aJ = [];

var _$e6 = ss.split("")

function _$bF() {
    for (_$kx = 0; _$kx <= 255; _$kx++) {
        _$3k[_$kx] = -1;
    }
    for (_$kx = 0; _$kx < _$e6.length; _$kx++) {
        var _$rM = _$e6[_$kx].charCodeAt(0);
        _$O4[_$rM] = _$kx << 2;
        _$oo[_$rM] = _$kx >> 4;
        _$Z0[_$rM] = (_$kx & 15) << 4;
        _$iH[_$rM] = _$kx >> 2;
        _$2n[_$rM] = (_$kx & 3) << 6;
        _$3k[_$rM] = _$kx;
    }
}
_$bF()
console.log(_$uF('S3BU7N4SVe0k_5dlGcJE0G'))
var intParams = [] // 抽取出的4个整形值
var strParams = [] // 抽取出的字符串值
var fourParams = [] // 从二十个函数中抽取的4个值

function _$3t() {
//	var _$T9 = _$uF(_$aJ._$Oi);
//	return _$T9.concat([_$aJ._$IK, _$aJ._$_E, _$aJ._$vu, _$aJ._$dX]);
	var _$T9 = _$uF(strParams[14]);
	return _$T9.concat([fourParams]
}

function _$o4(_$8I) {
    var _$rM = _$8I.length, _$7N = _$IO = 0, _$rq = _$8I.length * 4, _$Lp, _$Xz;
    _$Xz = new Array(_$rq);
    while (_$7N < _$rM) {
        _$Lp = _$8I[_$7N++];
        _$Xz[_$IO++] = (_$Lp >>> 24) & 0xFF;
        _$Xz[_$IO++] = (_$Lp >>> 16) & 0xFF;
        _$Xz[_$IO++] = (_$Lp >>> 8) & 0xFF;
        _$Xz[_$IO++] = _$Lp & 0xFF;
    }
    return _$Xz;
}

function _$9D(_$8I) {
    _$8I = Math.round(_$8I);
    return [((_$8I & 0xFF00) >> 8), (_$8I & 0xFF)];
}

function _$7d(_$8I) {
        var _$rM = _$8I.length;
        var _$7N, _$rq = new Array(_$rM - 1), _$Lp = _$8I.charCodeAt(0) - 97;
        for (var _$Xz = 0, _$ci = 1; _$ci < _$rM; ++_$ci) {
            _$7N = _$8I.charCodeAt(_$ci);
            if (_$7N >= 40 && _$7N < 92) {
                _$7N += _$Lp;
                if (_$7N >= 92)
                    _$7N = _$7N - 52;
            } else if (_$7N >= 97 && _$7N < 127) {
                _$7N += _$Lp;
                if (_$7N >= 127)
                    _$7N = _$7N - 30;
            }
            _$rq[_$Xz++] = _$7N;
        }
        return _$lv.apply(null, _$rq);
    }

 function _$1B(_$8I) {
        return [(_$8I >>> 24) & 0xFF, (_$8I >>> 16) & 0xFF, (_$8I >>> 8) & 0xFF, _$8I & 0xFF];
    }

  function _$wA(_$8I) {
        if (typeof _$8I === _$5U[3])
            _$8I = _$1_(_$8I);
        var _$rM = _$ZO._$5U || (_$ZO._$5U = _$hU());
        var _$7N = 0 ^ (-1)
          , _$rq = _$8I.length;
        for (var _$Lp = 0; _$Lp < _$rq; ) {
            _$7N = (_$7N >>> 8) ^ _$rM[(_$7N ^ _$8I[_$Lp++]) & 0xFF];
        }
        return (_$7N ^ (-1)) >>> 0;
    }

function _$0P() {
    return new Date().getTime()
}

var _$Z6;

function _$o$(_$8I) {
    var _$rM = _$8I.length, _$hH = 0, _$7N, _$rq = 0;
    var _$Lp = _$Xz();
    var _$t3 = new _$mn(_$Lp);
    while (_$hH < _$rM) {
        _$7N = _$Xz();
        _$t3[_$rq++] = _$8I.substr(_$hH, _$7N);
        _$hH += _$7N;
    }
    _$Z6 = _$ci;
    function _$Xz() {
        var _$rM = _$3k[_$8I.charCodeAt(_$hH++)];
        if (_$rM < 0) {
            return _$3k[_$8I.charCodeAt(_$hH++)] * 7396 + _$3k[_$8I.charCodeAt(_$hH++)] * 86 + _$3k[_$8I.charCodeAt(_$hH++)];
        } else if (_$rM < 64) {
            return _$rM;
        } else if (_$rM <= 86) {
            return _$rM * 86 + _$3k[_$8I.charCodeAt(_$hH++)] - 5440;
        }
    }
    function _$ci(_$V3) {
        var _$rM = _$V3 % 64;
        var _$7N = _$V3 - _$rM;
        _$rM = _$M4(_$rM);
//        _$rM ^= _$ZO._$3N;
        _$rM ^= intParams[0];
        _$7N += _$rM;
        return _$t3[_$7N];
    }
}

function _$M4(_$8I) {
    var _$rM = [0, 1, 3, 7, 0xf, 0x1f];
//    return (_$8I >> _$ZO._$Tt) | ((_$8I & _$rM[_$ZO._$Tt]) << (6 - _$ZO._$Tt));
    return (_$8I >> intParams[2]) | ((_$8I & _$rM[intParams[2]]) << (6 - intParams[2]));
}

function _$2v() {
//    var _$rM = _$uF(_$Z6(22) + _$ZO._$QQ);
    var _$rM = _$uF(_$Z6(22) + strParams[11]);
    return _$rM;

}

_$2v().slice(0, 4);

 function extract(param, _$2h) {
    var _$7N = 0;
    var _$rq = new Array(128), _$Lp = 0;
    var _Gl = _$0P();
    _$rq[_$Lp++] = _$3t();
    _$rq[_$Lp++] = _$o4([(_$2h / 0x100000000) & 0xffffffff, _$2h & 0xffffffff]);
    _$rq[_$Lp++] = 1
    _$rq[_$Lp++] = param;
    var _$9a = Math.floor((_$0P() - _$Gl) / 100.0);
    _$rq[_$Lp++] = _$9D(_$9a);
    var _$i4 = _$OP()
    var _$p1 = Math.floor((_$0P() - $i4) / 100.0);
    _$rq[_$Lp++] = _$9D(_$p1);
    _$rq[_$Lp++] = _$2v().slice(0, 4);
    11211   _$rq[_$Lp++] = _$6t;
    _$rq[_$Lp++] = '0'
    _$rq[_$Lp++] = 3;
    _$rq[_$Lp++] = _$o4([25165824, 2]);
    _$rq[_$Lp++] = 14;
    _$rq[_$Lp++] = undefined;
    11781  _$rq[_$Lp++] = _$rM; (10888 _$rM = _$l5(58))
    _$7N |= 1;
    10892  _$rq[_$Lp++] = _$uF(_$_f0);
    rand = Math.floor((Math.random() * 12) + 4);
    rand2 = Math.floor((Math.random() * 4) + 1)
    _$rq[_$Lp++] = _$9D(rand);
    _$rq[_$Lp++] = _$9D(mouseMoveCount);
    _$rq[_$Lp++] = _$9D(rand2);
	_$rq[_$Lp++] = _$9D(0);
	_$rq[_$Lp++] = _$9D(0);
	_$rq[_$Lp++] = _$9D(rand);
	_$rq[_$Lp++] = _$9D(rand2);
	_$rq[_$Lp++] = _$9D(Math.floor((Math.random() * 20) + 10));
	_$rq[_$Lp++] = _$9D(Math.floor((Math.random() * 20) + 10));
	_$rq[_$Lp++] = _$9D(0);
	_$rq[_$Lp++] = _$9D(0);
	_$7N |= 4;
    _$rq[_$Lp++] = _$uF(_$_fh0);
    _$7N |= 8;
	_$rq[_$Lp++] = _$uF(_$_f1);
    _$7N |= 16;
    _$rq[_$Lp++] = 100; // 电池
    _$rq[_$Lp++] = _$9D(0);
    _$7N |= 64;
    _$rq[_$Lp++] = 0; // 网络相关
    _$7N |= 128;
    9953 _$rq[_$Lp++] = _$IC;
    _$7N |= 131072;
    _$rq[_12] = _$1B(_$7N);
    _$rq['splice'](_$Lp)
    return Array['prototype'].concat['apply']([], _$rq);
 }