# ���ѥ��֥롼����

#==================#
# �� ID�����å�����#
#==================#
sub IDCHK {

    $mem=0; $perlv=0; $perlv2=0;
    $chksts = "NG"; $hostchk = "OK";
    for ($i=0; $i<$#userlist+1; $i++) {
        ($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_group,$w_gpass,$w_a_name,$w_feel,$w_host,$w_os) = split(/,/, $userlist[$i]);
        if ($w_id eq $id2) {    #ID���ס�
            if ($w_password eq $password2) {    #�ѥ�������
                if ($w_hit > 0) {
                    $chksts = "OK"; $Index=$i; $mem++; $perlv+=$w_level; $perlv2++; $plsmem[$w_pls]++;
                    ($id,$password,$f_name,$l_name,$sex,$cl,$no,$endtime,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg,$sts,$pls,$kill,$icon,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],$log,$dmes,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com,$inf,$group,$gpass,$a_name,$feel,$ho2,$os2) = split(/,/, $userlist[$i]);
                    &CSAVE;

                    if($mode eq "main") {
                        $rogindat = "$now,$year/$month/$mday $hour:$min:$sec,$id,$password,$f_name$l_name,$host,\n";
                        open(DB,">>$ADM_DIR/succeed$pgday.log"); seek(DB,0,0); print DB $rogindat; close(DB);
                    }

                    #�������ɹ�
                    open(DB,"$gun_log_file");seek(DB,0,0); @gunlog=<DB>;close(DB);

                    local($guntime,$gunpls,$wid,$wid2,$a) = split(/,/,$gunlog[0]) ;
                    if (($now < ($guntime+(15))) && ($wid ne $id) && ($wid2 ne $id)) {   #�ƻ��Ѥ���15�ð��⡩
                        $jyulog = "<font color=\"yellow\"><b>$gunpls �����ǡ�������ʹ��������������</b></font><br>" ;
                    } else { $jyulog = "" ; }
                    local($guntime,$gunpls,$wid,$wid2,$a) = split(/,/,$gunlog[1]) ;
                    if (($now < ($guntime+(15))) && ($wid ne $id) && ($wid2 ne $id) && ($place[$pls] eq $gunpls)) {  #��������15�ð��⡩
                        $jyulog2 = "<font color=\"yellow\"><b>�᤯�����Ĥ���ï���������줿�Τ���������</b></font><br>" ;
                    } else { $jyulog2 = "" ; }
                    local($guntime,$gunpls,$wid,$wid2,$a) = split(/,/,$gunlog[2]) ;
                    if (($now < ($guntime+(30)))) { #���ԡ������Ѥ���30�ð��⡩
                        $jyulog3 = "<font color=\"yellow\"><b>$gunpls ��������$wid������ʹ�����롦����</b></font><br><font color=\"lime\"><b>��$wid2��</b></font><br>" ;
                    } else { $jyulog3 = "" ; }
                    local($guntime,$gunpls,$wid,$wid2,$a) = split(/,/,$gunlog[3]) ;
                    if (($now < ($guntime+(15))) && ($wid ne $id) && ($wid2 ne $id)) {   #��ȯ����15�ð��⡩
                        $jyulog4 = "<font color=\"yellow\"><b>$gunpls �����ǡ�������ʹ��������������</b></font><br>" ;
                    } else { $jyulog4 = "" ; }
                } else {
                    &CDELETE;
                    &ERROR("���˻�˴���Ƥ��ޤ���<BR><BR>�����$w_death<BR><BR><font color=\"lime\"><b>$w_msg</b></font><br><br>����Ʈ����<br>$w_log") ;
                }
            } else {
                $rogindat = "$now,$year/$month/$mday $hour:$min:$sec,$id2,$password2,passerror,$host,\n";
                open(DB,">>$ADM_DIR/faired$pgday.log"); seek(DB,0,0); print DB $rogindat; close(DB);
                &ERROR("�ѥ���ɤ����פ��ޤ���") ;
            }
        } else {
            if ($w_hit > 0) {
                $plsmem[$w_pls]++ ;
                if ($w_inf !~ /NPC0/) { $mem ++ ; }
                if ($w_inf !~ /NPC/) {
                    $perlv+=$w_level; $perlv2++;
                    if ($host eq $w_host) { $hostchk = "NG"; }
                }
            }
        }
    }

    if ($chksts eq "NG") {
        $rogindat = "$now,$year/$month/$mday $hour:$min:$sec,$id2,$password2,iderror,$host,\n";
        open(DB,">>$ADM_DIR/faired$pgday.log"); seek(DB,0,0); print DB $rogindat; close(DB);
        &ERROR("�ɣĤ����Ĥ���ޤ���") ;
    }

    if ($IP_deny && $hostchk eq "NG" && $inf !~ /NPC/) {
        $rogindat = "$now,$year/$month/$mday $hour:$min:$sec,$id2,$password2,hosterror,$host,\n";
        open(DB,">>$ADM_DIR/faired$pgday.log"); seek(DB,0,0); print DB $rogindat; close(DB);
        &ERROR("��Ĥ�IP����³�Ǥ��륭���ϰ�ͤ����Ǥ���") ;
    }

    local($b_limit) = ($battle_limit * 3) + 1;
    if ((($mem == 1) && ($inf =~ /��/) && ($ar > $b_limit))||(($mem == 1) && ($ar > $b_limit))) {    #ͥ����
        if($fl !~ /��λ/){
            &LOGSAVE("WINEND1");
        }
        require "$LIB_DIR/ending.cgi";
        &ENDING;
    }elsif ($inf =~ /��/){
        require "$LIB_DIR/ending.cgi";
        &ENDING;
    }elsif ($fl =~ /���/){
        require "$LIB_DIR/ending.cgi";
        &ENDING;
    } else {
        if ($log ne '') {$wlog = $log ;$log="";&SAVE;$log=$wlog;}
        $bid = "" ;
    }
}

#==================#
# �� ���ơ�������  #
#==================#
sub STS {

    local($watt_2) = 0 ;

    if (($Command ne "INN2")&&($Command ne "HEAL2")&&($Command ne "KYUKEI2")) {
        $up = ($now - $endtime) / $kaifuku_time;
        if ($inf =~ /ʢ/) { $up = $up / 2 ; }
        if ($sts eq "��̲") {
            if ($club eq "���Х��Х���") { $up = $up * 1.5; }
            $maxp = $maxsta - $sta ;    #�����ͤޤǤ�����
            $up = int($up);
            if ($up > $maxp) { $up = $maxp ; }
            $sta += $up ;
            if ($sta > $maxsta) { $sta = $maxsta ; }
            $log = ($log . "��̲�η�̡������ߥʤ� $up ����������<BR>") ;
            $sts = "����"; $endtime = 0 ;
            &SAVE ;
        } elsif ($sts eq "����") {
            if ($kaifuku_rate == 0) { $kaifuku_rate = 1; }
            if ($club eq "�ݷ�Ѱ�") { $up = $up * 1.5; }
            $up = int($up / $kaifuku_rate) ;
            $maxp = $mhit - $hit ;  #�����ͤޤǤ�����
            if ($up > $maxp) { $up = $maxp ; }
            $hit += $up ;
            if ($hit > $mhit) { $hit = $mhit ; }
            $log = ($log . "���Ťη�̡����Ϥ� $up ����������<BR>") ;
            $sts = "����"; $endtime = 0 ;
            &SAVE ;
        }
    }

    local($w_name,$w_kind) = split(/<>/, $wep);
    local($b_name,$b_kind) = split(/<>/, $bou);
    local($b_name_h,$b_kind_h) = split(/<>/, $bou_h);
    local($b_name_f,$b_kind_f) = split(/<>/, $bou_f);
    local($b_name_a,$b_kind_a) = split(/<>/, $bou_a);
    local($b_name_i,$b_kind_i) = split(/<>/, $item[5]);

    $up = ($level * $level) + ($level * $baseexp);

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

    if (($we eq "B") && ($w_kind =~ /B/)) { $tactics2 = "��"; }
    elsif (($we eq "P") && ($w_kind =~ /P/)) { $tactics2 = "��"; }
    elsif (($we eq "A") && ($w_kind =~ /A/) && ($wtai > 0)) { $tactics2 = "��"; }
    elsif (($we eq "G") && ($w_kind =~ /G/) && ($wtai > 0)) { $tactics2 = "��"; }
    elsif (($we eq "N") && ($w_kind =~ /N/)) { $tactics2 = "��"; }
    elsif (($we eq "S") && ($w_kind =~ /S/)) { $tactics2 = "��"; }
    elsif (($we eq "D") && ($w_kind =~ /D/)) { $tactics2 = "��"; }
    elsif (($we eq "C") && ($w_kind =~ /C/)) { $tactics2 = "��"; }
    else { $tactics2 = "����̵��"; }

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

    local($hitbarleng,$hitbarlenr,$stabarleng,$stabarlenr);
    if ($hit > 0) { $hitbarleng = int($hit / $mhit * 45); } else { $hitbarleng = 0; }
    $hitbarlenr = 45 - $hitbarleng;
    $stabarleng = int($sta / $maxsta * 45);
    $stabarlenr = 45 - $stabarleng;

    $nowtime = sprintf("%04dǯ%02d��%02d����%s��%02d:%02d:%02d", $year, $month, $mday, ('��','��','��','��','��','��','��') [$wday], $hour, $min, $sec);

    local(@ars) = split(/,/, $arealist[2]);
    local($info) = "";
    $info .= "<b><font color=\"lime\">ʿ�ѥ�٥�</FONT>��<font color=\"#00ffff\">" . $perlv/$perlv2 . "</font></b><br>\n";

    if($lim_sec) {
        $info .= "<b><font color=\"lime\">Ϣ³�������</FONT>��<font color=\"#00ffff\">$lim_sec</font>��</b><br>\n";
    }

    $info .= "<b><font color=\"lime\">��ư��</font>��<font color=\"#00ffff\">$playmem</font>��</b><br>\n";
    $info .= "<b><font color=\"lime\">����ζػߥ��ꥢ</FONT></b><br>\n";

    if ($hackflg) {
        $info .= "<b><font color=\"aqua\">�ϥå��󥰤���Ƥ��ޤ���</font></b><br>\n";
    } else {
        $info .= "<b><font color=\"#ffff00\">$ars[$ar]��$ars[$ar+1]��$ars[$ar+2]</font></b><br>";
    }

print <<"_HERE_";
<TABLE width="610">
  <TBODY>
    <TR>
      <TD align="center" colspan="2"><B><FONT color="#ff0000" size="+3" face="�ͣ� ��ī">$place[$pls]��$area[$pls]��</FONT></B></TD>
    </TR>
    <TR>
      <TD align="center" colspan="2"><B><FONT color="#ff0000">@links</FONT></B></TD>
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
            <TH width="16%" nowrap>�� ̾</TH><TD nowrap colspan="3">$f_name $l_name ($cl $sex$no��)</TD>
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
            <TH nowrap>����Ľ�</TH><TD nowrap colspan="2">$kega</TD>
            <TH nowrap>����</TH><TD nowrap><font color="red"><b>$kill</b></font>�ͻ���</TD>
          </TR>
          <TR>
            <TH nowrap>���롼��</TH><TD nowrap colspan="2">$group($gpass)</TD>
            <TH nowrap>������</TH><TD nowrap>$att+$watt_2</TD>
          </TR>
          <TR>
            <TH nowrap>����</TH><TD nowrap colspan="2">$tactics(ȿ�⡧$tactics2)</TD>
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
                    $i_kind2 = "";
                    if ($item[$i] =~ /<>W/) {
                        if ($i_kind =~ /G/) { $i_kind2 .= "�ؽơ�"; }
                        if ($i_kind =~ /A/) { $i_kind2 .= "�صݡ�"; }
                        if ($i_kind =~ /B/) { $i_kind2 .= "������"; }
                        if ($i_kind =~ /N/) { $i_kind2 .= "�ػ¡�"; }
                        if ($i_kind =~ /S/) { $i_kind2 .= "�ػɡ�"; }
                        if ($i_kind =~ /D/) { $i_kind2 .= "������"; }
                        if ($i_kind =~ /C/) { $i_kind2 .= "�����"; }
                        if ($i_kind =~ /P/) { $i_kind2 .= "�ز���"; }
                        $i_kind2 = "<FONT COLOR=\"yellow\">$i_kind2</FONT>\n";
                    } elsif ($item[$i] =~ /<>D|<>A/) {
                        if ($item[$i] =~ /<>A/) { $i_kind2 = "�������ʡ�"; }
                        elsif ($i_kind =~ /DB/) { $i_kind2 = "�����ɶ��"; }
                        elsif ($i_kind =~ /DH/) { $i_kind2 = "��Ƭ�ɶ��"; }
                        elsif ($i_kind =~ /DA/) { $i_kind2 = "�����ɶ��"; }
                        elsif ($i_kind =~ /DF/) { $i_kind2 = "��­�ɶ��"; }
                        $i_kind2 = "<font color=\"orange\">$i_kind2</font>";
                    } elsif ($item[$i] =~ /<>S/) {
                        $i_kind2 = "�إ����ߥʲ�����";
                        if($i_kind =~ /��/) { $i_kind2 .= "�ؿ����"; }
                        $i_kind2 = "<font color=\"aqua\">$i_kind2</font>";
                    } elsif ($item[$i] =~ /<>H/) {
                        $i_kind2 = "�����ϲ�����";
                        if($i_kind =~ /��/) { $i_kind2 .= "�ؿ����"; }
                        $i_kind2 = "<font color=\"aqua\">$i_kind2</font>";
                    } elsif ($item[$i] =~ /<>T/) { $i_kind2 = "<font color=\"yellow\">��櫡�</font>";
                    } else { $i_kind2 = "<font color=\"silver\">�ؤ���¾��</font>"; }
                    print "$i_name/$eff[$i]/$itai[$i] $i_kind2<BR>\n";
                }
            }

print <<"_HERE_";
            </TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
      <TD valign="top" width="210" height="365">
      <TABLE border="1" cellspacing="0">
        <TBODY>
          <TR><TH width="210">���ޥ��</TH>
          <TR>
            <TD align="left" valign="top" width="210" height="278">
            <FORM METHOD="POST" name="f1">
            <INPUT TYPE="HIDDEN" NAME="mode" VALUE="command">
            <INPUT TYPE="HIDDEN" NAME="Id" VALUE="$id2">
            <INPUT TYPE="HIDDEN" NAME="Password" VALUE="$password2">
_HERE_

            &COMMAND;

print <<"_HERE_";
            </FORM>
            </TD>
          </TR>
          <TR>
            <TH width="210" height="9">$pgday���ܡʻĤ�$mem�͡�</TH>
          </TR>
          <TR>
            <TD width="210" height="70" nowrap>
$info
            </TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
    </TR>
    <TR>
      <TD valign="top" height="151">
      <TABLE border="1" cellspacing="0" height="150" cellpadding="0">
        <TBODY>
          <TR>
            <TH width="400" height="10">��������ɥ�</TH>
          </TR>
          <TR>
            <TD width="400" height="140" valign="top">$log</TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
      <TD valign="top" height="151">
      <TABLE border="1" cellspacing="0" height="150" cellpadding="0">
        <TBODY>
          <TR>
            <TH height="10" width="210" nowrap>���롼�ץ��С�</TH>
          </TR>
          <TR>
            <TD height="140" valign="top" width="210" nowrap>
_HERE_

            &GrpMem;

print <<"_HERE_";
            </TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
    </TR>
  </TBODY>
</TABLE>
<BR>
_HERE_
}

#==================#
# �� �ǥ����ɽ���  #
#==================#
sub DECODE {
    $p_flag=0;
    if ($ENV{'REQUEST_METHOD'} eq "POST") {
        $p_flag=1;
        if ($ENV{'CONTENT_LENGTH'} > 51200) { &ERROR("�۾�����ϤǤ�"); }
        read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
    } else { $buffer = $ENV{'QUERY_STRING'}; }

    @pairs = split(/&/, $buffer);
    foreach (@pairs) {
        ($name,$value) = split(/=/, $_);
        $value =~ tr/+/ /;
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        &jcode::convert(*value, "euc", "", "z");
        &jcode::tr(\$value, '��', ' ');

        $value =~ s/&amp;/&/g;
        $value =~ s/&lt;/</g;
        $value =~ s/&gt;/>/g;
        $value =~ s/&quot;/"/g;
        $value =~ s/&nbsp;/ /g;

        $value =~ s/&/&amp;/g;
        $value =~ s/</&lt;/g;
        $value =~ s/>/&gt;/g;
        $value =~ s/"/&quot;/g;
        $value =~ s/ /&nbsp;/g;
        $value =~ s/,/��/g; #�ǡ�����»�к�

        if ($name eq "ITDEL") { push(@IDEL,$value);}
        $in{$name} = $value;
    }

    $mode = $in{'mode'};
    $id2 = $in{'Id'};
    $password2 = $in{'Password'};

    $Command = $in{'Command'};
    $Command2 = $in{'Command2'};
    $Command3 = $in{'Command3'};
    $Command4 = $in{'Command4'};
    $Command5 = $in{'Command5'};
    $Command6 = $in{'Command6'};

    $l_name2 = $in{'L_Name'} ;
    $f_name2 = $in{'F_Name'} ;
    $a_name2 = $in{'A_Name'} ;
    $msg2  = $in{'Message'} ;
    $dmes2 = $in{'Message2'} ;
    $dengon = $in{'Dengon'} ;
    $com2 = $in{'Comment'} ;
    $sex2 = $in{'Sex'};
    $icon2 = $in{'Icon'};
    $itno2 = $in{'Itno'};
    $getid = $in{'WId'};
    $speech = $in{'speech'};
    $group2 = $in{'Group'};
    $gpass2 = $in{'Gpass'};

    srand;

}

#==================#
# �� ��˥塼��    #
#==================#
sub COMMAND {

    local($i) = 0 ;
    local($n) = 0 ;

    if (($Command eq "HEAL2") || ($Command eq "INN2")) {
        if ($Command eq "HEAL2") {
            $log = ($log . "����μ��Ť򤷤褦��<BR>") ;
            $sts = "����" ;
            print "�����桦������<BR><BR>\n";
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"HEAL2\" checked>����<BR><BR>\n";
        } elsif ($Command eq "INN2") {
            $log = ($log . "�������Ƥ�������<BR>") ;
            $sts = "��̲" ;
            print "��̲�桦������<BR><BR>\n";
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"INN2\" checked>��̲<BR><BR>\n";
        }
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MESSAGE\">�£ҥ�å�<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\">���<BR><BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\" ondblclick=\"dbk()\">\n";
        return ;
    }

    if (($Command eq '')||($Command eq "MAIN")) {   #MAIN
        $log = ($log . "$jyulog$jyulog2$jyulog3$jyulog4���ơ��ɤ����褦��������<br>") ;
        print "����Ԥ��ޤ�����<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MOVE\">��ư\n";
        local(@kin_ar) = split(/,/, $arealist[2]);
        if (($hackflg) || ($inf =~ /NPC/)) {
            $kinlist = "";
        }else{
            for($k=0;$k<$ar;$k++){
                $kinlist = ($kinlist . $kin_ar[$k]);
            }
        }
        print "��<select name=\"Command2\" onClick=\"sl($n)\">\n" ;
        for ($j=0; $j<$#place+1; $j++) {
            if (($place[$j] ne $place[$pls]) && ($kinlist !~ /$place[$j]/)) {
                print "<option value=\"MV$j\">$place[$j]($area[$j])</option>\n";
            }
        }
        print "</select><BR>\n";
        $n++;

        if (($place[$pls] ne "ʬ��") || ($hackflg)) {
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"ACTION\">��ư\n";
            print "��<select name=\"Command3\" onClick=\"sl($n)\">\n" ;
            print "<option value=\"SEARCH\">õ��</option>\n";
            if (($inf !~ /��/) && ($pgday < 7)) { print "<option value=\"HEAL\">����</option>\n"; }
            print "<option value=\"INN\">��̲</option>\n";
            print "</select><BR>\n";
            $n++;
        }

        print "��<INPUT type=\"radio\" name=\"Command\" value=\"ITMAIN\">ƻ��\n";
        print "��<select name=\"Command4\" onClick=\"sl($n)\">\n" ;
        print "<option value=\"ITEM\">���ѡ�����</option>\n";
        print "<option value=\"DEL\">���</option>\n";
        print "<option value=\"SEIRI\">����</option>\n";
        print "<option value=\"BUNKATU\">ʬ��</option>\n";
        print "<option value=\"GOUSEI\">����</option>\n";
        print "<option value=\"ITSEND\">����</option>\n";
        print "<option value=\"WEPKAI\">�����ʲ��</option>\n";
        print "<option value=\"WEPDEL\">���������</option>\n";
        if(($wep =~ /<>WG|<>WA/) && ($wtai > 0)) { 
            print "<option value=\"SPLIT\">���ʬ��</option>\n"; 
        }
        print "</select><BR>\n";
        $n++;

        print "��<INPUT type=\"radio\" name=\"Command\" value=\"KOUDOU\">����\n";
        print "��<select name=\"Command5\" onClick=\"sl($n)\">\n" ;
        print "<option value=\"KOU_0\">�̾�</option>\n";
        print "<option value=\"KOU_1\">����Ż�</option>\n";
        if ($pgday <= $tactlim) { print "<option value=\"KOU_2\">�ɸ�Ż�</option>\n"; }
        print "<option value=\"KOU_3\">��̩��ư</option>\n";
        print "<option value=\"KOU_4\">õ����ư</option>\n";
        print "<option value=\"KOU_5\">������ư</option>\n";
        print "<option value=\"KOU_6\">̿��Ż�</option>\n";
        print "<option value=\"KOU_7\">����Ż�</option>\n";
        if (($pgday > $tactlim) || ($mem <= 20 && $pgday > 1)) { print "<option value=\"KOU_8\">ϢƮ��ư</option>\n"; }
        print "</select><BR>\n";
        $n++;

        print "��<INPUT type=\"radio\" name=\"Command\" value=\"SPECIAL\">�ü�\n";
        print "��<select name=\"Command6\" onClick=\"sl($n)\">\n" ;
        print "<option value=\"CATCHG\">ȿ������</option>\n";
        print "<option value=\"MESSAGE\">�£ҥ�å�</option>\n";
        print "<option value=\"WINCHG\">�����ѹ�</option>\n";
        print "<option value=\"GRPCHG\">��°�ѹ�</option>\n";
        print "<option value=\"OUKYU\">���޽���</option>\n";
        print "<option value=\"PSCHECK\">�Ǹ�</option>\n";
        for ($poi=0; $poi<5; $poi++){
            if ($item[$poi] eq "����<>Y") {
                print "<option value=\"POISON\">��ʪ����</option>\n";
                last;
            }
        }
        for ($poi2=0; $poi2<5; $poi2++){
            if ($item[$poi2] eq "�����º�<>Y") {
                print "<option value=\"ANTIPS\">������</option>\n";
                last;
            }
        }
        for ($spi=0; $spi<5; $spi++){
            if (($item[$spi] eq "���ӥ��ԡ���<>Y") || ($club eq "������")) {
                print "<option value=\"SPIICH\">����</option>\n";
                last;
            }
        }
        for ($paso=0; $paso<5; $paso++){
            if (($item[$paso] eq "��Х���PC<>Y")&&($itai[$paso] >= 1)) {
                print "<option value=\"HACK\">�ϥå���</option>\n";
                last;
            }
        }
        print "</select><BR>\n";
        $n++;

        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\" ondblclick=\"dbk()\">\n";
    } elsif (($Command eq "ITMAIN") && ($Command4 eq "ITEM")) {  #�����ƥ�
        $log = ($log . "�ǥ��ѥå�����ˤϡ��������äƤ������ʡ�������<BR>") ;
        print "������Ѥ��ޤ�����<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>���<BR><BR>\n";
        for ($i=0; $i<5; $i++) {
            if ($item[$i] ne "�ʤ�") {
                ($in, $ik) = split(/<>/, $item[$i]);
                print "��<INPUT type=\"radio\" name=\"Command\" value=\"ITEM_$i\">$in/$eff[$i]/$itai[$i]<BR>\n";
            }
        }
        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\" ondblclick=\"dbk()\">\n";
    } elsif (($Command eq "ITMAIN") && ($Command4 eq "DEL")) {   #�����ƥ����
        $log = ($log . "�ǥ��ѥå�������������뤫��������<BR>") ;
        print "����ΤƤޤ�����<BR><BR>\n";
        for ($i=0; $i<5; $i++) {
            if ($item[$i] ne "�ʤ�") {
                ($in, $ik) = split(/<>/, $item[$i]);
                print "��<input type=\"checkbox\" name=\"ITDEL\" value=\"$i\">$in/$eff[$i]/$itai[$i]<BR>\n";
            }
        }
        print "<BR>\n";
        print "<input type=\"hidden\" name=\"Command\" value=\"ITEMDEL\">\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\" ondblclick=\"dbk()\">\n";
    } elsif (($Command eq "ITMAIN") && ($Command4 eq "SEIRI")) { #�����ƥ�����
        $log = ($log . "�ǥ��ѥå�������������뤫��������<BR>") ;
        print "���Ȳ���Ż��ޤ�����<BR><BR>\n";
        print "��<select name=\"Command\">\n" ;
        print "��<option value=\"MAIN\" selected>�ߤ��</option>\n";
        for ($i=0; $i<5; $i++) {
            if ($item[$i] ne "�ʤ�") {
                ($in, $ik) = split(/<>/, $item[$i]);
                print "��<option value=\"SEIRI_$i\">$in/$eff[$i]/$itai[$i]</option>\n";
            }
        }
        print "</select><BR>\n" ;
        print "<BR>\n";
        print "��<select name=\"Command2\">\n" ;
        print "��<option value=\"MAIN\" selected>�ߤ��</option>\n";
        for ($i2=0; $i2<5; $i2++) {
            if ($item[$i2] ne "�ʤ�") {
                ($in2, $ik2) = split(/<>/, $item[$i2]);
                print "��<option value=\"SEIRI2_$i2\">$in2/$eff[$i2]/$itai[$i2]</option>\n";
            }
        }
        print "</select><BR>\n" ;
        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\" ondblclick=\"dbk()\">\n";
    } elsif (($Command eq "ITMAIN") && ($Command4 eq "BUNKATU")) { #�����ƥ�����
        $log = ($log . "�����ƥ��ʬ�䤹�뤫��������<BR>") ;
        print "����ʬ�䤷�ޤ�����<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>���<BR><BR>\n";
        for ($i=0; $i<5; $i++) {
            if ($item[$i] ne "�ʤ�") {
                ($in, $ik) = split(/<>/, $item[$i]);
                print "��<INPUT type=\"radio\" name=\"Command\" value=\"BUNKATU_$i\">$in/$eff[$i]/$itai[$i]<BR>\n";
            }
        }
        print "<BR>\n";
        print "��������ʬ���롩��<INPUT type=\"text\" name=\"Command2\"><BR>\n";
        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\" ondblclick=\"dbk()\">\n";
    } elsif (($Command eq "ITMAIN") && ($Command4 eq "GOUSEI")) { #�����ƥ����
        $log = ($log . "�����äƤ����Τ��Ȥ߹�碌�ơ��������ʤ����ʡ�<BR>") ;
        print "���Ȳ���������ޤ�����<BR><BR>\n";
        print "��<select name=\"Command\">\n" ;
        print "��<option value=\"MAIN\" selected>�ߤ��</option>\n";
        for ($i=0; $i<5; $i++) {
            if ($item[$i] ne "�ʤ�") {
                ($in, $ik) = split(/<>/, $item[$i]);
                print "��<option value=\"GOUSEI_$i\">$in/$eff[$i]/$itai[$i]</option>\n";
            }
        }
        print "</select><BR>\n" ;
        print "<BR>\n";
        print "��<select name=\"Command2\">\n" ;
        print "��<option value=\"MAIN\" selected>�ߤ��</option>\n";
        for ($i2=0; $i2<5; $i2++) {
            if ($item[$i2] ne "�ʤ�") {
                ($in2, $ik2) = split(/<>/, $item[$i2]);
                print "��<option value=\"GOUSEI2_$i2\">$in2/$eff[$i2]/$itai[$i2]</option>\n";
            }
        }
        print "</select><BR>\n" ;
        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\" ondblclick=\"dbk()\">\n";
    } elsif (($Command eq "ITMAIN") && ($Command4 eq "ITSEND")) { #�����ƥ����
        $log = ($log . "��֤˥����ƥ���Ϥ���������<BR>") ;
        print "ï���Ϥ��ޤ�����<BR><BR>\n";
        print "��<select name=\"Command\">\n" ;
        print "<option value=\"MAIN\" selected>�ߤ��</option>\n";
        for ($k=0; $k<=$#userlist; $k++) {
            ($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_group,$w_gpass,$w_a_name,$w_feel,$w_host,$w_os) = split(/,/, $userlist[$k]);
            if (($id ne $w_id) && ($gpass eq $w_gpass) && ($w_hit > 0)) {
                print "<option value=\"ITSEND_$w_id\_$k\">$w_f_name $w_l_name</option>\n";
            }
        }
        print "</select><BR>\n" ;
        print "<BR>\n";
        print "�����Ϥ��ޤ�����<BR><BR>\n";
        print "��<select name=\"Command2\">\n" ;
        print "<option value=\"MAIN\" selected>�ߤ��</option>\n";
        for ($i=0; $i<5; $i++) {
            if ($item[$i] ne "�ʤ�") {
                ($in, $ik) = split(/<>/, $item[$i]);
                print "<option value=\"ITSEND_$i\">$in/$eff[$i]/$itai[$i]</option>\n";
            }
        }
        print "</select><BR>\n" ;
        print "<BR>\n";
        print "��å����������Ϥ��Ƥ���������<BR><BR>\n";
        print "��<INPUT size=\"30\" type=\"text\" name=\"speech\" maxlength=\"64\"><BR><BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\" ondblclick=\"dbk()\">\n";
    } elsif (($Command eq "ITMAIN") && ($Command4 eq "WEPKAI")) {   #�������
        print "���򳰤��ޤ�����<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>���<BR><BR>\n";
        if ($wep ne "�Ǽ�<>WP") { #���������
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"WEPKAI2_W\">���򳰤�<BR>\n";
        }
        if ($bou ne "����<>DN") { #���ɶ�������
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"WEPKAI2_B\">���ɶ�򳰤�<BR>\n";
        }
        if ($bou_h ne "�ʤ�") { #Ƭ�ɶ�������
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"WEPKAI2_H\">Ƭ�ɶ�򳰤�<BR>\n";
        }
        if ($bou_a ne "�ʤ�") { #���ɶ�������
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"WEPKAI2_A\">���ɶ�򳰤�<BR>\n";
        }
        if ($bou_f ne "�ʤ�") { #­�ɶ�������
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"WEPKAI2_F\">­�ɶ�򳰤�<BR>\n";
        }
        if ($item[5] ne "�ʤ�") { #������������
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"WEPKAI2_I\">�����ʤ򳰤�<BR>\n";
        }
        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\" ondblclick=\"dbk()\">\n";
    } elsif (($Command eq "ITMAIN") && ($Command4 eq "WEPDEL")) {   #�������
        print "���򳰤��ޤ�����<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>���<BR><BR>\n";
        if ($wep ne "�Ǽ�<>WP") { #���������
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"WEPDEL2_W\">����ΤƤ�<BR>\n";
        }
        if ($bou ne "����<>DN") { #���ɶ�������
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"WEPDEL2_B\">���ɶ��ΤƤ�<BR>\n";
        }
        if ($bou_h ne "�ʤ�") { #Ƭ�ɶ�������
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"WEPDEL2_H\">Ƭ�ɶ��ΤƤ�<BR>\n";
        }
        if ($bou_a ne "�ʤ�") { #���ɶ�������
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"WEPDEL2_A\">���ɶ��ΤƤ�<BR>\n";
        }
        if ($bou_f ne "�ʤ�") { #­�ɶ�������
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"WEPDEL2_F\">­�ɶ��ΤƤ�<BR>\n";
        }
        if ($item[5] ne "�ʤ�") { #������������
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"WEPDEL2_I\">�����ʤ�ΤƤ�<BR>\n";
        }
        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\" ondblclick=\"dbk()\">\n";
    } elsif (($Command eq "SPECIAL") && ($Command6 eq "POISON")) {    #��ʪ����
        $log = ($log . "���������򺮤���С������դդա�<BR>") ;
        print "������ʪ�������ޤ�����<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>���<BR><BR>\n";
        for ($i=0; $i<5; $i++) {
            if ($item[$i] =~ /<>SH|<>HH|<>SD|<>HD/) {
                local($in, $ik) = split(/<>/, $item[$i]);
                print "��<INPUT type=\"radio\" name=\"Command\" value=\"POI_$i\">$in/$eff[$i]/$itai[$i]<BR>\n";
            }
        }
        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\" ondblclick=\"dbk()\">\n";
    } elsif (($Command eq "SPECIAL")&&($Command6 eq "ANTIPS")) {    #������
        $log = ($log . "�Ǥ����¤��Ƥߤ뤫��������<BR>") ;
        print "���������ºޤ���Ѥ��ޤ�����<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>���<BR><BR>\n";
        for ($i=0; $i<5; $i++) {
            if ($item[$i] =~ /<>SH|<>HH|<>SD|<>HD/) {
                local($in, $ik) = split(/<>/, $item[$i]);
                print "��<INPUT type=\"radio\" name=\"Command\" value=\"ATPS_$i\">$in/$eff[$i]/$itai[$i]<BR>\n";
            }
        }
        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\" ondblclick=\"dbk()\">\n";
    } elsif (($Command eq "SPECIAL") && ($Command6 eq "PSCHECK")) {   #�Ǹ�
        $log = ($log . "��������������Ƥ��ʤ���Ĵ�٤Ƥߤ褦��������<BR>") ;
        print "�����Ǹ��򤷤ޤ�����<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>���<BR><BR>\n";
        for ($i=0; $i<5; $i++) {
            if ($item[$i] =~ /<>SH|<>HH|<>SD|<>HD/) {
                local($in, $ik) = split(/<>/, $item[$i]);
                print "��<INPUT type=\"radio\" name=\"Command\" value=\"PSC_$i\">$in/$eff[$i]/$itai[$i]<BR>\n";
            }
        }
        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\" ondblclick=\"dbk()\">\n";
    } elsif (($Command eq "SPECIAL") && ($Command6 eq "HACK")) {  #�ϥå���
        $log = ($log . "�������������Ϥ̤���ʤ���ʡ�����<BR>\n") ;
        print "�ϥå��󥰳��ϡ�<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>���<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"HACK2\">����<BR><BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\" ondblclick=\"dbk()\">\n";
    } elsif (($Command eq "SPECIAL") && ($Command6 eq "SPIICH")) { #���ӥ��ԡ�������
        $log = ($log . "����Ƕ��٤С��ߤ�ʤ�ʹ������Ȧ���ʡ�����<BR>") ;
        print "�����������������ޤ���<BR>\n";
        print "�����ѣ���ʸ���ޤǡ�<BR><BR>\n";
        print "��<INPUT size=\"30\" type=\"text\" name=\"speech\"maxlength=\"50\"><BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"SPEAKER\">������<BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>�ߤ��<BR><BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\" ondblclick=\"dbk()\">\n";
    } elsif (($Command eq "SPECIAL") && ($Command6 eq "WINCHG")) {    #�����ѹ�
        $log = ($log . "���ʤ��ѹ����ޤ���<BR>") ;
        print "���ʤ����Ϥ��Ƥ�������<BR>\n";
        print "�����ѣ���ʸ���ޤǡ�<BR><BR>\n";
        print "��������<BR>\n";
        print "��<INPUT size=\"30\" type=\"text\" name=\"Message\" maxlength=\"64\" value=\"$msg\"><BR><BR>\n";
        print "�����<BR>\n";
        print "��<INPUT size=\"30\" type=\"text\" name=\"Message2\" maxlength=\"64\" value=\"$dmes\"><BR><BR>\n";
        print "��������ȡ�<BR>\n";
        print "��<INPUT size=\"30\" type=\"text\" name=\"Comment\" maxlength=\"64\" value=\"$com\"><BR><BR>\n";
        print "���Ρ�<BR>\n";
        print "��<INPUT size=\"16\" type=\"text\" name=\"A_Name\" maxlength=\"16\" value=\"$a_name\"><BR><BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\" ondblclick=\"dbk()\">\n";
    } elsif (($Command eq "SPECIAL") && ($Command6 eq "GRPCHG")) {    #�����ѹ�
        $log = ($log . "��°���롼�פ��ѹ����ޤ���<BR>") ;
        print "��°���륰�롼�פ����Ϥ��Ƥ�������<BR>\n";
        print "�����ѣ���ʸ���ޤǡ�<BR><BR>\n";
        print "���롼�ףɣġ�<font color=\"yellow\">�����ߥ�$group_sta����</b></font><br>\n";
        print "��<INPUT size=\"20\" type=\"text\" name=\"Group\" maxlength=\"20\" value=\"$group\"><BR><BR>\n";
        print "���롼�ץѥ���<BR>\n";
        print "��<INPUT size=\"20\" type=\"text\" name=\"Gpass\" maxlength=\"20\" value=\"$gpass\"><BR><BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\" ondblclick=\"dbk()\">\n";
    } elsif (($Command eq "SPECIAL") && ($Command6 eq "OUKYU")) { #���޽���
        $log = ($log . "����μ��Ť򤹤뤫��������<BR>") ;

        print "������Ť��ޤ�����<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>���<BR><BR>\n";

        if ($inf =~ /Ƭ/) { print "��<INPUT type=\"radio\" name=\"Command\" value=\"OUK_0\">Ƭ<BR>\n"; }
        if ($inf =~ /��/) { print "��<INPUT type=\"radio\" name=\"Command\" value=\"OUK_1\">��<BR>\n"; }
        if ($inf =~ /ʢ/) { print "��<INPUT type=\"radio\" name=\"Command\" value=\"OUK_2\">ʢ��<BR>\n"; }
        if ($inf =~ /­/) { print "��<INPUT type=\"radio\" name=\"Command\" value=\"OUK_3\">­<BR>\n"; }
        if ($inf =~ /��/) { print "��<INPUT type=\"radio\" name=\"Command\" value=\"OUK_4\">��<BR>\n"; }
        if ($inf =~ /��/) { print "��<INPUT type=\"radio\" name=\"Command\" value=\"OUK_5\">����<BR>\n"; }

        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\" ondblclick=\"dbk()\">\n";
    } elsif (($Command eq "SPECIAL") && ($Command6 eq "CATCHG")) { #���޽���
        $log = ($log . "ȿ����ˡ��ͤ��뤫��������<BR>") ;

        print "�ɤ���ä�ȿ�⤷�ޤ�����<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>���<BR><BR>\n";

        ($w_name,$w_kind) = split(/<>/, $wep);
        if ($w_kind =~ /B/) { print "��<INPUT type=\"radio\" name=\"Command\" value=\"CATCHG2_WB\">��($wb)<BR>\n"; }
        if ($w_kind =~ /P/) { print "��<INPUT type=\"radio\" name=\"Command\" value=\"CATCHG2_WP\">��($wp)<BR>\n"; }
        if (($w_kind =~ /G/) && ($wtai > 0)) { print "��<INPUT type=\"radio\" name=\"Command\" value=\"CATCHG2_WG\">��($wg)<BR>\n"; }
        if (($w_kind =~ /A/) && ($wtai > 0)) { print "��<INPUT type=\"radio\" name=\"Command\" value=\"CATCHG2_WA\">��($wa)<BR>\n"; }
        if ($w_kind =~ /N/) { print "��<INPUT type=\"radio\" name=\"Command\" value=\"CATCHG2_WN\">��($wn)<BR>\n"; }
        if ($w_kind =~ /S/) { print "��<INPUT type=\"radio\" name=\"Command\" value=\"CATCHG2_WS\">��($ws)<BR>\n"; }
        if ($w_kind =~ /C/) { print "��<INPUT type=\"radio\" name=\"Command\" value=\"CATCHG2_WC\">��($wc)<BR>\n"; }
        if ($w_kind =~ /D/) { print "��<INPUT type=\"radio\" name=\"Command\" value=\"CATCHG2_WD\">��($wd)<BR>\n"; }

        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\" ondblclick=\"dbk()\">\n";
    } elsif ($Command =~ /BATTLE0/) {   #��Ʈ���ޥ��
        local($a,$wid) = split(/_/, $Command);
        $log = ($log . "���ơ��ɤ����褦��������") ;
        print "���򤷤ޤ�����<BR>\n";
        print "<BR>����å�����<BR>\n";
        print "��<INPUT size=\"30\" type=\"text\" name=\"Dengon\" maxlength=\"64\"><BR><BR>\n";
        $chk = "checked" ;
        ($w_name,$w_kind) = split(/<>/, $wep);
        if ($w_kind =~ /B/) {print "��<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WB_$wid\" $chk>����($wb)<BR>\n"; $chk="" ;}
        if ($w_kind =~ /P/) {print "��<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WP_$wid\" $chk>����($wp)<BR>\n"; $chk="" ;}
        if (($w_kind =~ /G/) && ($wtai > 0)) {print "��<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WG_$wid\" $chk>���($wg)<BR>\n"; $chk="" ;}
        if (($w_kind =~ /A/) && ($wtai > 0)) {print "��<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WA_$wid\" $chk>�ͤ�($wa)<BR>\n"; $chk="" ;}
        if ($w_kind =~ /N/) {print "��<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WN_$wid\" $chk>�¤�($wn)<BR>\n"; $chk="" ;}
        if ($w_kind =~ /S/) {print "��<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WS_$wid\" $chk>�ɤ�($ws)<BR>\n"; $chk="" ;}
        if ($w_kind =~ /C/) {print "��<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WC_$wid\" $chk>�ꤲ��($wc)<BR>\n"; $chk="" ;}
        if ($w_kind =~ /D/) {print "��<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WD_$wid\" $chk>�ꤲ��($wd)<BR>\n"; $chk="" ;}
        if (($w_kind !~ /S|N|C|P|D|B/)&&(($w_kind =~ /G|A/) && ($wtai == 0))) {print "��<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WB_$wid\" $chk>����($wb)<BR>\n"; $chk="" ;}
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"RUNAWAY\">ƨ˴<BR>\n";
        print "<BR>\n";
        if($feel == 300) {print "��<INPUT type=\"checkbox\" name=\"Command2\" value=\"CATKon\">ɬ��������Ѥ���<BR><BR>\n";}
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\" ondblclick=\"dbk()\">\n";
    } elsif ($Command eq "BATTLE2") {   #�����ƥදå
        local($itno) = -1;
        for ($i=0; $i<5; $i++) {
            if ($item[$i] eq "�ʤ�") {
                $itno = $i ;
            }
        }
        print "����å���ޤ�����<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>���<BR><BR>\n";
        print "<INPUT TYPE=\"HIDDEN\" NAME=\"Itno\" VALUE=\"$itno\">\n";
        print "<INPUT TYPE=\"HIDDEN\" NAME=\"WId\" VALUE=\"$w_id\">\n";

        if ($w_wep !~ /�Ǽ�/) { #�������
            local($in, $ik) = split(/<>/, $w_wep);
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"GET_6\">$in/$w_watt/$w_wtai<BR>\n";
        }
        if ($w_bou !~ /����/) { #�ɶ�����
            local($in, $ik) = split(/<>/, $w_bou);
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"GET_7\">$in/$w_bdef/$w_btai<BR>\n";
        }
        if ($w_bou_h !~ /�ʤ�/) { #�ɶ�����
            local($in, $ik) = split(/<>/, $w_bou_h);
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"GET_8\">$in/$w_bdef_h/$w_btai_h<BR>\n";
        }
        if ($w_bou_f !~ /�ʤ�/) { #�ɶ�����
            local($in, $ik) = split(/<>/, $w_bou_f);
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"GET_9\">$in/$w_bdef_f/$w_btai_f<BR>\n";
        }
        if ($w_bou_a !~ /�ʤ�/) { #�ɶ�����
            local($in, $ik) = split(/<>/, $w_bou_a);
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"GET_10\">$in/$w_bdef_a/$w_btai_a<BR>\n";
        }

        for ($i=0; $i<6; $i++) {
            if ($w_item[$i] ne "�ʤ�") {
                local($in, $ik) = split(/<>/, $w_item[$i]);
                print "��<INPUT type=\"radio\" name=\"Command\" value=\"GET_$i]\">$in/$w_eff[$i]/$w_itai[$i]<BR>\n";
            }
        }
        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\" ondblclick=\"dbk()\">\n";
    } elsif ($Command eq "DEATHGET") {  #���Υ����ƥදå
        local($itno) = -1;
        for ($i=0; $i<5; $i++) {
            if ($item[$i] eq "�ʤ�") {
                $itno = $i ;
            }
        }
        print "����å���ޤ�����<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>���<BR><BR>\n";
        print "<INPUT TYPE=\"HIDDEN\" NAME=\"Itno\" VALUE=\"$itno\">\n";
        print "<INPUT TYPE=\"HIDDEN\" NAME=\"WId\" VALUE=\"$w_id\">\n";

        if ($w_wep !~ /�Ǽ�/) { #�������
            local($in, $ik) = split(/<>/, $w_wep);
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"GET_6\">$in/$w_watt/$w_wtai<BR>\n";
        }
        if ($w_bou !~ /����/) { #�ɶ�����
            local($in, $ik) = split(/<>/, $w_bou);
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"GET_7\">$in/$w_bdef/$w_btai<BR>\n";
        }
        if ($w_bou_h !~ /�ʤ�/) { #�ɶ�����
            local($in, $ik) = split(/<>/, $w_bou_h);
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"GET_8\">$in/$w_bdef_h/$w_btai_h<BR>\n";
        }
        if ($w_bou_f !~ /�ʤ�/) { #�ɶ�����
            local($in, $ik) = split(/<>/, $w_bou_f);
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"GET_9\">$in/$w_bdef_f/$w_btai_f<BR>\n";
        }
        if ($w_bou_a !~ /�ʤ�/) { #�ɶ�����
            local($in, $ik) = split(/<>/, $w_bou_a);
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"GET_10\">$in/$w_bdef_a/$w_btai_a<BR>\n";
        }

        for ($i=0; $i<6; $i++) {
            if ($w_item[$i] ne "�ʤ�") {
                local($in, $ik) = split(/<>/, $w_item[$i]);
                print "��<INPUT type=\"radio\" name=\"Command\" value=\"GET_$i\">$in/$w_eff[$i]/$w_itai[$i]<BR>\n";
            }
        }
        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\" ondblclick=\"dbk()\">\n";
    } else {
        print "����Ԥ��ޤ�����<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>���<BR><BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\" ondblclick=\"dbk()\">\n";
    }


}
#====================#
# �� �桼��������¸  #
#====================#
sub SAVE {


    open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);

    $chksts = "NG";
    for ($i=0; $i<$#userlist+1; $i++) {
        ($w_i,$w_p,$a) = split(/,/, $userlist[$i]);
        if (($id2 eq $w_i) && ($password2 eq $w_p)) {   #ID���ס�
            $chksts = "OK";$Index=$i;last;
        }
    }

    if ($chksts eq "OK") {
        if ($hit <= 0) { $sts = "��˴"; }
        $userlist[$Index] = "$id,$password,$f_name,$l_name,$sex,$cl,$no,$endtime,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg,$sts,$pls,$kill,$icon,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],,$dmes,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com,$inf,$group,$gpass,$a_name,$feel,$host,$os,\n" ;
        open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);
    }


}
#====================#
# �� Ũ������¸      #
#====================#
sub SAVE2 {


    open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);

    if ($w_hit <= 0) { $w_sts = "��˴"; }
    $userlist[$Index2] = "$w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_group,$w_gpass,$w_a_name,$w_feel,$w_host,$w_os,\n" ;

    open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);


}

#====================#
# �� ���å����ɹ�    #
#====================#
sub CREAD {
    local($xx, $name, $value);
    for $xx (split(/; */, $ENV{'HTTP_COOKIE'})) {
        if ($xx =~ /BR/){
            $cooks = $xx;
            $cooks =~ s/BR=//;
            $cooks =~ s/([0-9A-Fa-f][0-9A-Fa-f])/pack("C", hex($1))/eg;
            ($c_id,$c_password,$c_f_name,$c_l_name,$c_sex,$c_cl,$c_no,$c_endtime,$c_att,$c_def,$c_hit,$c_mhit,$c_level,$c_exp,$c_sta,$c_wep,$c_watt,$c_wtai,$c_bou,$c_bdef,$c_btai,$c_bou_h,$c_bdef_h,$c_btai_h,$c_bou_f,$c_bdef_f,$c_btai_f,$c_bou_a,$c_bdef_a,$c_btai_a,$c_tactics,$c_death,$c_msg,$c_sts,$c_pls,$c_kill,$c_icon,$c_item[0],$c_eff[0],$c_itai[0],$c_item[1],$c_eff[1],$c_itai[1],$c_item[2],$c_eff[2],$c_itai[2],$c_item[3],$c_eff[3],$c_itai[3],$c_item[4],$c_eff[4],$c_itai[4],$c_item[5],$c_eff[5],$c_itai[5],$c_log,$c_dmes,$c_bid,$c_club,$c_wn,$c_wp,$c_wa,$c_wg,$c_we,$c_wc,$c_wd,$c_wb,$c_wf,$c_ws,$c_com,$c_inf,$c_group,$c_gpass,$c_a_name,$c_feel,$c_host,$c_os) = split(/,/, $cooks);
        }
    }
}

#====================#
# �� ���å�����¸    #
#====================#
sub CSAVE {
    $cook = "$id,$password,$f_name,$l_name,$sex,$cl,$no,0,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg,$sts,$pls,$kill,$icon,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],,$dmes,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com,$inf,$group,$gpass,$a_name,$feel,$host,$os,";
    $cook =~ s/(.)/sprintf("%02X", unpack("C", $1))/eg;
    print "Set-Cookie: BR=$cook; expires=$expires\n";
}

#====================#
# �� ���å������    #
#====================#
sub CDELETE {
    $cook = ",,,,,,,$now,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,";
    $cook =~ s/(.)/sprintf("%02X", unpack("C", $1))/eg;
    print "Set-Cookie: BR=$cook; expires=$expires\n";
}

#====================#
# �� ��ά�׻�        #
#====================#
sub TACTGET {

    $chkpnt  = 6 ;   #Ũ�������ƥ�ȯ��Ψ
    $chkpnt2 = 5 ;  #��������Ψ
    $atp = 0.5 ;
    $dfp = 1.0 ;

    $atp += $ar/100;
    $atp += int($feel/3)/200;

    if ($tactics eq "����Ż�") {
        $atp+=0.4;
        $dfp-=0.4;
    } elsif ($tactics eq "�ɸ�Ż�") {
        $atp-=0.4;
        $dfp+=0.4;
    } elsif ($tactics eq "��̩��ư") {
        $dfp-=0.2;
        $dfp-=0.2;
        $chkpnt -=4;
        $chkpnt2+=4;
    } elsif ($tactics eq "õ����ư") {
        $atp-=0.2;
        $dfp-=0.2;
        $chkpnt +=4;
        $chkpnt2+=2;
    } elsif ($tactics eq "������ư") {
        $atp-=0.2;
        $dfp-=0.2;
        $chkpnt +=2;
        $chkpnt2+=4;
    } elsif ($tactics eq "̿��Ż�") {
        $afp-=0.4;
    } elsif ($tactics eq "����Ż�") {
        $dfp-=0.4;
    } elsif ($tactics eq "ϢƮ��ư") {
    }

    if ($arsts[$pls] eq "WU") { #������
        $atp+=0.2 ;
    } elsif ($arsts[$pls] eq "WD") {    #���⸺
        $atp-=0.2 ;
    } elsif ($arsts[$pls] eq "DU") {    #�ɸ���
        $dfp+=0.2 ;
    } elsif ($arsts[$pls] eq "DD") {    #�ɸ渺
        $dfp-=0.2 ;
    } elsif ($arsts[$pls] eq "SU") {    #ȯ����
        $chkpnt+=2 ;
    } elsif ($arsts[$pls] eq "SD") {    #ȯ����
        $chkpnt-=2 ;
    }

    if ($inf =~ /��/) { $atp -= 0.2; }
    if ($inf =~ /��/) { $atp += 0.2; $dfp-=0.2 ; }

    local($kind) = $w_kind;
    local($wmei) = 0;
    local($wweps) = "" ;

    if (($kind =~ /B/) || (($kind =~ /G|A/) && ($wtai == 0))) { #���� or ��̵���� or ��̵����
        $wweps = "S" ;
        $wmei = 80 ;
        $wmei += int($wb/$BASE);
    } elsif ($kind =~ /A/) {        #
        $wweps = "L" ;
        $wmei = 60 ;
        $wmei += int($wa/$BASE);
    }elsif ($kind =~ /C/) { #��
        $wweps = "L" ;
        $wmei = 70 ;
        $wmei += int($wc/$BASE);
    }elsif ($kind =~ /D/) { #��
        $wweps = "L" ;
        $wmei = 60 ;
        $wmei += int($wd/$BASE);
    }elsif ($kind =~ /G/) { #��
        $wweps = "L" ;
        $wmei = 50 ;
        $wmei += int($wg/$BASE);
    }elsif ($kind =~ /N/) { #��
        $wweps = "S" ;
        $wmei = 80 ;
        $wmei += int($wn/$BASE);
    }elsif ($kind  =~ /S/) {    #��
        $wweps = "S" ;
        $wmei = 80 ;
        $wmei += int($ws/$BASE);
    } else {    #��
        $wweps = "S" ;
        $wmei = 70 ;
        $wmei += int($wp/$BASE);
    }

    $weps = $wweps ;
    $mei = $wmei ;

    if ($inf =~ /Ƭ/) { $mei -= 20; }
    if ($inf =~ /��/) { $mei -= 10; }
    if ($w_inf =~ /��/) { $mei += 10; }

    if ($tactics eq "̿��Ż�") { $mei += 20; }
    if ($w_tactics eq "����Ż�") { $mei -= 20; }

    $mei += int((300 - $feel) / 30);

    if ($mei > 90) { $mei = 90; }
    if ($mei < 30) { $mei = 30; }

}
#====================#
# �� ��ά�׻�        #
#====================#
sub TACTGET2 {

    $atn = 0.5 ;
    $dfn = 1.0 ;
    $sen = 1.0 ;  # ��ȯ��Ψ�� �ݤʤ�գ�
    $sen2 = 1.0 ; # ������Ψ�� �ݤʤ�գ�

    $atn += $ar/100;
    $atn += int($w_feel/3)/200;

    if ($w_tactics eq "����Ż�") {
        $atn+=0.4 ;
        $dfn-=0.4 ;
    } elsif ($w_tactics eq "�ɸ�Ż�") {
        $atn-=0.4 ;
        $dfn+=0.4 ;
    } elsif ($w_tactics eq "��̩��ư") {
        $atn-=0.2 ;
        $dfn-=0.2 ;
        $sen+=0.4 ;
    } elsif ($w_tactics eq "õ����ư") {
        $atn-=0.2 ;
        $dfn-=0.2 ;
        $sen-=0.2 ;
    } elsif ($w_tactics eq "������ư") {
        $atn-=0.2 ;
        $dfn-=0.2 ;
        $sen-=0.2 ;
    } elsif ($w_tactics eq "̿��Ż�") {
        $afn-=0.4 ;
    } elsif ($w_tactics eq "����Ż�") {
        $dfn-=0.4 ;
    } elsif ($w_tactics eq "ϢƮ��ư") {
    }

    if ($arsts[$w_pls] eq "WU") {   #������
        $atn+=0.2 ;
    } elsif ($arsts[$w_pls] eq "WD") {  #���⸺
        $atn-=0.2 ;
    } elsif ($arsts[$w_pls] eq "DU") {  #�ɸ���
        $dfn+=0.2 ;
    } elsif ($arsts[$w_pls] eq "DD") {  #�ɸ渺
        $dfn-=0.2 ;
    }

    if ($w_inf =~ /��/) { $atn -= 0.2; }
    if ($w_inf =~ /��/) { $atn += 0.2; $dfn -= 0.2; }

    local($kind) = $w_kind2;
    local($wmei) = 0;
    local($wweps) = "" ;

    if (($kind =~ /B/) || (($kind =~ /G|A/) && ($w_wtai == 0))) { #���� or ��̵���� or ��̵����
        $wweps = "S" ;
        $wmei = 80 ;
        $wmei += int($wb/$BASE);
    } elsif ($kind =~ /A/) {        #
        $wweps = "L" ;
        $wmei = 60 ;
        $wmei += int($wa/$BASE);
    }elsif ($kind =~ /C/) { #��
        $wweps = "L" ;
        $wmei = 70 ;
        $wmei += int($wc/$BASE);
    }elsif ($kind =~ /D/) { #��
        $wweps = "L" ;
        $wmei = 60 ;
        $wmei += int($wd/$BASE);
    }elsif ($kind =~ /G/) { #��
        $wweps = "L" ;
        $wmei = 50 ;
        $wmei += int($wg/$BASE);
    }elsif ($kind =~ /N/) { #��
        $wweps = "S" ;
        $wmei = 80 ;
        $wmei += int($wn/$BASE);
    }elsif ($kind  =~ /S/) {    #��
        $wweps = "S" ;
        $wmei = 80 ;
        $wmei += int($ws/$BASE);
    } else {    #��
        $wweps = "S" ;
        $wmei = 70 ;
        $wmei += int($wp/$BASE);
    }

    $weps2 = $wweps ;
    $mei2 = $wmei ;

    if ($w_inf =~ /Ƭ/) { $mei2 -= 20; }
    if ($w_inf =~ /��/) { $mei2 -= 10; }
    if ($inf =~ /��/) { $mei2 += 10; }

    if ($w_tactics eq "̿��Ż�") { $mei2 += 20; }
    if ($tactics eq "����Ż�") { $mei2 -= 20; }

    $mei2 += int((300 - $w_feel) / 30);

    if ($mei2 > 90) { $mei2 = 90; }
    if ($mei2 < 30) { $mei2 = 30; }
}

#====================#
# �� �����ߥ��ڤ�    #
#====================#
sub DRAIN{
    local($d_mode) = $_[0];
    $log = ($log . "$l_name�ϡ������ߥʤ��Ԥ���������������HP������������<BR>") ;
    $sta = $maxsta ;
    local($dhit) = int(rand(($mhit/100)*20)+(($mhit/100)*10));
    if ($dhit <= 0) { $dhit = 1 ;}
    $mhit -= $dhit;
    if ($mhit <= 0) {
        $hit = $mhit = 0;
        $log = ($log . "<font color=\"red\"><b>$f_name $l_name��$cl $sex$no�֡ˤϻ�˴������</b></font><br>") ;
            &LOGSAVE("DEATH") ; #��˴��
            $mem--; if ($mem == 1) {&LOGSAVE("WINEND1") ;}
        if($d_mode eq "mov"){
            &SAVE;
        }elsif($d_mode eq "eve"){
            $Command = "EVENT";
        }
    } elsif ($hit > $mhit) { $hit = $mhit ; }
}

#====================#
# �� ���롼�װ���ɽ��#
#====================#
sub GrpMem {

    foreach (@userlist) {
        ($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_group,$w_gpass,$w_a_name,$w_feel,$w_host,$w_os) = split(/,/, $_);
        if ($id ne $w_id) {
            if (($group eq $w_group) && ($gpass eq $w_gpass)) {
                if ($w_hit > 0) {
                    $w_hpper = $w_hit/$w_mhit ;
                    if ($w_hpper < 0.2) { $w_hpper="<font color=\"red\">�λ�</font>"; }
                    elsif ($w_hpper < 0.5) { $w_hpper="<font color=\"orange\">�Ž�</font>"; }
                    elsif ($w_hpper < 0.8) { $w_hpper="<font color=\"yellow\">�ڽ�</font>"; }
                    else { $w_hpper="<font color=\"lime\">����</font>"; }
                } else {
                    $w_hpper="<font color=\"red\">��˴</font>";
                }
                push(@gr_list, "<b>$w_f_name $w_l_name $w_hpper</b><BR>\n");
            } elsif (($group eq $w_group) || ($gpass eq $w_gpass)) {
                if ($w_hit > 0) {
                    $w_hpper="<font color=\"lime\">��¸</font>";
                } else {
                    $w_hpper="<font color=\"red\">��˴</font>";
                }
                push(@gp_list, "$w_f_name $w_l_name $w_hpper<BR>\n");
            }
        }
    }
    print "@gr_list @gp_list\n";
}
1
