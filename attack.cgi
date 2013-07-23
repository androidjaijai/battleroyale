#==================#
# ■ 先制攻撃処理  #
#==================#
sub ATTACK {

    $log = ($log . "$w_f_name $w_l_name（$w_cl $w_sex$w_no番）を発見した！<br>") ;
    $log = ($log . "$w_f_name $w_l_name　は こちらには気づいてないな・・・。<br>") ;

    $Command=("BATTLE0" . "_" . $w_id);

}
#==================#
# ■ 先制攻撃処理  #
#==================#
sub ATTACK1 {
    $kega2 = "" ; $kega3 = "" ;
    $hakaiinf2 = ""; $hakaiinf3 = "";

    local($i) = 0 ;
    local($result) = 0 ;
    local($result2) = 0 ;
    local($dice1) = int(rand(100)) ;
    local($dice2) = int(rand(100)) ;

    local($a,$w_kind,$wid) = split(/_/, $Command);

    open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
    for ($i=0; $i<$#userlist+1; $i++) {
        ($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf) = split(/,/, $userlist[$i]);
        if ($w_id eq $wid) {
            $Index2=$i ; last;
        }
    }

    if (($w_bid eq $id)||($w_hit <= 0)) {
        &ERROR("不正アクセスです") ;
    }

    &BB_CK; #ブラウザバック対処

    $log = ($log . "$w_f_name $w_l_name（$w_cl $w_sex$w_no番）と戦闘開始！<br>") ;

    ($w_name,$a) = split(/<>/, $wep);
    ($w_name2,$w_kind2) = split(/<>/, $w_wep);

    &TACTGET; &TACTGET2;    #基本行動

    #プレイヤー
    if ((($wep =~ /G|A/) && ($wtai == 0)) || (($wep =~ /G|A/) && ($w_kind eq "WB"))) {
        $att_p = (($watt/10) + $att) * $atp ;
    } else {
        $att_p = ($watt + $att) * $atp ;
    }
    local($ball) = $def + $bdef + $bdef_h + $bdef_a + $bdef_f ;
    if ($item[5] =~ /AD/) {$ball += $eff[5];} #装飾が防具？
    $def_p = $ball * $dfp ;

    #敵
    if (($w_wep =~ /G|A/) && ($w_wtai == 0)) {
        $att_n = (($w_watt/10) + $w_att) * $atn ;
    } else {
        $att_n = ($w_watt + $w_att) * $atn ;
    }
    local($ball2) = $w_def + $w_bdef + $w_bdef_h + $w_bdef_a + $w_bdef_f ;
    if ($w_item[5] =~ /AD/) {$ball2 += $w_eff[5];} #装飾が防具？
    $def_n = $ball2 * $dfn ;
    $w_bid = $id ;
    $bid = $w_id ;

    &BLOG_CK;
    &EN_KAIFUKU;

    $Command="BATTLE";

    if ($w_pls ne $pls) {   #既に移動？
        $log = ($log . "しかし、$w_f_name $w_l_name（$w_cl $w_sex$w_no番）に逃げられてしまった！<br>") ;
        &SAVE;
        return ;
    }

    if (length($dengon) > 0) {
        $log = ($log . "<font color=\"lime\"><b>$f_name $l_name（$cl $sex$no番）「$dengon」</b></font><br>") ;
        $w_log = ($w_log . "<font color=\"lime\"><b>$hour:$min:$sec $f_name $l_name（$cl $sex$no番）「$dengon」</b></font><br>") ;
    }

    &WEPTREAT($w_name, $w_kind, $wtai, $l_name, $w_l_name, "攻撃", "PC") ;
    if ($dice1 < $mei) {    #攻撃成功

        $result = ($att_p*$wk) - $def_n;
        $result /= 2 ;
        $result += rand($result);

        &DEFTREAT($w_kind, "NPC") ;
        $result = int($result * $pnt) ;

        if ($result <= 0) {$result = 1} ;
        $log = ($log . "<font color=\"red\"><b>$resultダメージ $hakaiinf3 $kega3 </b></font>！<br>") ;

        $w_hit -= $result;
        $w_btai--;
        if ($w_btai <= 0) { $w_bou = "下着<>DN"; $w_bdef=0; $w_btai="∞"; }

        $wep = $wep_2; $watt = $watt_2; $wtai = $wtai_2; $w_inf = $w_inf_2 ;

        $exp++;

    } else {
        $kega3 = "" ;
        $log = ($log . "しかし、避けられた！<br>") ;
    }

    if ($w_hit <= 0) {  #敵死亡？
        &DEATH2;
    } elsif (rand(10) < 5) {    #反撃

        if ($weps eq $weps2) {  #距離一緒？

            &WEPTREAT($w_name2, $w_kind2,  $w_wtai, $w_l_name, $l_name, "反撃", "NPC") ;

            if ($dice2 < $mei2) {   #攻撃成功
                $result2 = ($att_n*$wk) - $def_p;
                $result2 /= 2 ;
                $result2 += rand($result2);

                &DEFTREAT($w_kind2, "PC") ;
                $result2 = int($result2 * $pnt) ;

                if ($result2 <= 0) {$result2 = 1 ;}
                $log = ($log . "<font color=\"red\"><b>$result2ダメージ $kega2</b></font>！<br>") ;

                $btai--;$hit -= $result2;

                if ($btai <= 0) { $bou = "下着<>DN"; $bdef=0; $btai="∞"; }

                if ($hit <=0) { #死亡？
                    &DEATH;
                } else {    #逃亡
                    $log = ($log . "$w_l_name は 逃げ切った・・・。<br>") ;
                }
                $w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec 戦闘：$f_name $l_name（$cl $sex$no番） 攻:$result2 被:$result $hakaiinf2 $kega3 </b></font><br>") ;
                $w_wep = $w_wep_2; $w_watt = $w_watt_2; $w_wtai = $w_wtai_2; $inf = $inf_2 ;
                $w_exp++;
            } else {
                $w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec 戦闘：$f_name $l_name（$cl $sex$no番） 被:$result $kega3 </b></font><br>") ;
                $log = ($log . "しかし、間一髪避けた！<br>") ;
            }

            if (($w_kind2 =~ /G|A/) && ($w_wtai > 0)) { #銃・射？
                $w_wtai--; if ($w_wtai <= 0) {$w_wtai = 0 ;}
            } elsif ($w_kind2 =~ /C|D/) {
                $w_wtai--; if ($w_wtai <= 0) { $w_wep ="素手<>WP"; $w_watt=0; $w_wtai="∞"; }
            } elsif (($w_kind2 =~ /N/) && (int(rand(5)) == 0)) {
                $w_watt -= int(rand(2)+1) ; if ($w_watt <= 0) { $w_wep ="素手<>WP"; $w_watt=0; $w_wtai="∞"; }
            }

        } else {
            $log = ($log . "$w_l_name は 反撃できない！<br>") ;
            $log = ($log . "$w_l_name は 逃げ切った・・・。<br>") ;
            $w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec 戦闘：$f_name $l_name（$cl $sex$no番） 被:$result $hakaiinf2 $kega3 </b></font><br>") ;
        }
    } else {    #逃亡
        $log = ($log . "$w_l_name は 逃げ切った・・・。<br>") ;
        $w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec 戦闘：$f_name $l_name（$cl $sex$no番） 被:$result $hakaiinf2 $kega3 </b></font><br>") ;
    }

    if (($w_kind =~ /G|A/) && ($wtai > 0)) {    #銃・射？
        $wtai--; if ($wtai <= 0) { $wtai = 0 ; }
    } elsif ($w_kind =~ /C|D/) {
        $wtai--; if ($wtai <= 0) { $wep ="素手<>WP"; $watt=0; $wtai="∞"; }
    } elsif (($w_kind =~ /N/) && (int(rand(5)) == 0)) {
        $watt -= int(rand(2)+1) ; if ($watt <= 0) { $wep ="素手<>WP"; $watt=0; $wtai="∞"; }
    }

    &LVUPCHK() ;


    &SAVE;
    &SAVE2;

}
#==================#
# ■ 後攻攻撃処理  #
#==================#
sub ATTACK2 {
    $kega2 = "" ; $kega3 = "" ;
    $hakaiinf2 = ""; $hakaiinf3 = "";

    if ($w_hit <= 0) {
        &ERROR("不正アクセスです") ;
    }

    local($result) = 0 ;
    local($result2) = 0 ;
    local($i) = 0 ;
    local($dice1) = int(rand(100)) ;
    local($dice2) = int(rand(100)) ;
    ($w_name,$w_kind) = split(/<>/, $wep);
    ($w_name2,$w_kind2) = split(/<>/, $w_wep);

    &TACTGET; &TACTGET2;    #基本行動

    #プレイヤー
    if (($wep =~ /G|A/) && ($wtai == 0)) {
        $att_p = (($watt/10) + $att) * $atp ;
    } else {
        $att_p = ($watt + $att) * $atp ;
    }
    local($ball) = $def + $bdef + $bdef_h + $bdef_a + $bdef_f ;
    if ($item[5] =~ /AD/) {$ball += $eff[5];} #装飾が防具？
    $def_p = $ball * $dfp ;

    #敵
    if (($w_wep =~ /G|A/) && ($w_wtai == 0)) {
        $att_n = (($w_watt/10) + $w_att) * $atn ;
    } else {
        $att_n = ($w_watt + $w_att) * $atn ;
    }
    local($ball2) = $w_def + $w_bdef + $w_bdef_h + $w_bdef_a + $w_bdef_f ;
    if ($w_item[5] =~ /AD/) {$ball += $w_eff[5];} #装飾が防具？
    $def_n = $ball2 * $dfn ;

    &BLOG_CK;
    &EN_KAIFUKU;

    $Command="BATTLE";

    $log = ($log . "$w_f_name $w_l_name（$w_cl $w_sex$w_no番）が突如襲い掛かってきた！<br>") ;

    &WEPTREAT($w_name2, $w_kind2,  $w_wtai, $w_l_name, $l_name, "攻撃", "NPC") ;
    if ($dice2 < $mei2) {    #攻撃成功

        $result = ($att_n*$wk) - $def_p;
        $result /= 2 ;
        $result += rand($result);
        $result = int($result) ;

        &DEFTREAT($w_kind2, "PC") ;
        $result = int($result * $pnt) ;

        if ($result <= 0) {$result = 1 ;}
        $log = ($log . "<font color=\"red\"><b>$resultダメージ $kega2</b></font>！<br>") ;

        $hit -= $result;
        $btai--;

        if ($btai <= 0) { $bou = "下着<>DN"; $bdef=0; $btai="∞"; }
        $w_wep = $w_wep_2; $w_watt = $w_watt_2; $w_wtai = $w_wtai_2; $inf = $inf_2 ;
        ($w_name2,$w_kind2) = split(/<>/, $w_wep);
        $w_exp++;
    } else {
        $log = ($log . "しかし、間一髪避けた！<br>") ;
    }

    if ($hit <= 0) {    #死亡？
        &DEATH;
    } elsif (rand(10) <5) { #反撃

        if ($weps eq $weps2) {

            &WEPTREAT($w_name, $w_kind,  $wtai, $l_name, $w_l_name, "反撃", "PC") ;
            if ($dice1 < $mei) {    #攻撃成功

                $result2 = ($att_p*$wk) - $def_n;
                $result2 /= 2 ;
                $result2 += rand($result2);
                $result2 = int($result2) ;

                &DEFTREAT($w_kind, "NPC") ;
                $result2 = int($result2 * $pnt) ;

                if ($result2 <= 0) {$result2 = 1 ;}
                $log = ($log . "<font color=\"red\"><b>$result2ダメージ $hakaiinf3 $kega3</b></font>！<br>") ;

                $w_hit -= $result2;
                $w_btai--;

                if ($w_btai <= 0) { $w_bou = "下着<>DN"; $w_bdef=0; $w_btai="∞"; }

                if ($w_hit <=0) {   #死亡？
                    &DEATH2;
                } else {    #逃亡
                    $log = ($log . "$l_name は 逃げ切った・・・。<br>") ;
                }
                $w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec 戦闘：$f_name $l_name（$cl $sex$no番） 攻:$result 被:$result2 $hakaiinf2 $kega3 </b></font><br>") ;
                $wep = $wep_2; $watt = $watt_2; $wtai = $wtai_2; $w_inf = $w_inf_2 ;
                ($w_name,$w_kind) = split(/<>/, $wep);
                $exp++;
            } else {
                $w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec 戦闘：$f_name $l_name（$cl $sex$no番） 攻:$result $hakaiinf2 </b></font><br>") ;
                $log = ($log . "しかし、避けられた！<br>") ;
            }

            if (($w_kind =~ /G|A/) && ($wtai > 0)) {    #銃・射？
                $wtai--; if ($wtai <= 0) { $wtai = 0 ; }
            } elsif ($w_kind =~ /C|D/) {
                $wtai--; if ($wtai <= 0) { $wep ="素手<>WP"; $watt=0; $wtai="∞"; }
            } elsif (($w_kind =~ /N/) && (int(rand(5)) == 0)) {
                $watt -= int(rand(2)+1) ; if ($watt <= 0) { $wep ="素手<>WP"; $watt=0; $wtai="∞"; }
            }
        } else {
            $log = ($log . "$l_name は 反撃できない！<br>") ;
            $log = ($log . "$l_name は 逃げ切った・・・。<br>") ;
            $w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec 戦闘：$f_name $l_name（$cl $sex$no番） 攻:$result $hakaiinf2 $kega3 </b></font><br>") ;
        }
    } else {    #逃亡
        $log = ($log . "$l_name は 逃げ切った・・・。<br>") ;
        $w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec 戦闘：$f_name $l_name（$cl $sex$no番） 攻:$result $hakaiinf2 $kega3 </b></font><br>") ;
    }

    if (($w_kind2 =~ /G|A/) && ($w_wtai > 0)) { #銃・射？
        $w_wtai--; if ($w_wtai <= 0) {$w_wtai = 0 ;}
    } elsif ($w_kind2 =~ /C|D/) {
        $w_wtai--; if ($w_wtai <= 0) { $w_wep ="素手<>WP"; $w_watt=0; $w_wtai="∞"; }
    } elsif (($w_kind2 =~ /N/) && (int(rand(5)) == 0)) {
        $w_watt -= int(rand(2)+1) ; if ($w_watt <= 0) { $w_wep ="素手<>WP"; $w_watt=0; $w_wtai="∞"; }
    }

    &LVUPCHK();


    &SAVE;
    &SAVE2;
}
#==================#
# ■ 武器種別処理  #
#==================#
sub WEPTREAT {

    local($wname)   = @_[0] ;   #武器
    local($wkind)   = @_[1] ;   #武器
    local($wwtai)   = @_[2] ;   #残数
    local($pn)      = @_[3] ;   #攻撃者名
    local($nn)      = @_[4] ;   #防御者名
    local($ind)     = @_[5] ;   #攻撃種別（攻撃/反撃)
    local($attman)  = @_[6] ;   #攻撃者（PC/NPC)

    local($dice3) = int(rand(100)) ;
    local($dice4) = int(rand(4)) ;
    local($dice5) = int(rand(100)) ;

    local($kega)    = 0 ;
    local($kegainf) = "" ;
    local($k_work) = "" ;
    local($hakai) =  0 ;

    if ((($wkind =~ /B/) || (($wkind =~ /G|A/) && ($wwtai == 0))) && ($wname ne "素手")) { #棍棒 or 弾無し銃 or 矢無し弓
        $log = ($log . "$pnの$ind！$wname で $nnに殴りかかった！") ;
        if ($attman eq "PC") {$wb++;$wk=$wb;} else {$w_wb++;$wk=$w_wb;}
        $kega = 15 ;$kegainf = "頭腕" ; #怪我率、怪我個所
        $hakai = 3 ;    #破壊率
    } elsif ($wkind =~ /A/) {   #弓系？
        $log = ($log . "$pnの$ind！$wname を $nn目掛けて射た！") ;
        if ($attman eq "PC") {$wa++;$wk=$wa;} else {$w_wa++;$wk=$w_wa;}
        $kega = 20 ; $kegainf = "頭腕腹足" ;    #怪我率、怪我個所
        $hakai = 3 ;    #破壊率
    } elsif ($wkind =~ /C/) { #投系
        $log = ($log . "$pnの$ind！$wname を $nnに投げつけた！") ;
        if ($attman eq "PC") {$wc++;$wk=$wc;} else {$w_wc++;$wk=$w_wc;}
        $kega = 15 ;$kegainf = "頭腕" ; #怪我率、怪我個所
        $hakai = 0 ;    #破壊率
    } elsif ($wkind =~ /D/) { #爆系
        $log = ($log . "$pnの$ind！$wname を $nnに投げつけた！") ;
        if ($attman eq "PC") {$wd++;$wk=$wd;} else {$w_wd++;$wk=$w_wd;}
        $kega = 15 ;$kegainf = "頭腕腕足" ; #怪我率、怪我個所
        $hakai = 0 ;    #破壊率
    } elsif ($wkind =~ /G/) { #銃系
        $log = ($log . "$pnの$ind！$wname を $nn目掛けて発砲した！") ;
        if ($attman eq "PC") {$wg++;$wk=$wg;$ps=$pls;} else {$w_wg++;$wk=$w_wg;$ps=$w_pls;}
        $kega = 25 ; $kegainf = "頭腕腹足" ;    #怪我率、怪我個所
        $hakai = 3 ;    #破壊率
        open(DB,"$gun_log_file");seek(DB,0,0); @gunlog=<DB>;close(DB);
        $gunlog[0] = "$now,$place[$ps],$id,$w_id,\n";
        open(DB,">$gun_log_file"); seek(DB,0,0); print DB @gunlog; close(DB);
    } elsif ($wkind =~ /S/) { #刺系
        $log = ($log . "$pnの$ind！$wname で $nnを刺した！") ;
        if ($attman eq "PC") {$ws++;$wk=$ws;} else {$w_ws++;$wk=$w_ws;}
        $kega = 25 ; $kegainf = "頭腕腹足" ;    #怪我率、怪我個所
        $hakai = 3 ;    #破壊率
    } elsif ($wkind =~ /N/) { #斬系
        $log = ($log . "$pnの$ind！$wname で $nnに斬りつけた！") ;
        if ($attman eq "PC") {$wn++;$wk=$wn;} else {$w_wn++;$wk=$w_wn;}
        $kega = 25 ; $kegainf = "頭腕腹足" ;    #怪我率、怪我個所
        $hakai = 3 ;    #破壊率
    } elsif ($wkind =~ /P/) { #殴系
        $log = ($log . "$pnの$ind！$wname で $nnを殴った！") ;
        if ($attman eq "PC") {$wp++;$wk=$wp;} else {$w_wp++;$wk=$w_wp;}
        $kega = 0 ; $kegainf = "" ; #怪我率、怪我個所
        $hakai = 0 ;    #破壊率
    } else { #その他
        $log = ($log . "$pnの$ind！$wname で $nnを殴った！") ;
        if ($attman eq "PC") {$wp++;$wk=$wp;} else {$w_wp++;$wk=$w_wp;}
        $kega = 0 ; $kegainf = "" ; #怪我率、怪我個所
        $hakai = 0 ;    #破壊率
    }

    $wk = int($wk/$BASE) ;
    if ($wk == 0) { $wk = 0.9 ;
    }elsif ($wk == 1) { $wk = 0.95 ;
    }elsif ($wk == 2) { $wk = 1.0 ;
    }elsif ($wk == 3) { $wk = 1.05 ;
    }elsif ($wk == 4) { $wk = 1.1 ;
    } else {$wk = 1.15 ;}

    if ($attman eq "PC") {  #PC
        $wep_2 = $wep; $watt_2 = $watt; $wtai_2 = $wtai ;$w_inf_2 = $w_inf ;
    } else {
        $w_wep_2 = $w_wep; $w_watt_2 = $w_watt; $w_wtai_2 = $w_wtai ;$inf_2 = $inf ;
    }

    # 武器破壊
    if ($dice5 < $hakai) {  #破壊？
        if ($attman eq "PC") {  #PC
            $wep_2 = "素手<>WP"; $watt_2 = 0 ; $wtai_2 = "∞" ;
            $hakaiinf3 = "武器損傷！" ;
        } else {
            $w_wep_2 = "素手<>WP"; $w_watt_2 = 0 ; $w_wtai_2 = "∞" ;
            $hakaiinf2 = "武器損傷！" ;
        }
    } else {
        $hakaiinf2 = "" ;
        $hakaiinf3 = "" ;
    }

    # 怪我処理
    if ($dice3 < $kega) {
        if (($dice4 == 0) && ($kegainf =~ /頭/)) {  #頭
            $k_work =  "頭" ;
        } elsif (($dice4 == 1) && ($kegainf =~ /腕/)) { #腕
            $k_work =  "腕" ;
        } elsif (($dice4 == 2) && ($kegainf =~ /腹/)) { #腹
            $k_work =  "腹" ;
        } elsif (($dice4 == 3) && ($kegainf =~ /足/)) { #足
            $k_work =  "足" ;
        } else {
            return ;
        }

        if ($attman eq "PC") {  #PC
            if ((($w_item[5] =~ /AD/)||($w_bou =~ /<>DB/)) && ($k_work eq "腹")) {    #腹？
                if($w_item[5] =~ /AD/){
                    $w_itai[5] --; if ($w_itai[5] <= 0) {$w_item[5]="なし"; $w_eff[5]=$w_itai[5]=0;}
                }else{
                    $w_btai --; if ($w_btai <= 0) { $w_bou = "下着<>DN"; $w_bdef=0; $w_btai="∞"; }
                }
                return ;
            } elsif (($w_bou_h =~ /<>DH/) && ($k_work eq "頭")) {   #頭？
                $w_btai_h --; if ($w_btai_h <= 0) {$w_bou_h="なし"; $w_bdef_h=$w_btai_h=0;}
                return ;
            } elsif (($w_bou_f =~ /<>DF/) && ($k_work eq "足")) {   #足？
                $w_btai_f --; if ($w_btai_f <= 0) {$w_bou_f="なし"; $w_bdef_f=$w_btai_f=0;}
                return ;
            } elsif (($w_bou_a =~ /<>DA/) && ($k_work eq "腕")) {   #腕？
                $w_btai_a --; if ($w_btai_a <= 0) {$w_bou_a="なし"; $w_bdef_a=$w_btai_a=0;}
                return ;
            } else {
                $kega3 = ($k_work . "部負傷");
                $w_inf_2 =~ s/$k_work//g ;
                $w_inf_2 = ($w_inf_2 . $k_work) ;
            }
        } else {
            if ((($item[5] =~ /AD/)||($bou =~ /<>DB/)) && ($k_work eq "腹")) {    #腹？
                if($item[5] =~ /AD/){
                    $itai[5] --; if ($itai[5] <= 0) {$item[5]="なし"; $eff[5]=$itai[5]=0;}
                }else{
                    $btai --; if ($btai <= 0) { $bou = "下着<>DN"; $bdef=0; $btai="∞"; }
                }
                return ;
            } elsif (($bou_h =~ /<>DH/) && ($k_work eq "頭")) { #頭？
                $btai_h --; if ($btai_h <= 0) {$bou_h="なし"; $bdef_h=$btai_h=0;}
                return ;
            } elsif (($bou_f =~ /<>DF/) && ($k_work eq "足")) { #足？
                $btai_f --; if ($btai_f <= 0) {$bou_f="なし"; $bdef_f=$btai_f=0;}
                return ;
            } elsif (($bou_a =~ /<>DA/) && ($k_work eq "腕")) { #腕？
                $btai_a --; if ($btai_a <= 0) {$bou_a="なし"; $bdef_a=$btai_a=0;}
                return ;
            } else {
                $kega2 = ($k_work . "部負傷");
                $inf_2 =~ s/$k_work//g ;
                $inf_2 = ($inf_2 . $k_work) ;
            }
        }
    }


}
#==================#
# ■ 自分死亡処理  #
#==================#
sub DEATH {

    $hit = 0;$w_kill++;
    $mem--;

    $com = int(rand(6)) ;

    $log = ($log . "<font color=\"red\"><b>$f_name $l_name（$cl $sex$no番）は死亡した。</b></font><br>") ;
    if ($w_msg ne "") {
        $log = ($log . "<font color=\"lime\"><b>$w_f_name $w_l_name『$w_msg』</b></font><br>") ;
    }
    $w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec $f_name $l_name（$cl $sex$no番）と戦闘を行い、殺害した。【残り$mem人】</b></font><br>") ;

    local($b_limit) = ($battle_limit * 3) + 1;

    if (($mem == 1) && ($w_sts ne "NPC0") && ($ar > $b_limit)){$w_inf = ($w_inf . "勝") ;}

    open(DB,"$gun_log_file");seek(DB,0,0); @gunlog=<DB>;close(DB);
    $gunlog[1] = "$now,$place[$pls],$id,$w_id,\n";
    open(DB,">$gun_log_file"); seek(DB,0,0); print DB @gunlog; close(DB);

    #死亡ログ
    &LOGSAVE("DEATH2") ;
    $death = $deth ;
}
#================#
# ■ 敵死亡処理  #
#================#
sub DEATH2 {

    $w_hit = 0;$kill++;
    $wf = $w_id; #ブラウザバック対処
    if (($w_cl ne "$BOSS")&&($w_cl ne "$ZAKO")){ $mem--; }

    $w_com = int(rand(6)) ;
    $log = ($log . "<font color=\"red\"><b>$w_f_name $w_l_name（$w_cl $w_sex$w_no番）を殺害した。【残り$mem人】</b></font><br>") ;

    if (length($w_dmes) > 1) {
        $log = ($log . "<font color=\"yellow\"><b>$w_f_name $w_l_name『$w_dmes』</b></font><br>") ;
    }
    if (length($msg) > 1) {
        $log = ($log . "<font color=\"lime\"><b>$f_name $l_name『$msg』</b></font><br>") ;
    }

    local($b_limit) = ($battle_limit * 3) + 1;
    if (($mem == 1)&& ($ar > $b_limit)) {$inf = ($inf . "勝") ;}

    open(DB,"$gun_log_file");seek(DB,0,0); @gunlog=<DB>;close(DB);
    $gunlog[1] = "$now,$place[$pls],$id,$w_id,\n";
    open(DB,">$gun_log_file"); seek(DB,0,0); print DB @gunlog; close(DB);

    #死亡ログ
    &LOGSAVE("DEATH3") ;

    $Command = "BATTLE2" ;
    $w_death = $deth ;
    $w_bid = "";

}
#================#
# ■ 戦闘結果処理  #
#================#
sub BATTLE {

    $cln = "$w_cl（$w_sex$w_no番）" ;

print <<"_HERE_";
<P align="center"><B><FONT color="#ff0000" size="+3" face="ＭＳ 明朝">$place[$pls]（$area[$pls]）</FONT></B><BR>
</P>
<TABLE width="568">
<TR><TD><B><FONT color="#ff0000">
@links
</FONT></B></TD></TR>
</TABLE>

<TABLE width="568">
  <TBODY>
    <TR>
      <TD valign="top" width="279" height="311">
      <TABLE border="1" width="389" cellspacing="0" height="300">
        <TBODY>
          <TR align="center">
            <TD valign="top"><BR>
            <B><FONT color="#ff0000" size="5" face="ＭＳ 明朝">戦闘発生</FONT></B><BR>
            <BR>
            <TABLE border="0">
              <TBODY>
_HERE_

if($icon_mode){
    print "<TR align=\"center\">\n";
    print "<TD><IMG src=\"$imgurl$icon_file[$icon]\" width=\"70\" height=\"70\" border=\"0\" align=\"middle\"></TD>\n";
    print "<TD></TD>\n";
    print "<TD><IMG src=\"$imgurl$icon_file[$w_icon]\" width=\"70\" height=\"70\" border=\"0\" align=\"middle\"></TD>\n";
    print "</TR>\n";
}

print <<"_HERE_";
                <TR align="center">
                  <TD>$cl（$sex$no番）</TD>
                  <TD width="50" align="center">ＶＳ</TD>
                  <TD>$cln</TD>
                </TR>
                <TR align="center">
                  <TD>$f_name $l_name</TD>
                  <TD></TD>
                  <TD>$w_f_name $w_l_name</TD>
                </TR>
              </TBODY>
            </TABLE>
            <BR><BR><BR><BR>
            <BR>
            </TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
      <TD valign="top" width="200" height="311">
      <TABLE border="1" cellspacing="0">
        <TBODY>
          <TR><TD align="center" width="250"><B>コマンド</B></TD>
          <TR>
            <TD align="left" valign="top" width="190" height="280">
            <FORM METHOD="POST">
            <INPUT TYPE="HIDDEN" NAME="mode" VALUE="command">
            <INPUT TYPE="HIDDEN" NAME="Id" VALUE="$id2">
            <INPUT TYPE="HIDDEN" NAME="Password" VALUE="$password2">
_HERE_

            &COMMAND;

print <<"_HERE_";
            </FORM>
            </TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
    </TR>
    <TR>
      <TD colspan="2" valign="top" height="101">
      <TABLE border="1" cellspacing="0" height="150" cellpadding="0">
        <TBODY>
          <TR>
            <TD height="20" valign="top" width="600">$log</TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
    </TR>
  </TBODY>
</TABLE>
<BR>
_HERE_

$mflg="ON"; #ステータス非表示
}
#==================#
# ■ 逃亡処理  #
#==================#
sub RUNAWAY {

    $log = ($log . "$l_name は 全速力で逃げ出した・・・。<BR>") ;

    $Command = "MAIN";

}

#==================#
# ■ 防具種別処理  #
#==================#
sub DEFTREAT {

    local($wkind)   = @_[0] ;   #武器種別
    local($defman)   = @_[1] ;  #防御側(PC/NPC)

    local($p_up) = 1.5 ;
    local($p_down) = 0.5 ;

    if ($defman eq "PC") {  #PC?
        local($b_name,$b_kind) = split(/<>/, $bou);
        local($b_name_h,$b_kind_h) = split(/<>/, $bou_h);
        local($b_name_f,$b_kind_f) = split(/<>/, $bou_f);
        local($b_name_a,$b_kind_a) = split(/<>/, $bou_a);
        local($b_name_i,$b_kind_i) = split(/<>/, $item[5]);
    } else {
        local($b_name,$b_kind) = split(/<>/, $w_bou);
        local($b_name_h,$b_kind_h) = split(/<>/, $w_bou_h);
        local($b_name_f,$b_kind_f) = split(/<>/, $w_bou_f);
        local($b_name_a,$b_kind_a) = split(/<>/, $w_bou_a);
        local($b_name_i,$b_kind_i) = split(/<>/, $w_item[5]);
    }

    if (($wkind eq "WG") && ($b_kind_i eq "ADB")) { #銃→防弾
        $pnt = $p_down ;
    } elsif (($wkind eq "WG") && ($b_kind_h eq "DH")) { #銃→頭
        $pnt = $p_up ;
    } elsif (($wkind eq "WN") && ($b_kind eq "DBK")) { #斬→鎖
        $pnt = $p_down ;
    } elsif (($wkind eq "WN") && ($b_kind_i eq "ADB")) { #斬→防弾
        $pnt = $p_up ;
    } elsif ((($wkind eq "WB")||($wkind eq "WGB")||($wkind eq "WAB")) && ($b_kind_h eq "DH")) { #殴→頭
        $pnt = $p_down ;
    } elsif ((($wkind eq "WB")||($wkind eq "WGB")||($wkind eq "WAB")) && ($b_kind =~ /DBA/)) { #殴→鎧
        $pnt = $p_up ;
    } elsif (($wkind eq "WS") && ($b_kind =~ /DBA/)) { #刺→鎧
        $pnt = $p_down ;
    } elsif (($wkind eq "WS") && ($b_kind =~ /DBK/)) { #刺→鎖
        $pnt = $p_up ;
    } else {
        $pnt = 1.0 ;
    }

}
#======================#
# ■ レベルアップ処理  #
#======================#
sub LVUPCHK {

    if (($exp >= int($level*$baseexp+(($level-1)*$baseexp)))&&($hit > 0)) { #レベルアップ
        $log = ($log . "レベルが上がった。<br>") ;
        $mhit += int(rand(3)+7) ; $att += int(rand(3)+2); $def += int(rand(3)+2); $level++;
    }
    if (($w_exp >= int($w_level*$baseexp+(($w_level-1)*$baseexp)))&&($w_hit > 0)) { #レベルアップ
        $w_log = ($w_log . "レベルが上がった。<br>") ;
        $w_mhit += int(rand(3)+7) ; $w_att += int(rand(3)+2); $w_def += int(rand(3)+2); $w_level++;
    }

}

#======================#
# ■ 敵回復処理        #
#======================#
sub EN_KAIFUKU{ #敵回復処理
    $up = int(($now - $w_endtime) / (1 * $kaifuku_time));
    if ($w_inf =~ /腹/) { $up = int($up / 2); }
    if ($w_sts eq "睡眠") {
        $w_sta += $up;
        if ($w_sta > $maxsta) { $w_sta = $maxsta; }
        $w_endtime = $now;
    } elsif ($w_sts eq "治療") {
        if($kaifuku_rate == 0){$kaifuku_rate = 1;}
        $up = int($up / $kaifuku_rate);
        $w_hit += $up;
        if ($w_hit > $w_mhit) { $w_hit = $w_mhit; }
        $w_endtime = $now;
    }
}

#===========================#
# ■ 敵戦闘ログ自動削除処理 #
#===========================#
sub BLOG_CK{
    $log_len = length($w_log);
    if($log_len > 2000) {
        $w_log = "<font color=\"yellow\"><b>$hour:$min:$sec 戦闘ログは自動削除されました。</b></font><br>";
    }
}

1;
