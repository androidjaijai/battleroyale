#==================#
# �� �ǡ��������    #
#==================#
sub DATARESET {

    @userlist = ();
    if($npc_mode eq "0"){
        open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);
    }else{
        open(DB,"$npc_file");seek(DB,0,0); @baselist=<DB>;close(DB);
        $LEN = @baselist;

        if ($LEN > 0) {
            for ($i=0; $i<$LEN; $i++) {
                ($w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_att,$w_def,$w_mhit,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_msg,$w_sts,$w_pls,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_dmes,$w_com,$w_inf,$w_feel,$w_group,$w_gpass) = split(/,/, $baselist[$i]);

                if ($w_cl eq $BOSS) {  #����¦��NPC
                    $w_att = int(rand(10)) + $w_att ;
                    $w_def = int(rand(10)) + $w_def ;
                    $w_mhit = int(rand(30)) + $w_mhit ;
                    $w_icon = $n_icon_file[$w_icon];
                } elsif ($w_cl eq $ZAKO) {  #����¦��NPC
                    $w_att = int(rand(5)) + $w_att ;
                    $w_def = int(rand(5)) + $w_def ;
                    $w_mhit = int(rand(15)) + $w_mhit ;
                    $w_icon = $n_icon_file[$w_icon];
                } else {  #����¾��NPC�Ϥ��ä�
                    $w_att = int(rand(5))  + $w_att ;
                    $w_def = int(rand(5))  + $w_def ;
                    $w_mhit = int(rand(10)) + $w_mhit ;
                    $w_icon = $icon_file[$w_icon];
                }
                if ($w_pls == 99) { $w_pls = int(rand($#area)+1) ; }
                $w_level = 1; $w_exp = 0;
                $w_kill = 0 ;
                $w_death = "" ;
                $w_we = $w_wf = "";
                $w_log = "" ; $w_bid = "" ;
                $w_host = $w_os = "";
                $w_a_name = "";

                $w_id = ($a_id . "$i"); $w_password = $a_pass2;
                $w_hit=$w_mhit; $w_sta = $maxsta;
                $w_feel = int(rand(20)) + $w_feel ;
                if ($w_feel > 300) { $w_feel = 300;}

                for ($j=0; $j<5; $j++) {
                    if($w_item[$j] =~ /<>HH/){
                        if (int(rand(2)) == 0) { $w_item[$j] =~ s/<>HH/<>HD2/g; }
                    }elsif ($w_item[$j] =~ /<>SH/) {
                        if (int(rand(2)) == 0) { $w_item[$j] =~ s/<>SH/<>SD2/g; }
                    }
                }

                &NPCCLUBMAKE;

                $userlist[$i] = "$w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_group,$w_gpass,$w_a_name,$w_feel,$w_host,$w_os,\n" ;
            }
        }
        open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);
    }

    #���֥ե����빹��
    $endtime = $now + ($battle_limit*60*60*24);
    $timelist="$now,$endtime,\n" ;
    open(DB,">$time_file"); seek(DB,0,0); print DB $timelist; close(DB);

    #�����ֹ�ե����빹��
    $memberlist="0,0,0,0,\n" ;
    open(DB,">$member_file"); seek(DB,0,0); print DB $memberlist; close(DB);

    #�ػߥ��ꥢ�ե����빹��
    ($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime($now+(1*60*60*24));
    $year+=1900;
    $min = "0$min" if ($min < 10);  $month++;
    $areadata[0] = ($year . "," . $month . "," . $mday . "," . "0,0\n") ;   #���ꥢ�ɲû���
    $areadata[1] = "1,0,,\n" ; #�ػߥ��ꥢ�����ϥå��󥰥ե饰

    @work = @place ;
    @work2 = @area ;
    @work3 = @arno ;

    $ar = splice(@work,0,1) ;
    $areadata[2] = "$ar," ;
    $ar2 = splice(@work2,0,1) ;
    $areadata[3] = "$ar2," ;
    $ar3 = splice(@work3,0,1) ;
    $areadata[4] = "$ar3," ;

    for ($i=1; $i<$#place+1; $i++) {
        $chk=$#work+1;$index = int(rand($chk));
        $ar = splice(@work,$index,1) ;
        $areadata[2] = ($areadata[2] . "$ar,");
        $ar2 = splice(@work2,$index,1) ;
        $areadata[3] = ($areadata[3] . "$ar2,");
        $ar3 = splice(@work3,$index,1) ;
        $areadata[4] = ($areadata[4] . "$ar3,");
    }
    $areadata[2] = ($areadata[2] . "\n");
    $areadata[3] = ($areadata[3] . "\n");
    $areadata[4] = ($areadata[4] . "\n");

    open(DB,">$area_file"); seek(DB,0,0); print DB @areadata; close(DB);

    #������
    $loglist = "$now,,,,,,,,,,,NEWGAME,,,,,\n" ;
    open(DB,">$log_file"); seek(DB,0,0); print DB $loglist; close(DB);
    open(DB,">$joutolog_file"); seek(DB,0,0); print DB $loglist; close(DB);

    $loglist = "" ;
    open(DB,">$error_file"); seek(DB,0,0); print DB $loglist; close(DB);

    open(DB, "$A_Rogin_file"); seek(DB,0,0); @loglist=<DB>;close(DB);
    while (50 <= @loglist) { shift(@loglist); }
    @loglist = (@loglist, "$now,$year/$month/$mday $hour:$min:$sec,$admpass,$host,FORMATED,\n");
    open(DB,">$A_Rogin_file"); seek(DB,0,0); print DB @loglist; close(DB);

    for($i=1; $i<=7; $i++) {
        open(DB,">$ADM_DIR/succeed$i.log"); seek(DB,0,0); print DB $loglist; close(DB);
        open(DB,">$ADM_DIR/faired$i.log"); seek(DB,0,0); print DB $loglist; close(DB);
    }

    for ($i=0; $i<$#area+1; $i++) {
        @areaitem = "" ;
        $filename = "$LOG_DIR/$i$item_file";
        open(DB,">$filename"); seek(DB,0,0); print DB @areaitem; close(DB);
    }

    #��å���¸�ǡ������
    open(DB,">$MES_DIR$mes_file"); seek(DB,0,0); print DB $loglist; close(DB);

    #�����ƥ�ե����빹��
    open(DB, "$haitem_file");seek(DB,0,0); @itemlist=<DB>;close(DB);

    for ($i=0; $i<$#itemlist+1; $i++) {
        ($w_i,$w_e,$w_t) = split(/,/, $itemlist[$i]);

        $idx = int(rand($#place)+1) ;

        $filename = "$LOG_DIR/$idx$item_file";
        $newitem = "$w_i,$w_e,$w_t,\n";
        open(DB,">>$filename"); seek(DB,0,0); print DB $newitem; close(DB);
    }

    #�������ե����빹��
    local($null_data) = "0,,,,\n";
    open(DB,">$gun_log_file");
    for ($i=0; $i<6; $i++){
        print DB $null_data;
    }
    close(DB);

    @f_list = ();
    #�桼����¸�ǡ������
    opendir(DIR, "$u_save_dir");
    foreach $file (readdir(DIR)) {
        unless($file =~ /^\.{1,2}$/){
            if($file =~ /$u_save_file/){
                push (@f_list,"$u_save_dir$file");
            }
        }
    }
    closedir(DIR);
    unlink(@f_list);

    #FLAG�ե����빹��
    open(FLAG,">$end_flag_file"); print FLAG ""; close(FLAG);

}
#==================#
# �� �������      #
#==================#
sub WINLOG {

    if($fl !~ /��λ/) { &ERROR("�ޤ���λ���Ƥ��ޤ���") ; }

    #����
    $game = "��$kaisuu�������ץ������";
    $imgurl = "../iconimg/";

    #ͥ����Ƚ��
    $mem = 0; $winkind = "";
    for ($i=0; $i<$#userlist+1; $i++) {
        ($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_group,$w_gpass,$w_a_name,$w_feel,$w_host,$w_os) = split(/,/, $userlist[$i]);
        if ($w_inf =~ /��/) {    #ͥ����
            ($id,$password,$f_name,$l_name,$sex,$cl,$no,$endtime,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg,$sts,$pls,$kill,$icon,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],$log,$dmes,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com,$inf,$group,$gpass,$a_name,$feel,$ho2,$os2) = split(/,/, $userlist[$i]);
            $winkind = "ͥ��";
            last;
        } elsif ($w_inf =~ /��/){
            ($id,$password,$f_name,$l_name,$sex,$cl,$no,$endtime,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg,$sts,$pls,$kill,$icon,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],$log,$dmes,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com,$inf,$group,$gpass,$a_name,$feel,$ho2,$os2) = split(/,/, $userlist[$i]);
            $winkind = "�����������";
            last;
        } else {
            if (($w_hit > 0) && ($w_inf !~ /NPC/)) {
                $mem++;
                $no = $i;
            }
        }
    }
    if ($winkind eq "") {
        if ($mem == 1) {
            ($id,$password,$f_name,$l_name,$sex,$cl,$no,$endtime,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg,$sts,$pls,$kill,$icon,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],$log,$dmes,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com,$inf,$group,$gpass,$a_name,$feel,$ho2,$os2) = split(/,/, $userlist[$no]);
            $winkind = "ͥ��";
        } else {
            &ERROR("�ޤ���λ���Ƥ��ޤ���");
        }
    }

    #ɽ���ѷ׻�
    local($w_name,$w_kind) = split(/<>/, $wep);
    local($b_name,$b_kind) = split(/<>/, $bou);
    local($b_name_h,$b_kind_h) = split(/<>/, $bou_h);
    local($b_name_f,$b_kind_f) = split(/<>/, $bou_f);
    local($b_name_a,$b_kind_a) = split(/<>/, $bou_a);
    local($b_name_i,$b_kind_i) = split(/<>/, $item[5]);

    $up = ($level * $level) + ($level * $baseexp);

    $cln = "$cl $sex$no��" ;

    if (($w_kind =~ /G|A/) && ($wtai == 0)) { #���� or ��̵���� or ��̵����
        $watt_2 = int($watt/10) ;
    } else {
        $watt_2 = $watt ;
    }

    $ball = $bdef + $bdef_h + $bdef_a + $bdef_f ;
    if ($item[5] =~ /AD/) {$ball += $eff[5];} #�������ɶ�

    local($tension);
    if($feel == 300) {
        $tension = "<font color=\"red\">Ķ��</font>";
    }elsif($feel > 240) {
        $tension = "<font color=\"orange\">Ķ����</font>";
    }elsif($feel > 180) {
        $tension = "<font color=\"yellow\">����</font>";
    }elsif($feel > 120) {
        $tension = "<font color=\"lime\">����</font>";
    }elsif($feel > 60) {
        $tension = "<font color=\"aqua\">�嵤</font>";
    }elsif($feel > 0) {
        $tension = "<font color=\"blue\">ݵ</font>";
    }else{
        $tension = "<font color=\"fuchsia\">����</font>";
    }

    if (($we eq "B") && ($w_kind =~ /B/)) { $tactics2 = "��ȿ�⡧����"; }
    elsif (($we eq "P") && ($w_kind =~ /P/)) { $tactics2 = "��ȿ�⡧����"; }
    elsif (($we eq "A") && ($w_kind =~ /A/) && ($wtai > 0)) { $tactics2 = "��ȿ�⡧�ݡ�"; }
    elsif (($we eq "G") && ($w_kind =~ /G/) && ($wtai > 0)) { $tactics2 = "��ȿ�⡧�ơ�"; }
    elsif (($we eq "N") && ($w_kind =~ /N/)) { $tactics2 = "��ȿ�⡧�¡�"; }
    elsif (($we eq "S") && ($w_kind =~ /S/)) { $tactics2 = "��ȿ�⡧�ɡ�"; }
    elsif (($we eq "D") && ($w_kind =~ /D/)) { $tactics2 = "��ȿ�⡧����"; }
    elsif (($we eq "C") && ($w_kind =~ /C/)) { $tactics2 = "��ȿ�⡧���"; }
    else { $tactics2 = "��ȿ�⡧����̵����"; }

    $kega ="" ;
    if ($inf =~ /Ƭ/) {$kega = ($kega . "Ƭ����") ;}
    if ($inf =~ /��/) {$kega = ($kega . "�ӡ�") ;}
    if ($inf =~ /ʢ/) {$kega = ($kega . "ʢ����") ;}
    if ($inf =~ /­/) {$kega = ($kega . "­��") ;}
    if ($inf =~ /��/) {$kega = ($kega . "�ǡ�") ;}
    if ($inf =~ /��/) {$kega = ($kega . "������") ;}
    if ($kega eq "") { $kega = "��" ;}

    local($p_wa) = int($wa/$BASE);
    local($p_wb) = int($wb/$BASE);
    local($p_wc) = int($wc/$BASE);
    local($p_wd) = int($wd/$BASE);
    local($p_wg) = int($wg/$BASE);
    local($p_ws) = int($ws/$BASE);
    local($p_wn) = int($wn/$BASE);
    local($p_wp) = int($wp/$BASE);

    local($hitbarleng) = int($hit / $mhit * 45);
    local($hitbarlenr) = 45 - $hitbarleng;
    local($stabarleng) = int($sta / $maxsta * 45);
    local($stabarlenr) = 45 - $stabarleng;

    local($nowtime) = sprintf("%04dǯ%02d��%02d����%s��%02d:%02d:%02d",$year, $month, $mday, ('��','��','��','��','��','��','��') [$wday], $hour, $min, $sec);

    &HEADER ;
print <<"_HERE_";
<TABLE width="400">
  <TBODY>
    <TR>
      <TD align="center">
       <B><FONT color="#ff0000" size="+3" face="�ͣ� ��ī">$game</FONT></B><BR><BR>
       <B><FONT color="#ff0000" size="+3" face="�ͣ� ��ī">$winkind��</FONT></B>
      </TD>
    </TR>
    <TR>
      <TD valign="top" width="400" height="311">
      <TABLE border="1" width="400" cellspacing="0" height="300">
        <TBODY>
          <TR>
            <TH colspan="5">$nowtime</TH>
          </TR>
          <TR>
            <TD ROWSPAN="4" width="17%" nowrap><IMG src="$imgurl$icon" width="70" height="70" border="0" align="middle"></TD>
            <TH width="16%" nowrap>�� ̾</TH><TD nowrap colspan="3">$f_name $l_name ($cln)</TD>
          </TR>
          <TR>
            <TH nowrap>�� ��</TH><TD nowrap>$club</TD>
            <TH nowrap>����</TH><TD nowrap>$a_name</TD>
          </TR>
          <TR>
            <TH nowrap>�� ��</TH><TD nowrap><img src="$imgurl$bar_green" width=$hitbarleng height=10><img src="$imgurl$bar_red" width=$hitbarlenr height=10> $hit/$mhit</TD>
            <TH width="16%" nowrap>��٥�</TH><TD width="16%" nowrap>$level($exp/$up)</TD>
          </TR>
          <TR>
            <TH nowrap>�����ߥ�</TH><TD nowrap><img src="$imgurl$bar_green" width=$stabarleng height=10><img src="$imgurl$bar_red" width=$stabarlenr height=10> $sta/$maxsta</TD>
            <TH nowrap>�ƥ󥷥��</TH><TD nowrap>$tension</TD>
          </TR>
          <TR>
            <TH nowrap>����Ľ�</TH>
            <TD nowrap colspan="2">$kega</TD>
            <TH nowrap>����</TH><TD nowrap><font color="red"><b>$kill</b></font>�ͻ���</TD>
          </TR>
          <TR>
            <TH nowrap>���롼��</TH><TD nowrap colspan="2">$group</TD>
            <TH nowrap>������</TH><TD nowrap>$att+$watt_2</TD>
          </TR>
          <TR>
            <TH nowrap>����</TH><TD nowrap colspan="2">$tactics $tactics2</TD>
            <TH nowrap>�ɸ���</TH><TD nowrap>$def+$ball</TD>
          </TR>

          <TR><TH nowrap colspan="5">������</TH></TR>
          <TR><TD nowrap colspan="5" align="center">�͡�$p_wa($wa) ����$p_wb($wb) �ꡧ$p_wc($wc) ����$p_wd($wd) �ơ�$p_wg($wg) �ɡ�$p_ws($ws) �¡�$p_wn($wn) ����$p_wp($wp)</TD></TR>

          <TR><TH nowrap>������</TH><TH nowrap colspan="2">����̾��</TH><TH nowrap>����</TH><TH nowrap>���</TH></TR>
          <TR><TH nowrap>�� ��</TH><TD nowrap colspan="2">$w_name</TD><TD nowrap>$watt</TD><TD nowrap>$wtai</TD></TR>
          <TR><TH nowrap>���ɶ�</TH><TD nowrap colspan="2">$b_name</TD><TD nowrap>$bdef</TD><TD nowrap>$btai</TD></TR>
          <TR><TH nowrap>Ƭ�ɶ�</TH><TD nowrap colspan="2">$b_name_h</TD><TD nowrap>$bdef_h</TD><TD nowrap>$btai_h</TD></TR>
          <TR><TH nowrap>���ɶ�</TH><TD nowrap colspan="2">$b_name_a</TD><TD nowrap>$bdef_a</TD><TD nowrap>$btai_a</TD></TR>
          <TR><TH nowrap>­�ɶ�</TH><TD nowrap colspan="2">$b_name_f</TD><TD nowrap>$bdef_f</TD><TD nowrap>$btai_f</TD></TR>
          <TR><TH nowrap>������</TH><TD nowrap colspan="2">$b_name_i</TD><TD nowrap>$eff[5]</TD><TD nowrap>$itai[5]</TD></TR>

          <TR height="9"><TH colspan="5">�����</TH></TR>
          <TR height="70" valign="top">
            <TD nowrap colspan="5">
_HERE_

            for ($i=0; $i<5; $i++) {
                if ($item[$i] ne "�ʤ�") {
                    ($i_name,$i_kind) = split(/<>/, $item[$i]);
                    print "$i_name/$eff[$i]/$itai[$i]<BR>\n";
                }
            }

print <<"_HERE_";
            </TD>
          </TR>
          <TR height="9"><TH colspan="5">������</TH></TR>
          <TR height="70" align="center">
            <TD nowrap colspan="5"><B>$com</B></TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
    </TR>
  </TBODY>
</TABLE>
<BR>
_HERE_

    if($winkind eq "�����������") {
        push(@log,"<P align=\"center\"><B><FONT color=\"#ff0000\" size=\"+3\" face=\"�ͣ� ��ī\">æ���԰���</FONT></B><BR></P>");
        push(@log,"<TABLE border=\"1\" cellspacing=\"0\" width=\"568\">\n");
        push(@log,"<tr align=\"center\"><th nowrap>��������</th><th nowrap>̾��</th><th nowrap>����</th><th nowrap>���롼��</th><th width=\"100%\">������</th></tr>\n");
        foreach (0 .. $#userlist) {
            ($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_group,$w_gpass,$w_a_name,$w_feel,$w_host,$w_os) = split(/,/, $userlist[$_]);

            if (($w_hit > 0) && ($id ne $w_id) && (($w_inf !~ /NPC0/) || ($hackflg))) {
                if ($w_a_name ne "") { $w_a_name = "($w_a_name)"; }
                push(@log,"<tr><td align=\"center\"><IMG src=\"$imgurl$w_icon\" width=\"70\" height=\"70\" border=\"0\"></td><td align=\"center\" nowrap>$w_cl $w_sex$w_no��<br>$w_f_name $w_l_name<br>$w_a_name</td><td align=\"center\" nowrap>$w_club<br><font color=\"red\"><b>$w_kill</b></font>�ͻ���</td><td align=\"center\" nowrap>$w_group</td><td width=\"100%\">$w_com</td></tr>\n");
            }
        }
        push(@log,"</table><BR>\n");
    }

    push (@log,"</CENTER>\n") ;
    push (@log,"<B><FONT color=\"#ff0000\" size=\"+3\" face=\"�ͣ� ��ī\">�ʹԾ���</FONT></B><BR><BR>\n");

    open(DB,"$log_file");seek(DB,0,0); @loglist=<DB>;close(DB);

    $getmonth=$getday=0;
    foreach $loglist(@loglist) {
        ($gettime,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_f_name2,$w_l_name2,$w_sex2,$w_cl2,$w_no2,$getkind,$info1,$info2,$info3)= split(/,/, $loglist);
        ($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime($gettime);
        $hour = "0$hour" if ($hour < 10);
        $min = "0$min" if ($min < 10);  $month++;
        $year += 1900;
        $week = ('��','��','��','��','��','��','��') [$wday];
        if (($getmonth != $month) || ($getday != $mday)) {
            if ($getmonth !=0) { push (@log,"</LI></UL>\n"); }
            $getmonth=$month;$getday = $mday;
            push (@log,"<P><font color=\"lime\"><B>$month�� $mday�� ($week����)</B></font><BR>\n");
            push (@log,"<UL>\n");
        }

        if ($info1 eq "") { $info1 = ""; } else { $info1 = "($info1)" ; }

        if ($getkind eq "DEATH") {  #��˴�ʼ�ʬ��������
            push (@log,"<LI>$hour��$minʬ��<font color=\"red\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡�</b></font>��<font color=\"red\"><b>��˴</b></font>������<font color=\"red\"><b>$info1</b></font><BR>\n") ;
        } elsif ($getkind eq "DEATH1") { #��˴���ǻ���
            push (@log,"<LI>$hour��$minʬ��<font color=\"red\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡�</b></font>��<font color=\"red\"><b>���ǻ�</b></font>������<font color=\"red\"><b>$info1</b></font><BR>\n") ;
        } elsif ($getkind eq "DEATH2") { #��˴��¾����
            push (@log,"<LI>$hour��$minʬ��<font color=\"red\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡�</b></font>��<font color=\"yellow\"><b>$w_f_name2 $w_l_name2��$w_cl2 $w_sex2$w_no2�֡�</b></font>��<font color=\"aqua\"><b>$info2</b></font>��<font color=\"red\"><b>�֤�Ƥ��</b></font>�ˤ��줿��<font color=\"red\"><b>$info1</b></font><BR>\n") ;
        } elsif ($getkind eq "DEATH3") { #��˴��¾����
            push (@log,"<LI>$hour��$minʬ��<font color=\"red\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡�</b></font>��<font color=\"yellow\"><b>$w_f_name2 $w_l_name2��$w_cl2 $w_sex2$w_no2�֡�</b></font>��<font color=\"aqua\"><b>$info2</b></font>��<font color=\"red\"><b>$info3</b></font>���줿��<font color=\"red\"><b>$info1</b></font><BR>\n") ;
        } elsif ($getkind eq "DEATH4") { #��˴�����ܡ�
            push (@log,"<LI>$hour��$minʬ��<font color=\"red\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡�</b></font>�����ܤ�<font color=\"red\"><b>�跺</b></font>���줿��<font color=\"red\"><b>$info1</b></font><BR>\n") ;
        } elsif ($getkind eq "DEATHAREA") { #��˴�ʶػߥ��ꥢ��
            push (@log,"<LI>$hour��$minʬ��<font color=\"red\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡�</b></font>��<font color=\"red\"><b>�ػߥ��ꥢ</b></font>�ΰ١���˴������<font color=\"red\"><b>$info1</b></font><BR>\n") ;
        } elsif ($getkind eq "WINEND") { #ͥ���Է���
            push (@log,"<LI>$hour��$minʬ��<font color=\"lime\"><b>�����ཪλ���ʾ��ܥץ����»����������ǧ��˥����</B></font> <BR>\n") ;
        } elsif ($getkind eq "EX_END") { #�ץ�������
            push (@log,"<LI>$hour��$minʬ��<font color=\"lime\"><b>�����ཪλ���ץ����۵����</B></font> <BR>\n") ;
        } elsif ($getkind eq "HACK") { #�ϥå���
            push (@log,"<LI>$hour��$minʬ��<font color=\"lime\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡ˤˤ�äƥϥå��󥰤������ʬ���ε�ǽ����ߡ���</B></font> <BR>\n") ;
        } elsif ($getkind eq "SPEAKER") { #����
            push (@log,"<LI>$hour��$minʬ��<font color=\"aqua\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡�</b></font> �� <font color=\"aqua\"><b>$info1</b></font> �ȶ������<BR>\n") ;
        } elsif ($getkind eq "AREA") { #�ػߥ��ꥢ�ɲ�
            if ($info2 == 7) {
                push (@log,"<LI>$hour��$minʬ��<font color=\"lime\"><b>�ץ����ǽ�������</b></font>��<BR>\n") ;
            } elsif ($info2 == 8) {
                push (@log,"<LI>$hour��$minʬ��<font color=\"lime\"><b>�����ڤ�ˤ�ꥲ���ཪλ</b></font>��<BR>\n") ;
            } else {
                push (@log,"<LI>$hour��$minʬ��<font color=\"lime\"><b>�ץ����$info2���ܳ���</b></font>��<BR>\n") ;
            }
        } elsif ($getkind eq "ENTRY") { #������Ͽ
            push (@log,"<LI>$hour��$minʬ��<font color=\"yellow\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡�</b></font> �� ž�����Ƥ�����<font color=\"yellow\">$info1</font><BR>\n") ;
        } elsif ($getkind eq "NEWGAME") { #�����ͤˤ��ǡ��������
            push (@log,"<LI>$hour��$minʬ��<font color=\"lime\"><b>�����ץ���೫��</b></font>��<BR>\n") ;
        }
    }

    push (@log,"</UL>\n<CENTER>\n");
    push (@log,"<BR><B><a href=\"$home\">HOME</A></B><BR>\n");

    print @log;
    &FOOTER;
}

#==================#
# �� ����ֺ���    #
#==================#
sub NPCCLUBMAKE {


    local($dice) =  rand(100) ;
    local($dice2) = int(rand(8)) ;
    local($dice3) = int(rand(6)) ;

    if (($w_cl eq $BOSS) || ($w_cl eq $ZAKO)) {
        $w_club = "���ܷ�";
        $w_wa = $w_wg = $w_wc = $w_wd = $w_ws = $w_wn = $w_wb = $w_wp = 4 * $BASE;
    } else {
        $w_wa = int(rand(15)); $w_wg = int(rand(15));
        $w_wc = int(rand(15)); $w_wd = int(rand(15));
        $w_ws = int(rand(15)); $w_wn = int(rand(15));
        $w_wb = int(rand(15)); $w_wp = int(rand(15));
        if ($dice < 80) {
            if ($dice2 == 0) {
                $w_club = "��ƻ��";
                $w_wa += 1 * $BASE;
            }elsif ($dice2 == 1) {
                $w_club = "�ͷ���";
                $w_wg += 1 * $BASE;
            }elsif ($dice2 == 2) {
                $w_club = "������";
                $w_wb += 1 * $BASE;
            }elsif ($dice2 == 3) {
                $w_club = "�Х�����";
                $w_wc += 1 * $BASE;
            }elsif ($dice2 == 4) {
                $w_club = "�ʳ���";
                $w_wd += 1 * $BASE;
            }elsif ($dice2 == 5) {
                $w_club = "�ե��󥷥���";
                $w_ws += 1 * $BASE;
            }elsif ($dice2 == 6) {
                $w_club = "��ƻ��";
                $w_wn += 1 * $BASE;
            }else {
                $w_club = "�ܥ�������";
                $w_wp += 1 * $BASE;
            }
        } else {
            if ($dice3 == 0) {
                $w_club = "Φ����" ;
            }elsif ($dice3 == 1) {
                $w_club = "����������" ;
            }elsif ($dice3 == 2) {
                $w_club = "�ѥ�������" ;
            }elsif ($dice3 == 31) {
                $w_club = "�ݷ�Ѱ�" ;
            }elsif ($dice3 == 4) {
                $w_club = "���Х��Х���" ;
            }else {
                $w_club = "�����" ;
            }
        }
    }
}

#================#
# �� ���������  #
#================#
sub InitResetTime {
    if ($auto_reset) {
        local($sec,$min,$hour,$mday,$month,$year) = localtime($now+(60*60*12)+int(rand(60*60*12)));
        $year += 1900; $month++;
        $newareadata[0] = "$year,$month,$mday,$hour,0,\n";   #��ư���������
        $newareadata[1] = "$ar,0,�����,\n";
        $newareadata[2] = $arealist[2];
        $newareadata[3] = $arealist[3];
        $newareadata[4] = $arealist[4];
        open(DB,">$area_file"); seek(DB,0,0); print DB @newareadata; close(DB);
    }
}

#==================#
# �� ����ե�����  #
#==================#
sub INITFORM {

    push(@log,"<B><FONT color=\"#ff0000\" size=\"+3\" face=\"�ͣ� ��ī\">�����⡼��</FONT></B><BR><BR>\n");
    push(@log,"�������������\n");
    push(@log,"<FORM METHOD=\"POST\">\n");
    push(@log,"<INPUT TYPE=\"HIDDEN\" NAME=\"Command\" VALUE=\"RESINI2\">\n");
    push(@log,"<INPUT type=\"hidden\" name=\"Password\" value=\"$admpass\">\n");
    push(@log,"ǯ��<INPUT size=\"8\" type=\"text\" name=\"resyear\" maxlength=\"8\"><br>\n");
    push(@log,"�<INPUT size=\"8\" type=\"text\" name=\"resmon\" maxlength=\"8\"><br>\n");
    push(@log,"����<INPUT size=\"8\" type=\"text\" name=\"resday\" maxlength=\"8\"><br>\n");
    push(@log,"����<INPUT size=\"8\" type=\"text\" name=\"reshour\" maxlength=\"8\"><br>\n");
    push(@log,"ʬ��<INPUT size=\"8\" type=\"text\" name=\"resmin\" maxlength=\"8\"><br>\n");
    push(@log,"<INPUT type=\"submit\" name=\"Enter\" value=\"����\">\n");
    push(@log,"</FORM>\n");

    &HEADER ;
    print @log;
    &FOOTER;
}

#==================#
# �� �������������#
#==================#
sub RESINIT {

    if ($in{'resyear'} ne "" && $in{'resmon'} ne "" && $in{'resday'} ne "" && $in{'reshour'} ne "" && $in{'resmin'} ne "") {
        $newareadata[0] = "$in{'resyear'},$in{'resmon'},$in{'resday'},$in{'reshour'},$in{'resmin'},\n";   #��ư���������
        $newareadata[1] = "$ar,0,�����,\n";
        $newareadata[2] = $arealist[2];
        $newareadata[3] = $arealist[3];
        $newareadata[4] = $arealist[4];
        open(DB,">$area_file"); seek(DB,0,0); print DB @newareadata; close(DB);
        open(FLAG,">$end_flag_file"); print FLAG "��λ\n"; close(FLAG);
        push(@log,"<B><FONT color=\"#ff0000\" size=\"+3\" face=\"�ͣ� ��ī\">�����⡼��</FONT></B><BR><BR>\n");
        push(@log,"�����������$in{'resyear'}/$in{'resmon'}/$in{'resday'} $in{'reshour'}:$in{'resmin'}:0�ɤ����ꤷ�ޤ�����<br>\n");
        push(@log,"<br><B><FONT color=\"#ff0000\">>><a href=\"$home\">HOME</a> >><a href=\"$adm\">ADMIN</a></b></FONT>\n");
        &HEADER;
        print @log;
        &FOOTER;
    } else {
        &MENU;
        print "��$in{'resyear'}/$in{'resmon'}/$in{'resday'} $in{'reshour'}:$in{'resmin'}:0��";
    }
}

1
