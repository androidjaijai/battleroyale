#! /usr/local/bin/perl
require "jcode.pl";
require "br.cgi";
require "$LIB_DIR/lib.cgi";
require "$LIB_DIR/lib2.cgi";

&LOCK ;

require "pref.cgi";

&DECODE;
    # ¾�����Ȥ���Υ����������ӽ�
    if ($base_url) {
        local($url_ok) = 0;
        foreach $kyoka_url(@base_list){
            $ref_url = $ENV{'HTTP_REFERER'};
            $ref_url =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
            if ($ref_url =~ /$kyoka_url/i) { $url_ok = 1; }
        }
        if(!$url_ok){ &ERROR("�����ʥ��������Ǥ���");}
    }
    # GET �᥽�åɤ����
    if ($Met_Post && !$p_flag) {
        &ERROR("�����ʥ��������Ǥ���");
    }
&CREAD ;
&IDCHK;

if ($mode eq "main") { &MAIN; }
elsif ($mode eq "command") { &COM; }
else { &ERROR("�����ʥ��������Ǥ���") ; }
&UNLOCK;
exit;

#==================#
# �� �ᥤ�����    #
#==================#
sub MAIN {

    #����ɽ���ʥ�������������

    &HEADER;
    &STS();
    &FOOTER;

}
#==================#
# �� ���ޥ�ɽ���  #
#==================#
sub COM {

    if($Command =~ /MV/) {          #��ư��
        &MOVE;
    }elsif($Command eq "SEARCH") {  #õ��
        &SEARCH;
    }elsif($Command =~ /ITEM_/) {   #�����ƥ����
        require "$LIB_DIR/item.cgi";
        &ITEM;
    }elsif($Command =~ /DEL_/) {    #�����ƥ����
        require "$LIB_DIR/item.cgi";
        &ITEMDEL;
    }elsif(($Command =~ /SEIRI_/)&&($Command2 =~ /SEIRI2_/)) { #�����ƥ�����
        require "$LIB_DIR/itemsei.cgi";
        &ITEMSEIRI;
    }elsif(($Command =~ /GOUSEI_/)&&($Command2 =~ /GOUSEI2_/)) { #�����ƥ����
        require "$LIB_DIR/itemgou.cgi";
        &ITEMGOUSEI;
    }elsif($Command eq "HEAL") {    #����
        &HEAL;
    }elsif($Command eq "INN") {     #��̲
        &INN;
    }elsif($Command =~ /POI_/) {    #��ʪ����
        require "$LIB_DIR/poison.cgi";
        &POISON;
    }elsif($Command =~ /PSC_/) {    #�Ǹ�
        require "$LIB_DIR/poison.cgi";
        &PSCHECK;
    }elsif($Command =~ /GET_/) {    #������
        &WINGET;
    }elsif($Command =~ /OUK_/) {    #���޽���
        &OUKYU;
    }elsif(($msg2 ne "")||($dmes2 ne "")||($com2 ne "")) {          #�����ѹ�
        &WINCHG;
    }elsif($Command eq "WEPDEL") {  #��ﳰ��
        require "$LIB_DIR/item.cgi";
        &WEPDEL;
    }elsif($Command eq "WEPDEL2") { #���ΤƤ�
        require "$LIB_DIR/item.cgi";
        &WEPDEL2;
    }elsif($Command eq "WEPPNT") {  #�����ٳ�ǧ
        &WEPPNT;
    }elsif($Command eq "DEFCHK") {  #������ǧ
        &DEFCHK;
    }elsif($Command eq "SPEAKER") { #���ӥ��ԡ�������
        require "$LIB_DIR/speaker.cgi";
        &SPEAKER;
    }elsif($Command eq "HACK") {   #�ϥå���
        require "$LIB_DIR/hack.cgi";
        &HACKING;
    }elsif($Command =~ /ATK/) {     #����
        require "attack.cgi";
        &ATTACK1;
    }elsif($Command eq "RUNAWAY") { #ƨ˴
        require "attack.cgi";
        &RUNAWAY;
    }elsif($Command eq "BSAVE") {   #�Хå����å���¸
        require "admin.cgi";
        &BACKSAVE;
    }elsif($Command eq "BREAD") {   #�Хå����å��ɽ�
        require "admin.cgi";
        &BACKREAD;
    }elsif($Command eq "RESET") {   #�ǡ��������
        require "admin.cgi";
        &DATARESET;
    }

    if(($Command =~ /BATTLE/)||($Command =~ /ATK/)) {   #��Ʈ���
        &HEADER;
        require "attack.cgi";
        &BATTLE;
        &FOOTER;
    } elsif ($mflg ne "ON") {
        &MAIN;
    }
}
#==================#
# �� ���ޥ�ɽ���  #
#==================#
sub MOVE {

    local($mv) = $Command;
    $mv =~ s/MV//g ;

    ($ar[0],$ar[1],$ar[2],$ar[3],$ar[4],$ar[5],$ar[6],$ar[7],$ar[8],$ar[9],$ar[10],$ar[11],$ar[12],$ar[13],$ar[14],$ar[15],$ar[16],$ar[17],$ar[18],$ar[19],$ar[20],$ar[21]) = split(/,/, $arealist[2]);
    ($war,$a) = split(/,/, $arealist[1]);
    if(($ar[$war] eq $place[$mv])||($ar[$war+1] eq $place[$mv])||($ar[$war+2] eq $place[$mv])) {
        $log = ($log . "$place[$mv]�˰�ư���������ˤ����϶ػߥ��ꥢ�ˤʤäƤ��ޤ��ʡ�<br>$arinfo[$mv]<br>") ;
    } else {
        $log = ($log . "$place[$mv]�˰�ư������<BR>$arinfo[$mv]<br>") ;
        for ($i=0; $i<$war; $i++) {
            if (($ar[$i] eq $place[$mv]) && ($hackflg == 0)) {   #�ػߥ��ꥢ��
                $log = ("$place[$mv]�϶ػߥ��ꥢ������ư���뤳�ȤϽ���ʤ��ʡ�������<BR>") ;
                $Command = "MAIN";
                return ;
                $chkflg = 1 ;
            }
        }
    }


    $pls = $mv ;
    $Command = "MAIN";

    if ($inf =~ /­/) {
        $sta -= int(rand(5) + 13) ;
    } elsif ($club eq "Φ����") {
        $sta -= int(rand(5))+5 ;
    } else {
        $sta -= int(rand(5))+8 ;
    }

    if ($sta <= 0) {    #�����ߥ��ڤ졩
        &DRAIN("mov");
    }

    &SEARCH2;

    &SAVE;

}
#==================#
# �� õ������      #
#==================#
sub SEARCH {

    $log = ($log . "$l_name�ϡ��դ��õ��������������<br>") ;

    if ($inf =~ /­/) {
        $sta -= int(rand(5) + 23) ;
    } elsif ($club eq "Φ����") {
        $sta -= int(rand(5))+13;
    } else {
        $sta -= int(rand(5))+18 ;
    }

    if ($sta <= 0) {    #�����ߥ��ڤ졩
        &DRAIN("mov");
    }

    &SEARCH2;

    if ($chksts ne "OK") {
        $log = ($log . "�����������⸫�Ĥ���ʤ��ä���<BR>") ;
        $Command = "MAIN" ;
    }


    &SAVE;
}

#==================#
# �� õ������2     #
#==================#
sub SEARCH2 {

    local($i) = 0 ;
    srand(time ^ $i) ;

    srand($now);
    local($a) = int(rand(1)) ;  #Ũ�������ƥ�ɤ����ȯ��
    local($dice1) = int(rand(10)) ; #Ũ�������ƥ�ɤ����ȯ��

    &TACTGET ;

    open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);

    $chksts="NG";$chksts2="NG";

    if ($dice1 <= 5) {  #Ũȯ����
        for ($i=0; $i<$#userlist+1; $i++) {
            ($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf) = split(/,/, $userlist[$i]);
    push(@plist,$i) if (($w_pls eq $pls) && ($w_id ne $id) && ($w_bid ne $id));
        }

    for ($i=0;$i<@plist+5;$i++){
    push(@plist,splice(@plist,int(rand @plist+0),1));
    }

    foreach $i(@plist){
            local($dice2) = int(rand(10)) ; #Ũ�������ƥ�ȯ��
            local($dice3) = int(rand(10)) ; #��������

            ($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf) = split(/,/, $userlist[$i]);

            &TACTGET2 ;

            if (($w_pls eq $pls) && ($w_id ne $id) && ($w_bid ne $id)) {    #������¾�ץ쥤�䡼��
                local($chk) = int($dice2 * $sen);

                if ($chk < $chkpnt) {
                    if ($w_hit > 0) {
                        $wf = $w_id; #�֥饦���Хå��н���
                        if ($dice3 <= $chkpnt2) {   #��������
                            require "attack.cgi";
                            &ATTACK ;$chksts="OK";$chksts2="NG";last;
                        } else {    #��
                            $Index2 = $i;
                            $w_bid = $id ;
                            $bid = $w_id ;
                            require "attack.cgi";
                            &ATTACK2 ;$chksts="OK";$chksts2="NG";last;
                        }
                    } else {
                        local($chkflg) = 0 ;
                        local($dice4) = int(rand(10));
                        if ($dice4 > 8){
                            for ($j=0; $j<6; $j++) {
                                if ($w_item[$j] ne "�ʤ�" && $w_item[$j] ne "") {
                                    $chkflg=1;
                                    last;
                                }
                            }
#)))))))))))))))))))))))))))))
unless ($chkflg){if ($w_wep !~ /�Ǽ�/ || $w_bou !~ /����/ || $w_bou_h ne "�ʤ�" || $w_bou_f ne "�ʤ�" ||$w_bou_a ne "�ʤ�")
{$chkflg=1}}
#)))))))))))))))))))))))))))))
                        if ($chkflg == 1) { #����ȯ����
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
$userlist[$i] = "$w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,-1,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$id,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,\n" ;
open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                            $wf = $w_id; #�֥饦���Хå��н���
                            &DEATHGET ;last;
                        }
                    }}
                }else{ $chksts2="OK";}
            }
        }
        if ($chksts2 eq "OK") {
            $log = ($log . "���Ԥ�������Ǥ��뵤�ۤ����롦���������Τ�������<BR>") ;
        }
    } else {
        $dice2 = int(rand(10)) ;    #Ũ�������ƥ�ȯ��
        if (($dice2 < $chkpnt)&&($Command eq "SEARCH")) { #�����ƥ�ȯ��
            require "$LIB_DIR/item.cgi";
            &ITEMGET;
        } else {
            require "$LIB_DIR/event.cgi";
            &EVENT ;
        }
    }


}


#==================#
# �� ���Ž���      #
#==================#
sub HEAL {

    $sts = "����";
    $endtime = $now ;
    $Command = "HEAL2" ;

    &SAVE;
}

#==================#
# �� ��̲����      #
#==================#
sub INN {

    $sts = "��̲";
    $endtime = $now ;
    $Command = "INN2" ;
    &SAVE;

}
#==================#
# �� �����ʼ���    #
#==================#
sub WINGET {

    if ($item[$itno2] ne "�ʤ�" or $itno2>4 or $itno2<0) {
        $log = ($log . "����ʾ����ʤ��Ƥʤ���<br>") ;
        $Command = "MAIN";
        return;
    }
    if ($getid eq $id){
        $log = ($log . "��ʬ�Ǽ�ʬ�λ���ʪ��å�äƤߤ���<br>��������������<br>") ;
        $Command = "MAIN";
        return;
    }

    local($wk) = $Command;
    $wk =~ s/GET_//g;
    $wk+=0;
    $wk=int($wk);
    local($witem,$weff,$witai);

    open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);

    for ($i=0; $i<$#userlist+1; $i++) {
        ($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf) = split(/,/, $userlist[$i]);
        if ($w_id eq $getid) {
            &BB_CK; #�֥饦���Хå��н�
            if ($w_hit>0 || ($id eq $w_bid && $w_sta>-1)){
                $log = ($log . "$w_f_name�Τ��λ���ʪ���ߤ����ȶ���ǰ���Ƥߤ���<br>��������������<br>") ;
                $Command = "MAIN";
                return;
            }

            if ($wk==6) {
                ($witem,$weff,$witai) = ($w_wep,$w_watt,$w_wtai);
                $w_wep = "�Ǽ�<>WP"; $w_watt = 0; $w_wtai = "��";
            }elsif ($wk==7) {
                ($witem,$weff,$witai) = ($w_bou,$w_bdef,$w_btai);
                $w_bou = "����<>DN"; $w_bdef = 0; $w_btai = "��";
            }elsif ($wk==8) {
                ($witem,$weff,$witai) = ($w_bou_h,$w_bdef_h,$w_btai_h);
                $w_bou_h = "�ʤ�"; $w_bdef_h = $w_btai_h = 0;
            }elsif ($wk==9) {
                ($witem,$weff,$witai) = ($w_bou_f,$w_bdef_f,$w_btai_f);
                $w_bou_f = "�ʤ�"; $w_bdef_f = $w_btai_f = 0;
            }elsif ($wk==10) {
                ($witem,$weff,$witai) = ($w_bou_a,$w_bdef_a,$w_btai_a);
                $w_bou_a = "�ʤ�"; $w_bdef_a = $w_btai_a = 0;
            } else {
                ($witem,$weff,$witai) = ($w_item[$wk],$w_eff[$wk],$w_itai[$wk]);
                $w_item[$wk] = "�ʤ�"; $w_eff[$wk]=$w_itai[$wk] = 0;
            }
            $userlist[$i] = "$w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$id,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,\n" ;
            open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);
            last;
        }
    }

    if ($witem!~/^(�ʤ�|�Ǽ�|����)$/ && $i!=$#userlist+1){
        $item[$itno2] = $witem ;
        $eff[$itno2] = $weff; $itai[$itno2] = $witai ;
        ($witem)=split(/<>/,$witem,2);
        $log = ($log . "$l_name �� $witem�������줿��<BR>") ;
        &SAVE;
    }else{
        $log = ($log . "�����Τ����᤿��<BR>") ;
    }


    $Command = "MAIN";
}

#==================#
# �� �����ѹ�����  #
#==================#
sub WINCHG {

    $log = ($log . "���ʤ��ѹ����ޤ�����<br>") ;
    $msg = $msg2;
    $dmes = $dmes2 ;
    $com = $com2 ;

    &SAVE ;

    $Command = "MAIN" ;

}
#==================#
# �� ����ȯ������  #
#==================#
sub DEATHGET {

    $log = ($log . "$w_f_name $w_l_name�λ��Τ�ȯ��������<br>") ;

    if ($w_death =~ /�»�/) {
        if ($w_com == 0) {$log = ($log . "Ƭ������������ǤĤʤ��äƤ���֤��������������ͤ�줿�褦����<br>") ;}
        elsif ($w_com == 1) {$log = ($log . "ʢ���������ʿ�ʪ�Τ褦�ʤ�Τ�������ơ���¡���Ϥ߽Ф��Ƥ��롦������<br>") ;}
        elsif ($w_com == 2) {$log = ($log . "�������鶻�ˤ����Ƥη����ڤ�����������ڤ�������Ƥ롦������<br>") ;}
        elsif ($w_com == 3) {$log = ($log . "��ƹ��ξ�ӡ�ξ­��ʬ�Ǥ���Ƥ��롣�����������������οʹ֤˽����Τ�������������<br>") ;}
        elsif ($w_com == 4) {$log = ($log . "�����Ū���ڤ��ޤ�Ƥ��롣�������̱Ƥʤ�����̵����������<br>") ;}
        elsif ($w_com == 5) {$log = ($log . "ʢ�����ڤ�������Ƥ��뤬���褯����ȼ��ˤ��ڤ������¿�����롦������<BR>�����ڤ�줿��˼����򤷤褦�Ȼפä��Τ�������<br>") ;}
        else {$log = ($log . "Ƭ���鶻�ˤ�����̵�Ĥ��ڤ�������Ƥ��롦������<br>") ;}
    }elsif ($w_death =~ /�ͻ�/) {
        if ($w_com == 0) {$log = ($log . "�ۤ˰��ܤ����ͤ��ɤ��äƤ��롦������<br>") ;}
        elsif ($w_com == 1) {$log = ($log . "����˲��ܤ��𤬻ɤ��äƤ��롣ƨ���褦�Ȥ����ꡢ�ظ夫��ͤ�줿�褦����<br>") ;}
        elsif ($w_com == 2) {$log = ($log . "��¡�ξ��˰������Τ��𤬻ɤ��äƤ��롣�������Ӥλ����������������<br>") ;}
        elsif ($w_com == 3) {$log = ($log . "­��Ƭ����Ω�äƤ��롣­��ͤơ�ƨ����ʤ������Ƥ����Ƥ���޽��ͤ��褦����������<br>") ;}
        elsif ($w_com == 4) {$log = ($log . "�ɤ����˥���դ���줿�褦�ˤʤäƤ��롦�������르���ε֤ǽ跺���줿���ԤΤ褦��������������<br>") ;}
        elsif ($w_com == 5) {$log = ($log . "���ܤ���𤬤����ꡢ�ϥ�ͥ��ߤΤ褦�ˤʤäƤ��롦������<br>") ;}
        else {$log = ($log . "��˿��ܤ��𤬻ɤ��äƤ��롦���������ܤϳܤβ����ͤ�ȴ���Ƥ��롦������<br>") ;}
    }elsif ($w_death =~ /�ƻ�/) {
        if ($w_com == 0) {$log = ($log . "���ˡ�������ȯ���ۤˣ�ȯ���ƺ������롦�������ۤΰ�ȯ����̿���ˤʤä��ߤ�������������<br>") ;}
        elsif ($w_com == 1) {$log = ($log . "ʢ���˿�ȯ���ƺ������ꡢ�줬ή��Ф��Ƥ��롣�����������η��⤦�����Ƥ��롣<br>") ;}
        elsif ($w_com == 2) {$log = ($log . "Ƭ��������Ȥɤ�Ƥ��ʤ��̿᤭����Ǥ��롦������̾������ɤ�����̾����ʬ���ä����餤����<br>") ;}
        elsif ($w_com == 3) {$log = ($log . "���˿�ȯ�������ơ�Ǿ�񤬿᤭����Ǥ��롣�������塢���˽Ƥ��ͤù���Ƿ�ä���������դ��������Ȥ򤷤Ƥ��롦������<br>") ;}
        elsif ($w_com == 4) {$log = ($log . "ʢ���ˤݤä���꤬���ꡢ������¦�������롣���줸�����������Ƥ���ʤ��ʡ�������<br>") ;}
        elsif ($w_com == 5) {$log = ($log . "��˲�ȯ����ƺ������롦���������ߤǤ⤢�ä��ΤǤ�������<br>") ;}
        else {$log = ($log . "��Ƭ�����㤷��»������Ǿ��ή��Ф��Ƥ��롦��������<br>") ;}
    }elsif ($w_death =~ /�ʻ�/) {
        if ($w_com == 0) {$log = ($log . "�����Ǽ�������줿�Τ�����������������������̤��Ǥ���ʪ�򻵤����餷�Ƥ��롣<br>") ;}
        elsif ($w_com == 1) {$log = ($log . "�ʻ��Τ����������ᤷ�����ˤ�����˻���������Ƥ��롣<br>") ;}
        elsif ($w_com == 2) {$log = ($log . "�����Ǽ��ʤ��줿�ΤǤ����������Ф������ܤ������̵�ĤʻѤ���������<br>") ;}
        elsif ($w_com == 3) {$log = ($log . "ï���˼��ʤỦ���줿�褦�������ؤ��Ƥ��롦������<br>") ;}
        elsif ($w_com == 4) {$log = ($log . "���������ʤ���㤷���񹳤�������������ޤˤ����Τ褦�ʤ�Τ���������Ǥ��롦����<br>") ;}
        elsif ($w_com == 5) {$log = ($log . "���ߤ���Τ������������줿�塢�ߤ뤵�줿�Ȥ����ͤ����ʤ��ʡ�������<br>") ;}
        else {$log = ($log . "��ڤˡ������������դ���줿�褦�ʻ翧���ܤ����롦������<br>") ;}
    }elsif ($w_death =~ /����/) {
        if ($w_com == 0) {$log = ($log . "�����餸�夦�ˡ��ΤΥѡ��Ĥ�ʬ�����Ƥ��롣�ɼ�ˤ��줿�ߤ�������������<br>") ;}
        elsif ($w_com == 1) {$log = ($log . "ξ­���᤭���Ф���Ƥ��롣�Ӥ�������ä�ƨ���褦�Ȥ����Τ���������<br>") ;}
        elsif ($w_com == 2) {$log = ($log . "���ƤˤǤ⹶�⤵�줿�ΤǤ�������Ƭ�ȱ��Ӥ����ĤäƤ��ʤ���������<br>") ;}
        elsif ($w_com == 3) {$log = ($log . "���Ƥ˿᤭���Ф��줿�ΤǤ�������Ƭ��Ⱦʬ�礱����Ȥ��Τ����Ƥ��롦������<br>") ;}
        elsif ($w_com == 4) {$log = ($log . "�����ǿ᤭���Ф��줿���Ӥ�������ۤ���ˤ����äƤ��롦������<br>") ;}
        elsif ($w_com == 5) {$log = ($log . "���ΤȤ�����ꡢ���β����ʡ�������<br>") ;}
        else {$log = ($log . "��ȼ꤬��������ʤ��ʡ������������ǿ᤭���Ф��줿���������������<br>") ;}
    }elsif ($w_death =~ /�л�/) {
        if ($w_com == 0) {$log = ($log . "ʢ���ޤ��������ǡ��������ޤäƤ��뤬�������ɤ���顢���Τޤ�©�䤨���褦����������<br>") ;}
        elsif ($w_com == 1) {$log = ($log . "�����ɼ�˲���줿�ߤ��������������餬��˼��夬�äƤ��롦������<br>") ;}
        elsif ($w_com == 2) {$log = ($log . "��ι����ޤ�졢�󤫤�����ͤ��ФƤ��롦������<br>") ;}
        elsif ($w_com == 3) {$log = ($log . "���̤˴����ᡢ���̤η����̤���ή���Ƥ��롦�����ݤ줿�ꡢ��Ƭ�����Ǥ��줿�褦����<br>") ;}
        elsif ($w_com == 4) {$log = ($log . "������ߴ�Τ褦�ʤ�Τǲ���줿�Τ�������Ƭ���������ޤ��ݤ�Ƥ��롦������<br>") ;}
        elsif ($w_com == 5) {$log = ($log . "�ۤ���졢���Ǿ�����ʤ���Ƥ��롣�����̤���㤷������줿�褦���ʡ�����<br>") ;}
        else {$log = ($log . "�󤬸����˲��˸����Ƥ��롣�ɤ��ߤƤ⡢��ι����ޤ�Ƥ���ʡ�������<br>") ;}
    }elsif ($w_death =~ /�ɻ�/) {
        if ($w_com == 0) {$log = ($log . "���Ȥˡ����������ʿ�ʪ�ǻɤ��줿���������̤ˤ��롦���������Τβ��ϡ���γ�����������<br>") ;}
        elsif ($w_com == 1) {$log = ($log . "�Ͼ��ˤʤ��ơ����٤ⲿ�٤�ɤ��줿�褦�ʺ��פ����롦������<br>") ;}
        elsif ($w_com == 2) {$log = ($log . "��¡����ͤ���̤���˽�����줬ͯ���ФƤ��롦�����������줿�ΤϤĤ������Τ褦����<br>") ;}
        elsif ($w_com == 3) {$log = ($log . "����ɤ���Ƥ��롦�����ܤ����ܤ�त�Ƥ��롦������<br>") ;}
        elsif ($w_com == 4) {$log = ($log . "�����ʢ����ɤ�����ݤ�Ƥ��롣�԰��Ǥ����ä��Τ�����������<br>") ;}
        elsif ($w_com == 5) {$log = ($log . "��ʢ�����㤷��»�����Ƥ��롣�ɤ����塢�����ä��褦�ʽ������롦������<br>") ;}
        else {$log = ($log . "ξ�ܤ����ʤˤ��ǻɤ���Ƥ��롦����������ޤ�ή���Ƥ���褦����������<br>") ;}
    }elsif ($w_death =~ /��/) {
        if ($w_com == 0) {$log = ($log . "��ʪ����ˤ����Τ��ʡ��������Ǥ������פ⤢�롦������<br>\n") ;}
        elsif ($w_com == 1) {$log = ($log . "�������ڤη줬ή��Ƥ��롣�ѤäȤߤϡ�̲�äƤ���褦�ˤ����ߤ��ʤ��ʡ�������<br>\n") ;}
        elsif ($w_com == 2) {$log = ($log . "���Τ˴���Ť������ͭ�Υ������ɽ������롣�ǻ����줿�Τ���������<br>\n") ;}
        elsif ($w_com == 3) {$log = ($log . "�ǻ����줿�Τ������������̤η�κ����ä�ˢ��ᤤ�Ƥ��롦������<br>\n") ;}
        elsif ($w_com == 4) {$log = ($log . "�Ǥ����Ƕ줷����������������ʬ�Ƿ㤷���ޤǤ����ष�äƤ��롦������<br>\n") ;}
        elsif ($w_com == 5) {$log = ($log . "���Ԥ��������Ǥ⤫����줿�Τ������椬�㤷���ѿ����Ƥ��롦������<br>\n") ;}
        else {$log = ($log . "���椬�ɤ����������ѿ����ơ�����������̤η���Ǥ��Ƥ��롦������<br>\n") ;}
    } else {
        $log = ($log . "̵�Ĥˤ�ĸ�����ž���äƤ��롦������<br>") ;
    }
    $log = ($log . "�ǥ��ѥå�����Ȥ�ʪ�������Ƥ�餦����������<br>") ;
    $Command = "DEATHGET";

    $chksts="OK";

}
#==================#
# �� �����ٳ�ǧ����#
#==================#
sub WEPPNT {

    $log = ("���ߤν�����٥�ϡ�����<br>") ;

    local($p_wa) = int($wa/$BASE);
    local($p_wb) = int($wb/$BASE);
    local($p_wc) = int($wc/$BASE);
    local($p_wd) = int($wd/$BASE);
    local($p_wg) = int($wg/$BASE);
    local($p_ws) = int($ws/$BASE);
    local($p_wn) = int($wn/$BASE);
    local($p_wp) = int($wp/$BASE);

    $log = ($log . "<BR>��°����֡�$club<br><br>") ;
    $log = ($log . "���͡�$p_wa($wa)������$p_wb($wb)���ꡧ$p_wc($wc)������$p_wd($wd)<br>") ;
    $log = ($log . "���ơ�$p_wg($wg)���ɡ�$p_ws($ws)���¡�$p_wn($wn)������$p_wp($wp)<br>") ;

}
#==================#
# �� ������ǧ����  #
#==================#
sub DEFCHK {

    local($w_name,$w_kind) = split(/<>/, $wep);
    local($b_name,$b_kind) = split(/<>/, $bou);
    local($b_name_h,$b_kind_h) = split(/<>/, $bou_h);
    local($b_name_f,$b_kind_f) = split(/<>/, $bou_f);
    local($b_name_a,$b_kind_a) = split(/<>/, $bou_a);
    local($b_name_i,$b_kind_i) = split(/<>/, $item[5]);

    $log = ("�����������Ƥ����ɶ�ϡ�����<br><br>") ;

    $log = ($log . "���𡡡���$w_name/$watt/$wtai<br>") ;
    $log = ($log . "���Ρ�����$b_name/$bdef/$btai<br>") ;
    $log = ($log . "��Ƭ������$b_name_h/$bdef_h/$btai_h<br>") ;
    $log = ($log . "���ӡ�����$b_name_a/$bdef_a/$btai_a<br>") ;
    $log = ($log . "��­������$b_name_f/$bdef_f/$btai_f<br>") ;
    $log = ($log . "����������$b_name_i/$eff[5]/$itai[5]<br>") ;

}
#==================#
# �� ���޽��ֽ���  #
#==================#
sub OUKYU {

    local($wk) = $Command;
    $wk =~ s/OUK_//g;

    if ($wk == 0) { #Ƭ
        $inf =~ s/Ƭ//g ;
    }elsif ($wk == 1) { #��
        $inf =~ s/��//g ;
    }elsif ($wk == 2) { #ʢ��
        $inf =~ s/ʢ//g ;
    }elsif ($wk == 3) { #­
        $inf =~ s/­//g ;
    }

    $log = ($log . "���޽��֤򤷤���<BR>") ;

    $sta -= $okyu_sta ;

    if ($sta <= 0) {    #�����ߥ��ڤ졩
        &DRAIN("com");
    }

    &SAVE ;

    $Command = "MAIN" ;
}

#===========================#
# �� �֥饦���Хå������ɻ� #
#===========================#
sub BB_CK{

    if($wf eq $w_id){ $wf = ""; }else{ &ERROR("�������������Ǥ�") ; }

}

1